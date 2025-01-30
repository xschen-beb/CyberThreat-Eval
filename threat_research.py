import json
import sys
import os
import logging
import requests
import base64
import re
import tiktoken
# for exponential backoff
import tenacity
import ast
from tenacity import (retry, stop_after_attempt, wait_random_exponential)
from rich.console import Console
from rich.markdown import Markdown
from rich.align import Align
import playwright
from urllib.parse import urlparse
from datetime import datetime
from run_new_prompts import sys_prompt, user_prompt
from mdti_description.crawl_oneti import get_access_token
from mdti_description.mdti_pipeline import pipeline, get_actor
from mdti_description.mdti_pipeline import get_articles, get_profiles
from get_root_cause import root_cause_pipeline, get_root_cause_with_llm
from get_detection import mdti_detection_pipeline
from filter_similar_articles import *
from recommendations.utils import *
from htmldate import find_date
import csv
import io
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# from dotenv import load_dotenv
# load_dotenv()

# for exponential backoff
from tenacity import retry, stop_after_attempt, wait_random_exponential
from search_engine import (
    google_web_search,
    click_into_page,
    click_into_page_original,
    click_into_page_with_browser,
    bing_search,
)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# LOCAL_ENDPOINT = ""
# PROXY_KEY = ""
# CASSIE = ""
pat = os.getenv('ADO_PERSONAL_ACCESS_TOKEN')

VT_API_KEY = os.getenv("VT_API_KEY")
URL = 'https://www.virustotal.com/api/v3/'
HEADERS = {
    'x-apikey': VT_API_KEY
}

# ANSI escape codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"


_AUTH_SCOPE = "https://cognitiveservices.azure.com/.default"
_CREDENTIAL = DefaultAzureCredential()

_DEPLOYMENT_ENV = "local"
_LOG_ENABLED = True
_SEARCH_ENGINE = "google"
_HEADLESS_FLAG = False

total_llm_call = 0
total_tokens = 0

# os.environ["LOCAL_ENDPOINT"] = LOCAL_ENDPOINT
# os.environ["PROXY_KEY"] = PROXY_KEY
# os.environ['ADO_PERSONAL_ACCESS_TOKEN'] = CASSIE
# pat = os.environ['ADO_PERSONAL_ACCESS_TOKEN']

if _DEPLOYMENT_ENV == "local":
    client = AzureOpenAI(
        azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
        api_key=os.getenv("PROXY_KEY"),
        api_version="2024-05-01-preview",
    )
    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)


if _DEPLOYMENT_ENV == "playground":
    client = AzureOpenAI(
        azure_endpoint="https://riqds-openai-test.openai.azure.com",
        azure_ad_token_provider=get_bearer_token_provider(_CREDENTIAL, _AUTH_SCOPE),
        api_version="2024-05-01-preview",
    )


def debug_print(*args, **kwargs):
    if _LOG_ENABLED:
        message = ' '.join(str(arg) for arg in args)
        logging.debug(message)
        print(*args, **kwargs) 
    else:
        pass


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def api_call(messages, func_list, model= "gpt-4o", json_enabled=True):
    global total_llm_call
    global total_tokens
    total_llm_call += 1
    total_tokens += num_tokens_from_string(str(messages), model)
    debug_print(RED + "==> Total LLM Calls: " + RESET, total_llm_call)
    debug_print(RED + "==> Total Tokens: " + RESET, total_tokens)

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


def categorize(blog):
    debug_print(
        RED
        + "==> Categorizing the blog (identify if it is news or technical report)."
        + RESET
    )
    category_prompt = f"""
        I will give you a blog. Please analyze this report to identify if this blog has enough info to help people understand the root cause (including, vulnerable/misconfigured services, how to mitigate) behind the incident.
        Your output should be json format with 'is_enough' and 'explanation' as the keys. DO NOT add ```json at the beginning and ``` and the end.
        """
    messages = [
        {"role": "system", "content": category_prompt},
    ]

    question = f"Here is the blog: {blog}."
    messages.append({"role": "user", "content": question})

    response_message = api_call(messages, [])
    debug_print(response_message.choices[0].message.content)
    decision = json.loads(response_message.choices[0].message.content)
    if decision["is_enough"]:
        debug_print(
            RED
            + "This blog has enough info to help people understand the root cause behind the incident."
            + RESET
        )
        return True
    else:
        debug_print(
            RED
            + "This blog does not have enough info to help people understand the root cause behind the incident."
            + RESET
        )
        return False


def compare_docs(original, new_doc):
    if num_tokens_from_string(new_doc, "gpt-4o") > 120000:
        new_doc = new_doc[:80000]

    content_analysis_prompt = f"""
    You are a security expert. I will give you a original blog and a new found document. You goal is to step-by-step identify if the new found document described the same incident comapred to the original blog (i.e. talking the same thing with different aspects). First, identify if the new found document described a similar incident. 
    Then, please analyze the new found document to identify if it has enough info to help people understand the root cause (including, vulnerable/misconfigured services, how to mitigate) bechind the incident. If a doc has some IoCs related to this incident, we identify it as enough.
    Note that if a new found document covers a few different incidents, we called it a cyber-intel-brief, mark it as not the same incident.
    Please output your decision in JSON format with the key "is_same", "is_similar" or "is_enough" and "explanation". 
    The original blog is: {original}
    The new found document is: {new_doc}
    """
    # before second paragraph, including malware tools including ...
    # if doc have ioc, 
    new_messages = []
    new_messages.append({"role": "user", "content": content_analysis_prompt})

    response_message = api_call(new_messages, [])
    # debug_print(response_message)
    debug_print(
        RED + "LLM's Analysis (Relevant and enough) " + RESET,
        [response_message.choices[0].message.content],
    )

    info = json.loads(response_message.choices[0].message.content)
    return info


def find_related_ones(blog, enable_query=True):
    debug_print(RED + "==> Find more related documents." + RESET)

    # Step 1: Ask the model to generate search queries and to extract links
    sys_prompt = """
    You are a security expert. I will give a report on the Internet. I want to delve deeper into this incident to see what the reason behind and tech details. Can you sugggest a search query (including threat actor, malware,CVE, date, service or victims) that I can use to search in the search engine to understand the tech details of this attack/incident. Do not include general words like "cybersecurity", "personal information", etc because they are too general to search. You can use the threat actor name, malware name, victims, CVEs, or similar attack chain.
    You output should be json format with queries the key. Please also provide the links that described the same incident, CVE or links that may include IoCs (e.g., The indicators of compromise for this blog entry can be found <a href="https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/a/a-look-into-pikabot-spam-wave-campaign/ioc-pikabot-spam-campaign.txt"> here </a>) mentioned in the blog with the key "links". Output format: {"queries": ["query1", "query2"], "links": ["link1", "link2"]}
    """
    # output format add {"malware": "tools"} -> malpedia -> info -> thread_core
    # If you wan to include specific words in the results, please use double quotes.
    messages = [
        {"role": "system", "content": sys_prompt},
    ]
    if num_tokens_from_string(blog["blog"], "gpt-4o") > 120000:
        blog["blog"] = blog["blog"][:80000]
    misconf_qeustion = f"Here is the blog: {blog['blog']}."
    debug_print(RED + "==> Orginal html: " + RESET)
    debug_print(blog["blog"][0:2000])
    
    messages.append({"role": "user", "content": misconf_qeustion})
    response_message = api_call(messages, [])
    info = json.loads(response_message.choices[0].message.content)
    messages.append(
        {"role": "assistant", "content": response_message.choices[0].message.content}
    )

    queries = info["queries"]
    debug_print(RED + "Get Candidate Queries and Links: " + RESET)
    debug_print("queries: ", queries)
    links = info["links"]
    debug_print("links: ", links)

    # Step 2: Click into the links to get the content
    debug_print(RED + "==> Click into the some links to get the content." + RESET)
    all_related_docs = []

    identified_links = []
    identified_links.append(blog["link"])
    all_related_docs.append(
        {"link": blog["link"], "blog": blog["blog"], "is_same": True, "is_enough": True}
    )

    for link in links:
        debug_print(RED + "Delve into the link: " + RESET, link)
        if link in identified_links:
            debug_print("==> The link has been identified. Skip it.")
            continue
        if link.endswith(".png"):
            continue
        identified_links.append(link)

        for i in range(3):
            try:
                page_content = click_into_page_with_browser(link, headless_flag=_HEADLESS_FLAG)
                debug_print(RED + "Crawled page content: " + RESET, [page_content[0:4000]])
                info = compare_docs(blog["blog"], page_content)
                # if info["is_same"] in [True, "True", "true"] and info["is_enough"] in [True, "True", "true", 'yes']:
                if info["is_same"] in [True, "True", "true"]:
                    all_related_docs.append(
                        {
                            "link": link,
                            "blog": page_content,
                            "is_same": info["is_same"],
                            "is_enough": info["is_enough"],
                        }
                    )
                else:
                    debug_print(
                        RED + "==> Not the same incident (not same, crawling bloked)." + RESET,
                        link,
                    page_content[:200],
                )
                break
            except KeyError:
                debug_print("==> Error in parsing the response.")
                continue
            except playwright._impl._errors.Error:
                debug_print("==> Invalid URL.")
                break

    # Step 3: Search the candidate queries and select related docs
    debug_print("==> All Identfied Links: ", identified_links)

    # New dig deeper
    # new = dig_deeper(blog["blog"], identified_links)
    # debug_print("New identified blog: ", new["link"])
    # identified_links.append(new["link"])
    # all_related_docs.append(new)

    if not enable_query:
        return all_related_docs

    for query in queries[:3]:
        debug_print(RED + "Delve into the query: " + RESET, query)
        debug_print(RED + "LLM Decision: " + RESET, "Google Query -> : ", query)
        if _SEARCH_ENGINE == "bing":
            google_search_results = bing_search(query)
            debug_print(RED + "Bing Search Results: " + RESET, google_search_results)
        if _SEARCH_ENGINE == "google":
            # google_search_results = google_web_search(query + ' "details"')
            google_search_results = google_web_search(query)
            debug_print(RED + "Google Search Results: " + RESET, google_search_results)
        # google_search_results = google_web_search(query + ' "What we know about"')

        results_filtering_prompt = f"""
        You are a security expert. I will give the google search results and the original blog.
        You goal is to provide the top 2 links that you think are most relevant to the incident blog. But should not include in {identified_links}.  It can help understand the root cause (including, vulnerable/misconfigured services, how to mitigate). Your output should be JSON format with `urls` as the key and the value is a list (length 2) of urls.

        This is the google search results. {str(google_search_results)} 
        This is the original blog: {blog['blog']}.
        """
        select_messages = [{"role": "user", "content": results_filtering_prompt}]
        response_message = api_call(select_messages, [])

        debug_print(
            RED + "LLM selected links: " + RESET,
            response_message.choices[0].message.content,
        )
        info = json.loads(response_message.choices[0].message.content)
        links = info["urls"]
        for link in links:
            if link in identified_links:
                continue
            identified_links.append(link)
            debug_print(RED + "Delve into the link: " + RESET, link)
            # debug_print(RED + "New Selected Link: " + RESET, link)
            try:
                page_content = click_into_page_with_browser(
                    link, headless_flag=_HEADLESS_FLAG
                )
            except:
                debug_print(RED + "==> Crawling blocked." + RESET)
                page_content = "Crawling blocked."

            debug_print(RED + "Crawled page content: " + RESET, [page_content[0:4000]])

            for i in range(3):
                try:
                    info = compare_docs(blog["blog"], page_content[0:10000])
                    # if info["is_same"] in [True, "True", "true"] and info["is_enough"] in [True, "True", "true", 'yes']:
                    if info["is_same"] in [True, "True", "true"]:
                        all_related_docs.append(
                            {
                                "link": link,
                                "blog": page_content,
                                "is_same": True,
                                "is_enough": info["is_enough"],
                            }
                        )
                        break 
                except KeyError:
                    debug_print("==> Error in parsing the response.")
                    continue

    debug_print(RED + "==> New found related documents: " + RESET)
    for doc in all_related_docs:
        debug_print(doc["link"], doc["is_same"], doc["is_enough"], [doc["blog"][:200]])
    return all_related_docs


