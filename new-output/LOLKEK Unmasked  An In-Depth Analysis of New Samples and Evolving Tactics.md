Source: [https://www.sentinelone.com/blog/lolkek-unmasked-an-in-depth-analysis-of-new-samples-and-evolving-tactics/](https://www.sentinelone.com/blog/lolkek-unmasked-an-in-depth-analysis-of-new-samples-and-evolving-tactics/)

# LOLKEK Unmasked  An In-Depth Analysis of New Samples and Evolving Tactics

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: LOLKEK Unmasked | An In-Depth Analysis of New Samples and Evolving Tactics 

 Root cause: The primary vector for the spread of LOLKEK ransomware is not explicitly detailed, but the report highlights a persistent OPSEC mistake in the misconfiguration of the Apache web server used for the TOR-based victim portal. This misconfiguration exposes the server status page, revealing operational details that could assist in attributing the attack to known threat groups. *Additionally, the ADHUBLLKA ransomware family shows similar misconfigurations* (https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family). 

 Threat Actor/group/campaign: LOLKEK ransomware operators, potentially related to the broader GlobeImposter ransomware family, and possibly associated with the TA505 group (also known as G0092, GOLD TAHOE). *Connections to the ADHUBLLKA ransomware family, including BIT, OBZ, U2K, and TZW variants, have been identified* (https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family). 

 Organization/industry/location: The primary targets are small to medium-sized businesses (SMBs) and individual users. There is no specific organization, industry, or location identified. 

 Start date – End date: The report does not specify the exact start date, but it mentions new samples compiled in May 2023 and observed in August 2023. *The ADHUBLLKA ransomware strain was also active since August 1, 2023* (https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family). 

 MITRE TTPs: ['T1005 – Data from Local System', 'T1012 – Query Registry', 'T1027.002 – Obfuscated Files or Information: Software Packing', 'T1070.004 – Indicator Removal: File Deletion', 'T1082 – System Information Discovery', 'T1083 – File and Directory Discovery', 'T1112 – Modify Registry', 'T1202 – Indirect Command Execution', 'T1486 – Data Encrypted for Impact', 'T1490 – Inhibit System Recovery', 'T1547.001 – Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder', '*T1055 – Process Injection* (https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family)'] 

 Impact: The exact number of records or financial losses is not specified, but the ransom demands typically range around $1350 USD or 0.047BTC for decryption. *The genealogy traces back to CryptoLocker* (https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family). 

 Mitigation: ['Regularly backup data and ensure backups are stored offline or in a secure cloud environment.', 'Implement robust endpoint protection and detection solutions to identify and mitigate ransomware attacks.', 'Educate employees on recognizing phishing attempts and other common vectors for ransomware infection.', 'Secure and regularly update all internet-facing services, ensuring proper configurations, especially on web servers like Apache. Disable unnecessary services and ports.', 'Implement multi-factor authentication (MFA) for accessing critical systems and data.'] 

 Detection Signature: {'Service': 'Apache', 'Port': '80, 443', 'Severity': 'Critical', 'Incident': 'LOLKEK ransomware activities', 'Signature name': 'Apache server status page exposed', 'Internal checks': ['Ensure Apache does not expose server status page externally.', 'Validate Apache configuration to restrict access to sensitive administrative pages.', 'Regularly audit configurations and access controls on web servers.'], 'External scanning': ['Port (80, 443) open and accessible', 'Exposed Apache server status page']} 

 IoCs: {'SHA1': ['768b8d81a6b0f779394e4af48755ca3ad77ed951', 'ed247b58c0680b7c92632209181733e92f1b0721'], 'SHA256': ['08029396eb9aef9b413582d103b070c3f422e2b56e1326fe318bef60bdc382ed', '58ac26d62653a648d69d1bcaed1b43d209e037e6d79f62a65eb5d059e8d0fc3f'], 'Ransom Notes SHA256': ['0b179973dc267d9c300e9b7d3c27c67a18d7c79b2cc34927cbe5a465f83c6190', '2c66e5f96470526219f40c6adfd6990cc28d520975da1fdb6bb5497d55a54117'], 'Ransom Notes SHA1': ['456b0bda3f6d9ec9a874daac050b75fc28174510', '88baff4e1751bd364cdb1a4bb5fda4a37ee127c4'], 'IPs/URLs/Domains': ['filessupport@onionmail[.]org', 'https[:]//yip[.]su/2QstD5', 'Mmcbkgua72og66w4jz3qcxkkhefax754pg6iknmtfujvkt2j65ffraad[.]onion', '*104.18.14.101* (https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family)', '*20.99.184.37* (https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family)', '*192.229.211.108* (https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family)', '*23.216.147.61* (https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family)']} 

 Additional Information: {'Phishing emails': 'GlobeImposter is delivered via phishing email as an attachment, or a link to a malicious payload. Payloads are distributed as 7zip archives or similar. These archives contain the malicious JavaScript (.js) which is the GlobeImposter payload. Upon infection, victims are directed to a TOR-based URL (.onion) in order to initiate communication with the attackers. *The changes* (https://www.sentinelone.com/anthology/globeimposter/).', 'Necurs botnet': 'In 2017, GlobeImposter was distributed via the Necurs botnet as part of multiple spam campaigns. *The changes* (https://www.sentinelone.com/anthology/globeimposter/).'} 


# Related articles (describing the same threat) 
['https://www.sentinelone.com/blog/lolkek-unmasked-an-in-depth-analysis-of-new-samples-and-evolving-tactics/', 'https://www.sentinelone.com/anthology/globeimposter/', 'https://netenrich.com/blog/discovering-the-adhubllka-ransomware-family']
