Source: [https://asec.ahnlab.com/en/52899/](https://asec.ahnlab.com/en/52899/)

# SparkRAT Being Distributed Within a Korean VPN Installer

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: SparkRAT Being Distributed Within a Korean VPN Installer 

 Root cause: The root cause is the compromise of the VPN provider's legitimate installer, repackaged with a .NET dropper that installs SparkRAT. The dropper includes the original VPN installer and SparkRAT malware. *The dropper creates and executes the malware at %LOCALAPPDATA%\Syservices\svchost.exe* (https://asec.ahnlab.com/ko/52076/). *Recent attacks used a GoLang dropper instead of .NET and added MeshAgent for remote control* (https://asec.ahnlab.com/en/53267/). 

 Threat Actor/group/campaign: The specific threat actor is not identified, but it is suspected to be fluent in Chinese with connections to Chinese-speaking regions due to the tools and geographical impact. *SparkRAT and associated tools are developed by Chinese-speaking developers* (https://asec.ahnlab.com/ko/52076/). 

 Organization/industry/location: The targeted victims are users of a Korean VPN service, with more installations observed from users in China. 

 Start date – End date: The exact start and end dates are not provided. The blog post date is May 3, 2023, and detection signatures date back to August 28, 2022. 

 MITRE TTPs: ['T1059: Command and Scripting Interpreter', 'T1071.001: Application Layer Protocol: Web Protocols', 'T1105: Ingress Tool Transfer', 'T1053.005: Scheduled Task/Job: Scheduled Task', 'T1027: Obfuscated Files or Information'] 

 Impact: The number of users impacted is not provided, but many users, particularly in China, could be affected given the VPN's usage patterns. *The SparkRAT variant used is notable for lacking obfuscation, using the main.init() function to decrypt C&C data* (https://asec.ahnlab.com/ko/52076/). 

 Mitigation: ['Ensure the integrity of software installers by verifying checksums and digital signatures before installation.', 'Regularly update antivirus and endpoint protection solutions to detect and block malicious software.', 'Implement strict access controls and monitoring on systems that download and execute software from external sources.', 'Educate users about the risks of downloading software from unverified sources and encourage the use of trusted and verified software providers.'] 

 Detailed Steps for mitigation: ['Verify the integrity of downloaded files using MD5/SHA-256 checksums.', 'Enable real-time protection features in antivirus software.', 'Configure systems to require administrative privileges for software installations.', 'Regularly review and update firewall and security policies to block malicious traffic.', 'Conduct regular security training for employees to recognize phishing and malware distribution tactics.'] 

 Detection Signature: {'Service': 'N/A (General detection of malicious activity)', 'Port': 'N/A (General detection of malicious activity)', 'Severity': 'Critical', 'Incident': 'SparkRAT distribution via VPN installer', 'Signature name': 'SparkRAT dropper detection', 'Internal checks': ['Ensure all software downloads are vetted and verified before execution.', "Monitor task scheduler for unusual tasks like 'svchost.exe' in non-standard directories.", 'Check for the presence of known malicious files and processes associated with SparkRAT.'], 'External scanning': ['Monitor network traffic for connections to known malicious IPs and domains.', 'Inspect network traffic for unencrypted HTTP connections used by SparkRAT.']} 

 IoCs: ['MD5: 2e3ce7d90d988e1b0bb7ffce1731b04b, 54dd763bca743cbdbdfe709d9ab1d0db, 5b78c44262ebcb4ce52e75c331683b5b, 7923f9e0e28ceecdb34e924f2c04cda0, a5950704dfa60ba5362ec4a8845c25b2', 'URL: http[:]//59[.]22[.]167[.]217[:]34646/, https[:]//gwekekccef[.]webull[.]day/', '*Additional IOCs: MD5: 0574f906b97f2e74ae49b6e900b5c60d, 15d24570f3844987acce866d6541ba21, 162e17324f63f2e1d2c32f7c842b3917, 4a9369fcff5e934ab644c9aca6e42532, 8fce3a48d46b9c3d252806e7292647e6; URL: http[:]//54[.]180[.]27[.]29/cc/himart/api/kodbox-main/gr[.]png, http[:]//54[.]180[.]27[.]29/cc/himart/api/kodbox-main/ms-update[.]exe, https[:]//aggbvdfbbafdg[.]moeuda[.]link/* (https://asec.ahnlab.com/en/53267/)'] 

 Additional Information: SparkRAT is developed in Go language and its source code is available on GitHub. *It supports multiple OS platforms, including Windows, Linux, and MacOS* (https://asec.ahnlab.com/jp/52871/). The x86 SparkRAT variant utilizes the HTTP protocol instead of HTTPS, making it easier to detect unencrypted transmissions. *Previously identified file detections include Dropper/Win.Agent.C5421402 and Trojan/Win.Generic.C5228761* (https://asec.ahnlab.com/jp/52871/). *Recent detections also include Dropper/Win.Agent.C5431031, Downloader/Win.Agent.C5431029, Backdoor/Win.SparkRAT.C5431028, Dropper/Win.MeshAgent.C5431027, and Trojan/Win.MeshAgent.C5431026* (https://asec.ahnlab.com/en/53267/). *SparkRAT enables remote command execution, file and process control, payload downloads, and information collection* (https://advisory.eventussecurity.com/advisory/sparkrat-malware-being-distributed-within-a-korean-vpn-installer/). 


# Related articles (describing the same threat) 
['https://asec.ahnlab.com/en/52899/', 'https://asec.ahnlab.com/ko/52076/', 'https://asec.ahnlab.com/jp/52871/', 'https://asec.ahnlab.com/en/53267/', 'https://advisory.eventussecurity.com/advisory/sparkrat-malware-being-distributed-within-a-korean-vpn-installer/']