def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string, disallowed_special=()))
    return num_tokens

def parse_original_text_to_json(text):
    # Define a dictionary to store parsed data
    result = {
        "Incident": "Not specified",
        "Root cause": "Not specified",
        "Threat actor/group/campaign": "Not specified",
        "Organization/industry/location": "Not specified",
        "Start date – End date": "Not specified",
        "MITRE TTPs": [],
        "Impact": "Not specified",
        "Mitigation Steps": [],
        "Detection Signature": "Not specified",
        "IoCs": "No IoCs found"
    }

    # Extract each section using regex or simple splitting
    patterns = {
        "Incident": r"(?<=Incident:)(.*?)(?=\n|$)",
        "Root cause": r"(?<=Root cause:)(.*?)(?=\n|$)",
        "Threat actor/group/campaign": r"(?<=Threat actor/group/campaign:)(.*?)(?=\n|$)",
        "Organization/industry/location": r"(?<=Organization/industry/location:)(.*?)(?=\n|$)",
        "Start date – End date": r"(?<=Start date – End date:)(.*?)(?=\n|$)",
        "Impact": r"(?<=Impact:)(.*?)(?=\n|$)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            result[key] = match.group(1).strip()

    # Extract Mitigation Steps
    mitigation_pattern = r"(?<=Mitigation Steps:)(.*?)(?=\n(?:Detection Signature|IoCs|$))"
    mitigation_match = re.search(mitigation_pattern, text, re.DOTALL)
    if mitigation_match:
        steps = [step.strip("- ").strip() for step in mitigation_match.group(1).strip().split("\n") if step.strip()]
        result["Mitigation Steps"] = steps

    # Extract Detection Signature
    detection_pattern = r"(?<=Detection Signature:)(.*?)(?=\n(?:IoCs|$))"
    detection_match = re.search(detection_pattern, text, re.DOTALL)
    if detection_match:
        signature_text = detection_match.group(1).strip()
        service_match = re.search(r"Service:\s*(.*?)(?=\n|$)", signature_text)
        port_match = re.search(r"Port:\s*(.*?)(?=\n|$)", signature_text)
        severity_match = re.search(r"Severity:\s*(.*?)(?=\n|$)", signature_text)
        incident_match = re.search(r"Incident:\s*(.*?)(?=\n|$)", signature_text)
        signature_name_match = re.search(r"Signature name:\s*(.*?)(?=\n|$)", signature_text)

        internal_checks = {}
        external_scanning = {}

        internal_pattern = re.compile(r"-\s*(Setting\d+):\s*(.*?)(?=\n|$)")
        external_pattern = re.compile(r"-\s*(Port|Check for known vulnerabilities):\s*(.*?)(?=\n|$)")

        for match in internal_pattern.finditer(signature_text):
            internal_checks[match.group(1)] = match.group(2).strip()

        for match in external_pattern.finditer(signature_text):
            external_scanning[match.group(1)] = match.group(2).strip()

        result["Detection Signature"] = {
            "Service": service_match.group(1).strip() if service_match else "Not available",
            "Port": port_match.group(1).strip() if port_match else "Not available",
            "Severity": severity_match.group(1).strip() if severity_match else "Not available",
            "Incident": incident_match.group(1).strip() if incident_match else "Not available",
            "Signature name": signature_name_match.group(1).strip() if signature_name_match else "Not available",
            "Internal checks": internal_checks,
            "External scanning": external_scanning
        }

    # Extract MITRE TTPs with line merging
    mitre_pattern = r"(?<=MITRE TTPs:)(.*?)(?=\n(?:Impact|$))"
    mitre_match = re.search(mitre_pattern, text, re.DOTALL)

    if mitre_match:
        print("MITRE TTPs Section Found!")  # Debugging: Confirm section is found
        
        # Split the section into lines and merge justification lines with TTP lines
        mitre_ttp_lines = [line.strip("- ").strip() for line in mitre_match.group(1).strip().split("\n") if line.strip()]
        print("Original Lines for TTPs:", mitre_ttp_lines)  # Debugging: Log original lines

        # Merge TTP lines with their justification
        merged_lines = []
        temp_line = ""
        for line in mitre_ttp_lines:
            if line.startswith("T"):  # New TTP line
                if temp_line:  # Append the previous complete TTP entry
                    merged_lines.append(temp_line.strip())
                temp_line = line  # Start a new TTP entry
            else:  # Justification line
                temp_line += " " + line  # Append justification to the current TTP entry
        if temp_line:  # Add the last entry
            merged_lines.append(temp_line.strip())
        
        print("Merged Lines for TTPs:", merged_lines)  # Debugging: Log merged lines

        # Parse the merged TTP entries
        ttp_dict = {}
        for line in merged_lines:
            print("Processing Line:", line)  # Debugging: Log each line
            segments = line.split(". Justification: ")  # Split description and justification
            if len(segments) == 2:
                ttp_match = re.match(
                    r"^(T\d+\.\d+|T\d+):\s*(.*?),\s*Confidence:\s*(.*?)$", segments[0], re.IGNORECASE
                )
                if ttp_match:
                    ttp_id = ttp_match.group(1)  # Matches TTP ID (e.g., T1071.001 or T1071)
                    description = ttp_match.group(2)  # Matches the description (e.g., Application Layer Protocol: Web Protocols)
                    confidence = ttp_match.group(3)  # Matches the confidence level (e.g., High)
                    justification = segments[1]  # Matches justification part after split

                    # Add to the TTP dictionary
                    ttp_dict[ttp_id] = f"{description}, Confidence: {confidence}. Justification: {justification}"
                    print(f"Added TTP: {ttp_id}, Description: {description}")  # Debugging: Confirm addition
                else:
                    print(f"Failed to parse TTP line: {line}")
            else:
                print(f"Failed to split Justification: {line}")

        # Add the TTP dictionary to the result
        result["MITRE TTPs"] = ttp_dict

    else:
        print("No MITRE TTPs section found in the text.")  # Debugging: Confirm absence


    # Extract IoCs (if provided)
    iocs_pattern = r"(?<=IoCs:)(.*?)(?=$)"
    iocs_match = re.search(iocs_pattern, text, re.DOTALL)
    if iocs_match:
        iocs_text = iocs_match.group(1).strip()
        if iocs_text.lower() != "no iocs found":
            iocs_list = [ioc.strip() for ioc in iocs_text.split("\n") if ioc.strip()]
            result["IoCs"] = iocs_list

    return result


def enrichment(original, related_docs):
    debug_print(RED + "==> Starting Enrichment: " + RESET)
    if len(related_docs) == 1:
        original = parse_original_text_to_json(original)
        return original
    for doc in related_docs[1:]:
        '''
        analysis_prompt = """
        You are a top-notch expert in cybersecurity. I will give a threat report and a new found document. You goal is to see if we can add some new info to the report based on new found documents. Please merge the new info into original and mark for your changes in the enhanced report and and cite the new found doc with the following format: [*The new information*](link to new found document). Ensure that the enhanced report is concise, entity-dense, and grammatically correct. For every new piece of information added, ensure the sentence remains complete and flows naturally.
        
        You will generate increasingly entity-dense threat report based on the new found document. Repeat the following 2 steps 2 times.
        Step 1: Identify 1-4 informative Entities (";" delimited) from the new found document which are missing from the previously generated threat report.
        Step 2: Write a new, denser threat report to merge every entity and detail from the previous summary plus the Missing Entities.

        A Missing Entity is: 
        - Relevant: to the main story.
        - Specific: descriptive yet concise (5 words or fewer)
        - Novel: not in the previous summary.
        - Faithful: present in the new found document.
        - Anywhere: located anywhere in the new found document.
        - Security-related: e.g., IoCs (MAKE SURE to add all IoCs("ip", "ip_port",  "domain", "url", "email", "hash_md5", "hash_sha256", "hash_sha1") you find in the new found document). Change the URL/IP/Domain format to a valid format with standard syntax, without the extra brackets or colons (e.g., change hxxp[:]//2[.]57[.]149[.]233[:]3366/ to http://2.57.149.233:3366/) 
        
        Guidelines:
        - Merge the new Entities into the original report naturally and seamlessly. Mark the new information with citation in the format: [*The new information*](link to new found document). Do not create a new key (e.g., 'Added info').
        - Ensure each new addition results in a grammatically correct and self-contained sentence. Paraphrase the original sentence as needed to accommodate the new information while preserving clarity and flow.
        - Citations must be placed in a way that complements the surrounding text, and in grammatically correct positions. 
        - Check sentence correctness by imagining the citation is a direct part of the text. For example:
            - **Incorrect**: "This allowed law enforcement to gain control of the server [*the server*](...)."
            - **Reason**: After inserting the citation, the resulting sentence becomes: "This allowed law enforcement to gain control of the server the server," which is not grammatically correct due to redundancy.
            - **Correct**: "The FBI's operation was facilitated by sinkholing the [*PlugX worm*](...), which [*cost $7*](...)."
            - **Reason**: After inserting the citation, the sentence remains complete and grammatically correct: "The FBI's operation was facilitated by sinkholing the PlugX worm, which cost $7."
        - Re-write the previous summary to improve flow and make space for additional entities, and must be grammatically correct.
        - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
        - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
        - Missing entities can appear anywhere in the new summary.
        - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.

        In addition to merging entities, MITRE TTPs output should be in the following format:
        {'T1078': 'Valid Accounts, Confidence: High. Justification: The threat actors used a stolen Remote Support SaaS API key to reset passwords for local application accounts, which aligns with the use of valid accounts to gain access.', 'T1190': 'Exploit Public-Facing Application, Confidence: High. Justification: ...', ...}

        Answer in JSON. it has two keys. One is "thoughts", which described you step-by step thinks. Another is 'final_report'.
        The final report should be in the following format:
        {
        "Incident": "XXXX",
        "Root cause": "XXXX",
        "MITRE TTPs": {'T1078': 'Valid Accounts, Confidence: High. Justification: The threat actors...'}
        "XXX": "XXX",
        }
        """
        '''
        analysis_prompt = """
        You are a top-notch expert in cybersecurity. I will give a threat report and a new found document. Your goal is to see if we can add some new info to the report based on the new found documents. Then, merge that new info into the original report and mark it in the enhanced report, citing the new found document with this format: [*The new information*](link to new found document). Ensure the enhanced report is concise, entity-dense, and grammatically correct. For every new piece of information added, ensure the sentence remains complete and flows naturally.

        You will generate an increasingly entity-dense threat report based on the new found document by repeating the following two steps twice:
        1. **Identify 1-4 informative Entities** (";" delimited) from the new found document that are missing from the previously generated threat report.
        2. **Write a new, denser threat report** to merge every entity and detail from the previous summary plus the Missing Entities.

        A "Missing Entity" is:
        - **Relevant**: must pertain to the main story.
        - **Specific**: descriptive yet concise (5 words or fewer).
        - **Novel**: not in the previous summary.
        - **Faithful**: must appear in the new found document.
        - **Anywhere**: can appear anywhere in the new found document.

        ### Guidelines:
        - Merge the new Entities into the original report **naturally and seamlessly**. Mark each new piece of information in the format `[*The new information*](link to new found document)`. **Do not** create a new key such as "Added info."
        - Ensure each new addition results in a grammatically correct and self-contained sentence. You may paraphrase the original sentence as needed to accommodate the new info while preserving clarity and flow.
        - **Critical**: The resulting sentence must remain coherent even if we remove the bracketed part. For example:
            - **Correct**: “The FBI's operation was facilitated by sinkholing the [*PlugX worm*](...), which [*cost $7*](...).”  
            - If we strip out `[*PlugX worm*](...)` and `[*cost $7*](...)`, the sentence still reads:  
                “The FBI's operation was facilitated by sinkholing the , which .”  
                That might not be perfectly grammatical due to punctuation, so in practice you’d ensure it’s written so that removing the bracketed sections still forms a valid sentence. For instance:
                “The FBI's operation was facilitated by sinkholing the PlugX worm, which cost $7.”
                This sentence remains grammatically correct with or without the bracket references.
            - **Incorrect**: “The FBI's operation was facilitated by sinkholing the [*the worm*](...).” → Removing the bracketed text yields a duplicate or incomplete phrase.
        - Re-write the previous summary to improve flow and create space for additional entities while keeping everything grammatically correct.  
        - Use fusion, compression, and removal of uninformative phrases like "the article discusses" to keep the text concise and self-contained.
        - Missing entities can appear anywhere in the new summary.
        - If new data doesn’t fit well, compress or paraphrase existing text to make room, but do not drop existing content.

        ### MITRE TTPs Format:
        - You **MUST** also output MITRE TTPs in this structure (as a Python-like dictionary):
        {'T1078': 'Valid Accounts, Confidence: High. Justification: The threat actors used a stolen ...', 'T1190': 'Exploit Public-Facing Application, Confidence: High. Justification: ...', ... }
        - Keep existing TTP entries from the previous summary intact.
        - If more than 10 TTPs appear in the previous summary plus newly found doc, you should keep the top 10 TTPs with the highest confidence.

        ### Final Output (JSON):
        You will output a single JSON with two keys:
        1. `"thoughts"`: A short step-by-step description of your reasoning.
        2. `"final_report"`: The revised threat summary in JSON. For example:
        { "Incident": "XXXX", "Root cause": "XXXX", "MITRE TTPs": { "T1078": "Valid Accounts, Confidence: High. Justification: ...", ... }, "Organization/industry/location": "...", ... }

        Make sure `"final_report"` is valid JSON. Avoid quoting code fences or adding extra text beyond this JSON structure.
        """

        # If the previous summary already has entity, do not convert it to 'Not specified' or alter it otherwise. Only add to or paraphrase what's already there.


        # if contains threat actors / malware, ..
        # New item: Threat actors: description

        # """
        # You will generate increasingly entity-dense threat report based on the new found document. Repeat the following 2 steps 2 times.

        # Step 1: Identify 1-4 informative Entities (";" delimited) from the new found  which are missing from the previously generated threat report.
        # Step 2: Write a new, denser threat report to merge every entity and detail from the previous summary plus the Missing Entities.

        # A Missing Entity is:
        # - Relevant: to the main story.
        # - Specific: descriptive yet concise (5 words or fewer).
        # - Novel: not in the previous summary.
        # - Faithful: present in the new found document.
        # - Anywhere: located anywhere in the new found document.

        # Guidelines:
        # - Merge the new Entities into the original report. Mark the new information with *Your changes* (link to new found document). Do not create a new key (e.g., 'Added info').
        # - re-write the previous summary to improve flow and make space for additional entities.
        # - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
        # - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
        # - Missing entities can appear anywhere in the new summary.
        # - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.
        # """

        messages = [
            {"role": "system", "content": analysis_prompt},
        ]

        misconf_qeustion = (
            f"The original report is: {original}. The new found document is: {doc}"
        )
        if num_tokens_from_string(misconf_qeustion, "gpt-4o") > 128000:
            misconf_qeustion = f"The original report is: {original}. The new found document is: {str(doc)[0:100000]}"

        debug_print(RED + "===> The new found document is: " + RESET, doc)
        messages.append({"role": "user", "content": misconf_qeustion})

        # response_message = api_call(messages, [], json_enabled=False)

        for i in range(3):
            try:
                response_message = api_call(messages, [], model='gpt-4o', json_enabled=True)
                debug_print(response_message.choices[0].message.content)
                json_response = json.loads(response_message.choices[0].message.content)
                original = json_response["final_report"]
                break
            except json.decoder.JSONDecodeError:
                debug_print("==> Error in parsing the response.")
                continue
            except KeyError:
                debug_print("==> Error in parsing the response.")
                continue
                # response_message = api_call(messages, [])
                # json_response = json.loads(response_message.choices[0].message.content)  

        debug_print(RED + "===> The enhanced report is: " + RESET)
        debug_print(response_message.choices[0].message.content)
        # console = Console()
        # md = Markdown(original)
        # aligned_md = Align.left(md)
        # console.debug_print(md)

    return original


def get_titles_processed():
    list_of_titles = []
    if not os.path.isfile(output_filename):
        return list_of_titles
    with open(output_filename, "r") as f:
        for line in f:
            info = json.loads(line)
            list_of_titles.append(info["title"])
    return list_of_titles


def threat_research_core(url):
    link = url
    try:
        blog = click_into_page_with_browser(
            link, is_text=False, headless_flag=_HEADLESS_FLAG
        )
    except playwright._impl._errors.Error:
        debug_print("==> Invalid URL.")
        return "", []
    
    debug_print(f"Blog: {blog[:2000]} ...........")

    # if not categorize(blog):
    #     # dig_deeper(blog)
    #     md_filename = "empty-output/"+info["title"]+".md"
    #     with open(md_filename,"w") as mdf:
    #         mdf.write(f"Source: [{info['url']}]({info['url']})\n\n")
    #         mdf.write("# "+info["title"] + "\n\n")
    #         mdf.write("This blog does not have enough info to help people understand the root cause behind the incident.")
    #         mdf.write("\n")
    #     fw.write(json.dumps(info) + "\n")
    #     fw.flush()
    #     continue
    debug_print(RED + "==> INPUT URLS: " + RESET, url)
    related_docs = find_related_ones({"link": url, "blog": blog})
    debug_print(RED + "==> Related doc numbers: " + RESET, len(related_docs))
    # for item in related_docs[2:]:
    #     new_doc = find_related_ones({"link": item["link"], "blog": item["blog"]}, enable_query=False)
    #     debug_print(RED + "==> Identified new Docs: " + RESET, new_doc)
    #     for doc in new_doc:
    #         debug_print(doc["link"], doc["is_same"], doc["is_enough"], [doc["blog"][:200]])
    #     related_docs.extend(new_doc)

    # IoCs Types
    # "ip",
    # "ip_port",
    # "domain",
    # "url",
    # "email",
    # "hash_md5",
    # "hash_sha256",
    # "hash_sha1",
    # "yaml",
    # "log-based IOC", 
    # "filaname and path"

    # Enhance the documents
    debug_print(RED + f"=> Enhance the blog: {url}" + RESET)
    #         **For IoCs, please also extract those (e,g., hash1, hash256, hash_md5) inside the Yara Rule into the IoCs. e.g., extract '"hash1/hash256/hash_md5": "65c6798eedd33aa36d77432b2ba7ef45dfe760092810b4db487210b19299bdcb"' from YARA rule and put it into IoCs **

    analysis_prompt = r"""
        You are a security expert. I will give a report/blog on the Internet. You need to analyze it to understand the root cause (including, vulnerable/misconfigured services), how to detect this problem, and the mitigation behind the incident. You **must not** include any Indicators of Compromise (IoCs), such as IP addresses, domains, emails, or file hashes, even if they appear in the source text. Do not mention any IoCs in any of the fields (Incident, Root cause, TTPs, Detection Signature, etc.). 

        You should provide a signature in the following format:    
        Incident: A brief and specific name of the incident (e.g., Shanghai Police Datalake Leak). 
        
        Root cause: The summarized detailed context of the root cause behind the incident including vulnerable/misconfigured services (e.g., Misconfigured Kibana instance). Focus on the most critical vulnerabilities or misconfigurations that led to the incident. Group similar issues and avoiding just listing all vulnerabilities. If no blog provides the info, output "Not specified". If there are hints or general observations in the article, use them to supplement your answer.
        
        Threat actor/group/campaign: The detailed context of Who carried out the attack? It could be an orgainzation, a malware family, etc (if known). If no actors are identified in the blog, output "Not specified". If the article provides partial information, include it, and summarize the answer. 
        
        Organization/industry/location: Who was targeted/victim? (if known) If no victim are specified in the blog, output "Not specified". If the article provides relevant information, include it, and summarize the answer briefly. 
        
        Start date – End date: When did the attack happen? (if known) If the blog does not mention it, output "Not specified". If the article provides relevant information, include it. 

        MITRE TTPs: Provide details on how the attack was carried out. Include a confidence score ('High', 'Medium', 'Low') for each identified TTP based on related articles and your understanding. Additionally, include a justification for each TTP identified from the article. The output format is:
        - T xx: Technique name, Confidence: xx.
        Justification: Provide a justification for why this TTP is identified based on the report/blog. For example, "This TTP was identified because the report mentions spearphishing emails with malicious links, which aligns with T1203: Phishing: Spearphishing Link."
        - T xx: Technique name, Confidence: xx.
        Justification: ...
        - ...

        Impact: If there's info on how many devices, records, organizations or other entities affected, summarize it. (e.g., 100,000 records leaked). If the article only provides approximate or partial info (e.g., “numerous systems were affected,” “several machines compromised,” “some data leaked”), summarize that phrasing concisely (e.g., “Several machines were compromised, but the exact number is unknown.”). If the impact is not provided in the context, output "Not specified". 
 
        Mitigation Steps: (How to protect myself?) e.g., Secure the Kibana instance with authentication credentials. and **Detailed Steps for mitigation** The output format is:
        - Secure the Kibana instance with authentication credentials. and **Detailed Steps for mitigation** (e.g., based on the article, the Kibana instance was found to be exposed with default settings. To mitigate this, configure strong password policies, implement multi-factor authentication, and restrict access by IP address to only trusted sources. Additionally, ensure that any unnecessary services are disabled to reduce the attack surface.)
        - ...
        
        Detection Signature: (How to detect? i.e., detection rules) The output should be in the following format:
            Service: Redis, CouchDB, etc. (it is a concrete service name, not general words like "database")  
            Port: 6379 (make it concrete if possible)   
            Severity: Critical
            Incident: XXX 
            Signature name: “Redis publicly accessible”    
            Internal checks (see next)    
                - Setting1: Redis port (6379) should not be exposed on external Internet. – In platform    
                - Setting2: Redis port (6379) should not listen on the external Internet – Inside VMs    
                - Setting3: Redis server should secure with authentication credentials. – Inside VMs    
            External scanning (see next)    
                - Port (6379) open
                - Redis no-pass-login
    """   
        # IoCs: How do I know I am affected? (for example, IP, domain, email, sha1, sha256, hash1, hash256, hash_md5, url, etc). If the document does not have IoCs, please output "No IoCs found". If the document has IoCs, please MAKE SURE to list top 10 IoCs (IF HAVE) you found in the document.  Change the URL/IP/Domain format to a valid format with standard syntax, without the extra brackets or colons (e.g., change hxxp[:]//2[.]57[.]149[.]233[:]3366/ to http://2.57.149.233:3366/)
        # The IoCs should be a in the following format strictly:
        # '[{"type":"hash_md5","value":"3edcde37dcecb1b5a70b727ea36521de","source": "https://www.wheretheiocfrom.com/XX/XXXX/"},{"type":"url","value":"http:\/\/50.19.48.59:82\/me1.bat","source": "https://www.wheretheiocfrom.com/XX/XXXX/"}]'
        # The type can be "ip", "ip_port",  "domain", "url", "email", "hash_md5", "hash_sha256", "hash_sha1".
    
    ## description about the malware...
    ## Add confidence / source


    messages = [
        {"role": "system", "content": analysis_prompt},
    ]

    misconf_qeustion = f"Here is the blog: {blog}." # Additional info about thread actor from malpedia(others)
    messages.append({"role": "user", "content": misconf_qeustion})
    response_message = api_call(messages, [], json_enabled=False)
    original = response_message.choices[0].message.content

    debug_print(RED + "==> The first enhanced one: " + RESET, original)
    debug_print(RED + "==> Related doc numbers: " + RESET, len(related_docs))

    # merge related doc together to ehnchace the density
    new_ti = enrichment(original, related_docs)

    return new_ti, related_docs


def standardize_url(url):
    parsed = urlparse(url)
    # Remove trailing slash and reconstruct the URL
    return parsed._replace(path=parsed.path.rstrip("/")).geturl()


def format_iocs_markdown(iocs):
    formatted_iocs = []
    for ioc in iocs:
        try:
            ioc_type = ioc.get("type", "unknown")
            ioc_value = ioc.get("value", "unknown")
            ioc_source = ioc.get("source", "unknown")
            formatted_iocs.append(f"- {ioc_type}: {ioc_value} ([link]({ioc_source}))")
        except Exception:
            formatted_iocs.append(f"- Invalid IoC format: {str(ioc)}")
    return "\n".join(formatted_iocs)

def format_iocs_excel(iocs):
    formatted_iocs = []
    for ioc in iocs:
        try:
            ioc_type = ioc.get("type", "unknown")
            ioc_value = ioc.get("value", "unknown")
            ioc_source = ioc.get("source", "unknown")
            formatted_iocs.append(f"{ioc_type}\t{ioc_value}\t{ioc_source}")
        except Exception:
            formatted_iocs.append(f"Invalid\t{str(ioc)}\t")
    return "\n".join(formatted_iocs)


def extract_iocs_from_text(blog, url):

    user = f"""
    # Task

    Parse the article below according to the task description above.

    <article>
    {blog}
    </article>

    Response:
    """
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user}
    ]
    # misconf_qeustion = f"Here is the blog: {blog}."
    # messages.append({"role": "user", "content": misconf_qeustion})

    
    try:
        response = api_call(messages, [], json_enabled=False)
        original = response.choices[0].message.content
        return extract_iocs(original, url)
    except Exception as e:
        print(f"Failed to get response for IoC extraction: {e}")
        return []


