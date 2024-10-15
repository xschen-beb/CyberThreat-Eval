Source: [https://www.malwarebytes.com/blog/threat-intelligence/2023/01/new-data-wipers-deployed-by-sandworm-group-against-ukraine](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/new-data-wipers-deployed-by-sandworm-group-against-ukraine)

# New Data Wipers Deployed Against Ukraine

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: New Data Wipers Deployed Against Ukraine 

 Root cause: The root cause includes multiple instances of destructive malware (wipers) deployed against the systems. Attackers gained initial access and deployed wipers, bypassing security mechanisms and leveraging elevated privileges. The malware types involved include CaddyWiper, ZeroWipe, SDelete, AwfulShred, BidSwipe, WhisperGate, HermeticWiper, IsaacWiper, and DesertBlade, each targeting different operating systems (Windows, Linux, FreeBSD). *Additionally, a new wiper named SwiftSlicer was used, deleting shadow copies and overwriting files using 4096-byte blocks* (https://www.darkreading.com/cyberattacks-data-breaches/russia-sandworm-apt-swarm-wiper-attacks-ukraine). 

 Threat Actor/group/campaign: Sandworm (UAC-0082), a Russian state-sponsored group linked to *GRU* (https://www.darkreading.com/cyberattacks-data-breaches/russia-sandworm-apt-swarm-wiper-attacks-ukraine). 

 Organization/industry/location: Ukrinform, Ukraine’s national news agency. 

 Start date – End date: Initial access was established on December 7, 2022, and the attack culminated on January 17, 2023. 

 MITRE TTPs: ['T1071.001: Application Layer Protocol: Web Protocols', 'T1078: Valid Accounts', 'T1059.001: Command and Scripting Interpreter: PowerShell', 'T1070.004: Indicator Removal on Host: File Deletion', 'T1107: File Deletion', 'T1490: Inhibit System Recovery'] 

 Impact: The attack affected the integrity and availability of Ukrinform's data, causing significant operational disruption. Although the exact number of records or financial losses is not detailed in the document, the deployment of multiple wipers indicates a severe impact on systems and data. *CERT-UA reported the attack was only partially successful* (https://www.darkreading.com/cyberattacks-data-breaches/russia-sandworm-apt-swarm-wiper-attacks-ukraine). 

 Mitigation: ['**Secure Systems and Networks**: Implement comprehensive endpoint protection and intrusion detection systems (IDS) to monitor and alert on anomalous activities.', '**Patch Management**: Ensure all systems are up to date with the latest security patches to mitigate vulnerabilities.', '**Access Control**: Enforce stringent access control policies, including multi-factor authentication (MFA) and least privilege principles.', '**Regular Backups**: Maintain regular backups and ensure they are stored securely offline to prevent tampering.', '**Network Segmentation**: Segment networks to limit the spread of malware and isolate critical systems.', '**Incident Response Plan**: Develop and regularly update an incident response plan to quickly contain and mitigate the effects of an attack.', '**User Training**: Conduct regular security awareness training for employees to recognize phishing attempts and other social engineering tactics.'] 

 Detection Signature: {'Service': 'Windows OS, Linux, FreeBSD', 'Port': 'Not specified (varies based on specific malware and attack vector)', 'Severity': 'Critical', 'Incident': 'Destructive Malware Deployment', 'Signature name': '“Data Wiper Deployment”', 'Internal checks': {'Setting1': 'Monitor for unauthorized access attempts and privilege escalations.', 'Setting2': 'Validate integrity of critical system files and configurations.', 'Setting3': 'Check for unusual file deletions and modifications, especially in system directories.'}, 'External scanning': {'Setting1': 'Monitor for access from known malicious IP addresses.', 'Setting2': 'Scan for indicators of compromise related to the specific wiper malware variants.'}} 

 IoCs: No IoCs found in the document. For detailed IoCs, refer to the CERT-UA article linked in the blog. 

 Note: Always stay updated with threat intelligence sources and continuously adapt security measures to address emerging threats. 


# Related articles (describing the same threat) 
['https://www.malwarebytes.com/blog/threat-intelligence/2023/01/new-data-wipers-deployed-by-sandworm-group-against-ukraine', 'https://www.darkreading.com/cyberattacks-data-breaches/russia-sandworm-apt-swarm-wiper-attacks-ukraine', 'https://www.welivesecurity.com/2023/02/24/year-wiper-attacks-ukraine/']
