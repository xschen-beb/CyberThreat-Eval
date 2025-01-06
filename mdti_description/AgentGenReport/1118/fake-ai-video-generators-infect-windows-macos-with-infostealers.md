Source: [https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers](https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers
- https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers/
- https://app.any.run/tasks/896d628c-59ae-409e-b0b2-7fd6719b7c2a
- https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Fake AI video generators infect Windows, macOS with infostealers 

#### Root cause 
 The root cause behind the incident is the distribution of fake AI video and image generator applications through malicious websites. These websites distribute malware disguised as legitimate software, specifically Lumma Stealer for Windows and AMOS for macOS. *These fake websites impersonate EditPro and are promoted through search results and advertisements on X* (https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers/). *Lumma Stealer is also distributed through counterfeit websites posing as legitimate antivirus software* (https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/). 

#### Threat actor/group/campaign 
 The specific threat actors behind this campaign are not named, but they are using malicious websites and advertisements to distribute infostealers. *Cybersecurity researcher g0njxa discovered these websites* (https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers/). *Lumma Stealer is developed by a threat actor known as 'Shamel' who operates under the alias 'Lumma' and sells the malware through Telegram and a dedicated website* (https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/). 

#### Organization/industry/location 
 Individuals using Windows and macOS systems are being targeted by these fake AI video generator websites. 

#### Start date – End date 
 The blog reports that the campaign has been active over the past month (as of November 16, 2024). 

#### MITRE TTPs 
 The attack involves the use of:
- T1071.001: Application Layer Protocol - Web Traffic
- T1070.004: Indicator Removal on Host - File Deletion
- T1016: System Network Configuration Discovery
- T1083: File and Directory Discovery
*Additional TTPs include T1204.002: Malicious File, T1055: Process Injection, T1497: Virtualization/Sandbox Evasion, T1140: Deobfuscate/Decode Files or Information, T1564.001: Hidden Files and Directories, T1041: Exfiltration Over C2 Channel* (https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/). 

#### Impact 
 Users' credentials, cryptocurrency wallets, cookies, passwords, credit cards, and browsing history from various browsers are stolen. The stolen information can be used for further attacks or sold on cybercrime markets. *The malware is signed with a stolen code signing certificate from Softwareok.com* (https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers/). *Lumma Stealer also targets sensitive files within user directories and uses event-controlled write operations and encryption to evade detection* (https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/). 

#### Mitigation Steps 
 1. Avoid downloading software from unverified sources.
2. Use reputable antivirus and anti-malware solutions to scan for threats.
3. Enable multi-factor authentication on sensitive accounts like banking, email, and cryptocurrency exchanges.
4. Regularly update passwords and use unique passwords for different sites.
5. Monitor network traffic for suspicious activities. 

#### Detection Signature 
 {'Service': 'Web Browser (Google Chrome, Microsoft Edge, Mozilla Firefox, etc.)', 'Port': 'N/A (Application-level detection)', 'Severity': 'Critical', 'Incident': 'Fake AI video generators distributing infostealers', 'Signature name': '“Fake AI Video Generator Malware Distribution”', 'Internal checks': {'Setting1': "Monitor for the download of suspicious executables (e.g., 'Edit-ProAI-Setup-newest_release.exe' and 'EditProAi_v.4.36.dmg').", 'Setting2': 'Check for unauthorized network traffic to suspicious domains (e.g., proai.club).'}, 'External scanning': {'Setting1': 'Monitor for domain names associated with malware distribution (e.g., editproai.pro, editproai.org).', 'Setting2': 'Scan for executables signed with stolen certificates.'}} 

#### IoCs:
- url: http://editproai.pro ([link](https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers/)) 

- url: http://editproai.org ([link](https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers/)) 

- url: http://proai.club/panelgood/ ([link](https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers/)) 

- hash_sha256: a0041464eaecdb08119b38f377c919e512610307cd7f994aba11c02112fb6777 ([link](https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers/)) 

- hash_sha256: bc6f8cd01077e85c78664af75b95f6645eb611203ed2769304e23c2955fc8ca5 ([link](https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers/)) 

- domain: alcojoldwograpciw.shop ([link](https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/)) 

- domain: productivelookewr.shop ([link](https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/)) 

- domain: tolerateilusidjukl.shop ([link](https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/)) 

- domain: shatterbreathepsw.shop ([link](https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/)) 

- domain: shortsvelventysjo.shop ([link](https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/)) 

- domain: liabilitynighstjsko.shop ([link](https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/)) 

- domain: demonstationfukewko.shop ([link](https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/)) 

- ip_address: 172.67.157.23 ([link](https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/)) 

- ip_address: 104.21.48.243 ([link](https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/)) 

- url: https://alcojoldwograpciw.shop/api ([link](https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/)) 

- For more IoCs, please refer to the above links. 