def extract_iocs(iocs_text, url):
    iocs_content = re.search(r"<IOCS>\s*\[START\](.*?)\[END\]\s*</IOCS>", iocs_text, re.DOTALL)
    if not iocs_content:
        return []

    iocs_content = iocs_content.group(1).strip()
    iocs_lines = iocs_content.splitlines()
    
    iocs_list = []

    for line in iocs_lines:
        line = line.strip()
        if line:
            ioc_match = re.match(r"\|(\w+)\|(.+)", line)
            if ioc_match:
                ioc_type = ioc_match.group(1)
                values = ioc_match.group(2).split(", ")
                for value in values:
                    clean_value = value.replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https")
                    clean_value = re.sub(r'\[://\]', '://', clean_value)
                    if '|' in str(clean_value):
                        clean_value = clean_value.strip('|')
                    iocs_list.append({"type": ioc_type, "value": clean_value, "source": url})

    return iocs_list


def encode_url(url):
    url_bytes = url.encode("utf-8")
    base64_bytes = base64.urlsafe_b64encode(url_bytes)
    base64_string = base64_bytes.decode("utf-8").rstrip("=")
    return base64_string


def check_ioc(ioc_value, ioc_type):
    try:
        if ioc_type == 'domain':
            url = f"{URL}domains/{ioc_value}"
        elif ioc_type == 'ip':
            url = f"{URL}ip_addresses/{ioc_value}"
        elif ioc_type == 'url':
            submit_url = f"{URL}urls"
            data = {"url": ioc_value}
            response = requests.post(submit_url, headers=HEADERS, data=data)
            response.raise_for_status()
            encoded_url = encode_url(ioc_value)
            url = f"{URL}urls/{encoded_url}"
        elif ioc_type == 'hash':
            url = f"{URL}files/{ioc_value}"
        elif ioc_type == 'email':
            url = f"{URL}emails/{ioc_value}"
        else:
            raise ValueError("Unsupported IOC type")

        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  
        if 'data' in response.json():
            data = response.json()['data']
            if data['attributes']['last_analysis_stats']['malicious'] > 0:
                return True
            else:
                return False
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking IoC {ioc_value}: {e}")
        # return True
        # return "Error Information"
        return None


