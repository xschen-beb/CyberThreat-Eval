import json
import sys
import os
print(sys.path)
import argparse
import time
import logging
import tiktoken
import json5
import numpy as np
import pandas as pd
from tqdm import tqdm
from search_engine import click_into_page_with_browser
from tenacity import (retry, stop_after_attempt, wait_random_exponential)
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import requests
from datetime import datetime
from collections import Counter
from contextlib import redirect_stdout
from azure.identity import InteractiveBrowserCredential, TokenCachePersistenceOptions

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


### Baseline
def root_cause_baseline(client, model, article):
    sys_prompt = """
    You are a cybersecurity analyst. Your task is to carefully analyze the provided article or blog and generate the summarized detailed context of the root cause behind the incident including vulnerable/misconfigured services, exploitations, and malware name (e.g., Misconfigured Kibana instance, SmokeLoader malware). Focus on the most critical vulnerabilities/misconfigurations/malware that led to the incident. Group similar issues and avoiding just listing all vulnerabilities. If no blog provides the info, output "Not specified". If there are hints or general observations in the article, use them to supplement your answer.
    """
    user_prompt = f"Please analyze the following article and extract the threat actor information:\n\n{article}"
    
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    response_message = api_call(client, messages, model_name=model, json_enabled=False)
    result = response_message.choices[0].message.content
    return result


### RAG based augmentation
def get_access_token(client_id, scopes):
    """Get access token using InteractiveBrowserCredential"""
    options = {"client_id": client_id}
    browser_cred = InteractiveBrowserCredential(**options, cache_persistence_options=TokenCachePersistenceOptions(allow_unencrypted_storage=True))
    token = browser_cred.get_token(*scopes)
    return token


def get_articles(token, query):
    """Get articles based on the given query"""
    url = "https://onetiproda.trafficmanager.net/api/paperboy/articles?api-version=2023-01-01"
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "X-Riskiq-Client": "unknown"
    }
    params = {"Title": query}

    try:    
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        articles = response.json()
        return articles
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON deserialization error: {json_err}")


def get_profiles(token, query):
    """Get profiles based on the given query"""
    url = "https://onetiproda.trafficmanager.net/api/paperboy/profiles?api-version=2023-01-01"
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "X-Riskiq-Client": "unknown"
    }
    params = {"Title": query}

    try:    
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        profiles = response.json()
        return profiles
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON deserialization error: {json_err}")


def extract_root_cause(client, model, article):
    sys_prompt = """
    ### Task description:
    You are an expert in cybersecurity. I will provide you with an IoC report. Please extract the relevant and potential threat malwares (if it has other names, extract them.) in the **list format** from the "root cause" section of the report and ensure that the extracted term is suitable for use in a search query. For each output, it should be a phrase or a single word without any prefixes. If no specific threat actor is specified, the output should be ['None'].

    ### Example:
    Report Content: The incident was caused by a North Korean IT worker cluster (CL-STA-0237) exploiting a U.S.-based IT services company's credentials and infrastructure to carry out phishing attacks using malware-infected video conference apps, including InvisibleFerret malware *Your changes* (https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/) and BeaverTail stealer *Your changes* (https://objective-see.org/blog/blog_0x7A.html). *The attackers also posed as prospective employers to lure developers into fake interviews, delivering updated BeaverTail and InvisibleFerret malware* (https://thehackernews.com/2024/10/n-korean-hackers-use-fake-interviews-to.html). *The malware targets job seekers via platforms like LinkedIn and X, distributing through files disguised as legitimate applications such as MiroTalk and FreeConference* (https://www.infosecurity-magazine.com/news/beavertail-malware-job-seekers/). 
    ['InvisibleFerret', 'BeaverTail']

    Report Content: A compromised access token from a highly privileged developer, Aidosmf (aidosmf@gmail.com), allowed attackers to publish malicious versions of the @lottiefiles/lottie-player package on npm, designed to steal crypto wallet assets. *The attack stemmed from a phishing attack on an employee's NPM account* (https://www.securityweek.com/lottie-player-supply-chain-attack-targets-cryptocurrency-wallets/). *The employee's laptop was quarantined* (https://www.securityweek.com/lottie-player-supply-chain-attack-targets-cryptocurrency-wallets/). *Exaforce was engaged for rapid Incident Response and ongoing cloud detection and response* (https://lottiefiles.com/blog/inside-lottiefiles/resolution-of-security-incident-with-lottiefiles-lottie-player-package). *Attack leveraged an npm automation token to bypass 2FA controls* (https://thehackernews.com/2024/10/lottiefiles-issues-warning-about.html). 
    ['Aidosmf']
    """

    user_prompt = f"""
    ### Task description:
    I will provide you with an IoC report. Please extract the relevant and potential malwares(if it has other names, extract them.) in the list format from the "root cause" section of the report and ensure that the extracted term is suitable for use in a search query. For each item of the list, it should be a phrase or a single word without any prefixes. If no specific threat actor is specified, the output should be ['None'].

    ### Result:
    Report Content: {article}
    """
    
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    response_message = api_call(client, messages, model_name=model, json_enabled=False)
    result = response_message.choices[0].message.content
    return result


