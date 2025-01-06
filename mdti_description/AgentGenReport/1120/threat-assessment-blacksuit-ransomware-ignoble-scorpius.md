Source: [https://unit42.paloaltonetworks.com/threat-assessment-blacksuit-ransomware-ignoble-scorpius](https://unit42.paloaltonetworks.com/threat-assessment-blacksuit-ransomware-ignoble-scorpius)

## Related articles (describing the same threat) 
- https://candid.technology/blacksuit-ransomware-ramps-up-ops-hitting-93-organisations
- https://unit42.paloaltonetworks.com/threat-assessment-blacksuit-ransomware-ignoble-scorpius
- https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware
- https://fidelissecurity.com/threatgeek/threat-intelligence/blacksuit-ransomware

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: BlackSuit Ransomware Attack by Ignoble Scorpius 

#### Root cause 
 Multiple initial access vectors such as phishing campaigns, SEO poisoning with GootLoader, use of legitimate VPN credentials, and software supply chain attacks; *use of malicious drivers to disable antivirus* (https://candid.technology/blacksuit-ransomware-ramps-up-ops-hitting-93-organisations/). 

#### Threat actor/group/campaign 
 Ignoble Scorpius, rebranded from Royal ransomware, distributors of BlackSuit ransomware. 

#### Organization/industry/location 
 Various industries globally, including critical sectors such as healthcare, government, finance; significant victims in construction, manufacturing, and education sectors, primarily in the United States; *targeting VMware ESXi servers* (https://candid.technology/blacksuit-ransomware-ramps-up-ops-hitting-93-organisations/); *KADOKAWA corporation* (https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware); *victims include 53 organizations* (https://fidelissecurity.com/threatgeek/threat-intelligence/blacksuit-ransomware/). 

#### Start date – End date 
 May 2023 – March 2024, with operations ramping up significantly by March 2024. 

#### MITRE TTPs 
 ['T1566.001: Phishing: Spearphishing Attachment', 'T1566.004: Phishing: Spearphishing Voice', 'T1608.006: Compromise Infrastructure: SEO Poisoning', 'T1078: Valid Accounts', 'T1195.002: Supply Chain Compromise: Compromise Software Supply Chain', 'T1003.001: OS Credential Dumping: LSASS Memory', 'T1003.003: OS Credential Dumping: NTDS', 'T1003.006: OS Credential Dumping: DCSync', 'T1057: Process Discovery', 'T1021.001: Remote Services: Remote Desktop Protocol', 'T1021.002: Remote Services: SMB/Windows Admin Shares', 'T1570: Lateral Tool Transfer', 'T1557: Adversary-in-the-Middle', 'T1558/002: Steal or Forge Kerberos Tickets: Silver Ticket', 'T1562.001: Impair Defenses: Disable or Modify Tools', 'T1567.002: Exfiltration Over Web Service: Exfiltration to Cloud Storage', 'T1564.006: Hide Artifacts: Run Virtual Instance', 'T1486: Data Encrypted for Impact', 'T1490: Inhibit System Recovery', 'T1021.001: Remote Services: Remote Desktop Protocol', 'T1055.002: Process Injection: Portable Executable Injection', 'T1560.002: Archive Collected Data: Archive via Utility', 'T1560.003: Archive Collected Data: Archive via Library', '*partial encryption technique* (https://fidelissecurity.com/threatgeek/threat-intelligence/blacksuit-ransomware/)'] 

#### Impact 
 Over 93 victim organizations globally, with ransom demands averaging 1.6% of the victim organization’s annual revenue, impacting organizations with median revenue of $19.5 million; *ransom demand averaging $2.5 million* (https://fidelissecurity.com/threatgeek/threat-intelligence/blacksuit-ransomware/). 

#### Mitigation Steps 
 ['Implement multi-factor authentication (MFA) for all remote access points.', 'Conduct regular security awareness training focused on phishing and social engineering attacks.', 'Ensure endpoint protection tools are updated and configured to detect and prevent malware and unauthorized access.', 'Utilize network segmentation and least privilege access principles.', 'Regularly backup data and ensure backups are stored offline and tested for integrity.', 'Deploy advanced threat detection and response solutions, such as Palo Alto Networks Cortex XDR and XSIAM.', 'Engage in proactive threat hunting and incident response planning with services like Unit 42 Managed Threat Hunting.', '*Keep all software and systems current to close vulnerabilities* (https://fidelissecurity.com/threatgeek/threat-intelligence/blacksuit-ransomware/)', '*Segment the networks into smaller sections in order to contain the spread of ransomware* (https://fidelissecurity.com/threatgeek/threat-intelligence/blacksuit-ransomware/)'] 

#### Detection Signature 
 {'Service': 'Multiple (Network Security, Endpoint Detection and Response)', 'Port': 'Various (depending on the attack vector)', 'Severity': 'Critical', 'Incident': 'BlackSuit Ransomware Infection', 'Signature name': 'BlackSuit Ransomware Indicators', 'Internal checks': ['Monitor for unusual access patterns and unauthorized use of VPN credentials.', 'Detect and block phishing emails with malicious attachments.', 'Identify and respond to the use of tools like Mimikatz, NanoDump, and Impacket.'], 'External scanning': ['Monitor for exposed RDP and SMB services.', 'Detect abnormal data exfiltration activities to cloud storage services.']} 

#### IoCs: 
- url: http://weg7sdx54bevnvulapqu6bpzwztryeflq3s23tegbmnhkbpqz637f2yd.onion/?id=[ID] ([link](https://unit42.paloaltonetworks.com/threat-assessment-blacksuit-ransomware-ignoble-scorpius/)) 

- hash_sha256: f1684fb118d4d8fc56653fcc49e12a659b64c4459ba037fa94f21783235cc6ba ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: dede96fd44c0f78eb79ceb63b898874e8922efc59d8bfb9f86505b1992bc00a3 ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: 6a2e454942cfeebb1140e1a28cb05fd49461d07792e97663378399c719fbc9ee ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: 79ab73a0e9dd8eac045c00fd1bd172a7f359588901f93c83e6740157eb21e7df ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: 7f09c2e35783fca69f0e12f31d767cecf8a98567f2b6f1e2d81d2b2e93fe6307 ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: 60a9785ec20ec08b6792e304fc4b363abd54b8a7a2945dca9f97ee07783c4759 ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: 5aeaa5c4f4100b2084814be72a695a5bf4a95fdb8a0c65704523608baa79b726 ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: d96ff4b3e188f7ff96ed28c1381a6318dd76bb1fbd6ca02c6ab0236e1c7f35aa ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: 3be3a3c2c1abc1d401e845a2b8952f4f3e55b510f3d6c1eb2a4503c7be09bec1 ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: 90ae0c693f6ffd6dc5bb2d5a5ef078629c3d77f874b2d2ebd9e109d8ca049f2c ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: 6ad8215bd6b52d897dcfa0a9829720d0532adc741460ecb4b8f00c4427b6141c ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: 8605dec4ae4bd9f51297d1f244d0647bc0637d6ce6a957a5f810c64ae63276cb ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- hash_sha256: 2adcf43d221de2f72ba5088dac3a3193219412882df711d095f04e3f5b40767c ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- mutex: WLm87eV1oNRx6P3E4Cy9 ([link](https://www.deepinstinct.com/blog/deep-dive-exposing-stealthy-new-blacksuit-ransomware)) 

- For more IoCs, please refer to the above links. 

#### Additional Info 
 {'Ransom note': 'readme.blacksuit.txt', 'Extension': '.blacksuit'} 


