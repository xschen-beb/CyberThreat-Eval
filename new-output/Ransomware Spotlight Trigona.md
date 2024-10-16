Source: [https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-trigona](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-trigona)

# Ransomware Spotlight Trigona

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Trigona Ransomware 

 Root cause: Trigona ransomware attacks exploited CVE-2021-40539 vulnerability in Zoho ManageEngine ADSelfService Plus, brute-forced Microsoft SQL (MSSQL) Servers, and used compromised credentials from network access brokers. *They also used tools like Splashtop* (https://www.trendmicro.com/en_vn/research/23/f/an-overview-of-the-trigona-ransomware.html). *AhnLab Security Emergency Response Center (ASEC) identified the use of the CLR extended procedure feature for malicious functions* (https://blackswan-cybersecurity.com/trigona-ransomware-targeting-ms-sql-servers/). 

 Threat Actor/group/campaign: Trigona Ransomware group, potentially affiliated with CryLock and BlackCat ransomware groups. 

 Organization/industry/location: Various industries, notably government, technology, retail, FMCG, banking sectors, and SMBs across North America, Europe, Asia-Pacific, and Latin America. *Significant activity detected in the US, India, Israel, Turkey, Brazil, and Italy* (https://www.trendmicro.com/en_vn/research/23/f/an-overview-of-the-trigona-ransomware.html). 

 Start date – End date: October 2022 – October 2023 

 MITRE TTPs: ['T1190 - Exploit Public-Facing Application (CVE-2021-40539)', 'T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder', 'T1140 - Deobfuscate/Decode Files or Information', 'T1218.005 - System Binary Proxy Execution: Mshta', 'T1036.005 - Masquerading: Match Legitimate Name or Location', 'T1497.003 - Virtualization/Sandbox Evasion: Time-Based Evasion', 'T1083 - File and Directory Discovery', 'T1135 - Network Share Discovery', 'T1033 - System Owner/User Discovery', 'T1529 - System Shutdown/Reboot', 'T1486 - Data Encrypted for Impact', 'T1485 - Data Destruction'] 

 Impact: The ransomware group compromised 33 organizations, targeting government sectors and SMBs, through encrypted data, stolen documents, and contracts published on a leak site. *They used a double extortion scheme, with a leak site on IP address port 8000* (https://www.trendmicro.com/en_vn/research/23/f/an-overview-of-the-trigona-ransomware.html). *The ransomware executed via svcservice.exe and svchost.bat* (https://blackswan-cybersecurity.com/trigona-ransomware-targeting-ms-sql-servers/). 

 Mitigation: ['Regularly patch and update all systems and applications to address known vulnerabilities like CVE-2021-40539.', 'Implement robust password policies and multi-factor authentication (MFA).', 'Monitor network ports, protocols, and services, and restrict unnecessary exposure.', 'Employ network segmentation to limit ransomware spread.', 'Use advanced detection technologies such as AI and machine learning for early detection.', 'Implement data protection, backup, and recovery measures for quick restoration.', 'Conduct regular vulnerability assessments and penetration testing.'] 

 Detailed Steps for mitigation: ['**Patch Management**: Ensure all systems and applications are up-to-date with the latest patches.', '**Access Control**: Implement MFA and strong password policies. Limit administrative privileges.', '**Network Monitoring**: Monitor network traffic for unusual activities, particularly on ports commonly used by the exploited services.', '**Network Segmentation**: Isolate critical systems from less secure environments.', '**Endpoint Protection**: Deploy endpoint detection and response (EDR) solutions to monitor and respond to suspicious activities.', '**Backup Strategy**: Regularly back up data and verify the integrity of backups. Ensure backups are not connected to the network.', '**Employee Training**: Regularly train employees on phishing and social engineering attack recognition.'] 

 Detection Signature: {'Service': 'MSSQL', 'Port': '1433', 'Severity': 'Critical', 'Incident': 'Trigona Ransomware', 'Signature name': '“MSSQL Brute Force Attack”', 'Internal checks': ['Setting1: Monitor failed login attempts on MSSQL (event IDs 18456).', 'Setting2: Detect unusual spikes in MSSQL login attempts.', 'Setting3: Ensure MSSQL databases are secured with strong, unique passwords and MFA.'], 'External scanning': ['Port (1433) open', 'Unusual login attempts']} 

 IoCs: Indicators of compromise can be found [here](https://documents.trendmicro.com/images/TEx/articles/trigona-ransomware-iocs78HQqGi.txt). *The group also used the Mimikatz credential dumper and developed a Linux version of their ransomware* (https://www.trendmicro.com/en_vn/research/23/f/an-overview-of-the-trigona-ransomware.html). 

 Additional Tools: ['*Advanced Port Scanner* (https://www.itsc.cuhk.edu.hk/user-trainings/information-security-best-practices/ransomware-trigona/)', '*SoftPerfect Network Scanner* (https://www.itsc.cuhk.edu.hk/user-trainings/information-security-best-practices/ransomware-trigona/)', '*ScreenConnect* (https://www.itsc.cuhk.edu.hk/user-trainings/information-security-best-practices/ransomware-trigona/)', '*AnyDesk* (https://www.itsc.cuhk.edu.hk/user-trainings/information-security-best-practices/ransomware-trigona/)'] 


# Related articles (describing the same threat) 
['https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-trigona', 'https://www.trendmicro.com/en_vn/research/23/f/an-overview-of-the-trigona-ransomware.html', 'https://www.itsc.cuhk.edu.hk/user-trainings/information-security-best-practices/ransomware-trigona/', 'https://blackswan-cybersecurity.com/trigona-ransomware-targeting-ms-sql-servers/']
