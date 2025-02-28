import sys
import os
import json
import re
import csv
import pandas as pd
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from azure.identity import InteractiveBrowserCredential, TokenCachePersistenceOptions
import requests
from src.search_engine import click_into_page_with_browser
from datetime import datetime, timedelta
import base64

def get_access_token(client_id, scopes):
    """Get access token using InteractiveBrowserCredential"""
    options = {"client_id": client_id}
    # browser_cred = InteractiveBrowserCredential(**options)
    browser_cred = InteractiveBrowserCredential(**options, cache_persistence_options=TokenCachePersistenceOptions(allow_unencrypted_storage=True))
    token = browser_cred.get_token(*scopes)
    return token


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


def get_recent_urls(pat):
    authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + authorization
    }

    # Azure DevOps project URL for the Wiql API
    project_name = "Cassandra"
    organization = "threat-intel"
    wiql_url = f'https://dev.azure.com/{organization}/{project_name}/_apis/wit/wiql?api-version=7.1'

    # Wiql query in JSON format
    wiql_query = {
        "query": """
            SELECT
                [System.Id],
                [System.Title]
            FROM workitems
            WHERE
                [System.TeamProject] = @project
                AND [System.CreatedDate] > @today - 100
                AND [System.WorkItemType] = 'Source'
                AND [Cassandra.SourceType] IN ('Blog', 'OSINT', 'URL')
            ORDER BY [Cassandra.SourceDatePublished] DESC
        """
    }
    
    # Get the current date and the date two days ago
    today = datetime.today().date()

    # Make the POST request to execute the Wiql query
    response = requests.post(wiql_url, headers=headers, json=wiql_query)

    # Parse the response and filter results
    if response.status_code == 200:
        data = response.json()
        return data


def save_osint_articles_to_json(token, pat, workitems, output_file):
    results = []
    valid_ttp_pattern = re.compile(r"^T\d{4}(?:\.\d{3})? - .+")

    for item in workitems:
        project_url = item['url']
        # Create basic auth header using the PAT
        authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + authorization
        }
        
        # Get project details from the project_url
        try:
            response = requests.get(url=project_url, headers=headers)
            data = response.json()
            # Extract the source title from the project fields
            source_title = data['fields']['System.Title']
            query = source_title
            
            # Get articles using the source title as the query
            articles = get_articles(token.token, query)
            # Skip if no article content or not enough tags
            if not articles["data"]["content"] or len(articles["data"]["content"][0]['tags']) == 0:
                continue
            
            article = articles["data"]["content"][0]
            article_title = article['title']
            article_content = article['content']
            ttp_list = article['tags']
            # Remove 'OSINT' from the TTPs list
            filtered_ttps = [tag for tag in ttp_list if valid_ttp_pattern.match(tag)]
            
            # Skip if no valid TTP is found
            if not filtered_ttps:
                continue
            
            # Create a result dictionary for this article
            result_entry = {
                "title": article_title,
                "content": article_content,
                "ttps": filtered_ttps,
                "source": source_title
            }
            results.append(result_entry)
            
            # Optional: print article details
            print(f"Title: {article_title}\n")
            print(f"Content: {article_content[:200]}\n")
            print(f"TTPs: {filtered_ttps}\n")
        except Exception as e:
            print(f"Error: {e}")
            continue
    
    # Save all results to a JSON file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(results, outfile, ensure_ascii=False, indent=4)
    print(f"Results have been saved to {output_file}")


def main():
    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)
    pat = os.getenv('ADO_PERSONAL_ACCESS_TOKEN')
    
    data = get_recent_urls(pat)
    workitems = data['workItems']
    print(workitems)
    
    # Save the extracted article details to articles.json
    save_osint_articles_to_json(token, pat, workitems, "100-days-articles.json")
    
    with open("100-days-articles.json", 'r', encoding='utf-8') as f:
       articles = json.load(f)

    count = 0
    for article in articles:
        raw_ttps = article.get("ttps", [])
        count += len(raw_ttps)
        print(len(raw_ttps))

    print(f"All TTPs: {count}")


if __name__ == '__main__':
    csv_file='src/TTP_Mapping.csv'
    ttp_mapping = {}
    csv_file = 'src/TTP_Mapping.csv'

    # Read the CSV file using pandas
    df = pd.read_csv(csv_file, encoding='utf-8')

    # Select only the "TechniqueID" and "name" columns
    mapping_df = df[['TechniqueID', 'name']]

    # Convert the selected DataFrame to a dictionary mapping TechniqueID to name
    ttp_mapping = dict(zip(mapping_df['TechniqueID'], mapping_df['name']))

    # Print the resulting dictionary
    print(ttp_mapping)