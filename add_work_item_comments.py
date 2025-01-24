import os
import requests
import base64
import json

# CASSIE = "" # Set your CASSIE TOKEN with os.envir
# pat = CASSIE
# os.environ['ADO_PERSONAL_ACCESS_TOKEN'] = CASSIE
# pat = os.environ['ADO_PERSONAL_ACCESS_TOKEN']
authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')
project_name = "Cassandra"
organization = "threat-intel"

def add_comment_to_workitem(work_item_id, markdown):
    # Headers for API requests
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Basic ' + authorization,
        'Content-Type': 'application/json'
    }

    # Azure DevOps project and organization detail
    # Work item API URL
    comment_url = f'https://dev.azure.com/{organization}/{project_name}/_apis/wit/workitems/{work_item_id}/comments?format=markdown&api-version=7.2-preview.4'

    # Comment data
    comment_data = {
        "text": markdown
    }

    # Make the API request to add a comment
    response = requests.post(comment_url, headers=headers, data=json.dumps(comment_data))

    # Handle the API response
    try:
        print("Comment added successfully!")
        print(f"{response.status_code} - {response.text}")
        return response.json()
    except:
        print(f"Error: {response.status_code} - {response.text}")
        return {"error": response.text, "status_code": response.status_code}


# Example usage
if __name__ == "__main__":
    work_item_id = 18456155
    markdown = "### testing"
    response = add_comment_to_workitem(work_item_id)
