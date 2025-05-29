import json
import ast
import argparse
import os
import sys
import time
import logging
import tiktoken
import json5
import numpy as np
import pandas as pd
from tqdm import tqdm
from tenacity import (retry, stop_after_attempt, wait_random_exponential)
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from datetime import datetime
from collections import Counter
from contextlib import redirect_stdout

sys.stdout.reconfigure(encoding='utf-8')

# ----------------------------
# Global variables and logging
# ----------------------------
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
_LOG_ENABLED = True

_AUTH_SCOPE = "https://cognitiveservices.azure.com/.default"
_CREDENTIAL = DefaultAzureCredential()
total_llm_call = 0
total_tokens = 0

def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    if model_name == 'gpt-41':
        encoding_model = 'gpt-4o'
    else:
        encoding_model = model_name
    encoding = tiktoken.encoding_for_model(encoding_model)
    num_tokens = len(encoding.encode(string, disallowed_special=()))
    return num_tokens

def debug_print(*args, **kwargs):
    """Print debug information if _LOG_ENABLED is True."""
    if _LOG_ENABLED:
        message = ' '.join(str(arg) for arg in args)
        logging.debug(message)
        print(*args, **kwargs)

@retry(wait=wait_random_exponential(min=1, max=120), stop=stop_after_attempt(3))
def api_call(client, messages, model_name, json_enabled=True):
    global total_llm_call
    global total_tokens
    total_llm_call += 1
    total_tokens += num_tokens_from_string(str(messages), model_name)
    debug_print(RED + "==> Total LLM Calls: " + RESET, total_llm_call)
    debug_print(RED + "==> Total Tokens: " + RESET, total_tokens)

    # If using custom 'o3-mini' or other specialized series
    if model_name in ['o3-mini']:
        new_messages = []
        for message in messages:
            if message["role"] == "system":
                new_messages.append({"role": "developer", "content": [{"type": "text", "text": message["content"]}]})
            else:
                new_messages.append({"role": message["role"], "content": [{"type": "text", "text": message["content"]}]})
        
        return client.chat.completions.create(
            model=model_name,
            messages=new_messages,
            response_format={"type": "json_object"} if json_enabled else None,
            max_completion_tokens=100000
        )
    
    if model_name in ['gpt-41']:
        new_messages = []
        for message in messages:
            if message["role"] == "system":
                new_messages.append({"role": "system", "content": [{"type": "text", "text": message["content"]}]})
            else:
                new_messages.append({"role": message["role"], "content": [{"type": "text", "text": message["content"]}]})
        
        return client.chat.completions.create(
            model=model_name,
            messages=new_messages,
            temperature=0.01,
            response_format={"type": "json_object"} if json_enabled else None,
            max_completion_tokens=8196
        )


    # Otherwise for gpt-4 or other standard models
    if model_name == 'gpt-4-32k':
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.01,
            max_tokens=8192,
            top_p=0.9
        )
    if json_enabled:
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.01,
            response_format={"type": "json_object"},
            max_tokens=4096,
            top_p=0.9
        )
    else:
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.01,
            max_tokens=4096,
            top_p=0.9
        )


subject_weights = {
    "Disruption": 1.0,
    "Exfiltration": 1.0,
    "Access": 1.0,
    "Exploit": 1.0,
    "Tradecraft": 1.0,
    "Consumer": 0.8,
    "Informational": 0.4
}

subject_categories = {
    "Disruption": ["ransomware", "ddos", "defacement/spam"],
    "Exfiltration": ["rat", "info stealer"],
    "Access": ["phishing campaign", "brute force", "aitm", "supply chain", "backdoor", "cobalt strike"],
    "Exploit": ["CVEs"],
    "Tradecraft": ["threat actor updates", "new tooling", "new threat actors", "tooling updates", "tool overview"],
    "Consumer": ["crypto", "fraud", "video game related"],
    "Informational": ["trends", "vendor tool releases", "leak published", "policy update", "vulnerability fix"]
}

modifier_weights = {
    "If has_iocs": 1.2,
    "If no_iocs": 0.8,
    "If multiple_related_articles": 1.5,
    "If Exploit and CVSS >= 9": 1.2,
    "If Exploit and CVSS < 9": 0.5,
    "If threat actor/group/campaign mentioned": 1.5,
    "If is POC": 1.2,
    "If Exploit reported as active": 1.2,
    "If Exploit and multiple CVEs": 1.2,
    "If includes AI": 1.5
}
    
