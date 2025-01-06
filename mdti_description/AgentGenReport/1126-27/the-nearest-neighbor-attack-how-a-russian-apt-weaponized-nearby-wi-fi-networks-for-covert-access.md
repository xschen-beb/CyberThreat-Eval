Source: [https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access)

## Related articles (describing the same threat) 
- https://www.microsoft.com/en-us/security/blog/2024/04/22/analyzing-forest-blizzards-custom-post-compromise-tool-for-exploiting-cve-2022-38028-to-obtain-credentials
- https://www.bleepingcomputer.com/news/security/hackers-breach-us-firm-over-wi-fi-from-russia-in-nearest-neighbor-attack
- https://www.scworld.com/brief/neighboring-wi-fi-networks-exploited-in-apt28-attack
- https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access
- https://www.darkreading.com/cyberattacks-data-breaches/fancy-bear-nearest-neighbor-attack-wi-fi

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident 
 The Nearest Neighbor Attack: How A Russian APT Weaponized Nearby Wi-Fi Networks for Covert Access 

#### Root cause 
 Misconfigured Wi-Fi networks lacking multi-factor authentication (MFA). The Wi-Fi networks only required valid domain usernames and passwords to authenticate, which facilitated the attack. Additionally, dual-homed systems that were connected to both wired and wireless networks provided a vulnerable point of entry. The attacker exploited a zero-day privilege escalation (CVE-2022-38028) to further gain access. Credential-stuffing attacks were used to compromise the Wi-Fi networks. *The attackers utilized password-spraying attacks targeting public-facing services and used dual-home devices to pivot to target networks. APT28 resorted to breaching other nearby entities before discovering a device within range of the original target* (https://www.scworld.com/brief/neighboring-wi-fi-networks-exploited-in-apt28-attack). 

#### Threat actor/group/campaign 
 Russian APT group GruesomeLarch (also known as APT28, Forest Blizzard, Sofacy, Fancy Bear). *APT28 is part of Russia's military unit 26165 in the General Staff Main Intelligence Directorate (GRU). Forest Blizzard used a custom tool called GooseEgg for post-compromise activities* (https://www.microsoft.com/en-us/security/blog/2024/04/22/analyzing-forest-blizzards-custom-post-compromise-tool-for-exploiting-cve-2022-38028-to-obtain-credentials/; https://www.bleepingcomputer.com/news/security/hackers-breach-us-firm-over-wi-fi-from-russia-in-nearest-neighbor-attack/). 

#### Organization/industry/location 
 The primary target was an organization with expertise on Ukraine, referred to as Organization A. The attack was notably just ahead of the Russian invasion of Ukraine. Other organizations in close physical proximity (referred to as Organization B and Organization C) were also compromised. The attack targeted a Washington, DC-based organization. The attack involved dual-homed systems and a custom PowerShell script. *Cybersecurity company Volexity detected the attack on February 4, 2022. Volexity analysis indicated attackers' exploitation of a remote desktop connection to facilitate lateral network movement and data exfiltration* (https://www.scworld.com/brief/neighboring-wi-fi-networks-exploited-in-apt28-attack; https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/; https://www.darkreading.com/cyberattacks-data-breaches/fancy-bear-nearest-neighbor-attack-wi-fi; https://www.bleepingcomputer.com/news/security/hackers-breach-us-firm-over-wi-fi-from-russia-in-nearest-neighbor-attack/). 

#### Start date � End date 
 The attack began in early February 2022 and continued for over a month, with the final observed activity occurring over a month after the initial breach. 

#### MITRE TTPs 
 {'T1078': 'Valid Accounts - The attacker used brute-force attacks to obtain valid credentials. (Confidence: High)', 'T1076': 'Remote Desktop Protocol - The attacker used RDP to access systems. (Confidence: High)', 'T1036': 'Masquerading - Use of living-off-the-land techniques to disguise malicious activities. (Confidence: High)', 'T1105': 'Ingress Tool Transfer - Files were transferred to and executed on compromised systems. (Confidence: High)', 'T1003': 'Credential Dumping - Registry hives were exported and compressed. (Confidence: High)', 'T1486': 'Data Encrypted for Impact - Files were deleted securely using Cipher.exe. (Confidence: High)', 'T1074': 'Data Staged - Data was staged for exfiltration. (Confidence: High)', 'T1068': 'Exploitation for Privilege Escalation - GooseEgg exploited Print Spooler vulnerabilities (CVE-2021-34527, CVE-2021-1675) (Confidence: High) (https://www.microsoft.com/en-us/security/blog/2024/04/22/analyzing-forest-blizzards-custom-post-compromise-tool-for-exploiting-cve-2022-38028-to-obtain-credentials/)'} 

#### Impact 
 Multiple organizations were breached, leading to unauthorized access to sensitive data related to Ukraine. The exact number of records leaked or the total financial loss is not specified. 

#### Mitigation Steps 
 {'1': 'Implement multi-factor authentication (MFA) for Wi-Fi networks.', '2': 'Secure Wi-Fi networks with certificate-based solutions.', '3': 'Separate networking environments for Wi-Fi and Ethernet-wired networks.', '4': 'Monitor and alert on the use of the netsh and Cipher.exe utilities.', '5': 'Create custom detection rules for files executing from non-standard locations.', '6': 'Monitor network traffic for unexpected files on webservers and large file transfers.', '7': 'Reset all potentially compromised credentials and enforce strong password policies.', '8': 'Apply security updates for Print Spooler vulnerabilities (CVE-2021-34527, CVE-2021-1675) (https://www.microsoft.com/en-us/security/blog/2024/04/22/analyzing-forest-blizzards-custom-post-compromise-tool-for-exploiting-cve-2022-38028-to-obtain-credentials/)'} 

#### Detection Signature 
 {'Service': 'Wi-Fi Network', 'Port': 'Not applicable (Wi-Fi network)', 'Severity': 'Critical', 'Incident': 'Nearest Neighbor Attack', 'Signature name': '�Unauthorized Wi-Fi Access�', 'Internal checks': {'Setting1': 'Wi-Fi networks should require MFA for authentication.', 'Setting2': 'Dual-homed systems should be identified and monitored for unusual activity.', 'Setting3': 'Implement and monitor logging for suspicious activities involving netsh and Cipher.exe.'}, 'External scanning': {'Detection of brute-force attacks on public-facing services.': 'Detection of brute-force attacks on public-facing services.', 'Monitoring for unauthorized Wi-Fi connections and rogue devices.': 'Monitoring for unauthorized Wi-Fi connections and rogue devices.'}} 

#### IoCs:
- hash_sha256: 7d51e5cc51c43da5deae5fbc2dce9b85c0656c465bb25ab6bd063a503c1806a9 ([link](https://www.microsoft.com/en-us/security/blog/2024/04/22/analyzing-forest-blizzards-custom-post-compromise-tool-for-exploiting-cve-2022-38028-to-obtain-credentials)) 

- hash_sha256: c60ead92cd376b689d1b4450f2578b36ea0bf64f3963cfa5546279fa4424c2a5 ([link](https://www.microsoft.com/en-us/security/blog/2024/04/22/analyzing-forest-blizzards-custom-post-compromise-tool-for-exploiting-cve-2022-38028-to-obtain-credentials)) 

- hash_sha256: 6b311c0a977d21e772ac4e99762234da852bbf84293386fbe78622a96c0b052f ([link](https://www.microsoft.com/en-us/security/blog/2024/04/22/analyzing-forest-blizzards-custom-post-compromise-tool-for-exploiting-cve-2022-38028-to-obtain-credentials)) 

- hash_sha256: 41a9784f8787ed86f1e5d20f9895059dac7a030d8d6e426b9ddcaf547c3393aa ([link](https://www.microsoft.com/en-us/security/blog/2024/04/22/analyzing-forest-blizzards-custom-post-compromise-tool-for-exploiting-cve-2022-38028-to-obtain-credentials)) 

- url: https://www.scworld.com/brief/neighboring-wi-fi-networks-exploited-in-apt28-attack ([link](https://www.scworld.com/brief/neighboring-wi-fi-networks-exploited-in-apt28-attack)) 
Not found for url https://www.scworld.com/brief/neighboring-wi-fi-networks-exploited-in-apt28-attack in VT. 

- ip: 172.33.xx.xx ([link](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access)) 
Not found for ip 172.33.xx.xx in VT. 

- ip: 172.20.xx.xx ([link](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access)) 
Not found for ip 172.20.xx.xx in VT. 

- domain: Organization A ([link](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access)) 
Not found for domain Organization A in VT. 

- domain: Organization B ([link](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access)) 
Not found for domain Organization B in VT. 

- domain: Organization C ([link](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access)) 
Not found for domain Organization C in VT. 

- url: https://github.com/volexity/threat-intel/blob/main/2024/2024-11-22%20GruesomeLarch/wifi_ps1_redacted.cs ([link](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access)) 
Not found for url https://github.com/volexity/threat-intel/blob/main/2024/2024-11-22%20GruesomeLarch/wifi_ps1_redacted.cs in VT. 

- url: https://www.darkreading.com/cyberattacks-data-breaches/fancy-bear-nearest-neighbor-attack-wi-fi ([link](https://www.darkreading.com/cyberattacks-data-breaches/fancy-bear-nearest-neighbor-attack-wi-fi)) 
Not found for url https://www.darkreading.com/cyberattacks-data-breaches/fancy-bear-nearest-neighbor-attack-wi-fi in VT. 

- For more IoCs, please refer to the above links. 

#### paste IoC
7d51e5cc51c43da5deae5fbc2dce9b85c0656c465bb25ab6bd063a503c1806a9
c60ead92cd376b689d1b4450f2578b36ea0bf64f3963cfa5546279fa4424c2a5
6b311c0a977d21e772ac4e99762234da852bbf84293386fbe78622a96c0b052f
41a9784f8787ed86f1e5d20f9895059dac7a030d8d6e426b9ddcaf547c3393aa

