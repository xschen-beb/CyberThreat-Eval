Source: [https://www.fortinet.com/blog/threat-research/bandook-persistent-threat-that-keeps-evolving](https://www.fortinet.com/blog/threat-research/bandook-persistent-threat-that-keeps-evolving)

# Bandook - A Persistent Threat That Keeps Evolving

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Bandook - A Persistent Threat That Keeps Evolving 

 Root cause: The successful delivery of Bandook malware through a malicious PDF file containing a shortened URL that downloaded a password-protected .7z file. Upon extraction with the provided password, the malware was injected into `msinfo32.exe`, leveraging registry keys to control its behavior and establish persistence. *Fortinet researchers observed this new variant in October 2023, which includes 139 actions for C2 communications* (https://securityaffairs.com/157065/malware/bandook-rat-targets-windows.html). 

 Threat Actor/group/campaign: Various threat actors over the years have used Bandook malware. Specific threat actors for this incident are not named in the blog. 

 Organization/industry/location: The targeted victims are users of Microsoft Windows, but specific organizations or industries are not mentioned. 

 Start date – End date: The new Bandook variant was identified in October 2023. 

 MITRE TTPs: ['T1193: Spearphishing Attachment', 'T1055: Process Injection', 'T1105: Ingress Tool Transfer', 'T1071: Application Layer Protocol', 'T1083: File and Directory Discovery', 'T1112: Modify Registry', 'T1070: Indicator Removal on Host'] 

 Impact: Remote attackers can gain control of infected systems, perform keylogging, audio capture, video capture, and take screenshots. The financial losses and specific number of affected devices or users are not detailed in the blog. *The changes* (https://www.pcrisk.com/removal-guides/15004-bandook-rat#:~:text=Bandook%20is%20a%20high%2Drisk,to%20a%20number%20of%20issues.) 

 Mitigation: {'Ensure Email Security': ['Implement advanced email filtering solutions to block malicious attachments.', 'Educate users about the risks of opening attachments from unknown sources.'], 'Use Up-to-Date AV Solutions': ['Ensure that antivirus solutions like FortiGuard Antivirus are up-to-date.', 'Utilize FortiGuard AntiVirus engine components in FortiGate, FortiMail, FortiClient, and FortiEDR.'], 'Registry Monitoring': 'Regularly monitor and audit registry keys for unauthorized changes.', 'Endpoint Protection': 'Deploy endpoint detection and response (EDR) solutions to identify and mitigate threats.', 'Content Disarm & Reconstruction (CDR)': 'Use CDR services to disarm malicious macros in documents.', 'Security Awareness Training': 'Conduct regular security awareness training for employees using resources like Fortinet’s NSE training module.'} 

 Detection Signature: {'Service': 'Windows Registry', 'Severity': 'Critical', 'Incident': 'Bandook malware injection', 'Signature name': 'Bandook registry keys', 'Internal checks': ['`HKEY_CURRENT_USER\\Software\\[Bandook-related keys]` should not be present.', 'Monitor for creation of registry keys used for persistence and control codes.'], 'External scanning': 'Monitor network traffic for communication with known Bandook C2 IP addresses.'} 

 IoCs: {'IPs': ['77[.]91[.]100[.]237', '45[.]67[.]34[.]219'], 'Files': ['8904ce99827280e447cb19cf226f814b24b0b4eec18dd758e7fb93476b7bf8b8', 'd3e7b5be903eb9a596b9b2b78e5dd28390c6aadb8bdd4ea1ba3d896d99fa0057', '3169171e671315e18949b2ff334db83f81a3962b8389253561c813f01974670b', 'e87c338d926cc32c966fce2e968cf6a20c088dc6aedf0467224725ce36c9a525', '2e7998a8df9491dad978dee76c63cb1493945b9cf198d856a395ba0fae5c265a', '430b9e91a0936978757eb8c493d06cbd2869f4e332ae00be0b759f2f229ca8ce', 'cd78f0f4869d986cf129a6c108264a3517dbcf16ecfc7c88ff3654a6c9be2bca']} 


# Related articles (describing the same threat) 
['https://www.fortinet.com/blog/threat-research/bandook-persistent-threat-that-keeps-evolving', 'https://www.pcrisk.com/removal-guides/15004-bandook-rat#:~:text=Bandook%20is%20a%20high%2Drisk,to%20a%20number%20of%20issues.', 'https://securityaffairs.com/157065/malware/bandook-rat-targets-windows.html']
