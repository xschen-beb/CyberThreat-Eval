Source: [https://asec.ahnlab.com/en/62144/](https://asec.ahnlab.com/en/62144/)

# Analysis of Nood RAT Used in Attacks Against Linux (Gh0st RATs Variant)

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Noodle RAT Used in Attacks Against Linux (Gh0st RAT’s Variant) 

 Root cause: Exploitation of vulnerabilities in software such as WebLogic (CVE-2017-10271), weak configuration practices, and possibly insecure AWS server setups. 

 Threat Actor/group/campaign: Likely Chinese-speaking threat actors, potentially including the Rocke group and participants in the Cloud Snooper APT campaign. *Trend Micro identified this as a new malware strain* (https://www.infosecurity-magazine.com/news/chinese-noodle-rat-backdoor/). 

 Organization/industry/location: Multiple organizations across various countries including China, Russia, Hong Kong, Philippines, Vietnam, South Korea, *Thailand, India, Japan, Malaysia, and Taiwan* (https://www.infosecurity-magazine.com/news/chinese-noodle-rat-backdoor/). 

 Start date – End date: Ongoing since at least 2018. 

 MITRE TTPs: ['T1219 (Remote Access Tools)', 'T1071.001 (Application Layer Protocol: Web Protocols)', 'T1105 (Ingress Tool Transfer)', 'T1078 (Valid Accounts)', 'T1070.004 (Indicator Removal on Host: File Deletion)'] 

 Impact: Multiple organizations impacted with varying degrees of data exfiltration and system compromise. Specific financial losses are not detailed. 

 Mitigation: Secure Linux systems by updating to the latest versions and patching known vulnerabilities, particularly WebLogic (CVE-2017-10271). Implement strong authentication mechanisms and access controls to prevent unauthorized access to systems. Monitor and restrict outbound traffic to detect and prevent communication with malicious C&C servers. Use security solutions that can detect and block Nood RAT and its variants (e.g., update antivirus signatures). Regularly review and audit system configurations and credentials to ensure they follow security best practices. 

 Detailed Steps for mitigation: ['Patch Management: Regularly apply security patches for all software and systems. Specifically, address vulnerabilities like CVE-2017-10271 in WebLogic.', 'Access Controls: Implement multi-factor authentication (MFA) on all critical systems. Limit the use of administrative privileges and ensure accounts are configured with the least privilege principle.', 'Network Security: Configure firewalls to block known malicious IP addresses and domains listed in IoCs. Monitor network traffic for unusual activity, such as communication with C&C servers.', 'Endpoint Protection: Deploy and regularly update endpoint security solutions capable of detecting Nood RAT. Utilize behavioral analysis tools to identify and mitigate suspicious activities.', 'Incident Response: Develop and test an incident response plan to quickly address and mitigate infections. Train staff to recognize and respond to indicators of compromise.', 'Backup and Recovery: Maintain regular backups of critical data and ensure that backups are stored securely and tested for integrity.'] 

 Detection Signature: {'Service': 'MySQL, MS-SQL', 'Port': '3306, 1433', 'Severity': 'Critical', 'Incident': 'Nood RAT infection', 'Signature name': 'Nood RAT C2 Communication', 'Internal checks': ['Setting1: Ensure MySQL and MS-SQL servers are not exposed to the external Internet.', 'Setting2: Implement strict firewall rules to restrict access to MySQL (3306) and MS-SQL (1433) ports.', 'Setting3: Secure MySQL and MS-SQL with strong authentication credentials and regular audits.'], 'External scanning': ['Port (3306, 1433) open', 'Unusual outbound traffic to known malicious IPs/domains.']} 

 IoCs: {'MD5': ['035f83018cf96f5e1f6817ccd39fc0b6', '0a35e06f53c17ab1c8e18e7e0c0821d8', '35743db3dc333245ef5b69100721ced9', '4f3afdcfff8f7994b7d3d3fbaa6858b4', '75838e5d481da40db2e235a6d5a222ef'], 'URL': ['http[:]//1[.]117[.]165[.]141[:]53/', 'http[:]//101[.]42[.]139[.]110[:]53/', 'http[:]//101[.]42[.]139[.]110[:]8443/', 'http[:]//23[.]100[.]88[.]61[:]53/', 'http[:]//42[.]51[.]40[.]184[:]56/']} 

 Additional Information: Noodle RAT exists in two versions: *Win.NOODLERAT and Linux.NOODLERAT* (https://www.infosecurity-magazine.com/news/chinese-noodle-rat-backdoor/). The malware has been misclassified for years but was identified by *Trend Micro* (https://www.infosecurity-magazine.com/news/chinese-noodle-rat-backdoor/). *Virus Total uploads in 2024 confirm its active use* (https://www.infosecurity-magazine.com/news/chinese-noodle-rat-backdoor/). 


# Related articles (describing the same threat) 
['https://asec.ahnlab.com/en/62144/', 'https://www.infosecurity-magazine.com/news/chinese-noodle-rat-backdoor/']
