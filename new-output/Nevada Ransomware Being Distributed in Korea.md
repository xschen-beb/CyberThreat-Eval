Source: [https://asec.ahnlab.com/en/50063/](https://asec.ahnlab.com/en/50063/)

# Nevada Ransomware Being Distributed in Korea

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Nevada Ransomware Being Distributed in Korea 

 Root cause: The primary vector of the ransomware's distribution is not explicitly mentioned, but common vectors include phishing emails, malicious downloads, or exploiting vulnerabilities in systems. *Support for command-line options enables various encryption methods* (https://asec.ahnlab.com/jp/50048/). 

 Threat Actor/group/campaign: Not explicitly mentioned, but associated with the Nevada ransomware group and affiliates from the RAMP underground community *affiliates from RAMP underground community* (https://www.resecurity.com/blog/article/nevada-ransomware-waiting-for-the-next-dark-web-jackpot). 

 Organization/industry/location: General targets in Korea. 

 Start date – End date: The blog mentions the ransomware being detected on March 16, 2023, *and March 22, 2023* (https://asec.ahnlab.com/jp/50048/). *Updates on January 20th and February 2nd, 2023* (https://www.resecurity.com/blog/article/nevada-ransomware-waiting-for-the-next-dark-web-jackpot). No end date provided. 

 MITRE TTPs: ['T1490: Inhibit System Recovery (Volume Shadow Deletion)', 'T1021.002: Remote Desktop Protocol (RDP) (Encrypt Shared Network Folders)', 'T1083: File and Directory Discovery (Encryption of specific files and directories)', 'T1070.004: File Deletion (Self-deletion)'] 

 Impact: Not explicitly mentioned, but ransomware typically leads to significant data loss and potential financial losses due to ransom payments, operational disruptions, and recovery costs. 

 Mitigation: ['Secure Backups: Regularly back up data and ensure that backups are not connected to the network.', 'Endpoint Protection: Use advanced anti-malware solutions with real-time protection.', 'Security Awareness Training: Educate employees about phishing and safe internet practices.', 'Patch Management: Regularly update and patch systems to protect against vulnerabilities.', 'Network Segmentation: Implement network segmentation to limit the spread of ransomware.', 'Disable Macros: Disable macros in Office files from unknown sources.', 'Email Filtering: Use email filtering to block malicious attachments and links.', 'Least Privilege Principle: Apply the principle of least privilege to limit user access rights.', 'Firewall and IDS/IPS: Implement robust firewall and intrusion detection/prevention systems.'] 

 Detailed Steps for mitigation: ['Backup Strategy: Implement a 3-2-1 backup strategy (three copies of your data, two on different media, one off-site).', 'Anti-malware: Deploy and regularly update endpoint protection solutions like V3.', 'Patching: Automate patch management to ensure all software is up-to-date.', 'Training: Conduct regular security training sessions for employees.', 'Macros: Disable Office macros by default and only allow them for trusted documents.', 'Email Security: Use advanced email security solutions to filter out malicious emails.', 'Access Controls: Regularly review and adjust user permissions to ensure minimal access.'] 

 Detection Signature: {'Service': 'N/A (specific service not mentioned)', 'Port': 'N/A (specific port not mentioned)', 'Severity': 'Critical', 'Incident': 'Nevada Ransomware', 'Signature name': 'Nevada Ransomware behavior detection', 'Internal checks': ['Setting1: Monitor for creation of ransom notes with filenames like “README.txt”', 'Setting2: Detect file extensions being renamed to “.NEVADA”', 'Setting3: Monitor for unusual process behavior, such as self-deletion commands.'], 'External scanning': ['Monitor for command and control (C2) traffic', 'Scan for unusual network encryption activity']} 

 IoCs: ['MD5: b673d92b77489d12779dc1fb5e8f6fdd', 'Other detection signatures mentioned: File Detection: Ransomware/Win.Nevada.C5391542 (2023.03.06.03), Behavior Detection: Ransom/MDP.Decoy.M1171, Ransom/MDP.Event.M1785'] 

 Additional Information: ['*Rust-based malicious code* (https://asec.ahnlab.com/ko/49080/)', '*Tor Browser for payments* (https://asec.ahnlab.com/ko/49080/)', '*Self-deletion command* (https://asec.ahnlab.com/ko/49080/)', '*CIS country exclusions* (https://asec.ahnlab.com/ko/49080/)', '*Hidden drive encryption* (https://asec.ahnlab.com/jp/50048/)', '*Network shared folder encryption* (https://asec.ahnlab.com/jp/50048/)', '*Salsa20 encryption algorithm* (https://www.resecurity.com/blog/article/nevada-ransomware-waiting-for-the-next-dark-web-jackpot)'] 


# Related articles (describing the same threat) 
['https://asec.ahnlab.com/en/50063/', 'https://asec.ahnlab.com/ko/49080/', 'https://asec.ahnlab.com/jp/50048/', 'https://www.resecurity.com/blog/article/nevada-ransomware-waiting-for-the-next-dark-web-jackpot']
