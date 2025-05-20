import json
import ast
import argparse
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import os
from tenacity import (retry, stop_after_attempt, wait_random_exponential)
import tiktoken
import logging
import sys
import time
import pandas as pd
import json5
sys.stdout.reconfigure(encoding='utf-8')

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

def load_ttp_mapping(csv_file='src/TTP_Mapping.csv'):
    """
    Loads a mapping of TTP IDs to their names from a CSV file.

    Args:
        csv_file (str): Path to the CSV file containing the mapping data. Defaults to 'src/TTP_Mapping.csv'.

    Returns:
        dict: A dictionary where keys are TTP IDs and values are TTP names.
    """
    ttp_mapping = {}
    with open(csv_file, 'r', encoding='utf-8') as f:
        for line in f:
            if ',' in line:
                fields = line.strip().split(',')
                if len(fields) >= 3:
                    ttp_id = fields[1]
                    ttp_name = fields[2]
                    ttp_mapping[ttp_id] = ttp_name
    return ttp_mapping


def validate_ttps(ttp_dict_str):
    """
    Validates TTP descriptions against a known mapping.

    Args:
        ttp_dict_str (str or dict): A string representation of a Python dictionary or a dictionary 
                                    containing TTPs and their descriptions.

    Returns:
        dict: A dictionary of validated TTPs.
    """
    # Load the TTP mapping from the CSV
    ttp_mapping = load_ttp_mapping()

    # Convert input string to a dictionary, if necessary, using ast.literal_eval instead of json.loads
    if isinstance(ttp_dict_str, str):
        try:
            ttp_data = json5.loads(ttp_dict_str)

            ttp_data = ast.literal_eval(ttp_dict_str)
        except Exception as e:
            print(f"Error parsing TTP data: {e}")
            return {}
    else:
        ttp_data = ttp_dict_str

    validated_ttps = {}

    # Determine if the data is a list or dictionary
    if isinstance(ttp_data, list):
        # If a list is provided, take the first element as the TTP dictionary
        ttp_dict = ttp_data[0] if ttp_data else {}
    else:
        # Otherwise, use the provided dictionary
        ttp_dict = ttp_data

    # Iterate through the TTP dictionary to validate each entry
    for ttp_id, details in ttp_dict.items():
        # Extract the description from the details string
        description = details.split(',')[0].strip()

        if ttp_id in ttp_mapping:
            # If the TTP ID exists in the mapping, check if the description matches
            if description.lower() == ttp_mapping[ttp_id].lower():
                validated_ttps[ttp_id] = details
            else:
                print(f"Warning: Description mismatch for {ttp_id}")
                print(f"Expected: {ttp_mapping[ttp_id]}")
                print(f"Found: {description}")
        else:
            print(f"Warning: TTP ID {ttp_id} not found in mapping")

    return validated_ttps


def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string, disallowed_special=()))
    return num_tokens


def debug_print(*args, **kwargs):
    if _LOG_ENABLED:
        message = ' '.join(str(arg) for arg in args)
        logging.debug(message)
        print(*args, **kwargs) 
    else:
        pass


@retry(wait=wait_random_exponential(min=1, max=120), stop=stop_after_attempt(10))
def api_call(client, messages, model_name, json_enabled=True):
    global total_llm_call
    global total_tokens
    total_llm_call += 1
    total_tokens += num_tokens_from_string(str(messages), model_name)
    debug_print(RED + "==> Total LLM Calls: " + RESET, total_llm_call)
    debug_print(RED + "==> Total Tokens: " + RESET, total_tokens)

    # If models in ['o1 series', 'o3 series']
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


