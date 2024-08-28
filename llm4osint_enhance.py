import json
import sys
import os

from rich.console import Console
from rich.markdown import Markdown
from rich.align import Align

from openai import AzureOpenAI
# from dotenv import load_dotenv
# load_dotenv()

# for exponential backoff
from tenacity import (retry, stop_after_attempt, wait_random_exponential)  
from search_engine import google_web_search, click_into_page, click_into_page_original, click_into_page_with_browser

# ANSI escape codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

client = AzureOpenAI(
    azure_endpoint = "http://10.150.142.182:9999", 
    api_key= os.getenv('PROXY_KEY'),  
    api_version="2024-05-01-preview"
)

input_filename = "Published_Articles_2023.jsonl"
output_filename = "Enhanced_Data_Published_Articles_2023.jsonl"

# @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def api_call(messages, func_list, json_enabled=True):
    if json_enabled:
        return client.chat.completions.create(
                    # model="gpt-4-32k",
                    model="gpt-4o",
                    messages=messages,
                    # functions= func_list,
                    # function_call="auto",  # auto is default, but we'll be explicit
                    temperature=0.7,
                    response_format={ "type": "json_object" },
                    # seed=42,
                    max_tokens = 4096
                )
    else:
        return client.chat.completions.create(
                    # model="gpt-4-32k",
                    model="gpt-4o",
                    messages=messages,
                    # functions= func_list,
                    # function_call="auto",  # auto is default, but we'll be explicit
                    temperature=0.7,
                    # response_format={ "type": "json_object" },
                    # seed=42,
                    max_tokens = 4096
                )


def dig_deeper(blog, identified_links):
    # print("This is a critical security event.")
    # print("Summary:", response_dict["summary"])
    # print("Service:", response_dict["service"])
    # print("Impact:", response_dict["impact"])

    print(RED + "Step 2:" + RESET, "Search realated exploit documents or attack details. (LLM iteratively search and analyze the results)")

    sys_prompt = """
    You are a security expert. I will give a report on the Internet. I want to delve deeper into this incident to see what the reason behind and tech details. Can you sugggest a search query (including concrete entities, date, service or victims) that I can use to search in the search engine to understand the tech details of this attack/incident. Do not include general words like "cybersecurity", "personal information", etc because they are too general to search. 
    You output should be json format with query the key.   
    """
    # If you wan to include specific words in the results, please use double quotes.

    messages = [
        {"role": "system", "content": sys_prompt},
    ]

    
    misconf_qeustion = f"Here is the blog: {blog}."

    messages.append({"role": "user", "content": misconf_qeustion})
    
    response_message = api_call(messages, [])

    # print(response_message)
    print(response_message.choices[0].message.content)
    info = json.loads(response_message.choices[0].message.content)
    messages.append({"role": "assistant", "content": response_message.choices[0].message.content})
    query = info["query"]
    end_flag = False
    while True:
        if end_flag:
            break
        print(RED + "LLM Decision: " +RESET, "Google Query -> : ", query)
        google_search_results = google_web_search(query + ' "details"')
        # google_search_results = google_web_search(query + ' "What we know about"')

        results_filtering_prompt = f"""
        This is the google search results.
        {str(google_search_results)}
        Please provide the top 1 link that you think are most relevant to the incident. But not in {identified_links}. It can help understand the root cause (including, vulnerable/misconfigured services, how to mitigate). Your output should be json format with link as the key.
        """
        messages.append({"role": "user", "content": results_filtering_prompt})
        response_message = api_call(messages, [])
        # print(response_message)
        print(RED + "LLM Selected Link: " + RESET, response_message.choices[0].message.content)
        info = json.loads(response_message.choices[0].message.content)
        messages.append({"role": "assistant", "content": response_message.choices[0].message.content})
        link = info["link"]
        while True: 
            # print(RED + "New Selected Link: " + RESET, link)
            page_content = click_into_page_with_browser(link)
            
            print("Page Content: ", [page_content[0:500]])

            content_analysis_prompt = f"""
            This is the detailed information of the link you provided. 
            {page_content[0:6000]}
            Please analyze this report to identify if these blogs have enough info to help people understand the root cause (including, vulnerable/misconfigured services, how to mitigate) bechind the incident.
            If yes, please output <END>
            Else, please provide a new search query or a new link to search more information. with the key "query" or "link".
            """
            messages.append({"role": "user", "content": content_analysis_prompt})
            response_message = api_call(messages, [])
            # print(response_message)
            print(RED + "LLM Analysis Decision: " +RESET, [response_message.choices[0].message.content])
            
            if "<END>" in response_message.choices[0].message.content.strip():
                print("===> End of the search.")
                end_flag = True
                break
            else:
                info = json.loads(response_message.choices[0].message.content)
                if "query" in info:
                    query = info["query"]
                    break
                if "link" in info:
                    link = info["link"]
                    continue

    return {"link": link, "content": page_content}



