Source: [https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)

## Related articles (describing the same threat) 
- https://threatfox.abuse.ch/browse/tag/Hexon
- https://csirtasobancaria.com/nueva-amenaza-denominada-hexon-stealer
- https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident 
 Hexon Stealer Leak 

#### Root cause 
 The root cause behind the incident is the development and distribution of the Hexon Stealer malware, a rebranded version of the Stealit Stealer, leveraging the Electron framework and NSIS installer format. The malware is capable of stealing sensitive information such as browser credentials, Discord tokens, 2FA backup codes, credit card details, and cryptocurrency wallet data. The malware developers used various outlets, including Telegram and websites, to promote and distribute the malware, allowing remote control over compromised systems. *Key capabilities include Discord injection, game account access, and advanced remote control features like screen capture, keyboard/mouse input control, terminal command execution, and chat for ransom negotiations. It employs obfuscation techniques to evade detection and creates a secondary executable to facilitate data exfiltration* (https://csirtasobancaria.com/nueva-amenaza-denominada-hexon-stealer). 

#### Threat actor/group/campaign 
 The threat actor behind Hexon Stealer is likely a Turkish individual or group, previously associated with the Stealit Stealer group and using monikers such as ‘Xeina’ and ‘art6q’ and ‘dojkv2’. The group operates under a new channel called Hexon Grabber and previously rebranded from the Stealit group, which had its source code leaked on GitHub by the 'Returnit group'. 

#### Organization/industry/location 
 The malware targets organizations and individuals, particularly those using Discord, gaming accounts, and cryptocurrency wallets. It leverages Coinbase for anonymous cryptocurrency payments. 

#### Start date – End date 
 The malware was first seen in the wild in August 2024, and the report was published on November 22, 2024. First seen on October 23, 2024, and last seen on October 27, 2024. 

#### MITRE TTPs 
 {'Execution (TA0002)': ['T1047: Windows Management Instrumentation (Confidence: High)', 'T1059: Command and Scripting Interpreter (Confidence: High)'], 'Persistence (TA0003)': ['T1547.001: Registry Run Keys / Startup Folder (Confidence: High)', 'T1574.002: DLL Side-Loading (Confidence: Medium)'], 'Privilege Escalation (TA0004)': ['T1055: Process Injection (Confidence: High)', 'T1547.001: Registry Run Keys / Startup Folder (Confidence: High)'], 'Defense Evasion (TA0005)': ['T1036: Masquerading (Confidence: High)', 'T1055: Process Injection (Confidence: High)', 'T1497: Virtualization/Sandbox Evasion (Confidence: Medium)'], 'Credential Access (TA0006)': ['T1003: OS Credential Dumping (Confidence: High)'], 'Discovery (TA0007)': ['T1012: Query Registry (Confidence: High)', 'T1057: Process Discovery (Confidence: High)', 'T1018: Remote System Discovery (Confidence: Medium)', 'T1082: System Information Discovery (Confidence: High)'], 'Collection (TA0009)': ['T1005: Data from Local System (Confidence: High)'], 'Command and Control (TA0011)': ['T1573: Encrypted Channel (Confidence: Medium)', 'T1071: Application Layer Protocol (Confidence: High)']} 

#### Impact 
 The malware has a significant impact, potentially compromising numerous systems and stealing sensitive information such as browser credentials, Discord tokens, credit card details, and cryptocurrency wallet data. Specific figures on the number of devices or financial losses are not provided. 

#### Mitigation Steps 
 ['Implement Defense-in-Depth Strategy: Combine network segmentation, robust perimeter defenses, and endpoint security.', 'Invest in Threat Intelligence: Engage with threat intelligence services and update defenses regularly.', 'Enhance Employee Training: Conduct regular cybersecurity training programs.', 'Develop an Incident Response Plan: Establish and regularly test an incident response plan.', 'Conduct Regular Security Audits: Perform periodic security audits to identify and address potential weaknesses.', 'Collaborate with Industry Peers: Engage in information sharing with cybersecurity communities.', 'Update and Patch Systems: Regularly update and patch operating systems and applications.', 'Utilize Advanced Endpoint Protection: Deploy advanced endpoint protection solutions with behavioral analysis and heuristic detection.', 'Implement Application Whitelisting: Restrict execution of unauthorized applications.'] 

#### Detection Signature 
 {'Service': 'Electron Framework', 'Port': 'Not specified', 'Severity': 'Critical', 'Incident': 'Hexon Stealer', 'Signature name': 'Hexon Stealer detection', 'Internal checks': ['Setting1: Ensure Electron-based applications are verified before deployment.', 'Setting2: Monitor for suspicious JavaScript activity within Electron applications.', 'Setting3: Regularly audit and restrict access to sensitive information on systems.'], 'External scanning': ['Monitor for the presence of Hexon Stealer-related domains and IPs.', 'Check for unusual network traffic patterns associated with data exfiltration.']} 

#### Contact 
 csirt@asobancaria.com 

#### IoCs:
- email: csirt@asobancaria.com ([link](https://csirtasobancaria.com/nueva-amenaza-denominada-hexon-stealer)) 
Not found for email csirt@asobancaria.com in VT. 

- ip: 72.145.3.21 ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- ip: 20.19.32.198 ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- ip: 20.151.152.98 ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- ip: 20.199.91.177 ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- ip: 4.233.148.165 ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- domain: Hexon.fun ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- domain: hexoncopy.vercel.app ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- domain: stealit.vercel.app ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- hash_md5: e173d1216236bccdc15c56bf27859a1d ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- hash_sha256: 326c21e845863ea6ebe7d09ec3915d99e18f95e575e97aac2f71ae41160327e1 ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- hash_sha256: b55afdbd2e8d258a54aefd98570e4749ad993f4322ec7e3b27d7a7ab413f7246 ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- hash_sha256: 9a5aa40a67378d078046c2d22e23fa110881f722067a3a413c99cfbfd0402d1f ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 

- hash_sha1: e85b03f4f2fff63c48c6983ac1e8d6c0a505ca56 ([link](https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding)) 
Not found for hash_sha1 e85b03f4f2fff63c48c6983ac1e8d6c0a505ca56 in VT. 

- For more IoCs, please refer to the above links. 

#### paste IoC
72.145.3.21
20.19.32.198
20.151.152.98
20.199.91.177
4.233.148.165
Hexon.fun
hexoncopy.vercel.app
stealit.vercel.app
e173d1216236bccdc15c56bf27859a1d
326c21e845863ea6ebe7d09ec3915d99e18f95e575e97aac2f71ae41160327e1
b55afdbd2e8d258a54aefd98570e4749ad993f4322ec7e3b27d7a7ab413f7246
9a5aa40a67378d078046c2d22e23fa110881f722067a3a413c99cfbfd0402d1f

