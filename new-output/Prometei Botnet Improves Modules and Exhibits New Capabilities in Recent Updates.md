Source: [https://blog.talosintelligence.com/prometei-botnet-improves/](https://blog.talosintelligence.com/prometei-botnet-improves/)

# Prometei Botnet Improves Modules and Exhibits New Capabilities in Recent Updates

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Prometei Botnet Improvements 

 Root cause: The root cause includes the exploitation of various vulnerabilities across different systems using methods like *SMB with stolen credentials* (https://blog.talosintelligence.com/prometei-botnet-and-its-quest-for-monero/). Misconfigured or vulnerable services such as Windows services, Apache Webserver, and PowerShell scripts were targeted to deploy the botnet. Prometei has expanded to target *IoT devices* with a new Linux variant discovered in *December 2020* (https://cujo.com/iot-malware-journals-prometei-linux/), using techniques like *persistence with cron jobs* (https://cujo.com/iot-malware-journals-prometei-linux/). The botnet now includes *new capabilities to complicate forensic analysis* and *improved infrastructure components* (https://www.cybersecurity-help.cz/blog/3181.html). 

 Threat Actor/group/campaign: Prometei Botnet operators 

 Organization/industry/location: The victims are indiscriminate, spanning vulnerable entities across various regions and industry verticals around the world. The botnet infects systems worldwide with significant infections in Brazil, Indonesia, and Turkey. The botnet is designed to *avoid attacking Russia* (https://www.cybersecurity-help.cz/blog/3181.html). 

 Start date – End date: First reported in 2020, with recent updates observed since November 2022 and *active since March 2020* (https://blog.talosintelligence.com/prometei-botnet-and-its-quest-for-monero/). 

 MITRE TTPs: ['T1584.005: Compromise Infrastructure: Botnet', 'T1059.001: Command and Scripting Interpreter: PowerShell', 'T1569.002: System Services: Service Execution', 'T1505.003: Server Software Component: Webshell', 'T1027: Obfuscated Files or Information', 'T1036: Masquerading', 'T1070.004: Indicator Removal on Host: File Deletion', 'T1140: Deobfuscate/Decode Files or Information', 'T1562: Impair Defenses', 'T1210: Exploitation of Remote Services', 'T0884: Connection Proxy', 'T1090.003: Proxy: Multi-hop Proxy', 'T1105: Ingress Tool Transfer', '*T1089: Disabling Security Tools* (https://blog.talosintelligence.com/prometei-botnet-and-its-quest-for-monero/)', '*T1086: PowerShell* (https://blog.talosintelligence.com/prometei-botnet-and-its-quest-for-monero/)'] 

 Impact: Approximately 10,000 systems infected globally. 

 Mitigation: ['Ensure all systems and software are up-to-date with the latest security patches.', 'Disable unnecessary services and ports to reduce the attack surface.', 'Implement multi-factor authentication and strong password policies.', 'Regularly review and update firewall rules to prevent unauthorized access.', 'Monitor for unusual network traffic and system behavior.', 'Use endpoint protection solutions that detect and prevent malware execution.', 'Implement proper segmentation of networks to limit lateral movement.', 'Regularly back up data and ensure backups are protected from ransomware/encryption.', 'Conduct regular security audits and penetration testing to identify and mitigate vulnerabilities.', 'Educate employees on recognizing phishing and social engineering attacks.'] 

 Detection Signature: {'Service': 'PowerShell', 'Port': 'N/A (internal command execution)', 'Severity': 'Critical', 'Incident': 'Prometei Botnet', 'Signature name': '“Prometei PowerShell Command”', 'Internal checks': ['Monitor and alert on unusual PowerShell script executions.', 'Ensure proper logging of PowerShell commands and scripts.', 'Implement PowerShell Script Block Logging and Module Logging.'], 'External scanning': ['Monitor for connections to known malicious C2 domains.', 'Inspect and block unauthorized PowerShell commands.']} 

 IoCs: ['Domains: xinchaodbcdbh[.]org, xinchaodbcdbh[.]com, xinchaoabcdcf[.]org, xinchaocecclk[.]org, xinchaocecclk[.]net', 'IPs: 103.65.236[.]53, 221.120.144[.]101, 177.73.237[.]55', 'Monero Wallet: 4A1txQ9L8h8NqF4EtGsZDP5vRN3yTVKynbkyP1jvCiDajNLPepPbBdrbaqBu8fCTcFEFdCtgbekSsTf17B1MhyE2AKCEyfR', 'File names: sqhost.exe, zsvc.exe, SearchIndexer.exe, std.7z, srch.7z, AppServ180.zip', 'Known hashes (from ClamAV signatures): Win.Trojan.MSShellcode-6, Win.Coinminer.Generic-7151250-0, Win.Malware.Tgqv7oji-9939403-0, Win.Trojan.Mimikatz-6466236-0, Win.Trojan.Prometei-8977166-0'] 

 Indicators of Compromise (IoCs): Indicators of Compromise (IoCs) associated with this threat can be found [here](https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2023/03/prometei-botnet-improves.txt). 


# Related articles (describing the same threat) 
['https://blog.talosintelligence.com/prometei-botnet-improves/', 'https://blog.talosintelligence.com/prometei-botnet-and-its-quest-for-monero/', 'https://cujo.com/iot-malware-journals-prometei-linux/', 'https://www.cybersecurity-help.cz/blog/3181.html']