def llm_judgment_for_ioc_in_blog(ioc_value, original_text): 
    sys_prompt = f"""
    ### Role Description
    You are an expert in cybersecurity. Given the original text below, determine whether the IoC '{ioc_value}' appears in full form in the text, without any modifications or obfuscations. The IoC might be written with markers or characters like '[.]', 'hXXp', 'hXXps', etc., which are commonly used to obfuscate the actual value. No hallucination is allowed.

    ### Task description
    1. Search for any occurrence of '{ioc_value}' in the original text.
    2. If you find the IoC, check if it is surrounded by any obfuscations (such as '[.]', 'hXXp', etc.).
    3. If there are obfuscations, remove them to restore the original IoC.
    4. If the restored IoC matches the original IoC '{ioc_value}' in the text, return True. Otherwise, return False.
    5. If the IoC does not appear at all or cannot be fully restored, return False.
    6. Answer with either 'True' or 'False' directly without any prefixes or explanations.

    ### Example
    IoC_value given: 147.45.44.83
    original text: 
    Indicators of Compromise
    260f06f0c6c1544afcdd9a380a114489ebdd041b846b68703158e207b7c983d6
    3317b8e19e19218e5a7c77a47a76f36e37319f383b314b30179b837e46c87c45
    0d03c7c6335e06c45dd810fba6c52cdb9eafe02111da897696b83811bff0be92
    604fa32b76dbe266da3979b7a49e3100301da56f0b58c13041ab5febe55354d2
    6be9c015c82645a448831d9dc8fcae4360228f76dff000953a76e3bf203d3ec8
    b1a351ee61443b8558934dca6b2fa9efb0a6d2d18bae61ace5a761596604dbfa
    147[.]45.44.83:6483
    185[.]196.9.26:6302
    True
    """

    user_prompt = f"""
    ### Task description
    Given ioc values, parse the original text below according to the task description above.

    IoC_value given: {ioc_value}
    original text:
    {original_text}
    """

    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
    misconf_qeustion = f"Here is the blog: {original_text}."
    messages.append({"role": "user", "content": misconf_qeustion})

    try:
        response = api_call(messages, [], json_enabled=False)
        original = response.choices[0].message.content
        return original
    except Exception as e:
        return False


