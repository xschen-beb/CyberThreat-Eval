# Asylum Ambuscade A Cybercrime Group with Espionage Ambitions

Incident: Asylum Ambuscade: Cybercrime and Cyberespionage Operations

Root cause: Use of spearphishing emails with malicious Excel attachments and exploitation of the Follina vulnerability (CVE-2022-30190).

Impact: Over 4,500 victims worldwide, including individuals, cryptocurrency traders, and small and medium businesses (SMBs) in various regions. The financial losses are not explicitly detailed but could include stolen cryptocurrency, unauthorized access to SMB systems, and potential resale of access to other crimeware groups.

Mitigation: 
- Implement robust email filtering to detect and block spearphishing attempts.
- Regularly update and patch systems to mitigate known vulnerabilities like Follina (CVE-2022-30190).
- Deploy endpoint protection to detect and respond to malicious scripts and downloaders.
- Educate employees and users about the risks of spearphishing and how to recognize malicious documents.
- Use network traffic analysis to identify and block communication with known command and control (C&C) servers.
  
Detailed Steps for Mitigation:
1. **Email Filtering and Security Awareness:**
    - Deploy advanced email filtering solutions to detect and quarantine suspicious emails.
    - Conduct regular security awareness training for employees to recognize phishing attempts.
2. **Patch Management:**
    - Ensure all software and systems are up to date with the latest security patches, focusing on vulnerabilities like CVE-2022-30190.
3. **Endpoint Protection:**
    - Install and configure endpoint protection solutions to detect and block malicious scripts and downloaders.
    - Use behavior-based detection to identify unusual activities on endpoints.
4. **Network Monitoring:**
    - Implement network traffic monitoring to detect and block communications with known malicious IP addresses and domains.
    - Use intrusion detection systems (IDS) and intrusion prevention systems (IPS) to analyze network traffic for signs of compromise.
5. **Incident Response Plan:**
    - Develop and regularly update an incident response plan to quickly address detected threats.
    - Conduct regular drills and simulations to ensure readiness in case of an actual attack.

Detection Signature:
    Service: HTTP (C&C communication)
    Port: 80
    Severity: Critical
    Incident: Asylum Ambuscade Cybercrime and Cyberespionage
    Signature name: “HTTP C&C Communication”

    Internal checks:
        - Setting1: Monitor HTTP traffic for connections to known malicious IPs and domains – In network monitoring systems
        - Setting2: Check for execution of unusual script files (e.g., AutoHotkey, Lua, JavaScript) – Inside VMs
        - Setting3: Verify system configurations to ensure patches for known vulnerabilities like Follina are applied – Inside VMs

    External scanning:
        - Port (80) open
        - HTTP traffic to known malicious IPs and domains

