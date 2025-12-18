import json
import sys
import os
import traceback
print(sys.path)
import argparse
import time
import logging
import tiktoken
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tenacity import (retry, stop_after_attempt, wait_random_exponential)
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI, OpenAI
import requests
from datetime import datetime
from collections import Counter
from contextlib import redirect_stdout
from azure.identity import InteractiveBrowserCredential, TokenCachePersistenceOptions
from rich.console import Console
from rich.markdown import Markdown
from rich.align import Align
import playwright
from search_engine import (
    google_web_search,
    click_into_page_with_browser,
    bing_search,
)

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
_AUTH_SCOPE = "https://cognitiveservices.azure.com/.default"
_CREDENTIAL = DefaultAzureCredential()
total_llm_call = 0
total_tokens = 0
_SEARCH_ENGINE = "bing"
_HEADLESS_FLAG = False

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

@retry(wait=wait_random_exponential(min=1, max=120), stop=stop_after_attempt(3))
def api_call(client, messages, model_name, json_enabled=True):
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


def compare_docs(client, original, new_doc, model_name):
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            if num_tokens_from_string(new_doc, model_name) > 120000:
                new_doc = new_doc[:80000]

            content_analysis_prompt = f"""
            You are a security expert. I will give you a original blog and a new found document. You goal is to step-by-step identify if the new found document described the same incident comapred to the original blog (i.e. talking the same thing with different aspects). First, identify if the new found document described a similar incident. 
            Then, please analyze the new found document to identify if it has enough info to help people understand the root cause (including, vulnerable/misconfigured services, how to mitigate) bechind the incident. If a doc has some IoCs related to this incident, we identify it as enough.
            Note that if a new found document covers a few different incidents, we called it a cyber-intel-brief, mark it as not the same incident.
            Please output your decision in JSON format with the key "is_same", "is_similar" or "is_enough" and "explanation". The value for "is_same", "is_similar" and "is_enough" must be True/False.
            The original blog is: {original}
            The new found document is: {new_doc}
            """
            
            new_messages = []
            new_messages.append({"role": "user", "content": content_analysis_prompt})

            response_message = api_call(client, new_messages, model_name)
            debug_print(
                RED + "LLM's Analysis (Relevant and enough) " + RESET,
                [response_message.choices[0].message.content],
            )

            info = json.loads(response_message.choices[0].message.content)
            return info
            
        except Exception as e:
            retry_count += 1
            debug_print(RED + f"Error in compare_docs function (attempt {retry_count}/{max_retries}): {str(e)}" + RESET)
            traceback.print_exc()
            
            if retry_count < max_retries:
                debug_print(RED + f"Retrying compare_docs..." + RESET)
                time.sleep(2)  # Wait a bit before retrying
            else:
                # Return default value after all retries failed
                debug_print(RED + f"All retry attempts failed in compare_docs" + RESET)
                return {"is_same": False, "is_enough": False, "explanation": f"Error after {max_retries} attempts: {str(e)}"}


