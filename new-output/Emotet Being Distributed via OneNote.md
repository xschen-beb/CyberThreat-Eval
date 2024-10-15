Source: [https://asec.ahnlab.com/en/50564/](https://asec.ahnlab.com/en/50564/)

# Emotet Being Distributed via OneNote

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Emotet Being Distributed via OneNote 

 Root Cause: The root cause behind the incident is the malicious use of OneNote files in spear phishing emails. The OneNote file contains a malicious script (JS file) named `output1.js` that is obfuscated with string replacement techniques and ultimately connects to a Command and Control (C2) server to download and execute Emotet malware via `regsvr32.exe`. Additionally, a .wsf file named `click.wsf` is used, verifying payload size to ensure it exceeds *150 KB* (https://cyble.com/blog/recent-emotet-spam-campaign-utilizing-new-tactics/). When executed, users are prompted to click a *Next button* on the OneNote file to connect to the *cloud for document viewing* (https://asec.ahnlab.com/jp/50546/). The campaign *bypasses Microsoft macro blocks* (https://blog.checkpoint.com/security/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/). *The Emotet campaign is operated by the Mealybug or TA542 group* (https://www.welivesecurity.com/2023/07/06/whats-up-with-emotet/). 

 Threat Actor/Group/Campaign: Likely attributed to the Emotet cybercrime group. 

 Organization/Industry/Location: The report is generalized and does not specify a particular organization, industry, or location as the target. It warns users at large about the threat. 

 Start Date – End Date: The report was published on March 27, 2023. The exact start and end dates of the campaign are not mentioned. The incident was confirmed by *ASEC* on *March 29, 2023* (https://asec.ahnlab.com/jp/50546/). 

 MITRE TTPs: ['T1193: Spear Phishing Attachment', 'T1204: User Execution', 'T1059: Command and Scripting Interpreter', 'T1071: Application Layer Protocol'] 

 Impact: Users who run the malicious OneNote file may have their systems compromised by Emotet malware, potentially leading to data theft, further malware infections, and network propagation. The malware can *gather user email data* such as login credentials and contact information *The changes* (https://blog.checkpoint.com/security/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/). *It can deploy modules like Thunderbird Email Stealer, Thunderbird Contact Stealer, and Google Chrome Credit Card Stealer to exfiltrate sensitive information* (https://www.welivesecurity.com/2023/07/06/whats-up-with-emotet/). 

 Mitigation: {'User Education and Awareness': ['Educate users on the risks of opening email attachments from unknown or untrusted sources.', 'Conduct regular phishing awareness training and simulations.'], 'Email Security': ['Implement advanced email filtering solutions to detect and block spear phishing emails.', 'Use email authentication mechanisms like SPF, DKIM, and DMARC to prevent spoofing.'], 'Endpoint Protection': ['Deploy and maintain updated endpoint protection solutions that can detect and block malicious scripts and executables.', 'Implement behavioral analysis tools to identify unusual activities like the execution of `regsvr32.exe` from unexpected locations.'], 'Network Security': ['Monitor network traffic for unusual outbound connections to known C2 servers.', 'Implement network segmentation to limit the spread of malware.'], 'Patching and Updates': ['Regularly update software, operating systems, and applications to mitigate vulnerabilities.']} 

 Detailed Steps for Mitigation: ['Email Security Configuration: Ensure email security solutions are configured to scan attachments and block known malicious file types (e.g., .js, .exe) from unknown sources.', 'Endpoint Security Policies: Configure endpoint security policies to restrict the execution of scripts from email attachments unless explicitly allowed.', 'Network Monitoring: Set up alerts for suspicious outbound traffic patterns, particularly to known malicious IPs or domains associated with Emotet.'] 

 Detection Signature: {'Service': 'Email Gateway, Endpoint Security', 'Port': 'Not applicable', 'Severity': 'Critical', 'Incident': 'Emotet via OneNote', 'Signature Name': 'Emotet OneNote Phishing', 'Internal Checks': ['Setting1: Email gateway rules to block or quarantine emails with OneNote attachments from untrusted sources.', 'Setting2: Endpoint security rules to detect and block the execution of scripts from email attachments.', 'Setting3: Network monitoring rules for unusual outbound connections to Emotet C2 servers.'], 'External Scanning': ['Scanning for known malicious URLs and IPs associated with Emotet campaigns.', 'Checking for active connections to the listed IoCs.']} 

 IoCs: {'MD5': ['08d40c504500c324b683773b1c6189d9', '27f882a2b795abfae8f33440afcd3ad4', '32ec97bbc9826ee88697362023ba68ed', '50150db8010ddc87150cb8445f45d270', '6c442d3235f3e60f7a9ea3efca0289ab', 'b1a10568aa1e4a47ad2aa35788edc0af', 'ad0358aa96105ca02607a7605f3a1e80', '89457cb5c8b296b5fb9a39218b485e1a', 'c3d33ce14a48096e1cd5ce43fa4e307e'], 'URL': ['http[:]//meteo[.]camera/11/VkU/', 'http[:]//sdspush[.]beget[.]tech/connectors/GDSeP6kcWtck20hVy/', 'http[:]//sipo[.]ru/images/aCyHhlS8n0bXBg4BU/', 'http[:]//www[.]agropuno[.]gob[.]pe/wp-content/f9I32dWeuQcbpRt19mZ7/', 'http[:]//www[.]garrett[.]kz/faq/iSPVXBmuu3nUma5wkdy/']} 

 Detection Names: ['Malware/Win.Generic.C5398625', 'Downloader/JS.Agent', 'Dropper/MSOffice.Generic'] 

 References: ['https://asec.ahnlab.com/ko/50238/', 'https://asec.ahnlab.com/jp/50546/', 'https://blog.checkpoint.com/security/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/', 'https://cyble.com/blog/recent-emotet-spam-campaign-utilizing-new-tactics/', '*https://www.welivesecurity.com/2023/07/06/whats-up-with-emotet/*'] 

 Additional Information: {'Top Malware Families': ['Qbot', 'Emotet', 'FormBook'], 'Top Exploited Vulnerabilities': ['Apache Log4j Remote Code Execution', 'HTTP Headers Remote Code Execution', 'MVPower DVR Remote Code Execution'], 'Top Attacked Industries': ['Education/Research', 'Government/Military', 'Healthcare']} 


# Related articles (describing the same threat) 
['https://asec.ahnlab.com/en/50564/', 'https://asec.ahnlab.com/ko/50238/', 'https://asec.ahnlab.com/jp/50546/', 'https://blog.checkpoint.com/security/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/', 'https://cyble.com/blog/recent-emotet-spam-campaign-utilizing-new-tactics/', 'https://www.welivesecurity.com/2023/07/06/whats-up-with-emotet/']
