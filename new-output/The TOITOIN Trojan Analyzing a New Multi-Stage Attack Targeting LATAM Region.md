Source: [https://www.zscaler.com/blogs/security-research/toitoin-trojan-analyzing-new-multi-stage-attack-targeting-latam-region](https://www.zscaler.com/blogs/security-research/toitoin-trojan-analyzing-new-multi-stage-attack-targeting-latam-region)

# The TOITOIN Trojan Analyzing a New Multi-Stage Attack Targeting LATAM Region

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: TOITOIN Trojan: A New Multi-Stage Attack Targeting LATAM 

 Root cause: The incident involves using Amazon EC2 instances to host malicious ZIP archives, phishing emails, drive-by downloads, and a complex multi-stage infection chain with custom-built modules and macro-enabled documents *The changes* (https://www.secureblink.com/threat-research/unveiling-toitoin-dissecting-a-sophisticated-latam-cyber-attack). 

 Threat Actor/group/campaign: Not explicitly mentioned. 

 Organization/industry/location: Businesses in the Latin American (LATAM) region. 

 Start date – End date: The campaign commenced in March 2023 and is ongoing *The changes* (https://www.secureblink.com/threat-research/unveiling-toitoin-dissecting-a-sophisticated-latam-cyber-attack). 

 MITRE TTPs: ['T1566: Phishing', 'T1064: Scripting', 'T1037: Startup Items', 'T1055: Process Injection', 'T1018: Remote System Discovery', 'T1082: System Information Discovery', 'T1083: File and Directory Discovery', 'T1548.002: Bypass User Account Control', 'T1574.002: DLL Side-Loading', 'T1055.012: Process Hollowing'] 

 Impact: The exact number of impacted records or financial losses is not mentioned, but the campaign targets businesses in the LATAM region, aiming to steal system information and credentials from infected systems. 

 Mitigation: ['Implement multi-layered security measures, including sandboxing to detect and analyze malware behavior.', 'Educate employees on recognizing phishing emails and avoid clicking on suspicious links or downloading unknown files.', 'Regularly update and patch systems to mitigate vulnerabilities exploited by the malware.', 'Implement network segmentation to limit the spread of malware.', 'Use endpoint protection solutions that can detect and block malicious activities.', 'Apply strict access controls and the principle of least privilege to minimize the impact of successful attacks.'] 

 Detection Signature: {'Service': 'Amazon EC2', 'Port': '80, 443 (usual web service ports)', 'Severity': 'Critical', 'Incident': 'TOITOIN Trojan Infection', 'Signature name': 'Amazon EC2 malicious ZIP download', 'Internal checks': {'Setting1': 'Ensure that internal systems do not initiate outbound connections to suspicious Amazon EC2 instances.', 'Setting2': 'Monitor for unusual process activities, such as the creation of batch scripts and persistence mechanisms like LNK files.', 'Setting3': 'Validate the integrity of critical system files and DLLs to detect unauthorized modifications.'}, 'External scanning': {'Port': '80, 443 open', 'Identify': 'Unusual or unauthorized downloads from Amazon EC2 instances hosting ZIP archives.'}} 

 IoCs: {'Domains': ['atendimento-arquivos[.]com', 'arquivosclientes[.]online', 'fantasiacinematica[.]online', 'cartolabrasil[.]com', 'bragancasbrasil[.]com', 'afroblack[.]shop', '179[.]188[.]38[.]7'], 'IP': '191[.]252[.]203[.]222', 'Hashes': ['8fc3c83b88a3c65a749b27f8439a8416 (Downloader Module)', '2fa7c647c626901321f5decde4273633 (Downloader Module)', 'b7bc67f2ef833212f25ef58887d5035a (Krita Loader DLL)', '690bfd65c2738e7c1c42ca8050634166 (InjectorDLL Module)', 'e6c7d8d5683f338ca5c40aad462263a6 (ElevateInjectorDLL Module)', 'c35d55b8b0ddd01aa4796d1616c09a46 (BypassUAC Module)', '7871f9a0b4b9c413a8c7085983ec9a72 (TOITOIN Trojan)']} 

 Additional Information: {'Encryption': 'XOR encryption is used to obscure the payload data, complicating detection *The changes* (https://www.secureblink.com/threat-research/unveiling-toitoin-dissecting-a-sophisticated-latam-cyber-attack).', 'Browsers targeted': 'Google Chrome, Mozilla Firefox, Microsoft Edge, Internet Explorer, Opera *The changes* (https://www.pcrisk.com/removal-guides/27236-toitoin-trojan)', 'Detection Names': 'Avast (Win64:DropperX-gen [Drp]), Combo Cleaner (Gen:Variant.Ser.Midie.2293), ESET-NOD32 (A Variant Of Win64/TrojanDownloader.Age), Kaspersky (Trojan.Win64.Agent.qwijqz), Microsoft (TrojanDownloader:Win64/Lazy.MRD!MTB) *The changes* (https://www.pcrisk.com/removal-guides/27236-toitoin-trojan)', 'Distribution methods': 'Malicious attachments, malvertising, illegal activation tools, fake updates *The changes* (https://www.pcrisk.com/removal-guides/27236-toitoin-trojan)'} 


# Related articles (describing the same threat) 
['https://www.zscaler.com/blogs/security-research/toitoin-trojan-analyzing-new-multi-stage-attack-targeting-latam-region', 'https://www.secureblink.com/threat-research/unveiling-toitoin-dissecting-a-sophisticated-latam-cyber-attack', 'https://www.pcrisk.com/removal-guides/27236-toitoin-trojan']
