Source: [https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted](https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted)

## Related articles (describing the same threat) 
- https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted
- https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/
- https://www.extrahop.com/blog/Dark-web-market-for-EDR-Killers

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: EDR Bypass Extortion Attempt 

#### Root cause 
 The incident was caused by the Bring Your Own Vulnerable Driver (BYOVD) technique, using a vulnerable driver to bypass Endpoint Detection and Response (EDR) protections. The threat actor utilized a tool named 'disabler.exe' to exploit a vulnerable driver, disabling EDR hooks in user-mode libraries and kernel-mode callbacks *and used rogue systems to test the AV/EDR bypass tool on a virtual machine* (https://unit42.paloaltonetworks.com/edr-bypass-extortion-attempt-thwarted/). Additionally, tools like *Brute Ratel* (https://www.extrahop.com/blog/Dark-web-market-for-EDR-Killers), *SpyBoy Terminator kit*, and *AvNeutralizer* were employed to evade detection. 

#### Threat actor/group/campaign 
 The threat actor, associated with the user 'KernelMode', was involved in selling EDR bypass tools on forums like XSS and Exploit. *Baphomet* also listed advanced AV/EDR Kill Process Software on the dark web (https://www.extrahop.com/blog/Dark-web-market-for-EDR-Killers). 

#### Organization/industry/location 
 The victim organization was a client of Palo Alto Networks. The specific industry or location was not disclosed. 

#### Start date – End date 
 The exact start and end dates were not specified. 

#### MITRE TTPs 
 ['Initial Access (TA0001): Access via Atera RMM purchased from an initial access broker.', 'Persistence (TA0003): Creation of scheduled tasks to execute Cobalt Strike beacons.', "Defense Evasion (TA0005): Use of 'disabler.exe' to disable EDR hooks.", 'Credential Access (TA0006): Mimikatz and PowerShell to obtain LSASS process dump.', 'Discovery (TA0007): Internal discovery commands on a compromised domain controller.', 'Lateral Movement (TA0008): Windows RDP and PsExec for lateral movement.', 'Exfiltration (TA0010): Rclone to exfiltrate data to an SFTP server.', 'Command and Control (TA0011): Cobalt Strike beacon activity on multiple systems.'] 

#### Impact 
 The specific number of records leaked or financial losses were not disclosed. 

#### Mitigation Steps 
 ['Ensure EDR solutions are updated and configured against known vulnerabilities.', 'Implement strict access controls and multi-factor authentication.', 'Regularly monitor and audit network traffic for unusual activity.', 'Conduct regular security assessments and penetration tests.', 'Educate employees on recognizing phishing attempts and other social engineering tactics.', 'Use advanced threat detection tools to promptly block malicious activities.'] 

#### Detection Signature 
 {'Service': 'Cortex XDR, EDR solutions', 'Port': 'Not specified', 'Severity': 'Critical', 'Incident': 'EDR Bypass Extortion Attempt', 'Signature name': 'EDR bypass tool detection', 'Internal checks': ["EDR solutions should detect and block tools like 'disabler.exe.'", 'Monitor for unusual scheduled tasks and suspicious network connections.'], 'External scanning': ['Monitor for IoCs related to known C2 servers and malicious domains.']} 

#### IoCs:
- hash_sha256: 3758c5eb1fbab2362ef23091f082710606c1b4ebaeaff9b514896dc2a1e2ab17 ([link](unit42.paloaltonetworks.com))

- hash_sha256: 1228fd70d7ce0f31f7e7c98520e66a01935e428be561ce0d25140ba33598f688 ([link](unit42.paloaltonetworks.com))

- hash_sha256: 6106d1ce671b92d522144fcd3bc01276a975fe5d5b0fde09ca1cca16d09b7143 ([link](unit42.paloaltonetworks.com))

- hash_sha256: 14364f1969b83cf4ec2c0e293c6b4d8f750932f6cbf9a8f32173400de33469fd ([link](unit42.paloaltonetworks.com))

- hash_sha256: 264a29a703682456ebe9f679a0e7d18291af84ef4b53a669c2555061e4972394 ([link](unit42.paloaltonetworks.com))

- hash_sha256: 61c0810a23580cf492a6ba4f7654566108331e7a4134c968c2d6a05261b2d8a1 ([link](unit42.paloaltonetworks.com))

- hash_sha256: 8d36705a5b7f6179fdef2d600276f9c0cc6cb3b0a670c11d66baaaea6bd2c8ad ([link](unit42.paloaltonetworks.com))

- hash_sha256: 41f32a3d67b3f983c82070e067a121dd5b8fae2804c97e684acc7f599ba308da ([link](unit42.paloaltonetworks.com))

- hash_sha256: 6e37a054bd7c49b233cace747951911f320bd43be8a79ce455b97403c2f7de2c ([link](unit42.paloaltonetworks.com))

- hash_sha256: aa97acd5628c1f7a16cb98e7b9ce7228119759133f1649b1d5ed849a1a98448b ([link](unit42.paloaltonetworks.com))

- hash_sha256: 97f2676c6d1e16264584ce4c1f1e8790598ba2a85ae08e3d6e394669240b9908 ([link](unit42.paloaltonetworks.com))

- hash_sha256: 0112e3b20872760dda5f658f6b546c85f126e803e27f0577b294f335ffa5a298 ([link](unit42.paloaltonetworks.com))

- hash_sha256: 7c8559134a49c8d8739b66a549f10b22d4fd16afaff51976562f995b2bcd01a9 ([link](unit42.paloaltonetworks.com))

- hash_sha256: 22f52c9e66330642e836aaf1b6573dd7452e76e0f0b5e6ac594a0278689e1d8f ([link](unit42.paloaltonetworks.com))

- hash_sha256: 49d01f2e32808e24dc8129d3c1ebe444f71792ddec2efabee354335fc6d6f64c ([link](unit42.paloaltonetworks.com))

- hash_sha256: 71dfb3f52df040644221f8c59215f83eb516186b6f82dbbb2c16bf3c22e4baf6 ([link](unit42.paloaltonetworks.com))

- hash_sha256: f1c45cbbd98619e197154085a05fd972283af6788343aa04492e35798a06e2b7 ([link](unit42.paloaltonetworks.com))

- hash_sha256: d0c1662ce239e4d288048c0e3324ec52962f6ddda77da0cb7af9c1d9c2f1e2eb ([link](unit42.paloaltonetworks.com))

- hash_sha256: 8b9c7d2554fe315199fae656448dc193accbec162d4afff3f204ce2346507a8a ([link](unit42.paloaltonetworks.com))