def extract_ttps(client, input_article, model_name):
    global total_tokens
    sys_prompt = """
    You are a cybersecurity expert. Your task is to analyze the provided article text and accurately extract all MITRE ATT&CK TTPs that are directly supported by clear evidence in the article. For each identified TTP, you must:
    1. Identify the MITRE TTP code (e.g., "T1078").

    2. Provide a brief description of how the attack was carried out as described in the article.

    3. Assign a confidence score ("High", "Medium", or "Low") based solely on the evidence presented in the article.

    4. Offer a concise justification that cites specific evidence or phrases from the article to support the identification and confidence level.

    Your final output MUST be a Python dictionary format (in plain text) where each key is a MITRE TTP code, and the corresponding value is a string formatted exactly as follows:

        "<TTP Description>, Confidence: <score>. Justification: <your justification citing the article>"

    Do not include any additional text or commentary. Only output TTPs that are clearly supported by the article. For example, if the article provides strong evidence for T1078 and T1190, your output should look like:

        {"T1078": "Valid Accounts, Confidence: High. Justification: The article explicitly describes the use of stolen credentials to gain unauthorized access.", "T1190": "Exploit Public-Facing Application, Confidence: Medium. Justification: The article mentions vulnerabilities in a web application that were exploited during the attack."}

    Make sure to strictly follow this format and do not hallucinate any additional TTPs.

    """
    user_prompt = f"""
    Please analyze the following article text and extract all MITRE ATT&CK TTPs that are clearly supported by evidence in the article. For each identified TTP, provide:
    1. The MITRE TTP code (e.g., "T1078").
    2. A brief description of how the attack was carried out as described in the article.
    3. A confidence score ("High", "Medium", or "Low") based solely on the evidence presented.
    4. A concise justification that cites specific evidence or phrases from the article.

    Output your answer as a exactly Python dictionary format.

    Article text:
    {input_article}
    """
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
    response_message = api_call(client, messages, model_name, json_enabled=False)
    original = response_message.choices[0].message.content
    total_tokens += num_tokens_from_string(str(original), model_name)
    debug_print(RED + "==> Total Tokens: " + RESET, total_tokens)
    if original.startswith("```"):
        # Split lines and remove the first and last line if they contain ```
        lines = original.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        original = "\n".join(lines).strip()


    return original


def extract_ttps_with_ref(client, input_article, model_name):
    """
    Uses an LLM to extract MITRE ATT&CK TTP items from an article text.
    
    This function dynamically loads a TTP mapping from a CSV file and inserts it into the system prompt
    as a reference table. The LLM is then instructed to extract only those TTPs that are clearly supported
    by evidence in the article. The final output must be a Python dictionary (plain text) in which each key
    is a MITRE TTP code and its value is a string formatted as:
    
      "<TTP Description>, Confidence: <score>. Justification: <justification>"
    """

    # Load the TTP mapping from CSV file
    csv_file = 'src/TTP_Mapping.csv'
    df = pd.read_csv(csv_file, encoding='utf-8')
    # Select only the relevant columns ("TechniqueID" and "name")
    mapping_df = df[['TechniqueID', 'name']]
    # Create a dictionary mapping from TechniqueID to name
    ttp_mapping_dict = dict(zip(mapping_df['TechniqueID'], mapping_df['name']))
    
    # Build the reference string from the mapping dictionary, one entry per line
    reference_str = "\n".join([f"{ttp}: {name}" for ttp, name in ttp_mapping_dict.items()])
    
    # Define the system prompt, inserting the reference TTP table into the prompt text
    sys_prompt = f"""
    You are a cybersecurity expert. Your task is to analyze the provided article text along with the following MITRE ATT&CK TTP table to extract all TTP items that are clearly supported by evidence in the article.
    
    For each identified TTP, you must:
      1. Identify the MITRE TTP code (e.g., "T1078").
      2. Provide a brief description of how the attack was carried out as described in the article.
      3. Assign a confidence score ("High", "Medium", or "Low") based solely on the evidence in the article.
      4. Provide a concise justification that cites specific evidence or phrases from the article.
    
    Your final output MUST be a Python dictionary (in plain text) where each key is a MITRE TTP code and its corresponding value is a string formatted exactly as:
    
      "<TTP Description>, Confidence: <score>. Justification: <justification>"
    
    Use the following MITRE ATT&CK TTP table as reference:
    {reference_str}
    
    Note: This reference table is provided to ensure that if any TTP code cannot be mapped to a name properly, you must use the table's mapping to replace it.
    
    Do not include any extra text, commentary, or hallucinated TTPs.
    """
    
    # Define the user prompt with the article text to be analyzed
    user_prompt = f"""
    Please analyze the following article text and, using the provided MITRE ATT&CK TTP table as your reference, extract all TTP items that are clearly supported by the evidence in the article.
    
    For each identified TTP, provide:
      1. The MITRE TTP code (e.g., "T1078").
      2. A brief description of how the attack was carried out as described in the article.
      3. A confidence score ("High", "Medium", or "Low") based solely on the evidence.
      4. A concise justification that cites specific evidence or phrases from the article.
    
    Output your answer strictly as a Python dictionary.
    
    Article text:
    {input_article}
    """
    # Prepare the messages for the API call
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    # Call the API using the provided client and model name
    response_message = api_call(client, messages, model_name, json_enabled=False)
    
    # Extract the response content
    original = response_message.choices[0].message.content
    
    # Update the total token count for debugging
    total_tokens += num_tokens_from_string(str(original), model_name)
    debug_print(RED + "==> Total Tokens: " + RESET, total_tokens)
    
    # Remove markdown code fences if they are present in the output
    if original.startswith("```"):
        lines = original.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        original = "\n".join(lines).strip()
    
    return original


