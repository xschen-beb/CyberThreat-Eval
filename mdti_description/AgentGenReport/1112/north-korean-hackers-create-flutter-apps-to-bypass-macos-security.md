Source: [https://www.bleepingcomputer.com/news/security/north-korean-hackers-create-flutter-apps-to-bypass-macos-security](https://www.bleepingcomputer.com/news/security/north-korean-hackers-create-flutter-apps-to-bypass-macos-security)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/north-korean-hackers-create-flutter-apps-to-bypass-macos-security
- https://www.bleepingcomputer.com/news/security/north-korean-hackers-create-flutter-apps-to-bypass-macos-security/
- https://www.jamf.com/blog/jamf-threat-labs-apt-actors-embed-malware-within-macos-flutter-applications/
- https://thehackernews.com/2024/11/north-korean-hackers-target-macos-using.html
- https://cyberscoop.com/north-korea-macos-malware-flutter-jamf/
- https://www.infosecurity-magazine.com/news/north-korea-hackers-flutter-macos/
- https://www.pcmag.com/news/north-korean-hackers-craft-malware-apps-that-bypass-macos-security

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: North Korean hackers create Flutter apps to bypass macOS security 

#### Root cause 
 The incident stems from exploiting legitimate Apple developer IDs (BALTIMORE JEWISH COUNCIL, INC. (3AKYHFR584) and FAIRBANKS CURLING CLUB INC. (6W69GC943U)) to sign and notarize trojanized apps, bypassing macOS security checks. Google's Flutter platform obfuscates the malicious code within dynamic libraries (dylibs). *Jamf Threat Labs found malware on VirusTotal reported clean due to obfuscation* (https://www.jamf.com/blog/jamf-threat-labs-apt-actors-embed-malware-within-macos-flutter-applications/). *The malware includes Golang and Python variants* (https://thehackernews.com/2024/11/north-korean-hackers-target-macos-using.html). *The malware was embedded in a clone of the popular video game, Minesweeper, from a Github repository* (https://cyberscoop.com/north-korea-macos-malware-flutter-jamf/). The domain used gave a 404 response when accessed by researchers * (https://cyberscoop.com/north-korea-macos-malware-flutter-jamf/). *The malware was identified in applications including New Updates in Crypto Exchange (2024-08-28).app, New Era for Stablecoins and DeFi, CeFi (Protected).app, and Runner.app* (https://www.infosecurity-magazine.com/news/north-korea-hackers-flutter-macos/). *The malicious apps allowed remote access to victims' Macs* (https://www.pcmag.com/news/north-korean-hackers-craft-malware-apps-that-bypass-macos-security). 

#### Threat actor/group/campaign 
 North Korean threat actors (DPRK), potentially a subgroup known as BlueNoroff 

#### Organization/industry/location 
 Apple macOS users and potentially cryptocurrency-focused users 

#### Start date – End date 
 November 2024 (start date of discovery) 

#### MITRE TTPs 
 ['T1071.001: Application Layer Protocol - Web Protocols', 'T1071.003: Application Layer Protocol - Mail Protocols', 'T1204.002: User Execution - Malicious File', 'T1553.002: Subvert Trust Controls - Code Signing', 'T1059.002: Command and Scripting Interpreter - AppleScript'] 

#### Impact 
 Potential compromise of macOS systems, leading to unauthorized access and possible financial theft through cryptocurrency-themed malicious apps. Remote access to victims' systems could result in broader security breaches. 

#### Mitigation Steps 
 ['**Revoke Compromised Certificates**: Ensure Apple revokes the developer IDs used to sign the malicious applications.', '**Update Security Measures**: Update macOS systems to ensure they do not trust the revoked certificates.', '**Monitor Network Traffic**: Set up monitoring for unusual traffic patterns, especially those connecting to known DPRK-linked domains.', '**User Education**: Educate users about the risks of downloading apps from untrusted sources and the importance of verifying app authenticity.', '**Application Whitelisting**: Implement application whitelisting to ensure only approved applications can run on macOS systems.', '**Regular Audits**: Conduct regular security audits and software checks to identify and remove unauthorized applications.', '*Crypto Seed Phrase Storage*: Do not store your crypto seed phrase digitally. Write it down and store it in a secure physical location* (https://www.pcmag.com/news/north-korean-hackers-craft-malware-apps-that-bypass-macos-security).'] 

#### Detection Signature 
 {'Service': 'macOS system', 'Port': 'N/A (application-based detection)', 'Severity': 'Critical', 'Incident': 'North Korean hackers create Flutter apps to bypass macOS security', 'Signature name': '“Flutter-based malicious macOS apps”', 'Internal checks': ['Check for the presence of unauthorized apps that use the Flutter framework.', "Monitor for applications making network requests to known DPRK-linked domains such as 'mbupdate.linkpc.net'.", 'Ensure all applications are signed by verified and trusted developer IDs.'], 'External scanning': ['Scan for network traffic to known malicious domains.', 'Use cybersecurity tools to detect and block the execution of suspicious apps.']} 

#### IoCs: 
- url: http://mbupdate.linkpc.net ([link](https://www.bleepingcomputer.com/news/security/north-korean-hackers-create-flutter-apps-to-bypass-macos-security/)) 

- hash_sha1: 7cb8a9db65009f780d4384d5eaba7a7a5d7197c4 ([link](https://www.jamf.com/blog/jamf-threat-labs-apt-actors-embed-malware-within-macos-flutter-applications/)) 

- hash_sha256: a2cd8cf70629b5bb0ea62278be627e21645466a3 ([link](https://www.jamf.com/blog/jamf-threat-labs-apt-actors-embed-malware-within-macos-flutter-applications/)) 

- For more IoCs, please refer to the above links. 


