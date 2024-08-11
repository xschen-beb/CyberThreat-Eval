import json
import sys
import os

from rich.console import Console
from rich.markdown import Markdown
from rich.align import Align

from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

# for exponential backoff
from tenacity import (retry, stop_after_attempt, wait_random_exponential)  
from search_engine import google_web_search, click_into_page

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
                )


def dig_deeper(blog):
    sys_prompt = "You are a security expert.  I will give a blog, your goal is to identify if it is critial securty event. If yes, please provide basic summary which incluiding the impacted service, the impact, etc. You outout should be json format with is_critical, summary, service, impact as the key."

    # Update the system prompt
    messages = [
        {"role": "system", "content": sys_prompt},
    ]

    misconf_qeustion = f"Here is the blog: {blog}."

    messages.append({"role": "user", "content": misconf_qeustion})

    print(RED + "Step 1:" + RESET, "Ask the model to identify if it is a critical security event.")

    response_message = api_call(messages, [])

    # print(response_message)
    # print(response_message.choices[0])

    response = response_message.choices[0].message.content
    print(RED + "LLM Decision: " +RESET, response)
    response_dict = json.loads(response)
    if response_dict["is_critical"]:
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
            Please provide the top 1 link that you think are most relevant to the incident. It can help understand the root cause (including, vulnerable/misconfigured services, how to mitigate). Your output should be json format with link as the key.
            """
            messages.append({"role": "user", "content": results_filtering_prompt})
            response_message = api_call(messages, [])
            # print(response_message)
            print(RED + "LLM Selected Link: " + RESET, response_message.choices[0].message.content)
            info = json.loads(response_message.choices[0].message.content)
            link = info["link"]
            while True: 
                # print(RED + "New Selected Link: " + RESET, link)
                page_content = click_into_page(link)
                
                print("Page Content: ", [page_content])

                content_analysis_prompt = f"""
                This is the detailed information of the link you provided. 
                {page_content}
                Please analyze this report to identify if these blogs have enough info to help people understand the root cause (including, vulnerable/misconfigured services, how to mitigate) bechind the incident.
                If yes, please output <END>
                Else, please provide a new search query or a new link to search more information. with the key "query" or "link".
                """
                messages.append({"role": "user", "content": content_analysis_prompt})
                response_message = api_call(messages, [])
                # print(response_message)
                print(RED + "LLM Analysis Decision: " +RESET, [response_message.choices[0].message.content])
                

                
                if response_message.choices[0].message.content.strip() == "<END>":
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

            
        print(RED + "Step 3:" + RESET, "Ask the model to help identify related misconfiguration signatures.")
        misconf_qeustion = """
        You are a security expert. I will give a report on the Internet. You should provide some signature in the following format:    
        
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
        Here is the blog: {blog} and page content {page_content}.
        """

        messages.append({"role": "user", "content": misconf_qeustion})
        
        response_message = api_call(messages, [])

        print(response_message)
        print(response_message.choices[0].message.content)

    else:
        print("This is not a critical security event.")



def categorize(blogs):
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
def get_titles_processed():
    list_of_titles = []
    if not os.path.isfile(output_filename):
        return list_of_titles
    with open(output_filename, 'r') as f:
        for line in f:
            info = json.loads(line)
            list_of_titles.append(info["title"])
    return list_of_titles
    
titles_processed = get_titles_processed()
print (f"the list: {titles_processed}")
fw = open(output_filename, "a")
num = 0
with open(input_filename) as f:
    for line in f:

        info = json.loads(line)
        info["title"] = ''.join([char for char in info["title"] if char not in ['#','@',':','|','/','\\','*','\'','\"','?']])
        num += 1
        
        '''
        if num < 2:
            continue
        if num > 5:
            break
        '''
        print(f"The input is: {info}")
        if info["title"] in titles_processed:
            print(info["title"] + " has been processed. Continue to the next case.\n")
            continue

        print(RED +  f"=> Processing the blog: {info['url']} " + RESET)
        link = info["url"]
        blog = click_into_page(link)
        print(f"Blog: {blog[:300]} ...........")

        if not categorize(blog):
            # dig_deeper(blog)
            md_filename = "empty-output/"+info["title"]+".md"
            with open(md_filename,"w") as mdf:
                mdf.write(f"Source: [{info['url']}]({info['url']})\n\n")
                mdf.write("# "+info["title"] + "\n\n")
                mdf.write("This blog does not have enough info to help people understand the root cause behind the incident.")
                mdf.write("\n")
            fw.write(json.dumps(info) + "\n")
            fw.flush()
            continue

        analysis_prompt = f"""
            You are a security expert. I will give a report/blog on the Internet. You need to analyze it to understand the root cause (including, vulnerable/misconfigured services), how to detect this problem, and the mitigation behind the incident.

            You should provide a signature in the following format:    
            Incident: Shanghai Police Datalake Leak

            Root cause: Misconfigured Kibana instance

            Impact: 100,000 records leaked.  **how many devices people impacted and the financial losses**

            Mitigation: Secure the Kibana instance with authentication credentials. and **Detailed Steps for mitigation**

            Detection Signature:
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
            
            IoCs: (for example, IP, domain, hash, etc). If the document does not have IoCs, please output "No IoCs found". If the document has IoCs, please provide all the IoCs you found in the document.
            """

        messages = [
            {"role": "system", "content": analysis_prompt},
        ]

        misconf_qeustion = f"Here is the blog: {blog}."

        messages.append({"role": "user", "content": misconf_qeustion})

        print(RED +  f"=> Analyzing the blog: {info['url']}" + RESET)
        response_message = api_call(messages, [], json_enabled=False)
        print(RED + "==> The original one: " + RESET)
        console = Console()
        md = Markdown(info["content"])
        aligned_md = Align.left(md)
        console.print(md)   
        print(RED +  "The Enhanced Data is: " + RESET)
        
        console = Console()
        md = Markdown(response_message.choices[0].message.content)
        aligned_md = Align.left(md)
        console.print(md)
        md_filename = "output/"+info["title"]+".md"
        with open(md_filename,"w", encoding='utf-8') as mdf:
            mdf.write(f"Source: [{info['url']}]({info['url']})\n\n")
            mdf.write("# "+info["title"] + "\n\n")
            mdf.write(response_message.choices[0].message.content)
            mdf.write("\n")

        # print(response_message.choices[0].message.content)
        info["enhanced"] = response_message.choices[0].message.content
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