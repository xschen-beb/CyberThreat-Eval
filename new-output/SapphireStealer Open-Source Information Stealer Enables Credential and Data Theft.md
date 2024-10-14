Source: [https://blog.talosintelligence.com/sapphirestealer-goes-open-source/](https://blog.talosintelligence.com/sapphirestealer-goes-open-source/)

# SapphireStealer Open-Source Information Stealer Enables Credential and Data Theft

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: *SapphireStealer: Open-source information stealer enables credential and data theft* (https://www.pcrisk.com/removal-guides/27668-sapphirestealer-malware) 

 Root cause: The root cause involves the use of an open-source malware called SapphireStealer, made publicly available on GitHub. It facilitates credential and data theft by exploiting user systems *using DotNetZip* (https://github.com/0day2/SapphireStealer/), and targets device data such as CPU architecture and IP addresses *through multi-stage processes* (https://www.pcrisk.com/removal-guides/27668-sapphirestealer-malware). 

 Threat Actor/group/campaign: Multiple threat actors are involved, utilizing and modifying SapphireStealer, initially developed by R3VENGE#1539, to enhance its capabilities for data exfiltration. These actors aim to steal credentials and sell them for cyber-espionage, ransomware, and identity theft. *Some threat actors have extended SapphireStealer to support added functionality and used anti-detection mechanisms, reflecting an increasing trend* (https://malware.news/t/new-open-source-infostealer-and-reflections-on-2023-so-far/73009). 

 Organization/industry/location: Various organizations and industries globally, as the malware is sold and distributed across multiple underground forums. 

 Start date – End date: The initial public release of SapphireStealer was on December 25, 2022. Threat activities have been observed from mid-January 2023 through the first half of 2023. *The emergence of new stealers has been noted in 2023* (https://malware.news/t/new-open-source-infostealer-and-reflections-on-2023-so-far/73009). 

 MITRE TTPs: ['T1056.004: Credential Dumping: Credential API Hooking', 'T1056.001: Input Capture: Keylogging', 'T1113: Screen Capture', 'T1027: Obfuscated Files or Information', 'T1185: Browser Session Hijacking', 'T1071.001: Application Layer Protocol: Web Protocols'] 

 Impact: Multiple organizations have been affected with stolen credentials and sensitive data being exfiltrated. The exact number of impacted entities or financial losses is not specified. *The presence of SapphireStealer can result in severe privacy issues and identity theft* (https://www.pcrisk.com/removal-guides/27668-sapphirestealer-malware). 

 Mitigation: {'1': 'Secure environment from open-source malware by implementing the following steps:', 'steps': ['Regularly update and patch systems to prevent exploitation of vulnerabilities.', 'Use multi-factor authentication (MFA) to reduce the risk of credential compromise.', 'Implement network segmentation and least privilege principles to limit the spread of malware.', 'Employ endpoint detection and response (EDR) solutions to identify and mitigate malicious activities promptly.', 'Educate employees on phishing attacks and safe browsing practices to reduce the likelihood of initial infection.'], '2': 'Specific steps to protect against SapphireStealer:', 'steps_specific': ['Monitor and restrict access to GitHub repositories to prevent downloading malicious code.', 'Implement application whitelisting to prevent unauthorized execution of unknown applications.', 'Use secure email gateways to block phishing attempts and malicious attachments.', 'Employ web filtering solutions to block access to known malicious sites and IPs.']} 

 Detection Signature: {'Service': 'HTTP/HTTPS', 'Port': '80/443', 'Severity': 'Critical', 'Incident': 'SapphireStealer', 'Signature name': 'SapphireStealer data exfiltration via SMTP/Discord/Telegram', 'Internal checks': ['Monitor outbound connections to known SMTP servers, Discord webhooks, and Telegram APIs.', 'Detect and alert on the creation of directories like %TEMP%\\sapphire\\work.', 'Identify processes attempting to capture screenshots or access browser credential databases.'], 'External scanning': ['Detect unusual outbound traffic patterns, especially to known malicious domains or IPs.', 'Look for the presence of hardcoded credentials or PDB paths in executable files.']} 

 IoCs: ['Discord webhook URL: hxxps[:]//discord[.]com/api/webhooks/1123664977618817094/La_3GaXooH42oGRiy8o7sazh1Cg0V_mzkH67VryfSB1MCOlYee1_JPMCNsfOTji7J9jO', 'PDB Path: C:\\Users\\roman\\OneDrive\\Рабочий стол\\straler\\net452\\new_game.pdb', 'PDB Path: D:\\C# proect\\Sapphire\\obj\\Debug\\Sapphire.pdb', 'Sample URL: Various hosting URLs listed in the blog'] 

 Note: *These IoCs should be monitored and cross-referenced with internal logs and threat intelligence feeds to identify potential compromises. SapphireStealer is written entirely in C# and supports stealing logs from Chromium browsers* (https://github.com/0day2/SapphireStealer/). *Cisco Talos has observed increasing use of open-source infostealers like SapphireStealer across public malware repositories and underground forums* (https://malware.news/t/new-open-source-infostealer-and-reflections-on-2023-so-far/73009). 


# Related articles (describing the same threat) 
['https://blog.talosintelligence.com/sapphirestealer-goes-open-source/', 'https://github.com/0day2/SapphireStealer/', 'https://www.pcrisk.com/removal-guides/27668-sapphirestealer-malware', 'https://malware.news/t/new-open-source-infostealer-and-reflections-on-2023-so-far/73009']
