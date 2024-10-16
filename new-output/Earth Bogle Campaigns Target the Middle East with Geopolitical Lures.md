Source: [https://www.trendmicro.com/en_us/research/23/a/earth-bogle-campaigns-target-middle-east-with-geopolitical-lures.html](https://www.trendmicro.com/en_us/research/23/a/earth-bogle-campaigns-target-middle-east-with-geopolitical-lures.html)

# Earth Bogle Campaigns Target the Middle East with Geopolitical Lures

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Earth Bogle Campaign 

 Root cause: The root cause behind the incident is the use of public cloud storage services like files.fm and failiem.lv to host malware, and the distribution of malicious content via compromised web servers. The campaign leverages geopolitical-themed lures to entice victims to open a malicious Microsoft Cabinet (CAB) archive file masquerading as a sensitive audio file. Distribution mechanisms include social media, file sharing services like OneDrive, or phishing emails. An obfuscated VBS dropper retrieves the malware from a compromised or spoofed host, followed by a PowerShell script responsible for injecting NjRAT into the compromised machine. *NjRAT has capabilities like logging keystrokes, accessing the victim's camera, and stealing credentials* (https://malpedia.caad.fkie.fraunhofer.de/details/win.njrat). 

 Threat Actor/group/campaign: Earth Bogle campaign, using NjRAT malware (also known as Bladabindi) *and associated with AQUATIC PANDA, Earth Lusca, and the Gorgon Group* (https://malpedia.caad.fkie.fraunhofer.de/details/win.njrat). 

 Organization/industry/location: The campaign targets individuals and organizations in the Middle East and North Africa. 

 Start date – End date: Ongoing since at least mid-2022. 

 MITRE TTPs: ['T1193: Spear Phishing Attachment', 'T1071: Application Layer Protocol', 'T1059: Command and Scripting Interpreter', 'T1105: Ingress Tool Transfer', 'T1090: Connection Proxy'] 

 Impact: The extent of the impact is not quantified in terms of specific records or financial loss, but it involves unauthorized access to infected systems capable of data theft, remote control, and other malicious actions. 

 Mitigation: ['Ensure all systems have updated security solutions.', 'Properly secure cloud infrastructures.', 'Educate users on recognizing phishing attacks and sensational lures.', 'Avoid opening suspicious archive files, especially from untrusted sources.', 'Implement a multilayered defensive strategy that can detect, scan, and block malicious URLs.'] 

 Detection Signature: {'Service': 'Public cloud storage services (files.fm, failiem.lv)', 'Port': 'Various (HTTP/HTTPS, typically ports 80 and 443)', 'Severity': 'Critical', 'Incident': 'Earth Bogle Campaign', 'Signature name': 'Geopolitical-themed NjRAT distribution', 'Internal checks': ['Ensure all systems have updated security solutions.', 'Monitor and restrict access to public cloud storage services.', 'Educate users on recognizing phishing attacks and sensational lures.'], 'External scanning': ['Monitor for suspicious CAB files and VBS scripts.', 'Scan for low detection rate files on VirusTotal.']} 

 IoCs: ['SHA256: a7e2b399b9f0be7e61977b51f6d285f8d53bd4b92d6e11f74660791960b813da', 'SHA256: 4985b6e286020de70f0b74d457c7e387463ea711ec21634e35bc46707dfe4c9b', 'Malicious domain: gpla[.]gov[.]ly', 'SHA256: 6560ef1253f239a398cc5ab237271bddd35b4aa18078ad253fd7964e154a2580', 'SHA256: 78ac9da347d13a9cf07d661cdcd10cb2ca1b11198e4618eb263aec84be32e9c8'] 

 These IoCs can be used to detect potential compromises related to this campaign.: Incident: Earth Bogle Campaign 


# Related articles (describing the same threat) 
['https://www.trendmicro.com/en_us/research/23/a/earth-bogle-campaigns-target-middle-east-with-geopolitical-lures.html', 'https://advisory.eventussecurity.com/advisory/earth-bogle-campaign-unleashes-njrat-trojan-on-middle-east-and-north-africa/', 'https://malpedia.caad.fkie.fraunhofer.de/details/win.njrat']
