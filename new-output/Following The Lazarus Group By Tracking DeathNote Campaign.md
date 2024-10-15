Source: [https://securelist.com/the-lazarus-group-deathnote-campaign/109490/](https://securelist.com/the-lazarus-group-deathnote-campaign/109490/)

# Following The Lazarus Group By Tracking DeathNote Campaign

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Lazarus Group DeathNote Campaign 

 Root cause: Multiple vulnerabilities and infection vectors were exploited by the Lazarus group to carry out the DeathNote campaign. These include: - Exploitation of vulnerabilities in widely used legitimate software. - Use of weaponized documents with malicious macros. - Trojanized open-source software (PDF readers). - Use of DLL side-loading techniques. *Additionally, they employed Trojanized IDA Pro* (https://social.cyware.com/news/lazarus-is-back-at-it-again-6faf10e1). *The campaign is also referred to as 'Operation Dream Job' and tracked by Mandiant as UNC2970* (https://medium.com/hunter-strategy/top-five-cyber-threat-intel-stories-of-the-week-04-10-to-04-14-2023-fd0f574f004d). 

 Threat Actor/group/campaign: Lazarus Group 

 Organization/industry/location: Various targets across multiple industries, including cryptocurrency businesses, defense contractors, automotive and academic sectors in Eastern Europe, IT companies in Europe, government organizations in South Korea and Africa, *as well as a South Korean think tank and a Latvian asset developer* (https://social.cyware.com/news/lazarus-is-back-at-it-again-6faf10e1). *Additionally, the group was behind the 3CX attack, attributed to the Labyrinth Chollima sub-group* (https://medium.com/hunter-strategy/top-five-cyber-threat-intel-stories-of-the-week-04-10-to-04-14-2023-fd0f574f004d). 

 Start date – End date: Observed activity from October 2018 to at least July 2022. 

 MITRE TTPs: - T1133: External Remote Services - T1071: Application Layer Protocol - T1090: Connection Proxy - T1059: Command and Scripting Interpreter - T1070: Indicator Removal on Host - T1012: Query Registry - T1074: Data Staged - T1055: Process Injection - T1080: Taint Shared Content - T1105: Ingress Tool Transfer 

 Impact: Multiple organizations compromised, with data exfiltration, system control, and potential disruption of services. 

 Mitigation: 1. **Secure Document Handling:** - Disable macros by default and only enable them for trusted documents. - Train employees to recognize phishing and spear-phishing attempts. 2. **Software Security:** - Ensure all software, especially widely used and critical applications, are up-to-date with the latest security patches. - Use application whitelisting to prevent unauthorized software from running. 3. **Network Segmentation:** - Implement network segmentation to limit lateral movement within the network. - Use firewalls and network intrusion detection systems to monitor and block suspicious activities. 4. **Endpoint Protection:** - Deploy endpoint detection and response (EDR) solutions to monitor and respond to threats on endpoints. - Use multi-factor authentication (MFA) to secure remote access. 5. **Regular Audits and Penetration Testing:** - Conduct regular security audits and penetration testing to identify and remediate vulnerabilities. 6. **Incident Response Plan:** - Develop and regularly update an incident response plan that includes procedures for identifying, containing, and eradicating threats. 

 Detection Signature: - **Service:** Microsoft Word, PDF readers (SumatraPDF) - **Port:** N/A (document-based attacks) - **Severity:** Critical - **Incident:** Lazarus Group DeathNote Campaign - **Signature name:** “Malicious Document Execution” - **Internal checks:** - Setting1: Monitor for execution of macros in documents. - Setting2: Check for creation of unusual files or processes linked to document viewers or legitimate software. - Setting3: Look for suspicious network traffic from endpoints opening documents. - **External scanning:** - Monitor for known malicious documents and payloads associated with Lazarus Group. 

 IoCs: - **Malicious Documents:** - 265f407a157ab0ed017dd18cae0352ae - 7a73a2261e20bdb8d24a4fb252801db7 - 7a307c57ec33a23ce9b5c84659f133cc - ced38b728470c63abcf4db013b09cff7 - 9121f1c13955506e33894ffd780940cd - 50b2154de64724a2a930904354b5d77d - 8a05f6b3f1eb25bcbceb717aa49999cd - ee73a772b72a5f3393d4bf577fc48efe - **Downloader Malware:** - d1c652b4192857cb08907f0ba1790976 - 25b37c971fd7e9e50e45691aa86e5f0a - 0493f40628995ae1b7e3ffacd675ba5f - 8840f6d2175683c7ed8ac2333c78451a - c278d6468896af3699e058786a8c3d62 - 9fd35bad075c2c70678c65c788b91bc3 Additional IoCs provided in the blog for various stages and tools used. 

 Additional Info: *The use of the MATA framework* (https://social.cyware.com/news/lazarus-is-back-at-it-again-6faf10e1) suggests the APT group may expand its IT supply chain attacks. 


# Related articles (describing the same threat) 
['https://securelist.com/the-lazarus-group-deathnote-campaign/109490/', 'https://social.cyware.com/news/lazarus-is-back-at-it-again-6faf10e1', 'https://medium.com/hunter-strategy/top-five-cyber-threat-intel-stories-of-the-week-04-10-to-04-14-2023-fd0f574f004d']
