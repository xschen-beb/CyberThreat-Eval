Source: [https://www.proofpoint.com/us/blog/threat-insight/bumblebee-buzzes-back-black](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-buzzes-back-black)

# Bumblebee Buzzes Back in Black   Proofpoint US

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Bumblebee Buzzes Back in Black 

 Root cause: The root cause behind the incident involves the use of malicious Word documents with VBA macros. These macros create a script in the Windows temporary directory and execute it using 'wscript'. The script then downloads and executes additional malicious payloads, including the Bumblebee malware, which acts as an initial access broker. *The changes* (https://www.infosecurity-magazine.com/news/bumblebee-malware-new-attack/). 

 Threat Actor/group/campaign: The activity is not attributed to a specific threat actor by Proofpoint at this time. However, the tactics align with previous activities by TA579, and are believed to involve the Conti and TrickBot syndicate. The latest campaign targeted organizations with the subject 'Voicemail February' and spoofed a consumer electronics company called Humane. *The changes* (https://securityboulevard.com/2024/02/bumblebee-malware-targets-us-businesses-with-new-methods/). 

 Organization/industry/location: The campaign targeted organizations in the United States, leveraging AWS Simple Notification Service (SNS) in its tactics. *The changes* (https://www.tanium.com/blog/return-of-bumblebee-and-pikabot-malware-spammers-hit-aws-sns-cyber-threat-intelligence-roundup/). 

 Start date – End date: The attack was observed starting on February 8, 2024, after a four-month hiatus. *The changes* (https://www.tanium.com/blog/return-of-bumblebee-and-pikabot-malware-spammers-hit-aws-sns-cyber-threat-intelligence-roundup/). 

 MITRE TTPs: ['T1566.002: Phishing: Spearphishing Link', 'T1204.002: User Execution: Malicious File', 'T1059.001: Command and Scripting Interpreter: PowerShell', 'T1071.001: Application Layer Protocol: Web Protocols'] 

 Impact: The specific number of impacted records or devices is not provided in the blog, but the campaign involved several thousand emails targeting organizations in the United States. Each email contained OneDrive URLs leading to the malicious Word document. *The changes* (https://www.tanium.com/blog/return-of-bumblebee-and-pikabot-malware-spammers-hit-aws-sns-cyber-threat-intelligence-roundup/). 

 Mitigation: ['Disable macros in Microsoft Office files by default to prevent automatic execution of malicious scripts.', 'Use email security solutions to detect and block phishing emails containing malicious URLs or attachments.', 'Educate users on recognizing phishing emails and avoiding clicking on suspicious links or downloading unsolicited attachments.', 'Implement robust endpoint protection solutions that can detect and block malicious scripts and PowerShell commands.'] 

 Detailed Steps for mitigation: ["Disable VBA Macros by Default: In Office 365 Admin Center, configure the 'Macro Settings' in the 'Trust Center' to disable macros by default and only allow signed macros.", 'Email Security: Deploy advanced email security solutions that use machine learning to detect and block phishing emails. Implement URL filtering to block access to known malicious sites.', 'User Education: Conduct regular security awareness training for employees to recognize phishing attempts. Simulate phishing attacks to test and improve employee vigilance.', 'Endpoint Protection: Deploy endpoint detection and response (EDR) solutions that can monitor and block suspicious activities like script execution and unauthorized PowerShell commands. Ensure antivirus software is up-to-date and capable of detecting the latest malware signatures.'] 

 Detection Signature: {'Service': 'Microsoft Office', 'Port': 'N/A (Email/Document-based attack)', 'Severity': 'Critical', 'Incident': 'Bumblebee malware campaign', 'Signature name': 'Malicious VBA Macro Execution', 'Internal checks': ['Setting1: Macros should be disabled by default in all Microsoft Office applications. – In platform', 'Setting2: Enable logging for macro execution and monitor for suspicious activities. – Inside VMs', 'Setting3: Use endpoint protection to detect and block malicious script execution. – Inside VMs'], 'External scanning': ['Scan email traffic for known malicious URLs and attachments.', 'Monitor network traffic for connections to known malicious domains and IP addresses.']} 

 IoCs: ['hxxps[:]//1drv[.]ms/w/s!At-ya4h-odvFe-M3JKvLzB19GQA?e=djPGy', 'hxxps[:]//1drv[.]ms/w/s!AuSuRB5deTxugQ-83_HzIqbBWuE1?e=9f2plW', 'SHA256: 0cef17ba672793d8e32216240706cf46e3a2894d0e558906a1782405a8f4decf', 'SHA256: 86a7da7c7ed5b915080ad5eaa0fdb810f7e91aa3e86034cbab13c59d3c581c0e', 'SHA256: 2bc95ede5c16f9be01d91e0d7b0231d3c75384c37bfd970d57caca1e2bbe730f', 'hxxp[:]//213[.]139.205.131/update_ver', 'hxxp[:]//213[.]139.205.131/w_ver.dat', 'SHA256: c34e5d36bd3a9a6fca92e900ab015aa50bb20d2cd6c0b6e03d070efe09ee689a', 'q905hr35[.]life', '49.13.76[.]144:443', '*The changes* (https://www.tanium.com/blog/return-of-bumblebee-and-pikabot-malware-spammers-hit-aws-sns-cyber-threat-intelligence-roundup/)'] 


# Related articles (describing the same threat) 
['https://www.proofpoint.com/us/blog/threat-insight/bumblebee-buzzes-back-black', 'https://www.infosecurity-magazine.com/news/bumblebee-malware-new-attack/', 'https://securityboulevard.com/2024/02/bumblebee-malware-targets-us-businesses-with-new-methods/', 'https://www.tanium.com/blog/return-of-bumblebee-and-pikabot-malware-spammers-hit-aws-sns-cyber-threat-intelligence-roundup/']
