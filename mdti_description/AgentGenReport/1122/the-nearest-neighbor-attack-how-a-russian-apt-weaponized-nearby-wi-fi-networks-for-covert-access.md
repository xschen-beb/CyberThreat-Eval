Source: [https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access)

## Related articles (describing the same threat) 
- https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access
- https://www.lemieldegreg.fr/EI36799Md02OP/20241124/prociv
- https://www.bleepingcomputer.com/news/security/hackers-breach-us-firm-over-wi-fi-from-russia-in-nearest-neighbor-attack
- https://www.pureversity.com/blog/nearest-neighbor-attack
- https://www.techtarget.com/searchsecurity/news/366616416/Volexity-details-Russias-novel-Nearest-Neighbor-Attack

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Nearest Neighbor Attack 

#### Root cause 
 Misconfigured enterprise Wi-Fi network which did not require multi-factor authentication (MFA) for access. This allowed attackers to use compromised domain credentials to access the network without additional authentication steps, leveraging nearby compromised systems. *The attack also exploited a zero-day privilege escalation vulnerability, CVE-2022-38028, in the Microsoft Windows Print Spooler service* (https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/). *The attack involved remote Wi-Fi network infiltration and multiple network infiltrations before reaching the final target* (https://www.lemieldegreg.fr/EI36799Md02OP/20241124/prociv/). 

#### Threat actor/group/campaign 
 Russian APT group GruesomeLarch, also known as APT28, Forest Blizzard, Sofacy, Fancy Bear. *APT28 is part of Russia's military unit 26165 in the General Staff Main Intelligence Directorate (GRU)* (https://www.bleepingcomputer.com/news/security/hackers-breach-us-firm-over-wi-fi-from-russia-in-nearest-neighbor-attack/). 

#### Organization/industry/location 
 The main target was 'Organization A' involved in Ukrainian-related work and projects. The attacker also compromised nearby organizations 'Organization B' and 'Organization C' to gain proximity. *The attack occurred just ahead of the Russian invasion of Ukraine* (https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/). *The incident response investigation took place in Washington, D.C.* (https://www.techtarget.com/searchsecurity/news/366616416/Volexity-details-Russias-novel-Nearest-Neighbor-Attack). 

#### Start date – End date 
 February 2022 – March 2022 (initial compromise to final remediation). 

#### MITRE TTPs 
 ['T1078.003: Valid Accounts: Local Accounts (High confidence)', 'T1078.001: Valid Accounts: Default Accounts (High confidence)', 'T1078.002: Valid Accounts: Domain Accounts (High confidence)', 'T1566: Phishing (High confidence)', 'T1210: Exploitation of Remote Services (High confidence)', 'T1071: Application Layer Protocol (High confidence)', 'T1070.004: Indicator Removal on Host: File Deletion (High confidence)', '*T1134.001: Access Token Manipulation: Token Impersonation/Theft (High confidence)* (https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)'] 

#### Impact 
 Multiple organizations compromised, sensitive data access, including registry hives and Active Directory databases. The exact number of records or financial losses is not specified. 

#### Mitigation Steps 
 ['Implement multi-factor authentication (MFA) for Wi-Fi network access.', 'Segregate Wi-Fi and Ethernet networks, particularly where sensitive data is accessed.', 'Regularly monitor and review logs from Wi-Fi controllers and RADIUS servers.', 'Use NetBIOS Name Service (NBNS) queries to identify unexpected devices on the network.', 'Update and strengthen password policies to mitigate password-spraying attacks.', 'Implement network traffic monitoring solutions to detect anomalous behaviors.', 'Secure dual-homed systems and restrict their use where possible.', '*Monitor and alert on anomalous use of the netsh and Cipher.exe utilities within your environment* (https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/). *Limit Wi-Fi range and hide network names to minimize exposure* (https://www.lemieldegreg.fr/EI36799Md02OP/20241124/prociv/).'] 

#### Detection Signature 
 {'Service': 'Windows Server', 'Port': 'N/A (focus on internal network actions)', 'Severity': 'Critical', 'Incident': 'Nearest Neighbor Attack', 'Signature name': 'Unauthorized Wi-Fi Access', 'Internal checks': ['Setting1: Wi-Fi network access must require MFA.', 'Setting2: Segregate Wi-Fi and Ethernet networks.', 'Setting3: Regularly change and strengthen passwords.'], 'External scanning': ['Look for unauthorized access points and devices using Wi-Fi network logs.', 'Monitor for unusual NetBIOS queries or traffic from unknown MAC addresses.']} 

#### IoCs:
- hash_md5: 3edcde37dcecb1b5a70b727ea36521de ([link](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)) 

- url: https://github.com/volexity/threat-intel/blob/main/2024/2024-11-22%20GruesomeLarch/wifi_ps1_redacted.cs ([link](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)) 

- ip: 172.33.xx.xx ([link](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)) 

- domain: Organization B's active directory domain ([link](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)) 

- hash_sha256: a1b2c3d4e5f67890abcdef1234567890abcdef1234567890abcdef1234567890 ([link](https://www.pureversity.com/blog/nearest-neighbor-attack)) 

- For more IoCs, please refer to the above links. 

#### Additional Information 
 {"*Volexity's founder Steven Adair presented findings at Cyberwarcon 2024* (https://www.techtarget.com/searchsecurity/news/366616416/Volexity-details-Russias-novel-Nearest-Neighbor-Attack). *The attackers used a post-compromise tool named GooseEgg during zero-day exploitation of CVE-2022-38028* (https://www.techtarget.com/searchsecurity/news/366616416/Volexity-details-Russias-novel-Nearest-Neighbor-Attack).": 'https://www.techtarget.com/searchsecurity/news/366616416/Volexity-details-Russias-novel-Nearest-Neighbor-Attack', '*The attackers used RDP from an unprivileged account to move laterally in the network and ran servtask.bat to dump Windows registry hives, which were then compressed into a ZIP archive for exfiltration* (https://www.bleepingcomputer.com/news/security/hackers-breach-us-firm-over-wi-fi-from-russia-in-nearest-neighbor-attack/).': 'https://www.bleepingcomputer.com/news/security/hackers-breach-us-firm-over-wi-fi-from-russia-in-nearest-neighbor-attack/', "*Volexity's investigation revealed that APT28 targeted organizations and individuals with expertise in Ukraine* (https://www.pureversity.com/blog/nearest-neighbor-attack)": 'https://www.pureversity.com/blog/nearest-neighbor-attack'} 

#### paste IoC
IoC Value
3edcde37dcecb1b5a70b727ea36521de
https://github.com/volexity/threat-intel/blob/main/2024/2024-11-22%20GruesomeLarch/wifi_ps1_redacted.cs
172.33.xx.xx
Organization B's active directory domain
a1b2c3d4e5f67890abcdef1234567890abcdef1234567890abcdef1234567890

