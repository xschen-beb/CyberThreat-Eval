import os
import sys
parent_directory = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_directory)

from azure.identity import InteractiveBrowserCredential
import requests
from mdti_description.crawl_malpedia import *
from tqdm import tqdm
from utils import evaluate_root_cause_context

def find_files_with_threat_actor(directory):
    files_with_threat_actors = []

    # Use tqdm to wrap os.walk for progress tracking
    for root, _, files in tqdm(list(os.walk(directory)), desc="Scanning Directories", unit="directory"):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if extract_threat_actor_info(file_path):
                    files_with_threat_actors.append(file_path)
    return files_with_threat_actors


def get_access_token(client_id, scopes):
    """Get access token using InteractiveBrowserCredential"""
    options = {"client_id": client_id}
    browser_cred = InteractiveBrowserCredential(**options)
    token = browser_cred.get_token(*scopes)
    return token


def extract_root_cause(file_path):
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

    match = re.search(r"#### Root cause\s*(.*?)(?=\n####|\Z)", content, re.DOTALL)
    return match.group(1).strip() if match else None


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


def get_root_cause_with_llm(root_cause):
    sys_prompt = f"""
    ### Task description:
    You are an expert in cybersecurity. I will provide you with an IoC report. Please extract the relevant and potential threat malwares (if it has other names, extract them.) in the **list format** from the "root cause" section of the report and ensure that the extracted term is suitable for use in a search query. For each output, it should be a phrase or a single word without any prefixes. If no specific threat actor is specified, the output should be ['None'].

    ### Example:
    Report Content: The incident was caused by a North Korean IT worker cluster (CL-STA-0237) exploiting a U.S.-based IT services company's credentials and infrastructure to carry out phishing attacks using malware-infected video conference apps, including InvisibleFerret malware *Your changes* (https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/) and BeaverTail stealer *Your changes* (https://objective-see.org/blog/blog_0x7A.html). *The attackers also posed as prospective employers to lure developers into fake interviews, delivering updated BeaverTail and InvisibleFerret malware* (https://thehackernews.com/2024/10/n-korean-hackers-use-fake-interviews-to.html). *The malware targets job seekers via platforms like LinkedIn and X, distributing through files disguised as legitimate applications such as MiroTalk and FreeConference* (https://www.infosecurity-magazine.com/news/beavertail-malware-job-seekers/). 
    ['InvisibleFerret', 'BeaverTail']

    Report Content: A compromised access token from a highly privileged developer, Aidosmf (aidosmf@gmail.com), allowed attackers to publish malicious versions of the @lottiefiles/lottie-player package on npm, designed to steal crypto wallet assets. *The attack stemmed from a phishing attack on an employee's NPM account* (https://www.securityweek.com/lottie-player-supply-chain-attack-targets-cryptocurrency-wallets/). *The employee's laptop was quarantined* (https://www.securityweek.com/lottie-player-supply-chain-attack-targets-cryptocurrency-wallets/). *Exaforce was engaged for rapid Incident Response and ongoing cloud detection and response* (https://lottiefiles.com/blog/inside-lottiefiles/resolution-of-security-incident-with-lottiefiles-lottie-player-package). *Attack leveraged an npm automation token to bypass 2FA controls* (https://thehackernews.com/2024/10/lottiefiles-issues-warning-about.html). 
    ['Aidosmf']
    """

    user_prompt = f"""
    ### Task description:
    I will provide you with an IoC report. Please extract the relevant and potential malwares(if it has other names, extract them.) in the list format from the "root cause" section of the report and ensure that the extracted term is suitable for use in a search query. For each item of the list, it should be a phrase or a single word without any prefixes. If no specific threat actor is specified, the output should be ['None'].

    ### Result:
    Report Content: {root_cause}
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(new_messages, temperature=0.01, model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response


def augment_root_cause_context(root_cause, root_cause_info):
    sys_prompt = f"""
    ### Task description:
    You are an expert in cybersecurity. Based on the extracted information about the root cause from a blog, please generate a detailed context and summary about the root cause of the incident based on the report content and your knowledge. Ensure the context includes details about vulnerable or misconfigured services, exploited weaknesses, and contributing factors. Your output must be concise, professional, and factually accurate. No hallucination is allowed. Ensure the output provides sufficient information for a security professional to understand the root cause. No explanations or prefix texts like "Context:" are allowed in the output.

    ### Example:
    Root Cause: Misconfigured Kibana instance
    Context: The root cause of the incident was a misconfigured Kibana instance exposed to the Internet without authentication. This allowed attackers to inject malicious scripts and access sensitive data, resulting in data exfiltration.

    Root Cause: Exploitation of zero-day vulnerability
    Context: The incident was caused by attackers exploiting a zero-day vulnerability in a widely used web application framework, enabling unauthorized access and the deployment of ransomware on affected systems.

    Root Cause: Insufficient email filtering
    Context: The root cause was insufficient email filtering, allowing phishing emails with malicious attachments to bypass security controls and deliver malware to target devices.
    """

    user_prompt = f"""
    ### Task description:
    Based on the extracted information about the root cause from a blog, please briefly generate a detailed context and summary about the root cause of the incident based on the report content and your knowledge. No hallucination is allowed. Ensure the output is concise and provides sufficient information for a security professional to understand the root cause. No explanations or prefix texts like "Context:" are allowed in the output.

    ### Result:
    Root Cause: {root_cause}
    Report Content: {root_cause_info}
    Context:
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(new_messages, temperature=0.01, model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response

"""
def root_cause_pipeline(actors, token):
    actors_info = ""
    names = []
    links = []

    for actor in actors:
        articles = get_articles(token.token, actor)
        if articles and articles["data"]["totalPages"] > 0:
            content = articles["data"]["content"]
            
            # Check and add unique links
            for i in range(min(articles['data']['totalPages'], 5)):
                actors_info += str(content[i]['content'])
                
                # Extract link and ensure it is unique
                name = content[i]['guid']
                link = f"https://sip.security.microsoft.com/intel-profiles/{name}"
                if link not in links:
                    links.append(link)
                    names.append(actor)
        else:
            continue

    # Call augment_threat_actor_context if actors_info is not empty
    if names:
        context = augment_root_cause_context(names, actors_info)
        return names, links, context
    else:
        print("No relevant actors or unique links found.")
        return names, links, ""

"""

def root_cause_pipeline(actors, token):
    names = []
    links = []
    context = ""  # Use a single string to accumulate contexts

    for actor in actors:
        print(f"Processing actor: {actor}\n")
        articles = get_articles(token.token, actor)

        actors_info = ""

        if articles and articles["data"]["totalPages"] > 0:
            print(f"Found {articles['data']['totalPages']} pages of articles for {actor}.\n")
            content = articles["data"]["content"]

            # Process each article up to a limit of 5
            for i in range(min(articles['data']['totalPages'], 5)):
                # Generate unique link for the article
                name = content[i]['guid']
                link = f"https://sip.security.microsoft.com/intel-profiles/{name}"
                if link not in links:
                    links.append(link)
                    names.append(actor)
                    actors_info += str(content[i]['content'])

        else:
            print(f"No articles found for actor: {actor}\n")
            continue

        # Generate context for the actor using `augment_root_cause_context`
        if actors_info.strip():
            actor_context = augment_root_cause_context(actor, actors_info)
            context += f"- {actor_context}\n"
            print(f"Context for {actor} generated.\n")
        else:
            print(f"No sufficient information for {actor} to augment context.\n")

        if len(names) == 3:
            break

    if not names:
        print("No relevant actors or unique links found.")

    return names, links, context



def save_results(results, output_file):
    with open(output_file, 'a') as f:
        json.dump(results, f)
        f.write('\n')
    print(f"Results saved to {output_file}")


def raw_eval():
    directory = 'AgentGenReport'
    files = find_files_with_threat_actor(directory)

    all_results = []
    total_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    total_known_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    total_unknown_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    
    total_files = 0
    known_files = 0
    unknown_files = 0

    unknown = 0
    for file in tqdm(files, desc="Processing Files", unit="file"):
        print(f"File name: {file}")
        flag = True
        root_cause_info = extract_root_cause(file)
        root_cause = eval(get_root_cause_with_llm(root_cause_info))
        if 'None' in root_cause:
            unknown += 1
            flag = False

        evaluation_scores = evaluate_root_cause_context(root_cause, root_cause_info)
        
        if flag:
            file_results = {
                "file": file,
                "known": 'known',
                "evaluation_scores": evaluation_scores
            }
            known_files += 1
            # Sum up the scores for known files
            for key in total_known_scores:
                total_known_scores[key] += evaluation_scores.get(key, 0)
        else:
            file_results = {
                "file": file,
                "known": 'unknown',
                "evaluation_scores": evaluation_scores
            }
            unknown_files += 1
            # Sum up the scores for unknown files
            for key in total_unknown_scores:
                total_unknown_scores[key] += evaluation_scores.get(key, 0)

        save_results(file_results, "evaluation_results.json")
        all_results.append(file_results)

        # Sum up the scores for averaging later
        for key in total_scores:
            total_scores[key] += evaluation_scores.get(key, 0)
        
        total_files += 1

    # Calculate average scores for all files
    avg_scores = {key: total / total_files if total_files > 0 else 0 for key, total in total_scores.items()}

    # Calculate average scores for known files
    avg_known_scores = {key: total / known_files if known_files > 0 else 0 for key, total in total_known_scores.items()}

    # Calculate average scores for unknown files
    avg_unknown_scores = {key: total / unknown_files if unknown_files > 0 else 0 for key, total in total_unknown_scores.items()}

    # Save all results and averages to JSON file
    results_with_avg = {
        "averages": avg_scores,
        "known_averages": avg_known_scores,
        "unknown_averages": avg_unknown_scores
    }

    save_results(results_with_avg, "root_cause_raw_evaluation_results.json")

    print(f"Averages: {avg_scores}")
    print(f"Known Averages: {avg_known_scores}")
    print(f"Unknown Averages: {avg_unknown_scores}")
    print(f"Known files: {known_files}, unknown files: {unknown_files}")


def oneti_eval():
    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)

    directory = 'AgentGenReport'
    files = find_files_with_threat_actor(directory)

    all_results = []
    total_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    total_known_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    total_unknown_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    
    total_files = 0
    known_files = 0
    unknown_files = 0

    unknown = 0
    
    for file in tqdm(files, desc="Processing Files", unit="file"):
        temp = file.strip('.md').split('\\')[-1]
        fo = open(f'RootCause/{temp}.txt', 'w', encoding='utf-8')
        print(f"File name: {file}")
        flag = True
        root_cause_info = extract_root_cause(file)

        root_cause = eval(get_root_cause_with_llm(root_cause_info))
        root_cause_info = root_cause_pipeline(root_cause, token)
        
        if 'None' in root_cause or not root_cause_info:
            unknown += 1
            flag = False

        evaluation_scores = evaluate_root_cause_context(root_cause, root_cause_info)
        
        if flag:
            file_results = {
                "file": file,
                "known": 'known',
                "evaluation_scores": evaluation_scores
            }
            known_files += 1
            # Sum up the scores for known files
            for key in total_known_scores:
                total_known_scores[key] += evaluation_scores.get(key, 0)
            fo.write(root_cause_info)
        else:
            file_results = {
                "file": file,
                "known": 'unknown',
                "evaluation_scores": evaluation_scores
            }
            unknown_files += 1
            # Sum up the scores for unknown files
            for key in total_unknown_scores:
                total_unknown_scores[key] += evaluation_scores.get(key, 0)

        save_results(file_results, "evaluation_results.json")
        all_results.append(file_results)

        # Sum up the scores for averaging later
        for key in total_scores:
            total_scores[key] += evaluation_scores.get(key, 0)
        
        total_files += 1

    # Calculate average scores for all files
    avg_scores = {key: total / total_files if total_files > 0 else 0 for key, total in total_scores.items()}

    # Calculate average scores for known files
    avg_known_scores = {key: total / known_files if known_files > 0 else 0 for key, total in total_known_scores.items()}

    # Calculate average scores for unknown files
    avg_unknown_scores = {key: total / unknown_files if unknown_files > 0 else 0 for key, total in total_unknown_scores.items()}

    # Save all results and averages to JSON file
    results_with_avg = {
        "averages": avg_scores,
        "known_averages": avg_known_scores,
        "unknown_averages": avg_unknown_scores
    }

    save_results(results_with_avg, "root_cause_evaluation_results.json")

    print(f"Averages: {avg_scores}")
    print(f"Known Averages: {avg_known_scores}")
    print(f"Unknown Averages: {avg_unknown_scores}")
    print(f"Known files: {known_files}, unknown files: {unknown_files}")


if __name__ == '__main__':
    # oneti_eval()
    # raw_eval()
    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)

    # malware = ['QBot']
    malware = ['TraderTraitor', 'AppleJeus', 'InletDrift']
    names, link, res = root_cause_pipeline(malware, token)
    # print(res)
    print(names)
    print(link)
    print(res)

'''    
    directory = 'AgentGenReport'
    files = find_files_with_threat_actor(directory)
    count = 0
    for file in tqdm(files):
        # file = "AgentGenReport/1121/lumma-stealer-on-the-rise-how-telegram-channels-are-fueling-malware-proliferation.md"
        root_cause = extract_root_cause(file)
        print(root_cause)
        resp = get_root_cause_with_llm(root_cause)
        print(resp)

        # actors = ['InvisibleFerret', 'BeaverTail']
        malware = eval(resp)
        # malware = ['CL-STA-0237']
        res = root_cause_pipeline(malware, token)
        print(res)
        if not res:
            print("No specific information.")
            continue
        else:
            count += 1
    print(count)
'''