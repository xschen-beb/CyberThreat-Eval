Source: [https://www.securityjoes.com/post/raspberry-robin-detected-itw-targeting-insurance-financial-institutes-in-europe](https://www.securityjoes.com/post/raspberry-robin-detected-itw-targeting-insurance-financial-institutes-in-europe)

# Raspberry Robin Detected ITW Targeting Insurance & Financial Institutes In Europe

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Raspberry Robin Detected ITW Targeting Insurance & Financial Institutes In Europe 

 Root cause: Exploitation of compromised QNAP servers used as Command and Control (C2) servers. 

 Threat Actor/group/campaign: Raspberry Robin; DEV-0243; hacking groups. 

 Organization/industry/location: Insurance and financial institutions in Europe, with a focus on Spanish and Portuguese-speaking organizations. 

 Start date – End date: Not explicitly stated in the blog, but incidents were documented as occurring in the month leading up to January 2023. 

 MITRE TTPs: ['T1082: System Information Discovery', 'T1071.001: Application Layer Protocol: Web Protocols', 'T1105: Ingress Tool Transfer', 'T1203: Exploitation for Client Execution'] 

 Impact: The blog does not specify the exact number of records leaked or the financial losses. 

 Mitigation: ['Monitor and update defense mechanisms to detect and block the Raspberry Robin framework.', 'Ensure proper security controls on QNAP servers, including regular updates and patches.', 'Implement network segmentation to limit the spread of malware.', 'Educate employees on phishing and social engineering tactics to prevent initial infection vectors.', 'Regularly audit and monitor system logs for unusual activities or connections to known malicious IP addresses.'] 

 Detailed Steps for mitigation: ['**Update Security Systems**: Ensure that antivirus and endpoint detection systems are updated with the latest signatures to detect Raspberry Robin.', '**Secure QNAP Servers**: Apply the latest firmware updates, restrict access to the management interface, and disable unnecessary services.', '**Network Segmentation**: Isolate critical systems from general user networks to prevent lateral movement.', '**Employee Training**: Conduct regular training sessions on recognizing phishing attempts and suspicious email attachments.', '**System Audits**: Implement regular audits of system and network logs to identify and respond to abnormal activities promptly.'] 

 Detection Signature: {'Service': 'QNAP NAS', 'Port': '8080', 'Severity': 'Critical', 'Incident': 'Raspberry Robin Campaign', 'Signature name': 'QNAP C2 Server Detection', 'Internal checks': ['Ensure QNAP servers are updated with the latest firmware. – In platform', 'QNAP management interface should not be exposed to the external internet. – Inside VMs', 'Implement strong authentication mechanisms for accessing QNAP devices. – Inside VMs'], 'External scanning': ['Port (8080) open', 'Detect traffic to known C2 IPs, e.g., 85.56.236[.]45']} 

 IoCs: ['IP: 85.56.236[.]45 (Compromised QNAP server hosting the C2)', 'Hashes: 9c9426776b62a4461b7a9237a971fb3c5fc3222acd303506a763aa1d314a1573 (Malicious MSI installer)', 'b11805162d3ae3d3c6635c240d004d1fe942a9cde25fb701c92a8e135d37d100 (ZIP dropped by the malicious advertisement campaign)', 'ac7d57c011c1bf1b3158a64d4c91e1d5c54e8d05cdeb9d1fadcbb0c4d5103428 (Unpacked.bin)', '21122891977d9296eea86a8a292b2ba7677766a2085566a6e93ecf60f0ac6ee5 (JScript Encoded Dropper)'] 

 Additional Details: {'Infection Vectors': ['IcedID; *FakeUpdates* (https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/)', 'rundll32.exe; *fodhelper.exe* (https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/)'], 'Post-Compromise Activities': ['Cobalt Strike; *Clop ransomware* (https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/)'], 'Related Threat Actors': ['DEV-0243; *Truebot* (https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/)']} 


# Related articles (describing the same threat) 
['https://www.securityjoes.com/post/raspberry-robin-detected-itw-targeting-insurance-financial-institutes-in-europe', 'https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/']
