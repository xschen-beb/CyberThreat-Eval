# access: https://eng.ms/docs/microsoft-security/cloud-ecosystem-security/azure-data-governance/ti-collection-platform/interflow/seceng-interflow/oneti
# https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.managedidentitycredential?view=azure-python
# api: https://eng.ms/docs/microsoft-security/cloud-ecosystem-security/azure-data-governance/ti-collection-platform/interflow/oneti

# MDTI UI: https://sip.security.microsoft.com/
# OneTI Swagger UI: XXXX

from azure.identity import InteractiveBrowserCredential
import requests

# Set up the options with the client ID
options = {
    "client_id": "a92e7da0-0dec-4653-bae0-8b61258fd045"
}
# Create the InteractiveBrowserCredential
browser_cred = InteractiveBrowserCredential(**options)
# Define the scopes
scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
# Get the access token
token = browser_cred.get_token(*scopes)
# print(token)

def search_articles(token):
    url = "https://onetiproda.trafficmanager.net/api/paperboy/profiles/search?api-version=2023-01-01"
    headers = { 
        "Authorization": f"Bearer {token}", 
        "accept": "application/json",
        "X-Riskiq-Client": "unknown"
    }
    query_params = {
    }

    data = {
        "query": "microsoft",
    }

    try: 
        response = requests.post(url, headers=headers, params=query_params,data=data)
        response.raise_for_status()
        articles = response.json()
        return articles
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON deserialization error: {json_err}")
        

def get_articles(token):
    url = "https://onetiproda.trafficmanager.net/api/paperboy/articles?api-version=2023-01-01"
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "X-Riskiq-Client": "unknown"
    }

    try:    
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        articles = response.json()
        return articles
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON deserialization error: {json_err}")


def get_profiles(token):
    url = "https://onetiproda.trafficmanager.net/api/paperboy/profiles?api-version=2023-01-01"
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "X-Riskiq-Client": "unknown"
    }

    try:    
        response = requests.get(url, headers=headers)
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
    url = "https://onetiproda.trafficmanager.net/api/debug/who?api-version=2023-01-01"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    # params = {
    #     "Title": "microsoft"
    # }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the status is 4xx or 5xx
        user_object = response.json()  # Deserialize the JSON response
        return user_object
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON deserialization error: {json_err}")

# Example usage
tmp_token = token.token
# Test the debug API
user_object = get_user_object(tmp_token)
if user_object:
    print(user_object)

#  List all the articles
res = get_articles(tmp_token)
print(res["data"].keys())
print(res["data"]["totalPages"])

# List all the profiles
res = get_profiles(tmp_token)
print(res["data"].keys())
print(res["data"]["totalPages"])

content = res['data']['content']
for con in content:
    fw = open('new_content.txt', 'a+')
    fw.write(str(con) + '\n')
# print(res['data']['content'])
# Search for articles
res = search_articles(tmp_token)
print(res)



