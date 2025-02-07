import os
import sys

module_path = os.path.abspath(os.path.join("../.."))
if module_path not in sys.path:
    sys.path.append(module_path)
# from threat_research import *
from recommendations.utils import *
from azure.identity import InteractiveBrowserCredential, TokenCachePersistenceOptions
import requests
from mdti_description.crawl_malpedia import *

def threat_research_playground(url):
    for _ in range(1):
        try:
            new_ti, related_docs = threat_research_core(url)
            text_output = ""

            # Add the source URL
            text_output += f"Source: [{url}]({url})\n\n"

            # Process related articles
            text_output += "## Related articles (describing the same threat) \n"
            unique_urls = set()
            for doc in related_docs:
                normalized_url = standardize_url(doc["link"])
                unique_urls.add(normalized_url)
            for unique_url in unique_urls:
                text_output += f"- {unique_url}\n"
            text_output += "\n"

            # Enriched Document Section
            text_output += "## Enriched Doc (enrichments marked with *content*(link)): \n"
            paste_ioc_section = "#### paste IoC\n"
            ttps = ""

            for key, value in new_ti.items():
                if key == 'Threat actor/group/campaign':
                    text_output += f"#### {key} \n {value} \n\n"
                    threat_actors = eval(get_actor(value))
                    context = pipeline(threat_actors, 'oneti', token)
                    if '\n\n' in context:
                        context = context.replace('\n\n', '')
                    text_output += f"- Information from oneti: \n {context}\n\n"

                elif key == 'Root cause':
                    text_output += f"#### {key} \n {value} \n\n"
                    actors = eval(get_root_cause_with_llm(value))
                    context = root_cause_pipeline(actors, token)
                    if context:
                        context = context.replace('\n\n', '')
                        text_output += f"- Additional context: \n {context}\n\n"

                elif key == 'MITRE TTPs':
                    ttps += f"{value}"

                elif key == 'IoCs':
                    continue

                elif key == 'Mitigation Steps':
                    mitigation = process_all_ttps(ttps)
                    if mitigation:
                        text_output += f"- {rec['title']} Reason: {rec['reason']}\n"
                    else:
                        text_output += f"#### {key} \n {value} \n"
                    text_output += '\n'

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

            text_output += "#### IoCs:\n"

            iocs_dict = {}  # Use a dictionary to remove duplicates by value
            # for each url, extract iocs from url directly
            blog_for_urls = []

            iocs_dict = {}  # Use a dictionary to remove duplicates by value
            for link in unique_urls:
                blog = click_into_page_with_browser(
                    link, is_text=False, headless_flag=False
                )
                date = add_date(blog)
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
            print(unique_iocs)
            white_list = get_white_list_urls('All Intelligence Feeds.csv')
            unique_urls.update(white_list)

            for ioc_data in unique_iocs:
                ioc_value = ioc_data["value"]
                # if ioc_value in unique_urls or filter_url(ioc_value, unique_urls):
                if ioc_value in unique_urls or filter_url(ioc_value, unique_urls):
                    continue
                ioc_type = ioc_data["type"]
                pub_date = ioc_data['publish_date']
                ioc_source = ioc_data.get('source', 'No link provided')  # Ensure a default value
                blogs_for_target_source = next((entry["blog"] for entry in blog_for_urls if entry["source"] == ioc_source), None)

                try:
                    if ioc_type in ["hash_md5", "hash_sha1", "hash_sha256"]:
                        ioc_type_for_check = 'hash'
                    else:
                        ioc_type_for_check = ioc_type

                    is_malicious = check_ioc(ioc_value, ioc_type_for_check)
                    if is_malicious == True:
                        if ioc_value in blogs_for_target_source and "True" in llm_judgment_for_ioc_in_blog(ioc_value, blogs_for_target_source):
                            # ioc_source = ioc_data.get('source', 'No link provided')
                            text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source}))  Publish date: {pub_date}\n\n"
                            paste_ioc_section += f"{ioc_value}\n\n"

                            print(f"The {ioc_type} {ioc_value} is malicious.")
                        else:
                            print(f"The {ioc_type} {ioc_value} not in urls.")
                            continue
                            # text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source})) \n\n"
                            # text_output += f"Not found for {ioc_type} {ioc_value} in url. \n\n"

                    elif is_malicious == False:
                        print(f"The {ioc_type} {ioc_value} is clean.")
                    else:
                        if ioc_value in blogs_for_target_source and "True" in llm_judgment_for_ioc_in_blog(ioc_value, blogs_for_target_source):
                            text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source}))   Publish date: {pub_date}\n"
                            text_output += f"Found in URL, Not found for {ioc_type} {ioc_value} in VT. \n\n"
                            print(f"The {ioc_type} {ioc_value} in urls but not in VT.")
                        else:
                            print(f"Not Found in URL and VT for {ioc_type} {ioc_value}.")
                            continue
                            # text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source})) \n"
                            # text_output += f"Not Found in URL and VT for {ioc_type} {ioc_value}. \n\n"
                except Exception as e:
                    print(e)
            
            # For more IoCs note
            text_output += "- For more IoCs, please refer to the above links. \n\n"

            # Append the paste IoC section
            text_output += paste_ioc_section + "\n"

            return text_output
        except AttributeError as e:
            print(f"Error in processing the blog: {e}")
            continue