def filter_url(url, url_list, excluded_domains=None):
    if excluded_domains == None:
        excluded_domains = []

    parsed_url = urlparse(url)
    base_domain = parsed_url.netloc.replace('www.', '')
    
    if any(excluded_domain in base_domain for excluded_domain in excluded_domains):
        return False
        
    for u in url_list:
        parsed_u = urlparse(u)
        base_u = parsed_u.netloc.replace('www.', '')
        if base_u == base_domain:
            return True
    
    return False


def filter_email(email, url_list, white_list=None):
    # Extract the domain part from the email
    email_domain = email.split('@')[1].lower()

    def normalize_domain(domain):
        """Normalize a domain by removing 'www.' and handling subdomains."""
        return domain.replace('www.', '').strip().lower()

    # Normalize email domain
    email_domain_parts = email_domain.split('.')

    # Compare email domain with each URL in the list
    for url in url_list:
        parsed_url = urlparse(url)
        url_domain = normalize_domain(parsed_url.netloc)

        # Check if email domain matches URL domain or subdomain
        if email_domain == url_domain:
            return True
        
        # Check if the root domain matches (ignoring TLD)
        url_root_domain = '.'.join(url_domain.split('.')[:-1])  # Remove TLD
        if email_domain.startswith(url_root_domain):
            return True
        
        if len(email_domain_parts) > 1 and len(url_domain.split('.')) > 1 and email_domain_parts[-2:] == url_domain.split('.')[-2:]:
            return True

    # Check white list for additional matches
    if white_list:
        for allowed_domain in white_list:
            allowed_domain_normalized = normalize_domain(allowed_domain)

            # Check if email domain matches the white list domain
            if email_domain == allowed_domain_normalized:
                return True
            
            # Check if the root domain matches (ignoring TLD)
            allowed_root_domain = '.'.join(allowed_domain_normalized.split('.')[:-1])  # Remove TLD
            if email_domain.startswith(allowed_root_domain):
                return True
            
            if len(email_domain_parts) > 1 and len(allowed_root_domain.split('.')) > 1 and email_domain_parts[-2:] == allowed_root_domain.split('.')[-2:]:
                return True

    return False


def get_white_list_urls(csv_file_path):
    root_urls = set()

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                feed_url = row.get('Feed Url')
                
                if feed_url:
                    parsed_url = urlparse(feed_url)
                    root_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    root_urls.add(root_url)  
                    
        return list(root_urls)
    
    except FileNotFoundError:
        print(f"Not find for path {csv_file_path}.")
        return []
    except Exception as e:
        print(f"Error in reading file: {e}")
        return []
    

def extract_meta_date(text):
    meta_date_patterns = [
        r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})T',
        r'"datePublished"\s*:\s*"([^"]+)"',
        r'<meta\s+property="article:published_time"\s+content="([^"]+)"',
        r'<meta\s+name="date"\s+content="([^"]+)"',
        r'<meta\s+name="publish_date"\s+content="([^"]+)"',
        r'<time\s+datetime="([^"]+)"',
        r'<time\s+class="[^"]*"\s+datetime="([^"]+)"'
    ]
    
    for pattern in meta_date_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            try:
                date_str = match.group(1)

                if 'T' in date_str:
                    date_str = date_str.split('T')[0]

                if ' ' in date_str:
                    date_str = date_str.split(' ')[0]
                
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                return date_obj.strftime('%Y-%m-%d')
            except (ValueError, IndexError):
                continue
    
    return None


def add_date(text):
    meta_date = extract_meta_date(text)
    if meta_date:
        return meta_date
    try:
        date = find_date(text)
        return date
    except Exception as e:
        print(f"Error in fallback date extraction: {e}")
        return None


def mdti_recommendation_pipeline(actors, token):
    recommendations = ""
    recommendation_headers = [
        "## Recommendations",
        "### Recommendations",
        "#### Recommendations",
        "## Recommendation",
        "### Recommendation",
        "#### Recommendation",
        "## RECOMMENDATIONS",
        "## RECOMMENDATION",
        "## Mitigations",
        "## MITIGATIONS",
        "## Mitigation",
        "## MITIGATION",
        "## Protection",
        "## PROTECTION",
        "## Defensive Guidance",
        "## Defense Recommendations"
    ]

    def find_recommendation_section(text):
        for header in recommendation_headers:
            start = text.find(header)
            if start != -1:
                content_start = start + len(header)
                
                next_section_markers = ["## ", "### ", "#### "]
                end = len(text)
                for marker in next_section_markers:
                    next_section = text.find(marker, content_start)
                    if next_section != -1 and next_section < end:
                        end = next_section
                
                recommendation_text = text[content_start:end].strip()
                if recommendation_text:
                    return recommendation_text
        return None

    links = []
    names = []
    for actor in actors:
        profiles = get_profiles(token.token, actor)
        articles = get_articles(token.token, actor)
        
        if profiles["data"]["totalPages"] > 0:
            names.append(actor)
            print("="*20 +" Using oneti profile " + "="*20 + '\n')
            for i in range(min(profiles['data']['totalPages'], 5)):
                text = profiles["data"]["content"][i]['description']
                name = profiles['data']['content'][0]['name']
                link = f"https://sip.security.microsoft.com/intel-profiles/{name}"
                links.append(link)
                rec_text = find_recommendation_section(text)
                # intro = f"Recommendation from link: {link} \n"
                intro = f"\n"
                if rec_text:
                    recommendations += intro + rec_text + "\n\n"

        else:
            continue
            print("="*20 +" Using related articles " + "="*20 + '\n')
            if articles["data"]["totalPages"] == 0:
                continue
            for i in range(min(articles['data']['totalPages'], 5)):
                text = str(articles["data"]["content"][i]['content'])
                rec_text = find_recommendation_section(text)
                if rec_text:
                    recommendations += rec_text + "\n\n"
    
    if recommendations:
        return names, links, recommendations
    else:
        return names, links, "No recommendations found."


def gen_dict_recommendation_from_report(report):
    sys_prompt = """
    You are a cybersecurity expert tasked with mapping a given threat report to the most relevant mitigation recommendation from a predefined list.

    Given:
    - A preliminary threat report describing a specific threat.
    - A list of potential mitigation recommendations.

    Your goal:
    1. Analyze the provided threat report.
    2. Determine which single recommendation from the list directly applies to the threat.
    3. If a relevant recommendation is found, output exactly that recommendation.
    4. If no recommendation matches, output "None".

    Instructions:
    - Base your decision solely on the content of the threat report and the provided list.
    - Output exactly one recommendation from the list that is most relevant, or "None" if there is no match.
    - Do not include additional commentary or return multiple items.

    The list of mitigation recommendations:
    ['Recommendations to protect against RaaS', 'Recommendations to identify and mitigate cryptojacking attacks', 'Recommendations to protect against Information Stealers', 'Recommendations to protect against Malvertising', 'Recommendations to protect against phishing attacks', 'Recommendations to protect against Mobile Malware', 'Recommendations to protect against CVE-2024-3400 - command injection vulnerability', 'Tips for preventing keylogging', 'Guidance for CobaltStrike', 'Guidance for Botnets', 'Mitigate zero-day vulnerabilities', 'Mitigating data security incidents', 'Recommendations to protect IoT specific devices', 'Recommendations for supply-chain attacks', 'Social Engineering']
    """

    user_prompt = f"""
    Threat Report:
    {report}

    Based on the above threat report, output exactly one mitigation recommendation from the list that is most applicable, or "None" if none apply.
    """

    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response_message = api_call(messages, [], model='gpt-4o', json_enabled=False)

    rec = response_message.choices[0].message.content
    return rec

def get_recommendation_by_title(data_frame, title):
    try:
        matched_rows = data_frame[data_frame["Title"].str.strip() == title.strip()]
        if len(matched_rows) == 0:
            print(f"No recommendation for '{title}'")
            return None, None
        
        first_match = matched_rows.iloc[0]
        return first_match["Id"], first_match["Description"]
    except Exception as e:
        print(f"Error in finding recommendation: {str(e)}")
        return None, None


def is_valid_ioc(ioc_value, ioc_type):
    def is_valid_ip(ip):
        pattern = re.compile(
        r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
                )
        return pattern.match(ip) is not None
    
    def is_valid_email(email):
        pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return pattern.match(email) is not None
    
    def is_valid_hash(value, hash_type):
        hash_lengths = {
                    "hash_md5": 32,
                    "hash_sha1": 40,
                    "hash_sha256": 64
                }
        value = value.lower() 
        return len(value) == hash_lengths.get(hash_type, 0) and all(c in '0123456789abcdef' for c in value)
    
    def is_valid_domain(domain):
        pattern = re.compile(r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$')
        return pattern.match(domain) is not None
    
    def is_valid_url(url):
        url = url.lower()
        url = url.replace('hxxp', 'http')
        pattern = re.compile(
        r'^(https?|ftp):\/\/(?:[-\w.]|(?:%[\da-fA-F]{2}))+(:\d+)?(?:\/[\w._~:/?#[\]@!$&\'()*+,;=%]*)?$'
                )
        return pattern.match(url) is not None
    
    def is_valid_ip_port(ip_port):
        pattern = re.compile(
        r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?):'
        r'(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[0-9]{1,4})$'
                )
        return pattern.match(ip_port) is not None
    
    if ioc_type == "ip":
        return is_valid_ip(ioc_value)
    elif ioc_type == "email":
        return is_valid_email(ioc_value)
    elif ioc_type in ["hash_md5", "hash_sha1", "hash_sha256"]:
        return is_valid_hash(ioc_value, ioc_type)
    elif ioc_type == "domain":
        return is_valid_domain(ioc_value)
    elif ioc_type == "url":
        return is_valid_url(ioc_value)
    elif ioc_type == "ip_port":
        return is_valid_ip_port(ioc_value)
    else:
        return False
    

