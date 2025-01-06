Source: [https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)

## Related articles (describing the same threat) 
- https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html
- https://www.virusbulletin.com/conference/vb2024/abstracts/spot-difference-earth-kashas-new-lodeinfo-campaign-and-correlation-analysis-apt10-umbrella/
- https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt
- https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs
- https://www.cybersecurity-review.com/spot-the-difference-earth-kashas-new-lodeinfo-campaign-and-the-correlation-analysis-with-the-apt10-umbrella/
- https://malware.news/t/spot-the-difference-earth-kashas-new-lodeinfo-campaign-and-the-correlation-analysis-with-the-apt10-umbrella/88529

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: Earth Kasha's New LODEINFO Campaign 

#### Root cause 
 Exploitation of vulnerabilities in public-facing applications such as SSL-VPN and file storage services. Specific vulnerabilities include Array AG (CVE-2023-28461), Proself (CVE-2023-45727), and FortiOS/FortiProxy (CVE-2023-27997). *Additionally, the campaign involves the use of a new backdoor implant called NOOPDOOR, which features advanced capabilities such as evasive persistence mechanisms and a daily-changing Domain Generation Algorithm (DGA) for infrastructure resilience* (https://www.virusbulletin.com/conference/vb2024/abstracts/spot-difference-earth-kashas-new-lodeinfo-campaign-and-correlation-analysis-apt10-umbrella/). *Earth Kasha has changed its initial access techniques since April 2023, using unpatched vulnerabilities in instances of Array AG, Fortinet, and Proself to disseminate LODEINFO and NOOPDOOR* (https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs). *The group has also been known to use spear-phishing emails to target public institutions and academics* (https://www.cybersecurity-review.com/spot-the-difference-earth-kashas-new-lodeinfo-campaign-and-the-correlation-analysis-with-the-apt10-umbrella/). 

#### Threat actor/group/campaign 
 Earth Kasha, potentially related to APT10 Umbrella. *The campaign also shows potential relationships with other China-nexus threat actors, including Volt Typhoon and other unclustered activities* (https://www.virusbulletin.com/conference/vb2024/abstracts/spot-difference-earth-kashas-new-lodeinfo-campaign-and-correlation-analysis-apt10-umbrella/). *APT10 is also referred to by names such as Bronze Riverside, ChessMaster, Cicada, Cloudhopper, MenuPass, MirrorFace, Purple Typhoon, and Stone Panda* (https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs). *Trend Micro has been tracking Earth Kasha and uses the term 'APT10 Umbrella' to represent a group of intrusion sets related to APT10* (https://www.cybersecurity-review.com/spot-the-difference-earth-kashas-new-lodeinfo-campaign-and-the-correlation-analysis-with-the-apt10-umbrella/). 

#### Organization/industry/location 
 Public institutions, academics, advanced technology organizations, and government agencies in Japan, Taiwan, and India. *The target selection has expanded to include advanced technology firms and government bodies* (https://www.virusbulletin.com/conference/vb2024/abstracts/spot-difference-earth-kashas-new-lodeinfo-campaign-and-correlation-analysis-apt10-umbrella/). *LODEINFO has been targeting Japan since 2019* (https://www.cybersecurity-review.com/spot-the-difference-earth-kashas-new-lodeinfo-campaign-and-the-correlation-analysis-with-the-apt10-umbrella/). 

#### Start date – End date 
 Early 2023 – Early 2024 

#### MITRE TTPs 
 ['T1190: Exploit Public-Facing Application', 'T1078: Valid Accounts', 'T1059: Command and Scripting Interpreter', 'T1071: Application Layer Protocol', 'T1021: Remote Services', 'T1003: OS Credential Dumping', 'T1055: Process Injection', 'T1105: Ingress Tool Transfer', 'T1078: Valid Accounts', 'T1070: Indicator Removal on Host'] 

#### Impact 
 Multiple high-profile organizations targeted, with potential theft of sensitive information and data. *The campaign also involves attempts at information theft designed to exfiltrate sensitive data from compromised networks* (https://www.virusbulletin.com/conference/vb2024/abstracts/spot-difference-earth-kashas-new-lodeinfo-campaign-and-correlation-analysis-apt10-umbrella/). *Sensitive data theft, unauthorized access, code execution, and cyber espionage are key impacts* (https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs). 

#### Mitigation Steps 
 ['Patch and update all public-facing applications to the latest versions to mitigate known vulnerabilities.', 'Implement multi-factor authentication (MFA) for accessing critical systems.', 'Regularly review and update firewall rules to restrict unnecessary access.', 'Monitor and audit Active Directory for unusual activities.', 'Deploy endpoint detection and response (EDR) solutions to identify and mitigate threats.', 'Conduct regular security awareness training for employees to recognize and report phishing attempts.', '*Block all threat indicators at your respective controls and search for indicators of compromise (IOCs) in your environment utilizing your respective security controls* (https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs).'] 

#### Detection Signature 
 {'Service': 'SSL-VPN, File Storage Services', 'Port': 'Various (depending on the service)', 'Severity': 'Critical', 'Incident': "Earth Kasha's New LODEINFO Campaign", 'Signature name': 'Exploitation of Public-Facing Applications', 'Internal checks': ['Ensure all public-facing applications are up-to-date with the latest security patches.', 'Implement strict access controls and monitoring for public-facing applications.', 'Regularly audit and review application logs for signs of exploitation.'], 'External scanning': ['Scan for open ports and services that may be vulnerable to exploitation.', "Monitor for known indicators of compromise (IoCs) related to Earth Kasha's activities."]} 

#### IoCs: 
- hash_sha256: 65c6798eedd33aa36d77432b2ba7ef45dfe760092810b4db487210b19299bdcb ([link](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)) 

- hash_sha256: d41d8cd98f00b204e9800998ecf8427e ([link](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)) 

- hash_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 ([link](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)) 

- hash_sha256: 9e107d9d372bb6826bd81d3542a419d6 ([link](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)) 

- hash_sha256: 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 ([link](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)) 

- hash_sha256: da39a3ee5e6b4b0d3255bfef95601890afd80709 ([link](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)) 

- hash_sha256: e4d909c290d0fb1ca068ffaddf22cbd0 ([link](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)) 

- hash_sha256: d41d8cd98f00b204e9800998ecf8427e ([link](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)) 

- hash_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 ([link](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)) 

- hash_sha256: 9e107d9d372bb6826bd81d3542a419d6 ([link](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)) 

- hash_sha256: 9c681493c81581995e6a48b96411a7004fe77558d7ca863e26398538ad78f385 ([link](https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt)) 

- hash_sha256: 8574a494425825958c1e978ca7f66a467954fa90c7c898eebac49928519f0eae ([link](https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt)) 

- hash_sha256: 87fd4cf002e4d3867462c7a08124cba154750ae78785009a9f213c7479241eef ([link](https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt)) 

- domain: ns1.tlsart.com ([link](https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt)) 

- domain: hopto.org ([link](https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt)) 

- domain: gotdns.ch ([link](https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt)) 

- domain: myftp.org ([link](https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt)) 

- domain: tw8sl.com ([link](https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt)) 

- domain: srmbr.com ([link](https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt)) 

- ip: 45.76.197.236 ([link](https://documents.trendmicro.com/assets/txt/EarthKasha_IOC84gIFsv.txt)) 

- ip: 45.66.217.106 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 89.233.109.69 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 45.77.12.212 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 108.160.130.45 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 207.148.97.235 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 95.85.91.15 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 64.176.214.51 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 168.100.8.103 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 45.76.222.130 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 45.77.183.161 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 207.148.90.45 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- ip: 207.148.103.42 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- hash_md5: 4f1c68d2fe3b0255e706e4c7de0a739f ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- hash_md5: 213f4f64aa92b5cc06c2f38bd28f0d6c ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- hash_sha256: 93af6afb47f4c42bc0da3eedc6ecb9054134f4a47ef0add0d285404984011072 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- hash_sha256: 4f932d6e21fdd0072aba61203c7319693e490adbd9e93a49b0fe870d4d0aed71 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- hash_sha1: ca38f3f51a6739d9606dee27849a31775eb1d871 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- hash_sha1: d0a4d4f1bd228ce845817b17aa1989d9fee9d216 ([link](https://www.rewterz.com/threat-advisory/apt10-uses-noopdoor-and-lodeinfo-malware-to-attack-japanese-companies-active-iocs)) 

- For more IoCs, please refer to the above links. 


