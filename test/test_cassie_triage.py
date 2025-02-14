import os
import requests
import base64
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

pat = os.getenv('ADO_PERSONAL_ACCESS_TOKEN')


def get_cassie_ttp(work_item_id):
    """
    Extracts Cassandra.FileIndicatorSummary from an Azure DevOps work item,
    formats it as Markdown, and saves it to a file.

    :param work_item_id: The ID of the Azure DevOps work item.
    :param output_file: The path to the Markdown file to save the output.
    """
    # Set up the Azure DevOps Personal Access Token (PAT)
    # Azure DevOps API URL
    authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Basic ' + authorization
    }
    project_url = f'https://dev.azure.com/threat-intel/Cassandra/_apis/wit/workitems/{work_item_id}?api-version=7.1'

    # Make the request
    response = requests.get(url=project_url, headers=headers)

    # Parse the JSON response
    try:
        data = response.json()
        print(data)

    except json.JSONDecodeError:
        print("Failed to parse JSON. Response text:")
        print(response.text)


def get_cassie_triage(work_item_id):
    """
    Extracts Cassandra.FileIndicatorSummary from an Azure DevOps work item,
    formats it as Markdown, and saves it to a file.

    :param work_item_id: The ID of the Azure DevOps work item.
    :param output_file: The path to the Markdown file to save the output.
    """
    # Set up the Azure DevOps Personal Access Token (PAT)
    # Azure DevOps API URL
    authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Basic ' + authorization
    }
    project_url = f'https://dev.azure.com/threat-intel/Cassandra/_apis/wit/workitems/{work_item_id}?api-version=7.1'

    # Make the request
    response = requests.get(url=project_url, headers=headers)

    # Parse the JSON response
    try:
        data = response.json()

        # Access 'Cassandra.FileIndicatorSummary' if it exists
        if 'fields' in data and 'Cassandra.FileIndicatorSummary' in data['fields'] or 'Cassandra.NetworkIndicatorSummary' in data['fields']:
            file_indicator_summary = data['fields']['Cassandra.FileIndicatorSummary']
            network_indicator_summary = data['fields']['Cassandra.NetworkIndicatorSummary']
            markdown_output = "##### "

            # Parse HTML content with BeautifulSoup
            for summary in [file_indicator_summary, network_indicator_summary]:
                soup = BeautifulSoup(summary, 'html.parser')
                tables = soup.find_all('table')  # Find all <table> tags

                if not tables:
                    print("No <table> elements found in the summary.")
                    continue

                for table in tables:
                    # Find context (e.g., preceding <p> or <h3> tags)
                    context = []
                    prev_element = table.find_previous_sibling()
                    while prev_element and prev_element.name in ['p', 'h3', 'h2', 'h1']:
                        context.append(prev_element.text.strip())
                        prev_element = prev_element.find_previous_sibling()

                    # Reverse context list to get correct order
                    context.reverse()
                    context_text = "\n".join(context)

                    # Extract headers and rows
                    headers = [th.text.strip() for th in table.find_all('th')]  # Extract headers
                    rows = [
                        [td.text.strip() for td in row.find_all(['td', 'th'])]
                        for row in table.find_all('tr')
                    ]

                    # Format table as Markdown
                    if headers:
                        markdown_table = "| " + " | ".join(headers) + " |\n"
                        markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
                        for row in rows[1:]:  # Skip the header row
                            markdown_table += "| " + " | ".join(row) + " |\n"
                    else:
                        markdown_table = "\n"

                    # Combine context and table
                    markdown_section = f"{context_text}\n\n{markdown_table}"
                    markdown_output += markdown_section + "\n\n"
            if markdown_output != "##### ":
                return markdown_output
            else:
                return ""

        else:
            return ""

    except json.JSONDecodeError:
        print("Failed to parse JSON. Response text:")
        print(response.text)


