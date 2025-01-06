Source: [https://blogs.blackberry.com/en/2024/11/lightspy-apt41-deploys-advanced-deepdata-framework-in-targeted-southern-asia-espionage-campaign#new_tab](https://blogs.blackberry.com/en/2024/11/lightspy-apt41-deploys-advanced-deepdata-framework-in-targeted-southern-asia-espionage-campaign#new_tab)

## Related articles (describing the same threat) 
- https://blogs.blackberry.com/en/2024/11/lightspy-apt41-deploys-advanced-deepdata-framework-in-targeted-southern-asia-espionage-campaign#new_tab
- https://blogs.blackberry.com/en/2024/04/lightspy-returns-renewed-espionage-campaign-targets-southern-asia-possibly-india
- https://www.volexity.com/blog/2024/11/15/brazenbamboo-weaponizes-forticlient-vulnerability-to-steal-vpn-credentials-via-deepdata/
- https://thehackernews.com/2024/11/warning-deepdata-malware-exploiting.html
- https://www.securityweek.com/fortinet-vpn-zero-day-exploited-in-malware-attacks-remains-unpatched-report/

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: LightSpy: APT41 Deploys Advanced DeepData Framework in Targeted Southern Asia Espionage Campaign 

#### Root cause 
 The root cause behind the incident includes unauthorized infiltration and advanced espionage capabilities deployed by APT41. The threat actors utilized sophisticated malware frameworks and command-and-control infrastructure to carry out their operations, including *DeepData v3.2.1228, a modular Windows-based surveillance framework* (https://blogs.blackberry.com/en/2024/11/lightspy-apt41-deploys-advanced-deepdata-framework-in-targeted-southern-asia-espionage-campaign). *The resurgence of LightSpy, targeting Southern Asia and India, indicates a renewed focus on political tensions and espionage* (https://blogs.blackberry.com/en/2024/04/lightspy-returns-renewed-espionage-campaign-targets-southern-asia-possibly-india). *The DEEPDATA malware exploited a FortiClient vulnerability to steal VPN credentials* (https://www.volexity.com/blog/2024/11/15/brazenbamboo-weaponizes-forticlient-vulnerability-to-steal-vpn-credentials-via-deepdata/). *DEEPDATA also employed a zero-day vulnerability in Fortinet's FortiClient for Windows to extract VPN credentials* (https://thehackernews.com/2024/11/warning-deepdata-malware-exploiting.html). *The zero-day vulnerability in Fortinet VPN remains unpatched and was first reported in July 2024* (https://www.securityweek.com/fortinet-vpn-zero-day-exploited-in-malware-attacks-remains-unpatched-report/). 

#### Threat actor/group/campaign 
 APT41 (also known as Double Dragon); *BrazenBamboo* (https://www.volexity.com/blog/2024/11/15/brazenbamboo-weaponizes-forticlient-vulnerability-to-steal-vpn-credentials-via-deepdata/); *Space Pirates targeting Russian entities* (https://thehackernews.com/2024/11/warning-deepdata-malware-exploiting.html); *China-linked state-sponsored threat actor* (https://www.securityweek.com/fortinet-vpn-zero-day-exploited-in-malware-attacks-remains-unpatched-report/) 

#### Organization/industry/location 
 Targeted victims are located in Southern Asia, including political activists, politicians, and journalists. *Recent evidence suggests potential victims in India, aligning with warnings by Apple* (https://blogs.blackberry.com/en/2024/04/lightspy-returns-renewed-espionage-campaign-targets-southern-asia-possibly-india). *BrazenBamboo has also created the DeepPost post-exploitation data exfiltration tool* (https://www.securityweek.com/fortinet-vpn-zero-day-exploited-in-malware-attacks-remains-unpatched-report/). 

#### Start date � End date 
 Ongoing, with significant updates and expansions in capabilities and infrastructure observed from 2022 to 2024. 

#### MITRE TTPs 
 ['T1071: Application Layer Protocol', 'T1105: Ingress Tool Transfer', 'T1059: Command and Scripting Interpreter', 'T1113: Screen Capture', 'T1123: Audio Capture', 'T1213: Data from Information Repositories'] 

#### Impact 
 The impact includes unauthorized access to sensitive communications, credential theft, detailed system intelligence collection, and significant espionage activities. 

#### Mitigation Steps 
 ['Block identified command-and-control infrastructure.', 'Monitor network and devices for unauthorized audio recording activities.', 'Use secure communications platforms for business-sensitive data.', 'Deploy detection rules for DeepData components.', 'Review logs for indicators of compromise (IoCs).', 'Assess exposure of sensitive communication channels.'] 

#### Detection Signature 
 {'Service': 'Various (including messaging platforms and email clients)', 'Port': '28992 (plugin server), 28993 (command-and-control)', 'Severity': 'Critical', 'Incident': 'Advanced espionage campaign by APT41', 'Signature name': 'DeepData Surveillance Detection', 'Internal checks': ['Monitor for unauthorized access to sensitive communication platforms.', 'Detect unusual network traffic patterns indicative of data exfiltration.', 'Look for signs of credential theft and data collection activities.'], 'External scanning': ['Scan for command-and-control infrastructure.', 'Identify and block suspicious domains and IPs associated with APT41.']} 

#### IoCs: 
- hash_md5: b9129d83af902908fa7757e906ec0afe ([link](https://blogs.blackberry.com/en/2024/11/lightspy-apt41-deploys-advanced-deepdata-framework-in-targeted-southern-asia-espionage-campaign)) 

- hash_sha256: 666a4c569d435d0e6bf9fa4d337d1bf014952b42cc6d20e797db6c9df92dd724 ([link](same as above)) 

- hash_md5: 0f0fadd0546734c5c82f3c33d8268046 ([link](same as above)) 

- hash_sha256: cf59cd171270ec9bc2baf618838eb57802cc9d48f64205da308406811dd4da92 ([link](same as above)) 

- hash_md5: bdd8926f4be6576653ac96ee732d587a ([link](same as above)) 

- hash_sha256: efff4106cfd21a356b13a5a99c626a4f103f03b9491c0f1f5e135c1e3c84e76c ([link](same as above)) 

- hash_md5: 4b9aa7d571be1a6ec62931c4c6624328 ([link](same as above)) 

- hash_sha256: 88e5ca44189dabb4cec8a183f6268a42f3f92b2c6d7c722d7f55efd3dc5334c8 ([link](same as above)) 

- hash_md5: d521bf0f24c839e7ceb5db77de090fbc ([link](same as above)) 

- hash_sha256: 55e2dbb906697dd1aff87ccf275efd06ee5e43bb21ea7865aef59513a858cf9f ([link](same as above)) 

- hash_md5: 7efb1bc15ee6e3043f8eaefcf3f10864 ([link](same as above)) 

- hash_sha256: ac7e20d4ddccc5e249ff0c1a72e394f9c1667a896995cf55b97b4f9fbf5de2fd ([link](same as above)) 

- hash_md5: d66776ee123ef2947bc3175653a68d05 ([link](same as above)) 

- hash_sha256: ccfd6ef35c718e2484b3727035d162b667f4b56df43324782d106f50ed1e3bcc ([link](same as above)) 

- hash_md5: 847ec30a4ff2391f1eb7669c22940e51 ([link](same as above)) 

- hash_sha256: 735d59c0949e258501e177ec2dd5fbb60df9fa401ace08949b89077c6f0d41d0 ([link](same as above)) 

- hash_md5: ea47fd87c1b109d5fd529c213aea6b30 ([link](same as above)) 

- hash_sha256: 37a1ffaba2e3ea9a7b2aa272b0587826cc0b5909497d3744ec8c114b504d2544 ([link](same as above)) 

- hash_md5: 3b61d82be05f18754238e26b835da103 ([link](same as above)) 

- hash_sha256: b79629e820cdd36d0daed964a2c0338e125a1f90f08e226f52dc60070747c62e ([link](same as above)) 

- hash_md5: e79da1e448c60e12d835b47735f9da03 ([link](same as above)) 

- hash_sha256: a560931baa404189257ec9cbcc2b9449c579018218cc1d70c99b1d36dd292a0e ([link](same as above)) 

- hash_sha256: 4511567b33915a4c8972ef16e5d7de89de5c6dffe18231528a1d93bfc9acc59f ([link](https://blogs.blackberry.com/en/2024/04/lightspy-returns-renewed-espionage-campaign-targets-southern-asia-possibly-india)) 

- hash_md5: 54570441e91d8e65ea81bb265ba71c8c ([link](same as above)) 

- hash_sha256: 5fb67d42575151dd2a04d7dda7bd9331651c270d0f4426acd422b26a711156b5 ([link](same as above)) 

- hash_md5: 480da467b4687549b38eeea4d4ced293 ([link](same as above)) 

- hash_sha256: 0f662991dbd0568fc073b592f46e60b081eedf0c18313f2c3789e8e3f7cb8144 ([link](same as above)) 

- hash_md5: 6371a942334444029f73b2faa2b76cf6 ([link](same as above)) 

- hash_sha256: 65aa91d8ae68e64607652cad89dab3273cf5cd3551c2c1fda2a7b90aed2b3883 ([link](same as above)) 

- hash_md5: 32076ae7b19f2669fd7c36e48425acd6 ([link](same as above)) 

- hash_sha256: ac6d34f09fcac49c203e860da00bbbe97290d5466295ab0650265be242d692a6 ([link](same as above)) 

- hash_md5: ef92e192d09269628e65145070a01f97 ([link](same as above)) 

- hash_sha256: d2ccbf41552299b24f186f905c846fb20b9f76ed94773677703f75189b838f63 ([link](same as above)) 

- hash_md5: cad4de220316eebc9980fab812b9ed43 ([link](same as above)) 

- hash_sha256: fc7e77a56772d5ff644da143718ee7dbaf7a1da37cceb446580cd5efb96a9835 ([link](same as above)) 

- hash_md5: a2fee8cfdabe4fdeeeb8faa921a3d158 ([link](same as above)) 

- hash_sha256: 3d6ef4d88d3d132b1e479cf211c9f8422997bfcaa72e55e9cc5d985fd2939e6d ([link](same as above)) 

- hash_md5: f162b87ad9466381711ebb4fe3337815 ([link](same as above)) 

- hash_sha256: 18bad57109ac9be968280ea27ae3112858e8bc18c3aec02565f4c199a7295f3a ([link](same as above)) 

- hash_md5: 564235b40d78f9c763b5022954ee9aae ([link](same as above)) 

- hash_sha256: 4b973335755bd8d48f34081b6d1bea9ed18ac1f68879d4b0a9211bbab8fa5ff4 ([link](same as above)) 

- hash_md5: 2178d673779605ffb9cf7f2fa3ec8e97 ([link](same as above)) 

- hash_sha256: 0f66a4daba647486d2c9d838592cba298df2dbf38f2008b6571af8a562bc306c ([link](same as above)) 

- hash_md5: 59ac7dd41dca19a25a78a242e93a7ded ([link](same as above)) 

- hash_sha256: f4e72145e761bcc8226353bb121eb8e549dc0000c6535bfa627795351037dc8e ([link](https://www.volexity.com/blog/2024/11/15/brazenbamboo-weaponizes-forticlient-vulnerability-to-steal-vpn-credentials-via-deepdata/)) 

- For more IoCs, please refer to the above links. 


