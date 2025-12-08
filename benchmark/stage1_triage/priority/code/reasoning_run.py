"""
This file is used for some example methods of stage 1 triage.
"""

import sys
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

total_llm_call = 0
total_tokens = 0

def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string, disallowed_special=()))
    return num_tokens

def debug_print(*args, **kwargs):
    """Print debug information if _LOG_ENABLED is True."""
    if _LOG_ENABLED:
        message = ' '.join(str(arg) for arg in args)
        logging.debug(message)
        print(*args, **kwargs)

@retry(wait=wait_random_exponential(min=1, max=120), stop=stop_after_attempt(10))
def api_call(client, messages, model_name, json_enabled=True):
    """
    Generic API call wrapper with retry logic. 
    This remains outside the Baseline class to allow easy reuse.
    """
    global total_llm_call
    global total_tokens
    total_llm_call += 1
    total_tokens += num_tokens_from_string(str(messages), model_name)
    debug_print(RED + "==> Total LLM Calls: " + RESET, total_llm_call)
    debug_print(RED + "==> Total Tokens: " + RESET, total_tokens)

    # If using custom 'o3-mini' or other specialized series
    if model_name == 'o3-mini':
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


def get_target_candidate_list(priority_mapping, key):
    if key not in priority_mapping:
        return []
    
    score_mapping = priority_mapping[key]
    debug_print(f"=> target candidates: {score_mapping}")
    return [k for k, v in score_mapping.items() if v != 5]

priority_mapping = {
    "Defacement / Spam": {
        "Unknown/NA": 5, "Singular System": 3, "Singular Company": 3,
        "Singular Country": 3, "Multiple Countries": 3, "Industry/Sector": 3,
        "Platform/Service": 3, "Drive-by": 3, "ICS": 1
    },
    "Mobile Malware": {
        "Unknown/NA": 3, "Singular System": 3, "Singular Company": 3,
        "Singular Country": 3, "Multiple Countries": 3, "Industry/Sector": 3,
        "Platform/Service": 3, "Drive-by": 3, "ICS": 5
    },
    "Malware Updates": {
        "Unknown/NA": 2, "Singular System": 3, "Singular Company": 3,
        "Singular Country": 3, "Multiple Countries": 2, "Industry/Sector": 2,
        "Platform/Service": 2, "Drive-by": 2, "ICS": 1
    },
    "New Malware": {
        "Unknown/NA": 3, "Singular System": 3, "Singular Company": 3,
        "Singular Country": 3, "Multiple Countries": 2, "Industry/Sector": 2,
        "Platform/Service": 2, "Drive-by": 2, "ICS": 1
    },
    "Vulnerability Exploitation (CVE < 9)": {
        "Unknown/NA": 5, "Singular System": 2, "Singular Company": 2,
        "Singular Country": 5, "Multiple Countries": 5, "Industry/Sector": 5,
        "Platform/Service": 2, "Drive-by": 5, "ICS": 1
    },
    "Cryptominer / Resource Hijacking": {
        "Unknown/NA": 3, "Singular System": 3, "Singular Company": 3,
        "Singular Country": 3, "Multiple Countries": 3, "Industry/Sector": 3,
        "Platform/Service": 2, "Drive-by": 3, "ICS": 1
    },
    "Phishing Campaign": {
        "Unknown/NA": 2, "Singular System": 2, "Singular Company": 2,
        "Singular Country": 1, "Multiple Countries": 1, "Industry/Sector": 1,
        "Platform/Service": 1, "Drive-by": 2, "ICS": 1
    },
    "0-Day Vulnerability Exploitation": {
        "Unknown/NA": 5, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 5, "Multiple Countries": 5, "Industry/Sector": 5,
        "Platform/Service": 1, "Drive-by": 5, "ICS": 1
    },
    "Vulnerability Exploitation (CVE ≥ 9)": {
        "Unknown/NA": 5, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 5, "Multiple Countries": 5, "Industry/Sector": 5,
        "Platform/Service": 1, "Drive-by": 5, "ICS": 1
    },
    "APT / Threat Actor Activity": {
        "Unknown/NA": 1, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 1, "Multiple Countries": 1, "Industry/Sector": 1,
        "Platform/Service": 1, "Drive-by": 1, "ICS": 1
    },
    "Persistent Backdoor / C2": {
        "Unknown/NA": 1, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 1, "Multiple Countries": 1, "Industry/Sector": 1,
        "Platform/Service": 1, "Drive-by": 1, "ICS": 1
    },
    "Data Exfiltration": {
        "Unknown/NA": 1, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 1, "Multiple Countries": 1, "Industry/Sector": 1,
        "Platform/Service": 1, "Drive-by": 1, "ICS": 1
    },
    "Ransomware": {
        "Unknown/NA": 1, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 1, "Multiple Countries": 1, "Industry/Sector": 1,
        "Platform/Service": 1, "Drive-by": 1, "ICS": 1
    }
}
    
