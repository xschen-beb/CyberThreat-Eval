Source: [https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)

## Related articles (describing the same threat) 
- https://malware.news/t/stellar-discovery-of-a-new-cluster-of-andromeda-gamarue-c2/88931
- https://redcanary.com/threat-detection-report/threats/gamarue
- https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2
- https://www.anvilogic.com/threat-reports/rundll32-with-suspicious-command-line
- https://social.cyware.com/news/new-andromedagamarue-command-and-control-cluster-targets-apac-industries-6f631077

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident 
 New Cluster of Andromeda/Gamarue C2 

#### Root cause 
 The root cause of the incident is the infection through USB drives that host and hide malicious files. This is commonly known as a 'USB drive-by attack' or 'USB drop attack.' The attack utilized LNK shortcuts with generic file names to entice users to execute the malware. *Gamarue, also known as Andromeda, b66, or Wauchos, continues to spread primarily via infected USB drives, indicating poor security hygiene* (https://redcanary.com/threat-detection-report/threats/gamarue/). 

#### Threat actor/group/campaign 
 The threat actor behind this campaign is currently unknown, but the infrastructure used for the Command and Control (C2) communication was associated with the Andromeda/Gamarue malware family. There is a low to medium confidence link with the Turla campaign. *Mandiant reported that the Turla Team, tracked under the name UNC4210, re-registered expired Gamarue domains in 2022 to profile victims for follow-on malware attacks* (https://redcanary.com/threat-detection-report/threats/gamarue/). *The Cybereason Security Services Team unveiled the discovery of a new cluster of Command-and-Control (C2) servers linked to the infamous Andromeda (aka Gamarue) malware family and issued comprehensive Threat Analysis reports to inform on these threats* (https://malware.news/t/stellar-discovery-of-a-new-cluster-of-andromeda-gamarue-c2/88931). *Multiple occurrences of Andromeda-like malware (aka. b66 and Gamarue) have been identified across various customer environments, highlighting its modular nature* (https://www.anvilogic.com/threat-reports/rundll32-with-suspicious-command-line). 

#### Organization/industry/location 
 The targeted victims are manufacturing and logistics companies in the APAC region. 

#### Start date – End date 
 The specific start and end dates of the attack are not mentioned. 

#### MITRE TTPs 
 {'- TA0002: Initial Access (T1091 - Removable Media) - Confidence Score: High': '', '- TA0002: Execution (T1204.002 - User Execution: Malicious File) - Confidence Score: High': '', '- TA0002: Execution (T1055.001 - Process Injection: Dynamic-link Library Injection) - Confidence Score: Medium': '', '- TA0002: Execution (T1059 - Command and Scripting Interpreter) - Confidence Score: Medium': '', '- TA0003: Persistence (T1547.009 - Boot or Logon Autostart Execution: Shortcut Modification) - Confidence Score: High': '', '- TA0003: Persistence (T1543.003 - Create or Modify System Process: Windows Service) - Confidence Score: Medium': '', '- TA0003: Persistence (T1129 - Shared Modules) - Confidence Score: Low': '', '- TA0005: Defence Evasion (T1036.003 - Masquerading: Rename System Utilities) - Confidence Score: Medium': '', '- TA0005: Defence Evasion (T1027.002 - Obfuscated Files or Information: Software Packing) - Confidence Score: Medium': '', '- TA0005: Defence Evasion (T1112 - Modify Registry) - Confidence Score: High': '', '- TA0005: Defence Evasion (T1036.004 - Masquerading: Masquerade Task or Service) - Confidence Score: Medium': '', '- TA0011: Command and Control (T1071.001 Application Layer Protocol: Web Protocols) - Confidence Score: High': ''} 

#### Impact 
 Multiple manufacturing and logistics companies in the APAC region were targeted, leading to potential industrial espionage and data theft. 

#### Mitigation Steps 
 {'1. Implement and enforce the use of endpoint protection and EDR solutions to detect and block malicious files and processes.': '', '2. Enable Application Control to block the execution of unauthorized or suspicious applications.': '', '3. Enable Anti-Ransomware features with shadow copy detection to protect against ransomware attacks.': '', '4. Educate employees on the risks of using unknown USB drives and the importance of not clicking on suspicious files.': '', '5. Regularly update and patch systems to close security vulnerabilities.': '', '6. Implement network segmentation and access controls to limit the spread of malware.': '', '7. Monitor and analyze network traffic for signs of C2 communications and other suspicious activities.': '', '*8. Manage Removable Storage Access Control using group policy to restrict read, write, and/or execute actions from USB devices.* (https://redcanary.com/threat-detection-report/threats/gamarue/)': '', '*9. Enable the Windows attack surface reduction (ASR) rule to block untrusted and unsigned processes that run from USB devices.* (https://redcanary.com/threat-detection-report/threats/gamarue/)': '', '*10. Disable AutoPlay on Windows to prevent automatic execution of files from USB devices.* (https://redcanary.com/threat-detection-report/threats/gamarue/)': '', '*11. Investigate if your antivirus software has a feature to scan removable drives during mounting.* (https://redcanary.com/threat-detection-report/threats/gamarue/)': ''} 

#### Detection Signature 
 {'Service: Windows OS': '', 'Port: N/A': '', 'Severity: Critical': '', 'Incident: Andromeda/Gamarue C2 Cluster': '', 'Signature name: “Andromeda/Gamarue USB Infection”': '', 'Internal checks:': {'Setting1: Monitor for execution of rundll32.exe with unusual DLL names (e.g., ~$W*.USBDrv, ~$W*.FAT32) – Inside VMs': '', 'Setting2: Monitor for creation of LNK files with suspicious names – Inside VMs': '', 'Setting3: Monitor for registry modifications related to persistence techniques (e.g., adopeflash, adopeupdate) – Inside VMs': '', '*Setting4: Monitor for rundll32.exe command lines with long filenames and random function names* (https://redcanary.com/threat-detection-report/threats/gamarue/)': '', '*Setting5: Detect rundll32.exe with obfuscated strings (e.g., "C:\\Windows\\system32\\rundll32.exe" _----______--_-_-_---__---_----_-__---___-_____---_-__,wmSMWWOemsikSACk)* (https://www.anvilogic.com/threat-reports/rundll32-with-suspicious-command-line)': ''}, 'External scanning:': {'Monitor for C2 domain connections (e.g., suckmycocklameavindustry.in, deltaheavy.ru)': '', 'Monitor for connections to known malicious IP addresses (e.g., 34.29.71.138, 44.200.43.61)': ''}} 

#### IoCs:
- ip: 34.29.71.138 ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- ip: 104.198.2.251 ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- ip: 184.105.192.2 ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- ip: 35.204.181.10 ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- ip: 44.200.43.61 ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- domain: suckmycocklameavindustry.in ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- domain: deltaheavy.ru ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- hash_sha1: 274c2facba9d04e1f3cbf31528af0ac162da5db7 ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- hash_sha1: b0fb70192b26c18858893f09e9d75d2e52f3f475 ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- hash_sha1: 2620d60d8283936d6671713477cdd9ae2e28eb1b ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- hash_sha1: c20c26d9f4f9bff3cf4c29b5c1c30252d938eddb ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- hash_sha1: 72bc039f1d37b610ba6c4b577dbe82feba37e813 ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- hash_sha1: e4fcf9c1ee2dcc115f5fc8f074fa56ffd484aac9 ([link](https://www.cybereason.com/blog/new-cluster-andromeda-gamrue-c2)) 

- domain: securityonline.info ([link](https://social.cyware.com/news/new-andromedagamarue-command-and-control-cluster-targets-apac-industries-6f631077)) 

- For more IoCs, please refer to the above links. 

#### paste IoC
34.29.71.138
104.198.2.251
184.105.192.2
35.204.181.10
44.200.43.61
suckmycocklameavindustry.in
deltaheavy.ru
274c2facba9d04e1f3cbf31528af0ac162da5db7
b0fb70192b26c18858893f09e9d75d2e52f3f475
2620d60d8283936d6671713477cdd9ae2e28eb1b
c20c26d9f4f9bff3cf4c29b5c1c30252d938eddb
72bc039f1d37b610ba6c4b577dbe82feba37e813
e4fcf9c1ee2dcc115f5fc8f074fa56ffd484aac9
securityonline.info

