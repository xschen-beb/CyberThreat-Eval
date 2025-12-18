"""
Common utilities for evaluation scripts.
This module contains shared functions and constants used across evaluation scripts.
"""
import json
import sys
import os
import logging
import tiktoken
from tenacity import (retry, stop_after_attempt, wait_random_exponential)

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
    
    Args:
        client: AzureOpenAI client instance
        messages: List of message dictionaries for the API call
        model_name: Name of the model to use
        json_enabled: Whether to enable JSON response format
    
    Returns:
        API response object
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


def calculate_average_score(evaluation_dict):
    """
    Calculate the average score from an evaluation dictionary.
    
    Args:
        evaluation_dict: Dictionary with numeric values
    
    Returns:
        Average of all values in the dictionary
    """
    total_score = sum(evaluation_dict.values())
    average_score = total_score / len(evaluation_dict)
    return average_score


def calculate_average_score_for_criteria(total_scores, num_entries):
    """
    Calculate average scores for each criterion across multiple entries.
    
    Args:
        total_scores: Dictionary with lists of scores for each criterion
        num_entries: Number of entries (for averaging)
    
    Returns:
        Dictionary with average scores for each criterion
    """
    return {key: sum(values) / num_entries for key, values in total_scores.items()}


def get_client(model_name, use_azure=True, api_key=None, api_base=None):
    """
    Create and return an LLM client (Azure OpenAI or OpenAI).
    
    Args:
        model_name: Name of the model to use
        use_azure: Whether to use Azure OpenAI (default: True)
        api_key: API key for OpenAI (used when use_azure=False)
        api_base: API base URL for OpenAI (used when use_azure=False)
    
    Returns:
        AzureOpenAI or OpenAI client instance
    """
    from openai import AzureOpenAI, OpenAI
    
    if use_azure:
        return AzureOpenAI(
            azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
            api_key=os.getenv("PROXY_KEY"),
            api_version="2024-05-01-preview",
        )
    
    if api_key is None:
        raise ValueError("api_key is required when use_azure=False")
    
    if api_base:
        return OpenAI(
            api_key=api_key,
            base_url=api_base
        )
    
    return OpenAI(api_key=api_key)

