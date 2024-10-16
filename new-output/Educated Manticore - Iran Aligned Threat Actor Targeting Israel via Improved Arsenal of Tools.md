Source: [https://research.checkpoint.com/2023/educated-manticore-iran-aligned-threat-actor-targeting-israel-via-improved-arsenal-of-tools/](https://research.checkpoint.com/2023/educated-manticore-iran-aligned-threat-actor-targeting-israel-via-improved-arsenal-of-tools/)

# Educated Manticore - Iran Aligned Threat Actor Targeting Israel via Improved Arsenal of Tools

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Educated Manticore - Iran Aligned Threat Actor Targeting Israel via Improved Arsenal of Tools 

 Root cause: The root cause behind the incident includes the use of ISO images and other archive files to initiate infection chains. The threat actor employed sophisticated techniques such as .NET executables constructed as Mixed Mode Assembly, using both .NET and native C++ code to enhance tools’ functionality and complicate analysis. The initial loader in the ISO file used open-source tools like RunPE-In-Memory for further payload execution. 

 Threat Actor/group/campaign: Educated Manticore, closely related to Phosphorus (an Iranian-aligned threat actor) also known as APT35/Charming Kitten or *Mint Sandstorm* (https://www.microsoft.com/en-us/security/blog/2022/09/07/profiling-dev-0270-phosphorus-ransomware-operations/). 

 Organization/industry/location: The primary targets were entities in Israel, including possibly academic researchers, based on the nature of the lures used (Iraq-themed academic content). 

 Start date – End date: The specific start and end dates are not provided in the report. 

 MITRE TTPs: ['T1204.002: User Execution: Malicious File', 'T1203: Exploitation for Client Execution', 'T1059.001: Command and Scripting Interpreter: PowerShell', 'T1027: Obfuscated Files or Information', 'T1071.001: Application Layer Protocol: Web Protocols', 'T1036.005: Masquerading: Match Legitimate Name or Location', 'T1140: Deobfuscate/Decode Files or Information', 'T1070.004: Indicator Removal on Host: File Deletion'] 

 Impact: The impact is not quantified in terms of records leaked or financial losses in the report. However, individual ransom demands reached *USD 8,000* (https://www.microsoft.com/en-us/security/blog/2022/09/07/profiling-dev-0270-phosphorus-ransomware-operations/). 

 Mitigation: ['Educate end-users about the risks of opening unsolicited ISO files and other archive files.', 'Implement strict email filtering and antivirus solutions to detect and block malicious attachments.', 'Regularly update and patch systems to minimize vulnerabilities.', 'Implement robust endpoint protection solutions that can detect and block execution of unauthorized executables and scripts.', 'Monitor network traffic for unusual patterns that may indicate C2 communication.', 'Apply application whitelisting to prevent unauthorized applications from executing.', 'Use strong, unique passwords and enable multi-factor authentication (MFA) across all systems.'] 

 Detection Signature: {'Service': 'HTTP/HTTPS', 'Port': '80/443', 'Severity': 'Critical', 'Incident': 'Educated Manticore', 'Signature name': 'Malicious ISO Image Download', 'Internal checks': ['Secure the use of PowerShell with constrained language mode and logging.', 'Monitor for the creation of unexpected directories and files such as `C:\\Users\\User\\AppData\\Local\\SystemCall`.', 'Check for unusual registry modifications, especially under `HKCU\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Shell`.'], 'External scanning': ['Detect access to known malicious domains: subinfralab[.]info, deersharpfork[.]info, blackturtle.hopto[.]org.']} 

 IoCs: {'C&C domains': ['subinfralab[.]info', 'deersharpfork[.]info', 'blackturtle.hopto[.]org'], 'Hashes': {'Archives': ['3e1ed006e120a1afaa49f93b4156a992f8d799b1888ca6202c1098862323c308', '29318f46476dc0cfd7b928a2861fea1b761496eb5d6a26040e481c3bd655051a', '13bab4e32cd6365dba40424d20525cb84b4c6d71d3c5088fe94a6cfe07573e8e', '6e842691116c188b823b7692181a428e9255af3516857b9f2eebdeca4638e96e', 'bc8f075c1b3fa54f1d9f4ac622258f3e8a484714521d89aa170246ce04701441', '706510916cfc7624ec5d9f9598c95570d48fa8601eecbbae307e0af7618d1460'], 'PE files': ['e5ba06943abb666f69f757fcd591dd1cceb66cad698fb894d9bc8911282198c4', '97a615e69c38db9dffda6be7c11dd27547ce4036a4998a1469fa81b548c6f0b0', 'e5016dfeae584de20a90f1bef073c862028f410d5b0ae4c074a696b8f8528037', '5704bc31061c7ca675bb9d56b9b56a175bf949accf6542999b3a7305af485906', '4fcde8ec5983cf1465ff7dbcd7d90fcd47d666b0b8352db1dcd311084ed1b3e8', '7cc9d887d47f99ca37d2fee6171067df70b4417e96fdb661b9fef697124444cc', 'bdb2a12f2f84c3742240b8b9e1d6638a73c6b8752aff476051fe33a0bb408010', '5d216f5625caf92d224200647147d27bb79e1cff6c8a9fbcac63f321f6bbf02b', '62d0b8b5d4281ce107c43d36f222680b0cc85844b8973b645095ccdfb128454d'], 'LNK': ['1672a14a3e54a127493a2b8257599c5582204846a78521b139b074155003cba4', '0f4d309f0145324a6867108bb04a8d5d292e7939223d6d63f44e21a1ce45ce4e'], 'PowerShell': ['737cb075ba0b5ed6d8901dcd798eecff0bc8585091bc232c54f92df7f9e9e817', 'cd813d56cf9f2201a2fa69e77fb9acaaa37e64183c708de64cb5cb7c3035a184', 'c0de9b90a0ac591147d62864264bf00b6ec17c55f7095fdf58923085fe502400', '59a4b11b9fb93e3de7c27c25258cec43de38f86f37d88615687ab8402e4ae51e']}} 


# Related articles (describing the same threat) 
['https://research.checkpoint.com/2023/educated-manticore-iran-aligned-threat-actor-targeting-israel-via-improved-arsenal-of-tools/', 'https://www.microsoft.com/en-us/security/blog/2022/09/07/profiling-dev-0270-phosphorus-ransomware-operations/']