class Baseline:
    def __init__(self, client, model_name):
        self.client = client
        self.model_name = model_name

    def get_subject_category(self, article: str) -> str:
        try:
            system_prompt = """
            You are a cybersecurity expert. Your task is to determine the most appropriate Subject category from the following list:
            1. Disruption (includes: ransomware, ddos, defacement/spam)
            2. Exfiltration (includes: RAT, Info Stealer)
            3. Access (includes: phishing campaign, brute force, AITM, supply chain, backdoor, cobalt strike)
            4. Exploit (includes: CVEs)
            5. Tradecraft (includes: threat actor updates, new tooling, new threat actors, tooling updates, tool overview)
            6. Consumer (includes: crypto, fraud, video game related)
            7. Informational (The article should NOT include IoCs, and includes: trends, vendor tool releases, leak published, policy update, vulnerability fix)

            Output Format:
            - Return a JSON object with two keys: "answer" and "reason".
            - The "answer" key should contain only the most proper category name from the list (e.g., "Disruption", "Exfiltration", etc.)
            - The "reason" key should contain a brief explanation of why that category and the intermediate category (e.g., subject: Disruption, intermediate subject: ransomware) was chosen.
            """
            user_prompt = f"""
            Please analyze the following article and determine its Subject category:

            {article}
            """
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            result = api_call(self.client, messages, self.model_name, json_enabled=True)
            debug_print(RED + "==> Subject category raw result: " + RESET, result.choices[0].message.content)
            return result.choices[0].message.content
        except Exception as e:
            return None

    def get_modifiers(self, article: str) -> list:
        try:
            system_prompt = """
            You are a cybersecurity expert. Your task is to identify modifiers that you are 100% confident about based on clear evidence in the article.

            Available modifiers (only choose if you are 100% certain):
            1. "If has_iocs" (1.2) - ONLY if there are explicit, extractable IOCs in the article
            2. "If no_iocs" (0.8) - ONLY if you are certain there are no extractable IOCs
            3. "If multiple_related_articles" (1.5) - ONLY if multiple related articles are explicitly mentioned (NOT original source URL)
            4. "If Exploit and CVSS >= 9" (1.2) - ONLY if CVSS score >= 9 is explicitly stated
            5. "If Exploit and CVSS < 9" (0.5) - ONLY if CVSS score < 9 is explicitly stated
            6. "If threat actor/group/campaign mentioned" (1.5) - ONLY if a specific threat actor/group/campaign is explicitly named
            7. "If is POC" (1.2) - ONLY if the article explicitly states it's a proof of concept
            8. "If Exploit reported as active" (1.2) - ONLY if the article explicitly states the exploit is active
            9. "If Exploit and multiple CVEs" (1.2) - ONLY if multiple CVE numbers are explicitly listed
            10. "If includes AI" (1.5) - ONLY if AI-related information is explicitly mentioned

            Important Rules:
            - You MUST choose an answer from ["If has_iocs", "If no_iocs"]
            - Only choose modifiers you are 100% certain about
            - Each chosen modifier must have clear evidence in the article
            - Do not make assumptions or inferences
            - Use EXACTLY the modifier names as shown above

            Output Format:
            - Return a JSON object with two keys: "modifiers" and "reason"
            - The "modifiers" key should contain an array of modifier names you are 100% certain about
            - The "reason" key should contain a brief explanation with specific evidence from the article for each chosen modifier
            """
            user_prompt = f"""
            Please analyze the following article and identify modifiers you are 100% certain about based on clear evidence:

            {article}
            """
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            result = api_call(self.client, messages, self.model_name, json_enabled=True)
            debug_print(RED + "==> Modifiers raw result: " + RESET, result.choices[0].message.content)
            return result.choices[0].message.content
        except Exception as e:
            return None

    def calculate_priority_score(self, subject: str, modifiers: list) -> int:
        subject_weight = subject_weights.get(subject, 0) 

        # if subject == "Exploit":
        #     high_priority_modifiers = ["has_iocs", "exploit_active", "is_poc", "multiple_cves"]
        #    if any(mod in modifiers for mod in high_priority_modifiers):
        #        return 1 
        
        modifier_weight = 1.0
        for modifier in modifiers:
            if modifier in modifier_weights:
                modifier_weight *= modifier_weights[modifier]
        
        final_weight = subject_weight * modifier_weight
        print(f"==> Predicted subject weight: {subject_weight}")
        print(f"==> Predicted modifier weight: {modifier_weight}")
        print(f"==> Predicted final weight: {final_weight}")
        
        if final_weight >= 1.0:
            return 1
        elif final_weight >= 0.8:
            return 2
        elif final_weight >= 0.5:
            return 3
        else:
            return 4  

    def analyze_article_priority(self, article: str) -> int:
        for attempt in range(5):
            try:
                subject_result = self.get_subject_category(article)
                if not subject_result:
                    return 4
                subject_data = eval(subject_result)
                subject = subject_data['answer']
                print(f" ==> Predicted Subject category: {subject}")
                
                modifiers_result = self.get_modifiers(article)
                if not modifiers_result:
                    return 4
                modifiers_data = eval(modifiers_result)
                modifiers = modifiers_data['modifiers']
                print(f" ==> Predicted Modifiers: {modifiers}")
                
                score = self.calculate_priority_score(subject, modifiers)
                return score
                
            except Exception as e:
                print(f"Error encountered: {e}")
                if attempt < 5:
                    print(f"Retrying... Attempt {attempt + 2} of 5")
                    continue
                else:
                    print("Max retries reached. Returning default score.")
                    return 4

    def evaluate_subject_accuracy(self, data_dict, article_type):
        """Evaluate the accuracy of subject classification"""
        subject_true = []
        subject_pred = []
        subject_correct = 0
        total = 0
        
        print("\n====== Subject Category Evaluation ======")
        for data in tqdm(data_dict):
            if "Cassandra.SourceText" not in data or not data["Cassandra.SourceText"]:
                continue
                
            if article_type == 'article':
                if "Cassandra.SourceText" not in data or not data["Cassandra.SourceText"]:
                    continue
                article = data["Cassandra.SourceText"]
            elif article_type == 'description':
                article = data["System.Description"]
            subject_result = self.get_subject_category(article)
            
            if not subject_result:
                continue
                
            try:
                subject_data = eval(subject_result)
                predicted_subject = subject_data['answer']
                true_subject = data["subject"]
                
                subject_true.append(true_subject)
                subject_pred.append(predicted_subject)
                
                if predicted_subject == true_subject:
                    subject_correct += 1
                total += 1
                
                print(f"\nArticle ID: {data['id']}")
                print(f"True Subject: {true_subject}")
                print(f"Predicted Subject: {predicted_subject}")
                print(f"Correct: {predicted_subject == true_subject}")
                
            except Exception as e:
                print(f"Error processing article {data['id']}: {e}")
                continue
        
        if total > 0:
            accuracy = subject_correct / total
            print("\nSubject Classification Metrics:")
            print(f"Total Articles: {total}")
            print(f"Correct Predictions: {subject_correct}")
            print(f"Accuracy: {accuracy:.4f}")
            
            subject_categories = set(subject_true + subject_pred)
            for category in subject_categories:
                true_positives = sum(1 for t, p in zip(subject_true, subject_pred) if t == category and p == category)
                false_positives = sum(1 for t, p in zip(subject_true, subject_pred) if t != category and p == category)
                false_negatives = sum(1 for t, p in zip(subject_true, subject_pred) if t == category and p != category)
                
                precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
                recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
                f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
                
                print(f"\nCategory: {category}")
                print(f"Precision: {precision:.4f}")
                print(f"Recall: {recall:.4f}")
                print(f"F1 Score: {f1:.4f}")
        else:
            print("No valid articles found for evaluation")

    def gen_article_score_with_llms(self, data_dict, article_type):
        biases = []
        results = []
        y_true = []
        y_pred = []
        bias_dict = {1: [], 2: [], 3: [], 4: []}

        for data in tqdm(data_dict):
            print("="*60)
            print(f"Data ID {data['id']}")
            
            if article_type == 'article':
                if "Cassandra.SourceText" not in data or not data["Cassandra.SourceText"]:
                    continue
                article = data["Cassandra.SourceText"]
            elif article_type == 'description':
                article = data["System.Description"]
                
            result = self.analyze_article_priority(article)
            if result == 0:
                result = 4
                
            results.append({
                "id": data["id"],
                "score": data["priority"],
                "llm_result": result
            })
            
            bias = int(abs(result - data["priority"]))
            y_true.append(data["priority"])
            y_pred.append(result)
            biases.append(bias)
            
            print(f"==> Ground truth subject: {data["subject"]}")
            print(f"==> Ground truth intermediate subject: {data["intermediate_subject"]}")
            print(f"==> Ground truth subject weight: {data["subject_weight"]}")
            print(f"==> Ground truth modifier: {data["modifier"]}")
            print(f"==> Ground truth modifier weight: {data["modifier_weight"]}")
            print(f"==> Ground truth priority weight: {data["priority_weight"]}")
            print(f"==> Ground truth score: {data['score']}")
            print(f"==> Predicted score: {result}")
            print("="*30)
            print(f"==> Correct: {data['score'] == result}")
            print(f"==> Bias: {bias}")

            if data["priority"] in bias_dict:
                bias_dict[data["priority"]].append(bias)

        overall_bias = round(np.mean(biases), 4) if biases else 0

        avg_bias_per_class = {}
        for score, biases_list in bias_dict.items():
            if biases_list:
                avg_bias_per_class[score] = round(np.mean(biases_list), 4)
            else:
                avg_bias_per_class[score] = 0

        accuracy = accuracy_score(y_true, y_pred)

        cm = confusion_matrix(y_true, y_pred)
        report = classification_report(y_true, y_pred, zero_division=0, digits=3)
        
        print("\n====== Evaluation Metrics ======")
        print(f"Overall Accuracy: {accuracy:.4f}")
        print(f"Overall Bias: {overall_bias:4f}")
 
        print("\nConfusion Matrix:")
        print(cm)
        print("\nClassification Report:")
        print(report)

        matrix = np.array(cm)
        accept_matrix = matrix[0:3, 0:3]
        reject_matrix = matrix[3]

        accept_true_positives = np.sum(accept_matrix)
        accept_total = np.sum(matrix[0:3, :])
        accept_correct_rate = accept_true_positives / accept_total if accept_total else 0

        reject_true_positives = reject_matrix[3]
        reject_total = np.sum(reject_matrix)
        reject_correct_rate = reject_true_positives / reject_total if reject_total else 0

        print(f"Accept Category - Correct: {accept_true_positives}, Total: {accept_total}, Correct Rate: {accept_correct_rate:.4f}")
        print(f"Reject Category - Correct: {reject_true_positives}, Total: {reject_total}, Correct Rate: {reject_correct_rate:.4f}")
        
        TP = np.sum(accept_matrix)
        FN = np.sum(matrix[0:3, :]) - TP
        TN = matrix[3][3]
        FP = sum(reject_matrix) - TN

        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0
        accuracy = (TP + TN) / (TP + FP + FN + TN) if (TP + FP + FN + TN) > 0 else 0

        print(f"Accept Category - Precision: {precision:.4f}, Recall: {recall:.4f}")
        print(f"Accept Category - Accuracy: {accuracy:.4f}")

        print("\n====== Ground Truth Accept Group Metrics ======")
        accept_matrix_total = matrix[0:3, :]
        acc = np.trace(accept_matrix_total)
        accuracy_accept = acc / np.sum(accept_matrix_total) if np.sum(accept_matrix_total) > 0 else 0
        print(f"Overall Accuracy (Accept Group): {accuracy_accept:.4f}")

        total_bias = 0
        total_count = 0

        for true_index, true_val in enumerate([1, 2, 3]):
            for pred_index, pred_val in enumerate([1, 2, 3, 4]):
                bias = abs(true_val - pred_val)
                count = accept_matrix_total[true_index, pred_index]
                total_bias += bias * count
                total_count += count

        avg_bias_accept = total_bias / total_count if total_count != 0 else 0
        print(f"Average Bias (Accept Group): {avg_bias_accept:.4f}")

        combined_metrics = {
            "overall_accuracy": accuracy,
            "overall_bias": overall_bias,
            "confusion_matrix": cm,
            "classification_report": report,
            "avg_bias_per_class": avg_bias_per_class,
            "binary": {
                "accept_correct": accept_correct_rate,
                "reject_correct": reject_correct_rate,
                "accept_accuracy": accuracy_accept,
                "accept_avg_bias": avg_bias_accept
            }
        }
        return results, combined_metrics