def compute_precision_recall(articles, client, model_name):
    total_tp = 0
    total_fp = 0
    total_fn = 0
    
    for article in articles:
        try:
            time_start = time.time()
            # Extract raw TTPs from the article field "ttps" (a list of strings in format "Txxxx - ...")
            raw_ttps = article.get("ttps", [])
            # Extract TTP codes from the article list (e.g., "T1136" from "T1136 - Create Account")
            article_ttps_set = {ttp.split(" - ")[0].strip() for ttp in raw_ttps if " - " in ttp}
            print("Article TTP Codes:", article_ttps_set)
            
            # Use your extraction and validation functions to obtain validated TTPs
            result = extract_ttps(client, article, model_name)
            print("Extracted TTPs (raw):", result)
            if isinstance(result, str):
                try:
                    # result_fixed = result.replace("'", '"')
                    validated_ttps = json5.loads(result)
                except Exception as e:
                    print(f"Error parsing TTP data: {e}")
                    continue
            else:
                validated_ttps = result

            # For raw data
            # validated_ttps = validate_ttps(result)
            print("Validated TTPs:", validated_ttps)
            
            # Extract validated TTP codes (keys from validated_ttps)
            validated_ttps_set = set(validated_ttps.keys())
            print("Validated TTP Codes:", validated_ttps_set)
            
            # Calculate True Positives, False Positives, and False Negatives for this article
            tp = len(article_ttps_set.intersection(validated_ttps_set))
            fp = len(validated_ttps_set - article_ttps_set)
            fn = len(article_ttps_set - validated_ttps_set)
            
            print(f"Article metrics: TP: {tp}, FP: {fp}, FN: {fn}\n")
            time_end = time.time()
            print(f"==> Total time taken for TTPs: {time_end - time_start:.2f} seconds")
            
            total_tp += tp
            total_fp += fp
            total_fn += fn

        # Calculate overall precision and recall
            overall_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
            overall_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0

            print("Overall Metrics:")
            print(f"Total True Positives: {total_tp}")
            print(f"Total False Positives: {total_fp}")
            print(f"Total False Negatives: {total_fn}")
            print(f"Precision: {overall_precision:.4f}")
            print(f"Recall: {overall_recall:.4f}")
        except Exception as e:
            print(f"Error: {e}")
            continue

    return overall_precision, overall_recall


