from mdti_description.crawl_oneti import get_profiles
import markdown
from bs4 import BeautifulSoup

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
    print(f" ==> markdown text:\n\n {html}")
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
    
    print(f" ==> Result: {result}\n\n")
    if result:
        soup = BeautifulSoup(result, 'html.parser')
        result = soup.get_text(separator='\n', strip=True)
        return result
    else:
        return None

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
                    print(f"- [Detections of {actor}]({link}):\n" + detect_text + "\n\n")
                    print(f" ==> Detections: {detect_text}\n")
                    break

        else:
            continue
    
    print(f"==> Detections: \n {detections} \n")
    print(f"==> Actor names: \n {names} \n")
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
    context = """
## Snapshot

The Caffeine phishing as a service (PhaaS) platform provides ready-to-use phishing emails, website templates, how-to documentation, phishing infrastructure (domains and IP addresses), Adversary-in-the-Middle (AiTM) phishing capabilities, and user support systems to its customers, lowering the barrier to entry for less skilled phishing actors. Its registration process is uniquely open, allowing anyone with an email address and the funds to pay the subscription price to sign up for the service. Like most phishing services, there are multiple actors making use of the Caffeine platform with varying motivations and targeting. 



Microsoft Defender for Endpoint detects network connections to domains affiliated with the actor behind the Caffeine PhaaS platform and notifies affected customers with the alert Emerging threat activity group DEV-0867 detected. Refer to the Detection details section for more information.



## Description

In a typical Caffeine phishing attack, a user might receive an email prompting them to click a link to view documents. Initial phishing URLs Microsoft has observed follow this pattern:



- `hXXps[:]//[random alphanumeric string].[domain].[tld]/M[Base64-encoded user email address]`



If the targeted user follows the prompt by clicking the link, they are redirected to the phishing page at a URL matching this pattern:



- `hXXps[:]//[random alphanumeric string].[domain].[tld]/[two capital letters]-[alphanumeric string]`



Actors using the Caffeine platform can also customize phishing pages using application programming interface (API) calls to pull logos and backgrounds from legitimate, commonly used webpages. An example of this using the fictional company Contoso\[.\]com is below:



- `hXXps[:]//[random alphanumeric string].[domain].[tld]/api-[alphanumeric string]?email=user[.]name@contoso[.]com&data=logo`

- `hXXps[:]//[random alphanumeric string].[domain].[tld]/api-[alphanumeric string]?email=user[.]name@contoso[.]com&data=background`



![Image generate by intercepting and substituting original branding](https://cdn-riq-ti.azureedge.net/83d550d7-384c-4faf-8d59-91bf0d9da718)



*Image generated by intercepting and substituting original branding*



Since the Caffeine platform is in use by multiple different actors, there is variance among initial email lures, redirection sequences, and phishing landing pages. Microsoft observed Caffeine phishing pages on dozens of purposefully created domains since tracking of the service began in August 2022.



### AiTM phishing capability



In March 2023, Microsoft analysts found a service offering titled Office 2FA Cookie Stealer (30 Days, Never Red Screen) in the Caffeine PhaaS store, available for purchase for three-hundred dollars USD. The offer includes the following feature list:



- Auto capture two-factor authentication cookies (phone and Microsoft Authenticator application).

- Link statistics

- Auto grab victim number where the two-factor authentication code was sent

- One time (ON/OFF)

- Block countries (ON/OFF)

- Custom page title (ON/OFF)

- Telegram identification

- Custom redirect link

- Dynamic codes

- Auto grab email (normal, Base64)

- Auto fetch custom logos, backgrounds



![Image of Storm-0867’s Telegram post advertising Caffeine’s AiTM capabilities](https://cdn-riq-ti.azureedge.net/404b2f7d-4652-48f2-9990-803896698177)



*Image of Storm-0867’s Telegram post advertising Caffeine’s AiTM capabilities*



Another offer included the same features along with a private domain for four-hundred dollars USD. These prices are comparable to offers from NakedPages or EvilProxy. An earlier announcement indicates the AiTM capabilities were in a beta state from as early as September 2022.



![Image of Storm-0867’s Telegram post announcing beta tests for AiTM capabilities in Caffeine](https://cdn-riq-ti.azureedge.net/2d91af3a-7d50-46cd-be3a-5aacd45798be)



*Image of Storm-0867’s Telegram post announcing beta tests for AiTM capabilities in Caffeine*



Microsoft analysts confirmed Caffeine's AiTM capabilities on an active phishing page.



![Multifactor authentication phishing page generated by Caffeine](https://cdn-riq-ti.azureedge.net/50999a5b-ea92-4b87-ae98-c77a46c9fdfa)



*Multifactor authentication (MFA) phishing page generated by Caffeine*



## Attribution

Microsoft has identified Storm-0867 (DEV-0867) as the actor behind the Caffeine PhaaS platform and has tracked this actor since early August 2022. Clusters of domain registrations can be tied to this actor, domains that are subsequently used in phishing campaigns carried out by actors using the Caffeine platform.



## Recommendations

Implement multifactor authentication (MFA) to mitigate credential theft from phishing attacks. MFA can be complemented with the following solutions and best practices to protect organizations:



- Activate conditional access policies. [Conditional access](https://learn.microsoft.com/azure/active-directory/conditional-access/overview?ocid=magicti_ta_learndoc) policies are evaluated and enforced every time an attacker attempts to use a stolen session cookie. Organizations can protect themselves from attacks that leverage stolen credentials by activating policies regarding compliant devices or trusted IP address requirements.

- Configure [continuous access evaluation](https://learn.microsoft.com/azure/active-directory/conditional-access/concept-continuous-access-evaluation?ocid=magicti_ta_learndoc) in your tenant.

- Invest in advanced anti-phishing solutions that monitor incoming emails and visited websites. [Microsoft Defender for Office](https://learn.microsoft.com/microsoft-365/security/defender/microsoft-365-security-center-mdo?ocid=magicti_ta_learndoc) 365 brings together incident and alert management across email, devices, and identities, centralizing investigations for threats in email. Organizations can also leverage web browsers that automatically [identify and block malicious websites](https://learn.microsoft.com/deployedge/microsoft-edge-security-smartscreen?ocid=magicti_ta_learndoc), including those used in this phishing campaign.

- Monitor for suspicious or anomalous activities, and search for sign-in attempts with suspicious characteristics (for example location, internet service provider \[ISP\], user agent, and use of anonymizer services). Activity can be identified and investigated with [Microsoft Defender for Identity](https://learn.microsoft.com/microsoft-365/security/defender/microsoft-365-security-center-mdi?ocid=magicti_ta_learndoc), which contributes identity-focused information into incidents and alerts, providing key context and correlating alerts from other products within Microsoft 365 Defender. This ensures all alerts are available in one place, and the scope of a breach can be determined faster than before.



Defenders can also complement MFA with the following solutions and best practices to further protect their organizations from such attacks.  



- Use [security defaults](https://learn.microsoft.com/azure/active-directory/fundamentals/concept-fundamentals-security-defaults?ocid=magicti_ta_learndoc) as a baseline set of policies to improve identity security posture. For more granular control, enable conditional access policies. [Conditional access](https://learn.microsoft.com/azure/active-directory/conditional-access/overview?ocid=magicti_ta_learndoc) policies evaluate sign-in requests using additional identity-driven signals like user or group membership, IP location information, and device status, among others, and are enforced for suspicious sign-ins. Organizations can protect themselves from attacks that leverage stolen credentials by enabling policies such as compliant devices or trusted IP address requirements.

- Implement [continuous access evaluation](https://learn.microsoft.com/azure/active-directory/conditional-access/concept-continuous-access-evaluation?ocid=magicti_ta_learndoc).

- Invest in advanced anti-phishing solutions that monitor and scan incoming emails and visited websites. For example, organizations can leverage web browsers that automatically [identify and block malicious websites](https://learn.microsoft.com/deployedge/microsoft-edge-security-smartscreen?ocid=magicti_ta_learndoc), including those used in this phishing campaign, and solutions that [detect and block malicious emails, links, and files](https://www.microsoft.com/security/business/siem-and-xdr/microsoft-defender-office-365?ocid=magicti_ta_abbreviatedmktgpage).

- Continuously monitor suspicious or anomalous activities. Investigate sign-in attempts with suspicious characteristics (for example, location, ISP, user agent, and use of anonymizer services).



## Detections/Hunting Queries



### Microsoft Defender for Endpoint

Microsoft Defender for Endpoint detects network connections to domains affiliated with Storm-0867 (DEV-0867). Alerts with the following titles in the security center can indicate threat activity on your network: 



- Emerging threat activity group Storm-0867 (DEV-0867) detected



### Microsoft Sentinel

Microsoft Sentinel customers can use the following Microsoft Sentinel Analytics template to identify potential AiTM phishing attempts: 

 

- Possible AiTM Phishing Attempt Against Azure AD



This detection uses signals from Azure AD Identity Protection and looks for successful sign-ins that have been flagged as high risk. It combines this with data from Web Proxy services, such as ZScaler, to identify where users might have connected to the source of those sign-ins immediately prior. This can indicate a user interacting with a AiTM phishing site and having their session hijacked. This detection uses the Advanced Security Information Model (ASIM) Web Session schema. More details on the schema and its requirements can be found in the documentation: https://learn.microsoft.com/azure/sentinel/normalization-schema-web.



Customers can use the following identity-focused Analytics and Hunting Queries to detect and investigate anomalous sign-in events that may be indicative of a compromised user identity being accessed by a threat actor:



- [Anomalous sign-in location by user account and authenticating application](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Azure%20Active%20Directory/Analytic%20Rules/AnomalousUserAppSigninLocationIncrease-detection.yaml)

- [Azure Portal Signin from another Azure Tenant](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Azure%20Active%20Directory/Analytic%20Rules/AnomalousUserAppSigninLocationIncrease-detection.yaml%22%20HYPERLINK%20%22https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Azure%20Active%20Directory/Analytic%20Rules/AzurePortalSigninfromanotherAzureTenant.yaml)

- [User Accounts - Sign in Failure due to CA Spike](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Azure%20Active%20Directory/Analytic%20Rules/AzurePortalSigninfromanotherAzureTenant.yaml%22%20%EF%BF%BDHYPERLINK%20%22https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Azure%20Active%20Directory/Analytic%20Rules/UserAccounts-CABlockedSigninSpikes.yaml)

- [Signins From VPS Providers](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Cloud%20Identity%20Threat%20Protection%20Essentials/Hunting%20Queries/Signins-From-VPS-Providers.yaml)

- [Signins from Nord VPN Providers](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Cloud%20Identity%20Threat%20Protection%20Essentials/Hunting%20Queries/Signins-From-VPS-Providers.yaml%22%20HYPERLINK%20%22https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Cloud%20Identity%20Threat%20Protection%20Essentials/Hunting%20Queries/Signins-from-NordVPN-Providers.yaml)

- [Successful Signin From Non-Compliant Device](https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Cloud%20Identity%20Threat%20Protection%20Essentials/Hunting%20Queries/Signins-from-NordVPN-Providers.yaml%22%20HYPERLINK%20%22https://github.com/Azure/Azure-Sentinel/blob/master/Hunting%20Queries/SigninLogs/SuccessfulSigninFromNon-CompliantDevice.yaml)

- [User Login IP Address Teleportation](https://github.com/Azure/Azure-Sentinel/blob/master/Hunting%20Queries/SigninLogs/SuccessfulSigninFromNon-CompliantDevice.yaml%22%20%EF%BF%BDHYPERLINK%20%22https://github.com/Azure/Azure-Sentinel/blob/master/Hunting%20Queries/SigninLogs/UserLoginIPAddressTeleportation.yaml)

- [Anomalous Azure Active Directory apps based on authentication location](https://github.com/Azure/Azure-Sentinel/blob/master/Hunting%20Queries/SigninLogs/anomalous_app_azuread_signin.yaml)

- [Azure Active Directory signins from new locations](https://github.com/Azure/Azure-Sentinel/blob/master/Hunting%20Queries/SigninLogs/new_locations_azuread_signin.yaml)

- [Azure Active Directory sign-in burst from multiple locations](https://github.com/Azure/Azure-Sentinel/blob/master/Hunting%20Queries/SigninLogs/new_locations_azuread_signin.yaml%22%20%EF%BF%BDHYPERLINK%20%22https://github.com/Azure/Azure-Sentinel/blob/master/Hunting%20Queries/SigninLogs/signinBurstFromMultipleLocations.yaml)



Microsoft Sentinel customers can also use the data provided by [Microsoft Sentinel’s User and Entity Behavior Analytics](https://learn.microsoft.com/en-us/azure/sentinel/ueba-reference) (UEBA) engine to hunt for anomalous sign-in events, such as a user logging in from an internet service provider (ISP) not commonly seen in the tenant, or if the user agent is uncommon amongst the user’s peer group. More details on Microsoft Sentinel’s UEBA feature can be found here.



### Microsoft Defender XDR

Microsoft Defender XDR detects network connections to domains affiliated with Storm-0867 (DEV-0867). Alerts with the following titles in the security center can indicate threat activity on your network: 



- Emerging threat activity group Storm-0867 (DEV-0867) detected



## Change Log

- 2023-07-17 09:32 UTC | Updated threat actor names with new naming scheme

- 2023-05-22 22:30 UTC | Updated with AiTM details

- 2023-03-15 22:47 UTC | Entry created



## Copyright

**© Microsoft 2023**. All rights reserved. Reproduction or distribution of the content of this site, or any part thereof, without written permission of Microsoft is prohibited.

    """
    
    md = extract_markdown_section(context, "Detections/Hunting Queries")
    print(md)
    if md:
        # Add to detections with some spacing, etc.
        detections = f"- [Detections of {md}"
        print(f"Det: {detections}")
    
    # work_item_id = '18426220'  # Replace with your work item ID
    # output_file = 'full_md.md'  # Output Markdown file path
    # triage = get_cassie_triage(work_item_id)
    # print(triage)
    # client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    # scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    # token = get_access_token(client_id, scopes)
    # actors = ['Forest Blizzard']

    # actors = ['Amethyst Rain']
    # det = mdti_detection_pipeline(actors, token)
    # print(det)