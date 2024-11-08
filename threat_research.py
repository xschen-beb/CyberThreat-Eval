import json
import sys
import os

import tiktoken
# for exponential backoff
import tenacity
from tenacity import (retry, stop_after_attempt, wait_random_exponential)
from rich.console import Console
from rich.markdown import Markdown
from rich.align import Align
import playwright

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

if _DEPLOYMENT_ENV == "local":
    client = AzureOpenAI(
        azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
        api_key=os.getenv("PROXY_KEY"),
        api_version="2024-05-01-preview",
    )

if _DEPLOYMENT_ENV == "playground":
    client = AzureOpenAI(
        azure_endpoint="https://riqds-openai-test.openai.azure.com",
        azure_ad_token_provider=get_bearer_token_provider(_CREDENTIAL, _AUTH_SCOPE),
        api_version="2024-05-01-preview",
    )


def debug_print(*args, **kwargs):
    if _LOG_ENABLED:
        print(*args, **kwargs)
    else:
        pass


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def api_call(messages, func_list, model= "gpt-4o", json_enabled=True):
    if model == 'gpt-4-32k':
        return client.chat.completions.create(
            # model="gpt-4-32k",
            model=model,
            messages=messages,
            # functions= func_list,
            # function_call="auto",  # auto is default, but we'll be explicit
            temperature=0.7,
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
            temperature=0.7,
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
            temperature=0.7,
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
    Then, please analyze the new found document to identify if it has enough info to help people understand the root cause (including, vulnerable/misconfigured services, how to mitigate) bechind the incident.
    Note that if a new found document covers a few different incidents, we called it a cyber-intel-brief, mark it as not the same incident.
    Please output your decision in JSON format with the key "is_same", "is_similar" or "is_enough" and "explanation". 
    The original blog is: {original}
    The new found document is: {new_doc}
    """
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
    # If you wan to include specific words in the results, please use double quotes.
    messages = [
        {"role": "system", "content": sys_prompt},
    ]
    if num_tokens_from_string(blog["blog"], "gpt-4o") > 120000:
        blog["blog"] = blog["blog"][:80000]
    misconf_qeustion = f"Here is the blog: {blog['blog']}."
    debug_print(RED + "==> Orginal html: " + RESET)
    debug_print(blog["blog"])
    
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
    num_tokens = len(encoding.encode(string))
    return num_tokens


def enrichment(original, related_docs):
    for doc in related_docs[1:]:
        analysis_prompt = """
        You are a security researcher. I will give a threat report and a new found document. You goal is to see if we can add some new info to the report based on new found documents. Please merge the new info into original and mark for your changes in the enhanced report and and cite the new found doc with the following format *The changes* (link to new found document).
        
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
        - Merge the new Entities into the original report. Mark the new information with *Your changes* (link to new found document). Do not create a new key (e.g., 'Added info').
        - re-write the previous summary to improve flow and make space for additional entities.
        - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
        - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
        - Missing entities can appear anywhere in the new summary.
        - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.

        Answer in JSON. it has two keys. One is "thoughts", which described you step-by step thinks. Another is 'final_report'.
        The final report should be in the following format:
        {
        "Incident": "XXXX",
        "Root cause": "XXXX",
        "XXX": "XXX",
        }
        """

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
                response_message = api_call(messages, [])
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

    related_docs = find_related_ones({"link": url, "blog": blog})
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

    # Enhance the documents
    debug_print(RED + f"=> Enhance the blog: {url}" + RESET)
    analysis_prompt = """
        You are a security expert. I will give a report/blog on the Internet. You need to analyze it to understand the root cause (including, vulnerable/misconfigured services), how to detect this problem, and the mitigation behind the incident.
        **For IoCs, please also extract those (e,g., hash1, hash256, hash_md5) inside the Yara Rule into the IoCs. e.g., extract '"hash1/hash256/hash_md5": "65c6798eedd33aa36d77432b2ba7ef45dfe760092810b4db487210b19299bdcb"' from YARA rule and put it into IoCs **

        You should provide a signature in the following format:    
        Incident: Shanghai Police Datalake Leak
        
        Root cause: the root cause behind the indicent including vulnerable/misconfigured services. e.g., Misconfigured Kibana instance 
        
        Threat actor/group/campaign: Who carried out the attack? It could be an orgainzation, a malware family, etc (if known)
        
        Organization/industry/location: Who was targeted/vicim? (if known)
        
        Start date – End date: When did the attack happen? (if known)

        MITRE TTPs: How was the attack carried out?  (if known)

        Impact: 100,000 records leaked.  **how many devices people impacted or the financial losses**

        Mitigation Steps: (How to protect myself?) e.g., Secure the Kibana instance with authentication credentials. and **Detailed Steps for mitigation**

        Detection Signature: (How to detect? i.e., detection rules)
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
        
        IoCs: How do I know I am affected? (for example, IP, domain, email, sha1, sha256, hash1, hash256, hash_md5, url, etc). If the document does not have IoCs, please output "No IoCs found". If the document has IoCs, please MAKE SURE to list top 10 IoCs (IF HAVE) you found in the document.  Change the URL/IP/Domain format to a valid format with standard syntax, without the extra brackets or colons (e.g., change hxxp[:]//2[.]57[.]149[.]233[:]3366/ to http://2.57.149.233:3366/)
        The IoCs should be a in the following format:
        '[{"type":"hash_md5","value":"3edcde37dcecb1b5a70b727ea36521de","source": "https://www.wheretheiocfrom.com/XX/XXXX/"},{"type":"url","value":"http:\/\/50.19.48.59:82\/me1.bat","source": "same as above"}]'
        The type can be "ip", "ip_port",  "domain", "url", "email", "hash_md5", "hash_sha256", "hash_sha1".
        """

    messages = [
        {"role": "system", "content": analysis_prompt},
    ]

    misconf_qeustion = f"Here is the blog: {blog}."
    messages.append({"role": "user", "content": misconf_qeustion})
    response_message = api_call(messages, [], json_enabled=False)
    original = response_message.choices[0].message.content

    debug_print(RED + "==> The first enhanced one: " + RESET, original)

    # merge related doc together to ehnchace the density
    new_ti = enrichment(original, related_docs)

    return new_ti, related_docs


def threat_research_playground(url):
    for i in range(2):
        try:
            new_ti, related_docs = threat_research_core(url)
            text_output = ""

            text_output += f"Source: [{url}]({url})\n\n"
            text_output += "## Related articles (describing the same threat) \n"
            for i in related_docs:
                text_output += ("- " + str(i["link"]) + "\n")
            text_output += "\n"

            text_output += "## Enriched Doc (enrihcments marked with *content*(link)): \n"
            # mdf.write(json.dump(new_ti))
            for key, value in new_ti.items():
                if key == 'Incident':
                    text_output += f"#### {key}: {value} \n\n"
                elif key == 'IoCs':
                    text_output += "#### IoCs: \n"
                    for ioc in value:
                        try:
                            text_output += f"- {ioc['type']}: {ioc['value']} ([link]({ioc['source']})) \n\n"
                        except KeyError:
                            text_output += f"- {ioc} \n\n"
                    text_output += "- For more IoCs, please refer to the above links. \n\n"
                else:
                    text_output += f"#### {key} \n {value} \n\n"
            text_output += "\n"
            

            return text_output
        except AttributeError:
            print("Error in processing the blog.")
            continue


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
            ai_one += "# Enriched Doc (enrihcments marked with *content*(link)): \n"
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
                "# Enriched Doc (enrihcments marked with *content*(link)): \n"
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
    main()

