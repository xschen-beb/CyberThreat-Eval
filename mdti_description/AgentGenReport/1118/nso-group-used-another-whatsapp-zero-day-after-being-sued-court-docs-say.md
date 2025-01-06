Source: [https://www.bleepingcomputer.com/news/security/nso-group-used-another-whatsapp-zero-day-after-being-sued-court-docs-say](https://www.bleepingcomputer.com/news/security/nso-group-used-another-whatsapp-zero-day-after-being-sued-court-docs-say)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/nso-group-used-another-whatsapp-zero-day-after-being-sued-court-docs-say
- https://www.bleepingcomputer.com/news/security/nso-group-used-another-whatsapp-zero-day-after-being-sued-court-docs-say/
- https://thehackernews.com/2024/11/nso-group-exploited-whatsapp-to-install.html
- https://www.darkreading.com/endpoint-security/whatsapp-nso-group-operates-pegasus-spyware
- https://therecord.media/pegasus-spyware-infections-detailed-whatsapp-lawsuit
- https://cyberscoop.com/nso-group-used-whatsapp-exploits-after-the-messaging-app-sued-the-spyware-developer-court-filing-says/
- https://vulnera.com/newswire/nso-group-continued-exploiting-whatsapp-to-deliver-pegasus-spyware-post-meta-lawsuit/
- https://www.the420.in/nso-group-used-multiple-exploits-including-zero-click-attack-to-target-whatsapp-users-reveals-meta-despite-lawsuit/

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: NSO Group used another WhatsApp zero-day after being sued 

#### Root cause 
 The root cause behind the incident is the exploitation of multiple zero-day vulnerabilities in WhatsApp by NSO Group. These vulnerabilities, including CVE-2019-3568 (buffer overflow bug) (*The changes* https://thehackernews.com/2024/11/nso-group-exploited-whatsapp-to-install.html), allowed unauthorized access and installation of Pegasus spyware on target devices via zero-click attacks. *NSO developed an exploit named 'Heaven' before April 2018 using a custom WhatsApp client known as 'WhatsApp Installation Server' (WIS)* (https://www.bleepingcomputer.com/news/security/nso-group-used-another-whatsapp-zero-day-after-being-sued-court-docs-say/). *Newly released court documents from the US District Court for the Northern District of California reveal that NSO Group installed and operated the spyware for its customers, making the company directly liable. NSO Group exploited WhatsApp servers to distribute Pegasus to 1,400 mobile phones, according to a lawsuit filed by Meta's WhatsApp in October 2019* (https://www.darkreading.com/endpoint-security/whatsapp-nso-group-operates-pegasus-spyware). *Additional court filings reveal that NSO engaged in reverse-engineering WhatsApp�s code to develop the exploits and that Pegasus was used to target Dubai's Princess Haya* (https://therecord.media/pegasus-spyware-infections-detailed-whatsapp-lawsuit). *NSO's customers had minimal roles, only needing to enter target device numbers, with NSO controlling data retrieval and delivery processes* (https://cyberscoop.com/nso-group-used-whatsapp-exploits-after-the-messaging-app-sued-the-spyware-developer-court-filing-says/). *The 'Erised' exploit, part of the 'Hummingbird' exploit set, was used even after the lawsuit was filed in October 2019 and neutralized after May 2020* (https://vulnera.com/newswire/nso-group-continued-exploiting-whatsapp-to-deliver-pegasus-spyware-post-meta-lawsuit/). *NSO continued targeting WhatsApp users with advanced methods, adapting to new defenses deployed by the app* (https://www.the420.in/nso-group-used-multiple-exploits-including-zero-click-attack-to-target-whatsapp-users-reveals-meta-despite-lawsuit/). 

#### Threat actor/group/campaign 
 NSO Group 

#### Organization/industry/location 
 Various targets worldwide, including politicians, journalists, activists, government officials, diplomats, and U.S. Department of State employees. *Among other targets, NSO's Pegasus spyware was used to hack into the phones of Catalan politicians, journalists, activists, United Kingdom government officials, Finnish diplomats* (https://www.bleepingcomputer.com/news/security/nso-group-used-another-whatsapp-zero-day-after-being-sued-court-docs-say/). 

#### Start date � End date 
 The attacks using the 'Heaven' exploit occurred until December 2018, followed by the 'Eden' exploit in February 2019, and continued with the 'Erised' exploit after May 2019 until sometime after May 2020 (*The changes* https://thehackernews.com/2024/11/nso-group-exploited-whatsapp-to-install.html). 

#### MITRE TTPs 
 ['T1190: Exploit Public-Facing Application', 'T1059: Command and Scripting Interpreter', 'T1003: Credential Dumping', 'T1055: Process Injection'] 

#### Impact 
 The Pegasus spyware was used to target 'between hundreds and tens of thousands' of devices globally. 

#### Mitigation Steps 
 ['Ensure all applications, especially communication platforms like WhatsApp, are regularly updated to the latest versions to include security patches.', 'Use mobile device management (MDM) solutions to enforce security policies on mobile devices.', 'Implement strong endpoint protection to detect and block spyware installations.', 'Educate users about phishing and social engineering attacks to reduce the risk of zero-click vulnerabilities.', 'Monitor network traffic for unusual activities that may indicate spyware communications.'] 

#### Detection Signature 
 {'Service': 'WhatsApp', 'Port': 'N/A (No specific port associated since it uses standard network traffic)', 'Severity': 'Critical', 'Incident': 'Zero-day exploitation', 'Signature name': 'WhatsApp zero-day exploit detection', 'Internal checks': ['Setting1: Monitor for unusual activity or network traffic patterns from WhatsApp application.', 'Setting2: Use mobile threat defense solutions to detect abnormal behaviors in apps.', 'Setting3: Verify the integrity of WhatsApp client installations regularly.'], 'External scanning': ['Look for indicators of compromise (IoCs) such as unauthorized access attempts or data exfiltration patterns.']} 

#### IoCs:
- No IoCs found.

- For more IoCs, please refer to the above links. 


