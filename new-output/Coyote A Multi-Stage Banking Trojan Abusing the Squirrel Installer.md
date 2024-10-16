Source: [https://securelist.com/coyote-multi-stage-banking-trojan/111846/](https://securelist.com/coyote-multi-stage-banking-trojan/111846/)

# Coyote A Multi-Stage Banking Trojan Abusing the Squirrel Installer

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Coyote: A multi-stage banking Trojan abusing the Squirrel installer 

 Root cause: The root cause behind the incident involves the use of the Squirrel installer to distribute the malware, leveraging NodeJS and Nim as loaders to complete the infection chain. The Trojan uses DLL sideloading and persistence mechanisms such as Windows logon scripts to maintain its presence on the targeted systems. The installer masquerades as an update packager, bypassing traditional detection methods, and employs the Electron framework to run obfuscated JavaScript code, copying executables and loading the final stage, which uses Nim to unpack a .NET executable and execute it in memory using the CLR. Additionally, the malware uses the Chromium Embedded Framework (CEF) for DLL injection *Your changes* (https://blogs.blackberry.com/en/2024/07/coyote-banking-trojan-targets-latam-with-a-focus-on-brazilian-financial-institutions). Several executables, including Google Chrome and OBS Studio, facilitate the DLL sideloading process *Your changes* (https://www.pcrisk.com/removal-guides/29046-coyote-trojan). 

 Threat Actor/group/campaign: The threat actor behind this incident is not explicitly named, but the malware is identified as a Brazilian banking Trojan, indicating that it is likely developed by a cybercriminal group specializing in financial malware in Brazil. 

 Organization/industry/location: The primary targets are users of more than 60 banking institutions, mainly from Brazil. 

 Start date – End date: The specific dates of the attack are not provided, but the report was published on February 8, 2024. 

 MITRE TTPs: ['T1071.001: Application Layer Protocol: Web Protocols', 'T1055.001: Process Injection: Dynamic-link Library Injection', 'T1059.007: Command and Scripting Interpreter: JavaScript', 'T1027: Obfuscated Files or Information', 'T1053.005: Scheduled Task/Job: Scheduled Task', 'T1140: Deobfuscate/Decode Files or Information', 'T1204.002: User Execution: Malicious File'] 

 Impact: The report does not specify the number of records leaked or the financial losses, but it indicates that up to 90% of infections originated from Brazil and involved at least 61 banking applications. The Trojan can execute 24 different commands, including taking screenshots, keylogging, phishing overlays, and process termination *Your changes* (https://www.pcrisk.com/removal-guides/29046-coyote-trojan). 

 Mitigation: ['**Secure Software Installation**: Avoid installing software from untrusted sources. Verify the integrity and authenticity of software packages before installation.', '**Endpoint Protection**: Use robust endpoint protection solutions that can detect and block banking Trojans and other types of malware.', '**Regular Updates**: Keep all software, including operating systems and applications, up to date with the latest security patches.', '**Security Awareness Training**: Educate users on recognizing phishing attempts and the risks of downloading and installing software from unverified sources.', '**Monitor and Audit**: Implement monitoring and auditing tools to detect unusual behaviors and unauthorized access attempts on systems.', '**Application Whitelisting**: Use application whitelisting to prevent the execution of unauthorized software.'] 

 Detection Signature: {'Service': 'Node.js', 'Port': 'Various, typically 80 (HTTP) or 443 (HTTPS) for C2 communications', 'Severity': 'Critical', 'Incident': 'Coyote banking Trojan', 'Signature name': '“Node.js and Nim-based Trojan activity”', 'Internal checks': ['Setting1: Verify the presence of unauthorized Node.js applications.', 'Setting2: Monitor for DLL sideloading activities, particularly involving `libcef.dll`.', 'Setting3: Check for suspicious registry entries, such as `HKCU\\Environment\\UserInitMprLogonScript`.'], 'External scanning': ['Port (80/443) open', 'Node.js application making suspicious outbound connections']} 

 IoCs: {'Host-based (MD5 hash)': ['03eacccb664d517772a33255dff96020', '071b6efd6d3ace1ad23ee0d6d3eead76', '276f14d432601003b6bf0caa8cd82fec', '5134e6925ff1397fdda0f3b48afec87b', 'bf9c9cc94056bcdae6e579e724e8dbbd'], 'C2 domain list': ['atendesolucao[.]com', 'servicoasso[.]com', 'dowfinanceiro[.]com', 'centralsolucao[.]com', 'traktinves[.]com', 'diadaacaodegraca[.]com', 'segurancasys[.]com', 'bestoraculo[.]com', 'acaodegraca[.]com', 'turmadabruta[.]com', 'britoingresso[.]com', 'cinebrian[.]com', 'cloridatosys[.]com', 'flogoral[.]com', 'formitamina[.]com', 'bilatex[.]com', 'autoglobalcar[.]com', 'angelcallcenter[.]com', 'gargamellojas[.]com', 'carrodenatal[.]com', 'marvelnatal[.]com', 'nograusistema[.]com', 'navegacaodura[.]com', 'jogodequadra[.]com', 'carrosantigo[.]com', 'bermatechcliente[.]com']} 


# Related articles (describing the same threat) 
['https://securelist.com/coyote-multi-stage-banking-trojan/111846/', 'https://advisory.eventussecurity.com/advisory/a-multi-stage-banking-trojan-coyote-leveraging-the-squirrel-installer/', 'https://blogs.blackberry.com/en/2024/07/coyote-banking-trojan-targets-latam-with-a-focus-on-brazilian-financial-institutions', 'https://www.pcrisk.com/removal-guides/29046-coyote-trojan']
