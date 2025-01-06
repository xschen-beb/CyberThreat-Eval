Source: [https://www.proofpoint.com/us/blog/threat-insight/security-brief-clickfix-social-engineering-technique-floods-threat-landscape](https://www.proofpoint.com/us/blog/threat-insight/security-brief-clickfix-social-engineering-technique-floods-threat-landscape)

## Related articles (describing the same threat) 
- https://www.proofpoint.com/us/blog/threat-insight/security-brief-clickfix-social-engineering-technique-floods-threat-landscape
- https://blog.sekoia.io/clickfix-tactic-the-phantom-meet/
- https://krebsonsecurity.com/2024/09/this-windows-powershell-phish-has-scary-potential/
- https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clickfix-deception-a-social-engineering-tactic-to-deploy-malware/
- https://www.infosecurity-magazine.com/news/clickfix-cyber-malware-rise/
- https://www.computing.co.uk/news/2024/security/researchers-report-rise-in-clickfix-social-engineering-attacks
- https://duo.com/decipher/unique-social-engineering-attack-used-to-deliver-infostealers
- https://www.darkreading.com/remote-workforce/cut-paste-tactics-import-malware

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: ClickFix Social Engineering Technique Flood 

#### Root cause 
 The root cause is social engineering attacks luring users into executing PowerShell commands by impersonating legitimate services or software updates. *This includes phishing emails spoofing GitHub that prompt users to execute commands via the Windows Run prompt* (https://krebsonsecurity.com/2024/09/this-windows-powershell-phish-has-scary-potential/). *Proofpoint researchers noted that additional techniques involve HTML attachments in phishing emails that trick users into executing PowerShell scripts leading to malware downloads* (https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clickfix-deception-a-social-engineering-tactic-to-deploy-malware/). *Fake error messages and reCAPTCHA Phish toolkit are also used to trick users into executing malicious scripts*. *These methods prey on users' helpfulness by presenting what seems to be both an error and a solution, leading users to infect themselves* (https://www.infosecurity-magazine.com/news/clickfix-cyber-malware-rise/) *Fake error messages instructing users to copy and paste Base64-encoded PowerShell commands were observed, leading to malware infections* (https://duo.com/decipher/unique-social-engineering-attack-used-to-deliver-infostealers). *The infiltration can lead to data exfiltration, further malware downloads, or propagation of malicious code* (https://www.computing.co.uk/news/2024/security/researchers-report-rise-in-clickfix-social-engineering-attacks). *ClearFake campaigns use fake browser updates and software fixes to deliver malware via EtherHiding on blockchain platforms* (https://www.darkreading.com/remote-workforce/cut-paste-tactics-import-malware). 

#### Threat actor/group/campaign 
 TA571, ClearFake, and several unattributed threat clusters, including suspected espionage-focused groups. *Cybercrime groups such as Slavic Nation Empire (SNE) and Scamquerteo Team* (https://blog.sekoia.io/clickfix-tactic-the-phantom-meet/). *Malware families Lumma Stealer and DarkGate were observed leveraging this technique* (https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clickfix-deception-a-social-engineering-tactic-to-deploy-malware/). *Additional malware such as AsyncRAT, Danabot, and NetSupport were also deployed* (https://www.infosecurity-magazine.com/news/clickfix-cyber-malware-rise/). *Researchers Selena Larson, Tommy Madjar, and Dusty Miller highlighted the tactic's use in campaigns* (https://duo.com/decipher/unique-social-engineering-attack-used-to-deliver-infostealers). *Vidar stealer and Matanbuchus loader were also prevalent in these campaigns* (https://www.darkreading.com/remote-workforce/cut-paste-tactics-import-malware). 

#### Organization/industry/location 
 Targeted organizations include transportation and logistics firms, government entities in Ukraine, Swiss organizations, and various global entities. *A specific campaign targeted Ukrainian organizations by a suspected Russian espionage group, UAC-0050* (https://www.infosecurity-magazine.com/news/clickfix-cyber-malware-rise/). 

#### Start date – End date 
 Not explicitly stated, but campaigns were observed from March through October 2024. 

#### MITRE TTPs 
 ['T1566.001: Spear phishing via service', 'T1059.001: Command and Scripting Interpreter: PowerShell', 'T1204.002: User Execution: Malicious File'] 

#### Impact 
 At least 300 organizations were impacted globally. 

#### Mitigation Steps 
 ['Educate users to recognize and avoid social engineering techniques like ClickFix.', 'Implement and enforce the use of multi-factor authentication.', 'Regularly update and patch all software to reduce vulnerabilities.', 'Use email filters to block malicious email attachments and links.', 'Monitor and restrict the use of PowerShell and other scripting tools.', 'Deploy endpoint protection and response solutions to detect and mitigate threats.'] 

#### Detection Signature 
 {'Service': 'PowerShell', 'Port': 'N/A', 'Severity': 'Critical', 'Incident': 'ClickFix Social Engineering Technique', 'Signature name': 'PowerShell Execution via Social Engineering', 'Internal checks': ['Monitor for unusual PowerShell command executions.', 'Alert on PowerShell commands that contain encoded commands or download executables.', 'Block execution of scripts from email attachments or untrusted sources.'], 'External scanning': ['Monitor for domains and IPs associated with known ClickFix campaigns.', 'Scan for URLs hosting malicious payloads.']} 

#### IoCs:
- url: http://github-scanner.com/l6E.exe ([link](https://www.proofpoint.com/us/blog/threat-insight/security-brief-clickfix-social-engineering-technique-floods-threat-landscape)) 

- hash_sha256: d9ab6cfa60cc75785e31ca9b5a31dae1c33022bdb90cb382ef3ca823c627590d ([link](same as above)) 

- hash_sha256: d737637ee5f121d11a6f3295bf0d51b06218812b5ec04fe9ea484921e905a207 ([link](same as above)) 

- url: http://ricardo.aljiri.es/ricardo/captchaV4DE/ ([link](same as above)) 

- url: http://www.dropbox.com/scl/fi/z4vwx6uot2bwugh34fbvz/Captcha_V4ID882994ft.zip?rlkey=nuh8s42xr9mz2kzkonzwyseaa&st=vk2qu0te&dl=1 ([link](same as above)) 

- url: http://188.119.113.152/x64_stealth.dll ([link](same as above)) 

- ip: 185.91.69.119 ([link](same as above)) 

- ip: 193.124.185.116 ([link](same as above)) 

- ip: 92.118.112.130 ([link](same as above)) 

- url: http://31.214.157.49/chrome.zip ([link](same as above)) 

- domain: meet.google.us-join.com ([link](https://blog.sekoia.io/clickfix-tactic-the-phantom-meet/)) 

- domain: meet.googie.com-join.us ([link](same as above)) 

- domain: meet.google.com-join.us ([link](same as above)) 

- domain: meet.google.web-join.com ([link](same as above)) 

- domain: meet.google.webjoining.com ([link](same as above)) 

- domain: meet.google.cdm-join.us ([link](same as above)) 

- domain: meet.google.us07host.com ([link](same as above)) 

- domain: googiedrivers.com ([link](same as above)) 

- ip: 77.221.157.170 ([link](same as above)) 

- hash_sha256: 92a8cc4e385f170db300de8d423686eeeec72a32475a9356d967bee9e3453138 ([link](same as above)) 

- url: http://95.182.97.58/84b7b6f977dd1c65.php ([link](same as above)) 

- url: http://91.103.140.200:9078/3936a074a2f65761a5eb8/6fmfpmi7.fwf4p ([link](same as above)) 

- url: http://85.209.11.155/joinsystem ([link](same as above)) 

- hash_sha256: a834be6d2bec10f39019606451b507742b7e87ac8d19dc0643ae58df183f773c ([link](same as above)) 

- hash_sha256: 2853a61188b4446be57543858adcc704e8534326d4d84ac44a60743b1a44cbfe ([link](same as above)) 

- hash_sha256: 94379fa0a97cc2ecd8d5514d0b46c65b0d46ff9bb8d5a4a29cf55a473da550d5 ([link](same as above)) 

- url: https://www.rockcreekdds.com/wp-content/1.hta ([link](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clickfix-deception-a-social-engineering-tactic-to-deploy-malware/)) 

- url: https://weoleycastletaxis.co.uk/chao/baby/cow.html ([link](same as above)) 

- hash_sha256: c5545d28faee14ed94d650bda28124743e2d7dacdefc8bf4ec5fc76f61756df3 ([link](same as above)) 

- hash_sha256: 0db16db812cb9a43d5946911501ee8c0f1e3249fb6a5e45ae11cef0dddbe4889 ([link](same as above)) 

- hash_sha256: 5c204217d48f2565990dfdf2269c26113bd14c204484d8f466fb873312da80cf ([link](same as above)) 

- hash_sha256: e9ad648589aa3e15ce61c6a3be4fc98429581be738792ed17a713b4980c9a4a2 ([link](same as above)) 

- hash_sha256: 8c382d51459b91b7f74b23fbad7dd2e8c818961561603c8f6614edc9bb1637d1 ([link](same as above)) 

- hash_sha256: 7d8a4aa184eb350f4be8706afb0d7527fca40c4667ab0491217b9e1e9d0f9c81 ([link](same as above)) 

- hash_sha256: 07594ba29d456e140a171cba12d8d9a2db8405755b81da063a425b1a8b50d073 ([link](same as above)) 

- hash_sha256: 6608aeae3695b739311a47c63358d0f9dbe5710bd0073042629f8d9c1df905a8 ([link](same as above)) 

- hash_sha256: e60d911f2ef120ed782449f1136c23ddf0c1c81f7479c5ce31ed6dcea6f6adf9 ([link](same as above)) 

- For more IoCs, please refer to the above links. 