def categorize(blog):
    print(RED+ "==> Categorizing the blog (identify if it is news or technical report)." +RESET)
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
    print(response_message.choices[0].message.content)
    decision = json.loads(response_message.choices[0].message.content)
    if decision["is_enough"]:
        print(RED +"This blog has enough info to help people understand the root cause behind the incident." + RESET)
        return True
    else:
        print(RED + "This blog does not have enough info to help people understand the root cause behind the incident." + RESET)
        return False
    

def gen_queries_links(blog):
    analysis_prompt = f"""
    You are a security researcher. I will give a report on the Internet. I want to delve deeper into this incident to see what the reason behind and tech details. Can you sugggest a search query (including concrete entities, date, service or victims) that I can use to search in the search engine to understand the tech details of this attack/incident. Do not include general words like "cybersecurity", "personal information", etc because they are too general to search. 
    You output should be json format with query the key. Please also provide the links that described the same incident mentioned in the blog with the key "links".  
    """

    messages = [
        {"role": "system", "content": analysis_prompt},
    ]

    misconf_qeustion = f"Here is the blog: {blog}."

    messages.append({"role": "user", "content": misconf_qeustion})

    # response_message = api_call(messages, [], json_enabled=False)
    response_message = api_call(messages, [])
    return response_message.choices[0].message.content

def compare_docs(original, new_doc):
    content_analysis_prompt = f"""
    You are a security expert. I will give you a original blog and a new found document. You goal is to step-by-step identify if the new found document described the same incident comapred to the original blog (i.e. talking the same thing). If not, identify if the new found document described a similar incident.
    Then, please analyze the new found document to identify if it has enough info to help people understand the root cause (including, vulnerable/misconfigured services, how to mitigate) bechind the incident.
    Please output your decision in JSON format with the key "is_same", "is_similar" or "is_enough" and "explanation".
    The original blog is: {original}
    The new found document is: {new_doc}
    """
    new_messages = []
    new_messages.append({"role": "user", "content": content_analysis_prompt})
    response_message = api_call(new_messages, [])
    # print(response_message)
    print(RED + "LLM's Analysis (Relevant and enough) " +RESET, [response_message.choices[0].message.content])
    
    info = json.loads(response_message.choices[0].message.content)
    return info

