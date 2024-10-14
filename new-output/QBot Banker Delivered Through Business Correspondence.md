Source: [https://securelist.com/qbot-banker-business-correspondence/109535/](https://securelist.com/qbot-banker-business-correspondence/109535/)

# QBot Banker Delivered Through Business Correspondence

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: QBot banker delivered through business correspondence 

 Root cause: A social engineering attack leveraging compromised business email correspondence to distribute QBot malware. PDF files with malicious links downloaded a ZIP archive containing a Windows Script File (WSF) with obfuscated JScript, executing a PowerShell command to download and run the QBot DLL. 

 Threat Actor/group/campaign: The specific threat actor behind this campaign is not mentioned, but it involves the distribution of QBot (aka QakBot, QuackBot, and Pinkslipbot) malware. *TA570* (https://www.trellix.com/blogs/research/qakbots-endgame-the-final-move-before-the-takedown/). 

 Organization/industry/location: The attack targeted various users across multiple countries, notably Germany, Argentina, and Italy. *The United States experienced the highest prevalence* (https://www.trellix.com/blogs/research/qakbots-endgame-the-final-move-before-the-takedown/). 

 Start date – End date: The attack began in early April 2023, with significant activity spikes on April 4, April 5, April 6, and April 12. *A seven-fold increase in detections was noticed from January to June 2023* (https://www.trellix.com/blogs/research/qakbots-endgame-the-final-move-before-the-takedown/). 

 MITRE TTPs: ['T1071.001: Application Layer Protocol - Web Protocols', 'T1059.001: Command and Scripting Interpreter - PowerShell', 'T1027: Obfuscated Files or Information', 'T1204.002: User Execution - Malicious File'] 

 Impact: Approximately 4,500 malicious emails were detected in multiple waves, potentially impacting thousands of users. 

 Mitigation: ['Strengthen email security by using advanced email filtering and anti-phishing solutions.', 'Educate employees about the risks of opening attachments or clicking on links in unsolicited emails.', 'Implement multi-layered security solutions that include behavior-based detection for email attachments and scripts.', 'Regularly update and patch all software and systems to prevent exploitation of vulnerabilities.', 'Use PowerShell logging to monitor and detect suspicious activity.', 'Detailed Steps for mitigation: 1. Deploy email security solutions that can scan for and block malicious attachments and links. 2. Conduct regular security awareness training for employees to recognize phishing attempts. 3. Enable PowerShell script block logging and monitor logs for suspicious activity. 4. Employ endpoint detection and response (EDR) solutions to detect and mitigate threats in real-time. 5. Regularly back up important data and ensure backups are stored securely offline.'] 

 Detection Signature: Service: Email filtering/PowerShell Port: N/A Severity: Critical Incident: QBot Signature name: “QBot Email Campaign” Internal checks: - Setting1: Monitor and filter inbound emails for known QBot indicators (e.g., specific MD5 hashes, malicious URLs). - Setting2: Monitor PowerShell logs for Base64 encoded commands and attempts to download files from the internet. - Setting3: Implement JScript and PowerShell script block logging and review logs for suspicious activity. External scanning: - Monitor for known malicious URLs used in the QBot campaign. - Check for emails containing known QBot-related indicators such as specific MD5 hashes of attachments. 

 IoCs: ['MD5 hashes: - PDF files: 253E43124F66F4FAF23F9671BBBA3D98, 39FD8E69EB4CA6DA43B3BE015C2D8B7D - ZIP archives: 299FC65A2EECF5B9EF06F167575CC9E2, A6120562EB673552A61F7EEB577C05F8 - WSF files: 1FBFE5C1CD26C536FC87C46B46DB754D, FD57B3C5D73A4ECD03DF67BA2E48F661 - DLL: 28C25753F1ECD5C47D316394C7FCEDE2 - Malicious links: - cica.com[.]co/stai/stai.php - abhishekmeena[.]in/ducs/ducs.php - rosewoodlaminates[.]com/hea/yWY9SJ4VOH - agtendelperu[.]com/FPu0Fa/EpN5Xvh - capitalperurrhh[.]com/vQ1iQg/u6oL8xlJ - centerkick[.]com/IC5EQ8/2v6u6vKQwk8 - chimpcity[.]com/h7e/p5FuepRZjx - graficalevi.com[.]br/0p6P/R94icuyQ - kmphi[.]com/FWovmB/8oZ0BOV5HqEX - propertynear.co[.]uk/QyYWyp/XRgRWEdFv - theshirtsummit[.]com/MwBGSm/lGP5mGh'] 

 Additional Info: QBot has capabilities like virtual environment detection, credential dumping, email stealing, and can deploy additional threats like ProLock ransomware *The changes* (https://securelist.com/qakbot-technical-analysis/103931/). *On August 25, 2023, the FBI and international partners executed a coordinated operation to disrupt QakBot infrastructure. This resulted in a botnet takeover, severing connections between victim computers and QakBot C2 servers.* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-242a). *The operation, named 'DuckHunt,' was led by the Justice Department and the FBI* (https://www.trellix.com/blogs/research/qakbots-endgame-the-final-move-before-the-takedown/). 


# Related articles (describing the same threat) 
['https://securelist.com/qbot-banker-business-correspondence/109535/', 'https://securelist.com/qakbot-technical-analysis/103931/', 'https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-242a', 'https://www.trellix.com/blogs/research/qakbots-endgame-the-final-move-before-the-takedown/']
