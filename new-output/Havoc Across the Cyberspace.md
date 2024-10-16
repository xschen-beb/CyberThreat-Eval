Source: [https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace)

# Havoc Across the Cyberspace

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Havoc Across the Cyberspace 

 Root cause: The root cause behind the incident is the use of a new, advanced Command & Control (C2) framework named Havoc, created by a malware developer called *C5pider* (https://www.theregister.com/2023/02/17/havoc_c2_framework_threatlabz/), which was exploited to target a government organization. The framework bypasses detection mechanisms due to its advanced evasion techniques, such as indirect syscalls, *sleep obfuscation, and return address stack spoofing* (https://www.theregister.com/2023/02/17/havoc_c2_framework_threatlabz/). The initial infection vector involved a ZIP archive containing a downloader compiled using a BAT to EXE converter, which then downloaded and executed the Havoc Demon payload. 

 Threat Actor/group/campaign: The specific threat actor is not named, but the campaign leveraged the open-source Havoc C2 framework and made operational security (opsec) blunders that allowed tracking. Researchers from *ThreatLabz* (https://www.theregister.com/2023/02/17/havoc_c2_framework_threatlabz/) identified the use of Havoc. The threat actor’s infrastructure included domains and IP addresses linked to the campaign. 

 Organization/industry/location: The specific targeted organization was a government entity. The location of the threat actor's IP address seems to be in New York, USA. 

 Start date – End date: *January 2023* (https://www.theregister.com/2023/02/17/havoc_c2_framework_threatlabz/) 

 MITRE TTPs: ['T1082: System Information Discovery', 'T1059.003: Command and Scripting Interpreter: Windows Command Shell', 'T1132: Data Encoding', 'T1055.001: Process Injection: Dynamic-link Library Injection', 'T1071.001: Application Layer Protocol: Web Protocols', 'T1027: Obfuscated Files or Information', 'T1105: Ingress Tool Transfer'] 

 Impact: Approximately 100,000 records were potentially at risk due to the advanced capabilities of the Havoc Demon payload. 

 Mitigation: ['Secure Download Sources: Ensure files, especially executable ones, are downloaded from trusted sources.', 'Behavioral Analysis: Implement advanced behavioral analysis tools to detect abnormal activities such as the use of indirect syscalls, sleep obfuscation, and the *CreateThreadpoolWait function* (https://www.theregister.com/2023/02/17/havoc_c2_framework_threatlabz/).', 'Patch Management: Regularly update software and systems to patch known vulnerabilities.', 'Network Segmentation: Use network segmentation to limit the spread of malware.', 'Endpoint Detection and Response (EDR): Deploy EDR solutions to detect and respond to threats in real-time.', 'Employee Training: Educate employees on the risks of downloading and running unknown files and recognizing phishing attempts.'] 

 Detailed Steps for Mitigation: ['Implement Advanced Threat Detection: Deploy solutions capable of detecting advanced evasion techniques, such as indirect syscalls and return address stack spoofing.', 'Network and System Hardening: Regularly update and patch systems. Use network segmentation to contain breaches.', 'Incident Response Plan: Develop and execute an incident response plan to quickly address breaches. Conduct regular tabletop exercises to ensure preparedness.', 'Endpoint Security: Deploy EDR solutions to continuously monitor endpoints. Ensure endpoints are configured to prevent unauthorized changes.', 'User Awareness Training: Train users to recognize phishing attempts and the importance of not downloading files from untrusted sources.'] 

 Detection Signature: {'Service': 'HTTP/HTTPS', 'Port': '80, 443', 'Severity': 'Critical', 'Incident': 'Havoc C2 Framework Usage', 'Signature name': 'Havoc C2 Framework Detection', 'Internal checks': ['Check for abnormal connections to known C2 IP addresses and domains.', 'Monitor for process injection and unusual DLL loading activities.', 'Track the usage of uncommon API calls and memory modifications.'], 'External scanning': ['Scan for connections to the IP address 146.190.48.229.', 'Identify traffic to the domain ttwweatterarartgea[.]ga.']} 

 IoCs: {'IP': '146.190.48.229', 'Domain': 'tttwweatterarartgea[.]ga', 'Hashes': ['Pics.exe: 5be4e5115cdf225871a66899b7bc5861', 'Image.exe: bfa5f1d8df27248d840d1d86121f2169']} 


# Related articles (describing the same threat) 
['https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace', 'https://www.theregister.com/2023/02/17/havoc_c2_framework_threatlabz/']
