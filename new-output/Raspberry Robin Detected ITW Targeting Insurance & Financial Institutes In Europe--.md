Source: [https://www.securityjoes.com/post/raspberry-robin-detected-itw-targeting-insurance-financial-institutes-in-europe](https://www.securityjoes.com/post/raspberry-robin-detected-itw-targeting-insurance-financial-institutes-in-europe)

# Raspberry Robin Detected ITW Targeting Insurance & Financial Institutes In Europe

# Enriched Doc (enrihcments marked with *content*(link))

Incident: Raspberry Robin Detected ITW Targeting Insurance & Financial Institutes In Europe

Root cause: The primary root cause behind the incident is the use of a compromised QNAP server as a Command and Control (C2) server. The server hosted malicious payloads, including a *malicious DLL* (https://malpedia.caad.fkie.fraunhofer.de/details/win.raspberry_robin), and facilitated communication with infected machines. The infection method involved ZIP files, MSI installers, JScript encoded droppers, and *external drives* (https://malpedia.caad.fkie.fraunhofer.de/details/win.raspberry_robin), indicating the exploitation of user trust and social engineering. *Security Joes found a highly obfuscated variant targeting financial and insurance services, involving a 7-Zip file containing an MSI installer and RC4 encrypted payload* (https://cyware.com/news/raspberry-robin-upgrades-to-target-financial-and-insurance-services-in-europe-412cad2e). Attackers leveraged trusted cloud infrastructures like *Discord, Azure, and Github* to host malicious content and evade detection *Your changes* (https://www.cyberthreat.report/tag/eng/).

Threat Actor/group/campaign: Raspberry Robin framework, also known as *QNAP-Worm* or *LINK_MSIEXEC* (https://malpedia.caad.fkie.fraunhofer.de/details/win.raspberry_robin), is linked to the attack. Specific threat actors include DEV-0950, DEV-0243, and DEV-0651 *Your changes* (https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/).

Organization/industry/location: The targeted victims are insurance and financial institutions in Europe, focusing on Spanish and Portuguese-speaking organizations.

Start date - End date: Not explicitly mentioned. However, researchers responded to similar incidents twice in January 2023.

MITRE TTPs: ["Execution: T1059.001 (PowerShell)", "Persistence: T1053.005 (Scheduled Task/Job: Scheduled Task)", "Privilege Escalation: T1068 (Exploitation for Privilege Escalation)", "Defense Evasion: T1027 (Obfuscated Files or Information)", "Command and Control: T1071.001 (Web Protocols)", "Exfiltration: T1041 (Exfiltration Over C2 Channel)"]

Impact: The framework allows attackers to collect extensive machine data and exfiltrate it, leading to significant financial and reputational impacts. The activity has evolved to include pre-ransomware stages and Clop ransomware deployment *Your changes* (https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/). Post-infection capabilities enable lateral movement within networks, increasing the risk *Your changes* (https://www.cyberthreat.report/tag/eng/).

Mitigation: ["Secure QNAP servers by updating firmware and applying security patches.", "Implement multi-factor authentication (MFA) for access to network resources.", "Use advanced threat detection mechanisms to monitor for unusual activity such as the execution of unknown DLLs or unauthorized registry changes.", "Train employees to recognize phishing attempts and avoid downloading files from untrusted sources.", "Regularly back up crucial data and ensure the backups are secure and isolated from the main network."]

Detection Signature: {"Service": "QNAP NAS", "Port": 8080, "Severity": "Critical", "Incident": "Raspberry Robin", "Signature name": "QNAP NAS publicly accessible", "Internal checks": ["Setting1: QNAP port (8080) should not be exposed on the external Internet.", "Setting2: QNAP port (8080) should not listen on the external Internet.", "Setting3: QNAP server should secure with authentication credentials."], "External scanning": ["Port (8080) open", "Publicly accessible QNAP NAS"]},

IoCs: ["IP Address: 85.56.236[.]45 (Compromised QNAP server hosting the C2)", "File Hashes: 9c9426776b62a4461b7a9237a971fb3c5fc3222acd303506a763aa1d314a1573 (Malicious MSI installer)", "b11805162d3ae3d3c6635c240d004d1fe942a9cde25fb701c92a8e135d37d100 (ZIP dropped by the malicious advertisement campaign)", "ac7d57c011c1bf1b3158a64d4c91e1d5c54e8d05cdeb9d1fadcbb0c4d5103428 (Unpacked.bin)", "21122891977d9296eea86a8a292b2ba7677766a2085566a6e93ecf60f0ac6ee5 (JScript Encoded Dropper)", "URLs: hxxps://eu.adbison-redirect[.]com/click?payload= (Malicious advertisement redirector)", "hxxps://cdn.discordapp[.]com/attachments/ /File_Part.1.ZIP (Abused discord-related domain)"], "YARA rule provided in the original document for detecting Raspberry Robin shellcode.": "New Document Link: https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/"


# Related articles (describing the same threat):
['https://www.securityjoes.com/post/raspberry-robin-detected-itw-targeting-insurance-financial-institutes-in-europe', 'https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/', 'https://malpedia.caad.fkie.fraunhofer.de/details/win.raspberry_robin', 'https://cyware.com/news/raspberry-robin-upgrades-to-target-financial-and-insurance-services-in-europe-412cad2e', 'https://www.cyberthreat.report/tag/eng/']
