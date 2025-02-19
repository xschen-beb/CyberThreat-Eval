import os
from openai import AzureOpenAI
from tenacity import (retry, stop_after_attempt, wait_random_exponential)
import tiktoken
import argparse

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
_LOG_ENABLED = True

os.environ["LOCAL_ENDPOINT"] = "http://10.150.142.182:9999"
os.environ["PROXY_KEY"] = "59ddb6820482b719e33661ccbfa98042"

client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)
total_llm_call = 0
total_tokens = 0

def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string, disallowed_special=()))
    return num_tokens

def debug_print(*args, **kwargs):
    if _LOG_ENABLED:
        message = ' '.join(str(arg) for arg in args)
        print(*args, **kwargs) 
    else:
        pass

@retry(wait=wait_random_exponential(min=1, max=120), stop=stop_after_attempt(2))
def api_call(messages, func_list, model= "gpt-4o", json_enabled=True):
    global total_llm_call
    global total_tokens
    total_llm_call += 1
    total_tokens += num_tokens_from_string(str(messages), model)
    debug_print(RED + "==> Total LLM Calls: " + RESET, total_llm_call)
    debug_print(RED + "==> Total Tokens: " + RESET, total_tokens)

    # for models in ['o1 series', 'o3 series']
    if model == 'o3-mini':
        new_messages = []
        for message in messages:
            if message["role"] == "system":
                new_messages.append({"role": "developer", "content": [{"type": "text", "text": message["content"]}]})
            else:
                new_messages.append({"role": message["role"], "content": [{"type": "text", "text": message["content"]}]})
        
        return client.chat.completions.create(
            model=model,
            messages=new_messages,
            response_format={"type": "json_object"} if json_enabled else None,
            max_completion_tokens=100000,
        )

    if model == 'gpt-4-32k':
        return client.chat.completions.create(
            # model="gpt-4-32k",
            model=model,
            messages=messages,
            # functions= func_list,
            # function_call="auto",  # auto is default, but we'll be explicit
            temperature=0.01,
            # seed=42,
            max_tokens=8192,
        )
    if json_enabled:
        return client.chat.completions.create(
            # model="gpt-4-32k",
            model=model,
            messages=messages,
            # functions= func_list,
            # function_call="auto",  # auto is default, but we'll be explicit
            temperature=0.01,
            response_format={"type": "json_object"},
            # seed=42,
            max_tokens=4096,
        )
    else:
        return client.chat.completions.create(
            # model="gpt-4-32k",
            model=model,
            messages=messages,
            # functions= func_list,
            # function_call="auto",  # auto is default, but we'll be explicit
            temperature=0.01,
            # response_format={ "type": "json_object" },
            # seed=42,
            max_tokens=4096,
        )


def gen_ans(model_name):
    messages = [{"role": "system", "content": "Answer the question without explanation."}, {"role": "user", "content": "what are the names of the last 5 US presidents? Answer in json format."}]
    response = api_call(messages, func_list=[], model=model_name)
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def main():
    client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
    )
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=50
    )
    print(response.choices[0].message.content)
    
    parser = argparse.ArgumentParser(description="Run an LLM model")
    parser.add_argument("-model", type=str, required=False, help="Model name to run")
    args = parser.parse_args()

    model_name = args.model
    gen_ans(model_name)



if __name__ == '__main__':
    main()