def augment_root_cause_context(client, model, root_cause, root_cause_info):
    sys_prompt = """
    ### Task description:
    You are an expert in cybersecurity. Based on the extracted information about the root cause from a blog, please generate a detailed context and summary about the root cause of the incident based on the report content and your knowledge. Ensure the context includes details about vulnerable or misconfigured services, exploited weaknesses, and contributing factors. Your output must be concise, professional, and factually accurate. No hallucination is allowed. Ensure the output provides sufficient information for a security professional to understand the root cause. No explanations or prefix texts like "Context:" are allowed in the output.

    ### Example:
    Root Cause: Misconfigured Kibana instance
    Context: The root cause of the incident was a misconfigured Kibana instance exposed to the Internet without authentication. This allowed attackers to inject malicious scripts and access sensitive data, resulting in data exfiltration.

    Root Cause: Exploitation of zero-day vulnerability
    Context: The incident was caused by attackers exploiting a zero-day vulnerability in a widely used web application framework, enabling unauthorized access and the deployment of ransomware on affected systems.

    Root Cause: Insufficient email filtering
    Context: The root cause was insufficient email filtering, allowing phishing emails with malicious attachments to bypass security controls and deliver malware to target devices.
    """

    user_prompt = f"""
    ### Task description:
    Based on the extracted information about the root cause from a blog, please briefly generate a detailed context and summary about the root cause of the incident based on the report content and your knowledge. No hallucination is allowed. Ensure the output is concise and provides sufficient information for a security professional to understand the root cause. No explanations or prefix texts like "Context:" are allowed in the output.

    ### Result:
    Root Cause: {root_cause}
    Report Content: {root_cause_info}
    Context:
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(client, new_messages, model_name=model, json_enabled=False)
    response = response_message.choices[0].message.content
    return response


def rag_root_cause_pipeline(client, model, article_content, token):
    actors = extract_root_cause(client, model, article_content)
    names = []
    links = []
    context = ""  # Use a single string to accumulate contexts

    if not actors:
        return ""

    actors = eval(actors)
    if actors and 'None' not in actors:
        for actor in actors:
            print(f"Processing actor: {actor}\n")
            articles = get_articles(token.token, actor)

            actors_info = ""

            if articles and articles["data"]["totalPages"] > 0:
                print(f"Found {articles['data']['totalPages']} pages of articles for {actor}.\n")
                content = articles["data"]["content"]

                # Process each article up to a limit of 5
                for i in range(min(articles['data']['totalPages'], 5)):
                    # Generate unique link for the article
                    name = content[i]['guid']
                    link = f"https://sip.security.microsoft.com/intel-profiles/{name}"
                    if link not in links:
                        links.append(link)
                        names.append(actor)
                        actors_info += str(content[i]['content'])

            else:
                print(f"No articles found for actor: {actor}\n")
                continue

            # Generate context for the actor using `augment_root_cause_context`
            if actors_info.strip():
                actor_context = augment_root_cause_context(client, model, actor, actors_info)
                context += f"{actor_context}\n"
                print(f"Context for {actor} generated.\n")
            else:
                print(f"No sufficient information for {actor} to augment context.\n")

            if len(names) == 3:
                break

        if not names:
            print("No relevant actors or unique links found.")

        return context
    return ""


### Evaluation
def calculate_average_score(evaluation_dict):
    total_score = sum(evaluation_dict.values())
    average_score = total_score / len(evaluation_dict)
    return average_score


def calculate_average_score_for_criteria(total_scores, num_entries):
    return {key: sum(values) / num_entries for key, values in total_scores.items()}


def evaluate_root_cause_context(client, model, original_article, generated_context):
    sys_prompt = """
    ### Task description:
    You are an expert evaluator in cybersecurity. I will provide you with the name of a malware/tool and the corresponding LLM-generated context.
    Your task is to assess the quality of the LLM-generated context based on the following criteria and scoring metrics, ensuring that you consider how well the malware contributes to the root cause of an incident is explained in the context and its relationship to the overall cybersecurity landscape.


    ### Evaluation Criteria and Metrics:

    1. Relevance:
        - 1: Unrelated to the root cause of the incident or fails to mention key aspects of the malware's role (e.g., attack vector, exploitation method, malware behavior).
        - 2: Limited relevance; partial or tangentially related information but misses key aspects of the malware or incident context.
        - 3: Moderately relevant; covers some important aspects but lacks depth or misses critical connections between the malware and the incident context.
        - 4: Mostly relevant; covers most key aspects with minor omissions or inaccuracies in the relationship between malware and incident context.
        - 5: Highly relevant; fully aligns with the incident's root cause, addressing all key aspects of the malware's role and its relationship with the incident's context comprehensively.

    2. Accuracy:
        - 1: Factually incorrect or inconsistent with known details about the malware and the incident's root cause.
        - 2: Significant inaccuracies or contradictions, though some elements are correct.
        - 3: Moderately accurate; factual but contains minor inconsistencies or errors about how the malware contributes to the incident.
        - 4: Mostly accurate; aligns well with known information about the malware and the incident with very few errors.
        - 5: Completely accurate; perfectly reflects known factual content about the malware's role in the incident's root cause.

    3. Comprehensiveness:
        - 1: Highly incomplete; fails to cover critical details about the malware’s role or the broader context of the incident.
        - 2: Covers only minimal details; significant gaps remain in explaining how the malware is related to the incident.
        - 3: Moderately comprehensive; includes some critical details but misses others, such as the attack methodology or the specific impact of the malware.
        - 4: Comprehensive; covers most critical details with minor omissions, explaining how the malware's characteristics contributed to the incident.
        - 5: Fully comprehensive; captures all essential details about the malware, its functionality, and how it relates to the overall context of the incident.

    4. Clarity:
        - 1: Poorly written, unclear, and difficult to understand, with significant ambiguity around the role of the malware in the incident.
        - 2: Significant clarity issues; partially understandable but requires effort to interpret the relationship between the malware and the incident.
        - 3: Moderately clear; generally understandable but with some ambiguities regarding how the malware influenced the incident's outcome.
        - 4: Mostly clear; easy to understand the connection between the malware and the incident with minor ambiguities.
        - 5: Fully clear; well-organized and easy to understand, with a clear and logical explanation of the malware’s role in the incident.

    5. Coherence:
        - 1: Explanation lacks logical flow, with no clear connection between the malware and the incident root cause.
        - 2: Some coherence, but there are significant logical gaps or unclear relationships between malware and incident root cause.
        - 3: Generally coherent, though some links between malware and incident root cause may be weak or unclear.
        - 4: Mostly coherent; strong logical connection between malware and incident root cause with only minor gaps.
        - 5: Fully coherent; logical and clear connection throughout, detailing how the malware directly led to the incident's root cause.

    6. Attribution:
        - 1: Attribution is completely incorrect; no connection between the malware and the actual threat actor or root cause.
        - 2: Significant attribution errors; the threat actor is misidentified, or motives are unclear.
        - 3: Basic attribution is correct, but there are minor inaccuracies or omissions regarding the threat actor's identity or objectives.
        - 4: Mostly correct attribution; the threat actor and motives are clearly identified, with only minor inaccuracies.
        - 5: Perfect attribution; accurately identifies the threat actor, their objectives, and the precise relationship to the incident's root cause.

    ### Evaluation Instructions:
    For each criterion, assign a score between 1 and 5 based on the metrics provided above. Then output the evaluation scores strictly in the JSON format below without any prefixes or explanations:
    {"Relevance": <score>, "Accuracy": <score>, "Comprehensiveness": <score>, "Clarity": <score>, "Coherence": <score>, "Attribution": <score>}

    Do not include any additional text or comments outside the JSON object.
    """

    user_prompt = f"""
    ### Task description:
    Evaluate the quality of the generated context for the root cause malware/tool by comparing it against the original article based on the provided criteria and metrics.

    Original article:
    {original_article}

    Generated Context:
    {generated_context}
    """

    # Prepare messages for API call
    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    # Call the API to perform the evaluation
    response_message = api_call(client, new_messages, model_name=model, json_enabled=True)
    response = response_message.choices[0].message.content

    # Parse the JSON response
    try:
        evaluation_scores = json.loads(response)
    except json.JSONDecodeError as e:
        print(f"Error parsing evaluation response: {e}")
        evaluation_scores = {"error": "Unable to parse scores"}

    return evaluation_scores


def main():
    _AUTH_SCOPE = "https://cognitiveservices.azure.com/.default"
    _CREDENTIAL = DefaultAzureCredential()
    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)

    parser = argparse.ArgumentParser(description="Run an LLM model for threat actor extraction")
    parser.add_argument("-model", type=str, required=True, help="Model name to run (e.g., gpt-4o, o3-mini, etc.)")

    args = parser.parse_args()
    model_name = args.model

    eval_client = AzureOpenAI(
        azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
        api_key=os.getenv("PROXY_KEY"),
        api_version="2024-05-01-preview",
    )

    # Setup the AzureOpenAI client based on the model name
    if model_name in ['gpt-4o-mini', 'gpt-4o']:
        client = AzureOpenAI(
            azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
            api_key=os.getenv("PROXY_KEY"),
            api_version="2024-05-01-preview",
        )
    elif model_name == 'o3-mini':
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
    
    log_dir = os.path.join("score_evaluation", "root_cause")
    os.makedirs(log_dir, exist_ok=True)
    output_json = os.path.join(log_dir, f"{model_name}.json")
    input_json = 'score_evaluation/0330-articles-with-rejected-score.json'

    # Open input file to read data
    with open(input_json, 'r', encoding='utf-8') as fi:
        input_data = json.load(fi)

    # Open output file in append mode for writing results
    with open(output_json, 'w', encoding='utf-8') as fo:
        # Initialize total score variables for calculating overall averages
        total_baseline_score = 0
        total_rag_score = 0
        total_scores_baseline = { "Relevance": [], "Accuracy": [], "Comprehensiveness": [], "Clarity": [], "Coherence": [], "Attribution": [] }
        total_scores_rag = { "Relevance": [], "Accuracy": [], "Comprehensiveness": [], "Clarity": [], "Coherence": [], "Attribution": [] }
        
        num_entries = len(input_data)
        
        # Extract the article content from "System.Description"
        for data in tqdm(input_data):
            article_content = data.get("System.Description", "")
            
            # Extract threat actor context using the baseline method
            threat_actor_context = root_cause_baseline(client, model_name, article_content)
            
            # Evaluate the threat actor context from the baseline using the 'evaluate_actor_context' method
            baseline_evaluation = evaluate_root_cause_context(eval_client, 'gpt-4o', article_content, threat_actor_context)
            baseline_average = calculate_average_score(baseline_evaluation)
            
            # Add the baseline evaluation scores to the total scores
            for criterion in baseline_evaluation:
                total_scores_baseline[criterion].append(baseline_evaluation[criterion])
            
            # Evaluate the RAG-based actor pipeline results using 'rag_based_actor_pipeline'
            rag_context = rag_root_cause_pipeline(client, model_name, article_content, token)
            print(f"=> RAG raw result: {rag_context}")
            print(f"=> Original result: {threat_actor_context}")
            if rag_context and threat_actor_context:
                rag_evaluation = threat_actor_context + "\nThe following is from the retrieved profiles or articles:\n" + rag_context
            else:
                rag_evaluation = threat_actor_context
            print(f"=> RAG total result: {rag_evaluation}")
            rag_evaluation_result = evaluate_root_cause_context(eval_client, 'gpt-4o', article_content, rag_evaluation)
            rag_average = calculate_average_score(rag_evaluation_result)
            
            # Add the RAG evaluation scores to the total scores
            for criterion in rag_evaluation_result:
                total_scores_rag[criterion].append(rag_evaluation_result[criterion])
            
            # Prepare the output data with the required structure
            output_data = {
                "id": data['id'],
                "url": data['url'],
                "description": article_content,
                "baseline_threat_actor_context": threat_actor_context,
                "rag_threat_actor_context": rag_evaluation,
                "baseline_evaluation": baseline_evaluation,  # baseline evaluation result
                "baseline_average": baseline_average,  # average score for baseline
                "rag_evaluation": rag_evaluation_result,  # rag evaluation result
                "rag_average": rag_average  # average score for rag evaluation
            }

            # Write the output data to the file as JSON
            json.dump(output_data, fo, ensure_ascii=False)
            fo.write('\n')  # Add newline to separate each JSON object

        # After the loop, calculate and add the overall averages to the final output file
        overall_baseline_average = calculate_average_score_for_criteria(total_scores_baseline, num_entries)
        overall_rag_average = calculate_average_score_for_criteria(total_scores_rag, num_entries)

        # Write the overall averages to a separate JSON object (e.g., at the end of the file)
        overall_averages = {
            "overall_baseline_average": overall_baseline_average,
            "overall_rag_average": overall_rag_average
        }

        json.dump(overall_averages, fo, ensure_ascii=False)
        fo.write('\n')  # Add newline to separate the overall averages


if __name__ == '__main__':
    main()