def process_mitre_ttps_format(key, value):
    """
    Processes the MITRE TTPs field and formats the output.
    """
    text_output = ""
    
    if not value:
        text_output += f"#### {key} \n - No TTPs provided.\n\n"
        return text_output

    formatted_ttps = []
    
    # Check and parse value
    try:
        if isinstance(value, str):
            data = ast.literal_eval(value)  # Convert string to dict/list
        else:
            data = value  # Already a dict or list
    except Exception as e:
        text_output += f"#### {key} \n - Error parsing TTPs: {str(e)}\n\n"
        return text_output

    if isinstance(data, dict):  # If TTPs are a dictionary
        for ttp_id, details in data.items():
            try:
                # Split details into description, confidence, and justification
                parts = details.split(', Confidence: ')
                description = parts[0].strip()
                confidence_justification = parts[1].split('. Justification: ')
                confidence = confidence_justification[0].strip()
                justification = confidence_justification[1].strip()
                
                formatted_ttps.append(
                    f"- {ttp_id}: {description};\n  Confidence: {confidence}.\n  Justification: {justification}"
                )
            except IndexError:
                formatted_ttps.append(f"- {ttp_id}: {details};\n  Confidence: Not specified.\n  Justification: Not specified")
    elif isinstance(data, list):  # If TTPs are a list of dictionaries
        for ttp in data:
            for ttp_id, details in ttp.items():
                try:
                    parts = details.split(', Confidence: ')
                    description = parts[0].strip()
                    confidence_justification = parts[1].split('. Justification: ')
                    confidence = confidence_justification[0].strip()
                    justification = confidence_justification[1].strip()
                    
                    formatted_ttps.append(
                        f"- {ttp_id}: {description};\n  Confidence: {confidence}.\n  Justification: {justification}"
                    )
                except IndexError:
                    formatted_ttps.append(f"- {ttp_id}: {details};\n  Confidence: Not specified.\n  Justification: Not specified")
    else:  # Unsupported data type
        text_output += f"#### {key} \n - Unsupported TTP format: {data}\n\n"
        return text_output

    # Add formatted TTPs to text output
    text_output += f"#### {key} \n" + "\n".join(formatted_ttps) + "\n\n"
    return text_output


