from crawl_oneti import get_profiles, get_articles
from mdti_description.crawl_oneti import get_access_token
import mistune
from markdown_it import MarkdownIt
import markdown
from bs4 import BeautifulSoup
import re


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
                    detections += "\n" + detect_text + "\n\n"
                    break

        else:
            continue
    
    if detections.strip():
        return names, links, detections
    else:
        return names, links, "No detections found."

def extract_section_with_mistune(markdown_text, target_title):
    md = MarkdownIt()
    tokens = md.parse(markdown_text)

    found = False
    result = []

    for token in tokens:
        # Check if the current token is a heading
        if token.type == "heading_open" and token.tag == "h1":
            next_token = tokens[tokens.index(token) + 1]
            if next_token.type == "inline" and next_token.content.strip() == target_title:
                found = True
                continue

        # Stop capturing at the next heading
        if found and token.type == "heading_open":
            break

        # Capture paragraph or other content
        if found and token.type in {"paragraph", "fence"}:
            result.append(token.content)

    return "\n".join(result).strip()


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
    # return ''.join(str(elem) for elem in result) if result else None


# Example Usage
if __name__ == '__main__':
    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)
    actors = ['Forest Blizzard']
    detections = mdti_detection_pipeline(actors, token)
    print("\nFinal Detections:\n", detections)
    md_Test = """
## Snapshot
The Cybereason Global Security Operations Center (GSOC) has analyzed StealBit, a data exfiltration tool developed by the LockBit ransomware group

## Description
StealBit is provided to affiliates as part of LockBit's ransomware-as-a-service program and is used to exfiltrate data from compromised systems to facilitate double extortion attacks. The tool has evolved over time, incorporating new features aimed at enhancing evasion and efficiency. Notably, while older versions avoided execution on systems in certain countries, including Russia, Ukraine, Belarus, Tajikistan, Armenia, Azerbaijan, Georgia, Kazakhstan, Kyrgyzstan, Turkmenistan, Uzbekistan, and Moldova, newer versions have removed this restriction, broadening their target base.

StealBit employs the I/O completion port threading model to optimize data exfiltration efficiency, allowing for parallel processing of multiple files and reducing the overall time required for exfiltration. It also supports interprocess communication between multiple StealBit processes on a single system, enabling scalable designation of files for exfiltration. Additionally, StealBit offers a drag-and-drop feature for operators with graphical user interface access, enhancing usability. However, some features, such as data compression and hidden operation modes, are not fully implemented, potentially exposing the malware's presence on compromised systems.

## Microsoft Analysis and Additional OSINT Context
StealBit is a data exfiltration tool associated with the LockBit ransomware group, particularly noted for its use in LockBit 2.0 operations.     
It facilitates the rapid transfer of stolen data to attacker-controlled endpoints, supporting the group's double extortion tactics. StealBit is sometimes employed alongside other tools like Rclone or WinSCP to exfiltrate data before encryption.

## Recommendations
Apply these mitigations to reduce the impact of this threat. Check the recommendations card for the deployment status of monitored mitigations.  

- Turn on [cloud-delivered protection](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/configure-block-at-first-sight-microsoft-defender-antivirus) in Microsoft Defender Antivirus or the equivalent for your antivirus product to cover rapidly evolving attacker tools and techniques.
- Turn on [tamper protection](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/prevent-changes-to-security-settings-with-tamper-protection) features to prevent attackers from stopping security services.
- Run [endpoint detection and response (EDR) in block mode](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/edr-in-block-mode) so that Microsoft Defender for Endpoint can block malicious artifacts, even when your non-Microsoft antivirus doesn’t detect the threat or when Microsoft Defender Antivirus is running in passive mode. EDR in block mode works behind the scenes to remediate malicious artifacts that are detected post-breach.
- Enable [investigation and remediation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/automated-investigations) in full automated mode to allow Microsoft Defender for Endpoint to take immediate action on alerts to resolve breaches, significantly reducing alert volume.
- Use [device discovery](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/device-discovery) to increase your visibility into your network by finding unmanaged devices on your network and onboarding them to Microsoft Defender for Endpoint.
- Invest in advanced anti-phishing solutions that monitor incoming emails and visited websites. [Microsoft Defender for Office 365](https://learn.microsoft.com/microsoft-365/security/defender/microsoft-365-security-center-mdo?ocid=magicti_ta_learndoc) brings together incident and alert management across email, devices, and identities, centralizing investigations for threats in email. Organizations can also leverage web browsers that automatically [identify and block malicious websites](https://learn.microsoft.com/deployedge/microsoft-edge-security-smartscreen?ocid=magicti_ta_learndoc), including those used in this phishing campaign. To build resilience against phishing attacks in general, organizations can use [anti-phishing policies](https://docs.microsoft.com/microsoft-365/security/office-365-security/set-up-anti-phishing-policies?view=o365-worldwide) to enable mailbox intelligence settings, as well as configure impersonation protection settings for specific messages and sender domains. Enabling [SafeLinks](https://docs.microsoft.com/microsoft-365/security/office-365-security/safe-links?view=o365-worldwide) ensures real-time protection by scanning at time of delivery and at time of click.
- Additionally, block phishing websites and other malicious URLs and domains in the browser through [Microsoft Defender SmartScreen](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/), as well as the detection of suspicious and malicious behavior on endpoints.

## Detections/Hunting Queries

### Microsoft Defender Antivirus
- [Ransom:Win32/Stealbit.PA!MTB](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Ransom:Win32/Stealbit.PA!MTB)
- [Trojan:Win32/StealBit.MP!MTB](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:Win32/StealBit.MP!MTB)

## References
[THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool) Cybereason (Accessed 2024-12-27)

## Copyright
**© Microsoft 2024**. All rights reserved. Reproduction or distribution of the content of this site, or any part thereof, without written permission of Microsoft is prohibited.

    """

    # md = extract_markdown_section(md_Test, "Detections/Hunting Queries")
    # print(md)