def get_access_token(client_id, scopes):
    """Get access token using InteractiveBrowserCredential"""
    options = {"client_id": client_id}
    # browser_cred = InteractiveBrowserCredential(**options)
    browser_cred = InteractiveBrowserCredential(**options, cache_persistence_options=TokenCachePersistenceOptions(allow_unencrypted_storage=True))
    token = browser_cred.get_token(*scopes)
    return token

# TODO
def search_articles(token, query):
    """Search for articles based on query"""
    url = 'https://onetiproda.trafficmanager.net/api/paperboy/articles/search?Active=true&ActiveVersion=true'
    headers = { 
        "Authorization": f"Bearer {token}", 
        "accept": "application/json",
        "X-Riskiq-Client": "unknown"
    }
    params = {"Title": query}

    try: 
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        articles = response.json()
        return articles
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON deserialization error: {json_err}")

def get_articles(token, query):
    """Get articles based on the given query"""
    url = "https://onetiproda.trafficmanager.net/api/paperboy/articles?api-version=2023-01-01"
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "X-Riskiq-Client": "unknown"
    }
    params = {"Title": query}

    try:    
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        articles = response.json()
        return articles
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON deserialization error: {json_err}")

def get_profiles(token, query):
    """Get profiles based on the given query"""
    url = "https://onetiproda.trafficmanager.net/api/paperboy/profiles?api-version=2023-01-01"
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "X-Riskiq-Client": "unknown"
    }
    params = {"Title": query}

    try:    
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        profiles = response.json()
        return profiles
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON deserialization error: {json_err}")

def get_user_object(token):
    """Get the user object for debugging"""
    url = "https://onetiproda.trafficmanager.net/api/debug/who?api-version=2023-01-01"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        user_object = response.json()
        return user_object
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON deserialization error: {json_err}")


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

    for actor in actors:
        profiles = get_profiles(token.token, actor)
        articles = get_articles(token.token, actor)
        
        if profiles["data"]["totalPages"] > 0:
            print("="*20 +" Using oneti profile " + "="*20 + '\n')
            for i in range(min(profiles['data']['totalPages'], 5)):
                text = profiles["data"]["content"][i]['description']
                rec_text = find_recommendation_section(text)
                if rec_text:
                    recommendations += rec_text + "\n\n"

        else:
            print("="*20 +" Using related articles " + "="*20 + '\n')
            if articles["data"]["totalPages"] == 0:
                continue
            for i in range(min(articles['data']['totalPages'], 5)):
                text = str(articles["data"]["content"][i]['content'])
                rec_text = find_recommendation_section(text)
                if rec_text:
                    recommendations += rec_text + "\n\n"

    return recommendations if recommendations else "No recommendations found."

def validate_recommendations_with_llm(ttp_description, recommendations):
    # Construct the LLM prompts including a system prompt for context
    system_prompt = """
    You are an expert cybersecurity analyst with extensive knowledge in identifying and mitigating threats.
    Your task is to analyze the provided TTP description and a set of recommendations. Extract and return only the sections of the recommendations that are directly and highly relevant to the TTP description. Ensure that the extracted parts address the specific aspects of the TTP effectively.
    
    Instructions:
    - Focus solely on relevance; disregard any recommendations that do not directly pertain to the TTP.
    - Maintain the original wording of the relevant recommendations without adding or altering content.
    - Present the extracted recommendations in a clear and organized manner.
    - If no relevant recommendations are found, respond with "No relevant recommendations found."
    """

    # Define a precise user prompt with clear instructions and context
    user_prompt = f"""
    TTP Description:
    {ttp_description}
    
    Recommendations:
    {recommendations}
    
    Please extract and return only the parts of the recommendations that are directly and highly relevant to the TTP description above. 
    
    Results:
    """

 
    # Prepare messages for the LLM API
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
 
    # Call the LLM API
    response_message = api_call(messages, [], model="gpt-4-32k")
 
    # Parse the LLM response
    try:
        relevant_part = response_message.choices[0].message.content.strip()
        return relevant_part
    except Exception as e:
        print(f"Error in LLM response: {e}")
        return "Unable to extract relevant parts"
    

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

    response_message = api_call(messages, temperature=0.01, model='gpt-4o', json_enabled=False)

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

