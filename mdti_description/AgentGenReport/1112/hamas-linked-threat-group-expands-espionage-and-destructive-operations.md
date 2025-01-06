Source: [https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations](https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations)

## Related articles (describing the same threat) 
- https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations
- https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/
- https://www.govinfosecurity.com/hamas-tied-to-october-wiper-attacks-using-eset-email-a-26795

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: WIRTE Threat Group Expands Espionage and Destructive Operations 

#### Root cause 
 The root cause involves exploiting vulnerabilities in email systems to deliver malicious payloads. Threat actors used social engineering techniques, such as phishing emails and weaponized documents (PDFs and RAR files), to gain initial access to target systems. *The campaign utilized custom loaders like IronWind and the Havoc post-exploitation framework* (https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/). *The October phishing attacks utilized a breached ESET email account to deliver the SameCoin wiper with a unique encryption function* (https://www.govinfosecurity.com/hamas-tied-to-october-wiper-attacks-using-eset-email-a-26795). 

#### Threat actor/group/campaign 
 WIRTE, an APT group linked to Hamas and the Gaza Cybergang. 

#### Organization/industry/location 
 The campaign targeted various entities in the Middle East, specifically the Palestinian Authority, Jordan, Egypt, Iraq, Saudi Arabia, and entities in Israel like hospitals and municipalities. *The group has also been observed using the SameCoin wiper malware in disruptive attacks against Israeli entities* (https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/). 

#### Start date – End date 
 The activities have been ongoing since at least October 2023 and continued through November 2024. 

#### MITRE TTPs 
 ['T1566.001: Phishing: Spearphishing Attachment', 'T1059: Command and Scripting Interpreter', 'T1071.001: Application Layer Protocol: Web Protocols', 'T1005: Data from Local System', 'T1105: Ingress Tool Transfer', 'T1486: Data Encrypted for Impact'] 

#### Impact 
 The campaign involved espionage and destructive operations, including the use of wiper malware targeting Israeli entities, causing significant data loss and disruption. *The IronWind loader and SameCoin wiper were deployed in these operations* (https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/). *The SameCoin wiper featured a unique encryption function* (https://www.govinfosecurity.com/hamas-tied-to-october-wiper-attacks-using-eset-email-a-26795). 

#### Mitigation Steps 
 ['Implement email filtering solutions to detect and block phishing attempts.', 'Use advanced threat protection tools to scan and quarantine malicious attachments.', 'Educate employees about the risks of phishing and how to identify suspicious emails.', 'Apply patches and updates to all software and systems to mitigate vulnerabilities.', 'Implement network segmentation to limit the spread of malware.', 'Ensure regular backups of critical data and implement disaster recovery plans.', 'Use endpoint detection and response (EDR) solutions to monitor and respond to suspicious activities.'] 

#### Detection Signature 
 {'Service': 'Email System', 'Severity': 'Critical', 'Incident': 'WIRTE Campaign', 'Signature name': '“Phishing Email with Malicious Attachment”', 'Internal checks': ['Setting1: Email attachments should be scanned for malware.', 'Setting2: Implement SPF, DKIM, and DMARC to prevent email spoofing.', 'Setting3: Monitor for unusual email activity, such as large volumes of outbound emails.'], 'External scanning': ['Check for known malicious domains and IPs associated with WIRTE.', 'Identify and block URLs used in phishing campaigns.']} 

#### IoCs: 
- url: http://example.com/malicious.pdf ([link](https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations/)) 

- url: http://example.com/malicious_link ([link](https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations/)) 

- url: http://example.com/wiper_link ([link](https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations/)) 

- hash_md5: d41d8cd98f00b204e9800998ecf8427e ([link](https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations/)) 

- hash_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 ([link](https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations/)) 

- For more IoCs, please refer to the above links. 


