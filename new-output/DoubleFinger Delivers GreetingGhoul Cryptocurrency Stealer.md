Source: [https://securelist.com/doublefinger-loader-delivering-greetingghoul-cryptocurrency-stealer/109982/](https://securelist.com/doublefinger-loader-delivering-greetingghoul-cryptocurrency-stealer/109982/)

# DoubleFinger Delivers GreetingGhoul Cryptocurrency Stealer

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: DoubleFinger delivers GreetingGhoul cryptocurrency stealer 

 Root cause: The root cause includes the use of a multi-stage loader (DoubleFinger) utilizing steganography, DLL sideloading, and encrypted components from Imgur to execute a cryptocurrency stealer (GreetingGhoul). The initial infection vector is a malicious PIF attachment in an email, leading to a modified binary that downloads and decrypts payloads, employing the Doppelgänging technique to bypass security measures and install the GreetingGhoul crypto stealer. *The DoubleFinger loader also hides the styler in PNG files and replaces the cryptocurrency wallet interface* (https://tadviser.com/index.php/Article:Malware_(malware)). 

 Threat Actor/group/campaign: The campaign shows signs of being conducted by Russian-speaking cybercriminals, though the exact threat actor or group is not mentioned. 

 Organization/industry/location: Victims are in Europe, the USA, and Latin America. *In Russia, the Loki virus, associated with the Mythic framework, has been spreading through targeted attacks on engineering and medical companies* (https://tadviser.com/index.php/Article:Malware_(malware)). 

 Start date – End date: Not specified. 

 MITRE TTPs: ['T1059: Command and Scripting Interpreter', 'T1071: Application Layer Protocol', 'T1110: Brute Force', 'T1127: Trusted Developer Utilities Proxy Execution', 'T1203: Exploitation for Client Execution', 'T1566: Phishing', 'T1027: Obfuscated Files or Information', 'T1070: Indicator Removal on Host'] 

 Impact: The impact includes the theft of cryptocurrency-related credentials, including seed phrases and potentially other sensitive information. The exact number of affected records or financial losses is not specified. *In addition, the Eldorado ransomware, written in Go, has been targeting Windows and VMware ESXi environments* (https://tadviser.com/index.php/Article:Malware_(malware)). 

 Mitigation: ['Educate users about the risks of opening email attachments from unknown sources.', 'Implement email filtering solutions to detect and block email-based threats.', 'Use endpoint protection solutions to detect and block malicious executables and shellcode.', 'Regularly update software and apply patches to mitigate exploitation of known vulnerabilities.', 'Employ network monitoring and intrusion detection systems to identify and respond to suspicious activities.', 'Implement multi-factor authentication for accessing sensitive applications and data.', 'Use secure methods for managing and storing cryptocurrency credentials, avoiding inputting recovery seeds on computers.'] 

 Detailed Steps for mitigation: ['**User Education**: Conduct regular training sessions on email security and phishing awareness.', '**Email Filtering**: Deploy and configure email security gateways to filter out malicious attachments and links.', '**Endpoint Protection**: Install and maintain up-to-date antivirus and anti-malware solutions on all endpoints.', '**Software Updates**: Ensure all operating systems, applications, and software are updated with the latest security patches.', '**Network Monitoring**: Use SIEM (Security Information and Event Management) solutions to monitor network traffic for suspicious activities.', '**Multi-Factor Authentication**: Implement MFA across all critical systems to add an extra layer of security.', '**Cryptocurrency Security**: Use hardware wallets and avoid entering recovery phrases on computers.'] 

 Detection Signature: {'Service': 'Email Security Gateway', 'Port': 'N/A (Email service)', 'Severity': 'Critical', 'Incident': 'DoubleFinger and GreetingGhoul', 'Signature name': 'Malicious PIF Attachment', 'Internal checks': ['Setting1: Email security gateway should scan and filter PIF files – In email security solution.', 'Setting2: Endpoint protection should detect and block modified binaries – Inside endpoint protection solution.'], 'External scanning': ['Detect suspicious email attachments with PIF extensions.', 'Analyze email headers and body for indicators of phishing attempts.']} 

 IoCs: {'Hashes': ['a500d9518bfe0b0d1c7f77343cac68d8', 'dbd0cf87c085150eb0e4a40539390a9a', '56acd988653c0e7c4a5f1302e6c3b1c0', '16203abd150a709c0629a366393994ea', 'd9130cb36f23edf90848ffd73bd4e0e0', '642f192372a4bd4fb3bfa5bae4f8644c', 'a9a5f529bf530d0425e6f04cbe508f1e'], 'Domain': 'cryptohedgefund[.]us'} 


# Related articles (describing the same threat) 
['https://securelist.com/doublefinger-loader-delivering-greetingghoul-cryptocurrency-stealer/109982/', 'https://www.phishprotection.com/phishing-awareness/crypto-wallets-face-advanced-multi-stage-double-finger-threat', 'https://tadviser.com/index.php/Article:Malware_(malware)']
