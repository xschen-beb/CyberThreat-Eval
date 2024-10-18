Source: [https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)

# Ransomware Spotlight Play

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Play Ransomware Attacks 

 Root cause: The Play ransomware attacks primarily exploit vulnerabilities in public-facing applications and services, notably FortiOS SSL VPN (CVE-2018-13379, CVE-2020-12812), ProxyNotShell (CVE-2022-41040), OWASSRF (CVE-2022-41080), and MS Exchange Server Remote Code Execution (CVE-2022-41082). *Fortigate SSL-VPN vulnerabilities were notably exploited* (https://nologs-nobreach.com/2022/07/24/play-ransomware/). 

 Threat Actor/group/campaign: Play ransomware group 

 Organization/industry/location: Primary targets include organizations in telecommunications, healthcare, communication and media sectors, with significant activity in Germany, the United States, Portugal, *as well as North America and South America*, and *Argentina’s Judiciary of Cordoba and the German hotel chain H-Hotels* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a) *with Brazil as a primary target* (https://www.avertium.com/resources/threat-reports/an-in-depth-look-at-play-ransomware). 

 Start date – End date: June 2022 – May 2023 

 MITRE TTPs: - Initial Access: T1190 (Exploit Public-Facing Application)
- Execution: T1059 (Command and Scripting Interpreter), T1203 (Exploitation for Client Execution)
- Defense Evasion: T1562 (Impair Defenses), T1140 (Deobfuscate/Decode Files or Information), T1070 (Indicator Removal)
- Credential Access: T1003 (OS Credential Dumping), T1552 (Unsecured Credentials)
- Discovery: T1033 (System Owner/User Discovery), T1082 (System Information Discovery), T1083 (File and Directory Discovery), T1135 (Network Share Discovery), T1057 (Process Discovery), T1007 (System Service Discovery)
- Lateral Movement: T1021 (Remote Services: SMB/Windows Admin Shares)
- Command and Control: T1071 (Application Layer Protocol)
- Exfiltration: T1002 (Data Compressed), T1048 (Exfiltration Over Alternative Protocol)
- Impact: T1486 (Data Encrypted for Impact), T1489 (Service Stop), T1490 (Inhibit System Recovery). *Rubeus was used for privilege escalation* (https://nologs-nobreach.com/2022/07/24/play-ransomware/) *and Cobalt Strike for post-compromise and SystemBC RAT for persistence* (https://www.avertium.com/resources/threat-reports/an-in-depth-look-at-play-ransomware). *The group employs a double-extortion model, encrypting systems after exfiltrating data* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a). 

 Impact: Play ransomware has targeted numerous organizations, compromising 110 victims who refused to pay the ransom within the observed period. *As of October 2023, the FBI was aware of approximately 300 affected entities* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a). 

 Communication Method: *The ransomware group uses the email address gyeceeidia7y@gmx.com for communication* (https://www.bleepingcomputer.com/forums/t/773651/play-ransomware-play-findom-support-topic/). Note, the email in some incidents was different but used the gmx.de domain* (https://nologs-nobreach.com/2022/07/24/play-ransomware/). 

 Mitigation: {'Audit and Inventory': '- Take an inventory of assets and data.\n- Identify authorized and unauthorized devices and software.\n- Audit event and incident logs.', 'Configure and Monitor': '- Manage hardware and software configurations.\n- Grant admin privileges and access only when necessary.\n- Monitor network ports, protocols, and services.\n- Activate security configurations on network infrastructure devices.\n- Establish a software allowlist for legitimate applications.', 'Patch and Update': '- Conduct regular vulnerability assessments.\n- Perform patching or virtual patching for operating systems and applications.\n- Update software and applications to their latest versions.', 'Protect and Recover': '- Implement data protection, backup, and recovery measures.\n- Enable multifactor authentication (MFA).', 'Secure and Defend': '- Employ sandbox analysis to block malicious emails.\n- Deploy the latest security solutions to all system layers.\n- Use AI and machine learning-powered detection technologies.', 'Train and Test': '- Regularly train and assess employees on security skills.\n- Conduct red-team exercises and penetration tests.'} 

 Detection Signature: {'Service': 'Microsoft Exchange, FortiOS SSL VPN', 'Port': 'Various (specific to vulnerabilities exploited, such as SSL VPN ports)', 'Severity': 'Critical', 'Incident': 'Play Ransomware', 'Signature name': 'Play ransomware vulnerability exploitation', 'Internal checks': '- Ensure patches for CVE-2018-13379, CVE-2020-12812, CVE-2022-41040, CVE-2022-41080, CVE-2022-41082 are applied.\n- Regularly audit user accounts for signs of compromise.', 'External scanning': '- Scan for open ports commonly associated with the vulnerabilities.\n- Monitor for exploitation attempts against known vulnerabilities.'} 

 IoCs: The document indicates that indicators of compromise (IoCs) for Play ransomware are available but not explicitly listed in the provided text. The IoCs can be found [here](https://documents.trendmicro.com/assets/txt/ioc-list-ransomware-spotlight-play-8mFIjbD.txt). *Additional IoCs include filenames ppp.exe and zxc.exe and SHA256 hash dd101db5d9503f33a0c23d79da3642e999375748f7c1532e98c813b114bdfa1a. Initial Access IPs: 139.177.192[.]90, 84.32.190[.]6* (https://nologs-nobreach.com/2022/07/24/play-ransomware/). *Additional IoCs include SHA256 hashes 453257c3494addafb39cb6815862403e827947a1e7737eb8168cd10522465deb, 47c7cee3d76106279c4c28ad1de3c833c1ba0a2ec56b0150586c7e8480ccae57, and 7dea671be77a2ca5772b86cf8831b02bff0567bce6a3ae023825aa40354f8aca* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a). 

 Additional Details: *The ransomware does not typically include a ransom note or extortion letter, only a .txt file with an email address* (https://www.bleepingcomputer.com/forums/t/773651/play-ransomware-play-findom-support-topic/). *Additionally, the C:\PerfLog directory was used for staging malicious tools and ransomware execution was carried out through scheduled tasks and direct command line execution* (https://nologs-nobreach.com/2022/07/24/play-ransomware/). *Play ransomware actors use tools like AdFind to query Active Directory, GMER to disable anti-virus software, and WinRAR to compress files* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a). 


# Related articles (describing the same threat) 
['https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play', 'https://www.bleepingcomputer.com/forums/t/773651/play-ransomware-play-findom-support-topic/', 'https://nologs-nobreach.com/2022/07/24/play-ransomware/', 'https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a', 'https://www.avertium.com/resources/threat-reports/an-in-depth-look-at-play-ransomware']