def get_recent_urls():
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
                [System.WorkItemType],
                [System.Title],
                [System.AssignedTo],
                [System.State],
                [System.Tags],
                [Cassandra.SourceDatePublished],
                [System.Description],
                [Custom.SentinelArtifactId],
                [Cassandra.SourceIOCsExtracted],
                [Cassandra.SourceUrl],
                [Cassandra.SourceType]
            FROM workitems
            WHERE
                [System.TeamProject] = @project
                AND [System.CreatedDate] > @today - 2
                AND [System.WorkItemType] = 'Source'
                AND [Cassandra.SourceType] IN ('Blog', 'OSINT', 'URL')
            ORDER BY [Cassandra.SourceDatePublished] DESC
        """
    }
    
    # Get the current date and the date two days ago
    today = datetime.today().date()
    two_days_ago = today - timedelta(days=2)

    # Make the POST request to execute the Wiql query
    response = requests.post(wiql_url, headers=headers, json=wiql_query)

    # Parse the response and filter results
    if response.status_code == 200:
        data = response.json()
        filtered_data = []
        data_dict = {}

        for work_item in data.get("workItems", []):
            work_item_id = work_item['id']

            # Get detailed info for the work item
            detail_url = f'https://dev.azure.com/{organization}/{project_name}/_apis/wit/workitems/{work_item_id}?api-version=7.1'
            detail_response = requests.get(detail_url, headers=headers)

            if detail_response.status_code == 200:
                work_item_details = detail_response.json()
                fields = work_item_details['fields']

                # Extract date and state
                date_published = fields.get('Cassandra.SourceDatePublished')
                state = fields.get('System.State', '')
                url = fields.get('Cassandra.SourceUrl')
                asssigned_to = fields.get('System.AssignedTo')
                # if not asssigned_to:
                #     continue
                if not url:
                    continue
                # Parse the date and filter based on conditions
                if date_published and state != 'Rejected':
                    published_date = datetime.strptime(date_published.split("T")[0], "%Y-%m-%d").date()
                    if two_days_ago <= published_date:
                        print(work_item_id)
                        filtered_data.append({
                            "ID": work_item_id,
                            "Title": fields.get('System.Title', 'No Title'),
                            "State": state,
                            "URL": url,
                            "PublishedDate": date_published,
                            "AssignedTo": asssigned_to
                        })
                        data_dict.update({str(work_item_id): url})

        # Save filtered data to a file
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f'scheduled_logs/filtered_data_{current_time}.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, indent=4, ensure_ascii=False)

        print("Filtered data saved to 'scheduled_logs/filtered_data.json'")
        return data_dict
    else:
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == '__main__':
    cassie = get_cassie_triage("18474995")
    print(f"Cassie: {cassie}")
    # data_dict = get_recent_urls()
    # print(data_dict)
    # links_dict = {'18447575': 'https://intezer.com/blog/malware-analysis/weaponized-software-targets-chinese/', '18446105': 'https://www.bleepingcomputer.com/news/security/gdpr-complaints-filed-against-tiktok-temu-for-sending-user-data-to-china/', '18445871': 'https://www.guidepointsecurity.com/blog/ransomhub-affiliate-leverage-python-based-backdoor/#new_tab', '18445870': 'https://www.welivesecurity.com/en/eset-research/under-cloak-uefi-secure-boot-introducing-cve-2024-7344/#new_tab', '18445859': 'https://www.bleepingcomputer.com/news/security/w3-total-cache-plugin-flaw-exposes-1-million-wordpress-sites-to-attacks/', '18445858': 'https://www.bleepingcomputer.com/news/security/microsoft-expands-testing-of-windows-11-admin-protection-feature/', '18445848': 'https://blog.talosintelligence.com/find-the-helpers/', '18445841': 'https://www.bleepingcomputer.com/news/security/us-cracks-down-on-north-korean-it-worker-army-with-more-sanctions/', '18445842': 'https://www.bleepingcomputer.com/news/security/biden-signs-executive-order-to-bolster-national-cybersecurity/', '18445819': 'https://blog.sekoia.io/sneaky-2fa-exposing-a-new-aitm-phishing-as-a-service/', '18445827': 'https://news.sophos.com/en-us/2025/01/16/gootloader-inside-out/', '18445820': 'https://www.bleepingcomputer.com/news/security/wolf-haldenstein-law-firm-says-35-million-impacted-by-data-breach/', '18445821': 'https://www.bleepingcomputer.com/news/security/ftc-sues-godaddy-for-years-of-poor-hosting-security-practices/', '18445822': 'https://www.bleepingcomputer.com/news/security/new-uefi-secure-boot-flaw-exposes-systems-to-bootkits-patch-now/', '18445823': 'https://www.bleepingcomputer.com/news/security/mfa-failures-the-worst-is-yet-to-come/', '18445791': 'https://cyble.com/blog/ukraine-cyberthreat-landscape-2024/', '18445792': 'https://cyble.com/blog/hitachi-energy-critical-risk/', '18445860': 'https://www.cisa.gov/news-events/ics-advisories/icsa-25-016-06', '18445861': 'https://www.cisa.gov/news-events/ics-advisories/icsa-25-016-01', '18445862': 'https://www.cisa.gov/news-events/ics-advisories/icsa-25-016-05', '18445863': 'https://www.cisa.gov/news-events/ics-advisories/icsa-25-016-04', '18445864': 'https://www.cisa.gov/news-events/ics-advisories/icsa-25-016-07'}
    skipped = []
    not_skipped = []
    # for work_id, link in links_dict.items():
        # work_item_id = '18445819'  # Replace with your work item ID
        # output_file = 'full_md.md'  # Output Markdown file path
    
    

    # Wiql query in JSON format
    
    # Make the POST request to execute the Wiql query
    # response = requests.post(wiql_url, headers=headers, json=wiql_query)
    

    # Parse the JSON response

    """
    if response.status_code == 200:
        data = response.json()
        print("Query Results:")
        for work_item in data.get("workItems", []):
            # work_item_id = work_item['id']
            work_item_id = 37
            print(f"Fetching details for Work Item ID: {work_item_id}")
            
            # Get detailed info for the work item
            detail_url = f'https://dev.azure.com/{organization}/{project_name}/_apis/wit/workitems/{work_item_id}?api-version=7.1'
            detail_response = requests.get(detail_url, headers=headers)

            if detail_response.status_code == 200:
                work_item_details = detail_response.json()
                print(f"Details for Work Item ID {work_item_id}:")
                print(work_item_details)  # Print full JSON
                break  # Print details for only one item
            else:
                print(f"Failed to fetch details for Work Item ID {work_item_id}. Error: {detail_response.status_code}")
    else:
        print(f"Error: {response.status_code} - {response.text}")            
    """    
        
        # Access 'Cassandra.FileIndicatorSummary' if it exists
        # if 'fields' in data and 'Cassandra.FileIndicatorSummary' in data['fields'] or 'Cassandra.NetworkIndicatorSummary' in data['fields']:
            # print(f"Detection for {work_id}:\n{triage}\n")
            # not_skipped.append(work_id)

        # else:

        # triage = get_cassie_triage(work_id)
        # if not triage:
            # print(f"Skip for {work_id}\n\n")
            # skipped.append(work_id)
        # else:
            # print(f"Detection for {work_id}:\n{triage}\n")
            # not_skipped.append(work_id)

    # print(f"Not skipped ids: {not_skipped}")



"""    
    authorization = str(base64.b64encode(bytes(':' + pat, 'ascii')), 'ascii')

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Basic ' + authorization
    }
    project_url = f'https://dev.azure.com/threat-intel/Cassandra/_apis/wit/workitems/{work_item_id}?api-version=7.1'

    # Make the request
    response = requests.get(url=project_url, headers=headers)

    # Parse the JSON response
    data = response.json()
    print(data['fields'].keys())
    network_indicator_summary = data['fields']['Cassandra.NetworkIndicatorSummary']
    print(network_indicator_summary)
    soup = BeautifulSoup(network_indicator_summary, 'html.parser')
    tables = soup.find_all('table')
    for table in tables:
        context = []
        prev_element = table.find_previous_sibling()
        while prev_element and prev_element.name in ['p', 'h3', 'h2', 'h1']:
            context.append(prev_element.text.strip())
            prev_element = prev_element.find_previous_sibling()

        # Reverse context list to get correct order
        context.reverse()
        context_text = "\n".join(context)

        # Extract headers and rows
        headers = [th.text.strip() for th in table.find_all('th')]  # Extract headers
        rows = [
            [td.text.strip() for td in row.find_all(['td', 'th'])]
            for row in table.find_all('tr')
        ]

        # Format table as Markdown
        if headers:
            markdown_table = "| " + " | ".join(headers) + " |\n"
            markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
            for row in rows[1:]:  # Skip the header row
                markdown_table += "| " + " | ".join(row) + " |\n"
        else:
            markdown_table = "No headers detected in the table.\n"
        markdown_section = f"{context_text}\n\n{markdown_table}"

    print(markdown_section)
"""