def find_related_ones(blog):
    print(RED + "==> Find more related documents." + RESET)

    # Step 1: Ask the model to generate search queries and to extract links
    sys_prompt = """
    You are a security expert. I will give a report on the Internet. I want to delve deeper into this incident to see what the reason behind and tech details. Can you sugggest a search query (including concrete entities, date, service or victims) that I can use to search in the search engine to understand the tech details of this attack/incident. Do not include general words like "cybersecurity", "personal information", etc because they are too general to search. 
    You output should be json format with queries the key. Please also provide the links that described the same incident mentioned in the blog with the key "links".    
    """
    # If you wan to include specific words in the results, please use double quotes.
    messages = [
        {"role": "system", "content": sys_prompt},
    ]
    misconf_qeustion = f"Here is the blog: {blog['blog']}."
    messages.append({"role": "user", "content": misconf_qeustion})
    response_message = api_call(messages, [])
    info = json.loads(response_message.choices[0].message.content)
    messages.append({"role": "assistant", "content": response_message.choices[0].message.content})
    
    queries = info["queries"]
    print(RED + "Get Candidate Queries and Links: " + RESET)
    print("queries: ", queries)
    links = info["links"]
    print("links: ", links)

    # Step 2: Click into the links to get the content
    print(RED + "==> Click into the some links to get the content." + RESET)
    all_related_docs = []

    # Demo: click into the first link
    # with open("beelp.txt") as f:
    #     text = f.read()
    # print("hard load: ", [text[0:500]])
    # all_related_docs.append({"link": "https://www.bleepingcomputer.com/news/security/android-tv-box-on-amazon-came-pre-installed-with-malware/", "content": text})

    identified_links = []
    identified_links.append(blog["link"])
    all_related_docs.append({"link": blog["link"], "blog": blog["blog"], "is_same": True, "is_enough": True})

    for link in links[:3]:
        print(RED + "Delve into the link: " + RESET, link)
        if link in identified_links:
            print("==> The link has been identified. Skip it.")
            continue
        identified_links.append(link)
        page_content = click_into_page_with_browser(link)
        print(RED + "Crawled page content: " + RESET, [page_content[0:4000]])
        info = compare_docs(blog["blog"], page_content)
        if info["is_same"]:
            all_related_docs.append({"link": link, "blog": page_content, "is_same": True, "is_enough": info["is_enough"]})
        else:
            print(RED + "==> Not the same incident (not same, crawling bloked)." + RESET, link, page_content[:200])


    # Step 3: Search the candidate queries and select related docs
    print("Identfied Links: ", identified_links)

    # New dig deeper
    # new = dig_deeper(blog["blog"], identified_links)
    # print("New identified blog: ", new["link"])
    # identified_links.append(new["link"])
    # all_related_docs.append(new)

    for query in queries[:2]: 
        print(RED + "Delve into the query: " + RESET, query)
        print(RED + "LLM Decision: " +RESET, "Google Query -> : ", query)
        google_search_results = google_web_search(query + ' "details"')
        # google_search_results = google_web_search(query + ' "What we know about"')

        results_filtering_prompt = f"""
        You are a security expert. I will give the google search results and the original blog.
        You goal is to provide the top 2 links that you think are most relevant to the incident blog. But should not include in {identified_links}.  It can help understand the root cause (including, vulnerable/misconfigured services, how to mitigate). Your output should be JSON format with `urls` as the key and the value is a list (length 2) of urls.

        This is the google search results. {str(google_search_results)} 
        This is the original blog: {blog['blog']}.
        """
        select_messages = [{"role": "user", "content": results_filtering_prompt}]
        response_message = api_call(select_messages, [])

        print(RED + "LLM selected links: " + RESET, response_message.choices[0].message.content)
        info = json.loads(response_message.choices[0].message.content)
        links = info["urls"]
        for link in links:
            if link in identified_links:
                continue
            identified_links.append(link)
            print(RED + "Delve into the link: " + RESET, link)
            # print(RED + "New Selected Link: " + RESET, link)
            page_content = click_into_page_with_browser(link)
            
            print(RED + "Crawled page content: " + RESET, [page_content[0:4000]])

            info = compare_docs(blog["blog"], page_content)
            if info["is_same"]:
                all_related_docs.append({"link": link, "blog": page_content, "is_same": True, "is_enough": info["is_enough"]})
    
    print(RED + "==> New found related documents: " + RESET)
    for doc in all_related_docs:
        print(doc["link"], doc["is_same"], doc["is_enough"], [doc["blog"][:200]])
    return all_related_docs


