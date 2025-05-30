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
def extract_threat_actor(client, model, article):
    sys_prompt = """
    You are a cybersecurity analyst. Your task is to carefully analyze the provided article or blog and extract detailed information about the threat actor, group, or campaign responsible for the attack. Identify who carried out the attack, which may include an organization, a malware family, or any related threat group. If the article does not specify any actors, output "Not specified". If the article provides partial information, include and succinctly summarize the details. You should not merely listing names or short phrases, and no explanations or prefixes are included.
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


def get_actor(client, model_name, threat_actor):
    # threat_actor = extract_threat_actor_info(file)
    sys_prompt = """
    ### Task description:
    You are an expert in cybersecurity. I will provide you with an OSINT report. Please extract the relevant and potential threat actors (if it has other names, extract them.) in the list format and ensure that the extracted term is suitable for use in a search query. For each output, it should be a phrase or a single word without any prefixes. If no threat actor is specified, the output should be ['None'].

    ### Example:
    Report Content: BrazenBamboo, a Chinese state-affiliated threat actor, developer of DEEPDATA, DEEPPOST, and LIGHTSPY malware families. *BrazenBamboo's cross-platform reach extends to Windows, macOS, and iOS* (https://cyberinsider.com/chinese-hackers-exploit-fortinet-zero-day-to-steal-vpn-credentials/). *APT41 and Space Pirates, suspected to be involved* (https://thehackernews.com/2024/11/warning-deepdata-malware-exploiting.html). *Volexity�s analysis reveals that BrazenBamboo maintains a sophisticated infrastructure for command and control (C2) operations* (https://cybersecuritynews.com/brazenbamboo-apt-forticlient-zero-day/). *DEEPDATA malware uses a modular architecture with 12 unique plugins* (https://securityonline.info/zero-day-vulnerability-in-forticlient-exploited-by-brazenbamboo-apt/). 
    ['BrazenBamboo']

    Report Content: Earth Estries (also known as Salt Typhoon); overlaps with FamousSparrow and UNC4841 (https://thehackernews.com/2023/08/earth-estries-espionage-campaign.html). Similarities with FamousSparrow APT observed in operation and TTPs (https://duo.com/decipher/new-espionage-threat-group-targets-tech-government-entities). 
    ['Earth Estries', 'Salt Typhoon']

    Report Content: Unknown threat actor.
    ['None']
    """

    user_prompt = f"""
    ### Task description:
    I will provide you with an OSINT report. Please extract the relevant and potential threat actors(if it has other names, extract them.) in the list format and ensure that the extracted term is suitable for use in a search query. For each item of the list, it should be a phrase or a single word without any prefixes. If no threat actor is specified, the output should be ['None'].
    ### Result:
    Report Content: {threat_actor}
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(client, messages=new_messages, model_name=model_name, json_enabled=False)
    response = response_message.choices[0].message.content
    return response


def augment_threat_actor_context(client, model, threat_actor, actor_info):
    sys_prompt = """
    ### Task description:
    You are an expert in cybersecurity. Based on the extracted information about the threat actor from an OSINT report, please generate a detailed context and summary about this threat actor based on report context given and your knowledge. No hallucination is allowed. Your context should be brief. This will be used to enhance the description of the threat actor in the report. Make sure the context provides enough details for a security professional to understand the actor's profile and their behaviors. No explanations or prefix texts are allowed in the output.

    ### Example:
    Threat Actor: BrazenBamboo
    Context: BrazenBamboo is a Chinese state-affiliated APT group. It is responsible for various attacks targeting government entities, private companies, and critical infrastructure worldwide. The group utilizes sophisticated malware such as DEEPDATA and DEEPPOST to exploit vulnerabilities in both Windows and macOS systems. They are known to use advanced techniques like spear-phishing and zero-day vulnerabilities to achieve their objectives. In the past, they have targeted industries such as telecommunications, finance, and energy.

    Threat Actor: Earth Estries
    Context: Earth Estries, also known as Salt Typhoon, is a Chinese cyber espionage group primarily focused on targeting the technology sector and governmental entities in Western countries. They are known to overlap with other APT groups such as FamousSparrow and UNC4841. Their primary modus operandi includes spear-phishing emails with malicious attachments, web shell exploitation, and using remote access tools (RATs) to gain unauthorized access to target networks.
    """

    user_prompt = f"""
    ### Task description:
    Based on the extracted information about the threat actor from an an OSINT report, please briefly generate a detailed context and summary about this threat actor based on report context given and your knowledge. No hallucination is allowed. This will be used to enhance the description of the threat actor in the report. No explanations or prefix texts are allowed in the output.

    ### Result:
    Threat Actor: {threat_actor}
    Report Content: {actor_info}
    Context:
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(client, new_messages, model_name=model, json_enabled=False)
    response = response_message.choices[0].message.content
    return response


def oneti_pipeline(client, model, actors, token):
    names = []
    links = []
    count = 0
    context = ""  # Use a single string to accumulate contexts

    for actor in actors:
        print(f"Processing {actor}: ... \n")
        profiles = get_profiles(token.token, actor)
        articles = get_articles(token.token, actor)

        actors_info = ""

        if profiles and profiles["data"]["totalPages"] > 0 :
            print("=" * 20 + " Using oneti profile " + "=" * 20 + '\n')
            content = profiles["data"]["content"]
            print(profiles["data"]["totalPages"])

            # Generate unique link for the actor's profile
            name = profiles['data']['content'][0]['name']
            link = f"https://sip.security.microsoft.com/intel-profiles/{name}"
            if link not in links:
                names.append(actor)
                links.append(link)
                count += 1
                for i in range(min(profiles['data']['totalPages'], 1)):
                    actors_info += str(profiles["data"]["content"][i]['description'])

        elif articles and articles['data']['totalPages'] > 0:
            print("=" * 20 + " Using related articles " + "=" * 20 + '\n')
            content = articles["data"]["content"]

            for i in range(min(articles['data']['totalPages'], 5)):
                actors_info += str(articles["data"]["content"][i]['content'])
                count += 1

        else:
            print(f"No profiles or articles found for {actor}")
            continue

        # Generate context for the actor using augment_threat_actor_context
        if actors_info.strip():
            actor_context = augment_threat_actor_context(client, model, actor, actors_info)
            context += f"{actor_context}\n"
            print(f"Context for {actor}:\n{actor_context}\n")
        else:
            print(f"No information found for {actor} to augment context.")


        if count == 3:
            break
    return names, links, context


def rag_based_actor_pipeline(client, model_name, article_content, token):
    actors = get_actor(client, model_name, article_content)
    if actors and 'None' not in actors:
        threat_actors = eval(actors)
        actor_name, links, context = oneti_pipeline(client, model_name, threat_actors, token)
        print(f"==> Context: {context}\n")
        valid_links = []

        for link in links:
            try:
                blog_content = click_into_page_with_browser(link)  # Assuming this function returns blog content as a string
                num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                
                # Only include links with content exceeding 500 tokens
                if num_tokens > 500:
                    valid_links.append(link)
            except Exception as e:
                print(f"Error processing {link}: {e}")
        
        if context:
            context = context.replace('\n\n', '\n')
        
        else:
            context = augment_threat_actor_context(client, model_name, actors, article_content)
            
        return context
    return ""


### Evaluation
def calculate_average_score(evaluation_dict):
    total_score = sum(evaluation_dict.values())
    average_score = total_score / len(evaluation_dict)
    return average_score


def calculate_average_score_for_criteria(total_scores, num_entries):
    return {key: sum(values) / num_entries for key, values in total_scores.items()}


def evaluate_actor_context(client, model, original_article, generated_context):
    sys_prompt = """
    ### Task Description:
    You are an expert evaluator in cybersecurity research with a strong background in threat intelligence and OSINT analysis. Based on recent literature and best practices, your task is to assess the quality of a generated context provided for a specific threat actor by comparing it against an original article containing verified details.

    ### Input:
    - Generated Context: An automatically generated summary or analysis about the threat actor.
    - Original Article: The source article containing verified information on the threat actor.

    ### Evaluation Criteria and Metrics:

    1. Relevance: Measures how closely the generated context aligns with the key details of the original article (e.g., aliases, motivations, tactics).
    - 1: Unrelated or fails to mention key aspects.
    - 2: Limited relevance; misses critical details.
    - 3: Moderately relevant; covers some aspects but lacks depth.
    - 4: Mostly relevant; minor omissions or inaccuracies.
    - 5: Highly relevant; fully aligns with the original article.

    2. Accuracy: Assesses the factual correctness of the generated context compared to the original article.
    - 1: Factually incorrect or inconsistent.
    - 2: Contains significant inaccuracies.
    - 3: Moderately accurate; minor inconsistencies.
    - 4: Mostly accurate; very few errors.
    - 5: Completely accurate; perfectly reflects the original article.

    3. Comprehensiveness: Evaluates the extent to which the generated context covers all critical details from the original article.
    - 1: Highly incomplete; critical details missing.
    - 2: Covers only minimal details; significant gaps.
    - 3: Moderately comprehensive; some key details missing.
    - 4: Comprehensive; minor omissions.
    - 5: Fully comprehensive; captures all essential details.

    4. Clarity: Measures how clear and understandable the generated context is.
    - 1: Poorly written, unclear, and difficult to understand.
    - 2: Significant clarity issues; partially understandable.
    - 3: Moderately clear; some ambiguities.
    - 4: Mostly clear; minor issues.
    - 5: Perfectly clear; highly readable and easily understandable.

    5. Coherence: Assesses the logical structure and flow of the generated context.
    - 1: Disorganized and difficult to follow.
    - 2: Significant coherence issues; scattered information.
    - 3: Moderately coherent; inconsistent flow.
    - 4: Mostly coherent; well-organized with minor issues.
    - 5: Fully coherent; logically structured and easy to follow.

    6. Attribution: Evaluates whether the generated context properly attributes information to the original article.
    - 1: Information is unverified or unattributed.
    - 2: Major attribution issues; many details are not clearly linked.
    - 3: Moderately attributable; some details lack clear source references.
    - 4: Mostly attributable; minor gaps in linking information.
    - 5: Fully attributable; all details are clearly linked to the original article.

    ### Evaluation Instructions:
    For each criterion, assign a score between 1 and 5 based on the metrics provided. Then output the evaluation scores strictly in the following JSON format without any additional text, prefixes, or comments:

    {"Relevance": <score>, "Accuracy": <score>, "Comprehensiveness": <score>, "Clarity": <score>, "Coherence": <score>, "Attribution": <score>}
    """

    user_prompt = f"""
    ### Task Description:
    Evaluate the quality of the generated context for the given threat actor by comparing it against the original article.

    Generated Context:
    {generated_context}

    Original Article:
    {original_article}
    """

    # Prepare messages for API call
    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    # Call the API to perform the evaluation
    response_message = api_call(client, new_messages, model_name=model, json_enabled=True)
    response = response_message.choices[0].message.content

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
    
    log_dir = os.path.join("score_evaluation", "description")
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
            threat_actor_context = extract_threat_actor(client, model_name, article_content)
            
            # Evaluate the threat actor context from the baseline using the 'evaluate_actor_context' method
            baseline_evaluation = evaluate_actor_context(eval_client, 'gpt-4o', article_content, threat_actor_context)
            baseline_average = calculate_average_score(baseline_evaluation)
            
            # Add the baseline evaluation scores to the total scores
            for criterion in baseline_evaluation:
                total_scores_baseline[criterion].append(baseline_evaluation[criterion])
            
            # Evaluate the RAG-based actor pipeline results using 'rag_based_actor_pipeline'
            rag_context = rag_based_actor_pipeline(client, model_name, article_content, token)
            print(f"=> RAG raw result: {rag_context}")
            print(f"=> Original result: {threat_actor_context}")
            if rag_context and threat_actor_context:
                rag_evaluation = threat_actor_context + "\nThe following is from the retrieved profiles or articles:\n" + rag_context
            else:
                rag_evaluation = threat_actor_context
            print(f"=> RAG total result: {rag_evaluation}")
            rag_evaluation_result = evaluate_actor_context(eval_client, 'gpt-4o', article_content, rag_evaluation)
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
    client = AzureOpenAI(
        azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
        api_key=os.getenv("PROXY_KEY"),
        api_version="2024-05-01-preview",
    )
    model = "gpt-4o"
    actor = "Andariel group"
    desc = "Andariel group, operators of HelloKitty ransomware\nThe following is from the retrieved profiles or articles:\n Andariel, also known as Stonefly or Silent Chollima, is a North Korean state-affiliated APT group. They are responsible for deploying Maui ransomware and DTrack malware, targeting various entities globally. Their attack strategy includes using legitimate proxy and tunneling tools, PowerShell scripts, and Bitsadmin to download additional malware. They exploit known but unpatched vulnerabilities in public services like WebLogic and HFS. Andariel's operations often involve prolonged dwell times within target networks before deploying ransomware, indicating a focus on financial gain and extensive interest. Their malware, DTrack, shows high code similarity with previous variants, reinforcing their consistent use of specific tools and techniques.HelloKitty is a ransomware group known for its lack of stealth compared to other notorious ransomware families like Ryuk, REvil, and Conti. Despite this, HelloKitty has successfully targeted several high-profile organizations, including CEMIGO. The group employs ransomware to encrypt victims' data and demands a ransom for decryption. Their attacks typically involve exploiting vulnerabilities in systems and using social engineering techniques to gain initial access. HelloKitty's operations have been documented and analyzed, providing indicators of compromise (IoCs) for cybersecurity professionals to detect and mitigate their threats.Mauri is a ransomware group known for exploiting vulnerabilities such as CVE-2023-46604 in Apache ActiveMQ to target systems, particularly in South Korea. Their primary objective is to install CoinMiners on unpatched systems. Mauri employs sophisticated techniques to infiltrate networks and deploy ransomware, causing significant disruptions and financial losses. They have been active in targeting various industries, leveraging unpatched vulnerabilities to maximize their impact."
    # res = evaluate_actor_context(eval_client, 'gpt-4o', actor, desc)
    # print(res)

