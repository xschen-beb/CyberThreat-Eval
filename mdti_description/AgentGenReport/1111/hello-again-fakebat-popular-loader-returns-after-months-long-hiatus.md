Source: [https://www.malwarebytes.com/blog/cybercrime/2024/11/hello-again-fakebat-popular-loader-returns-after-months-long-hiatus](https://www.malwarebytes.com/blog/cybercrime/2024/11/hello-again-fakebat-popular-loader-returns-after-months-long-hiatus)

## Related articles (describing the same threat) 
- https://www.malwarebytes.com/blog/cybercrime/2024/11/hello-again-fakebat-popular-loader-returns-after-months-long-hiatus
- https://blog.sekoia.io/exposing-fakebat-loader-distribution-methods-and-adversary-infrastructure/
- https://www.spamtitan.com/blog/fakebat-malware-malvertising/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: Hello again, FakeBat: popular loader returns after months-long hiatus 

#### Root cause 
 The root cause of the incident is the use of malicious Google ads to distribute malware. The threat actors used a click tracker or tracking template to bypass detection and impersonate legitimate brands. The campaign also utilized the drive-by download technique to trick users into downloading fake software installers or browser updates *The changes* (https://blog.sekoia.io/exposing-fakebat-loader-distribution-methods-and-adversary-infrastructure/). 

#### Threat actor/group/campaign 
 The campaign involves the FakeBat loader (also known as Eugenloader or PaykLoader), which is used to drop follow-up payloads such as the Lumma stealer, IcedID, and Redline. Additionally, FakeBat is offered under a malware-as-a-service model. Some attacks were conducted by Initial Access Brokers (IABs) *The changes* (https://blog.sekoia.io/exposing-fakebat-loader-distribution-methods-and-adversary-infrastructure/; https://www.spamtitan.com/blog/fakebat-malware-malvertising/). 

#### Organization/industry/location 
 The general target is users who search for popular productivity applications such as Notion via search engines. The malicious ads were shown in various geographic locations. Additionally, campaigns leveraged fake web browser updates and social engineering schemes on social networks. Google’s Mandiant researchers reported a surge in FakeBat infections *The changes* (https://blog.sekoia.io/exposing-fakebat-loader-distribution-methods-and-adversary-infrastructure/; https://www.spamtitan.com/blog/fakebat-malware-malvertising/). 

#### Start date – End date 
 The latest instance was detected on November 8, 2024. The previous instance was on July 25, 2024. 

#### MITRE TTPs 
 ['T1071.001: Application Layer Protocol: Web Protocols', 'T1105: Ingress Tool Transfer', 'T1203: Exploitation for Client Execution', 'T1140: Deobfuscate/Decode Files or Information'] 

#### Impact 
 The impact details such as the number of affected devices or financial losses are not provided in the blog. 

#### Mitigation Steps 
 ['Regularly monitor and audit your Google ads campaigns for any suspicious activity.', 'Utilize advanced threat protection solutions to detect and block malicious ads.', 'Educate users on the risks of clicking on ads and encourage them to visit official websites directly.', 'Implement endpoint protection solutions to detect and block malicious payloads.', 'Keep software and systems up to date with the latest security patches.', 'Use phishing simulators to train employees on recognizing threats *The changes* (https://www.spamtitan.com/blog/fakebat-malware-malvertising/).'] 

#### Detection Signature 
 {'Service': 'Web Browser, Search Engine', 'Port': 'N/A', 'Severity': 'High', 'Incident': 'FakeBat Malvertising Campaign', 'Signature name': 'Malicious Google Ads Detection', 'Internal checks': ['Monitor search engine ad traffic for unusual patterns.', 'Use web filtering to block known malicious domains.', 'Deploy behavior-based detection tools to identify suspicious activity.'], 'External scanning': ['Monitor for domains associated with the campaign (e.g., solomonegbe.com, notion.ramchhaya.com).', 'Check for known malicious payloads and their hashes.']} 

#### IoCs: 
- domain: solomonegbe.com ([link](https://www.malwarebytes.com/blog/cybercrime/2024/11/hello-again-fakebat-popular-loader-returns-after-months-long-hiatus)) 

- domain: notion.ramchhaya.com ([link](same as above)) 

- hash_sha256: 34c46b358a139f1a472b0120a95b4f21d32be5c93bc2d1a5608efb557aa0b9de ([link](same as above)) 

- domain: ghf-gopp1rip.com ([link](same as above)) 

- hash_sha256: 2de8a18814cd66704edec08ae4b37e466c9986540da94cd61b2ca512d495b91a ([link](same as above)) 

- hash_sha256: de64c6a881be736aeecbf665709baa89e92acf48c34f9071b8a29a5e53802019 ([link](same as above)) 

- hash_sha256: 6341d1b4858830ad691344a7b88316c49445754a98e7fd4a39a190c590e8a4db ([link](same as above)) 

- url: furliumalerer.site/1.jar ([link](same as above)) 

- url: pastebin.pl/view/raw/a58044c5 ([link](same as above)) 

- domain: rottieud.sbs ([link](same as above)) 

- domain: amydlesk.com ([link](https://blog.sekoia.io/exposing-fakebat-loader-distribution-methods-and-adversary-infrastructure/)) 

- domain: notilon.co ([link](same as above)) 

- domain: notliion.com ([link](same as above)) 

- domain: notlon.top ([link](same as above)) 

- domain: notlilon.co ([link](same as above)) 

- domain: notion.findreaders.com ([link](same as above)) 

- domain: findreaders.com ([link](same as above)) 

- domain: notion.ilusofficial.com ([link](same as above)) 

- domain: brow-ser-update.top ([link](same as above)) 

- url: brow-ser-update.top/download/dwnl.php ([link](same as above)) 

- url: brow-ser-update.top/GoogleChrome-x86.msix ([link](same as above)) 

- domain: photoshop-adobe.shop ([link](same as above)) 

- url: photoshop-adobe.shop/download/dwnl.php ([link](same as above)) 

- hash_sha256: c336d98d8d4810666ee4693e8c3a2a34191bad864d6b46e468a7eed36e7085f4 ([link](same as above)) 

- hash_sha256: b5ed2f42359e809bf171183a444457c378355d07b414f5828e1e4f7b35bb505f ([link](same as above)) 

- domain: app.getmess.io ([link](same as above)) 

- url: app.getmess.io/download/dwnl.php ([link](same as above)) 

- url: getmess.download/Getmess.msix ([link](same as above)) 

- domain: utd-corts.com ([link](same as above)) 

- url: utd-corts.com/buy/ ([link](same as above)) 

- hash_sha256: 12ea41f2dfa89ad86f082fdf80ca57f14cd8a8f27280aca4f18111758de96d15 ([link](same as above)) 

- hash_sha256: 72a1f6e7979daae38d8e0e14893db4c182b8362acc5d721141ed328ed02c7e28 ([link](same as above)) 

- For more IoCs, please refer to the above links. 


