import os
import requests
import base64
import json

# Azure DevOps Personal Access Token (PAT)
TOKEN = ""
CASSIE = ""

# os.environ['ADO_PERSONAL_ACCESS_TOKEN'] = TOKEN
os.environ['ADO_PERSONAL_ACCESS_TOKEN'] = CASSIE
pat = os.environ['ADO_PERSONAL_ACCESS_TOKEN']
authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')

# Headers for API requests
headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic ' + authorization,
    'Content-Type': 'application/json'
}

# Azure DevOps project and organization details
# project_name = "xuafeng9" 
project_name = "Cassandra"
# organization = "LLM-OSINT"
organization = "threat-intel"

# Work item API URL
comment_url = f'https://dev.azure.com/{organization}/{project_name}/_apis/wit/workitems/18456155/comments?format=markdown&api-version=7.2-preview.4'


comment_data = {
    "text": "### This is a new comment.\n ##### this is for testing,"
}

# Make the API request to add a comment
response = requests.post(comment_url, headers=headers, data=json.dumps(comment_data))

# Handle the API response
try:  # 201 indicates resource creation success
    print("Comment added successfully!")
    # print("Response:", json.dumps(response.json(), indent=2))
    print(f"{response.status_code} - {response.text}")
except:
    print(f"Error: {response.status_code} - {response.text}")
