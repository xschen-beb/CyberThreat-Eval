Source: [https://www.trendmicro.com/en_us/research/23/h/monti-ransomware-unleashes-a-new-encryptor-for-linux.html](https://www.trendmicro.com/en_us/research/23/h/monti-ransomware-unleashes-a-new-encryptor-for-linux.html)

# Monti Ransomware Unleashes a New Encryptor for Linux

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Monti Ransomware Unleashes a New Encryptor for Linux 

 Root cause: The root cause includes the continued use of the Conti source code with significant modifications. This has enabled the Monti ransomware group to develop a new Linux-based variant. The new version employs a different encryptor and tampers with specific files, indicating a sophisticated attack vector. *This variant uses AES-256-CTR encryption and has a 29% similarity with the old variant, replacing the '-type=hard' parameter with '-type=soft'* (https://gbhackers.com/monti-ransomware-linux-variant/). 

 Threat Actor/group/campaign: Monti ransomware group, which has emulated Conti ransomware in tactics and procedures. 

 Organization/industry/location: The targeted industries include legal, financial services, healthcare, and others. Specific organizations were not mentioned. *However, several legal and government sectors have been infected* (https://www.bdrsuite.com/blog/monti-ransomware-returns-how-to-protect-your-linux-machines/). 

 Start date – End date: The data indicates activity from March to August 2023, with a noted resurgence in August 2023. 

 MITRE TTPs: {'T1486': 'Data Encrypted for Impact', 'T1490': 'Inhibit System Recovery', 'T1070': 'Indicator Removal on Host', 'T1203': 'Exploitation for Client Execution'} 

 Impact: The blog does not specify the number of records leaked or the financial losses incurred. 

 Mitigation: {'1': 'Implement multifactor authentication (MFA) to impede attackers from progressing horizontally within a network and gaining access to sensitive data.', '2': 'Adhere to the 3-2-1 guideline when generating backups for crucial files. This guideline entails creating three backup copies in two distinct file formats, with one copy stored at a separate location.', '3': 'Employ a multilayered approach to security using solutions such as: Trend Vision One™ for multilayered protection and behavior detection; Trend Cloud One™ – Workload Security for protection against known and unknown threats; Trend Micro™ Deep Discovery™ Email Inspector for blocking malicious emails; Trend Micro Apex One™ for automated threat detection and response.'} 

 Detection Signature: {'Service': 'Linux', 'Port': 'N/A (based on malware behavior, not specific ports)', 'Severity': 'Critical', 'Incident': 'Monti Ransomware', 'Signature name': 'Monti ransomware activity detected', 'Internal checks': {'1': 'Check for unexpected modifications to /etc/motd and index.html.', '2': 'Monitor for the presence of the “MONTI” string in files.', '3': 'Detect the use of the --whitelist, --vmkill, or --detach command line arguments.'}, 'External scanning': {'1': 'Look for files with the .monti extension.', '2': 'Monitor for the presence of ransom notes named readme.txt in directories.'}} 

 IoCs: {'Hashes': {'1': 'f1c0054bc76e8753d4331a881cdf9156dd8b812a (Ransom.Linux.MONTI.THGOCBC)', '2': 'a0c9dd3f3e3d0e2cd5d1da06b3aac019cdbc74ef (Ransom.Linux.MONTI.THGADBC)'}, 'URLs': {'1': 'hxxp://monti5o7lvyrpyk26lqofnfvajtyqruwatlfaazgm3zskt3xiktudwid[.]onion', '2': 'hxxp://mblogci3rudehaagbryjznltdp33ojwzkq6hn2pckvjq33rycmzczpid[.]onion'}} 

 Enhanced Information: {'*': "*Monti ransomware was discovered by researchers in June 2022 and has been emulating Conti ransomware in tactics and procedures. Monti's new Linux variant uses a different encryptor and tampers with specific files, indicating a sophisticated attack vector. The ransomware group exploits the Log4Shell vulnerability on VMware Horizon systems and has been investigated by Blackberry's Incident Response team. Monti has targeted legal, financial, healthcare, and other industries from March to August 2023, with a resurgence in August 2023. They also use tools like Action1 for remote monitoring. Notable MITRE TTPs include T1486, T1490, T1070, and T1203. The impact remains unspecified regarding records leaked or financial losses. Mitigation strategies include implementing MFA, adhering to the 3-2-1 backup guideline, and employing multilayered security solutions such as Trend Vision One™, Trend Cloud One™ – Workload Security, Trend Micro™ Deep Discovery™ Email Inspector, and Trend Micro Apex One™. Detection signatures focus on unexpected modifications to /etc/motd and index.html, presence of the “MONTI” string, specific command-line arguments, and files with the .monti extension. IoCs include hashes and URLs associated with the ransomware. *Only three security vendors have identified Ransom.Linux.MONTI.THGOCBC as malicious. The Monti group has targeted 13 organizations including legal, financial, healthcare, and others. They offer a free decryption key for random files to prove their claims* (https://www.bdrsuite.com/blog/monti-ransomware-returns-how-to-protect-your-linux-machines/). *This variant uses AES-256-CTR encryption and has a 29% similarity with the old variant, replacing the '-type=hard' parameter with '-type=soft'* (https://gbhackers.com/monti-ransomware-linux-variant/)."} 


# Related articles (describing the same threat) 
['https://www.trendmicro.com/en_us/research/23/h/monti-ransomware-unleashes-a-new-encryptor-for-linux.html', 'https://www.avertium.com/resources/threat-reports/monti-ransomware', 'https://www.bdrsuite.com/blog/monti-ransomware-returns-how-to-protect-your-linux-machines/', 'https://gbhackers.com/monti-ransomware-linux-variant/']
