Source: [https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend)

## Related articles (describing the same threat) 
- https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend
- https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/
- https://www.eurojust.europa.eu/news/malware-targeting-millions-people-taken-down-international-coalition
- https://github.com/eset/malware-ioc/tree/master/redline
- https://securityscorecard.com/research/detailed-analysis-redline-stealer/
- https://cloudsek.com/blog/technical-analysis-of-the-redline-stealer
- https://www.justice.gov/usao-wdtx/pr/us-joins-international-action-against-redline-and-meta-infostealers
- https://flashpoint.io/blog/redline-meta-takedown-infostealer/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: RedLine Stealer and Meta Stealer Takedown 

#### Root cause 
 Use of GitHub repositories as dead-drop resolvers and insufficient security within backend infrastructure, including cleartext password storage. 

#### Threat actor/group/campaign 
 Unknown operators behind RedLine Stealer and Meta Stealer. *Two people were taken into custody in Belgium* (https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/). *Maxim Rudometov, a developer and administrator of RedLine Stealer, was charged with multiple offenses* (https://www.justice.gov/usao-wdtx/pr/us-joins-international-action-against-redline-and-meta-infostealers). *LAPSUS$ group was also linked to using RedLine* (https://flashpoint.io/blog/redline-meta-takedown-infostealer/). 

#### Organization/industry/location 
 General Internet users targeted worldwide. 

#### Start date – End date 
 Active from 2020 until takedown on October 28, 2024. 

#### MITRE TTPs 
 ['T1583.003: Acquire Infrastructure: Virtual Private Server', 'T1583.004: Acquire Infrastructure: Server', 'T1587.001: Develop Capabilities: Malware', 'T1588.003: Develop Capabilities: Code Signing Certificates', 'T1608.001: Stage Capabilities: Upload Malware', 'T1622: Debugger Evasion', 'T1027.002: Obfuscated Files or Information: Software Packing', 'T1132.001: Data Encoding: Standard Encoding', 'T1573.001: Encrypted Channel: Symmetric Cryptography', 'T1573.002: Encrypted Channel: Asymmetric Cryptography', 'T1071.001: Application Layer Protocol: Web Protocols', 'T1095: Non-Application Layer Protocol', 'T1102.001: Web Service: Dead Drop Resolver', 'T1571: Non-Standard Port'] 

#### Impact 
 Thousands of victims across the globe, with the potential for ongoing data theft due to existing malware samples and cracked versions. *Operation Magnus resulted in the takedown of three servers in the Netherlands and the seizure of two domains* (https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/). *Millions of unique credentials, email addresses, and financial information were stolen* (https://www.justice.gov/usao-wdtx/pr/us-joins-international-action-against-redline-and-meta-infostealers). *Flashpoint has collected over 451 million unique credentials this year alone* (https://flashpoint.io/blog/redline-meta-takedown-infostealer/). 

#### Mitigation Steps 
 ['Disable and remove any known instances of RedLine and Meta Stealer panels and backends.', 'Regularly update and patch systems to prevent exploitation by similar malware.', 'Implement multi-factor authentication (MFA) for access to critical systems.', 'Monitor for indicators of compromise (IoCs) and unusual network activity.', 'Use endpoint protection and intrusion detection systems (IDS) to identify and block malicious activity.', 'Educate users about phishing and social engineering tactics to avoid initial malware infection.'] 

#### Detection Signature 
 {'Service': 'GitHub, Backend Servers', 'Port': 'Various ports including 6677, 7766, 8778', 'Severity': 'Critical', 'Incident': 'RedLine Stealer and Meta Stealer', 'Signature name': 'RedLine and Meta Stealer Infrastructure', 'Internal checks': {'Setting1': 'Monitor for unauthorized access to GitHub repositories hosting dead-drop resolvers.', 'Setting2': 'Monitor for use of abnormal or non-standard ports used by RedLine.', 'Setting3': 'Implement and monitor for multi-factor authentication on systems potentially targeted by malware.'}, 'External scanning': {'Check for the presence of RedLine and Meta Stealer related domains and IPs. *Notable domains include spasshik.xyz and fivto.online* (https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/). IoCs: \'[{"type":"hash_sha1","value":"1AD92153B56FC0B39F8FCEC949241EC42C22FA54","source": "https://github.com/eset/malware-ioc/tree/master/redline"},{"type":"hash_sha1","value":"8A0CAFE86C0774F1D9C7F198505AE15D04447DD6","source": "same as above"},{"type":"hash_sha1","value":"607DBA5F630A1DBFF0E13EEBA2730AB9AB2FB253","source": "same as above"},{"type":"hash_sha1","value":"FB3ABAC1FAC852AE6D22B7C4843A04CE75B65663","source": "same as above"},{"type":"hash_sha1","value":"EE153B3F9B190B1492DEFBB1C70830A28F7C41B2","source": "same as above"},{"type":"hash_sha1","value":"1AB006B1C5403BA4648059DF93B6DAEB0E3EC43F","source": "same as above"},{"type":"hash_sha1","value":"DC3A236245AE8C4D5D079E429ED6B77A5B5245C2","source": "same as above"},{"type":"hash_sha1","value":"06A2A900561C122F45088A5EAE9146F7675C63F6","source": "same as above"},{"type":"hash_sha1","value":"1626F2666782710FC28D4AFE607C7BE54F1FC67F","source": "same as above"},{"type":"domain","value":"spasshik.xyz","source": "same as above"}]\'. Include monitoring for domains and servers used for command and control, such as those seized during Operation Magnus, and *Telegram accounts used by the administrators* (https://www.justice.gov/usao-wdtx/pr/us-joins-international-action-against-redline-and-meta-infostealers).': {}, 'Additional Information': '*An international coalition including Eurojust, Federal Bureau of Investigation, Naval Criminal Investigative Service, and Internal Revenue Service Criminal Investigations supported the takedown* (https://www.eurojust.europa.eu/news/malware-targeting-millions-people-taken-down-international-coalition). *Additional IoCs include MainServer.exe, rsa.exe, Nodes.Api.exe, and Panel.exe* (https://github.com/eset/malware-ioc/tree/master/redline). *The RedLine Stealer also used C2 server siyatermi.duckdns.org:17044, SHA256 hash E3544F1A9707EC1CE083AFE0AE64F2EDE38A7D53FC6F98AAB917CA049BC63E69, and targeted directories %LocalApplicationData%\\Yandex\\YaAddon and %AppData%\\winlogon.exe* (https://securityscorecard.com/research/detailed-analysis-redline-stealer/). *RedLine Stealer operates on a MaaS model, using Regsvcs.exe and process hollowing to deploy, and collects Discord tokens* (https://cloudsek.com/blog/technical-analysis-of-the-redline-stealer). *Operation Magnus included the participation of the Dutch National Police, Belgian Federal Police, UK National Crime Agency, Australian Federal Police, Portuguese Federal Police, and Eurojust* (https://www.justice.gov/usao-wdtx/pr/us-joins-international-action-against-redline-and-meta-infostealers).'}} 