class Baseline:
    def __init__(self, client, model_name):
        """
        :param client: The AzureOpenAI client instance
        :param model_name: The model name (e.g., 'gpt-4-32k', 'o3-mini', etc.)
        """
        self.client = client
        self.model_name = model_name

    def get_subject_matter_category(self, article: str) -> str:
        try:
            system_prompt = """
            You are a cybersecurity analyst. Your task is to determine the most appropriate Subject Matter category from the following list:
            1. Defacement / Spam
            2. Mobile Malware
            3. Malware Updates
            4. New Malware
            5. Vulnerability Exploitation (CVE < 9)
            6. Cryptominer / Resource Hijacking
            7. Phishing Campaign
            8. 0-Day Vulnerability Exploitation
            9. Vulnerability Exploitation (CVE ≥ 9)
            10. APT / Threat Actor Activity
            11. Persistent Backdoor / C2
            12. Data Exfiltration
            13. Ransomware
            14. Others

            Output Format:
            - Return a JSON object with two keys: "answer" and "reason".
            - The "answer" key should contain only the category name from the list (e.g., "Vulnerability Exploitation (CVE < 9)", "Defacement / Spam", etc.), and no extra text, prefixes, explanations are allowed.           
            - The "reason" key should contain a brief explanation of why that category was chosen.
            - If multiple categories apply, return the one with the highest confidence.
            - If no category applies, return "None" in the "answer" key.
            """
            user_prompt = f"""
            Please analyze the following article and determine its Subject Matter category:

            {article}
            """
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            result = api_call(self.client, messages, self.model_name, json_enabled=True)
            debug_print(RED + "==> Subject Matter raw result: " + RESET, result.choices[0].message.content)
            return result.choices[0].message.content
        except Exception as e:
            return None


    def get_targeting_category(self, subject, article: str) -> str:
        try:
            print("====== Generating target candidates ======")
            target_candidates = get_target_candidate_list(priority_mapping, subject)
            target_candidates.append("Others")
            print(f"=> Target candidates: {target_candidates}")
            system_prompt = f"""
            You are a cybersecurity analyst. Your task is to determine the most appropriate Targeting category from the following list:
            {target_candidates}

            Output Format:
            - Return a JSON object with two keys: "answer" and "reason".
            - The "answer" key should contain only the category name from the list (e.g., "Singular System", "Platform/Service", etc.), and no extra text, prefixes, explanations are allowed.
            - Do NOT return names that not included in the list (e.g., "Singular Platform/Service").
            - The "reason" key should contain a brief explanation of why that category was chosen.
            - Return only the category name from the list, (e.g., Platform/Service, Singular System), no explanations or additional text
            - If multiple categories apply, return the one with highest confidence
            - If no category applies, return 'None' without any additional text or explanations in the "answer" key.
            """
            user_prompt = f"""
            Please analyze the following article and determine its Targeting category:

            {article}
            """
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            result = api_call(self.client, messages, self.model_name, json_enabled=True)
            debug_print(RED + "==> Targeting raw result: " + RESET, result.choices[0].message.content)
            return result.choices[0].message.content
        except Exception as e:
            return None

    def get_priority_score(self, subject_matter: str, targeting: str, priority_mapping) -> int:
        """
        Return the priority score based on subject_matter and targeting categories.
        """
        return priority_mapping.get(subject_matter, {}).get(targeting, 0)

    def analyze_article_priority(self, article: str) -> int:
        for attempt in range(5):
            try:
                if not self.get_subject_matter_category(article):
                    return 5
                subject_matter = eval(self.get_subject_matter_category(article))
                subject_matter = subject_matter['answer']
                print(f" => Subject matter: {subject_matter}")
                if subject_matter == 'Others' or not subject_matter or 'None' in subject_matter:
                    return 5
                elif subject_matter in ["APT / Threat Actor Activity", "Persistent Backdoor / C2", "Data Exfiltration", "Ransomware"]:
                    return 1
                print(f"====== Processing target ======")
                if not self.get_targeting_category(subject_matter, article):
                    return 5
                targeting = eval(self.get_targeting_category(subject_matter, article))
                targeting = targeting['answer']
                print(f" => Target matter: {targeting}")
                if subject_matter == 'Others':
                    return 5
                
                if not targeting or 'None' in targeting:
                    targeting = "Unknown/NA"
                
                score = self.get_priority_score(subject_matter, targeting, priority_mapping)
                return score
            except Exception as e:
                print(f"Error encountered: {e}")
                if attempt < 5:  # If it's not the last attempt, retry
                    print(f"Retrying... Attempt {attempt + 2} of 5")
                    continue
                else:
                    print("Max retries reached. Returning default score.")
                    return 5

    def gen_article_score_with_llms(self, data_dict, article_type):
        biases = []
        results = []
        y_true = []
        y_pred = []
        bias_dict = {1: [], 2: [], 3: [], 5: []}

        for data in tqdm(data_dict):
            print("="*60)
            print(f"Data ID {data['id']}")
            # if data['score'] == 4 or data["priority"] is None:
                # continue
            if article_type == 'article':
                if "Cassandra.SourceText" not in data or not data["Cassandra.SourceText"]:
                    continue
                article = data["Cassandra.SourceText"]
            elif article_type == 'description':
                article = data["System.Description"]
            result = self.analyze_article_priority(article)
            if result == 0:
                result = 5
            results.append({
                "id": data["id"],
                "score": data["score"],
                "llm_result": result
            })
            bias = int(abs(result - data["score"]))
            y_true.append(data["score"])
            y_pred.append(result)
            biases.append(bias)
            print(f"==> Ground truth score: {data['score']}")
            print(f"==> Predicted score: {result}")
            print(f"==> Correct: {data['score'] == result}")
            print(f"==> Bias: {bias}")

            if data["score"] in bias_dict:
                bias_dict[data["score"]].append(bias)

        overall_bias = round(np.mean(biases), 4) if biases else 0

        avg_bias_per_class = {}
        for score, biases_list in bias_dict.items():
            if biases_list:
                avg_bias_per_class[score] = round(np.mean(biases_list), 4)
            else:
                avg_bias_per_class[score] = 0

        accuracy = accuracy_score(y_true, y_pred)
        precision_macro = precision_score(y_true, y_pred, average='macro', zero_division=0)
        recall_macro = recall_score(y_true, y_pred, average='macro', zero_division=0)
        f1_macro = f1_score(y_true, y_pred, average='macro', zero_division=0)
        cm = confusion_matrix(y_true, y_pred)
        report = classification_report(y_true, y_pred, zero_division=0, digits=3)
        print("\n====== Evaluation Metrics ======")
        print(f"Overall Accuracy: {accuracy:.4f}")
        print(f"Overall Bias: {overall_bias:4f}")
        print(f"Overall Precision (macro): {precision_macro:.4f}")
        print(f"Overall Recall (macro): {recall_macro:.4f}")
        print(f"Overall F1 Score (macro): {f1_macro:.4f}")
        print("\nConfusion Matrix:")
        print(cm)
        print("\nClassification Report:")
        print(report)

        matrix = np.array(cm)

        accept_matrix = matrix[0:3, 0:3]  # submatrix for accept (first 3 rows and first 3 columns)
        # Reject category: 4th row (for score 5)
        reject_matrix = matrix[3]  # 4th row

        # Calculate correctness rates:
        # Accept: True positives = diagonal sum of accept submatrix
        accept_true_positives = np.sum(accept_matrix)
        # Total number of elements in the first 3 rows
        accept_total = np.sum(matrix[0:3, :])
        accept_correct_rate = accept_true_positives / accept_total if accept_total else 0

        # Reject: True positive is the (4,4) element (last element in the 4th row)
        reject_true_positives = reject_matrix[3]
        # Total number of elements in the 4th row
        reject_total = np.sum(reject_matrix)
        reject_correct_rate = reject_true_positives / reject_total if reject_total else 0

        print(f"Accept Category - Correct: {accept_true_positives}, Total: {accept_total}, Correct Rate: {accept_correct_rate:.4f}")
        print(f"Reject Category - Correct: {reject_true_positives}, Total: {reject_total}, Correct Rate: {reject_correct_rate:.4f}")
        TP = np.sum(accept_matrix)
        FN = np.sum(matrix[0:3, :]) - TP
        TN = matrix[3][3]
        FP = sum(reject_matrix) - TN

        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        accuracy = (TP + FN) / (TP + FP + FN + TN)

        print(f"Accept Category - Precision: {precision:.4f}, Recall: {recall:.4f}")
        print(f"Accept Category - Accuracy: {accuracy:.4f}")


        print("\n====== Ground Truth Accept Group Metrics ======")
        accept_matrix_total = matrix[0:3, :]
        acc = np.trace(accept_matrix_total)
        accuracy_accept = acc / np.sum(accept_matrix_total)  # Accuracy for accept group
        print(f"Overall Accuracy (Accept Group): {accuracy_accept:.4f}")

        total_bias = 0  # Total bias sum
        total_count = 0  # Total number of elements considered for bias calculation
 

        for true_index, true_val in enumerate([1, 2, 3]):  # Ground truth values (1, 2, 3)
            for pred_index, pred_val in enumerate([1, 2, 3, 5]):  # Predicted values (1, 2, 3, 5)
                # Calculate bias: absolute difference between ground truth and prediction
                bias = abs(true_val - pred_val)
                # Count is the number of occurrences in the matrix (matrix element at [true_index, pred_index])
                count = accept_matrix_total[true_index, pred_index]
                
                # Update total bias and total count
                total_bias += bias * count
                total_count += count

        # Calculate Average Bias for Accept Group
        avg_bias_accept = total_bias / total_count if total_count != 0 else 0  # Avoid division by zero
        print(f"Average Bias (Accept Group):     {avg_bias_accept:.4f}")

        combined_metrics = {
            "overall_accuracy": accuracy,
            "overall_bias": overall_bias,
            "precision_macro": precision_macro,
            "recall_macro": recall_macro,
            "f1_macro": f1_macro,
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

 
class Method1:
    def __init__(self, client, model_name):
        self.client = client
        self.model_name = model_name

    def get_subject_matter_category(self, article: str) -> str:
        try:
            system_prompt = """
            ### Task Description
            You are a top-notch cybersecurity analyst. You will be given an article about a threat incident. Your task is to think step-by-step to determine the most appropriate Subject Matter category from the following list:
            1. Defacement / Spam
            2. Mobile Malware
            3. Malware Updates
            4. New Malware
            5. Vulnerability Exploitation (CVE < 9)
            6. Cryptominer / Resource Hijacking
            7. Phishing Campaign
            8. 0-Day Vulnerability Exploitation
            9. Vulnerability Exploitation (CVE ≥ 9)
            10. APT / Threat Actor Activity
            11. Persistent Backdoor / C2
            12. Data Exfiltration
            13. Ransomware
            14. Others

            ### Instruction
            - First, analyze the article and identify key information related to cybersecurity incidents
            - Then, determine which category the identified information best fits into

            ### Output Format:
            - Return a JSON object with two keys: "answer" and "reason".
            - The "answer" key should contain only the category name from the list (e.g., "Vulnerability Exploitation (CVE < 9)", "Defacement / Spam", etc.), and no extra text, prefixes, explanations are allowed.
            - The "reason" key should contain a brief explanation of why that category was chosen.
            - If multiple categories apply, return the one with the highest confidence.
            - If no category applies, return "None" in the "answer" key.
            """
            user_prompt = f"""
            Please analyze the following article and determine its Subject Matter category:

            {article}
            """
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            result = api_call(self.client, messages, self.model_name, json_enabled=True)
            debug_print(RED + "==> Subject Matter raw result: " + RESET, result.choices[0].message.content)
            return result.choices[0].message.content.strip()
        except Exception as e:
            return None

    def get_targeting_category(self, subject, article: str) -> str:
        try:
            print("====== Generating target candidates ======")
            target_candidates = get_target_candidate_list(priority_mapping, subject)
            target_candidates.append("Others")
            print(f"=> Target candidates: {target_candidates}")
            system_prompt = f"""
            You are a cybersecurity analyst. Your task is to determine the most appropriate Targeting category from the following list:
            {target_candidates}


            ### Instruction
            - First, analyze the article and identify key information related to cybersecurity incidents
            - Then, determine which category the identified information best fits into

            ### Output Format
            - Return a JSON object with two keys: "answer" and "reason".
            - The "answer" key should contain only the category name from the list (e.g., "Singular System", "Platform/Service", etc.), and no extra text, prefixes, explanations are allowed.
            - Do NOT return names that not included in the list (e.g., "Singular Platform/Service").
            - The "reason" key should contain a brief explanation of why that category was chosen.
            - Return only the category name from the list, (e.g., Platform/Service, Singular System), no explanations or additional text
            - If multiple categories apply, return the one with highest confidence
            - If no category applies, return 'None' without any additional text or explanations in the "answer" key.
            """
            user_prompt = f"""
            Please analyze the following article and determine its Targeting category:

            {article}
            """
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            result = api_call(self.client, messages, self.model_name, json_enabled=True)
            debug_print(RED + "==> Targeting raw result: " + RESET, result.choices[0].message.content)
            return result.choices[0].message.content.strip()
        except Exception as e:
            return None

    def get_priority_score(self, subject_matter: str, targeting: str, priority_mapping) -> int:
        """
        Return the priority score based on subject_matter and targeting categories.
        """
        return priority_mapping.get(subject_matter, {}).get(targeting, 0)

    def analyze_article_priority(self, article: str) -> int:
        for attempt in range(5):
            try:
                if not self.get_subject_matter_category(article):
                    return 5
                subject_matter = eval(self.get_subject_matter_category(article))
                subject_matter = subject_matter['answer']
                print(f" => Subject matter: {subject_matter}")
                if subject_matter == 'Others' or not subject_matter or 'None' in subject_matter:
                    return 5
                elif subject_matter in ["APT / Threat Actor Activity", "Persistent Backdoor / C2", "Data Exfiltration", "Ransomware"]:
                    return 1
                print(f"====== Processing target ======")
                if not self.get_targeting_category(subject_matter, article):
                    return 5
                targeting = eval(self.get_targeting_category(subject_matter, article))
                targeting = targeting['answer']
                print(f" => Target matter: {targeting}")
                if subject_matter == 'Others':
                    return 5
                
                if not targeting or 'None' in targeting:
                    targeting = "Unknown/NA"
                
                score = self.get_priority_score(subject_matter, targeting, priority_mapping)
                return score
            except Exception as e:
                print(f"Error encountered: {e}")
                if attempt < 5:  # If it's not the last attempt, retry
                    print(f"Retrying... Attempt {attempt + 2} of 5")
                    continue
                else:
                    print("Max retries reached. Returning default score.")
                    return 5

    def gen_article_score_with_llms(self, data_dict, article_type):
        biases = []
        results = []
        y_true = []
        y_pred = []
        bias_dict = {1: [], 2: [], 3: [], 5: []}

        for data in tqdm(data_dict):
            print("="*60)
            print(f"Data ID {data['id']}")
            # if data['score'] == 4 or data["priority"] is None:
                # continue
            if article_type == 'article':
                if "Cassandra.SourceText" not in data or not data["Cassandra.SourceText"]:
                    continue
                article = data["Cassandra.SourceText"]
            elif article_type == 'description':
                article = data["System.Description"]
            result = self.analyze_article_priority(article)
            if result == 0:
                result = 5
            results.append({
                "id": data["id"],
                "score": data["score"],
                "llm_result": result
            })
            bias = int(abs(result - data["score"]))
            y_true.append(data["score"])
            y_pred.append(result)
            biases.append(bias)
            print(f"==> Ground truth score: {data['score']}")
            print(f"==> Predicted score: {result}")
            print(f"==> Correct: {data['score'] == result}")
            print(f"==> Bias: {bias}")

            if data["score"] in bias_dict:
                bias_dict[data["score"]].append(bias)

        overall_bias = round(np.mean(biases), 4) if biases else 0

        avg_bias_per_class = {}
        for score, biases_list in bias_dict.items():
            if biases_list:
                avg_bias_per_class[score] = round(np.mean(biases_list), 4)
            else:
                avg_bias_per_class[score] = 0

        accuracy = accuracy_score(y_true, y_pred)
        precision_macro = precision_score(y_true, y_pred, average='macro', zero_division=0)
        recall_macro = recall_score(y_true, y_pred, average='macro', zero_division=0)
        f1_macro = f1_score(y_true, y_pred, average='macro', zero_division=0)
        cm = confusion_matrix(y_true, y_pred)
        report = classification_report(y_true, y_pred, zero_division=0, digits=3)
        print("\n====== Evaluation Metrics ======")
        print(f"Overall Accuracy: {accuracy:.4f}")
        print(f"Overall Bias: {overall_bias:4f}")
        print(f"Overall Precision (macro): {precision_macro:.4f}")
        print(f"Overall Recall (macro): {recall_macro:.4f}")
        print(f"Overall F1 Score (macro): {f1_macro:.4f}")
        print("\nConfusion Matrix:")
        print(cm)
        print("\nClassification Report:")
        print(report)

        matrix = np.array(cm)

        accept_matrix = matrix[0:3, 0:3]  # submatrix for accept (first 3 rows and first 3 columns)
        # Reject category: 4th row (for score 5)
        reject_matrix = matrix[3]  # 4th row

        # Calculate correctness rates:
        # Accept: True positives = diagonal sum of accept submatrix
        accept_true_positives = np.sum(accept_matrix)
        # Total number of elements in the first 3 rows
        accept_total = np.sum(matrix[0:3, :])
        accept_correct_rate = accept_true_positives / accept_total if accept_total else 0

        # Reject: True positive is the (4,4) element (last element in the 4th row)
        reject_true_positives = reject_matrix[3]
        # Total number of elements in the 4th row
        reject_total = np.sum(reject_matrix)
        reject_correct_rate = reject_true_positives / reject_total if reject_total else 0

        print(f"Accept Category - Correct: {accept_true_positives}, Total: {accept_total}, Correct Rate: {accept_correct_rate:.4f}")
        print(f"Reject Category - Correct: {reject_true_positives}, Total: {reject_total}, Correct Rate: {reject_correct_rate:.4f}")
        TP = np.sum(accept_matrix)
        FN = np.sum(matrix[0:3, :]) - TP
        TN = matrix[3][3]
        FP = sum(reject_matrix) - TN

        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        accuracy = (TP + FN) / (TP + FP + FN + TN)

        print(f"Accept Category - Precision: {precision:.4f}, Recall: {recall:.4f}")
        print(f"Accept Category - Accuracy: {accuracy:.4f}")


        print("\n====== Ground Truth Accept Group Metrics ======")
        accept_matrix_total = matrix[0:3, :]
        acc = np.trace(accept_matrix_total)
        accuracy_accept = acc / np.sum(accept_matrix_total)  # Accuracy for accept group
        print(f"Overall Accuracy (Accept Group): {accuracy_accept:.4f}")

        total_bias = 0  # Total bias sum
        total_count = 0  # Total number of elements considered for bias calculation
 

        for true_index, true_val in enumerate([1, 2, 3]):  # Ground truth values (1, 2, 3)
            for pred_index, pred_val in enumerate([1, 2, 3, 5]):  # Predicted values (1, 2, 3, 5)
                # Calculate bias: absolute difference between ground truth and prediction
                bias = abs(true_val - pred_val)
                # Count is the number of occurrences in the matrix (matrix element at [true_index, pred_index])
                count = accept_matrix_total[true_index, pred_index]
                
                # Update total bias and total count
                total_bias += bias * count
                total_count += count

        # Calculate Average Bias for Accept Group
        avg_bias_accept = total_bias / total_count if total_count != 0 else 0  # Avoid division by zero
        print(f"Average Bias (Accept Group):     {avg_bias_accept:.4f}")

        combined_metrics = {
            "overall_accuracy": accuracy,
            "overall_bias": overall_bias,
            "precision_macro": precision_macro,
            "recall_macro": recall_macro,
            "f1_macro": f1_macro,
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