IoCs found:
- IP Addresses:
    - 5.39.222[.]150
    - 5.44.42[.]27
    - 5.230.68[.]137
    - 5.230.71[.]166
    - 5.230.72[.]38
    - 5.230.72[.]148
    - 5.230.73[.]57
    - 5.230.73[.]63
    - 5.230.73[.]241
    - 5.230.73[.]247
    - 5.230.73[.]248
    - 5.230.73[.]250
    - 5.252.118[.]132
    - 5.252.118[.]204
    - 5.255.88[.]222
    - 23.106.123[.]119
    - 31.192.105[.]28
    - 45.76.211[.]131
    - 45.77.185[.]151
    - 45.132.1[.]238
    - 45.147.229[.]20
    - 46.17.98[.]190
    - 46.151.24[.]197
    - 46.151.24[.]226
    - 46.151.25[.]15
    - 46.151.25[.]49
    - 46.151.28[.]18
    - 51.83.182[.]153
    - 51.83.189[.]185
    - 62.84.99[.]195
    - 62.204.41[.]171
    - 77.83.197[.]138
    - 79.137.196[.]121
    - 79.137.197[.]187
    - 80.66.88[.]155
    - 84.32.188[.]29
    - 84.32.188[.]96
    - 85.192.49[.]106
    - 85.192.63[.]13
    - 85.192.63[.]126
    - 85.239.60[.]40
    - 88.210.10[.]62
    - 89.41.182[.]94
    - 89.107.10[.]7
    - 89.208.105[.]255
    - 91.245.253[.]112
    - 94.103.83[.]46
    - 94.140.114[.]133
    - 94.140.114[.]230
    - 94.140.115[.]44
    - 94.232.41[.]96
    - 94.232.41[.]108
    - 94.232.43[.]214
    - 98.142.251[.]26
    - 98.142.251[.]226
    - 104.234.118[.]163
    - 104.248.149[.]122
    - 109.107.173[.]72
    - 116.203.252[.]67
    - 128.199.82[.]141
    - 139.162.116[.]148
    - 141.105.64[.]121
    - 146.0.77[.]15
    - 146.70.79[.]117
    - 157.254.194[.]225
    - 157.254.194[.]238
    - 172.64.80[.]1
    - 172.86.75[.]49
    - 172.104.94[.]104
    - 172.105.235[.]94
    - 172.105.253[.]139
    - 176.124.214[.]229
    - 176.124.217[.]20
    - 185.70.184[.]44
    - 185.82.126[.]133
    - 185.123.53[.]49
    - 185.150.117[.]122
    - 185.163.45[.]221
    - 193.109.69[.]52
    - 193.142.59[.]152
    - 193.142.59[.]169
    - 194.180.174[.]51
    - 195.2.81[.]70
    - 195.133.196[.]230
    - 212.113.106[.]27
    - 212.113.116[.]147
    - 212.118.43[.]231
    - 213.109.192[.]230

- Domains:
    - snowzet[.]com
    - namesilo.my[.]id

Files (SHA-1):
    - 2B42FD41A1C8AC12221857DD2DF93164A71B95D7
    - D5F8ACAD643EE8E1D33D184DAEA0C8EA8E7FD6F8
    - 57157C5D3C1BB3EB3E86B24B1F4240C867A5E94F
    - 7DB446B95D5198330B2B25E4BA6429C57942CFC9
    - 5F67279C195F5E8A35A24CBEA76E25BAD6AB6E8E
    - C98061592DE61E34DA280AB179465580947890DE
    - 519E388182DE055902C656B2D95CCF265A96CEAB
    - AC3AFD14AD1AEA9E77A84C84022B4022DF1FC88B
    - 64F5AC9F0C6C12F2A48A1CB941847B0662734FBF
    - 557C5150A44F607EC4E7F4D0C0ED8EE6E9D12ADF
    - F85B82805C6204F34DB0858E2F04DA9F620A0277
    - 5492061DE582E71B2A5DA046536D4150F6F497F1
    - C554100C15ED3617EBFAAB00C983CED5FEC5DB11
    - AD8143DE4FC609608D8925478FD8EA3CD9A37C5D
    - F2948C27F044FC6FB4849332657801F78C0F7D5E
    - 7AA23E871E796F89C465537E6ECE962412CDA636
    - 384961E19624437EB4EB22B1BF45953D7147FB8F
    - 7FDB9A73B3F13DBD94D392132D896A5328DACA59
    - 3E38D54CC55A48A3377A7E6A0800B09F2E281978
    - 7F8742778FC848A6FBCFFEC9011B477402544171
    - 7A78AF75841C2A8D8A5929C214F08EB92739E9CB
    - 441369397D0F8DB755282739A05CB4CF52113C40
    - 117ECFA95BE19D5CF135A27AED786C98EC8CE50B
    - D24A9C8A57C08D668F7D4A5B96FB7B5BA89D74C3
    - 95EDC096000C5B8DA7C8F93867F736928EA32575
    - 62FA77DAEF21772D599F2DC17DBBA0906B51F2D9
    - A9E3ACFE029E3A80372C0BB6B7C500531D09EDBE
    - EE1CFEDD75CBA9028904C759740725E855AA46B5
    - 29604997030752919EA42B6D6CEE8D3AE28F527E