def augment_threat_actor_with_blog(threat_actor, actor_info):
    sys_prompt = f"""
    ### Task description:
    You are an expert in cybersecurity. Based on the extracted information about the threat actor(s) from an IoC report, please generate a detailed context and summary about threat actor(s) based on report context given and your knowledge. No hallucination is allowed. Your context should be brief. This will be used to enhance the description of the threat actor(s) in the report. Make sure the context provides enough details for a security professional to understand all the actors' profile(s) and their behaviors. No explanations or prefix texts are allowed in the output.

    ### Example:
    Threat Actor(s): BrazenBamboo
    Context: BrazenBamboo is a Chinese state-affiliated APT group. It is responsible for various attacks targeting government entities, private companies, and critical infrastructure worldwide. The group utilizes sophisticated malware such as DEEPDATA and DEEPPOST to exploit vulnerabilities in both Windows and macOS systems. They are known to use advanced techniques like spear-phishing and zero-day vulnerabilities to achieve their objectives. In the past, they have targeted industries such as telecommunications, finance, and energy.

    Threat Actor(s): Earth Estries
    Context: Earth Estries, also known as Salt Typhoon, is a Chinese cyber espionage group primarily focused on targeting the technology sector and governmental entities in Western countries. They are known to overlap with other APT groups such as FamousSparrow and UNC4841. Their primary modus operandi includes spear-phishing emails with malicious attachments, web shell exploitation, and using remote access tools (RATs) to gain unauthorized access to target networks.
    """

    user_prompt = f"""
    ### Task description:
    Based on the extracted information about the threat actor(s) from an IoC report, please briefly generate a detailed context and summary about threat actor(s) based on report context given and your knowledge. No hallucination is allowed. This will be used to enhance the description of the threat actor(s) in the report. No explanations or prefix texts are allowed in the output.

    ### Result:
    Threat Actor(s): {threat_actor}
    Report Content: {actor_info}
    Context:
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(new_messages, [], model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response

def get_cassie_triage(work_item_id):
    """
    Extracts Cassandra.FileIndicatorSummary from an Azure DevOps work item,
    formats it as Markdown, and saves it to a file.

    :param work_item_id: The ID of the Azure DevOps work item.
    :param output_file: The path to the Markdown file to save the output.
    """
    # Set up the Azure DevOps Personal Access Token (PAT)
    # Azure DevOps API URL
    authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Basic ' + authorization
    }
    project_url = f'https://dev.azure.com/threat-intel/Cassandra/_apis/wit/workitems/{work_item_id}?api-version=7.1'

    # Make the request
    response = requests.get(url=project_url, headers=headers)

    # Parse the JSON response
    try:
        data = response.json()

        # Access 'Cassandra.FileIndicatorSummary' if it exists
        if 'fields' in data and 'Cassandra.FileIndicatorSummary' in data['fields'] or 'Cassandra.NetworkIndicatorSummary' in data['fields']:
            file_indicator_summary = data['fields']['Cassandra.FileIndicatorSummary']
            network_indicator_summary = data['fields']['Cassandra.NetworkIndicatorSummary']
            markdown_output = "##### "

            # Parse HTML content with BeautifulSoup
            for summary in [file_indicator_summary, network_indicator_summary]:
                soup = BeautifulSoup(summary, 'html.parser')
                tables = soup.find_all('table')  # Find all <table> tags

                if not tables:
                    print("No <table> elements found in the summary.")
                    continue

                for table in tables:
                    # Find context (e.g., preceding <p> or <h3> tags)
                    context = []
                    prev_element = table.find_previous_sibling()
                    while prev_element and prev_element.name in ['p', 'h3', 'h2', 'h1']:
                        context.append(prev_element.text.strip())
                        prev_element = prev_element.find_previous_sibling()

                    # Reverse context list to get correct order
                    context.reverse()
                    context_text = "\n".join(context)

                    # Extract headers and rows
                    headers = [th.text.strip() for th in table.find_all('th')]  # Extract headers
                    rows = [
                        [td.text.strip() for td in row.find_all(['td', 'th'])]
                        for row in table.find_all('tr')
                    ]

                    # Format table as Markdown
                    if headers:
                        markdown_table = "| " + " | ".join(headers) + " |\n"
                        markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
                        for row in rows[1:]:  # Skip the header row
                            markdown_table += "| " + " | ".join(row) + " |\n"
                    else:
                        markdown_table = "\n"

                    # Combine context and table
                    markdown_section = f"{context_text}\n\n{markdown_table}"
                    markdown_output += markdown_section + "\n\n"
            if markdown_output != "##### ":
                return markdown_output
            else:
                return ""

        else:
            return ""

    except json.JSONDecodeError:
        print("Failed to parse JSON. Response text:")
        print(response.text)


def threat_research_playground(url, work_item_id):
    for _ in range(2):
        try:
            new_ti, related_docs = threat_research_core(url)
            source_blog = click_into_page_with_browser(
                url, is_text=True, headless_flag=False
            )
            if num_tokens_from_string(source_blog, 'gpt-4o') > 120000:
                source_blog = source_blog[:120000]
            text_output = ""

            # Add the source URL
            text_output += f"Source: [{url}]({url})\n\n"

            # Process related articles
            articles_text = "## Related articles (describing the same threat) \n"
            text_output += "## Related articles (describing the same threat) \n"
            unique_urls = set()
            for doc in related_docs:
                normalized_url = standardize_url(doc["link"])
                unique_urls.add(normalized_url)
            for unique_url in unique_urls:
                # text_output += f"- {unique_url}\n"
                articles_text += f"- {unique_url}\n"
            print(f"articles:\n {articles_text}")
            output = filter_duplicate_pipeline(url, articles_text)
            print(f"Related links: {output}")
            
            if output:
                text_output += output
                articles_text = output
            else:
                text_output += "No related articles found.\n"
                articles_text = "No related articles found.\n"
            text_output += "\n"

            # Enriched Document Section
            text_output += "## Enriched Doc (enrichments marked with *content*(link)): \n"
            paste_ioc_section = "#### paste IoC\n"
            ttps = ""
            print(new_ti)

            for key, value in new_ti.items():
                if key == 'Threat actor/group/campaign':
                    text_output += f"#### {key} \n {value} \n\n"
                    actors = get_actor(value)
                    if actors and 'None' not in actors:
                        # threat_actors = eval(get_actor(value))
                        threat_actors = eval(actors)
                        actor_name, links, context = pipeline(threat_actors, 'oneti', token)
                        actor_info_name = ", ".join(f"{name}" for name in set(actor_name[:3]))
                        # prof_links = "\n".join(f"- {link}" for link in set(links))
                        valid_links = []
    
                        for link in links:
                            # Fetch the page content
                            try:
                                blog_content = click_into_page_with_browser(link)  # Assuming this function returns blog content as a string
                                num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                                
                                # Only include links with content exceeding 500 tokens
                                if num_tokens > 500:
                                    valid_links.append(link)
                            except Exception as e:
                                print(f"Error processing {link}: {e}")
                        
                        # Remove duplicates and format as a list
                        prof_links = "\n".join(f"- {link}" for link in set(valid_links))    

                        if context:
                            context = context.replace('\n\n', '\n')
                            if prof_links:
                                text_output += f"- Based on MDTI profile for {actor_info_name} from the following links: \n\n{prof_links}\n\n The additional threat actor information is:\n\n {context}\n\n"
                            else:
                                text_output += f"- Based on profile for {actor_info_name} from the source and the related articles above: \n\n The additional threat actor information is:\n\n {context}\n\n"
                        else:
                            if num_tokens_from_string(value, 'gpt-4o') < 50:
                                context = augment_threat_actor_with_blog(actors, source_blog)
                                if context:
                                    context = context.replace('\n\n', '')
                                    text_output += f"- Based on profile from the source and the related articles above: \n\n The additional threat actor information is:\n\n {context}\n\n"
                                else:
                                    continue
                            else:
                                continue

                    else:
                        continue
                    print(f"After threat actors, \n\n {text_output}\n\n")

                elif key == 'Root cause':
                    text_output += f"#### {key} \n {value} \n\n"
                    actors = eval(get_root_cause_with_llm(value))
                    actor_name, links, context = root_cause_pipeline(actors, token)
                    # prof_links = "\n".join(f"- {link}" for link in set(links))
                    valid_links = []
    
                    for link in links:
                        # Fetch the page content
                        try:
                            blog_content = click_into_page_with_browser(link)  # Assuming this function returns blog content as a string
                            num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                            
                            # Only include links with content exceeding 500 tokens
                            if num_tokens > 500:
                                valid_links.append(link)
                        except Exception as e:
                            print(f"Error processing {link}: {e}")
                    
                    # Remove duplicates and format as a list
                    prof_links = "\n".join(f"- {link}" for link in set(valid_links))
                    cause = ", ".join(f"{name}" for name in set(actor_name[:3]))
                    if context:
                        context = context.replace('\n\n', '\n')
                        # text_output += f"- Based on MDTI profile for {cause} from the following links: \n\n{prof_links}\n\n The additional context for root cause is:\n\n {context}\n\n"
                        if prof_links:
                            text_output += f"- Based on MDTI profile for {cause}, the additional context for root cause is:\n\n {context}\n\n"
                        else:
                            text_output += f"- Based on profile for {cause} from the source and the related articles above, the additional context for root cause is:\n\n {context}\n\n"
                    print(f"After root cause, \n\n {text_output}\n\n")
                        

                elif key == 'MITRE TTPs':
                    ttp_text = process_mitre_ttps_format(key, value)
                    text_output += ttp_text
                    print(f"After TTPs, \n\n {text_output}\n\n")

                elif key == 'IoCs':
                    continue

                elif key == 'Mitigation Steps':
                    text_output += f"#### {key} \n"
                    actors = get_actor(value)
                    has_mitigation = False

                    if actors and 'None' not in actors:
                        names, links, mdti_recommendation = mdti_recommendation_pipeline(actors, token)
                        # prof_links = "\n".join(f"- {link}" for link in set(links))
                        valid_links = []
    
                        for link in links:
                            # Fetch the page content
                            try:
                                blog_content = click_into_page_with_browser(link)  # Assuming this function returns blog content as a string
                                num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                                
                                # Only include links with content exceeding 500 tokens
                                if num_tokens > 500:
                                    valid_links.append(link)
                            except Exception as e:
                                print(f"Error processing {link}: {e}")
                        
                        # Remove duplicates and format as a list
                        prof_links = "\n".join(f"- {link}" for link in set(valid_links))

                        mitigation_name =  ", ".join(f"{name}" for name in set(actor_name[:3]))
                        if mdti_recommendation != "No recommendations found.":
                            cleaned_recommendation = re.sub(r'\n\s*\n', '\n', mdti_recommendation)
                            if prof_links:
                                text_output += f"- Based on MDTI profile for ({mitigation_name}) from the following links: \n\n{prof_links}\n\n The recommendations are:\n\n"
                            else:
                                text_output += f"- Based on profile for ({mitigation_name}) from the source and the related articles above, the recommendations are:\n\n"

                            text_output += f"{cleaned_recommendation}\n"
                            has_mitigation = True
                    # elif mdti_recommendation == "No recommendations found.":
                    # else:
                    if not has_mitigation:
                        # rec_dict_mitigation = process_rec_dict_ttps(ttps)
                        rec_dict_mitigation = gen_dict_recommendation_from_report(text_output)
                        if rec_dict_mitigation:
                            text_output += f"- Based on OSINT recommendation dictionary ({rec_dict_mitigation}), the recommendations are:\n\n"
                            tech = pd.read_csv('recommendations/RecDict.csv')
                            res = get_recommendation_by_title(tech, rec_dict_mitigation)
                            text_output += f"{rec_dict_mitigation}: {res[1]}\n"
                            # for rec in rec_dict_mitigation:
                                # text_output += f"- [{rec["ttp_id"]}] {rec['title']}: {rec['reason']}\n"
                            has_mitigation = True

                        mitigation = process_all_ttps(ttp_text)
                        if not rec_dict_mitigation and mitigation:
                            # recommendation = eval(mitigation)
                            # for rec in recommendation:
                            # text_output += f"- Based on recommendation table, the source recommends:\n"
                            text_output += f"- Did not find related recommendations from MDTI and OSINT Recommendation Dictionary, based on TTPs, we suggest the following recommendations: \n"
                            for rec in mitigation:
                                text_output += f"- [{rec['ttp_id']}] {rec['title']}: {rec['reason']}\n"
                            has_mitigation = True
                        # else:
                    if not has_mitigation and value:
                        text_output += f"#### {key} \n {value} \n"
                    text_output += '\n'
                    print(f"After mitigation, \n\n {text_output}\n\n")
                
                elif key == 'Detection Signature':
                    text_output += f"#### Detections/Hunting Queries \n"
                    has_detection = False
                    has_cassie_detection = False

                    if actors and 'None' not in actors:
                        actor_names, links, mdti_detection = mdti_detection_pipeline(threat_actors, token)
                        valid_links = []
    
                        for link in links:
                            # Fetch the page content
                            try:
                                blog_content = click_into_page_with_browser(link)  
                                num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                                
                                if num_tokens > 500:
                                    valid_links.append(link)
                            except Exception as e:
                                print(f"Error processing {link}: {e}")
                        
                        # Remove duplicates and format as a list
                        prof_links = "\n".join(f"- {link}" for link in set(valid_links))

                        detection_name =  ", ".join(f"{name}" for name in set(actor_name[:3]))
                        if mdti_detection != "No detections found.":
                            cleaned_detection = re.sub(r'\n\s*\n', '\n', mdti_detection)
                            if prof_links:
                                text_output += f"- Based on MDTI profile for ({detection_name})\n\n The detections are:\n\n"
                            else:
                                continue

                            text_output += f"{cleaned_detection}\n"
                            has_detection = True
                    # elif mdti_recommendation == "No recommendations found.":
                    # else:
                    if not has_detection:
                        cassie_detection = get_cassie_triage(work_item_id)
                        if cassie_detection:
                            text_output += f"- Based on Cassie Triage profile for ID {work_item_id}\n\n The detections are:\n\n{cassie_detection}\n"
                            has_cassie_detection = True
                        else:
                            text_output += f"- No detections found.\n\n"

                    if not has_detection and not has_cassie_detection:
                        continue
                        # text_output += f"#### {key} \n {value} \n"
                    text_output += '\n'
                    print(f"After detection, \n\n {text_output}\n\n")

                else:
                    formatted_output = ""
                    try:
                        if isinstance(eval(value), dict):
                            for k, v in eval(value).items():
                                if isinstance(v, dict):
                                    formatted_output += f"- {k}\n"
                                    for sub_k, sub_v in v.items():
                                        formatted_output += f"\t - {sub_k}: {sub_v}\n"
                                else:
                                    formatted_output += f"- {k}: {v}\n"
                        else:
                            text_output += f"#### {key} \n {value} \n\n"
                    except Exception as e:
                        text_output += f"#### {key} \n {value} \n\n"
                    print(text_output)

            text_output += "#### IoCs:\n"

            iocs_dict = {}  # Use a dictionary to remove duplicates by value
            # for each url, extract iocs from url directly
            blog_for_urls = []

            iocs_dict = {}  # Use a dictionary to remove duplicates by value
            for link in unique_urls:
                #blog = click_into_page_with_browser(
                    #link, is_text=False, headless_flag=False
                #)
                blog = click_into_page_with_browser(
                    link, is_text=True, headless_flag=False
                )
                html = url_open_with_browser(link)
                date = add_date(html)
                if date:
                    pub_date = date
                else:
                    pub_date = "Unspecified"

                length = num_tokens_from_string(blog, "gpt-4o")
                if length > 120000:
                    blog = blog[:120000]
                # Proper formatting for IoCs
                blog = blog.replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https")
                blog_for_urls.append({"blog": blog, "source": link})
                
                iocs_json = extract_iocs_from_text(blog, link)
                if iocs_json:
                    for ioc in iocs_json:
                        ioc_tuple = (ioc['type'], ioc['value'], ioc['source'], pub_date)
                        # Use ioc['value'] as the key to ensure uniqueness
                        iocs_dict[ioc['value']] = ioc_tuple


            unique_iocs = [{"type": ioc[0], "value": ioc[1], "source": ioc[2], "publish_date": ioc[3]} for ioc in iocs_dict.values()]
            print(f"Unique IoCs: {unique_iocs}")
            if not unique_iocs:
                text_output += "- No IoCs found. \n"
                return text_output
            white_list = get_white_list_urls('All Intelligence Feeds.csv')
            unique_urls.update(white_list)

            for ioc_data in unique_iocs:
                ioc_value = ioc_data["value"].replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https").replace("[", "").replace("]", "")
                print(f"====== Processing IoC: {ioc_value} ======")
                if ioc_value in unique_urls or filter_url(ioc_value, unique_urls, white_list):
                    continue
                ioc_type = ioc_data["type"]

                pub_date = ioc_data['publish_date']
                ioc_source = ioc_data.get('source', 'No link provided')
                blogs_for_target_source = next((entry["blog"] for entry in blog_for_urls if entry["source"] == ioc_source), None)

                try:
                    if ioc_type in ["hash_md5", "hash_sha1", "hash_sha256"]:
                        ioc_type_for_check = 'hash'
                    else:
                        ioc_type_for_check = ioc_type

                    is_malicious = check_ioc(ioc_value, ioc_type_for_check)
                    in_article = ioc_value in blogs_for_target_source and "True" in llm_judgment_for_ioc_in_blog(ioc_value, blogs_for_target_source)

                    if is_malicious == True and in_article and is_valid_ioc(ioc_value, ioc_type):
                        # if ioc_type.lower() == 'email' and filter_email(ioc_value, unique_urls, white_list):
                            # continue
                        text_output += f"- {ioc_type}: {ioc_value}  Publish date: {pub_date} [In [this link]({ioc_source}), Verified via VT]\n"
                        paste_ioc_section += f"{ioc_value}\n\n"
                        print(f"The {ioc_type} {ioc_value} is malicious and in article link.")
                    
                    elif is_malicious == False and in_article and is_valid_ioc(ioc_value, ioc_type):
                        # text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source}))  Publish date: {pub_date} [In Articles, identified as not malicious via VT]\n"
                        print(f"The {ioc_type} {ioc_value} is not malicious but in article link.")
                    
                    elif is_malicious is None and in_article and is_valid_ioc(ioc_value, ioc_type):
                        if ioc_type.lower() == 'email' and filter_email(ioc_value, unique_urls, white_list):
                            continue
                        text_output += f"- {ioc_type}: {ioc_value}  Publish date: {pub_date} [In [this link]({ioc_source}), not included in VT database]\n"
                        paste_ioc_section += f"{ioc_value}\n\n"
                        print(f"The {ioc_type} {ioc_value} is not in VT database but in article link.")
                    
                    else:
                        print(f"{ioc_type} {ioc_value} is not found in neither article link nor VT.")
                        continue

                except Exception as e:
                    print(f"Error processing {ioc_type} {ioc_value}: {e}")
            
            if paste_ioc_section == "#### paste IoC\n":
                text_output += "- No IoCs found.\n\n"

            text_output += "\n" + paste_ioc_section + "\n"

            return text_output
        except AttributeError as e:
            print(RED + "==> Error in processing the blog." + RESET) 
            print(e)
            continue

'''
def threat_research_playground(url):
    for i in range(2):
        try:
            new_ti, related_docs = threat_research_core(url)
            text_output = ""

            text_output += f"Source: [{url}]({url})\n\n"
            text_output += "## Related articles (describing the same threat) \n"
            # for i in related_docs:
            #    text_output += ("- " + str(i["link"]) + "\n")
            # text_output += "\n"
            # Use a set to store unique URLs
            unique_urls = set()
            for doc in related_docs:
                normalized_url = standardize_url(doc["link"])
                unique_urls.add(normalized_url)

            # Add unique URLs to the output
            for unique_url in unique_urls:
                text_output += f"- {unique_url}\n"
            text_output += "\n"

            text_output += "## Enriched Doc (enrichments marked with *content*(link)): \n"
            # mdf.write(json.dump(new_ti))
            # IoC copy/pasting format
            for key, value in new_ti.items():
                if key == 'Incident':
                    text_output += f"#### {key}: {value} \n\n"
                elif key == 'IoCs':
                    text_output += "#### IoCs:\n"
                    for ioc in value:
                        try:
                            text_output += f"- {ioc['type']}: {ioc['value']} ([link]({ioc['source']})) \n\n"
                        except KeyError:
                            text_output += f"- {ioc} \n\n"
                        except Exception as e:
                            text_output += f"- {ioc} \n\n"
                    text_output += "- For more IoCs, please refer to the above links. \n\n"
                else:
                    text_output += f"#### {key} \n {value} \n\n"
            text_output += "\n"
            

            return text_output
        except AttributeError:
            print("Error in processing the blog.")
            continue

'''

# TODO: using code to evaluate IoCs
def eval_threat_research(info, new_ti, related_docs):
    content_analysis_prompt = f"""
    You are a security expert assistant designed to validate the quality of an AI-generated report.
    Your task:    
    • Compare the AI-generated report with the human generated report provided. Determine if they descibe the same underlying threat/vulnerability/attack, even if phrased differently. Focus on the threat/vulnerability/attack, root cause concepts, and implications rather than exact wording.  
    • Compare the indicators filed in the human-generated report with the IoCs in the AI-generated report. Please list each IOC in the human-generated report and one by one determine if it is included in the AI-generated report. Ingore the prefix (e.g., hxxp) or some minoir changes (e.g., [:] vs :) Based on the one-by-one comapre to determine if they include the same indicators. 
    
    Instructions:
    • If the human-generated report have the same intent or describe the threat/vulnerability/attack, return True.    
    • If they describe different threat/vulnerability/attack, return False. 
    • If there is one IoC that present in the human-generated report but does not exist in the AI-generated report, return False. Output them in the explannation
    • If the AI-generated report covers all IoCs that are in the human-generated report, return True. 
    • If the AI-generated report has more IoCs, output them in the explanation.
    • Only respond with a single word: True or False.
    
    Please output your decision in JSON format with the key "step_by_step_thinking_for_iocs_comparing", "is_same_content", "is_same_iocs", "is_ai_generated_has_more_iocs", "is_human_generated_has_more_iocs" and "explanation".
    The human generated report is: {info}
    The AI generated report is: {new_ti}
    """
    for i in range(3):
        try:
            new_messages = []
            new_messages.append({"role": "user", "content": content_analysis_prompt})
            response_message = api_call(new_messages, [], model="gpt-4-32k")

            f_eval.write("=============================================================== \n")    
            orignial_one = "### Original Human generated report: " + '\n'
            orignial_one = orignial_one + "Title: " + info["title"]  + '\n'
            orignial_one = orignial_one + "Url: " + info["url"]  + '\n'
            orignial_one = orignial_one + "Summary: " + info["summary"]  + '\n'
            orignial_one = orignial_one + "Content: " + info["content"]  + '\n'
            orignial_one = orignial_one + "Indicators: "  + '\n'
            for ioc in info["indicators"]:
                if ioc["source"] == "public":
                    orignial_one = orignial_one + ioc["type"] + "   " + ioc["value"]  + '\n'

            debug_print(orignial_one)
            f_eval.write(orignial_one + "\n")

            ai_one = "### AI generated report: "  + '\n'
            ai_one += "# Enriched Doc (enrichments marked with *content*(link)): \n"
            # mdf.write(json.dump(new_ti))
            for key, value in new_ti.items():
                ai_one += f" {key}: {value} \n\n"
            ai_one += "\n"
            ai_one += "# Related articles (describing the same threat) \n"
            ai_one += str([i["link"] for i in related_docs])
            ai_one += "\n"

            debug_print(ai_one)
            f_eval.write(ai_one + "\n")

            debug_print(
                RED + "LLM's Evalution " + RESET,
                [response_message.choices[0].message.content],
            )
            f_eval.write("### Evalution Result: " + '\n')
            f_eval.write(response_message.choices[0].message.content + "\n")

            eval_info = json.loads(response_message.choices[0].message.content)
            if not eval_info["is_same_iocs"] or not eval_info["is_same_content"]:
                debug_print(
                    RED + f"==> Error Report: {eval_info}" + RESET
                )
            break
        except json.decoder.JSONDecodeError:
            debug_print("==> Error in parsing the response.")
            if i == 2:
                return {}
            continue
    
    return eval_info

f_eval = open("eval_results_articles_2024_after181.txt", "w")

def main():

    input_filename = "articles2024.jsonl"
    output_filename = "enhanced_articles2024.jsonl"

    # input_filename = "2024_failed.jsonl"
    # output_filename = "enhanced_2024_failed.jsonl"
    # titles_processed = get_titles_processed()
    titles_processed = []
    debug_print(f"the list: {titles_processed}")
    fw = open(output_filename, "a")
    num = 0
    with open(input_filename) as f:
        for line in f:
            info = json.loads(line)
            info["title"] = "".join(
                [
                    char
                    for char in info["title"]
                    if char not in ["#", "@", ":", "|", "/", "\\", "*", "'", '"', "?"]
                ]
            )
            num += 1
            if num < 181:
                continue
            if num >  500:
                break
            
            # Remove the internal indicators
            iocs = info["indicators"]
            new_iocs = []
            for ioc in iocs:
                if ioc["source"] == "public":
                    new_iocs.append(ioc)
            info["indicators"] = new_iocs

            debug_print(RED + f"==> The input is: " + RESET)
            debug_print(info)

            if info["title"] in titles_processed:
                debug_print(
                    info["title"] + " has been processed. Continue to the next case.\n"
                )
                continue

            debug_print(RED + f"==> Start to process the blog: " + RESET)
            debug_print("link: ", info["url"])
            if not info["url"]:
                debug_print("The URL is empty. Skip this one.")
                continue
            debug_print("title: ", info["title"])

            new_ti, related_docs = threat_research_core(info["url"])
            if not new_ti:
                debug_print(RED + "==> The blog does not have enough info. Skip this one." + RESET)
                continue
            
            # TODO(xuafeng): add evalution, need to refine
            try:
                eval_results = eval_threat_research(info, new_ti, related_docs)
            except tenacity.RetryError:
                debug_print("==> Retry Error")
                continue
            debug_print(RED + "==> The Evaluation Results: " + RESET)
            debug_print(eval_results)

            debug_print(RED + "==> The original one: " + RESET)
            console = Console()
            md = Markdown(info["content"])
            aligned_md = Align.left(md)
            console.print(md)
            debug_print(RED + "The Enhanced Data is: " + RESET)
            debug_print(new_ti)

            text_output = ""

            text_output += f"Source: [{info['url']}]({info['url']})\n\n"
            text_output += "# " + info["title"] + "\n\n"
            text_output += (
                "# Enriched Doc (enrichments marked with *content*(link)): \n"
            )
            # mdf.write(json.dump(new_ti))
            try:
                for key, value in new_ti.items():
                    text_output += f" {key}: {value} \n\n"
            except AttributeError:
                text_output += f" {new_ti} \n\n"
            text_output += "\n"
            text_output += "# Related articles (describing the same threat) \n"
            text_output += str([i["link"] for i in related_docs])
            text_output += "\n"

            md_filename = "new-output/" + info["title"] + ".md"
            with open(md_filename, "w", encoding="utf-8") as mdf:
                mdf.write(text_output)
                mdf.write("\n")

            # debug_print(response_message.choices[0].message.content)
            info["enhanced"] = new_ti
            info["related_docs"] = [i["link"] for i in related_docs]
            fw.write(json.dumps(info) + "\n")
            fw.flush()
            # break


if __name__ == "__main__":
    # main()
    white_list = get_white_list_urls('All Intelligence Feeds.csv')
    print(white_list)

