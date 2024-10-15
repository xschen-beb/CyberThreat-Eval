Source: [https://blog.talosintelligence.com/new-phishing-as-a-service-tool-greatness-already-seen-in-the-wild/](https://blog.talosintelligence.com/new-phishing-as-a-service-tool-greatness-already-seen-in-the-wild/)

# New Phishing-As-A-Service Tool “Greatness” Already Seen In The Wild

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Greatness Phishing-as-a-Service (PaaS) Campaign 

 Root Cause: Exploitation of human vulnerability through phishing emails. The phishing kit and API allow attackers to perform man-in-the-middle attacks, intercepting authentication credentials, and bypassing MFA. 

 Threat Actor/group/campaign: Unknown affiliates using the Greatness PaaS. 

 Organization/industry/location: Targeted sectors include manufacturing, health care, technology, and real estate. Geographic focus includes the U.S., U.K., Australia, South Africa, and Canada. Greatness mainly targets businesses using Microsoft 365, especially in the U.S. and U.K. *The changes* (https://medium.com/hunter-strategy/cti-notification-greatness-phishing-kit-9ccecf0e0667) 

 Start date – End date: Mid-2022 to present, with activity spikes in December 2022 and March 2023. 

 MITRE TTPs: ['T1566.002: Phishing: Spearphishing Link', 'T1071.001: Application Layer Protocol: Web Protocols', 'T1078: Valid Accounts', 'T1110.001: Brute Force: Password Guessing', 'T1556.001: Modify Authentication Process: Multi-factor Authentication Interception'] 

 Impact: Compromise of Microsoft 365 accounts, theft of authentication credentials, and session cookies. The exact financial losses or number of affected individuals are not specified. 

 Mitigation: ['Educate employees about phishing attacks and how to recognize suspicious emails.', 'Implement and enforce robust email filtering to detect and block phishing emails.', 'Enable MFA for all accounts, preferably using methods less susceptible to man-in-the-middle attacks, such as hardware tokens.', 'Regularly review and update incident response plans to address phishing attacks.', 'Monitor for unusual login activities and enforce strict access controls.', 'Use anti-phishing tools and services to detect and block phishing attempts in real-time.'] 

 Detection Signature: {'Service': 'Web server hosting phishing kit', 'Port': '443 (commonly used for HTTPS)', 'Severity': 'Critical', 'Incident': 'Greatness PaaS phishing campaign', 'Signature name': 'Phishing Kit Deployment Detected', 'Internal checks': {'Setting1': 'Monitor for unexpected deployments of web server instances.', 'Setting2': 'Check for abnormal configurations or unauthorized API keys usage.', 'Setting3': 'Monitor for unusual traffic patterns to web server instances.'}, 'External scanning': {'Port': '443 open with unusual or suspicious activity.', 'Presence': 'Phishing pages mimicking Microsoft 365 login pages.'}} 

 IoCs: No specific IoCs found in the document. For additional IoCs, refer to the provided GitHub repository: [GitHub IoCs](https://github.com/Cisco-Talos/IOCs/tree/main/2023/04). *The changes* (https://www.vadesecure.com/en/blog/greatness-phishing-as-a-service) 

 Additional Analysis: *The analysis from JOESandbox Cloud* reveals that Greatness phishing kits *customize malicious Microsoft 365 authentication pages* to include the target’s brand, as seen in phishing pages for an analytical and scientific laboratories company. The Vade Threat Intelligence and Response Center (TIRC) and *Talos’s GitHub repository IoCs/2023/04* have provided crucial indicators of compromise. Further, the campaign is linked to *United Bangladeshi Hackers (UBH TEAM)*, which has been active with webshells and phishing campaigns. *Greatness incorporates advanced features like IP filtering, Telegram bots integration, pre-filling victim’s email, and displaying the target's company logo* (https://www.infosecurity-magazine.com/news/greatness-phishing-exploits/). The campaign also employs *Business Email Compromise (BEC)* tactics and sends phishing emails with an *HTML attachment* that, when opened, leads to a fake Microsoft 365 login page *configured via a user-facing control panel* within the phishing kit. *Cisco Talos researchers identified three components* of Greatness: the phishing kit, an API, and a Telegram bot or email address *The changes* (https://medium.com/hunter-strategy/cti-notification-greatness-phishing-kit-9ccecf0e0667). 


# Related articles (describing the same threat) 
['https://blog.talosintelligence.com/new-phishing-as-a-service-tool-greatness-already-seen-in-the-wild/', 'https://www.vadesecure.com/en/blog/greatness-phishing-as-a-service', 'https://www.infosecurity-magazine.com/news/greatness-phishing-exploits/', 'https://medium.com/hunter-strategy/cti-notification-greatness-phishing-kit-9ccecf0e0667']
