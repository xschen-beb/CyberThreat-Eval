import os
import requests
import base64
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
from tqdm import tqdm
import sys
sys.stdout.reconfigure(encoding='utf-8')


def get_work_items(pat):
    authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + authorization
    }

    # Azure DevOps project URL for the Wiql API
    project_name = "Cassandra"
    organization = "threat-intel"
    wiql_url = f'https://dev.azure.com/{organization}/{project_name}/_apis/wit/wiql?api-version=7.1'

    # WIQL query in JSON format
    wiql_query = {
        "query": """
            SELECT
                [System.Id],
                [System.Title],
                [Custom.Subject],
                [Custom.IntermediateSubject],
                [Custom.Modifier],
                [Microsoft.VSTS.Common.Priority]
            FROM workitems
            WHERE
                [System.TeamProject] = 'Cassandra'
                AND [System.WorkItemType] = 'Source'
                AND [Custom.Subject] <> ''
        """
    }
    
    today = datetime.today().date()
    two_days_ago = today - timedelta(days=2)

    # Make the POST request to execute the Wiql query
    response = requests.post(wiql_url, headers=headers, json=wiql_query)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return {}

    data = response.json()
    work_items = data.get("workItems", [])

    return work_items


def get_article_data(pat, output_file):
    authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + authorization
    }

    # Azure DevOps project URL for the Wiql API
    project_name = "Cassandra"
    organization = "threat-intel"

    work_items = get_work_items(pat)

    filtered_data = []
    return_dict = {}  # We'll store { str(work_item_id): { ... } }

    for item in tqdm(work_items):
        work_item_id = item["id"]

        # Get detailed info for the work item
        detail_url = (
            f"https://dev.azure.com/{organization}/{project_name}"
            f"/_apis/wit/workitems/{work_item_id}?api-version=7.1"
        )
        detail_response = requests.get(detail_url, headers=headers, timeout=120)

        if detail_response.status_code != 200:
            print(f"Detail request error: {detail_response.status_code} for ID {work_item_id}")
            continue

        work_item_details = detail_response.json()
        fields = work_item_details.get("fields", {})

        # Extract relevant fields
        date_published = fields.get("Cassandra.SourceDatePublished")
        state = fields.get("System.State", "")
        priority = fields.get("Microsoft.VSTS.Common.Priority")  # Could be None
        url_field = fields.get("Cassandra.SourceUrl", "")

        iocs_extracted = fields.get("Cassandra.SourceIOCsExtracted")  # Might be None
        source_text = fields.get("Cassandra.SourceText")             # Might be None
        description = fields.get("System.Description")
        subject = fields.get('Custom.Subject')
        IntermediateSubject = fields.get('Custom.IntermediateSubject')
        SubjectWeight = fields.get('Custom.SubjectWeight')
        modifier = fields.get('Custom.Modifier')
        ModifierWeight = fields.get('Custom.ModifierWeight')
        PriorityWeight = fields.get('Custom.PriorityWeight')
        if not source_text:
            continue

        soup = BeautifulSoup(source_text, 'html.parser')

        plain_text = soup.get_text(separator=' ', strip=True)
        plain_text = plain_text.replace('&nbsp;', '')


        # Determine the score
        if priority is None and state == "Rejected":
            continue
        elif (priority is None and state != "Rejected"):
            continue
        else:
            score = priority

        # Build a minimal dictionary with the required fields
        minimal_info = {
            "id": work_item_id,
            "state": state,
            "priority": priority,
            "score": score,
            "source_url": url_field,
            "Cassandra.SourceIOCsExtracted": iocs_extracted,
            "System.Description": description,
            "Cassandra.SourceText": plain_text,
            "subject": subject,
            "intermediate_subject": IntermediateSubject,
            "subject_weight": SubjectWeight,
            "modifier": modifier,
            "modifier_weight": ModifierWeight,
            "priority_weight": PriorityWeight
        }

        filtered_data.append(minimal_info)

        # Also store in the return_dict, keyed by the work item ID as string
        return_dict[str(work_item_id)] = {
            "id": work_item_id,
            "state": state,
            "priority": priority,
            "score": score,
            "source_url": url_field,
            "Cassandra.SourceIOCsExtracted": iocs_extracted,
            "System.Description": description,
            "Cassandra.SourceText": plain_text,
            "subject": subject,
            "intermediate_subject": IntermediateSubject,
            "subject_weight": SubjectWeight,
            "modifier": modifier,
            "modifier_weight": ModifierWeight,
            "priority_weight": PriorityWeight
        }

    # Save filtered_data to a file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(filtered_data, f, indent=4, ensure_ascii=False)

    print(f"Filtered data saved to {output_file}")
    return return_dict


def test_single_triage(work_items):
    authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + authorization
    }
    project_name = "Cassandra"
    organization = "threat-intel"
    for item in tqdm(work_items):
        work_item_id = item["id"]

        # Get detailed info for the work item
        detail_url = (
            f"https://dev.azure.com/{organization}/{project_name}"
            f"/_apis/wit/workitems/{work_item_id}?api-version=7.1"
        )
        detail_response = requests.get(detail_url, headers=headers, timeout=120)

        if detail_response.status_code != 200:
            print(f"Detail request error: {detail_response.status_code} for ID {work_item_id}")
            continue

        work_item_details = detail_response.json()
        fields = work_item_details.get("fields", {})
        return fields


if __name__ == '__main__':
    pat = os.getenv('ADO_PERSONAL_ACCESS_TOKEN')
    output_file = '0528-triage.json'
    get_article_data(pat, output_file)
    # work_items = get_work_items(pat)
    # print(test_single_triage(work_items))

