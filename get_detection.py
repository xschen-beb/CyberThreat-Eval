from crawl_oneti import get_profiles
import markdown
from bs4 import BeautifulSoup
from mdti_description.crawl_oneti import get_access_token

import re
import json
import os
import requests
import base64

def extract_markdown_section(md_text, section_header):
    def remove_code_fences(md_text):
        cleaned = re.sub(r'```+.*?\n', '', md_text)
        cleaned = re.sub(r'```+', '', cleaned)
        return cleaned
    
    md_text = remove_code_fences(md_text)

    html = markdown.markdown(md_text, extensions=[])
    print(html)
    soup = BeautifulSoup(html, 'html.parser')

    all_headings = soup.find_all(['h2', 'h3', 'h4'])
    result = None

    def heading_level(h_tag):
        return int(h_tag.name[1])

    for tag in all_headings:
        current_title = tag.get_text(strip=True)

        if current_title == section_header:
            current_level = heading_level(tag)
            contents = []

            for sibling in tag.next_siblings:
                if sibling.name in ['h2','h3','h4']:
                    if heading_level(sibling) <= current_level:
                        break
                contents.append(str(sibling))

            result = ''.join(contents).strip()
            break

    soup = BeautifulSoup(result, 'html.parser')
    result = soup.get_text(separator='\n', strip=True)
    return result

def mdti_detection_pipeline(actors, token):
    detections = ""
    # We define the headers we’re looking for. 
    # You can expand this if you have alternate header text (##, ###, etc.).

    links = []
    names = []

    for actor in actors:
        # Example of how you'd fetch profiles/articles from your existing logic
        profiles = get_profiles(token.token, actor)
        
        if profiles and profiles["data"]["totalPages"] > 0:
            names.append(actor)
            print("="*20 + " Using oneti profile " + "="*20 + '\n')
            for i in range(min(profiles['data']['totalPages'], 1)):
                text = profiles["data"]["content"][i]['description']
                print(text)
                name = profiles['data']['content'][0]['name']
                link = f"https://sip.security.microsoft.com/intel-profiles/{name}"
                links.append(link)

                # detect_text = find_detection_section(text)
                detect_text = extract_markdown_section(text, "Detections/Hunting Queries")
                # Optionally add an intro or do any other formatting
                if detect_text:
                    # Add to detections with some spacing, etc.
                    detections += f"- [Detections of {actor}]({link}):\n" + detect_text + "\n\n"
                    break

        else:
            continue
    
    if detections.strip():
        return names, links, detections
    else:
        return names, links, "No detections found."
    
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
        if 'fields' in data and 'Cassandra.FileIndicatorSummary' in data['fields']:
            file_indicator_summary = data['fields']['Cassandra.FileIndicatorSummary']

            # Parse HTML content with BeautifulSoup
            soup = BeautifulSoup(file_indicator_summary, 'html.parser')
            tables = soup.find_all('table')  # Find all <table> tags

            if not tables:
                print("No <table> elements found in the summary.")
                return

            markdown_output = "### "

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
                    markdown_table = "No headers detected in the table.\n"

                # Combine context and table
                markdown_section = f"{context_text}\n\n{markdown_table}"
                markdown_output += markdown_section + "\n\n"

            # Save the Markdown output to a file
            # with open(output_file, 'w', encoding='utf-8') as fo:
                # fo.write(markdown_output)
            # print(f"Markdown content saved to {output_file}")
            return markdown_output

        else:
            return ""
            print("'Cassandra.FileIndicatorSummary' not found in fields.")

    except json.JSONDecodeError:
        print("Failed to parse JSON. Response text:")
        print(response.text)

# Example Usage
if __name__ == '__main__':
    # work_item_id = '18426220'  # Replace with your work item ID
    # output_file = 'full_md.md'  # Output Markdown file path
    # triage = get_cassie_triage(work_item_id)
    # print(triage)
    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)
    actors = ['Forest Blizzard']

    actors = ['Amethyst Rain']
    det = mdti_detection_pipeline(actors, token)
    print(det)