Source: [https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html](https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html)

# Black Basta-Affiliated Water Curupira’s Pikabot Spam Campaign

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Pikabot Spam Campaign 

 Root cause: The root cause involves phishing emails with malicious attachments (ZIP files or PDFs) containing obfuscated JavaScript or IMG files with DLL payloads. The payload (Pikabot) and DarkGate malware enable unauthorized remote access and command execution via a command-and-control (C&C) server. Pikabot employs advanced anti-analysis techniques including dynamic API resolution and indirect syscalls. *Pikabot infections have facilitated the dissemination of post-exploitation tools such as Cobalt Strike* (https://flashpoint.io/blog/emerging-threat-pikabot-malware/). *The malware checks the system's language and halts execution if Russian or Ukrainian* (https://thehackernews.com/2024/01/alert-water-curupira-hackers-actively.html). *Infections often start with email thread hijacking* (https://darktrace.com/blog/pikabot-malware-battling-a-fast-moving-loader-malware-in-the-wild). 

 Threat Actor/group/campaign: Water Curupira (affiliated with Black Basta ransomware) distributed by TA577. *TA571 also observed delivering QakBot* (https://thehackernews.com/2024/01/alert-water-curupira-hackers-actively.html). 

 Organization/industry/location: Various organizations targeted through phishing campaigns using hijacked email threads, no specific organization or industry mentioned. 

 Start date – End date: Q1 2023, paused end of June 2023, resumed September 2023, active as of Q4 2023. *Increase in phishing campaigns post-QakBot takedown in August* (https://thehackernews.com/2024/01/alert-water-curupira-hackers-actively.html). 

 MITRE TTPs: ['Initial Access (T1566.001): Spearphishing Attachment', 'Execution (T1204.002): User Execution: Malicious File', 'Defense Evasion (T1027): Obfuscated Files or Information', 'Command and Control (T1071.001): Application Layer Protocol: Web Protocols', 'Collection (T1056.004): Keylogging', 'Exfiltration (T1041): Exfiltration Over C2 Channel'] 

 Impact: Extensive phishing campaigns leading to potential unauthorized access, data exfiltration, and possible deployment of ransomware (Black Basta). Due to loader capabilities, victims are at risk of more sophisticated threats like reconnaissance malware and ransomware. *DarkGate spam campaigns and a few IcedID campaigns were conducted during early Q3 2023* (https://thehackernews.com/2024/01/alert-water-curupira-hackers-actively.html). *In October 2023, Darktrace detected a Pikabot campaign targeting European customers* (https://darktrace.com/blog/pikabot-malware-battling-a-fast-moving-loader-malware-in-the-wild). 

 Mitigation: {'Secure Email Practices': 'Educate users to hover over links to verify URLs. Verify sender identities and legitimacy of email content. Avoid opening attachments from unknown or suspicious emails.', 'System Hardening': 'Regularly update operating systems and software with the latest patches. Implement robust email filtering solutions to block phishing emails.', 'Data Backup': 'Regularly back up important data to secure, offline locations.', 'Security Solutions': 'Use multilayered security solutions like Trend Vision One for behavior detection. Deploy endpoint protection solutions like Trend Micro Apex One for advanced threat detection and response. Use email security solutions like Trend Micro Deep Discovery Email Inspector to block malicious emails.'} 

 Detection Signature: {'Service': 'Email Service', 'Port': 'N/A (Email-based)', 'Severity': 'Critical', 'Incident': 'Pikabot Spam Campaign', 'Signature name': '“Malicious Email Attachment”', 'Internal checks': {'Setting1': 'Emails with attachments should be scanned for malicious content. – Email Gateway', 'Setting2': 'Block emails with executable attachments from unknown senders. – Email Gateway', 'Setting3': 'Implement sandboxing for email attachments. – Email Gateway'}, 'External scanning': 'Scan incoming emails for known malicious indicators. Monitor for suspicious email patterns and high-volume phishing attacks.'} 

 IoCs: {'Malicious URLs and IP addresses associated with C&C servers': ['70[.]34[.]209[.]101:13720', '137[.]220[.]55[.]190:2223', '139[.]180[.]216[.]25:2967', '154[.]61[.]75[.]156:2078', '154[.]92[.]19[.]139:2222', '158[.]247[.]253[.]155:2225', '172[.]233[.]156[.]100:13721']} 

 Additional Malware Delivery Mechanisms: The phishing campaign also utilizes JS Droppers, Excel-DNA Loader, VBS Downloaders, and LNK Downloaders for distributing malware payloads. Pikabot is also spread via malvertising and OneNote files. *Additional infection methods include .HTA files, .XLL files, and Windows Script Files* (https://flashpoint.io/blog/emerging-threat-pikabot-malware/). *In some cases, cURL was used for the initial payload download* (https://darktrace.com/blog/pikabot-malware-battling-a-fast-moving-loader-malware-in-the-wild). 


# Related articles (describing the same threat) 
['https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html', 'https://cofense.com/blog/are-darkgate-and-pikabot-the-new-qakbot/', 'https://blog.sekoia.io/pikabot-a-guide-to-its-deep-secrets-and-operations/', 'https://flashpoint.io/blog/emerging-threat-pikabot-malware/', 'https://thehackernews.com/2024/01/alert-water-curupira-hackers-actively.html', 'https://darktrace.com/blog/pikabot-malware-battling-a-fast-moving-loader-malware-in-the-wild']
