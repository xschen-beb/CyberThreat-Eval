import os
import sys
parent_directory = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_directory)

from azure.identity import InteractiveBrowserCredential
import requests
from mdti_description.crawl_malpedia import *

def get_access_token(client_id, scopes):
    """Get access token using InteractiveBrowserCredential"""
    options = {"client_id": client_id}
    browser_cred = InteractiveBrowserCredential(**options)
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

"""
def oneti_pipeline(actors, token):
    actors_info = ""
    names = []
    links = []

    for actor in actors:
        print(f"Processing {actor}: ... \n")
        profiles = get_profiles(token.token, actor)
        articles = get_articles(token.token, actor)
        if profiles["data"]["totalPages"] > 0 and profiles:
            print("="*20 +" Using oneti profile " + "="*20 + '\n')
            content = profiles["data"]["content"]
            print(profiles["data"]["totalPages"])
            names.append(actor)
            for i in range(min(profiles['data']['totalPages'], 5)):
                actors_info += str(profiles["data"]["content"][i]['description'])
                name = profiles['data']['content'][0]['name']
                link = f"https://sip.security.microsoft.com/intel-profiles/{name}"
                links.append(link)
        elif articles['data']['totalPages'] > 0 and articles:
            print("="*20 +" Using related articles " + "="*20 + '\n')
            content = articles["data"]["content"]
            names.append(actor)
            for i in range(min(articles['data']['totalPages'], 5)):
                actors_info += str(articles["data"]["content"][i]['content'])
                link_name = content[0]['guid']
                link = f"https://sip.security.microsoft.com/intel-profiles/{link_name}"
                links.append(link)
        else:
            continue
    
    context = augment_threat_actor_context(actors, actors_info)
    print(context)
    return names, links, context

"""

"""
def oneti_pipeline(actors, token):
    actors_info = ""
    names = []
    links = []

    for actor in actors:
        print(f"Processing {actor}: ... \n")
        profiles = get_profiles(token.token, actor)
        articles = get_articles(token.token, actor)

        if profiles["data"]["totalPages"] > 0 and profiles:
            print("="*20 + " Using oneti profile " + "="*20 + '\n')
            content = profiles["data"]["content"]
            print(profiles["data"]["totalPages"])
            
            # Check if actor's profile link is unique before adding
            name = profiles['data']['content'][0]['name']
            link = f"https://sip.security.microsoft.com/intel-profiles/{name}"
            if link not in links:
                names.append(actor)
                links.append(link)
            
            for i in range(min(profiles['data']['totalPages'], 5)):
                actors_info += str(profiles["data"]["content"][i]['description'])
        
        elif articles['data']['totalPages'] > 0 and articles:
            print("="*20 + " Using related articles " + "="*20 + '\n')
            content = articles["data"]["content"]
            
            # Check if article link is unique before adding
            # link_name = content[0]['guid']
            # link = f"https://sip.security.microsoft.com/intel-profiles/{link_name}"
            # if link not in links:
                # names.append(actor)
                # links.append(link)
            
            for i in range(min(articles['data']['totalPages'], 5)):
                actors_info += str(articles["data"]["content"][i]['content'])
        else:
            continue

    # Only call augment_threat_actor_context if names is not empty
    if names:
        context = augment_threat_actor_context(names, actors_info)
        print(context)
    else:
        context = ""

    return names, links, context
"""

def oneti_pipeline(actors, token):
    names = []
    links = []
    count = 0
    context = ""  # Use a single string to accumulate contexts

    for actor in actors:
        print(f"Processing {actor}: ... \n")
        profiles = get_profiles(token.token, actor)
        articles = get_articles(token.token, actor)

        actors_info = ""

        if profiles and profiles["data"]["totalPages"] > 0 :
            print("=" * 20 + " Using oneti profile " + "=" * 20 + '\n')
            content = profiles["data"]["content"]
            print(profiles["data"]["totalPages"])

            # Generate unique link for the actor's profile
            name = profiles['data']['content'][0]['name']
            link = f"https://sip.security.microsoft.com/intel-profiles/{name}"
            if link not in links:
                names.append(actor)
                links.append(link)
                count += 1
                for i in range(min(profiles['data']['totalPages'], 1)):
                    actors_info += str(profiles["data"]["content"][i]['description'])

        elif articles and articles['data']['totalPages'] > 0:
            print("=" * 20 + " Using related articles " + "=" * 20 + '\n')
            content = articles["data"]["content"]

            for i in range(min(articles['data']['totalPages'], 5)):
                actors_info += str(articles["data"]["content"][i]['content'])
                count += 1

        else:
            print(f"No profiles or articles found for {actor}")
            continue

        # Generate context for the actor using `augment_threat_actor_context`
        if actors_info.strip():
            actor_context = augment_threat_actor_context(actor, actors_info)
            context += f"- {actor_context}\n"
            print(f"Context for {actor}:\n{actor_context}\n")
        else:
            print(f"No information found for {actor} to augment context.")


        if count == 3:
            break
        
    return names, links, context


if __name__ == '__main__':
    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)
    actors = ['Lazarus Group', 'Citrine Sleet', 'APT38', 'BlueNoroff', 'Stardust Chollima', 'Jade Sleet', 'UNC4899', 'Slow Pisces']
    # n, l, c = oneti_pipeline(actors, token)
    # print(n)
    # print(l)
    query = "Inside the LockBit Arsenal - The StealBit Exfiltration Tool"
    articles = get_articles(token.token, query)
    print(articles['data'])



    '''
    user_object = get_user_object(token.token)
    if user_object:
        print(user_object)
    
    query = "WIRTE"
    # articles = get_articles(token.token, query)
    articles = get_profiles(token.token, query)
    print(articles["data"].keys())
    print(articles["data"]["totalPages"])
    content = articles["data"]["content"]
    actors_info = ''
    for i in range(min(articles['data']['totalPages'], 5)):
        actors_info += str(articles["data"]["content"][i]['content'])

    context = augment_threat_actor_context(query, actors_info)
    print(context)
    with open('oneai_wirte_selected_context.txt', 'w') as fo:
        fo.write(context)
    ''' 
