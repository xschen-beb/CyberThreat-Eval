Source: [https://blog.talosintelligence.com/emotet-switches-to-onenote/](https://blog.talosintelligence.com/emotet-switches-to-onenote/)

# Emotet Resumes Spam Operations, Switches to OneNote

# Enriched Doc (enrihcments marked with *content*(link))

Incident: Emotet Resumes Spam Operations 

Root cause: Continued use of malicious email attachments and documents to distribute malware. The threat actors utilized heavily padded Microsoft Word documents and later switched to malicious OneNote documents for evasion. *They employed zip-bombing techniques to evade detection* (https://cyble.com/blog/emotet-strikes-again-resuming-spamming-operations/). *Click-to-run content was hidden in OneNote files* (https://www.esentire.com/blog/pulse-check-on-onenote-for-malware-delivery#:~:text=In%20early%20March%202023%2C%20security,the%20form%20of%20a%20DLL.).

Threat Actor/group/campaign: Emotet malware group *and Qbot Trojan* (https://www.checkpoint.com/press-releases/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/).

Organization/industry/location: Broadly targeted; specific industries or locations were not mentioned. *The campaign affected over 16 countries* (https://cyble.com/blog/emotet-strikes-again-resuming-spamming-operations/). *Top 10 impacted countries include Estonia, Thailand, Guatemala, Israel, Singapore, Turkey, Italy, United Arab Emirates, Ukraine, and Portugal; top targeted industries include E-Commerce, Energy/Utilities, Financial Services, Government, and Healthcare* (https://www.trellix.com/blogs/research/icymi-emotet-reappeared-early-this-year-unfortunately/).

Start date - End date: The campaign resumed on March 7, 2023, and the switch to OneNote documents started on March 16, 2023. *Emotet utilized Epoch4 servers to distribute spam emails* (https://cyble.com/blog/emotet-strikes-again-resuming-spamming-operations/). *VirusTotal submissions peaked in February 2023* (https://www.esentire.com/blog/pulse-check-on-onenote-for-malware-delivery#:~:text=In%20early%20March%202023%2C%20security,the%20form%20of%20a%20DLL.).

MITRE TTPs: ["T1566.001: Phishing: Spearphishing Attachment", "T1204.002: User Execution: Malicious File", "T1059.005: Command and Scripting Interpreter: Visual Basic"]\

Impact: Potentially thousands of users and systems could be impacted globally, given Emotet's historical reach and impact. Exact numbers are not provided. *Emotet can also download payloads like Cobalt Strike* (https://cyble.com/blog/emotet-strikes-again-resuming-spamming-operations/). *Check Point Research reported that the Apache Log4j vulnerability was the most exploited* (https://www.checkpoint.com/press-releases/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/).

Mitigation: ["Implement email filtering solutions to block malicious attachments and links.", "Educate users about the risks of opening unsolicited email attachments.", "Employ endpoint protection solutions that can detect and block malicious scripts and executables.", "Regularly update and patch systems to protect against known vulnerabilities that can be exploited by Emotet.", "*Monitor for Qbot and Ahmyth RAT infections* (https://www.checkpoint.com/press-releases/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/)."]

Detailed Steps for mitigation: ["**Email Filtering**:", "Use email security solutions like Cisco Secure Email to filter out suspicious attachments and links.", "**User Education**:", "Conduct regular training sessions to inform employees about phishing tactics and the importance of not opening unknown attachments.", "**Endpoint Protection**:", "Deploy and maintain endpoint protection systems such as Cisco Secure Endpoint to detect and block malware.", "**System Patching**:", "Regularly apply updates and patches to operating systems and software.", "**Network Segmentation**:", "Implement network segmentation to limit the spread of malware if an endpoint gets infected.", "**Backup Strategies**:", "Maintain regular backups of critical data to ensure recovery in case of an infection."]

Detection Signature: {"Service": "Email Security Gateway", "Severity": "High", "Incident": "Emotet Malware Campaign", "Signature name": "\u201cSuspicious OneNote Attachment\u201d", "Internal checks": ["Monitor for emails with OneNote attachments (.one) containing embedded scripts.", "Use heuristic analysis to detect padded documents that exceed typical file sizes."], "External scanning": ["Monitor for known Emotet distribution URLs.", "Utilize threat intelligence feeds to update detection rules for new Emotet indicators."]}

IoCs: The Indicators of Compromise (IoCs) associated with ongoing Emotet campaigns can be found [here](https://github.com/Cisco-Talos/IOCs/tree/main/2023/03). *Emotet payloads used regsvr32.exe for execution* (https://www.esentire.com/blog/pulse-check-on-onenote-for-malware-delivery#:~:text=In%20early%20March%202023%2C%20security,the%20form%20of%20a%20DLL.).
 

# Related articles (describing the same threat):
['https://blog.talosintelligence.com/emotet-switches-to-onenote/', 'https://cyble.com/blog/emotet-strikes-again-resuming-spamming-operations/', 'https://www.checkpoint.com/press-releases/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/', 'https://www.esentire.com/blog/pulse-check-on-onenote-for-malware-delivery#:~:text=In%20early%20March%202023%2C%20security,the%20form%20of%20a%20DLL.', 'https://www.trellix.com/blogs/research/icymi-emotet-reappeared-early-this-year-unfortunately/']
