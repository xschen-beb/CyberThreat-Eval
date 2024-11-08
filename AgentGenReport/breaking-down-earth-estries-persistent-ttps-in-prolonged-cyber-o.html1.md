Source: [https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-o.html](https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-o.html)

## Related articles (describing the same threat) 
- https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-o.html
- https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations/iocs-breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations.txt
- https://medium.com/@cybermaterial/cyber-briefing-2024-11-08-3a580f43d56e
- https://candid.technology/earth-estries-targets-exchange-servers-network-tools-in-a-new-campaign/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: Earth Estries Persistent TTPs in Prolonged Cyber Operations 

#### Root cause 
 The root cause behind the incident includes the exploitation of vulnerabilities in Microsoft Exchange servers and misconfigured QConvergeConsole installations, abuse of network adapter management tools, Apache Tomcat vulnerabilities, and new advanced tactics employing PsExec, Cobalt Strike, Trillclient, Hemigate, and Crowdoor delivered via CAB files. Additionally, malware such as Zingdoor and SnappyBee are deployed through cURL downloads, maintaining persistence and stealing credentials. *The changes* (https://medium.com/@cybermaterial/cyber-briefing-2024-11-08-3a580f43d56e). *The use of wget commands, ChinaCopper web shell, and DLL sideloading were also noted* (https://candid.technology/earth-estries-targets-exchange-servers-network-tools-in-a-new-campaign/). 

#### Threat actor/group/campaign 
 Earth Estries (also known as Salt Typhoon); BlueNoroff targeting cryptocurrency firms with Hidden Risk macOS malware *The changes* (https://medium.com/@cybermaterial/cyber-briefing-2024-11-08-3a580f43d56e). 

#### Organization/industry/location 
 The targeted entities include government and technology sectors. *The changes* (https://medium.com/@cybermaterial/cyber-briefing-2024-11-08-3a580f43d56e). 

#### Start date – End date 
 The attacks have been active since at least 2020, with the report published on November 08, 2024, indicating ongoing activities. 

#### MITRE TTPs 
 ['T1078: Valid Accounts', 'T1071: Application Layer Protocol', 'T1021: Remote Services', 'T1059: Command and Scripting Interpreter', 'T1047: Windows Management Instrumentation', 'T1053: Scheduled Task/Job', 'T1070: Indicator Removal on Host', 'T1105: Ingress Tool Transfer', 'T1083: File and Directory Discovery', 'T1016: System Network Configuration Discovery', 'T1110: Brute Force', 'T1560: Archive Collected Data', 'T1003: Credential Dumping', 'ZIP concatenation evasion technique *The changes* (https://medium.com/@cybermaterial/cyber-briefing-2024-11-08-3a580f43d56e). *Additional techniques include the use of wget commands and DLL sideloading* (https://candid.technology/earth-estries-targets-exchange-servers-network-tools-in-a-new-campaign/).'] 

#### Impact 
 The impact includes unauthorized access to internal systems, theft of credentials, exfiltration of sensitive documents, and evasion of security detection through ZIP concatenation. *The changes* (https://medium.com/@cybermaterial/cyber-briefing-2024-11-08-3a580f43d56e). 

#### Mitigation Steps 
 ['Patch known vulnerabilities in Microsoft Exchange servers and other publicly exposed services.', 'Secure QConvergeConsole and other management tools by applying the latest updates and following best security practices.', 'Implement robust credential management practices, including the use of multi-factor authentication.', 'Regularly audit and restrict the use of administrative tools like PsExec and WMIC.', 'Utilize network segmentation to limit lateral movement.', 'Monitor and block suspicious network traffic, especially related to known IoCs.', 'Deploy endpoint detection and response (EDR) solutions to detect and remediate malicious activities.', 'Use behavioral analysis to detect unusual patterns indicative of an ongoing attack.', 'Implement a comprehensive backup and disaster recovery plan to ensure data integrity and availability.'] 

#### Detection Signature 
 {'Service': 'QConvergeConsole, Microsoft Exchange Server', 'Port': '443 (HTTPS), 8080 (HTTP)', 'Severity': 'Critical', 'Incident': 'Earth Estries Persistent TTPs', 'Signature name': 'Earth Estries Activity Detection', 'Internal checks': ['Setting1: QConvergeConsole should be updated to the latest version.', 'Setting2: Microsoft Exchange Server should be patched for known vulnerabilities.', 'Setting3: Administrative tools should be restricted and monitored.'], 'External scanning': ['Port 443 open with known vulnerabilities', 'Port 8080 open with known vulnerabilities']} 

#### IoCs: 
- url: http://mail.ocac.org.pk/UNBCL.docx ([link](https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations)) 

- url: http://mail.ocac.org.pk/Portscan.docx ([link](https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations)) 

- url: https://api.anonfiles.com/upload ([link](https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations)) 

- url: https://file.io ([link](https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations)) 

- url: http://96.44.160.181/VXTR.txt ([link](https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations)) 

- url: http://mail.ocac.org.pk/SetupPlatform.docx ([link](https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations)) 
- ...


