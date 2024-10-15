Source: [https://blog.google/threat-analysis-group/ukraine-remains-russias-biggest-cyber-focus-in-2023/](https://blog.google/threat-analysis-group/ukraine-remains-russias-biggest-cyber-focus-in-2023/)

# Ukraine Remains Russia’s Biggest Cyber Focus in 2023

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Ukraine remains Russia’s biggest cyber focus in 2023 

 Root cause: The incidents described in the blog primarily revolve around multiple types of phishing attacks, exploitation of vulnerabilities in EXIM mail servers, and the use of reflected cross-site scripting (XSS) on Ukrainian government websites. These point towards misconfigured or vulnerable services such as EXIM mail servers and web applications not properly handling XSS vulnerabilities. *APT44 has been involved in nearly all disruptive operations against Ukraine in the past decade* (https://nsarchive.gwu.edu/media/32139/ocr). 

 Threat Actor/group/campaign: FROZENBARENTS (aka Sandworm), a group attributed to Russian Armed Forces’ Main Directorate of the General Staff (GRU) Unit 74455; FROZENLAKE (aka APT28); PUSHCHA (Belarusian threat actor); Internet Research Agency (IRA); Cuba Ransomware/RomCom. *APT44 (aka Sandworm, Seashell Blizzard)* (https://nsarchive.gwu.edu/media/32139/ocr). 

 Organization/industry/location: The targeted sectors include government, defense, energy, transportation/logistics, education, and humanitarian organizations in Ukraine and Europe. *APT44 operations have global scope, targeting North America, Europe, the Middle East, Central Asia, and Latin America* (https://nsarchive.gwu.edu/media/32139/ocr). 

 Start date – End date: January - March 2023 

 MITRE TTPs: ['T1193: Spear Phishing Attachment', 'T1071: Application Layer Protocol', 'T1200: Hardware Additions', 'T1190: Exploit Public-Facing Application', 'T1496: Resource Hijacking', 'T1566: Phishing', 'T1195: Supply Chain Compromise', '*T1078: Valid Accounts* (https://nsarchive.gwu.edu/media/32139/ocr)'] 

 Impact: Although the exact number of records leaked or financial losses is not stated, the incidents involved the exfiltration of credentials, data breaches, and the dissemination of stolen information. *APT44 has also attempted to interfere with democratic processes by leaking politically sensitive information* (https://nsarchive.gwu.edu/media/32139/ocr). 

 Mitigation: ['Secure EXIM mail servers by ensuring they are updated to the latest versions and properly configured.', 'Implement multi-factor authentication (MFA) to protect against credential phishing.', 'Regularly audit and apply security patches to web applications to prevent XSS vulnerabilities.', 'Use web application firewalls (WAFs) to detect and block malicious traffic.', 'Monitor and restrict access to critical systems based on the principle of least privilege.', 'Educate users on recognizing phishing attempts and safe browsing practices.', '*Employ endpoint detection and response (EDR) solutions to detect and mitigate lateral movement techniques used by APT44* (https://nsarchive.gwu.edu/media/32139/ocr).'] 

 Detailed Steps for mitigation: ['Update and configure EXIM mail servers correctly.', 'Implement MFA across all user accounts.', 'Regularly scan web applications for vulnerabilities and apply patches.', 'Deploy WAFs to block XSS and other web-based attacks.', 'Conduct regular security awareness training for employees.', 'Enable and monitor logging to detect unusual access patterns or data exfiltration activities.', '*Deploy EDR solutions to monitor and respond to lateral movement* (https://nsarchive.gwu.edu/media/32139/ocr).'] 

 Detection Signature: {'Service': 'EXIM Mail Server', 'Port': '25, 587', 'Severity': 'Critical', 'Incident': 'EXIM mail server exploitation', 'Signature name': '“EXIM exploit detection”', 'Internal checks': ['Verify EXIM version (should be the latest)', 'Ensure EXIM configurations align with security best practices'], 'External scanning': ['Open EXIM ports', 'Detection of known exploit payloads targeting EXIM vulnerabilities']} 

 IoCs: ['cpcpipe[.]com', 'cpcpipe[.]org', '104.156.149[.]126', 'c80656fe59bdeb3e701d1f7eeaaba2ef673368b2c4947945f598e3e84a6cb7f8', 'telegram.org.security.ohsxy[.]com', 'telegram.org.4234e8234ad0f.24o1[.]com', 'ukroboronprom.com.ukr[.]pm', '181.119.30[.]71', '45.76.31[.]101', '45.56.93[.]83', '45.124.86[.]84', 'https://t.me/s/bio_genie', 'https://biogenie.substack.com', 'setnewcreds.ukr.net[.]frge[.]io', 'ukrprivatesite.frge[.]io', 'robot-876.frge[.]io', '85.240.182[.]23', '68.76.150[.]97', 'passport-ua[.]site', 'passport-log[.]online', 'meta-l[.]space', 'support@passport-ua[.]online', 'openai@chatgpt4beta[.]com', 'chatgpt4beta[.]com', 'mod2023@masterofdigital[.]org', 'masterofdigital[.]org', '4f0b12caa97e52f3d2edada9133f2e4a3442953d14c8ed12deb7219c722ea197'] 


# Related articles (describing the same threat) 
['https://blog.google/threat-analysis-group/ukraine-remains-russias-biggest-cyber-focus-in-2023/', 'https://nsarchive.gwu.edu/media/32139/ocr']
