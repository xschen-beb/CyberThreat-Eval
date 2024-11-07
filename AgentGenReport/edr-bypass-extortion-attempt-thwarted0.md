Source: [https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted)

## Related articles (describing the same threat) 
- https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted
- https://unit42.paloaltonetworks.com/feed/
- https://webboard-nsoc.ncsa.or.th/topic/1407/cyber-threat-intelligence-04-november-2024/1
- https://www.ic3.gov/CSA/2024/240807.pdf

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: TA Phone Home: EDR Evasion Testing Reveals Extortion Actor's Toolkit 

#### Root cause 
 Misuse of Atera RMM for initial access and unprotected virtual environment allowing threat actor activities. 

#### Threat actor/group/campaign 
 Likely individual(s) associated with the username 'Marti71' on cybercrime forums and potentially linked to the actor using the moniker 'KernelMode'. *Additionally, possible collaboration with North Korean actors Jumpy Pisces and Play ransomware* (https://unit42.paloaltonetworks.com/north-korean-threat-group-play-ransomware/). 

#### Organization/industry/location 
 Not specified, but the victim organization had an incident involving EDR evasion attempts. 

#### Start date – End date 
 Not specified 

#### MITRE TTPs 
 ['Initial access (TA0001): Access via Atera RMM', 'Persistence (TA0003): Creation of scheduled tasks for Cobalt Strike beacons', "Defense Evasion (TA0005): Use of AV/EDR bypass tool 'disabler.exe'", 'Credential Access (TA0006): Use of Mimikatz and PowerShell for credential dumping', 'Discovery (TA0007): Use of internal discovery commands', 'Lateral Movement (TA0008): Use of Windows RDP and PsExec', 'Exfiltration (TA0010): Data exfiltration using Rclone', 'Command and Control (TA0011): Cobalt Strike beacon activity', '*Data Exfiltration (TA0010): Use of PondRAT and POOLRAT* (https://unit42.paloaltonetworks.com/gleaming-pisces-applejeus-poolrat-and-pondrat/)'] 

#### Impact 
 Specific impact details not disclosed, potential exposure of sensitive data and unauthorized access to client networks. *Additionally, the incident involved the exploitation of CVE-2024-10443, CVE-2024-9379, and CVE-2024-6781, increasing the impact scope* (https://webboard-nsoc.ncsa.or.th/topic/1407/cyber-threat-intelligence-04-november-2024/1) (https://www.ic3.gov/CSA/2024/240807.pdf). 

#### Mitigation Steps 
 ['Secure remote access tools like Atera RMM with multi-factor authentication and monitor their usage.', 'Regularly update and patch endpoint protection tools.', 'Implement strict access controls and monitor for unauthorized access or unusual activity on systems.', 'Use advanced endpoint detection and response solutions like Cortex XDR to detect and prevent unauthorized activities.', 'Review and secure shared drives and virtual environments.', 'Enable agent tampering protection on security tools to prevent bypass attempts.', '*Detect and mitigate DNS hijacking attempts through machine learning analysis of DNS records* (https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)', '*Patch Synology NAS appliances to address zero-day vulnerabilities CVE-2024-10443 and RISK:STATION* (https://www.bleepingcomputer.com/news/security/synology-fixed-two-critical-zero-days-exploited-at-pwn2own-within-days/)'] 

#### Detection Signature 
 {'Service': 'Atera RMM', 'Port': 'Not specified', 'Severity': 'Critical', 'Incident': 'Unauthorized use of remote access tools', 'Signature name': 'Atera RMM unauthorized access', 'Internal checks': ['Ensure Atera RMM usage is monitored and MFA is enabled.', 'Verify that Atera RMM is only used by authorized personnel.', 'Monitor for unauthorized installation of Atera RMM agents.'], 'External scanning': ['Check for unauthorized Atera RMM connections.', 'Monitor network traffic for unusual patterns indicating remote access tool misuse.', '*Scan for DNS hijacking and domain shadowing activities* (https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)', '*Monitor for signs of CVE-2024-9379 exploitation attempts* (https://blog.sonicwall.com/en-us/2024/11/cve-2024-9379-ivanti-cloud-service-appliance-authenticated-sql-injection/)']} 

#### IoCs: 
- hash_sha256: 3758c5eb1fbab2362ef23091f082710606c1b4ebaeaff9b514896dc2a1e2ab17 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 1228fd70d7ce0f31f7e7c98520e66a01935e428be561ce0d25140ba33598f688 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 6106d1ce671b92d522144fcd3bc01276a975fe5d5b0fde09ca1cca16d09b7143 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 14364f1969b83cf4ec2c0e293c6b4d8f750932f6cbf9a8f32173400de33469fd ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 264a29a703682456ebe9f679a0e7d18291af84ef4b53a669c2555061e4972394 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 61c0810a23580cf492a6ba4f7654566108331e7a4134c968c2d6a05261b2d8a1 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 8d36705a5b7f6179fdef2d600276f9c0cc6cb3b0a670c11d66baaaea6bd2c8ad ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 41f32a3d67b3f983c82070e067a121dd5b8fae2804c97e684acc7f599ba308da ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 6e37a054bd7c49b233cace747951911f320bd43be8a79ce455b97403c2f7de2c ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: aa97acd5628c1f7a16cb98e7b9ce7228119759133f1649b1d5ed849a1a98448b ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 97f2676c6d1e16264584ce4c1f1e8790598ba2a85ae08e3d6e394669240b9908 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 0112e3b20872760dda5f658f6b546c85f126e803e27f0577b294f335ffa5a298 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 7c8559134a49c8d8739b66a549f10b22d4fd16afaff51976562f995b2bcd01a9 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 22f52c9e66330642e836aaf1b6573dd7452e76e0f0b5e6ac594a0278689e1d8f ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 49d01f2e32808e24dc8129d3c1ebe444f71792ddec2efabee354335fc6d6f64c ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 71dfb3f52df040644221f8c59215f83eb516186b6f82dbbb2c16bf3c22e4baf6 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: d0c1662ce239e4d288048c0e3324ec52962f6ddda77da0cb7af9c1d9c2f1e2eb ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 8b9c7d2554fe315199fae656448dc193accbec162d4afff3f204ce2346507a8a ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: f1c45cbbd98619e197154085a05fd972283af6788343aa04492e35798a06e2b7 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- ip: 94.75.225.81 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- ip: 82.192.88.95 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- ip: 89.251.22.32 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- ip: 180.131.145.85 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- ip: 45.67.34.123 ([link](https://www.ic3.gov/CSA/2024/240807.pdf)) 

- domain: beamofthemoon.com ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- domain: mail.beamofthemoon.com ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- domain: store.beamofthemoon.com ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- cve: CVE-2024-10443 ([link](https://webboard-nsoc.ncsa.or.th/topic/1407/cyber-threat-intelligence-04-november-2024/1)) 

- cve: CVE-2024-9379 ([link](https://blog.sonicwall.com/en-us/2024/11/cve-2024-9379-ivanti-cloud-service-appliance-authenticated-sql-injection/)) 

- cve: CVE-2024-6781 ([link](https://www.ic3.gov/CSA/2024/240807.pdf)) 