def find_related_ones(client, blog, enable_query, model_name):
    try:
        debug_print(RED + "==> Find more related documents." + RESET)

        # Step 1: Ask the model to generate search queries and to extract links
        sys_prompt = """
        You are a security expert. I will give a report on the Internet. I want to delve deeper into this incident to see what the reason behind and tech details. Can you sugggest a search query (including threat actor, malware,CVE, date, service or victims) that I can use to search in the search engine to understand the tech details of this attack/incident. Do not include general words like "cybersecurity", "personal information", etc because they are too general to search. You can use the threat actor name, malware name, victims, CVEs, or similar attack chain.
        You output should be JSON format with queries the key. Please also provide the links that described the same incident, CVE or links that may include IoCs (e.g., The indicators of compromise for this blog entry can be found <a href="https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/a/a-look-into-pikabot-spam-wave-campaign/ioc-pikabot-spam-campaign.txt"> here </a>) mentioned in the blog with the key "links". Output JSON format: {"queries": ["query1", "query2"], "links": ["link1", "link2"]}
        """
        
        messages = [
            {"role": "system", "content": sys_prompt},
        ]
        
        # Try to generate search queries with retry
        info = {"queries": [], "links": []}
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                if num_tokens_from_string(blog["blog"], model_name) > 120000:
                    blog["blog"] = blog["blog"][:80000]
                    
                misconf_qeustion = f"Here is the blog: {blog['blog']}."
                debug_print(RED + "==> Original html: " + RESET)
                debug_print(blog["blog"][0:2000])
                
                messages.append({"role": "user", "content": misconf_qeustion})
                response_message = api_call(client, messages, model_name)
                info = json.loads(response_message.choices[0].message.content)
                messages.append(
                    {"role": "assistant", "content": response_message.choices[0].message.content}
                )
                break  # Success - exit retry loop
                
            except Exception as e:
                retry_count += 1
                debug_print(RED + f"Error generating search queries (attempt {retry_count}/{max_retries}): {str(e)}" + RESET)
                traceback.print_exc()
                
                if retry_count < max_retries:
                    debug_print(RED + f"Retrying search query generation..." + RESET)
                    time.sleep(2)  # Wait a bit before retrying
                else:
                    debug_print(RED + f"All retry attempts failed in search query generation" + RESET)

        queries = info.get("queries", [])
        debug_print(RED + "Get Candidate Queries and Links: " + RESET)
        debug_print("queries: ", queries)
        links = info.get("links", [])
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
            try:
                debug_print(RED + "Delve into the link: " + RESET, link)
                if link in identified_links:
                    debug_print("==> The link has been identified. Skip it.")
                    continue
                if link.endswith(".png"):
                    continue
                identified_links.append(link)

                page_content = None
                # Try to get page content with retry
                for attempt in range(3):  # 3 attempts for page fetching
                    try:
                        page_content = click_into_page_with_browser(link, headless_flag=_HEADLESS_FLAG)
                        debug_print(RED + "Crawled page content: " + RESET, [page_content[0:4000]])
                        break  # Success - exit retry loop
                    except Exception as e:
                        if attempt < 2:  # 0, 1 - retry on attempts 0 and 1
                            debug_print(f"Error fetching page (attempt {attempt+1}/3): {str(e)}")
                            time.sleep(2)  # Wait before retrying
                        else:
                            debug_print(RED + f"Failed to fetch page after 3 attempts: {str(e)}" + RESET)
                            page_content = None
                            break
                
                if page_content is None:
                    continue  # Skip this link if we couldn't fetch it
                            
                # Document comparison with retry
                info = {"is_same": False, "is_enough": False}
                for attempt in range(3):
                    try:
                        info = compare_docs(client, blog["blog"], page_content, model_name)
                        break  # Success - exit retry loop
                    except Exception as e:
                        if attempt < 2:
                            debug_print(f"Error comparing documents (attempt {attempt+1}/3): {str(e)}")
                            time.sleep(2)
                        else:
                            debug_print(RED + f"Failed to compare documents after 3 attempts: {str(e)}" + RESET)
                            
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
                        RED + "==> Not the same incident (not same, crawling blocked)." + RESET,
                        link,
                        page_content[:200],
                    )
                
            except Exception as e:
                debug_print(RED + f"Error processing link {link}: {str(e)}" + RESET)
                traceback.print_exc()
                continue

        # Step 3: Search the candidate queries and select related docs
        debug_print("==> All Identified Links: ", identified_links)

        if not enable_query:
            return all_related_docs

        for query in queries[:3]:
            try:
                debug_print(RED + "Delve into the query: " + RESET, query)
                debug_print(RED + "LLM Decision: " + RESET, "Google Query -> : ", query)
                
                # Search engine query with retry
                google_search_results = []
                for attempt in range(3):
                    try:
                        if _SEARCH_ENGINE == "bing":
                            google_search_results = bing_search(query)
                            debug_print(RED + "Bing Search Results: " + RESET, google_search_results)
                        elif _SEARCH_ENGINE == "google":
                            google_search_results = google_web_search(query)
                            debug_print(RED + "Google Search Results: " + RESET, google_search_results)
                        break  # Success - exit retry loop
                    except Exception as e:
                        if attempt < 2:
                            debug_print(f"Error in search engine query (attempt {attempt+1}/3): {str(e)}")
                            time.sleep(2)
                        else:
                            debug_print(RED + f"Failed to search after 3 attempts: {str(e)}" + RESET)
                            google_search_results = []

                if not google_search_results:
                    debug_print(RED + f"Search query '{query}' returned no results, skipping" + RESET)
                    continue
                
                results_filtering_prompt = f"""
                You are a security expert. I will give the google search results and the original blog.
                You goal is to provide the top 2 links that you think are most relevant to the incident blog. But should not include in {identified_links}.  It can help understand the root cause (including, vulnerable/misconfigured services, how to mitigate). Your output should be JSON format with `urls` as the key and the value is a list (length 2) of urls.

                This is the google search results. {str(google_search_results)} 
                This is the original blog: {blog['blog']}.
                """
                select_messages = [{"role": "user", "content": results_filtering_prompt}]
                
                # Filter results with retry
                links = []
                for attempt in range(3):
                    try:
                        response_message = api_call(client, select_messages, model_name)
                        debug_print(
                            RED + "LLM selected links: " + RESET,
                            response_message.choices[0].message.content,
                        )
                        info = json.loads(response_message.choices[0].message.content)
                        links = info.get("urls", [])
                        break  # Success - exit retry loop
                    except Exception as e:
                        if attempt < 2:
                            debug_print(f"Error parsing LLM selected links (attempt {attempt+1}/3): {str(e)}")
                            time.sleep(2)
                        else:
                            debug_print(RED + f"Failed to parse LLM selected links after 3 attempts: {str(e)}" + RESET)
                            # links = []
                            links = [item['url'] for item in google_search_results]


                # links = [item['url'] for item in google_search_results]
                print(f"==> Links: {links}")
                for link in links:
                    try:
                        if link in identified_links:
                            continue
                        identified_links.append(link)
                        debug_print(RED + "Delve into the link: " + RESET, link)
                        
                        # Fetch page content with retry
                        page_content = f"Crawling blocked: Unknown error"
                        for attempt in range(3):
                            try:
                                page_content = click_into_page_with_browser(
                                    link, headless_flag=_HEADLESS_FLAG
                                )
                                debug_print(RED + "Crawled page content: " + RESET, [page_content[0:4000]])
                                break  # Success - exit retry loop
                            except Exception as e:
                                if attempt < 2:
                                    debug_print(f"Error crawling page (attempt {attempt+1}/3): {str(e)}")
                                    time.sleep(2)
                                else:
                                    debug_print(RED + f"Failed to crawl page after 3 attempts: {str(e)}" + RESET)
                                    page_content = f"Crawling blocked: {str(e)}"

                        # Compare documents with retry
                        for attempt in range(3):
                            try:
                                info = compare_docs(client, blog["blog"], page_content[0:10000], model_name)
                                if info["is_same"] in [True, "True", "true"]:
                                    all_related_docs.append(
                                        {
                                            "link": link,
                                            "is_same": True,
                                            "is_enough": info["is_enough"],
                                        }
                                    )
                                break  # Exit loop regardless of result
                            except Exception as e:
                                if attempt < 2:
                                    debug_print(f"Error comparing documents (attempt {attempt+1}/3): {str(e)}")
                                    time.sleep(2)
                                else:
                                    debug_print(RED + f"Failed to compare documents after 3 attempts: {str(e)}" + RESET)
                    except Exception as e:
                        debug_print(RED + f"Error processing link {link}: {str(e)}" + RESET)
                        traceback.print_exc()
                        continue
            except Exception as e:
                debug_print(RED + f"Error processing query '{query}': {str(e)}" + RESET)
                traceback.print_exc()
                continue

        debug_print(RED + "==> New found related documents: " + RESET)
        for doc in all_related_docs:
            try:
                debug_print(doc["link"], doc.get("is_same", False), doc.get("is_enough", False))
            except Exception as e:
                debug_print(RED + f"Error outputting document info: {str(e)}" + RESET)
                
        return all_related_docs
    except Exception as e:
        debug_print(RED + f"Error in find_related_ones function: {str(e)}" + RESET)
        traceback.print_exc()
        # Return currently collected content or empty list
        return all_related_docs if 'all_related_docs' in locals() else []


