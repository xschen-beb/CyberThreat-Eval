Source: [https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade)

## Related articles (describing the same threat) 
- https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade
- https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/
- https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me
- https://www.welivesecurity.com/2023/06/08/asylum-ambuscade-crimeware-or-cyberespionage/
- https://github.com/Cisco-Talos/IOCs/tree/main/2024/10/
- https://www.infosecurity-magazine.com/news/malware-warmcookie-users-malicious/
- https://any.run/malware-trends/warmcookie

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: TA866/Asylum Ambuscade Activity Since 2021 

#### Root cause 
 The root cause includes the exploitation of malspam, malvertising, and phishing emails with malicious Excel spreadsheet attachments. Misconfigured or vulnerable systems lacking adequate email filtering, web security, and endpoint protection are particularly susceptible to these attacks. 

#### Threat actor/group/campaign 
 TA866, also known as Asylum Ambuscade 

#### Organization/industry/location 
 *The primary targets are organizations in the United States and Germany, with additional cases in Canada, the United Kingdom, Germany, Italy, Austria, and the Netherlands. The most affected industries include manufacturing, government, and financial services* (https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me). 

#### Start date – End date 
 The activity has been observed since at least 2020 and continues until the present (October 2024). 

#### MITRE TTPs 
 - T1589.002 Gather Victim Identity Information: Email Addresses
- T1586.002 Compromise Accounts: Email Accounts
- T1608.006 Stage Capabilities: SEO Poisoning
- T2583.008 Acquire Infrastructure: Malvertising
- T1566 Phishing
- T1566.001 Spearphishing Attachment
- T1566.002 Spearphishing Link
- T1059.001 Command and Scripting Interpreter: PowerShell
- T1059.003 Command and Scripting Interpreter: Windows Command Shell
- T1047 Windows Management Instrumentation
- T1574.002 Hijack Execution Flow: DLL Side-Loading
- T1218.007 System Binary Proxy Execution: Msiexec
- T1069.002 Permission Groups Discovery: Domain Groups
- T1016 System Network Configuration Discovery
- T1482 Domain Trust Discovery
- T1018 Remote System Discovery
- T1057 Process Discovery
- T1007 System Service Discovery
- T1518.001 Software Discovery: Security Software Discovery
- T1124 System Time Discovery
- T1082 System Information Discovery
- T1033 System Owner / User Discovery
- T1105 Ingress Tool Transfer
- T1219 Remote Access Software
- T1071.001 Application Layer Protocol: Web Protocols 

#### Impact 
 Numerous organizations affected across various industries, with the deployment of malware leading to potential data theft, network compromise, and operational disruptions. 

#### Mitigation Steps 
 1. Implement robust email filtering to detect and block malspam.
2. Use web security solutions to block access to known malicious sites and prevent malvertising.
3. Deploy and maintain up-to-date endpoint protection solutions to detect and block malware.
4. Conduct regular security awareness training for employees to recognize phishing attempts.
5. Employ network segmentation to limit the spread of malware within the network.
6. Regularly update and patch systems to fix known vulnerabilities.
7. Monitor network traffic for unusual activity that may indicate a compromise. 

#### Detection Signature 
 Service: Email, Web, and Endpoint Security
Severity: Critical
Incident: TA866/Asylum Ambuscade Activity
Signature name: “TA866 Malspam and Malvertising Detection”
Internal checks (see next)
- Setting1: Implement email filtering rules to detect and block phishing attempts.
- Setting2: Use web proxies or secure web gateways to block access to malicious sites.
- Setting3: Deploy endpoint detection and response (EDR) solutions to identify and mitigate malware. 

#### External scanning 
 Monitor email traffic for signs of phishing and malspam.
Scan web traffic for access to known malicious domains.
Use EDR solutions to identify suspicious processes and unauthorized software. 

#### IoCs: 
- ip: 185.73.124.164 ([link](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/)) 

- ip: 109.236.80.191 ([link](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/)) 

- url: https://perfectsystems-ltd.com/x-css/cd.msi ([link](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/)) 

- url: https://temp.sh/ThuNJ/2.dll ([link](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/)) 

- url: https://temp.sh/esuJB/resident.exe ([link](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/)) 

- domain: southfirstarea.com ([link](https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me)) 

- domain: black-socks.org ([link](https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me)) 

- url: http://79.137.198.60/1/ke.msi ([link](https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me)) 

- ip: 5.39.222.150 ([link](https://www.welivesecurity.com/2023/06/08/asylum-ambuscade-crimeware-or-cyberespionage/)) 

- ip: 5.44.42.27 ([link](https://www.welivesecurity.com/2023/06/08/asylum-ambuscade-crimeware-or-cyberespionage/)) 

- ip: 45.154.69.66 ([link](https://github.com/Cisco-Talos/IOCs/tree/main/2024/10/)) 

- ip: 192.155.95.222 ([link](https://github.com/Cisco-Talos/IOCs/tree/main/2024/10/)) 

- file: gophish-powerrat-dcrat.json ([link](https://github.com/Cisco-Talos/IOCs/tree/main/2024/10/)) 

- file: threat-actor-believed-to-be-spreading-new-medusalocker-variant-since-2022.json ([link](https://github.com/Cisco-Talos/IOCs/tree/main/2024/10/)) 

- ip: 45.134.174.245 ([link](https://any.run/malware-trends/warmcookie)) 

- ip: 91.222.173.245 ([link](https://any.run/malware-trends/warmcookie)) 

- ip: 195.66.213.243 ([link](https://any.run/malware-trends/warmcookie)) 

- domain: reports.checkfedexexp.com ([link](https://any.run/malware-trends/warmcookie)) 

- domain: mx1.info.tntseminars.com ([link](https://any.run/malware-trends/warmcookie)) 

#### Tools/Utilities 
 WarmCookie; BadSpace; Resident backdoor; CSharp-Streamer-RAT; Cobalt Strike; Rhadamanthys; AdFind; AnyDesk; Remote Utilities; AHK Bot; WasabiSeed; Screenshotter; 404 TDS; SunSeed; AHKBOT; NODEBOT *Your changes* (https://www.welivesecurity.com/2023/06/08/asylum-ambuscade-crimeware-or-cyberespionage/); *malicious JavaScript downloaders; C2 commands; sandbox detection capabilities; persistent access* (https://www.infosecurity-magazine.com/news/malware-warmcookie-users-malicious/); *phishing emails with job lures; WarmCookie backdoor; encrypted communication with C2* (https://any.run/malware-trends/warmcookie) 


