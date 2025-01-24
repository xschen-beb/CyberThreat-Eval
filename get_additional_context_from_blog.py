from tenacity import (retry, stop_after_attempt, wait_random_exponential)
import os
from openai import AzureOpenAI
from search_engine import click_into_page_with_browser

os.environ["LOCAL_ENDPOINT"] = "http://10.150.142.182:9999"
os.environ["PROXY_KEY"] = "59ddb6820482b719e33661ccbfa98042"

client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def api_call(messages, func_list, model= "gpt-4o", json_enabled=True):
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
    
def get_threat_actor_context_from_blog(blog_content, threat_actor):
    sys_prompt = f"""
    ### Task description:
    You are an expert in cybersecurity. Based on the given blog content and the specified threat actor, provide a detailed but concise context about the threat actor. This context should include their behaviors, known targets, and any notable techniques or tools they use. Your response must be factually accurate and derived from the blog content without hallucination. Directly output your answer without explanation or prefixes like "contents:".

    ### Example:
    Threat Actor: BrazenBamboo
    Blog Content: The group BrazenBamboo, a Chinese APT, has been linked to a series of cyberattacks against government entities. Their tools include DEEPDATA and DEEPPOST malware, which exploit Windows and macOS vulnerabilities. They have targeted sectors such as finance, energy, and telecommunications.
    BrazenBamboo is a Chinese APT group focusing on cyber espionage and attacks against critical infrastructure. They use advanced malware like DEEPDATA and DEEPPOST, and employ techniques such as spear-phishing and exploiting zero-day vulnerabilities.

    Threat Actor: Earth Estries
    Blog Content: Earth Estries has been identified as a Chinese cyber espionage group targeting Western technology companies. Their activities overlap with FamousSparrow and UNC4841. Techniques include spear-phishing, web shell exploitation, and the use of RATs.
    Earth Estries is a Chinese cyber espionage group targeting technology and governmental entities. They are associated with groups like FamousSparrow and UNC4841 and utilize techniques such as spear-phishing and web shell exploitation.
    """

    user_prompt = f"""
    ### Task description:
    Based on the given blog content and the specified threat actor, provide a brief but detailed context about the threat actor. Directly output your answer without explanation or prefixes like "contents:".

    Threat Actor: {threat_actor}
    Blog Content: {blog_content}
    """

    # LLM API call
    new_messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response_message = api_call(new_messages, [], model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response

def get_root_cause_context_from_blog(blog_content, root_cause):
    sys_prompt = f"""
    ### Task description:
    You are an expert in cybersecurity. Based on the given blog content and the specified root cause, provide a concise and detailed explanation of the root cause behind the incident. Include any vulnerable or misconfigured services, exploited weaknesses, and contributing factors mentioned in the blog. Your response must be factually accurate and based solely on the blog content. Directly output your answer without explanation or prefixes like "contents:".

    ### Example:
    Root Cause: Misconfigured Kibana instance
    Blog Content: The attack exploited a misconfigured Kibana instance, which was exposed to the public Internet without authentication. Attackers used this to inject malicious scripts and exfiltrate sensitive data.
    The root cause of the incident was a misconfigured Kibana instance exposed to the Internet without authentication. This allowed attackers to inject malicious scripts and access sensitive data.

    Root Cause: Phishing emails
    Blog Content: The attackers used phishing emails to deceive employees into providing their credentials. These emails contained malicious links that directed victims to fake login pages, allowing attackers to steal login information.
    The root cause was phishing emails containing malicious links. Employees were tricked into providing credentials through fake login pages, enabling unauthorized access.
    """
    

    user_prompt = f"""
    ### Task description:
    Based on the given blog content and the specified root cause, provide a brief but detailed explanation of the root cause. Directly output your answer without explanation or prefixes like "contents:".

    Root Cause: {root_cause}
    Blog Content: {blog_content}
    Context:
    """

    # LLM API call
    new_messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response_message = api_call(new_messages, [], model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response

if __name__ == '__main__':
    url = 'https://research.checkpoint.com/2025/banshee-macos-stealer-that-stole-code-from-macos-xprotect'
    blog = click_into_page_with_browser(url)
    actor = 'Banshee'
    res = get_threat_actor_context_from_blog(blog, actor)
    print(res)
