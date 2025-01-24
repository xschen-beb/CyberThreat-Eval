import sys
import os

parent_directory = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_directory)

from playwright.sync_api import sync_playwright
from search_engine import click_into_page_with_browser
import os
from openai import AzureOpenAI
from tenacity import retry, stop_after_attempt, wait_random_exponential
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from bs4 import BeautifulSoup
import re
import json

os.environ["LOCAL_ENDPOINT"] = "http://10.150.142.182:9999"
os.environ["PROXY_KEY"] = "59ddb6820482b719e33661ccbfa98042"

client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)

def extract_threat_actor_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        # Retry with 'latin-1' encoding as a fallback
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                content = file.read()
        except Exception as e:
            print(f"Failed to read file {file_path} with fallback encoding: {e}")
            return None

    match = re.search(r"#### Threat actor/group/campaign\s*(.*?)(?=\n####|\Z)", content, re.DOTALL)
    return match.group(1).strip() if match else None


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def api_call(messages, temperature, model="gpt-4o", json_enabled=True):
    if model == 'gpt-4-32k':
        return client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            max_tokens=512,
        )
    if json_enabled:
        return client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            response_format={"type": "json_object"},
            max_tokens=512,
        )
    else:
        return client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            max_tokens=512,
        )


# def get_actor(file):
# input: the contexts containing threat actors
# output: list of threat actors
def get_actor(threat_actor):
    # threat_actor = extract_threat_actor_info(file)
    sys_prompt = f"""
    ### Task description:
    You are an expert in cybersecurity. I will provide you with an IoC report. Please extract the relevant and potential threat actors (if it has other names, extract them.) in the list format from the "threat actor" section of the report and ensure that the extracted term is suitable for use in a search query. For each output, it should be a phrase or a single word without any prefixes. If no threat actor is specified, the output should be ['None'].

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
    I will provide you with an IoC report. Please extract the relevant and potential threat actors(if it has other names, extract them.) in the list format from the "threat actor" section of the report and ensure that the extracted term is suitable for use in a search query. For each item of the list, it should be a phrase or a single word without any prefixes. If no threat actor is specified, the output should be ['None'].
    ### Result:
    Report Content: {threat_actor}
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(new_messages, temperature=0.01, model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response


def check_page_not_found(actor_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(actor_url, wait_until="domcontentloaded")
            page_content = page.content()
            if "Page not Found" in page_content:
                return True
            return False
        except Exception as e:
            print(f"Error while loading {actor_url}: {e}")
            return True
        finally:
            browser.close()


def extract_relevant_section(actor_info, keyword):
    sys_prompt = f"""
    ### Task description:
    I will provide you with text from a threat actor's page. Your task is to find the part of the text that is most relevant to the given keyword and extract it. The extracted part should contain detailed information related to the keyword.

    ### Result:
    Keyword: {keyword}
    Text: {actor_info}

    ### Extracted relevant section:
    """

    user_prompt = f"""
    ### Task description:
    Please provide the part of the text that is most relevant to the keyword '{keyword}'.

    ### Result:
    Text: {actor_info}
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(new_messages, temperature=0.01, model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response


def save_actor_info(actor, actor_info, keyword):
    relevant_section = extract_relevant_section(actor_info, keyword)
    file_name = f"actor_info_{actor.replace(' ', '_').lower()}_relevant.txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(relevant_section)
    print(f"Saved relevant actor information for {actor} to {file_name}")
    return relevant_section


def augment_threat_actor_context(threat_actor, actor_info):
    sys_prompt = f"""
    ### Task description:
    You are an expert in cybersecurity. Based on the extracted information about the threat actor from an IoC report, please generate a detailed context and summary about this threat actor based on report context given and your knowledge. No hallucination is allowed. Your context should be brief. This will be used to enhance the description of the threat actor in the report. Make sure the context provides enough details for a security professional to understand the actor's profile and their behaviors.

    ### Example:
    Threat Actor: BrazenBamboo
    Context: BrazenBamboo is a Chinese state-affiliated APT group. It is responsible for various attacks targeting government entities, private companies, and critical infrastructure worldwide. The group utilizes sophisticated malware such as DEEPDATA and DEEPPOST to exploit vulnerabilities in both Windows and macOS systems. They are known to use advanced techniques like spear-phishing and zero-day vulnerabilities to achieve their objectives. In the past, they have targeted industries such as telecommunications, finance, and energy.

    Threat Actor: Earth Estries
    Context: Earth Estries, also known as Salt Typhoon, is a Chinese cyber espionage group primarily focused on targeting the technology sector and governmental entities in Western countries. They are known to overlap with other APT groups such as FamousSparrow and UNC4841. Their primary modus operandi includes spear-phishing emails with malicious attachments, web shell exploitation, and using remote access tools (RATs) to gain unauthorized access to target networks.
    """

    user_prompt = f"""
    ### Task description:
    Based on the extracted information about the threat actor from an IoC report, please briefly generate a detailed context and summary about this threat actor based on report context given and your knowledge. No hallucination is allowed. This will be used to enhance the description of the threat actor in the report.

    ### Result:
    Threat Actor: {threat_actor}
    Report Content: {actor_info}
    Context:
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(new_messages, temperature=0.01, model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response


def pipeline(file):
    actors = eval(get_actor(file))
    print(actors)

    actors_info = ""

    for actor in actors:
        if actor:
            print(f"Extracted Threat Actor: {actor}")
            actor_url = f"https://malpedia.caad.fkie.fraunhofer.de/actor/{actor.replace(' ', '-').lower()}"
            if check_page_not_found(actor_url):
                print(f"Actor {actor} not found, skipping.")
            else:
                actor_info = click_into_page_with_browser(actor_url)
                actors_info += actor_info
                print(f"Actor Information: {actor_info}")
        else:
            print("Failed to extract Threat Actor.")

    relevent_section = save_actor_info(actor, actor_info, actor)
    context = augment_threat_actor_context(actors, relevent_section)
    print(context)
    fo = open('wirte_selected_context.txt', 'w')
    fo.write(context)
    context = augment_threat_actor_context(actors, actor_info)
    print(context)
    fo = open('wirte_not_selected_context.txt', 'w')
    fo.write(context)

"""
def malpedia_pipeline(actors):
    actors_info = ""

    for actor in actors:
        if 'None' not in actor:
            print(f"Extracted Threat Actor: {actor}")
            actor_url = f"https://malpedia.caad.fkie.fraunhofer.de/actor/{actor.replace(' ', '-').lower()}"
            if check_page_not_found(actor_url):
                print(f"Actor {actor} not found, skipping.")
                continue
            else:
                actor_info = click_into_page_with_browser(actor_url)
                actors_info += actor_info
                print(f"Actor Information: {actor_info}")
        else:
            print("Failed to extract Threat Actor.")
            actor_info = ""

    if actors_info:
        relevent_section = save_actor_info(actor, actors_info, actor)
        context = augment_threat_actor_context(actors, relevent_section)
    else:
        print("No external actor information available to process.")
        relevent_section = ""
        # context = augment_threat_actor_context(actors, relevent_section)
        context = ""

    return context

"""
if __name__ == '__main__':
    # file = os.path.join(os.path.dirname(__file__), '..', '241112_AgentReport', 'hamas-linked-threat-group-expands-espionage-and-destructive-operations.md')
    # threat_actor_info = extract_threat_actor_info(file)
    # print(threat_actor_info)
    # threat_actors = eval(get_actor(threat_actor_info))
    threat_actors = ['UAC-0194']
    # context = malpedia_pipeline(threat_actors)
    # print(context)
    # pipeline(file)
