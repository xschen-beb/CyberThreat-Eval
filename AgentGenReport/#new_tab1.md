Source: [https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/#new_tab](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/#new_tab)

## Related articles (describing the same threat) 
- https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/#new_tab
- https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/
- https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/amp/
- https://any.run/malware-trends/strela
- https://unit42.paloaltonetworks.com/strelastealer-campaign/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: Strela Stealer Targets Europe Stealthily Via WebDav 

#### Root cause 
 The incident exploits WebDAV servers to deliver malicious DLL payloads via base64-encoded PowerShell commands embedded in obfuscated JavaScript files. The phishing campaign leverages spear-phishing emails with ZIP file attachments containing these obfuscated scripts. *The malware also uses ISO files and batch files to execute its payload* (https://any.run/malware-trends/strela). *The updated infection chain involves a JScript file that decodes a Base64-encrypted DLL file* (https://unit42.paloaltonetworks.com/strelastealer-campaign/). 

#### Threat actor/group/campaign 
 The threat actor behind this campaign is the Strela Stealer malware, first identified by DCSO and analyzed by various cybersecurity research organizations including Cyble and Palo Alto. *Strela Stealer has been active since 2022 and frequently updates its tactics and payloads to evade detection* (https://any.run/malware-trends/strela). 

#### Organization/industry/location 
 The targeted regions include Central and Southwestern Europe, specifically Germany and Spain. *Additional targeted industries include IT & ITES, Government & LEA, Technology, Healthcare, and BFSI* (https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/amp/). *The campaign has also affected organizations in the U.S. and targeted over 100 organizations since its emergence* (https://any.run/malware-trends/strela). 

#### Start date – End date 
 The campaign was reported on October 30, 2024, but specific start and end dates are not provided in the blog. *The malware was first observed on November 1, 2022, with significant campaigns in late 2023 and early 2024* (https://any.run/malware-trends/strela). *A new large-scale campaign was observed in January 2024* (https://unit42.paloaltonetworks.com/strelastealer-campaign/). 

#### MITRE TTPs 
 Initial Access (TA0001) - Phishing (T1566); Execution (TA0002) - User Execution (T1203), Command and Scripting Interpreter (T1059); Credential Access (TA0006) - Credential Dumping (T1003); Discovery (TA0007) - System Information Discovery (T1082), File and Directory Discovery (T1083); Command and Control (TA0011) - Application Layer Protocol (T1071); Exfiltration (TA0010) - Exfiltration Over Command and Control Channel (T1041). *Additional Techniques: T1140 - Deobfuscate/Decode Files or Information, T1486 - Data Encrypted for Impact, T1105 - Ingress Tool Transfer* (https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/amp/). 

#### Impact 
 The campaign aims to steal sensitive email configuration details and credentials, perform reconnaissance, and potentially launch further targeted actions on compromised systems. The exact financial losses or the number of impacted individuals/devices are not specified. 

#### Mitigation Steps 
 ['Conduct regular training sessions to educate employees about phishing tactics.', 'Deploy robust endpoint protection solutions to detect and respond to malicious activity.', 'Implement strict access controls on WebDAV servers, ensuring only authorized users have access.', 'Disable WebDAV if it is not required for business operations.', 'Limit the execution of PowerShell scripts and other scripting languages on endpoints.', 'Develop and regularly update an incident response plan for handling phishing attacks and malware infections.', 'Implement multi-factor authentication for accessing sensitive systems and accounts.'] 

#### Detection Signature 
 {'Service': 'WebDAV', 'Port': '80, 443 (typical WebDAV ports)', 'Severity': 'Critical', 'Incident': 'Strela Stealer', 'Signature name': 'WebDAV malicious payload delivery', 'Internal checks': ['Ensure WebDAV is disabled if not required.', 'Implement access controls on WebDAV servers.', 'Monitor for unusual WebDAV access patterns.'], 'External scanning': ['Detect base64-encoded PowerShell commands in web traffic.', 'Identify obfuscated JavaScript files containing suspicious code.']} 

#### IoCs: 
- hash_sha256: dcd7dd2aaef3e87b467ce4e4682a63d2d01da20e31fada494435ae8a921c09ae ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- hash_sha256: 75d996a0a5262bff134d7a752efd1fb6325bc2ce347b084967e06725008180f9 ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- hash_sha256: c5279ff9c215afbd5c54793c6fc36c80d2cefb0342a1471581b15e43bd4a9b08 ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- hash_sha256: be76ab2054ef174331abfef53825254ac26bfc9657dca9c3767a5e5daf7bec1e ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- hash_sha256: 4e38abd0fef9a4b3f4cbc674601bc10766d4db588cb83d3e5fb50ec573c372cd ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- domain: vaultdocker.com ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- domain: cloudslimit.com ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- domain: dailywebstats.com ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- domain: endpointexperiment.com ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- domain: apitestlabs.com ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- ip: 94.159.113.48 ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/)) 

- hash_sha256: a31f222fc283227f5e7988d1ad9c0aecd66d58bb7b4d8518ae23e110308dbf91 ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/amp/)) 