def compute_raw_precision_recall(articles, client, model_name):
    """
    Compute raw precision and recall metrics for extracted TTPs from a list of articles.

    For each article:
      1. Extract raw TTP codes from the article's "ttps" field.
      2. Use the extraction function to obtain validated TTPs.
      3. Validate each extracted TTP against a known mapping:
         - If a TTP's description does not match the expected mapping,
           issue a warning and do NOT add this TTP to the final validated TTPs.
           (Such TTPs will be treated as false positives.)
      4. Compute TP, FP, FN for the article and update overall totals.

    Returns:
        overall_precision (float), overall_recall (float)
    """
    total_tp = 0
    total_fp = 0
    total_fn = 0
    
    # Load the TTP mapping from CSV (assume this function is defined)
    ttp_mapping = load_ttp_mapping()

    for article in articles:
        try:
            time_start = time.time()
            # Extract raw TTP codes from the article field "ttps"
            raw_ttps = article.get("ttps", [])
            # Extract TTP codes from the article list (e.g., "T1136" from "T1136 - Create Account")
            article_ttps_set = {ttp.split(" - ")[0].strip() for ttp in raw_ttps if " - " in ttp}
            print("Article TTP Codes:", article_ttps_set)
            
            # Use the extraction function to obtain validated TTPs
            result = extract_ttps(client, article, model_name)
            print("Extracted TTPs (raw):", result)
            if isinstance(result, str):
                try:
                    validated_ttps = json5.loads(result)
                except Exception as e:
                    print(f"Error parsing TTP data: {e}")
                    continue
            else:
                validated_ttps = result

            print("Validated TTPs (pre-validation):", validated_ttps)
            
            # Validate extracted TTPs using mapping.
            # If a TTP's description does not match, do not add it to validated_ttps_final,
            # and count it as a false positive.
            miscount = 0
            validated_ttps_final = {}
            for ttp_id, details in validated_ttps.items():
                description = details.split(',')[0].strip()
                if ttp_id in ttp_mapping:
                    if description.lower() == ttp_mapping[ttp_id].lower():
                        validated_ttps_final[ttp_id] = details
                    else:
                        # Description mismatch: do not add to validated_ttps_final
                        print(f"Warning: Description mismatch for {ttp_id}")
                        print(f"Expected: {ttp_mapping[ttp_id]}")
                        print(f"Found: {description}")
                        # total_fp += 1  # Count as false positive
                        miscount += 1
                else:
                    print(f"Warning: TTP ID {ttp_id} not found in mapping")
            validated_ttps_set = set(validated_ttps_final.keys())
            print("Validated TTP Codes (after validation):", validated_ttps_set)
            
            # Calculate True Positives, False Positives, and False Negatives for this article
            tp = len(article_ttps_set.intersection(validated_ttps_set))
            fp = miscount
            # fp = len(validated_ttps_set - article_ttps_set)
            # fn = len(article_ttps_set - validated_ttps_set)
            fn = len(article_ttps_set) - tp - fp
            
            print(f"Article metrics: TP: {tp}, FP: {fp}, FN: {fn}\n")
            time_end = time.time()
            print(f"==> Total time taken for TTPs: {time_end - time_start:.2f} seconds")
            
            total_tp += tp
            total_fp += fp
            total_fn += fn

            overall_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
            overall_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0

            print("Overall Metrics:")
            print(f"Total True Positives: {total_tp}")
            print(f"Total False Positives: {total_fp}")
            print(f"Total False Negatives: {total_fn}")
            print(f"Precision: {overall_precision:.4f}")
            print(f"Recall: {overall_recall:.4f}")
        except Exception as e:
            print(f"Error: {e}")

    return overall_precision, overall_recall

