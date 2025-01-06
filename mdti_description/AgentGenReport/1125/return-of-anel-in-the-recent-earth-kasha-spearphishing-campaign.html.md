Source: [https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)

## Related articles (describing the same threat) 
- https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html
- https://app.daily.dev/posts/guess-who-s-back---the-return-of-anel-in-the-recent-earth-kasha-spear-phishing-campaign-in-2024-bujwkorvp

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Earth Kasha Spear-phishing Campaign 

#### Root cause 
 The root cause behind the incident is the use of spear-phishing emails containing malicious attachments or links. These emails trick recipients into downloading and executing malware, specifically the ANEL backdoor and NOOPDOOR, by exploiting human curiosity and trust. The campaign used various techniques to bypass security measures, including macro-enabled documents, shortcut files, and encoded payloads. *The ANEL malware was previously used by APT10 until 2018* (https://app.daily.dev/posts/guess-who-s-back---the-return-of-anel-in-the-recent-earth-kasha-spear-phishing-campaign-in-2024-bujwkorvp). 

#### Threat actor/group/campaign 
 Earth Kasha (potentially linked to APT10) 

#### Organization/industry/location 
 Individuals and organizations in Japan, particularly those affiliated with political organizations, research institutions, think tanks, and those related to international relations. 

#### Start date – End date 
 June 2024 – Ongoing (as of October 2024) 

#### MITRE TTPs 
 {'T1566.001': 'Spearphishing Attachment - Confidence: High', 'T1203': 'Exploitation for Client Execution - Confidence: Moderate', 'T1059.001': 'PowerShell - Confidence: Moderate', 'T1064': 'Scripting - Confidence: Moderate', 'T1071.001': 'Web Protocols - Confidence: High', 'T1027': 'Obfuscated Files or Information - Confidence: High', 'T1105': 'Ingress Tool Transfer - Confidence: High', 'T1078': 'Valid Accounts - Confidence: Moderate'} 

#### Impact 
 Potentially significant given the targeted nature, focusing on political and research entities, but specific numbers of affected individuals or organizations were not disclosed. 

#### Mitigation Steps 
 {'1': 'Educate employees on recognizing spear-phishing emails and the dangers of enabling macros in documents.', '2': 'Implement robust email filtering solutions to detect and block malicious attachments and links.', '3': 'Use endpoint security solutions that can detect and block malicious macros and scripts.', '4': 'Regularly update and patch all software to mitigate exploitation of known vulnerabilities.', '5': 'Employ network segmentation and least privilege principles to limit the spread of malware.', '6': 'Conduct regular security awareness training for all employees, focusing on phishing threats.', '7': 'Use advanced threat detection tools to identify and respond to suspicious activities quickly.'} 

#### Detection Signature 
 {'Service': 'Email Security, Endpoint Security', 'Port': 'N/A (Email-based attack)', 'Severity': 'Critical', 'Incident': 'Earth Kasha Spear-phishing Campaign', 'Signature name': 'Earth Kasha Spear-phishing Detection', 'Internal checks': {'Setting1': 'Ensure email filtering rules are in place to detect spear-phishing attempts.', 'Setting2': 'Monitor for suspicious macro-enabled document executions.', 'Setting3': 'Alert on the execution of known malicious PowerShell commands and scripts.'}, 'External scanning': 'Look for indicators of compromise related to spear-phishing email patterns and known malicious domains.'} 

#### IoCs:
- url: http://139.84.131.62 ([link](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)) 

- url: http://139.84.136.105 ([link](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)) 

- url: http://45.32.116.146 ([link](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)) 

- url: http://45.77.252.85 ([link](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)) 

- url: http://208.85.18.4 ([link](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)) 

- For more IoCs, please refer to the above links. 

#### paste IoC
IoC Value
http://139.84.131.62
http://139.84.136.105
http://45.32.116.146
http://45.77.252.85
http://208.85.18.4

