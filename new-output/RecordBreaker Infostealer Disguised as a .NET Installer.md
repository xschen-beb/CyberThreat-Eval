Source: [https://asec.ahnlab.com/en/54658/](https://asec.ahnlab.com/en/54658/)

# RecordBreaker Infostealer Disguised as a .NET Installer

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: RecordBreaker Infostealer Disguised as a .NET Installer 

 Root cause: The root cause is the distribution of malware disguised as legitimate software installers. The malware, RecordBreaker (Raccoon Stealer V2), is embedded within a compressed file that includes several normal files, making it difficult to detect. It is mainly distributed in abnormally large sizes with padding added between sections, leading to file sizes between 3 to 7MB compressed and 300 to 700MB decompressed *The changes* (https://asec.ahnlab.com/en/35981/). Additionally, the malware employs various virtual environment detection techniques to avoid analysis. 

 Threat Actor/group/campaign: The specific threat actor is not mentioned in the blog. 

 Organization/industry/location: Not specified who was targeted or the victim. 

 Start date – End date: The blog mentions the detection on Jun 13, 2023, but does not specify the start date of the attack. The malware's distribution became widespread starting from May 20th *The changes* (https://asec.ahnlab.com/en/35981/). 

 MITRE TTPs: ['T1027: Obfuscated Files or Information', 'T1112: Modify Registry', 'T1071: Application Layer Protocol', 'T1059.001: Command and Scripting Interpreter: PowerShell', 'T1204.002: User Execution: Malicious File', 'T1105: Ingress Tool Transfer'] 

 Impact: The impact is not quantified in the blog, but it implies potential theft of sensitive information from affected users. The malware also collects various sensitive information including usernames, MachineGUID, browser cookies, IDs, passwords, and cryptocurrency wallet information *The changes* (https://asec.ahnlab.com/en/35981/). 

 Mitigation: {'Avoid using illegal tools such as cracks or keygens.': True, 'Use installers that are officially provided by developers.': True, 'Treat files downloaded from unknown websites, especially those that are password-protected or contain executables named setup, activate, or install, as suspicious.': True, 'Detailed Steps for mitigation': ['Educate users on the risks of downloading and using pirated or cracked software.', 'Implement robust email and web filtering to block malicious attachments and URLs.', 'Deploy endpoint protection solutions capable of detecting and responding to malware.', 'Regularly update and patch all software to mitigate vulnerabilities.', 'Use application whitelisting to prevent unauthorized executables from running.', 'Monitor network traffic for unusual activities that could indicate data exfiltration.', 'Employ sandboxing and other advanced malware analysis tools to detect sophisticated threats.']} 

 Detection Signature: {'Service': 'PowerShell', 'Port': 'N/A', 'Severity': 'Critical', 'Incident': 'RecordBreaker Infostealer', 'Signature name': '“PowerShell command execution for delay and malware download”', 'Internal checks': ['Monitor for suspicious PowerShell command invocations, especially those using encoded commands (-enc).', 'Track network connections to known malicious C2 domains/IPs.'], 'External scanning': ["Look for PowerShell scripts that include commands like 'Start-Sleep' followed by encoded payloads.", 'Check network logs for communication with the C2 server at 89.185.85[.]117.']} 

 IoCs: {'MD5': ['0c34e053a1641c0f48f7cac16b743a82', '0c819835aa1289985c5292f48e7c1f24', '14eb67caa2c8c5e312e1bc8804f7135f', '19e491dfe1ab656f715245ec9401bdd1', '21a8a6cfa229862eedc12186f0139da0', '0013a631fa834f5bc5e030915f04bae3', '02b4bc8444cbbe15c4d5cac0c64dbd40', '058874fe5f95c762a3fa016faf1077a1', '06c09cc561f860fec73a342d5948c064', '074e3f68a87a7eed362466c685ca4190'], 'URL': ['http[:]//77[.]91[.]73[.]11[:]2705/', 'http[:]//78[.]46[.]248[.]198/', 'http[:]//79[.]137[.]202[.]161/7yd0ymt74ny7qbuk/Pangl[.]exe', 'http[:]//79[.]137[.]203[.]217/', 'http[:]//85[.]192[.]40[.]245/fol1paf2nyg0/bn1[.]exe', 'http://146.19.247[.28/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/nss3.dll', 'http://146.19.247[.28/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/msvcp140.dll', 'http://146.19.247[.28/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/vcruntime140.dll', 'http://146.19.247[.28/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/mozglue.dll', 'http://146.19.247[.28/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/freebl3.dll', 'http://146.19.247[.28/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/softokn3.dll', 'http://146.19.247[.28/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/sqlite3.dll'], 'C2': ['89.185.85[.]117', '94.142.138[.]74', '135[.]181[.]105[.]89', '146[.]19[.]247[.]28', '146[.]19[.]247[.]52', '146[.]19[.]75[.]8', '146[.]70[.]124[.]71']} 


# Related articles (describing the same threat) 
['https://asec.ahnlab.com/en/54658/', 'https://asec.ahnlab.com/en/35981/']
