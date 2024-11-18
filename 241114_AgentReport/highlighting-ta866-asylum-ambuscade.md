Source: [https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade)

## Related articles (describing the same threat) 
- https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade
- https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/
- https://malpedia.caad.fkie.fraunhofer.de/actor/ta866
- https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me
- https://www.cyberthreatalliance.org/member_share/highlighting-ta866-asylum-ambuscade-activity-since-2021/
- https://thehackernews.com/2023/06/asylum-ambuscade-cybercrime-group-with.html
- https://blog.talosintelligence.com/warmcookie-analysis/
- https://www.infosecurity-magazine.com/news/malware-warmcookie-users-malicious/
- https://hackread.com/ta866-group-warmcookie-malware-espionage-campaign/

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: TA866/Asylum Ambuscade Activity 

#### Root cause 
 The primary root cause behind the incidents attributed to TA866 involves the use of malspam and malvertising to gain initial access to victim systems. Following initial access, a variety of malicious toolkits, including JavaScript downloaders, WasabiSeed, Screenshotter, AHK Bot, SunSeed, and others such as WarmCookie, Resident backdoor, CSharp-Streamer-RAT, Cobalt Strike, Rhadamanthys Stealer, NODEBOT, AdFind, and network scanners, are deployed to facilitate further compromise and data exfiltration with financially motivated campaigns and possible espionage objectives (https://malpedia.caad.fkie.fraunhofer.de/actor/ta866). The attack chain often involves a 404 Traffic Distribution System (TDS) to filter traffic and redirect victims to download malicious payloads (https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me). The attackers have exploited the Follina vulnerability (CVE-2022-30190) to download MSI packages (https://thehackernews.com/2023/06/asylum-ambuscade-cybercrime-group-with.html). *WarmCookie, also known as BadSpace, has been distributed via malspam and malvertising since April 2024. It facilitates continuous long-term access and deployment of additional malware such as CSharp-Streamer-RAT and Cobalt Strike. WarmCookie campaigns use invoice and job agency themes, and leverage infrastructure like the LandUpdates808 cluster. The malware is often delivered through email attachments or malicious links, and it includes extensive functionality like command execution and screenshot capture. Recent samples indicate updates in its persistence mechanism and sandbox detection capabilities* (https://blog.talosintelligence.com/warmcookie-analysis/, https://www.infosecurity-magazine.com/news/malware-warmcookie-users-malicious/). *TA866's persistent attacks and sophisticated tactics involve a multi-stage infection chain, beginning with a malicious JavaScript downloader that retrieves payloads such as WasabiSeed and uses AutoHotKey scripts for various malicious activities* (https://hackread.com/ta866-group-warmcookie-malware-espionage-campaign/). 

#### Threat actor/group/campaign 
 TA866 (also known as Asylum Ambuscade) 

#### Organization/industry/location 
 The most affected industries are manufacturing, government, and financial services across multiple countries including the United States, Canada, United Kingdom, Germany, Italy, Austria, and the Netherlands. 

#### Start date – End date 
 Since at least 2019 (https://malpedia.caad.fkie.fraunhofer.de/actor/ta866) – Ongoing as of October 2024 

#### MITRE TTPs 
 ['T1589.002 Gather Victim Identity Information: Email Addresses', 'T1586.002 Compromise Accounts: Email Accounts', 'T1608.006 Stage Capabilities: SEO Poisoning', 'T2583.008 Acquire Infrastructure: Malvertising', 'T1566 Phishing', 'T1566.001 Spearphishing Attachment', 'T1566.002 Spearphishing Link', 'T1059.001 Command and Scripting Interpreter: PowerShell', 'T1059.003 Command and Scripting Interpreter: Windows Command Shell', 'T1047 Windows Management Instrumentation', 'T1574.002 Hijack Execution Flow: DLL Side-Loading', 'T1218.007 System Binary Proxy Execution: Msiexec', 'T1069.002 Permission Groups Discovery: Domain Groups', 'T1016 System Network Configuration Discovery', 'T1482 Domain Trust Discovery', 'T1018 Remote System Discovery', 'T1057 Process Discovery', 'T1007 System Service Discovery', 'T1518.001 Software Discovery: Security Software Discovery', 'T1124 System Time Discovery', 'T1082 System Information Discovery', 'T1033 System Owner / User Discovery', 'T1105 Ingress Tool Transfer', 'T1219 Remote Access Software', 'T1071.001 Application Layer Protocol: Web Protocols'] 

#### Impact 
 Multiple organizations across several industries have been impacted, with significant data exfiltration and potential espionage-related activities. 

#### Mitigation Steps 
 ['Implement robust email filtering to block malspam campaigns.', 'Employ web filtering solutions to prevent access to malicious websites and malvertising.', 'Regularly update and patch systems to prevent exploitation of known vulnerabilities.', 'Use multi-factor authentication to secure email accounts and other critical systems.', 'Monitor network traffic for signs of unusual activity indicative of TDS and C2 communications.', 'Deploy endpoint detection and response (EDR) solutions to detect and block malicious executables and scripts.', 'Conduct regular security awareness training for employees to recognize phishing and malvertising attempts.'] 

#### Detection Signature 
 {'Service': 'Web Filtering (Cisco Secure Web Appliance), Email Security (Cisco Secure Email), Snort IDS/IPS', 'Port': '80, 443', 'Severity': 'Critical', 'Incident': 'TA866/Asylum Ambuscade Activity', 'Signature name': '“Malicious JavaScript Downloader”, “WasabiSeed Detection”, “Screenshotter Detection”, “AHK Bot Detection”', 'Internal checks': ['Ensure email filtering systems are configured to identify and block malicious attachments and links.', 'Ensure web filtering solutions are in place to prevent access to known malicious domains and sites.', 'Regularly update EDR solutions with the latest threat intelligence signatures.'], 'External scanning': ['Monitor for unusual outbound traffic patterns indicative of data exfiltration.', 'Use IDS/IPS systems to detect known malicious activities and payloads associated with TA866.']} 

#### IoCs:
- ip: 185.73.124.164 ([link](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/)) 

- ip: 109.236.80.191 ([link](same as above)) 

- url: https://perfectsystems-ltd.com/x-css/cd.msi ([link](same as above)) 

- url: https://temp.sh/ThuNJ/2.dll ([link](same as above)) 

- url: https://temp.sh/esuJB/resident.exe ([link](same as above)) 

- hash_md5: 3edcde37dcecb1b5a70b727ea36521de ([link](same as above)) 

- domain: southfirstarea.com ([link](https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me)) 

- domain: black-socks.org ([link](same as above)) 

- sha256: d934d109f5b446febf6aa6a675e9bcc41fade563e7998788824f56b3cc16d1ed ([link](same as above)) 

- sha256: 29e447a6121dd2b1d1221821bd6c4b0e20c437c62264844e8bcbb9d4be35f013 ([link](same as above)) 

- sha256: 292344211976239c99d62be021af2f44840cd42dd4d70ad5097f4265b9d1ce01 ([link](same as above)) 

- sha256: 02049ab62c530a25f145c0a5c48e3932fa7412a037036a96d7198cc57cef1f40 ([link](same as above)) 

- sha256: d0a4cd67f952498ad99d78bc081c98afbef92e5508daf723007533f000174a98 ([link](same as above)) 

- sha256: 6e53a93fc2968d90891db6059bac49e975c09546e19a54f1f93fb01a21318fdc ([link](same as above)) 

- sha256: 322dccd18b5564ea000117e90dafc1b4bc30d256fe93b7cfd0d1bdf9870e0da6 ([link](same as above)) 

- sha256: 1f6de5072cc17065c284b21acf4d34b4506f86268395c807b8d4ab3d455b036b ([link](same as above)) 

- sha256: 3242e0a736ef8ac90430a9f272ff30a81e2afc146fcb84a25c6e56e8192791e4 ([link](same as above)) 

- sha256: 3db3f919cad26ca155adf8c5d9cab3e358d51604b51b31b53d568e7bcf5301e2 ([link](same as above)) 

- For more IoCs, please refer to the above links. 


