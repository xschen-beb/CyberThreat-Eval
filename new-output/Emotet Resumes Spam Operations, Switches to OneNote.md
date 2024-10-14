Source: [https://blog.talosintelligence.com/emotet-switches-to-onenote/](https://blog.talosintelligence.com/emotet-switches-to-onenote/)

# Emotet Resumes Spam Operations, Switches to OneNote

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Emotet Resumes Spam Operations 

 Root cause: The root cause behind the incident is the use of malicious OneNote documents and heavily padded Microsoft Word documents containing macros and scripts. The vulnerability exploited is the lack of proper email filtering and endpoint protection to detect these malicious attachments. *Healthcare Sector* (https://www.hhs.gov/sites/default/files/emotet-the-enduring-and-persistent-threat-to-the-hph-tlpclear.pdf). 

 Threat Actor/group/campaign: Emotet Botnet, *GOLD CABIN*, *MUMMY SPIDER* (https://malpedia.caad.fkie.fraunhofer.de/details/win.emotet) 

 Organization/industry/location: General targets (not specified), potentially multiple industries and locations due to the widespread nature of Emotet campaigns. *HPH Sector (Healthcare and Public Health)* (https://www.hhs.gov/sites/default/files/emotet-the-enduring-and-persistent-threat-to-the-hph-tlpclear.pdf). 

 Start date – End date: March 7, 2023 – Ongoing (as of the latest update on March 22, 2023) 

 MITRE TTPs: ['T1193 - Spear Phishing Attachment', 'T1204.002 - User Execution: Malicious File', 'T1071.001 - Application Layer Protocol: Web Protocols'] 

 Impact: The exact number of devices or financial losses is not specified, but Emotet campaigns typically aim to infect as many systems as possible, leading to significant network disruptions and potential data breaches. *Credential Theft and Data Exfiltration* (https://www.hhs.gov/sites/default/files/emotet-the-enduring-and-persistent-threat-to-the-hph-tlpclear.pdf). 

 Mitigation: {'Email Filtering': 'Implement advanced email filtering to block suspicious attachments and links.', 'Endpoint Protection': 'Use endpoint protection solutions that can detect and block macro-based malware and malicious scripts.', 'User Training': 'Conduct regular training sessions to educate users on recognizing phishing emails and suspicious attachments.', 'Macro Settings': 'Disable macros by default in Microsoft Office applications and enforce strict policies on the use of macros.', 'Network Segmentation': 'Segment the network to limit the spread of malware.', 'Regular Updates': 'Ensure all systems and software are regularly updated with the latest security patches.'} 

 Detailed Steps for Mitigation: ['Configure Email Gateways: Block emails with executable content inside attachments (e.g., .js, .vbs, .wsf).', 'Deploy Advanced Threat Protection: Use solutions like Cisco Secure Endpoint, Cisco Secure Email, and Cisco Secure Firewall.', 'Implement Policies: Use Group Policy Objects (GPO) to disable macros in Office files received from the internet.', 'User Awareness Training: Regularly simulate phishing attacks to train employees on identifying suspicious emails.', 'Monitor Network Traffic: Use tools like Cisco Secure Network Analytics to identify unusual network activities.'] 

 Detection Signature: {'Service': 'Email servers (e.g., Microsoft Exchange)', 'Port': 'Varies (typically 25, 465, 587 for SMTP)', 'Severity': 'Critical', 'Incident': 'Emotet Resumes Spam Operations', 'Signature name': 'Emotet Phishing Email with OneNote/Word Attachment', 'Internal checks': ['Setting1: Scan incoming emails for known Emotet IOCs.', 'Setting2: Block emails with attachments of specific file types (e.g., .one, .docm).', 'Setting3: Monitor for execution of macros and scripts from Office documents.'], 'External scanning': ['Monitor email server logs for indicators of Emotet-related email patterns.', 'Use IDS/IPS to detect malicious VBA macro execution and script downloads.']} 

 IoCs: {'Indicators of Compromise (IOCs) associated with ongoing Emotet campaigns can be found [here](https://github.com/Cisco-Talos/IOCs/tree/main/2023/03).': 'No specific IoCs found in the provided document text itself.'} 

 Additional Information: Emotet, historically a banking malware, has evolved to serve as infrastructure for distributing other malware like *Trickbot* and facilitating *Ryuk ransomware* attacks (https://malpedia.caad.fkie.fraunhofer.de/details/win.emotet). Emotet's new campaign bypasses Microsoft's macro block by sending spam emails with malicious OneNote files containing a fake message to trick victims into downloading the malware. Once installed, it gathers email data for expanding the attack campaign. *Qbot as prevalent malware* (https://blog.checkpoint.com/security/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/). *VirusTotal spike observed*; *Payload Obfuscation*; *URLs for Emotet payloads* (https://www.esentire.com/blog/pulse-check-on-onenote-for-malware-delivery). 


# Related articles (describing the same threat) 
['https://blog.talosintelligence.com/emotet-switches-to-onenote/', 'https://www.hhs.gov/sites/default/files/emotet-the-enduring-and-persistent-threat-to-the-hph-tlpclear.pdf', 'https://malpedia.caad.fkie.fraunhofer.de/details/win.emotet', 'https://blog.checkpoint.com/security/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/', 'https://www.esentire.com/blog/pulse-check-on-onenote-for-malware-delivery']