def main():
    parser = argparse.ArgumentParser(description="Run an LLM model for priority scoring")
    parser.add_argument("-model", type=str, required=True, help="Model name to run (e.g., gpt-4o, o3-mini, etc.)")
    parser.add_argument("-method", type=str, required=True, choices=["baseline"],
                        help="Method to use (baseline uses gen_article_score_with_llms)")
    parser.add_argument("-input_dataset", type=str, required=True, help="Input dataset to run")
    parser.add_argument("-dataset", type=str, required=True, choices=["article", "description"],
                    help="Dataset to use: 'article' (for gen_article_score_with_llms) or 'description' (for gen_score_with_llms)")
    args = parser.parse_args()

    model_name = args.model
    method_name = args.method
    dataset_choice = args.dataset
    data_file = args.input_dataset

    # Setup the AzureOpenAI client based on the model name
    if model_name in ['gpt-4o-mini', 'gpt-4o', 'o3-mini', 'gpt-41']:
        client = AzureOpenAI(
            azure_endpoint="https://onetiai-swec.openai.azure.com/",
            azure_ad_token_provider=get_bearer_token_provider(_CREDENTIAL, _AUTH_SCOPE),
            api_version="2024-12-01-preview",
        )
    elif model_name in ['gpt-4o-2024-08-06-ti_prune2_1030', 'gpt-4o-mini-2024-07-18-model_1_datasets_v01_no_sa_all_csf']:
        client = AzureOpenAI(
            azure_endpoint="https://yingqiliu-secphi-aoai.openai.azure.com/",
            azure_ad_token_provider=get_bearer_token_provider(_CREDENTIAL, _AUTH_SCOPE),
            api_version="2024-12-01-preview",
        )
    else:
        raise ValueError("Unsupported model")
    
    current_date = datetime.today().strftime('%Y-%m-%d')

    log_dir = os.path.join("triage_latest", current_date, dataset_choice)
    os.makedirs(log_dir, exist_ok=True)
    log_filename = os.path.join(log_dir, f"{model_name}_{method_name}_{dataset_choice}.log")

    # Load data from the appropriate file
    with open(data_file, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)

    time_start = time.time()
    subject_log_filename = os.path.join(log_dir, f"{model_name}_{method_name}_{dataset_choice}_subject.log")

    with open(subject_log_filename, 'w', encoding='utf-8') as log_f:
        with redirect_stdout(log_f):
            print(f"Running {method_name} with dataset {dataset_choice}")
            # Create the appropriate method instance and run evaluation.
            if method_name == "baseline":
                baseline = Baseline(client, model_name)
                if dataset_choice == "article":
                    baseline.evaluate_subject_accuracy(data_dict, article_type='article')
                else:
                    baseline.evaluate_subject_accuracy(data_dict, article_type='description')
            else:
                raise ValueError("Invalid method option provided.")
            time_end = time.time()
            print(f"==> Total time taken for {method_name} in {dataset_choice}: {time_end - time_start:.2f} seconds")
            print(f"Log saved to: {log_filename}")

    
    with open(log_filename, 'w', encoding='utf-8') as log_f:
        with redirect_stdout(log_f):
            print(f"Running {method_name} with dataset {dataset_choice}")
            # Create the appropriate method instance and run evaluation.
            if method_name == "baseline":
                baseline = Baseline(client, model_name)
                if dataset_choice == "article":
                    baseline.gen_article_score_with_llms(data_dict, article_type='article')
                else:
                    baseline.gen_article_score_with_llms(data_dict, article_type='description')
            else:
                raise ValueError("Invalid method option provided.")
            time_end = time.time()
            print(f"==> Total time taken for {method_name} in {dataset_choice}: {time_end - time_start:.2f} seconds")
            print(f"Log saved to: {log_filename}")
    
    # Also print a message on the console.
    print(f"Results for dataset '{data_file}' using model '{model_name}' and method '{method_name}' have been saved to {log_filename}")


if __name__ == '__main__':
    main()