if __name__ == '__main__':
    """
    import pandas as pd
    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)
    # actors = 'Storm-0558'
    actors = ['Amethyst Rain']
    actors = ['Storm-0558']
    profiles = get_articles(token.token, actors)
    print(profiles['data']['content'][0])
    name = profiles['data']['content'][0]['name']
    link = f"https://sip.security.microsoft.com/intel-profiles/{name}"
    print(link)
    """
    text = """
Source: [https://isc.sans.edu/diary/rss/31550](https://isc.sans.edu/diary/rss/31550)

## Related articles (describing the same threat) 
- https://isc.sans.edu/diary/31550

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident 
 SSL and TLS Support Changes in 2024 

#### Root cause 
 The root cause behind the incident is the continued support for deprecated versions of SSL and TLS (i.e., SSL 2.0, SSL 3.0, TLS 1.0, and TLS 1.1) on various web and email servers. These outdated protocols are not configured in line with current security best practices and likely indicate that the servers lack important updates and patches. 

#### Threat actor/group/campaign 
 Not applicable (this is a general security issue rather than a targeted attack). 

#### Organization/industry/location 
 This issue affects various web and email servers globally, across multiple industries. *Shodan scans detected between 124 and 166 million web servers accessible from the internet during the course of the year* (https://isc.sans.edu/diary/31550). 

#### Start date – End date 
 The data covers the year 2024. 

#### MITRE TTPs 
 {'T1078': 'Valid Accounts, Confidence: Medium. Justification: The use of outdated SSL/TLS protocols can be exploited by attackers to gain unauthorized access to systems.', 'T1040': 'Network Sniffing, Confidence: High. Justification: Deprecated SSL/TLS protocols are vulnerable to network sniffing attacks, allowing attackers to intercept and decrypt sensitive information.', 'T1557': 'Man-in-the-Middle, Confidence: High. Justification: The use of outdated cryptographic protocols makes systems susceptible to man-in-the-middle attacks, where attackers can intercept and alter communications.', 'T1190': 'Exploit Public-Facing Application, Confidence: Medium. Justification: Public-facing web and email servers using outdated SSL/TLS protocols can be exploited by attackers to gain access to the underlying systems.'}

#### Impact 
 The impact is widespread, affecting millions of web and email servers globally. The exact number of records or financial losses is not specified. 
 """
    
    rec_list = ['Recommendations to protect against RaaS', 'Recommendations to identify and mitigate cryptojacking attacks', 'Recommendations to protect against Information Stealers', 'Recommendations to protect against Malvertising', 'Recommendations to protect against phishing attacks', 'Recommendations to protect against Mobile Malware', 'Recommendations to protect against CVE-2024-3400 - command injection vulnerability', 'Tips for preventing keylogging', 'Guidance for CobaltStrike', 'Guidance for Botnets', 'Mitigate zero-day vulnerabilities', 'Mitigating data security incidents', 'Recommendations to protect IoT specific devices', 'Recommendations for supply-chain attacks', 'Social Engineering ']
    rec = gen_dict_recommendation_from_report(text)
    tech = pd.read_csv('recommendations/RecDict.csv')
    res = get_recommendation_by_title(tech, rec)
    print(res[0], res[1])
    




    # rec = mdti_recommendation_pipeline(actors, token)
    # tech = pd.read_csv('recommendations/Techniques.csv')['ID']
    # numbers = 0
    # items = ['T1059', 'T1190']
    # for item in items:
        # rec_dict = process_rec_dict_ttps(item)
        # print(f"Recommendation: \n\n {rec_dict}")
        # related = validate_recommendations_with_llm(rec_dict[0]["ttp_name"], rec_dict[0]["description"])
        # print(related)
    # oneti_pipeline(actors, token)
    # profiles = get_articles(token.token, 'Qubitstrike')
    # profiles = get_profiles(token.token, actors)
    # profiles = get_profiles(token.token, actors)
    # profiles = get_profiles(token.token, 'Qubitstrike')
    # content = profiles["data"]["content"][0]["content"]
    
    # text = profiles["data"]["content"][0]['description']

    # start = text.find("## Recommendations")
    # if start == -1:
        # print("")
        
    # end = text.find("##", start + 2)
    # if end == -1:
        # end = len(text)
        
    # 提取内容
    # recommendations = text[start:end].strip()
    # print(recommendations)