# method 3
def compute_mapping_precision_recall(articles, client, model_name):
    """
    Compute precision and recall metrics for TTP extraction from a list of articles,
    using a known TTP mapping to validate the extracted TTP descriptions.

    For each article:
      1. Extract ground truth TTP codes from the article's "ttps" field.
      2. Use an LLM-based extraction function to obtain a dictionary of validated TTPs.
      3. For each extracted TTP:
         - If the TTP ID exists in the mapping:
              * If its description matches the expected description (case-insensitive),
                add it to the final validated TTP dictionary.
              * If the description does not match, print a warning, replace the description
                with the correct one from the mapping, and add it to the final validated TTP dictionary.
         - If the TTP ID is not found in the mapping, print a warning and count it as a false positive.
      4. Compute:
         - True Positives (TP): Number of TTP codes that are present in both the article and the final validated set.
         - False Positives (FP): Number of TTP codes in the final validated set that are not present in the article plus any TTP IDs not found in the mapping.
         - False Negatives (FN): Number of TTP codes in the article that are missing from the final validated set.
      5. Accumulate overall TP, FP, FN across all articles and compute overall precision and recall.

    Returns:
        overall_precision (float), overall_recall (float)
    """
    total_tp = 0
    total_fp = 0
    total_fn = 0

    # Load the TTP mapping from CSV (assume this function is defined elsewhere)
    ttp_mapping = load_ttp_mapping()

    for article in articles:
        try:
            time_start = time.time()
            
            # Extract raw TTP codes from the article's "ttps" field.
            # Each entry is expected to be in the format "Txxxx - description".
            raw_ttps = article.get("ttps", [])
            article_ttps_set = {ttp.split(" - ")[0].strip() for ttp in raw_ttps if " - " in ttp}
            print("Article TTP Codes (Ground Truth):", article_ttps_set)
            
            # Use the extraction function (e.g., an LLM call) to obtain a dictionary of validated TTPs.
            result = extract_ttps(client, article, model_name)
            print("Extracted TTPs (raw):", result)
            if isinstance(result, str):
                try:
                    validated_ttps = json5.loads(result)
                except Exception as e:
                    print(f"Error parsing TTP data: {e}")
                    continue
            else:
                validated_ttps = result

            print("Extracted Validated TTPs (pre-mapping):", validated_ttps)
            
            # Validate each extracted TTP using the mapping.
            # If the description mismatches, replace it with the correct description.
            validated_ttps_final = {}
            missing_in_mapping_count = 0  # Count TTPs not found in mapping
            for ttp_id, details in validated_ttps.items():
                # Assume details is a string like "Description, Confidence: ..., Justification: ..."
                description = details.split(',')[0].strip()
                if ttp_id in ttp_mapping:
                    if description.lower() == ttp_mapping[ttp_id].lower():
                        validated_ttps_final[ttp_id] = details
                    else:
                        # Description mismatch: update the description using the mapping.
                        print(f"Warning: Description mismatch for {ttp_id}")
                        print(f"Expected: {ttp_mapping[ttp_id]}")
                        print(f"Found: {description}")
                        # Replace the description with the correct one from the mapping.
                        corrected_details = ttp_mapping[ttp_id]
                        validated_ttps_final[ttp_id] = corrected_details
                else:
                    # TTP ID not found in mapping, count as false positive.
                    print(f"Warning: TTP ID {ttp_id} not found in mapping")
                    missing_in_mapping_count += 1
            
            # Final set of validated TTP codes after mapping correction.
            validated_ttps_set = set(validated_ttps_final.keys())
            print("Validated TTP Codes (after mapping validation):", validated_ttps_set)
            
            # Compute metrics for the article.
            tp = len(article_ttps_set.intersection(validated_ttps_set))
            # FP: TTPs in validated set but not in ground truth, plus those not found in mapping.
            fp = len(validated_ttps_set - article_ttps_set) + missing_in_mapping_count
            # FN: TTP codes in ground truth that are missing from the validated set.
            fn = len(article_ttps_set) - tp - fp
            
            print(f"Article metrics: TP: {tp}, FP: {fp}, FN: {fn}\n")
            time_end = time.time()
            print(f"==> Total time taken for TTP processing: {time_end - time_start:.2f} seconds")
            
            total_tp += tp
            total_fp += fp
            total_fn += fn

        except Exception as e:
            print(f"Error processing article: {e}")

        overall_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
        overall_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0

        print("Overall Metrics:")
        print(f"Total True Positives: {total_tp}")
        print(f"Total False Positives: {total_fp}")
        print(f"Total False Negatives: {total_fn}")
        print(f"Precision: {overall_precision:.4f}")
        print(f"Recall: {overall_recall:.4f}")

    return overall_precision, overall_recall

