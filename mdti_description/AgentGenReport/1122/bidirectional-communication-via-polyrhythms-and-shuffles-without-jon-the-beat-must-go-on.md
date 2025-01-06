Source: [https://blog.talosintelligence.com/bidirectional-communication-via-polyrhythms-and-shuffles-without-jon-the-beat-must-go-on](https://blog.talosintelligence.com/bidirectional-communication-via-polyrhythms-and-shuffles-without-jon-the-beat-must-go-on)

## Related articles (describing the same threat) 
- https://blog.talosintelligence.com/bidirectional-communication-via-polyrhythms-and-shuffles-without-jon-the-beat-must-go-on
- https://thehackernews.com/2024/11/vietnamese-hacker-group-deploys-new-pxa.html
- https://gurucul.com/latest-threats/new-pxa-stealer-targets-government-and-education-sectors-for-sensitive-information
- https://socprime.com/blog/pxa-stealer-detection
- https://www.rewterz.com/threat-advisory/vietnamese-threat-group-launches-new-pxa-stealer-to-target-asia-and-europe-active-iocs
- https://blog.talosintelligence.com/new-pxa-stealer
- https://www.scworld.com/brief/novel-pxa-stealer-leveraged-by-vietnamese-hackers

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: PXA Stealer Campaign 

#### Root cause 
 The PXA Stealer malware, a Python-based information stealer, targets sensitive information, including credentials for online accounts, VPN and FTP clients, financial data, browser cookies, gaming software data, and cryptocurrency wallets. The malware decrypts browser master passwords to steal stored credentials. Complex obfuscation techniques and a Rust loader executable are used for deployment *The changes* (https://blog.talosintelligence.com/new-pxa-stealer/). The campaign features advanced obfuscation techniques in batch scripts and employs a Glassdoor job application form as a lure document *The changes* (https://socprime.com/blog/pxa-stealer-detection/). The malware uses advanced obfuscation techniques to evade detection *The changes* (https://gurucul.com/latest-threats/new-pxa-stealer-targets-government-and-education-sectors-for-sensitive-information/). The stealer disables antivirus programs and targets Facebook cookies for further account information *The changes* (https://thehackernews.com/2024/11/vietnamese-hacker-group-deploys-new-pxa.html). *Attackers delivered phishing emails with a ZIP file attachment containing a Rust-based loader that prompts Windows batch scripts, facilitating the deactivation of antivirus software prior to deploying the malware* (https://www.scworld.com/brief/novel-pxa-stealer-leveraged-by-vietnamese-hackers). 

#### Threat actor/group/campaign 
 Vietnamese-speaking threat actor, potentially linked to CoralRaider *The changes* (https://blog.talosintelligence.com/new-pxa-stealer/). They leverage a Telegram bot for data exfiltration *The changes* (https://socprime.com/blog/pxa-stealer-detection/). The actor has been selling stolen credentials on a Telegram channel linked to CoralRaider *The changes* (https://gurucul.com/latest-threats/new-pxa-stealer-targets-government-and-education-sectors-for-sensitive-information/). The attacker uses Vietnamese comments and a hard-coded Telegram account named 'Lone None' with an icon of Vietnam's national flag and emblem of Vietnam's Ministry of Public Security *The changes* (https://thehackernews.com/2024/11/vietnamese-hacker-group-deploys-new-pxa.html). 

#### Organization/industry/location 
 Government and education entities in Europe and Asia, including India, Sweden, and Denmark. 

#### Start date – End date 
 Not specified. 

#### MITRE TTPs 
 ['T1071.001: Application Layer Protocol: Web Protocols (High confidence)', 'T1070.004: Indicator Removal on Host: File Deletion (Medium confidence)', 'T1003.002: Credential Dumping: Security Account Manager (SAM) (High confidence)', 'T1083: File and Directory Discovery (Medium confidence)'] 

#### Impact 
 Compromises sensitive information, including online credentials, financial data, browser cookies, and cryptocurrency wallets, potentially allowing direct access to victims' environments. *Exploits Facebook Ads Manager and Graph API for further account and ad-related information* (https://socprime.com/blog/pxa-stealer-detection/). 

#### Mitigation Steps 
 ['Deploy the Snort rules and ClamAV signatures released by Cisco Talos to detect and defend against PXA Stealer.', 'Implement multi-factor authentication (MFA) for all online accounts to add an extra layer of security.', 'Regularly update and patch systems and software to mitigate vulnerabilities.', 'Conduct security awareness training for employees to recognize phishing attempts and other social engineering tactics.', 'Implement endpoint detection and response (EDR) solutions to monitor and respond to suspicious activities.', 'Regularly back up critical data and store backups in a secure, offline location.'] 

#### Detection Signature 
 {'Service': 'General Malware Detection (PXA Stealer)', 'Port': 'Not specified', 'Severity': 'Critical', 'Incident': 'PXA Stealer Campaign', 'Signature name': 'PXA Stealer Detection', 'Internal checks': ['Deploy Snort rules and ClamAV signatures for PXA Stealer detection. – In platform', 'Monitor for abnormal credential usage and access patterns. – Inside VMs', 'Ensure endpoint security solutions are updated and configured to detect PXA Stealer. – Inside VMs'], 'External scanning': ['Monitor network traffic for indicators of PXA Stealer communication.', 'Scan for unauthorized access attempts and unusual login activities.']} 

#### IoCs:
- hash_sha256: c20fbc33680d745ec5ff7022c282a6fe969c6e6c7d77b7cfac34e6c19367cf9a ([link](https://www.virustotal.com/gui/file/c20fbc33680d745ec5ff7022c282a6fe969c6e6c7d77b7cfac34e6c19367cf9a/details%C2%A0)) 

- hash_md5: 3bc6d86fc4b3262137d8d33713ed6082 ([link](https://www.virustotal.com/gui/file/c20fbc33680d745ec5ff7022c282a6fe969c6e6c7d77b7cfac34e6c19367cf9a/details%C2%A0)) 

- hash_sha256: bea312ccbc8a912d4322b45ea64d69bb3add4d818fd1eb7723260b11d76a138a ([link](https://www.virustotal.com/gui/file/bea312ccbc8a912d4322b45ea64d69bb3add4d818fd1eb7723260b11d76a138a/details)) 

- hash_md5: 200206279107f4a2bb1832e3fcd7d64c ([link](https://www.virustotal.com/gui/file/bea312ccbc8a912d4322b45ea64d69bb3add4d818fd1eb7723260b11d76a138a/details)) 

- hash_sha256: 47ecaab5cd6b26fe18d9759a9392bce81ba379817c53a3a468fe9060a076f8ca ([link](https://www.virustotal.com/gui/file/47ecaab5cd6b26fe18d9759a9392bce81ba379817c53a3a468fe9060a076f8ca/details%C2%A0)) 

- hash_md5: 71fea034b422e4a17ebb06022532fdde ([link](https://www.virustotal.com/gui/file/47ecaab5cd6b26fe18d9759a9392bce81ba379817c53a3a468fe9060a076f8ca/details%C2%A0)) 

- hash_sha256: 3a2ea65faefdc64d83dd4c06ef617d6ac683f781c093008c8996277732d9bd66 ([link](https://virustotal.com/gui/file/3a2ea65faefdc64d83dd4c06ef617d6ac683f781c093008c8996277732d9bd66/details%C2%A0)) 

- hash_md5: 8b84d61bf3ffec822e2daf4a3665308c ([link](https://virustotal.com/gui/file/3a2ea65faefdc64d83dd4c06ef617d6ac683f781c093008c8996277732d9bd66/details%C2%A0)) 

- domain: tvdseo.com ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- url: http://tvdseo.com/file/synaptics.zip ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- url: http://tvdseo.com/file/PXA/PXA_PURE_ENC ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- url: http://tvdseo.com/file/PXA/PXA_BOT ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- url: http://tvdseo.com/file/PXA/Cookie_Ext.zip ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- token: 7545164691:AAEJ4E2f-4KZDZrLID8hSRSJmPmR1h-a2M4 ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- token: 7414494371:AAGgbY4XAvxTWFgAYiAj6OXVJOVrqgjdGVs ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- chat_id: -1002174636072 ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- chat_id: -1002150158011 ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- chat_id: -4559798560 ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- chat_id: -4577199885 ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- chat_id: -4575205410 ([link](https://blog.talosintelligence.com/new-pxa-stealer/)) 

- For more IoCs, please refer to the above links. 

#### paste IoC
IoC Value
c20fbc33680d745ec5ff7022c282a6fe969c6e6c7d77b7cfac34e6c19367cf9a
3bc6d86fc4b3262137d8d33713ed6082
bea312ccbc8a912d4322b45ea64d69bb3add4d818fd1eb7723260b11d76a138a
200206279107f4a2bb1832e3fcd7d64c
47ecaab5cd6b26fe18d9759a9392bce81ba379817c53a3a468fe9060a076f8ca
71fea034b422e4a17ebb06022532fdde
3a2ea65faefdc64d83dd4c06ef617d6ac683f781c093008c8996277732d9bd66
8b84d61bf3ffec822e2daf4a3665308c
tvdseo.com
http://tvdseo.com/file/synaptics.zip
http://tvdseo.com/file/PXA/PXA_PURE_ENC
http://tvdseo.com/file/PXA/PXA_BOT
http://tvdseo.com/file/PXA/Cookie_Ext.zip
7545164691:AAEJ4E2f-4KZDZrLID8hSRSJmPmR1h-a2M4
7414494371:AAGgbY4XAvxTWFgAYiAj6OXVJOVrqgjdGVs
-1002174636072
-1002150158011
-4559798560
-4577199885
-4575205410