- hash_sha256: 7bdbd180c081fa63ca94f9c22c457376 ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/amp/)) 

- hash_sha256: c67b03c0a91eaefffd2f2c79b5c26a2648b8d3c19a22cadf35453455ff08ead0 ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/amp/)) 

- hash_sha256: 8c69830a50fb85d8a794fa46643493b2 ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/amp/)) 

- hash_sha256: bbcf7a68f4164a9f5f5cb2d9f30d9790 ([link](https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/amp/)) 

- url: http://94.159.113.48/server.php ([link](https://any.run/malware-trends/strela)) 

- url: http://193.109.85.231/server.php ([link](https://any.run/malware-trends/strela)) 

- url: http://91.215.85.209/server.php ([link](https://any.run/malware-trends/strela)) 

- url: http://45.9.74.12/server.php ([link](https://any.run/malware-trends/strela)) 

- url: http://193.109.85.77/server.php ([link](https://any.run/malware-trends/strela)) 

- ip: 45.9.74.32 ([link](https://any.run/malware-trends/strela)) 

- hash_sha256: 0d2d0588a3a7cff3e69206be3d75401de6c69bcff30aa1db59d34ce58d5f799a ([link](https://unit42.paloaltonetworks.com/strelastealer-campaign/)) 

- hash_sha256: e6991b12e86629b38e178fef129dfda1d454391ffbb236703f8c026d6d55b9a1 ([link](https://unit42.paloaltonetworks.com/strelastealer-campaign/)) 

- hash_sha256: f95c6817086dc49b6485093bfd370c5e3fc3056a5378d519fd1f5619b30f3a2e ([link](https://unit42.paloaltonetworks.com/strelastealer-campaign/)) 

- hash_sha256: aea9989e70ffa6b1d9ce50dd3af5b7a6a57b97b7401e9eb2404435a8777be054 ([link](https://unit42.paloaltonetworks.com/strelastealer-campaign/)) 

- hash_sha256: b8e65479f8e790ba627d0deb29a3631d1b043160281fe362f111b0e080558680 ([link](https://unit42.paloaltonetworks.com/strelastealer-campaign/)) 

- hash_sha256: 3189efaf2330177d2817cfb69a8bfa3b846c24ec534aa3e6b66c8a28f3b18d4b ([link](https://unit42.paloaltonetworks.com/strelastealer-campaign/)) 

- hash_sha256: 544887bc3f0dccb610dd7ba35b498a03ea32fca047e133a0639d5bca61cc6f45 ([link](https://unit42.paloaltonetworks.com/strelastealer-campaign/)) 

- hash_sha256: 193.109.85.231 ([link](https://unit42.paloaltonetworks.com/strelastealer-campaign/)) 

#### Additional Information 
 ['Locale settings: The malware checks locale settings using GetKeyboardLayout API, targeting German and Spanish locales *Your changes* (https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/).', "Command-and-control (C2) server: The stolen data is sent to the threat actor's C2 server at 94.159.113.48 *Your changes* (https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/).", "Hardcoded key: Encryption uses a hardcoded key '96be98b2-8a00-410d-87da-2482cc8b7793' *Your changes* (https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/).", 'Encrypted data: Data is encrypted using custom encryption before exfiltration *Your changes* (https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/).', '*The campaign has identified several CVEs: CVE-2024-21887, CVE-2023-46805, CVE-2017-11882, CVE-2024-21893, CVE-2021-44228* (https://cyble.com/blog/strela-stealer-targets-europe-stealthily-via-webdav/amp/).', '*The malware employs advanced obfuscation techniques such as control flow obfuscation and the removal of debugging symbols (PDB strings) to evade detection* (https://any.run/malware-trends/strela).', "*The malware's tactics include using localized language and subject lines in phishing emails to lure victims* (https://any.run/malware-trends/strela).", '*The malware has targeted over 100 organizations since its emergence* (https://any.run/malware-trends/strela).', "*The malware's new variant employs updated obfuscation techniques and is detected by Cortex XDR and Advanced WildFire* (https://unit42.paloaltonetworks.com/strelastealer-campaign/)."] 


