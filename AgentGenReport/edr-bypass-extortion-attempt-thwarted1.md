Source: [https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted)

## Related articles (describing the same threat) 
- https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted
- https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: EDR Bypass Testing Reveals Extortion Actor's Toolkit 

#### Root cause 
 Use of a BYOVD (Bring Your Own Vulnerable Driver) technique to bypass EDR (Endpoint Detection and Response) systems. In this case, using a vulnerable driver file (`wnbios.sys` or `WN_64.sys`) along with a modified version of the EDRSandBlast tool to disable security mechanisms *and a rogue virtual machine `DESKTOP-J8AOTJS` used for testing* (https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/). 

#### Threat actor/group/campaign 
 Likely associated with cybercriminal actors involved in extortion campaigns. The specific actor identified through the investigation is linked to usernames such as `Marti71` and `KernelMode` on cybercrime forums. 

#### Organization/industry/location 
 The specific organization targeted is not disclosed, but the incident occurred within the context of a client environment using Cortex XDR *and rogue endpoints with older Cortex XDR agents* (https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/). 

#### Start date – End date 
 The exact dates of the incident are not provided. 

#### MITRE TTPs 
 {'Initial Access (TA0001)': 'Access purchased via Atera RMM from an initial access broker.', 'Persistence (TA0003)': 'Creation of scheduled tasks to execute Cobalt Strike beacons.', 'Defense Evasion (TA0005)': 'Use of the `disabler.exe` tool to bypass AV/EDR systems.', 'Credential Access (TA0006)': 'Use of Mimikatz and PowerShell to obtain credentials.', 'Discovery (TA0007)': 'Internal discovery commands using built-in tools like `nltest`, `net`, `dsquery`, and `rundll32`.', 'Lateral Movement (TA0008)': 'Use of Windows RDP and PsExec for lateral movement.', 'Exfiltration (TA0010)': 'Use of Rclone for data exfiltration.', 'Command and Control (TA0011)': 'Cobalt Strike Beacon activity on multiple systems.'} 

#### Impact 
 The incident provided Unit 42 researchers with visibility into the threat actor's toolkit, including AV/EDR bypass tools, and enabled the identification of one of the actors involved. *The rogue system revealed additional tools, files, and identifying details of the threat actor, including personal and professional background* (https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/). The actual number of records or devices impacted is not specified. 

#### Mitigation Steps 
 ['Implement strict monitoring and control over the use of remote management tools like Atera RMM.', 'Ensure that all security agents, such as EDR and AV, have tamper protection enabled.', 'Regularly update and patch all software and drivers to mitigate vulnerabilities.', 'Conduct regular security assessments and incident response readiness reviews.', 'Deploy advanced threat detection technologies (e.g., Cortex XDR, Advanced WildFire).', 'Monitor cybercrime forums for emerging threats and associated indicators of compromise (IoCs).'] 

#### Detection Signature 
 {'Service': 'Cortex XDR (or other EDR solutions)', 'Severity': 'Critical', 'Incident': 'EDR Bypass using vulnerable drivers', 'Signature name': '“EDR Bypass via BYOVD”', 'Internal checks': ['Ensure all security agents have tamper protection enabled.', 'Monitor for unusual scheduled tasks and processes related to known bypass tools.', 'Validate the integrity and versioning of all installed drivers.'], 'External scanning': ['Scan for the presence of known vulnerable drivers (`wnbios.sys` or `WN_64.sys`).', 'Detect execution attempts of known bypass tools like `disabler.exe`.']} 

#### IoCs: 
- hash_sha256: 3758c5eb1fbab2362ef23091f082710606c1b4ebaeaff9b514896dc2a1e2ab17 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 1228fd70d7ce0f31f7e7c98520e66a01935e428be561ce0d25140ba33598f688 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 6106d1ce671b92d522144fcd3bc01276a975fe5d5b0fde09ca1cca16d09b7143 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 14364f1969b83cf4ec2c0e293c6b4d8f750932f6cbf9a8f32173400de33469fd ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 264a29a703682456ebe9f679a0e7d18291af84ef4b53a669c2555061e4972394 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 61c0810a23580cf492a6ba4f7654566108331e7a4134c968c2d6a05261b2d8a1 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 8d36705a5b7f6179fdef2d600276f9c0cc6cb3b0a670c11d66baaaea6bd2c8ad ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 41f32a3d67b3f983c82070e067a121dd5b8fae2804c97e684acc7f599ba308da ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 6e37a054bd7c49b233cace747951911f320bd43be8a79ce455b97403c2f7de2c ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: aa97acd5628c1f7a16cb98e7b9ce7228119759133f1649b1d5ed849a1a98448b ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 97f2676c6d1e16264584ce4c1f1e8790598ba2a85ae08e3d6e394669240b9908 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 0112e3b20872760dda5f658f6b546c85f126e803e27f0577b294f335ffa5a298 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 7c8559134a49c8d8739b66a549f10b22d4fd16afaff51976562f995b2bcd01a9 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 22f52c9e66330642e836aaf1b6573dd7452e76e0f0b5e6ac594a0278689e1d8f ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 49d01f2e32808e24dc8129d3c1ebe444f71792ddec2efabee354335fc6d6f64c ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 71dfb3f52df040644221f8c59215f83eb516186b6f82dbbb2c16bf3c22e4baf6 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: d0c1662ce239e4d288048c0e3324ec52962f6ddda77da0cb7af9c1d9c2f1e2eb ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 8b9c7d2554fe315199fae656448dc193accbec162d4afff3f204ce2346507a8a ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: f1c45cbbd98619e197154085a05fd972283af6788343aa04492e35798a06e2b7 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- ip: 94.75.225.81 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- ip: 82.192.88.95 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- ip: 89.251.22.32 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- ip: 180.131.145.85 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- domain: beamofthemoon.com ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- domain: mail.beamofthemoon.com ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- domain: store.beamofthemoon.com ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 