def related_urls(client, url, model_name):
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            link = url
            
            # Try to fetch the blog content with retry
            blog = None
            for attempt in range(3):
                try:
                    blog = click_into_page_with_browser(
                        link, is_text=False, headless_flag=_HEADLESS_FLAG
                    )
                    break  # Success - exit retry loop
                except Exception as e:
                    if attempt < 2:
                        debug_print(f"Error crawling page (attempt {attempt+1}/3): {str(e)}")
                        time.sleep(2)
                    else:
                        debug_print(RED + f"Failed to crawl page after 3 attempts: {str(e)}" + RESET)
                        return []
            
            if blog is None:
                debug_print(f"==> Could not fetch content for URL: {url}")
                return []
            
            # debug_print(f"Blog: {blog[:2000]} ...........")

            debug_print(RED + "==> INPUT URLS: " + RESET, url)
            related_docs = find_related_ones(client, {"link": url, "blog": blog}, True, model_name)
            debug_print(RED + "==> Related doc numbers: " + RESET, len(related_docs))

            return related_docs
            
        except Exception as e:
            retry_count += 1
            debug_print(RED + f"Error in related_urls function (attempt {retry_count}/{max_retries}): {str(e)}" + RESET)
            traceback.print_exc()
            
            if retry_count < max_retries:
                debug_print(RED + f"Retrying related_urls..." + RESET)
                time.sleep(2)  # Wait a bit before retrying
            else:
                debug_print(RED + f"All retry attempts failed in related_urls" + RESET)
                return []
