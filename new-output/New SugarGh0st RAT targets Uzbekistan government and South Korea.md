Source: [https://blog.talosintelligence.com/new-sugargh0st-rat/](https://blog.talosintelligence.com/new-sugargh0st-rat/)

# New SugarGh0st RAT targets Uzbekistan government and South Korea

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: New SugarGh0st RAT targets Uzbekistan government and South Korea 

 Root cause: The root cause behind the incident is the delivery of a new remote access trojan (RAT) named SugarGh0st. This trojan is a customized variant of the Gh0st RAT, delivered via phishing emails containing malicious RAR archive files with Windows Shortcut files embedded with malicious JavaScript. 

 Threat Actor/group/campaign: Suspected Chinese-speaking threat actor named SneakyChef (*The changes* (https://duo.com/decipher/espionage-threat-actor-hits-multiple-government-entities#:~:text=The%20infection%20chain%20leads%20to,Security%20and%20System%20event%20logs.)) 

 Organization/industry/location: Targeted victims include the Uzbekistan Ministry of Foreign Affairs, users in South Korea, Ministries of Foreign Affairs in Latvia, Kazakhstan, Turkmenistan, India, and Angola, and the Royal Embassy of Saudi Arabia (*The changes* (https://duo.com/decipher/espionage-threat-actor-hits-multiple-government-entities#:~:text=The%20infection%20chain%20leads%20to,Security%20and%20System%20event%20logs.)) 

 Start date – End date: Likely started as early as August 2023. 

 MITRE TTPs: ['T1566.001: Phishing: Spear Phishing Attachment', 'T1204.002: User Execution: Malicious File', 'T1059.007: Command and Scripting Interpreter: JavaScript', 'T1055.001: Process Injection: Dynamic-link Library Injection', 'T1027: Obfuscated Files or Information', 'T1071.001: Application Layer Protocol: Web Protocols', 'T1083: File and Directory Discovery', 'T1105: Ingress Tool Transfer', 'T1112: Modify Registry', 'T1036.004: Masquerading: Masquerade Task or Service', 'T1023: Shortcut Modification'] 

 Impact: The impact of this campaign includes unauthorized access to sensitive information, keylogging, remote control of infected systems, and potential surveillance and espionage activities. 

 Mitigation: [{'Secure Email Gateways': ['Implement robust email filtering solutions to block phishing emails.', 'Use advanced threat protection to detect and eliminate malicious attachments.']}, {'Endpoint Protection': ['Deploy anti-malware solutions to detect and block malicious files and activities.', 'Use behavior-based detection to identify suspicious activities like unauthorized file modifications.']}, {'User Education': ['Train employees to recognize phishing attempts and avoid opening suspicious attachments.', 'Encourage reporting of suspicious emails to the IT/security team for further analysis.']}, {'Network Security': ['Monitor network traffic for unusual outbound connections, especially to known malicious domains.', 'Implement intrusion detection and prevention systems to identify and block malicious activities.']}, {'Regular Updates and Patching': ['Ensure all systems and software are up-to-date with the latest security patches.', 'Regularly update anti-malware definitions to protect against new threats.']}] 

 Detection Signature: {'Service': 'Windows (File System, Registry, Network)', 'Port': 'N/A (OS-level monitoring)', 'Severity': 'Critical', 'Incident': 'SugarGh0st RAT', 'Signature name': 'SugarGh0st RAT Detection', 'Internal checks': {'Setting1': 'Monitor for the creation of suspicious LNK files and execution of JavaScript via `cscript`.', 'Setting2': "Detect registry modifications such as the creation of the 'CTFMON.exe' subkey.", 'Setting3': 'Monitor for abnormal file operations, such as creating keylogger files in `%Program Files%\\WinRAR\\WinLog.txt`.'}, 'External scanning': {'Indicator1': 'Unusual outbound connections to domains like `login[.]drive-google-com[.]tk` and `account[.]drive-google-com[.]tk`.', 'Indicator2': 'Network traffic containing the heartbeat message `0x000011A40100`.'}} 

 Detection Tools: ['Cisco Secure Endpoint: Prevent execution of malware.', 'Cisco Secure Web Appliance: Block access to malicious websites.', 'Cisco Secure Email: Block malicious emails.', 'Cisco Secure Firewall: Detect malicious activity.', 'ClamAV: Detect specific malware signatures.', 'Orbital: Use OSqueries to detect indicators of compromise.'] 

 IoCs: {'Domains': ['login[.]drive-google-com[.]tk', 'account[.]drive-google-com[.]tk'], 'Files': ['Investment project details.docx', 'Account.pdf', 'MakerDAO MKR approaches highest since August.docx', 'Equipment_Repair_Guide.docx'], 'Registry Keys': ['HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\CTFMON.exe'], 'ClamAV Signatures': ['Win.Trojan.SugarGh0stRAT-10014937-0', 'Win.Tool.DynamicWrapperX-10014938-0', 'Txt.Loader.SugarGh0st_Bat-10014939-0', 'Win.Trojan.SugarGh0stRAT-10014940-0', 'Lnk.Dropper.SugarGh0stRAT-10014941-0', 'Js.Trojan.SugarGh0stRAT-10014942-1', 'Win.Loader.Ramnit-10014943-1', 'Win.Backdoor.SugarGh0stRAT-10014944-0']} 

 Additional Information: Researchers have also discovered a new RAT named SpiceRAT in conjunction with the SugarGh0st campaign. SpiceRAT uses a sideloading technique involving a legitimate Samsung executable to deploy a malicious DLL, significantly increasing the attack surface (*The changes* (https://duo.com/decipher/espionage-threat-actor-hits-multiple-government-entities#:~:text=The%20infection%20chain%20leads%20to,Security%20and%20System%20event%20logs.)). 


# Related articles (describing the same threat) 
['https://blog.talosintelligence.com/new-sugargh0st-rat/', 'https://duo.com/decipher/espionage-threat-actor-hits-multiple-government-entities#:~:text=The%20infection%20chain%20leads%20to,Security%20and%20System%20event%20logs.']
