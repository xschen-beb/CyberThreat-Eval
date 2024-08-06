import json
from openai import AzureOpenAI

# for exponential backoff
from tenacity import (retry, stop_after_attempt, wait_random_exponential)  


# ANSI escape codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

client = AzureOpenAI(
    azure_endpoint = "http://10.150.142.182:8999", 
    api_key="placeholder",  
    api_version="2023-07-01-preview"
)



# @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def api_call(messages, func_list):
    return client.chat.completions.create(
                model="gpt-4-32k",
                messages=messages,
                # functions= func_list,
                # function_call="auto",  # auto is default, but we'll be explicit
                temperature=0.7,
                # response_format={ "type": "json_object" },
                # seed=42,
            )


with open("es_incidents.txt", "r") as f:
    blog = f.read()


sys_prompt = "You are a security expert.  I will give a blog, you goal is to identify if it is critial securty event. If yes, please provide basic summary which incluiding the impacted service, the impact, etc. You outout should be json format with is_critical, summary, service, impact as the key."


# Update the system prompt
messages = [
    {"role": "system", "content": sys_prompt},
]

misconf_qeustion = f"Here is the blog: {blog}."

messages.append({"role": "user", "content": misconf_qeustion})

print(RED + "Step 1:" + RESET, "Ask the model to identify if it is a critical security event.")

response_message = api_call(messages, [])

print(response_message)
print(response_message.choices[0])

response = response_message.choices[0].message.content
response_dict = json.loads(response)
if response_dict["is_critical"]:
    print("This is a critical security event.")
    print("Summary:", response_dict["summary"])
    print("Service:", response_dict["service"])
    print("Impact:", response_dict["impact"])

    print(RED + "Step 2:" + RESET, "Search realated exploit documents or attack details. (Manual done)")

    sys_prompt = """
    You are security expert. I will give a report on the Intent. You should provide some signature in the following format:    
    
    Service: Redis    
    Port: 6379    
    Severity: Critical    
    Signature name: “Redis publicly accessible”    
    Internal checks (see next)    
    - Setting1: Redis port (6379) should not be exposed on external Internet. – In platform    
    - Setting2: Redis port (6379) should not listen on the external Internet – Inside VMs    
    - Setting3: Redis server should secure with authentication credentials. – Inside VMs    
    External scanning (see next)    
    - Port (6379) open    
    - Redis no-pass-login
    """

    messages = [
        {"role": "system", "content": sys_prompt},
    ]

    misconf_qeustion = f"Here is the blog: {blog}."

    messages.append({"role": "user", "content": misconf_qeustion})
    print(RED + "Step 3:" + RESET, "Ask the model to help indentify related misconfiguration signatures.")
    response_message = api_call(messages, [])

    print(response_message)
    print(response_message.choices[0].message.contentcd )

else:
    print("This is not a critical security event.")
