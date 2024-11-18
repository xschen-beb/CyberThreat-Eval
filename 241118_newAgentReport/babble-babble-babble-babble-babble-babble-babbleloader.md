Source: [https://intezer.com/blog/research/babble-babble-babble-babble-babble-babble-babbleloader](https://intezer.com/blog/research/babble-babble-babble-babble-babble-babble-babbleloader)

## Related articles (describing the same threat) 
- https://intezer.com/blog/research/babble-babble-babble-babble-babble-babble-babbleloader
- https://intezer.com/blog/research/babble-babble-babble-babble-babble-babble-babbleloader/
- https://www.broadcom.cn/support/security-center/protection-bulletin/babbleloader-makes-diabolical-use-of-junk-code

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: BabbleLoader Malware Campaign 

#### Root cause 
 The root cause behind the incident is the deployment of the BabbleLoader, a sophisticated loader that uses advanced evasion techniques to bypass antivirus and sandbox environments. The loader uses methods such as junk code insertion, dynamic API resolution, shellcode loading, anti-analysis measures, and *metamorphic transformations* (https://intezer.com/blog/research/babble-babble-babble-babble-babble-babble-babbleloader/) to evade detection. 

#### Threat actor/group/campaign 
 Not explicitly mentioned in the document, but the BabbleLoader campaign is associated with delivering malware like the WhiteSnake stealer. 

#### Organization/industry/location 
 The campaigns target a vast range of users, including English and Russian-speaking individuals. Specific focus on business professionals in finance and administration. The loader masquerades as *accounting software and eligibility checks forms* (https://intezer.com/blog/research/babble-babble-babble-babble-babble-babble-babbleloader/). 

#### Start date – End date 
 Not explicitly mentioned in the document. 

#### MITRE TTPs 
 ['T1027: Obfuscated Files or Information', 'T1055: Process Injection', 'T1071: Application Layer Protocol', 'T1082: System Information Discovery', 'T1497: Virtualization/Sandbox Evasion'] 

#### Impact 
 The impact includes the delivery of malicious payloads such as info-stealers or ransomware, including *WhiteSnake stealer and Meduza stealer* (https://intezer.com/blog/research/babble-babble-babble-babble-babble-babble-babbleloader/), to target systems. Specific numbers of impacted devices or financial losses are not mentioned. 

#### Mitigation Steps 
 ['Implement advanced endpoint protection solutions that can detect and block suspicious behavior associated with malware loaders.', 'Regularly update antivirus and anti-malware tools to recognize the latest threats and evasion techniques.', 'Use network monitoring tools to detect unusual traffic patterns that may indicate malware communication with C2 servers.', 'Educate employees about the risks of downloading and executing software from untrusted sources.', 'Implement strict access controls and application whitelisting to prevent unauthorized execution of software.', 'Conduct regular security audits and penetration testing to identify and mitigate vulnerabilities.'] 

#### Detection Signature 
 {'Service': 'Windows (BabbleLoader)', 'Port': 'N/A (Dynamic API resolution and in-memory execution)', 'Severity': 'Critical', 'Incident': 'BabbleLoader infection', 'Signature name': 'BabbleLoader detection', 'Internal checks': ['Setting1: Monitor for unusual API calls, especially those resolved dynamically at runtime.', 'Setting2: Detect excessive use of junk code and metamorphic transformations in executable files.', 'Setting3: Identify and block processes attempting to decrypt and execute shellcode in memory.'], 'External scanning': ['Detect connections to known C2 infrastructure or unusual network traffic patterns.', 'Monitor for the presence of known BabbleLoader and WhiteSnake stealer hashes.']} 

#### IoCs:
- hash_sha256: a08db4c7b7bacc2bacd1e9a0ac7fbb91306bf83c279582f5ac3570a90e8b0f87 ([link](https://intezer.com/blog/research/babble-babble-babble-babble-babble-babble-babbleloader/)) 

- hash_sha256: 052c776fdc9700dfb37f964a73d461a57efad30a01bcf54505d7abcd601e6ff3 ([link](same as above)) 

- hash_sha256: 0ad8513b62a778d7e426627be3ed2dbaf00d99b9802a1f566dc9203e3d311fc3 ([link](same as above)) 

- hash_sha256: 0f6847d33cb38b0ed6dc1d8cfe3dc5d2e293d91c4880e3b4f5ddb77fd9d4cd1f ([link](same as above)) 

- hash_sha256: 114b868f319162c5d6ff92796e41910f54de0e89f895a066fd4980c6dba2e323 ([link](same as above)) 

- hash_sha256: 1367fb270f35512b17fe5e73cc0233ace272daafe15cf94e45f696431f52332f ([link](same as above)) 

- hash_sha256: 1537965c7722a9886d542688fcbafecd1248b2fbd56e9a90a803a50e880e1bb8 ([link](same as above)) 

- hash_sha256: 16200bbe4646fe8cefeee5be20ce55c50300485f3356ab181fb930bd02536709 ([link](same as above)) 

- hash_sha256: 1da4de2b4b87bff7f9f1a3208c5c663a06f7f9b67f918e5a5e8e860e759b7075 ([link](same as above)) 

- hash_sha256: 200289d5a408a2e49a894228edb3324548ca5c5c0283d09486aa287df41f15bc ([link](same as above)) 

- For more IoCs, please refer to the above links. 


