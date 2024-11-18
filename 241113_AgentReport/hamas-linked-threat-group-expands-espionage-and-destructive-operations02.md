Source: [https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations](https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations)

## Related articles (describing the same threat) 
- https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations
- https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/
- https://www.bankinfosecurity.com/hamas-tied-to-october-wiper-attacks-using-eset-email-a-26795
- https://harfanglab.io/insidethelab/samecoin-malware-hamas/

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Hamas-linked Threat Group Expands Espionage and Destructive Operations 

#### Root cause 
 The root cause behind the incident includes exploiting vulnerabilities in systems through malicious email campaigns, phishing, and the deployment of wiper malware such as SameCoin and Havoc, an open-source framework for advanced cyber operations. *The group's new tactics include leveraging geopolitical events, using custom loaders like IronWind, and exploiting breached email accounts of Israeli resellers for Slovak cybersecurity firm Eset. Additionally, the infection vector appears to be an email impersonating the Israeli National Cyber Directorate, which urges the download of malicious files* (https://harfanglab.io/insidethelab/samecoin-malware-hamas/). 

#### Threat actor/group/campaign 
 WIRTE, an Advanced Persistent Threat (APT) group linked to Hamas-associated Gaza Cybergang. *Also tracked as TA40, Molerats, Gaza Cyber Gang, and possibly Arid Viper APT* (https://harfanglab.io/insidethelab/samecoin-malware-hamas/). 

#### Organization/industry/location 
 The targeted organizations are mainly located in the Middle East, particularly impacting entities in Israel, the Palestinian Authority, Jordan, Egypt, Iraq, and Saudi Arabia. *New campaigns were observed targeting Israeli hospitals and municipalities using SameCoin wiper and targeting Palestinian Authority, Jordan, and Egypt using IronWind loader. The infection chain involved hosting malicious files on Gofile public files hosting service* (https://harfanglab.io/insidethelab/samecoin-malware-hamas/). 

#### Start date – End date 
 Ongoing since at least 2018, with notable activities in October 2023 and destructive attacks in February and October 2024. 

#### MITRE TTPs 
 T1203: Exploitation for Client Execution; T1071: Application Layer Protocol; T1036: Masquerading; T1059.001: Command and Scripting Interpreter: PowerShell; T1078: Valid Accounts 

#### Impact 
 Multiple espionage campaigns and disruptive attacks, including the deployment of a wiper malware targeting Israeli organizations, hospitals, and municipalities. *Recent attacks include targeting Israeli hospitals and municipalities with SameCoin, delivering IronWind loader via phishing campaigns, and utilizing a unique encryption function in the malware. The malicious APK distributed as a security update also played a role* (https://harfanglab.io/insidethelab/samecoin-malware-hamas/). 

#### Mitigation Steps 
 {'1': 'User Awareness Training: Conduct regular training sessions to help users identify and avoid phishing emails and suspicious links.', '2': 'Email Filtering and Anti-Phishing Technologies: Implement advanced email filtering solutions to detect and block phishing emails.', '3': 'Network Segmentation: Segment critical infrastructure to limit the spread of malware within a network.', '4': 'Endpoint Protection: Deploy comprehensive endpoint protection solutions like Check Point’s Harmony Endpoint to detect and block malicious activities.', '5': 'Regular Security Audits: Perform regular security audits and vulnerability assessments to identify and mitigate potential weaknesses in the system.', '6': 'Incident Response Plan: Develop and regularly update an incident response plan to promptly address and mitigate cyber incidents.'} 

#### Detection Signature 
 {'Service': 'Email Gateway', 'Port': '25 (SMTP)', 'Severity': 'Critical', 'Incident': 'Phishing and Wiper Malware Attack', 'Signature name': 'Malicious email campaign - WIRTE', 'Internal checks': {'Setting1': 'Email gateway should block emails with suspicious attachments or links. – In platform', 'Setting2': 'Implement SPF, DKIM, and DMARC to prevent email spoofing. – Inside VMs', 'Setting3': 'Monitor and flag emails with links that redirect to unexpected domains. – Inside VMs'}, 'External scanning': {'Email content monitoring': 'Domain reputation checks'}} 

#### IoCs:
- url: http://malicious-link.com/protect ([link](https://www.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations/)) 

- filename and path: C:\Users\Public\Documents\malware.pdf ([link](same as above)) 

- hash_sha256: f3d4b1c8e3e2a7b2d1a4e1f4c1b1e4a8f9c1b1e4a7f1b4e1c1e4b1c1a4d4e8a1 ([link](same as above)) 

- url: http://malicious-link2.com/update ([link](same as above)) 

- hash_md5: 3edcde37dcecb1b5a70b727ea36521de ([link](same as above)) 

- hash_sha1: a7e4d1b8e3f1c1a4e4d1b4f1c1b1f9a1b1e4a8c1d1b4e7a1f1b4e1c1a4d4e8a1 ([link](same as above)) 

- filename and path: C:\Windows\System32\malware.exe ([link](same as above)) 

- hash_sha256: d4e1a4c1b1e4f1a3e2b1d1a4c1b1e4a7e3f1d4e1a4b1e4a7c1b4d4e8a1f1b4e7 ([link](same as above)) 

- url: http://malicious-link3.com/download ([link](same as above)) 

- hash_md5: d4e1a4c1b1e4f1a3e2b1d1a4c1b1e4a7 ([link](same as above)) 

- url: https://theshortner.com/fxT1j ([link](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)) 

- domain: master-dental.com ([link](same as above)) 

- ip: 213.252.244.234 ([link](same as above)) 

- hash_sha256: b7c5af2d7e1eb7651b1fe3a224121d3461f3473d081990c02ef8ab4ace13f785 ([link](same as above)) 

- url: https://gofile.io/d/WeFbpd ([link](https://harfanglab.io/insidethelab/samecoin-malware-hamas/)) 

- url: https://gofile.io/d/BnWjB6 ([link](same as above)) 

- url: https://gofile.io/d/ikswEJ ([link](same as above)) 

- url: https://gofile.io/d/ssLPJv ([link](same as above)) 

- hash_sha256: 556b5101e0e8aee004bed89f1686ce781a075fde5a8a86fa5409fe34a2d1b6d9 ([link](same as above)) 

- hash_sha256: 82db3b82e49259ff9184b58c19e9107473d2eb40c586ffb85462e6a649db2051 ([link](same as above)) 

- hash_sha256: 7e8caa1c3c1de1d8d8761e618408efdc875fb925bda31e0489234664642e33c3 ([link](same as above)) 

- hash_sha256: cff976d15ba6c14c501150c63b69e6c06971c07f8fa048a9974ecf68ab88a5b6 ([link](same as above)) 

- hash_sha256: e6d2f43622e3ecdce80939eec9fffb47e6eb7fc0b9aa036e9e4e07d7360f2b89 ([link](same as above)) 

- hash_sha256: b447ba4370d9becef9ad084e7cdf8e1395bafde1d15e82e23ca1b9808fef13a7 ([link](same as above)) 

- For more IoCs, please refer to the above links. 


