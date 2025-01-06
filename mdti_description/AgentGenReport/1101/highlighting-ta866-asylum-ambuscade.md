Source: [https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/)


# Related articles (describing the same threat) 
https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/   [TA866 (also known as Asylum Ambuscade), malware WarmCookie is related to TA866]
https://blog.talosintelligence.com/warmcookie-analysis/             [WarmCookie analysis]
https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me [Report about TA866 in February 08, 2023 by Proofpoint]
https://www.welivesecurity.com/2023/06/08/asylum-ambuscade-crimeware-or-cyberespionage/   [Asylum Ambuscade, Jun 2023]
https://malpedia.caad.fkie.fraunhofer.de/details/win.warmcookie   [Malpedia for WarmCookie]
https://malpedia.caad.fkie.fraunhofer.de/actor/ta866                [Malpedia for TA866]
https://github.com/Cisco-Talos/IOCs/tree/main/2024/10/            [GitHub with IoCs, highlighting-ta866-asylum-ambuscade.txt]
https://www.infosecurity-magazine.com/news/malware-warmcookie-users-malicious/  [news]


# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Highlighting TA866/Asylum Ambuscade Activity Since 2021 

 Root cause: The root cause behind the incident includes the use of malspam and malvertising to facilitate malware distribution, leveraging Traffic Distribution Systems (TDS) for delivering malicious content, and exploiting trust relationships for initial access and spreading within networks. TA866 employs both commodity and custom tools including the WarmCookie malware (also known as Badspace, KongTuke, QUICKBIND), Resident backdoor, WasabiSeed, Screenshotter, and AHK Bot for initial access, persistence, and reconnaissance (https://blog.talosintelligence.com/warmcookie-analysis/; https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me). *WarmCookie communicates via HTTP C&C and is distributed through FAKEUPDATES campaigns* (https://malpedia.caad.fkie.fraunhofer.de/details/win.warmcookie). The group has also used CVE-2022-30190 (Follina vulnerability) for delivering payloads and developed NODEBOT, a Node.js-based tool (https://www.welivesecurity.com/2023/06/08/asylum-ambuscade-crimeware-or-cyberespionage/). *WarmCookie campaigns use lure themes such as job offers and invoices* (https://www.infosecurity-magazine.com/news/malware-warmcookie-users-malicious/). 

 Threat Actor/group/campaign: TA866, also known as Asylum Ambuscade 

 Organization/industry/location: Various industries including manufacturing, government, and financial services primarily in the United States, Canada, United Kingdom, Germany, Italy, Austria, and the Netherlands. Additional targets include bank customers and cryptocurrency traders in North America and Europe (https://www.welivesecurity.com/2023/06/08/asylum-ambuscade-crimeware-or-cyberespionage/). 

 Start date – End date: 2020 – October 2024 

 MITRE TTPs: ['T1589.002 Gather Victim Identity Information: Email Addresses', 'T1586.002 Compromise Accounts: Email Accounts', 'T1608.006 Stage Capabilities: SEO Poisoning', 'T2583.008 Acquire Infrastructure: Malvertising', 'T1566 Phishing', 'T1566.001 Spearphishing Attachment', 'T1566.002 Spearphishing Link', 'T1059.001 Command and Scripting Interpreter: PowerShell', 'T1059.003 Command and Scripting Interpreter: Windows Command Shell', 'T1047 Windows Management Instrumentation', 'T1574.002 Hijack Execution Flow: DLL Side-Loading', 'T1218.007 System Binary Proxy Execution: Msiexec', 'T1069.002 Permission Groups Discovery: Domain Groups', 'T1016 System Network Configuration Discovery', 'T1482 Domain Trust Discovery', 'T1018 Remote System Discovery', 'T1057 Process Discovery', 'T1007 System Service Discovery', 'T1518.001 Software Discovery: Security Software Discovery', 'T1124 System Time Discovery', 'T1082 System Information Discovery', 'T1033 System Owner / User Discovery', 'T1105 Ingress Tool Transfer', 'T1219 Remote Access Software', 'T1071.001 Application Layer Protocol: Web Protocols', 'T1083 File and Directory Discovery (https://blog.talosintelligence.com/warmcookie-analysis/)', 'T1055.001 Process Injection: Dynamic-link Library Injection (https://blog.talosintelligence.com/warmcookie-analysis/)', 'T1059.007 Command and Scripting Interpreter: JavaScript (https://www.welivesecurity.com/2023/06/08/asylum-ambuscade-crimeware-or-cyberespionage/)'] 

 Impact: Multiple industries affected, including the manufacturing sector, government, and financial services, across several countries. Recent campaigns are financially motivated with possible espionage objectives (https://malpedia.caad.fkie.fraunhofer.de/actor/ta866). 

 Mitigation: ['Implement email security solutions to block malspam.', 'Use web security appliances to prevent access to malicious websites.', 'Deploy endpoint protection solutions to prevent execution of malware.', 'Regularly update and patch systems to close vulnerabilities.', 'Train employees on recognizing phishing and malvertising attempts.', 'Implement network segmentation to limit the spread of malware.', 'Regularly back up critical data and verify the integrity of backups.'] 

 Detection Signature: {'Service': 'Web server, email server', 'Port': 'Various (e.g., HTTP/HTTPS, SMTP)', 'Severity': 'Critical', 'Incident': 'TA866/Asylum Ambuscade', 'Signature name': '“TA866 malspam and malvertising detection”', 'Internal checks': ['Ensure email filtering and scanning for malicious attachments and links.', 'Monitor web traffic for connections to known malicious URLs.'], 'External scanning': ['Identify and block IPs and domains associated with TA866 infrastructure.', 'Implement threat intelligence feeds to update detection mechanisms.']} 

 IoCs:
 ip: 185.73.124.164 

 ip: 109.236.80.191 

 url: http://temp.sh/ThuNJ/2.dll 

 url: http://temp.sh/esuJB/resident.exe 

 url: hxxps://perfectsystems-ltd.com/x-css/cd.msi 

 url: hxxps://landupdates808.com/upgrade/update.php 

 domain: southfirstarea[.]com 

 sha1: D5F8ACAD643EE8E1D33D184DAEA0C8EA8E7FD6F8 

 sha1: 519E388182DE055902C656B2D95CCF265A96CEAB 

 References: ['https://blog.talosintelligence.com/warmcookie-analysis/', 'https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me', 'https://www.welivesecurity.com/2023/06/08/asylum-ambuscade-crimeware-or-cyberespionage/', 'https://malpedia.caad.fkie.fraunhofer.de/details/win.warmcookie', '*highlighting-ta866-asylum-ambuscade.json and highlighting-ta866-asylum-ambuscade.txt* (https://github.com/Cisco-Talos/IOCs/tree/main/2024/10/)', '*WarmCookie campaigns use lure themes such as job offers and invoices* (https://www.infosecurity-magazine.com/news/malware-warmcookie-users-malicious/)'] 