Source: [https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted)

## Related articles (describing the same threat) 
- https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted
- https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: EDR Bypass Extortion Attempt Thwarted 

#### Root cause 
 Misconfigured access controls on remote management software (Atera RMM) and lack of stringent monitoring mechanisms. The threat actor exploited vulnerable drivers (BYOVD) to bypass Endpoint Detection and Response (EDR) systems. 

#### Threat actor/group/campaign 
 Unknown threat actor using the alias 'KernelMode.' The threat actor is speculated to be the developer or distributor of the AV/EDR bypass tool. *The involvement of Marti71 was also noted* (https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/). 

#### Organization/industry/location 
 The targeted organization is not disclosed, and the threat actor is linked to a company based in Kazakhstan. 

#### Start date – End date 
 Not specified, but the report was published on November 1, 2024. 

#### MITRE TTPs 
 ['TA0001: Initial Access (Access via Atera RMM)', 'TA0003: Persistence (Creation of scheduled tasks)', 'TA0005: Defense Evasion (AV/EDR bypass tool)', 'TA0006: Credential Access (Usage of Mimikatz)', 'TA0007: Discovery (Internal discovery commands)', 'TA0008: Lateral Movement (RDP and PsExec)', 'TA0010: Exfiltration (Rclone utility)', 'TA0011: Command and Control (Cobalt Strike Beacon)'] 

#### Impact 
 The impact is not quantified in terms of financial loss or the number of records/devices affected. 

#### Mitigation Steps 
 ['Secure Remote Management Tools:', 'Implement multi-factor authentication (MFA).', 'Regularly audit and review access privileges.', 'Ensure that remote management tools are configured securely and are only accessible to authorized personnel.', 'Monitor and Detect BYOVD Attacks:', 'Deploy advanced endpoint protection that can detect and block attempts to load vulnerable drivers.', 'Regularly update and patch systems and drivers to mitigate vulnerabilities.', 'Strengthen EDR and AV Protections:', 'Use EDR solutions that provide robust tampering protection.', 'Enable comprehensive logging and monitoring for suspicious activities.', 'Conduct Regular Security Assessments:', 'Perform penetration testing and vulnerability assessments to identify and rectify potential security weaknesses.', 'Implement continuous monitoring for unusual network and system activities.'] 

#### Detection Signature 
 {'Service': 'Atera RMM, Windows EDR', 'Port': 'Not specified', 'Severity': 'Critical', 'Incident': 'EDR Bypass Extortion Attempt', 'Signature name': 'Unauthorized Remote Management Access and EDR Tampering', 'Internal checks': ['Ensure that remote management tools like Atera RMM are configured securely and are not accessible externally.', 'Verify that EDR systems have tampering protection enabled.', 'Regularly audit and review access controls on remote management tools.'], 'External scanning': ['Detect attempts to load vulnerable drivers on endpoints.', 'Monitor for unauthorized access to remote management tools.']} 

#### IoCs: 
- hash_sha256: 3758c5eb1fbab2362ef23091f082710606c1b4ebaeaff9b514896dc2a1e2ab17 ([link](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/)) 

- hash_sha256: 1228fd70d7ce0f31f7e7c98520e66a01935e428be561ce0d25140ba33598f688 ([link](same as above)) 

- hash_sha256: 6106d1ce671b92d522144fcd3bc01276a975fe5d5b0fde09ca1cca16d09b7143 ([link](same as above)) 

- hash_sha256: 6106d1ce671b92d522144fcd3bc01276a975fe5d5b0fde09ca1cca16d09b7143 ([link](same as above)) 

- hash_sha256: 14364f1969b83cf4ec2c0e293c6b4d8f750932f6cbf9a8f32173400de33469fd ([link](same as above)) 

- hash_sha256: 264a29a703682456ebe9f679a0e7d18291af84ef4b53a669c2555061e4972394 ([link](same as above)) 

- hash_sha256: 61c0810a23580cf492a6ba4f7654566108331e7a4134c968c2d6a05261b2d8a1 ([link](same as above)) 

- hash_sha256: 8d36705a5b7f6179fdef2d600276f9c0cc6cb3b0a670c11d66baaaea6bd2c8ad ([link](same as above)) 

- hash_sha256: 41f32a3d67b3f983c82070e067a121dd5b8fae2804c97e684acc7f599ba308da ([link](same as above)) 

- hash_sha256: 6e37a054bd7c49b233cace747951911f320bd43be8a79ce455b97403c2f7de2c ([link](same as above)) 

- hash_sha256: aa97acd5628c1f7a16cb98e7b9ce7228119759133f1649b1d5ed849a1a98448b ([link](same as above)) 

- hash_sha256: 97f2676c6d1e16264584ce4c1f1e8790598ba2a85ae08e3d6e394669240b9908 ([link](same as above)) 

- hash_sha256: 0112e3b20872760dda5f658f6b546c85f126e803e27f0577b294f335ffa5a298 ([link](same as above)) 

- hash_sha256: 7c8559134a49c8d8739b66a549f10b22d4fd16afaff51976562f995b2bcd01a9 ([link](same as above)) 

- hash_sha256: 22f52c9e66330642e836aaf1b6573dd7452e76e0f0b5e6ac594a0278689e1d8f ([link](same as above)) 

- hash_sha256: 49d01f2e32808e24dc8129d3c1ebe444f71792ddec2efabee354335fc6d6f64c ([link](same as above)) 

- hash_sha256: 71dfb3f52df040644221f8c59215f83eb516186b6f82dbbb2c16bf3c22e4baf6 ([link](same as above)) 

- hash_sha256: d0c1662ce239e4d288048c0e3324ec52962f6ddda77da0cb7af9c1d9c2f1e2eb ([link](same as above)) 

- hash_sha256: 8b9c7d2554fe315199fae656448dc193accbec162d4afff3f204ce2346507a8a ([link](same as above)) 

- ip: 94.75.225.81 ([link](same as above)) 

- ip: 82.192.88.95 ([link](same as above)) 

- ip: 89.251.22.32 ([link](same as above)) 

- ip: 180.131.145.85 ([link](same as above)) 

- domain: beamofthemoon.com ([link](same as above)) 

- domain: mail.beamofthemoon.com ([link](same as above)) 

- domain: store.beamofthemoon.com ([link](same as above)) 


