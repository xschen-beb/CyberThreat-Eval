Source: [https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/](https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/)

# Beyond the Horizon Traveling the World on Camaro Dragon’s USB Flash Drives

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Camaro Dragon USB Flash Drive Malware Campaign 

 Root cause: The incident was primarily caused by the use of infected USB drives. The malware utilized a set of tools, including WispRider and HopperTick, which were able to self-propagate through USB drives and networked storage devices *The changes* (https://social.cyware.com/news/self-propagating-chinese-malware-inadvertently-affects-networked-storage-devices-1d4ab4b2). Vulnerable/misconfigured services included lack of proper endpoint protection, insufficient USB device security policies, and the exploitation of legitimate software components (like Symantec and Vivaldi) to side-load malicious DLLs. The infection originated from an employee who attended an Asian conference and used an infected USB drive. The malware campaign also involved a novel Go-based backdoor called TinyNote, capable of bypassing SmadAV, a popular antivirus software in Southeast Asia *The changes* (https://www.keysight.com/blogs/en/tech/nwvs/2023/07/05/threat-simulator-june-2023-update). 

 Threat Actor/group/campaign: Camaro Dragon (linked to Chinese-based espionage groups, Mustang Panda, and LuminousMoth); *TinyNote Backdoor* (https://www.keysight.com/blogs/en/tech/nwvs/2023/07/05/threat-simulator-june-2023-update) 

 Organization/industry/location: European healthcare institution, with evidence of infections in Myanmar, South Korea, Great Britain, India, and Russia. 

 Start date – End date: Early 2023 (exact dates not specified) 

 MITRE TTPs: ['T1090: Connection Proxy', 'T1071: Application Layer Protocol', 'T1059: Command and Scripting Interpreter', 'T1105: Remote File Copy', 'T1027: Obfuscated Files or Information', 'T1074: Data Staged', 'T1055: Process Injection'] 

 Impact: The self-propagating nature of the malware led to widespread infections across multiple countries. The exact number of records or financial losses is not specified. 

 Mitigation: ['Enforce strict USB device usage policies, including prohibiting unauthorized USB devices.', 'Implement endpoint protection solutions to detect and block malware from USB drives.', 'Regularly update and patch software to prevent exploitation of known vulnerabilities.', 'Use application whitelisting to prevent unauthorized executables from running.', 'Conduct regular security awareness training to educate employees on the risks of using external USB devices.', 'Utilize advanced threat detection solutions like Check Point Harmony Endpoint and Threat Emulation.'] 

 Detection Signature: {'Service': 'Endpoint Protection (e.g., Check Point Harmony Endpoint)', 'Port': 'N/A (local endpoint monitoring)', 'Severity': 'Critical', 'Incident': 'Camaro Dragon USB Flash Drive Malware Campaign', 'Signature name': '“USB Malware Propagation Detection”', 'Internal checks': {'Setting1': 'Monitor for unauthorized USB device connections', 'Setting2': 'Scan for and block execution of files from USB drives', 'Setting3': 'Ensure endpoint protection is up to date and configured to block malware'}, 'External scanning': 'N/A (focus on endpoint monitoring rather than network scanning)'} 

 IoCs: ['EACore.dll: aeacc2d47a88eb68d503f9e30b189641572eb35423df931845f90a4c447ed1be', 'libcef.dll: fc598a686a5a77436684cbd0f72f39033cb70a41d4dbcf5dbab47a7c2522fdda', 'avkkid.dll: 68eb5590d8ad952215cf54741b0ed6204c19bba4dcb8d704883e007f16de5028', 'RiotClient.dat: 6c4226aa2f8bb646f753ffd282cf4624f6bc8e5ca8a2cb2373f640a2a29cdd95', 'LDVPOCX.OCX: 7d8b568746a643aa0470b14f271f681dd3b09dbc08c893b191d1d6607b86c501', 'vivaldi_elf.dll: 3738e414f43d3b213cf7475a8bb616a3379c09e90c0ba5c6ac0e398d2967ca95', 'EACore.dat: 7752fc0c747149d45deeec1023fef8ca73f83a154643531ae9db9cb89b6ce1dc', 'EACore.dll: 464888b81e4d67aad73b245efa6442fecf8221abe3ec74d4cd180e4beedaddc6', 'ZIPDLL.dll: 0279a0a3effc688097eb14d4bd6f1ab8be86f880d01952af7e2b55c51cf107b1', 'HopperTick: 5c878a05fb54c6d06ca4f66d28906d17a423b1305b6aa9bde19df8e8b3e91c5c', 'Delphi USB Launcher: 491d9f6f4e754a430a29ac6842ee12c43615e33b0e720c61e3f06636559813f7', 'Stealer: ce1615ec67296edd05d9dc9a6a075a4724553fca5398c425372b85170aec2106'] 

 *New Details*: ['Check Point Incident Response Team (CPIRT) investigated the attack and found that it was perpetrated by Camaro Dragon.', 'WispRider bypasses SmadAV, a popular antivirus software in Southeast Asia.', "The malware is part of a toolset labeled 'SSE'.", '*Also utilizes TinyNote and HorseShell* (https://social.cyware.com/news/self-propagating-chinese-malware-inadvertently-affects-networked-storage-devices-1d4ab4b2).', '*Exploits G-DATA Total Security components* (https://social.cyware.com/news/self-propagating-chinese-malware-inadvertently-affects-networked-storage-devices-1d4ab4b2).', "*KeySight's ATI Research Center identified the threat* (https://www.keysight.com/blogs/en/tech/nwvs/2023/07/05/threat-simulator-june-2023-update)."] 


# Related articles (describing the same threat) 
['https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/', 'https://www.infosecurity-magazine.com/news/usb-trojan-camaro-dragon/', 'https://social.cyware.com/news/self-propagating-chinese-malware-inadvertently-affects-networked-storage-devices-1d4ab4b2', 'https://www.keysight.com/blogs/en/tech/nwvs/2023/07/05/threat-simulator-june-2023-update']
