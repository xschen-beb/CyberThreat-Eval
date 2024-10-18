Source: [https://cofense.com/blog/open-source-gh0st-rat-still-haunting-inboxes-15-years-after-release/](https://cofense.com/blog/open-source-gh0st-rat-still-haunting-inboxes-15-years-after-release/)

# Open-Source Gh0st RAT Still Haunting Inboxes 15 Years After Release

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Gh0st RAT in Phishing Campaign 

 Root Cause: Phishing email with embedded link to download Gh0st RAT affiliated with Tencent, based in Hong Kong. 

 Threat Actor/group/campaign: Potentially APT27; EMISSARY PANDA; Hurricane Panda; Lazarus Group (uncertain, as the source code is publicly available and could be used by various actors) *The changes* (https://malpedia.caad.fkie.fraunhofer.de/details/win.ghost_rat) 

 Organization/industry/location: European-owned medical technology organization in China. 

 Start date – End date: Ongoing, as Gh0st RAT is still actively distributed. 

 MITRE TTPs: ['T1071.001: Application Layer Protocol – Web Protocols', 'T1078: Valid Accounts', 'T1059: Command and Scripting Interpreter', 'T1074.001: Data Staged – Local Data Staging'] 

 Impact: Potential impact includes unauthorized access to sensitive data, keystroke logging, live webcam access, file downloads, remote shutdowns, and more. 

 Mitigation: [{'Email Filtering and Analysis': ['Use advanced email filtering solutions to detect and block phishing emails.', 'Implement sandboxing to analyze email attachments and links in a secure environment before delivering them to end-users.']}, {'User Awareness and Training': ['Provide regular training to employees on recognizing phishing attempts.', 'Encourage users to report suspicious emails to the IT department.']}, {'Endpoint Protection': ['Install and maintain updated antivirus and anti-malware solutions.', 'Enable endpoint detection and response (EDR) solutions to monitor and respond to suspicious activities.']}, {'Network Security': ['Monitor network traffic for unusual patterns that may indicate data exfiltration or command and control (C2) communications.', 'Restrict access to known malicious IP addresses and domains.']}, {'Patch Management': ['Regularly update all software and systems to patch known vulnerabilities that could be exploited.']}] 

 Detection Signature: {'Service': 'Email Security Gateway', 'Port': 'N/A', 'Severity': 'High', 'Incident': 'Gh0st RAT Phishing Campaign', 'Signature name': '“Gh0st RAT phishing email detection”', 'Internal checks': ['Check for the presence of emails with embedded links leading to known malicious domains or IPs.', 'Analyze email metadata for suspicious sender addresses or spoofing attempts.', 'Monitor for emails containing attachments or links with known IoC hashes.'], 'External scanning': ['Monitor for attempts to access known malicious URLs and C2 IPs.', 'Use threat intelligence feeds to update detection rules with the latest IoCs.']} 

 IoCs: {'Files': [{'File': '1680478346389.zip', 'MD5': '9e6c45b6b8b20bf3c5959dbba8f27117'}, {'File': 'LiveUpdate360.dat', 'MD5': 'f149d3f3ef0361ebe4d346811f29b527'}, {'File': 'LiveUpdate.exe', 'MD5': '96e4b47a136910d6f588b40d872e7f9d'}, {'File': 'setting.ini', 'MD5': '91aab4bbe634be62d11d132738c23a82'}, {'File': 'SqlVersion9.dll', 'MD5': '317f9ff06c076e87e5b1d11242396d5f'}, {'File': 'ú¿╡τ-╫╙-╖ó-╞▒ú⌐.exe', 'MD5': '4723a2a8f68c1eaf82809cff29b8e56f'}], 'URLs': ['hxxps://api[.]youkesdt[.]asia/admin/down/hash/79b7c6ed-c4d8-4b36-b1cd-f968e6570010', 'hxxp://datacache[.]cloudservicesdevc[.]tk/picturess/2023/SqlVersion9[.]dll', 'hxxp://datacache[.]cloudservicesdevc[.]tk/picturess/2023/Media[.]xml', 'hxxp://datacache[.]cloudservicesdevc[.]tk/picturess/2023/LiveUpdate360[.]dat', 'hxxp://datacache[.]cloudservicesdevc[.]tk/picturess/2023/LiveUpdate[.]exe', 'hxxp://datacache[.]cloudservicesdevc[.]tk/picturess/2023/223[.]114[.]txt'], 'Command and Control': ['hxxp://61[.]160[.]223[.]114:18076']} 


# Related articles (describing the same threat) 
['https://cofense.com/blog/open-source-gh0st-rat-still-haunting-inboxes-15-years-after-release/', 'https://malpedia.caad.fkie.fraunhofer.de/details/win.ghost_rat']
