Source: [https://www.sentinelone.com/blog/from-conti-to-akira-decoding-the-latest-linux-esxi-ransomware-families/](https://www.sentinelone.com/blog/from-conti-to-akira-decoding-the-latest-linux-esxi-ransomware-families/)

# From Conti to Akira  Decoding the Latest Linux & ESXi Ransomware Families

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Not specified in the document 

 Root cause: The root causes behind the incidents involving the ransomware families discussed (MONTI, Akira, Trigona, Abyss Locker) include: 

 - Exploitation of vulnerabilities in ESXi servers, *phishing and social engineering* (https://www.bdrsuite.com/blog/monti-ransomware-returns-how-to-protect-your-linux-machines/).: Various ransomware operators leveraging the codebases of Conti, Babuk, LockBit, HelloKitty, Vice Society, and others 

 Organization/industry/location: Targets include educational institutions, financial, manufacturing, real estate, and medical industries, as well as businesses using VMware ESXi environments, *legal and government sectors* (https://www.bdrsuite.com/blog/monti-ransomware-returns-how-to-protect-your-linux-machines/). 

 Start date – End date: Specific dates for each ransomware family are not provided, but they have been active from mid-2022 to the present 

 MITRE TTPs: ['T1078: Valid Accounts', 'T1134: Access Token Manipulation', 'T1486: Data Encrypted for Impact', 'T1490: Inhibit System Recovery', 'T1021: Remote Services', 'T1048: Exfiltration Over Alternative Protocol', 'T1105: Ingress Tool Transfer'] 

 Impact: No specific number of records leaked or financial losses are mentioned. However, the ransomware attacks have significant impacts, including encryption of virtual machines and data, leading to potential business disruption and data loss. 

 Mitigation: ['Secure ESXi servers by patching known vulnerabilities.', 'Enforce strong authentication mechanisms, including multifactor authentication.', 'Regularly update software and firmware to mitigate known exploits.', 'Implement network segmentation to limit access to critical systems.', 'Use robust endpoint protection solutions to detect and prevent ransomware activities.', 'Ensure regular data backups and practice disaster recovery plans.'] 

 Detection Signature: {'Service': 'VMware ESXi', 'Port': '443 (default management port for ESXi)', 'Severity': 'Critical', 'Incident': 'Ransomware targeting ESXi environments', 'Signature name': '“ESXi Ransomware Activity”', 'Internal checks': ['Verify ESXi server software is up to date with patches applied.', 'Ensure strong authentication and access controls are in place for ESXi management interfaces.', 'Regularly review and audit access logs for suspicious activities.'], 'External scanning': ['Monitor for open management ports (e.g., 443) and unexpected network traffic patterns.', 'Use threat intelligence feeds to identify indicators of compromise (IoCs) related to ransomware activities.']} 

 IoCs: {'MONTI Locker': ['a0c9dd3f3e3d0e2cd5d1da06b3aac019cdbc74ef', 'f1c0054bc76e8753d4331a881cdf9156dd8b812a'], 'Akira': ['9180ea8ba0cdfe0a769089977ed8396a68761b40'], 'Trigona': ['0144800f67ef22f25f710d181954869f1d11d471', '55f47e767dd5fdd1a54a0b777b00ffb473acd329', '62e4537a0a56de7d4020829d6463aa0b28843022'], 'Abyss Locker': ['40ceb71d12954a5e986737831b70ac669e8b439e']} 


# Related articles (describing the same threat) 
['https://www.sentinelone.com/blog/from-conti-to-akira-decoding-the-latest-linux-esxi-ransomware-families/', 'https://www.bdrsuite.com/blog/monti-ransomware-returns-how-to-protect-your-linux-machines/']