def enrichment(original, related_docs):
    for doc in related_docs[1:]:

        analysis_prompt = f"""
        You are a security researcher. I will give a threat report and a new found document. You goal is to see if we can add some new info to the report based on new found documents. Please merge the new info into original and mark for your changes in the enhanced report and and cite the new found doc with the following format *Your changes* (link to new found document).
        
        You will generate increasingly entity-dense threat report based on the new found document. Repeat the following 2 steps 2 times.
        Step 1: Identify 1-4 informative Entities (";" delimited) from the new found document which are missing from the previously generated threat report.
        Step 2: Write a new, denser threat report to merge every entity and detail from the previous summary plus the Missing Entities.

        A Missing Entity is:
        - Relevant: to the main story.
        - Specific: descriptive yet concise (5 words or fewer).
        - Novel: not in the previous summary.
        - Faithful: present in the new found document.
        - Anywhere: located anywhere in the new found document.
        
        Guidelines:
        - Merge the new Entities into the original report. Mark the new information with *Your changes* (link to new found document). Do not create a new key (e.g., 'Added info').
        - re-write the previous summary to improve flow and make space for additional entities.
        - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
        - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
        - Missing entities can appear anywhere in the new summary.
        - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.

        Answer in JSON. it has two keys. One is "thoughts", which described you step-by step thinks. Another is final_report.
        """

        # """
        # You will generate increasingly entity-dense threat report based on the new found document. Repeat the following 2 steps 2 times.

        # Step 1: Identify 1-4 informative Entities (";" delimited) from the new found document which are missing from the previously generated threat report.
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


        old_analysis_prompt = f"""

        You are a security researcher. I will give a threat report and a new found documents. You goal is to see if you can add some new info to the report based on new found documents. please mark for your changes
        in the enhanced report.

        You will generate increasingly entity-dense summaries based on the new found document. Repeat the following 2 steps 2 times.

        Step 1: Identify 1-4 informative Entities (";" delimited) from the new Article which are missing from the previously generated summary.
        Step 2: Write a new, denser summary of identical length which covers every entity and detail from the previous summary plus the Missing Entities.

        A Missing Entity is:
        - Relevant: to the main story.
        - Specific: descriptive yet concise (5 words or fewer).
        - Novel: not in the previous summary.
        - Faithful: present in the Article.
        - Anywhere: located anywhere in the Article.
        
        Guidelines:
        - Make every word count: re-write the previous summary to improve flow and make space for additional entities.
        - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
        - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
        - Missing entities can appear anywhere in the new summary.
        - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.
        
        Remember, use the exact same structure for each summary. 
        Answer in JSON. it has two keys. One is "thoughts", which should be a list (length 2) of dictionaries whose keys are "Missing_Entities" and "new_threat_report". Another is final_report. Please inlculde you changes in the end of the report.
        """
        
        new_prompt = """
        You are a security researcher. I will give a threat report and a new found documents. You goal is to see if you can add some new info to the report based on new found documents. please add mark for your changes
        output the enhanced report.

        You will generate increasingly concise, entity-dense summaries of the above Article. Repeat the following 2 steps 5 times.

        Step 1: Identify 1-3 informative Entities (";" delimited) from the Article which are missing from the previously generated summary.
        Step 2: Write a new, denser summary of identical length which covers every entity and detail from the previous summary plus the Missing Entities.

        A Missing Entity is:
        - Relevant: to the main story.
        - Specific: descriptive yet concise (5 words or fewer).
        - Novel: not in the previous summary.
        - Faithful: present in the Article.
        - Anywhere: located anywhere in the Article.
        
        Guidelines:
        - The first summary should be long (4-5 sentences, ~80 words) yet highly non-specific, containing little information beyond the entities marked as missing. Use overly verbose language and fillers (e.g., "this article discusses") to reach ~80 words.
        - Make every word count: re-write the previous summary to improve flow and make space for additional entities.
        - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
        - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
        - Missing entities can appear anywhere in the new summary.
        - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.
        
        Remember, use the exact same number if words for ehch summary. 
        Answer in JSON. The JSON should be a list (length 5) of dictionaries whose keys are "Missing_Entities" and "Denser_Summary".
        """


        messages = [
            {"role": "system", "content": analysis_prompt},
        ]

        misconf_qeustion = f"The original report is: {original}. The new found document is: {doc}"
        print(RED + "===> The new found document is: " + RESET, doc)
        messages.append({"role": "user", "content": misconf_qeustion})

        # response_message = api_call(messages, [], json_enabled=False)
        response_message = api_call(messages, [])
        
        json_response = json.loads(response_message.choices[0].message.content)
        
        original = json_response["final_report"]
        print(RED + "===> The enhanced report is: "  + RESET)
        print(response_message.choices[0].message.content)
        # console = Console()
        # md = Markdown(original)
        # aligned_md = Align.left(md)
        # console.print(md)
    
    return original


def get_titles_processed():
    list_of_titles = []
    if not os.path.isfile(output_filename):
        return list_of_titles
    with open(output_filename, 'r') as f:
        for line in f:
            info = json.loads(line)
            list_of_titles.append(info["title"])
    return list_of_titles


