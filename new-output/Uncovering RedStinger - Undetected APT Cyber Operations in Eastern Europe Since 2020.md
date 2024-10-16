Source: [https://www.malwarebytes.com/blog/threat-intelligence/2023/05/redstinger](https://www.malwarebytes.com/blog/threat-intelligence/2023/05/redstinger)

# Uncovering RedStinger - Undetected APT Cyber Operations in Eastern Europe Since 2020

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: RedStinger APT Cyber Operations in Eastern Europe 

 Root cause: Operations attributed to multiple vectors, including spear-phishing with malicious attachments (MSI files), and the use of legitimate tools (like ngrok) for malicious purposes. Vulnerabilities in endpoint security, particularly around email and file handling, enabled the initial foothold and subsequent attack stages. 

 Threat Actor/group/campaign: RedStinger APT (also referred to as Bad Magic by Kaspersky), tracked by Malwarebytes’ Roberto Santos and Fortinet’s Hossein Jazi *The changes* (https://www.threatdown.com/blog/uncovering-redstinger-undetected-apt-cyber-operations-in-eastern-europe-since-2020/). *Additionally, CloudWizard APT is linked with RedStinger* (https://malpedia.caad.fkie.fraunhofer.de/details/ps1.power_magic). *Malwarebytes researchers identified Red Stinger* (https://www.wired.com/story/red-stinger-russia-ukraine-apt/). 

 Organization/industry/location: Targets were primarily in Eastern Ukraine, including military, transportation, critical infrastructure entities, and individuals involved in the September East Ukraine referendums. Administrative organizations in Donetsk, Lugansk, and Crimea regions were also attacked with PowerMagic backdoor and CommonMagic framework. *Military personnel, Yasinovataya Administration, and an advisor from the Ukrainian Central Election Commission were also targeted* (https://cyware.com/news/red-stinger-apt-group-targeting-ukrainian-military-transport-orgs-since-2020-53a7412c). 

 Start date – End date: Attacks spanned from late 2020 to at least September 2022. 

 MITRE TTPs: ['T1193: Spearphishing Attachment', 'T1059: Command and Scripting Interpreter', 'T1056: Input Capture', 'T1071: Application Layer Protocol', 'T1105: Ingress Tool Transfer', 'T1113: Screen Capture', 'T1123: Audio Capture'] 

 Impact: Various critical data types were exfiltrated, including screenshots, USB drive contents, keystrokes, and microphone recordings. The specific number of records or financial losses was not disclosed, but the impact is significant given the nature of the targets. 

 Mitigation: {'1. Enhance Email Security': 'Implement advanced email filtering to detect and block malicious attachments and links.', '2. Endpoint Protection': 'Utilize endpoint detection and response (EDR) tools to identify and mitigate malicious activity.', '3. User Awareness Training': 'Conduct regular training to help users recognize and avoid phishing attempts.', '4. Network Segmentation': 'Segment networks to limit lateral movement and isolate critical infrastructure.', '5. Regular Patching': 'Ensure all systems and software are up-to-date with the latest security patches.', '6. Audit and Monitoring': 'Regularly audit and monitor network traffic and user activity for signs of compromise.'} 

 Detection Signature: {'Service': 'Email Security Gateway, EDR (Endpoint Detection and Response), Managed Detection & Response (MDR) *The changes* (https://www.threatdown.com/blog/uncovering-redstinger-undetected-apt-cyber-operations-in-eastern-europe-since-2020/)', 'Port': 'Not applicable (Email services and endpoint network activities)', 'Severity': 'Critical', 'Incident': 'RedStinger APT Campaign', 'Signature name': 'RedStinger spear-phishing detection', 'Internal checks': {'Setting1': 'Email filtering rules to detect and block suspicious attachments (e.g., MSI files).', 'Setting2': 'EDR rules to identify and respond to unusual script execution and network activity.', 'Setting3': 'Endpoint logging and monitoring for unauthorized access and data exfiltration attempts.'}, 'External scanning': {'Phishing simulation tests': 'Assess user awareness and response.', 'Network traffic analysis': 'Identify malicious communication patterns.'}} 

 IoCs: {'Hosts': ['91.234.33.185', '91.234.33.108', '185.230.90.163', '176.114.9.192', '45.154.116.147', '185.166.217.184'], 'Files and Hashes': ['MSI: C68ce59f73c3d5546d500a296922d955ccc57c82b16ce4bd245ca93de3e32366', 'DLL: 9e73dacedf847410dd4a0caa6aac83d31f848768336514335d4872d0fde28202', 'ZIP: 301e819008e19b9803ad8b75ecede9ecfa5b11a3ecd8df0316914588b95371c8', 'PowerShell: 78634be886ccb3949c8e5b8f0893cff32c474a466e4d4ceba35ba05c3d373bff'], 'Additional IoCs': 'Listed in the blog post and should be utilized for comprehensive detection and threat hunting.'} 

 Contributors: ['Kaspersky Labs', 'Georgy Kucherin', 'Igor Kuznetsov', 'Leonid Bezvershenko'] 

 *New Entities*: {'Additional Malware': 'DBoxShell, SolarTools (https://cyware.com/news/red-stinger-apt-group-targeting-ukrainian-military-transport-orgs-since-2020-53a7412c).', 'Operations': '*Operation Four and Operation Five targeted critical infrastructure and election officials in Ukraine* (https://www.wired.com/story/red-stinger-russia-ukraine-apt/).'} 


# Related articles (describing the same threat) 
['https://www.malwarebytes.com/blog/threat-intelligence/2023/05/redstinger', 'https://www.threatdown.com/blog/uncovering-redstinger-undetected-apt-cyber-operations-in-eastern-europe-since-2020/', 'https://securelist.com/bad-magic-apt/109087/', 'https://malpedia.caad.fkie.fraunhofer.de/details/ps1.power_magic', 'https://cyware.com/news/red-stinger-apt-group-targeting-ukrainian-military-transport-orgs-since-2020-53a7412c', 'https://www.wired.com/story/red-stinger-russia-ukraine-apt/']