# method 2
def compute_raw_with_mapping_precision_recall(articles, client, model_name):
    """
    Compute raw precision and recall metrics for extracted TTPs from a list of articles.

    For each article:
      1. Extract raw TTP codes from the article's "ttps" field.
      2. Use the extraction function to obtain validated TTPs.
      3. Validate each extracted TTP against a known mapping:
         - If a TTP's description does not match the expected mapping,
           issue a warning and do NOT add this TTP to the final validated TTPs.
           (Such TTPs will be treated as false positives.)
      4. Compute TP, FP, FN for the article and update overall totals.

    Returns:
        overall_precision (float), overall_recall (float)
    """
    total_tp = 0
    total_fp = 0
    total_fn = 0
    
    # Load the TTP mapping from CSV (assume this function is defined)
    ttp_mapping = load_ttp_mapping()

    for article in articles:
        try:
            time_start = time.time()
            # Extract raw TTP codes from the article field "ttps"
            raw_ttps = article.get("ttps", [])
            # Extract TTP codes from the article list (e.g., "T1136" from "T1136 - Create Account")
            article_ttps_set = {ttp.split(" - ")[0].strip() for ttp in raw_ttps if " - " in ttp}
            print("Article TTP Codes:", article_ttps_set)
            
            # Use the extraction function to obtain validated TTPs
            result = extract_ttps_with_ref(client, article, model_name)
            print("Extracted TTPs (raw):", result)
            if isinstance(result, str):
                try:
                    validated_ttps = json5.loads(result)
                except Exception as e:
                    print(f"Error parsing TTP data: {e}")
                    continue
            else:
                validated_ttps = result

            print("Validated TTPs (pre-validation):", validated_ttps)
            
            # Validate extracted TTPs using mapping.
            # If a TTP's description does not match, do not add it to validated_ttps_final,
            # and count it as a false positive.
            miscount = 0
            validated_ttps_final = {}
            for ttp_id, details in validated_ttps.items():
                description = details.split(',')[0].strip()
                if ttp_id in ttp_mapping:
                    if description.lower() == ttp_mapping[ttp_id].lower():
                        validated_ttps_final[ttp_id] = details
                    else:
                        # Description mismatch: do not add to validated_ttps_final
                        print(f"Warning: Description mismatch for {ttp_id}")
                        print(f"Expected: {ttp_mapping[ttp_id]}")
                        print(f"Found: {description}")
                        # total_fp += 1  # Count as false positive
                        miscount += 1
                else:
                    print(f"Warning: TTP ID {ttp_id} not found in mapping")
            validated_ttps_set = set(validated_ttps_final.keys())
            print("Validated TTP Codes (after validation):", validated_ttps_set)
            
            # Calculate True Positives, False Positives, and False Negatives for this article
            tp = len(article_ttps_set.intersection(validated_ttps_set))
            fp = miscount
            # fp = len(validated_ttps_set - article_ttps_set)
            # fn = len(article_ttps_set - validated_ttps_set)
            fn = len(article_ttps_set) - tp - fp
            
            print(f"Article metrics: TP: {tp}, FP: {fp}, FN: {fn}\n")
            time_end = time.time()
            print(f"==> Total time taken for TTPs: {time_end - time_start:.2f} seconds")
            
            total_tp += tp
            total_fp += fp
            total_fn += fn

            overall_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
            overall_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0

            print("Overall Metrics:")
            print(f"Total True Positives: {total_tp}")
            print(f"Total False Positives: {total_fp}")
            print(f"Total False Negatives: {total_fn}")
            print(f"Precision: {overall_precision:.4f}")
            print(f"Recall: {overall_recall:.4f}")
        except Exception as e:
            print(f"Error: {e}")

    return overall_precision, overall_recall


def main():
    _AUTH_SCOPE = "https://cognitiveservices.azure.com/.default"
    _CREDENTIAL = DefaultAzureCredential()
    parser = argparse.ArgumentParser(description="Run an LLM model")
    parser.add_argument("-model", type=str, required=False, help="Model name to run")
    args = parser.parse_args()

    model_name = args.model
    if model_name in ['gpt-4o-mini', 'gpt-4o']:
        client = AzureOpenAI(
            azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
            api_key=os.getenv("PROXY_KEY"),
            api_version="2024-05-01-preview",
        )
    elif model_name in ['o3-mini']:
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
    with open('TTP/100-days-articles.json', 'r', encoding='utf-8') as f:
        articles = json.load(f)

    time_start = time.time()
    # compute_precision_recall(articles, client, model_name)
    # compute_raw_precision_recall(articles, client, model_name)
    # compute_raw_with_mapping_precision_recall(articles, client, model_name)
    compute_mapping_precision_recall(articles, client, model_name)
    time_end = time.time()
    print(f"==> Total time taken for all TTPs: {time_end - time_start:.2f} seconds")
    
if __name__ == '__main__':
    # mapping = load_ttp_mapping()
    # print(mapping)
    main()