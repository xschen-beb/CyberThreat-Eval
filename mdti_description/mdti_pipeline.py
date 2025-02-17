import sys
import os

parent_directory = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_directory)

from playwright.sync_api import sync_playwright
from src.search_engine import click_into_page_with_browser
import os
from openai import AzureOpenAI
from tenacity import retry, stop_after_attempt, wait_random_exponential
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from bs4 import BeautifulSoup
from mdti_description.crawl_malpedia import *
from mdti_description.crawl_oneti import *
import re
import json


client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def api_call(messages, temperature, model="gpt-4o", json_enabled=True):
    if model == 'gpt-4-32k':
        return client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=512,
        )
    if json_enabled:
        return client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            response_format={"type": "json_object"},
            max_tokens=512,
        )
    else:
        return client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=512,
        )


def extract_threat_actor_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            content = file.read()
    pattern = r"#### Threat actor/group/campaign\s*(.*?)(?=\n####|\Z)"
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    else:
        return "Threat actor/group/campaign section not found."
    return None


# input: the contexts containing threat actors
# output: list of threat actors
def get_actor(threat_actor):
    # threat_actor = extract_threat_actor_info(file)
    sys_prompt = """
    ### Task description:
    You are an expert in cybersecurity. I will provide you with a threat intelligence report. Please extract the relevant and potential threat actors (if it has other names, extract them.) in the list format from the "threat actor" section of the report and ensure that the extracted term is suitable for use in a search query. For each output, it should be a phrase or a single word without any prefixes. If no content is provided, output is None.

    ### Example:
    Report Content: BrazenBamboo, a Chinese state-affiliated threat actor, developer of DEEPDATA, DEEPPOST, and LIGHTSPY malware families. *BrazenBamboo's cross-platform reach extends to Windows, macOS, and iOS* (https://cyberinsider.com/chinese-hackers-exploit-fortinet-zero-day-to-steal-vpn-credentials/). *APT41 and Space Pirates, suspected to be involved* (https://thehackernews.com/2024/11/warning-deepdata-malware-exploiting.html). *Volexity�s analysis reveals that BrazenBamboo maintains a sophisticated infrastructure for command and control (C2) operations* (https://cybersecuritynews.com/brazenbamboo-apt-forticlient-zero-day/). *DEEPDATA malware uses a modular architecture with 12 unique plugins* (https://securityonline.info/zero-day-vulnerability-in-forticlient-exploited-by-brazenbamboo-apt/). 
    ['BrazenBamboo']

    Report Content: Earth Estries (also known as Salt Typhoon); overlaps with FamousSparrow and UNC4841 (https://thehackernews.com/2023/08/earth-estries-espionage-campaign.html). Similarities with FamousSparrow APT observed in operation and TTPs (https://duo.com/decipher/new-espionage-threat-group-targets-tech-government-entities). 
    ['Earth Estries', 'Salt Typhoon']

    Report Content:
    None
    """

    user_prompt = f"""
    ### Task description:
    I will provide you with a threat intelligence report. Please extract the relevant and potential threat actors(if it has other names, extract them.) in the list format from the "threat actor" section of the report and ensure that the extracted term is suitable for use in a search query. For each item of the list, it should be a phrase or a single word without any prefixes.

    ### Result:
    Report Content: {threat_actor}
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(new_messages, temperature=0.01, model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response


def get_actor_v1(threat_actor):
    # threat_actor = extract_threat_actor_info(file)
    sys_prompt = """
    ### Task description:
    You are an expert in cybersecurity. I will provide you with a threat intelligence report. Please extract the relevant and potential threat actors, vulnerable softwares, and malicious tools/framework (if it has other names, extract them.) from the report. Output in the list format and ensure that the extracted term is suitable for use in a search query. For each output, it should be a phrase or a single word without any prefixes. If no content is provided, output is None.

    ### Example:

    Report Content: Earth Estries (also known as Salt Typhoon); overlaps with FamousSparrow and UNC4841 (https://thehackernews.com/2023/08/earth-estries-espionage-campaign.html). Similarities with FamousSparrow APT observed in operation and TTPs (https://duo.com/decipher/new-espionage-threat-group-targets-tech-government-entities). 
    ['Earth Estries', 'Salt Typhoon']

    Report Content: Cybercriminals are actively exploiting vulnerabilities in SimpleHelp Remote Monitoring and Management (RMM) software to infiltrate networks, create unauthorized administrator accounts, and deploy malware, including the Sliver backdoor. These accounts facilitated the installation of malicious payloads like the Sliver post-exploitation framework. Sliver, an open-source tool originally designed for penetration testing, has been repurposed by threat actors for command-and-control (C2) operations.
    ['Sliver', 'RMM', 'Remote Monitoring and Management']

    Report Content: BrazenBamboo, a Chinese state-affiliated threat actor, developer of DEEPDATA, DEEPPOST, and LIGHTSPY malware families. *BrazenBamboo's cross-platform reach extends to Windows, macOS, and iOS* (https://cyberinsider.com/chinese-hackers-exploit-fortinet-zero-day-to-steal-vpn-credentials/). *APT41 and Space Pirates, suspected to be involved* (https://thehackernews.com/2024/11/warning-deepdata-malware-exploiting.html). *Volexity�s analysis reveals that BrazenBamboo maintains a sophisticated infrastructure for command and control (C2) operations* (https://cybersecuritynews.com/brazenbamboo-apt-forticlient-zero-day/). *DEEPDATA malware uses a modular architecture with 12 unique plugins* (https://securityonline.info/zero-day-vulnerability-in-forticlient-exploited-by-brazenbamboo-apt/). 
    ['BrazenBamboo']

    """

    user_prompt = f"""
    ### Task description:
    I will provide you with a threat intelligence report. Please extract the Top 3 relevant and potential threat actors, vulnerable softwares, and malicious tools/framework (if it has other names, extract them.) from the report. Output in the list format and ensure that the extracted term is suitable for use in a search query. For each item of the list, it should be a phrase or a single word without any prefixes.

    ### Result:
    Report Content: {threat_actor}
    """

    print("==> The input to Thrat Actor Extraction is: ", threat_actor)

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(new_messages, temperature=0.01, model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response


def pipeline(threat_actors, source_name, oneti_token):
    if not threat_actors:
        return None
    else:
        if source_name.lower() == 'malpedia':
            names, context = malpedia_pipeline(threat_actors)
            return names, [], context
        elif source_name.lower() == 'oneti':
            names, links, context = oneti_pipeline(threat_actors, oneti_token)
            return names, links, context
    
if __name__ == '__main__':
    text = """
'Not specified    """
    # url = "https://gbhackers.com/eagerbee-malware"
    # text = click_into_page_with_browser(url, is_text=True)
    # print(text)
    actors = get_actor(text)            
    print(actors)
    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)

    actors = eval(actors)
    if actors and 'None' not in actors:
        actors = actors[:5]
        name, context = pipeline(actors, 'oneti', token)
        print(context)
        print(name)
    else:
        print(000)

    # client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    # scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    # token = get_access_token(client_id, scopes)

    # threat_actors = ['Forest Blizzard', 'Amethyst Rain']
    # name, context = pipeline(threat_actors, 'oneti', token)
    # actors = ", ".join(threat_actors)
    # print(f"Actors: {actors}\n")
    # print(context)


    # file = os.path.join(os.path.dirname(__file__), '..', '241112_AgentReport', 'hamas-linked-threat-group-expands-espionage-and-destructive-operations.md')
    # file = "AgentGenReport/1119/chinese-hackers-exploit-fortinet-vpn-zero-day-to-steal-credentials1.md"
    # threat_actor_info = extract_threat_actor_info(file)

    # threat_actors = eval(get_actor(threat_actor_info))
    # output = ""
    # sources = ['malpedia', 'oneti']
    # for source in sources:
        # output += f"======================== {source} ========================\n"
        # context = pipeline(threat_actors, source, oneti_token=token)
        # output += str(context)
        # output += f"\n======================== {source} ========================\n"

    # print (f"\n\n\n{output}")    