# titles_processed = get_titles_processed()
titles_processed = []
print(f"the list: {titles_processed}")
fw = open(output_filename, "w")
num = 0
with open(input_filename) as f:
    for line in f:
        info = json.loads(line)
        info["title"] = ''.join([char for char in info["title"] if char not in ['#','@',':','|','/','\\','*','\'','\"','?']])
        num += 1
        
        # if num < 2:
        #     continue
        if num > 2:
            break
        
        print(RED +  f"==> The input is: " + RESET)
        print(info)

        if info["title"] in titles_processed:
            print(info["title"] + " has been processed. Continue to the next case.\n")
            continue

        print(RED +  f"==> Start to process the blog: " + RESET)
        print("link: ", info['url'])
        print("title: ", info['title'])
        link = info["url"]
        blog = click_into_page_with_browser(link, is_text=False)
        print(f"Blog: {blog[:2000]} ...........")

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

        related_docs = find_related_ones({"link": info["url"], "blog": blog})

        # Enhance the documents
        print(RED +  f"=> Enhance the blog: {info['url']}" + RESET)
        analysis_prompt = f"""
            You are a security expert. I will give a report/blog on the Internet. You need to analyze it to understand the root cause (including, vulnerable/misconfigured services), how to detect this problem, and the mitigation behind the incident.

            You should provide a signature in the following format:    
            Incident: Shanghai Police Datalake Leak
            
            Root cause: the root cause behind the indicent including vulnerable/misconfigured services. e.g., Misconfigured Kibana instance 
            
            Threat Actor/group/campaign: Who carried out the attack? In could a orgainze a malware family, etc (if known)
            
            Organization/industry/location: Who was targeted/vicim? (if known)
            
            Start date – Eend date: When did the attack happen? (if known)

            MITRE TTPs: How was the attack carried out?  (if known)

            Impact: 100,000 records leaked.  **how many devices people impacted or the financial losses**

            Mitigation: (How to protect myself?) e.g., Secure the Kibana instance with authentication credentials. and **Detailed Steps for mitigation**

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
            
            IoCs: How do I know I am affected? (for example, IP, domain, hash, etc). If the document does not have IoCs, please output "No IoCs found". If the document has IoCs, please provide all the IoCs you found in the document.
            """

        messages = [
            {"role": "system", "content": analysis_prompt},
        ]

        misconf_qeustion = f"Here is the blog: {blog}."
        messages.append({"role": "user", "content": misconf_qeustion})
        response_message = api_call(messages, [], json_enabled=False)
        original = response_message.choices[0].message.content

        print(RED + "==> The first enhanced one: " + RESET)
        console = Console()
        md = Markdown(original)
        aligned_md = Align.left(md)
        console.print(md)

        # merge related doc together to ehnchace the density
        new_ti = enrichment(original, related_docs)

        print(RED + "==> The original one: " + RESET)
        console = Console()
        md = Markdown(info["content"])
        aligned_md = Align.left(md)
        console.print(md)   
        print(RED +  "The Enhanced Data is: " + RESET)
        print(new_ti)

        md_filename = "output/"+info["title"]+".md"
        with open(md_filename,"w", encoding='utf-8') as mdf:
            mdf.write(f"Source: [{info['url']}]({info['url']})\n\n")
            mdf.write("# "+info["title"] + "\n\n")
            mdf.write(response_message.choices[0].message.content)
            mdf.write("\n")

        # print(response_message.choices[0].message.content)
        info["enhanced"] = new_ti
        info["related_docs"] = [i["link"] for i in related_docs]
        fw.write(json.dumps(info) + "\n")
        fw.flush()
        # break

'''
=============useless code====================
md_filename = "empty-output/"+info["title"]+".md"
if os.path.isfile(md_filename):
    out_md_filename = "empty-output-tmp/"+info["title"]+".md"
else:
    md_filename = "output/"+info["title"]+".md"
    if os.path.isfile(md_filename):
        out_md_filename = "output-tmp/"+info["title"]+".md"
    else:
        print(f"no file for {info['title']}")
print (f"{num}  {info['url']}")

with open(out_md_filename, 'w', encoding='utf-8') as outfile:
    outfile.write(f"Source: [{info['url']}]({info['url']})\n\n")
    try:
        with open(md_filename, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
    except:
        with open(md_filename, 'r') as infile:
            outfile.write(infile.read())
continue
'''