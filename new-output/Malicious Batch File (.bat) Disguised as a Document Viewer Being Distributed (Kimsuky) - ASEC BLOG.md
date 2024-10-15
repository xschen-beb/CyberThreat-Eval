Source: [https://asec.ahnlab.com/en/55219/](https://asec.ahnlab.com/en/55219/)

# Malicious Batch File (.bat) Disguised as a Document Viewer Being Distributed (Kimsuky) - ASEC BLOG

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Malicious Batch File (*.bat) Disguised as a Document Viewer Being Distributed (Kimsuky) 

 Root cause: The incident was caused by a phishing campaign distributing malicious batch files disguised as document viewers like docview.bat, pdfview.bat, and hwp.bat. The batch files were designed to download various scripts based on the anti-malware process installed in the user's environment using the *WMIC command* (https://asec.ahnlab.com/jp/55207/). The campaign also involved *APT37* (https://asec.ahnlab.com/wp-content/uploads/2023/09/ATIP_2023_Jul_Threat-Trend-Report-on-Kimsuky-Group.pdf) and utilized *LNK file tactics* (https://asec.ahnlab.com/wp-content/uploads/2023/09/ATIP_2023_Jul_Threat-Trend-Report-on-Kimsuky-Group.pdf). 

 Threat Actor/group/campaign: Kimsuky 

 Organization/industry/location: Not specified, but targets included individuals handling *military, unification documents* (https://asec.ahnlab.com/jp/55207/). 

 Start date – End date: Identified between Mar. 22, 2023, and Jun. 21, 2023 

 MITRE TTPs: ['T1204.002: User Execution - Malicious File', 'T1105: Ingress Tool Transfer', 'T1566.001: Phishing - Spearphishing Attachment', 'T1082: System Information Discovery', 'T1129: Execution through API'] 

 Impact: The exact number of records or financial losses is not specified, but the impact includes potential unauthorized access to sensitive military and unification-related documents. 

 Mitigation: ['Implement email filtering to block phishing emails and malicious attachments.', 'Regularly update anti-malware software to detect and block malicious scripts.', 'Educate users on recognizing and avoiding phishing attempts.', 'Use multi-factor authentication to reduce the risk of unauthorized access.', 'Monitor network traffic for access to suspicious URLs and block them.', 'Regularly audit and update security policies to include the latest threat intelligence.'] 

 Detection Signature: {'Service': 'Not applicable to a specific service (Phishing and Malware detection)', 'Port': 'Not applicable', 'Severity': 'Critical', 'Incident': 'Distribution of malicious batch files disguised as document viewers', 'Signature name': 'Malicious Batch File Distribution', 'Internal checks': ['Monitor for execution of batch files from email attachments.', 'Check for unusual network connections to external URLs, especially Google Drive and suspicious domains.', 'Inspect for modifications to startup scripts and registry entries related to persistence.'], 'External scanning': ['Monitor and block access to known malicious URLs (e.g., joongang.site, namsouth.com, staradvertiser.store)', 'Detect suspicious downloads from Google Drive and Docs. *C2 servers* (https://asec.ahnlab.com/wp-content/uploads/2023/09/ATIP_2023_Jul_Threat-Trend-Report-on-Kimsuky-Group.pdf).']} 

 IoCs: {'MD5': ['00119ed01689e76cb7f33646693ecd6a', '7d79901b01075e29d8505e72d225ff52', '8536d838dcdd026c57187ec2c3aec0f6', 'a7ac7d100184078c2aa5645552794c19'], 'URLs': ['hxxp://joongang[.]site/doc/', 'hxxp://joongang[.]site/docx/', 'hxxp://joongang[.]site/pprb/sec/', 'hxxp://namsouth[.]com/gopprb/OpOpO/', 'hxxp://staradvertiser[.]store/signal/', 'hxxps://drive.google.com/file/d/1e41uC2ZTYvTc3CvS6wIKox22AGdP4nFB/view?usp=sharing', 'hxxps://drive.google.com/file/d/1tI4J95-7HDGES8e6oHR-wu0cXD8wHPUc/view?usp=sharing', 'hxxps://docs.google.com/document/d/1NJfvSpdku2PW3gwg0dnoELrlVp3CEGB4mtNIFE4bOVE/edit?usp=sharing', 'hxxps://docs.google.com/document/d/1C3h0agp3E6Z4a9z-YxnMTgP3Fd9y8n2C/edit?rtpof=true&sd=true', 'hxxps://drive.google.com/file/d/1rCws6IDhJvynpM3TOSv3IKGWNKXI5uH9/view?usp=sharing']} 


# Related articles (describing the same threat) 
['https://asec.ahnlab.com/en/55219/', 'https://asec.ahnlab.com/ko/54952/', 'https://asec.ahnlab.com/jp/55207/', 'https://asec.ahnlab.com/wp-content/uploads/2023/09/ATIP_2023_Jul_Threat-Trend-Report-on-Kimsuky-Group.pdf']
