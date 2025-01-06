Source: [https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/#new_tab](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/#new_tab)

## Related articles (describing the same threat) 
- https://www.helpnetsecurity.com/2024/11/26/romcom-backdoor-cve-2024-9680-cve-2024-49039
- https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild#new_tab
- https://thehackernews.com/2024/11/romcom-exploits-zero-day-firefox-and.html
- https://www.darkreading.com/application-security/romcom-apt-zero-day-zero-click-browser-escapes-firefox-tor
- https://www.techtarget.com/searchsecurity/news/366616460/Russian-hackers-exploit-Firefox-Windows-zero-days-in-wild
- https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild
- https://www.bleepingcomputer.com/news/security/firefox-and-windows-zero-days-exploited-by-russian-romcom-hackers
- https://www.govinfosecurity.com/russian-hackers-target-mozilla-windows-in-new-exploit-chain-a-26916

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: RomCom exploits Firefox and Windows zero days in the wild 

#### Root cause 
 The root cause involves zero-day vulnerabilities in Mozilla (CVE-2024-9680) and Windows (CVE-2024-49039). The Firefox vulnerability is a use-after-free bug in the animation timeline feature, affecting Firefox, Thunderbird email client, and Tor Browser. The Windows vulnerability is a privilege escalation bug in the Task Scheduler. CVE-2024-9680 has a CVSS score of 9.8, enabling code execution in the restricted context of the browser. CVE-2024-49039 has a CVSS score of 8.8, allowing arbitrary code execution in the context of the logged-in user. *ESET discovered the sandbox escape exploit used in conjunction with CVE-2024-9680* (https://www.techtarget.com/searchsecurity/news/366616460/Russian-hackers-exploit-Firefox-Windows-zero-days-in-wild). *The first vulnerability (CVE-2024-9680) allows code execution in the browser's restricted context, and the second (CVE-2024-49039) allows arbitrary code execution outside Firefox’s sandbox. Both vulnerabilities were discovered by ESET researcher Damien Schaeffer, and were fixed by Mozilla and Microsoft shortly after being reported* (https://www.helpnetsecurity.com/2024/11/26/romcom-backdoor-cve-2024-9680-cve-2024-49039/). *The attack chain involved a fake website (economistjournal.cloud) redirecting victims to a server hosting the payload* (https://thehackernews.com/2024/11/romcom-exploits-zero-day-firefox-and.html). *RomCom used a combination of browser-based exploit and privilege escalation flaw to bypass the Firefox sandbox, as noted by Satnam Narang* (https://www.govinfosecurity.com/russian-hackers-target-mozilla-windows-in-new-exploit-chain-a-26916). *RomCom exploited Firefox and Tor Browser users across Europe and North America* (https://www.bleepingcomputer.com/news/security/firefox-and-windows-zero-days-exploited-by-russian-romcom-hackers/). *The campaign leveraged a zero-click code execution exploit, spreading the RomCom backdoor from RomCom-controlled servers* (https://www.darkreading.com/application-security/romcom-apt-zero-day-zero-click-browser-escapes-firefox-tor). 

#### Threat actor/group/campaign 
 The attack was carried out by the Russia-aligned RomCom group, also known as Storm-0978, Tropical Scorpius, or UNC2596. RomCom has a track record of cybercrime and espionage since 2022. In June 2023, RomCom exploited CVE-2023-36884, a Windows Search zero-day, for espionage and ransomware attacks. *RomCom also targeted Tor Browser users (versions 12 and 13)* (https://www.bleepingcomputer.com/news/security/firefox-and-windows-zero-days-exploited-by-russian-romcom-hackers/). *RomCom's recent activities include politically motivated espionage* (https://www.darkreading.com/application-security/romcom-apt-zero-day-zero-click-browser-escapes-firefox-tor). 

#### Organization/industry/location 
 Targets included governmental entities in Ukraine and Europe, the pharmaceutical and insurance sectors in the US, the legal sector in Germany, and the defense and energy sectors in Ukraine. Potential victims were located mainly in Europe and North America. 

#### Start date – End date 
 The attacks were identified from October 8, 2024 to November 4, 2024. 

#### MITRE TTPs 
 {'T1583': 'Acquire Infrastructure (Confidence: High)', 'T1587.001': 'Develop Capabilities: Malware (Confidence: High)', 'T1587.004': 'Develop Capabilities: Exploits (Confidence: High)', 'T1588.003': 'Obtain Capabilities: Code Signing Certificates (Confidence: Medium)', 'T1588.005': 'Obtain Capabilities: Exploits (Confidence: High)', 'T1588.006': 'Obtain Capabilities: Vulnerabilities (Confidence: Medium)', 'T1608': 'Stage Capabilities (Confidence: High)', 'T1189': 'Drive-by Compromise (Confidence: High)', 'T1053.005': 'Scheduled Task/Job: Scheduled Task (Confidence: High)', 'T1546.015': 'Event Triggered Execution: Component Object Model Hijacking (Confidence: Medium)', 'T1068': 'Exploitation for Privilege Escalation (Confidence: High)', 'T1622': 'Debugger Evasion (Confidence: Medium)', 'T1480': 'Execution Guardrails (Confidence: Medium)', 'T1027.011': 'Obfuscated Files or Information: Fileless Storage (Confidence: Medium)', 'T1553.002': 'Subvert Trust Controls: Code Signing (Confidence: Medium)', 'T1555.003': 'Credentials from Password Stores: Credentials from Web Browsers (Confidence: High)', 'T1552.001': 'Unsecured Credentials: Credentials In Files (Confidence: Medium)', 'T1087': 'Account Discovery (Confidence: Medium)', 'T1518': 'Software Discovery (Confidence: Medium)', 'T1614': 'System Location Discovery (Confidence: Medium)', 'T1021': 'Remote Services (Confidence: Medium)', 'T1560': 'Archive Collected Data (Confidence: Medium)', 'T1185': 'Man in the Browser (Confidence: High)', 'T1005': 'Data from Local System (Confidence: Medium)', 'T1114.001': 'Email Collection: Local Email Collection (Confidence: Medium)', 'T1113': 'Screen Capture (Confidence: Medium)', 'T1071.001': 'Standard Application Layer Protocol: Web Protocols (Confidence: High)', 'T1573.002': 'Encrypted Channel: Asymmetric Cryptography (Confidence: Medium)', 'T1041': 'Exfiltration Over Command-and-Control Channel (Confidence: High)', 'T1565': 'Data Manipulation (Confidence: Medium)', 'T1657': 'Financial Theft (Confidence: Medium)'} 

#### Impact 
 Multiple organizations across various sectors were targeted, with potential victims numbering from a single individual per country to up to 250 according to ESET telemetry. 

#### Mitigation Steps 
 {'1': 'Update to the latest versions of Firefox, Thunderbird, Tor Browser, and Windows to apply security patches.', '2': 'Monitor network traffic for connections to known malicious domains and IP addresses.', '3': 'Implement strict security policies to restrict the use of RPC interfaces and enforce secure configurations.', '4': 'Regularly review and update security measures for software and hardware.', '5': 'Conduct regular security training and awareness programs for employees.', '6': 'Utilize advanced threat detection solutions to identify and mitigate zero-day exploits.'} 

#### Detection Signature 
 {'Service': 'Firefox, Windows Task Scheduler', 'Port': 'Not applicable (browser-based exploit)', 'Severity': 'Critical', 'Incident': 'RomCom exploits Firefox and Windows zero days', 'Signature name': 'RomCom zero-day exploitation', 'Internal checks': {'1': 'Ensure all software is up to date with the latest security patches.', '2': 'Monitor for signs of unusual activity in browsers and task scheduler.', '3': 'Implement sandboxing and isolation techniques for web browsers.'}, 'External scanning': {'1': 'Check for known malicious domains and IP addresses.', '2': 'Look for abnormal network traffic patterns indicating exfiltration.'}} 

#### IoCs:
- hash_sha1: A4AAD0E2AC1EE0C8DD25968FA4631805689757B6 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- hash_sha1: CA6F8966A3B2640F49B19434BA8C21832E77A031 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- hash_sha1: 21918CFD17B378EB4152910F1246D2446F9B5B11 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- hash_sha1: 703A25F053E356EB6ECE4D16A048344C55DC89FD ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- hash_sha1: ABB54C4751F97A9FC1C9598FED1EC9FB9E6B1DB6 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- hash_sha1: A9D445B77F6F4E90C29E385264D4B1B95947ADD5 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- domain: journalctd.live ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- domain: correctiv.sbs ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- domain: cwise.store ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- domain: redircorrectiv.com ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- domain: devolredir.com ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- domain: redirconnectwise.cloud ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- domain: redjournal.cloud ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- ip: 194.87.189.171 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- ip: 178.236.246.241 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- ip: 62.60.238.81 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- ip: 147.45.78.102 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- ip: 46.226.163.67 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- ip: 62.60.237.116 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- ip: 62.60.237.38 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- ip: 194.87.189.19 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- ip: 45.138.74.238 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- ip: 176.124.206.88 ([link](https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/)) 

- For more IoCs, please refer to the above links. 

#### paste IoC
IoC Value
A4AAD0E2AC1EE0C8DD25968FA4631805689757B6
CA6F8966A3B2640F49B19434BA8C21832E77A031
21918CFD17B378EB4152910F1246D2446F9B5B11
703A25F053E356EB6ECE4D16A048344C55DC89FD
ABB54C4751F97A9FC1C9598FED1EC9FB9E6B1DB6
A9D445B77F6F4E90C29E385264D4B1B95947ADD5
journalctd.live
correctiv.sbs
cwise.store
redircorrectiv.com
devolredir.com
redirconnectwise.cloud
redjournal.cloud
194.87.189.171
178.236.246.241
62.60.238.81
147.45.78.102
46.226.163.67
62.60.237.116
62.60.237.38
194.87.189.19
45.138.74.238
176.124.206.88

