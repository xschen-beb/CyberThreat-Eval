Source: [https://www.gendigital.com/blog/insights/research/glove-stealer#new_tab](https://www.gendigital.com/blog/insights/research/glove-stealer#new_tab)

## Related articles (describing the same threat) 
- https://www.gendigital.com/blog/insights/research/glove-stealer#new_tab
- https://github.com/avast/ioc/tree/master/GloveStealer
- https://www.securityweek.com/glove-stealer-malware-bypasses-chromes-app-bound-encryption/
- https://www.bleepingcomputer.com/news/security/new-glove-infostealer-malware-bypasses-google-chromes-cookie-encryption/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: Glove Stealer: Leveraging IElevator to Bypass App-Bound Encryption & Steal Sensitive Data 

#### Root cause 
 The root cause behind the incident is the exploitation of a vulnerability in Chrome's App-Bound Encryption using the IElevator service. The malware leverages this to bypass encryption and steal sensitive data from browsers, cryptocurrency wallets, 2FA authenticators, and other applications. *The bypass method was disclosed roughly two weeks ago and relies on the internal COM-based IElevator service unique to each browser to harvest and decrypt the necessary keys* (https://www.securityweek.com/glove-stealer-malware-bypasses-chromes-app-bound-encryption/). *The malware first needs to get local admin privileges on the compromised systems to place this module in Google Chrome's Program Files directory and use it to retrieve encrypted keys* (https://www.bleepingcomputer.com/news/security/new-glove-infostealer-malware-bypasses-google-chromes-cookie-encryption/). 

#### Threat actor/group/campaign 
 The specific threat actor or group behind the Glove Stealer campaign is not mentioned in the blog. *The malware was first spotted by Gen Digital security researchers* (https://www.bleepingcomputer.com/news/security/new-glove-infostealer-malware-bypasses-google-chromes-cookie-encryption/). 

#### Organization/industry/location 
 The blog does not specify a particular organization, industry, or location targeted by the Glove Stealer campaign. 

#### Start date – End date 
 The blog does not provide specific start and end dates for the attack. 

#### MITRE TTPs 
 ['T1071.001: Application Layer Protocol: Web Protocols', 'T1059.001: Command and Scripting Interpreter: PowerShell', 'T1119: Automated Collection', 'T1027: Obfuscated Files or Information', 'T1566.001: Phishing: Spearphishing Attachment', '*T1078: Valid Accounts* (https://www.bleepingcomputer.com/news/security/new-glove-infostealer-malware-bypasses-google-chromes-cookie-encryption/)'] 

#### Impact 
 The impact includes the theft of sensitive data from browsers, cryptocurrency wallets, 2FA authenticators, password managers, and email clients. The exact number of records or financial losses is not specified. *Glove Stealer targets multiple browsers and extensions to exfiltrate sensitive information such as cookies and credentials, along with data from cryptocurrency wallets, authenticators, password managers, email clients, and other applications* (https://www.securityweek.com/glove-stealer-malware-bypasses-chromes-app-bound-encryption/). *It also tries to exfiltrate sensitive information from a list of 280 browser extensions and more than 80 locally installed applications* (https://www.bleepingcomputer.com/news/security/new-glove-infostealer-malware-bypasses-google-chromes-cookie-encryption/). 

#### Mitigation Steps 
 ['Educate users about phishing tactics and the risks of executing unknown scripts.', 'Implement email filtering to block phishing emails.', 'Use endpoint protection solutions to detect and block malicious scripts and executables.', 'Regularly update and patch software to mitigate known vulnerabilities.', 'Implement multi-factor authentication to protect sensitive accounts.', 'Monitor network traffic for unusual activity and potential data exfiltration.'] 

#### Detection Signature 
 {'Service': 'Chrome', 'Port': 'N/A', 'Severity': 'Critical', 'Incident': 'Glove Stealer', 'Signature name': 'Chrome App-Bound Encryption Bypass', 'Internal checks': ['Monitor for the presence of IElevator service usage.', "Check for unauthorized access to Chrome's Local State file.", 'Detect and block execution of unknown .NET executables.'], 'External scanning': ['Monitor for connections to known C&C servers (e.g., master.hdsjfkgsadoghdsiougds.space, master.volt-texs.online).']} 

#### IoCs: 
- hash_sha256: 2bf6fab237ab58ae6cfe78f9a61ab6dcaf55f437cb7a77878e2e6aae3b208e80 ([link](https://github.com/avast/ioc/tree/master/GloveStealer)) 

- hash_sha256: 56da496329d54587c31119d8878a7831a9814a92839aa6a9873ceeb91575b11a ([link](https://github.com/avast/ioc/tree/master/GloveStealer)) 

- hash_sha256: 86ad4082e086a0b9a22dc91a16d0d9be38232975ab4d3d035224fb6d6cc7a44c ([link](https://github.com/avast/ioc/tree/master/GloveStealer)) 

- domain: master.hdsjfkgsadoghdsiougds.space ([link](https://github.com/avast/ioc/tree/master/GloveStealer)) 

- domain: master.volt-texs.online ([link](https://github.com/avast/ioc/tree/master/GloveStealer)) 

- PDB path: C:\Users\Calypso\Desktop\SOURCE\BabyMeloAVBypasser\obj\Debug\RukavicaPlyashet.pdb ([link](https://github.com/avast/ioc/tree/master/GloveStealer)) 

- PDB path: C:\Users\111818\Desktop\DevHelp\CSHR Source\BENZOPILA\Chromiumz\Chromiumz\obj\Debug\Chromiumz.pdb ([link](https://github.com/avast/ioc/tree/master/GloveStealer)) 

- For more IoCs, please refer to the above links. 


