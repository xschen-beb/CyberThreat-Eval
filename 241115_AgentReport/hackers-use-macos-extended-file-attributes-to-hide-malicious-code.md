Source: [https://www.bleepingcomputer.com/news/security/hackers-use-macos-extended-file-attributes-to-hide-malicious-code](https://www.bleepingcomputer.com/news/security/hackers-use-macos-extended-file-attributes-to-hide-malicious-code)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/hackers-use-macos-extended-file-attributes-to-hide-malicious-code
- https://www.bleepingcomputer.com/news/security/hackers-use-macos-extended-file-attributes-to-hide-malicious-code/
- https://www.infosecurity-magazine.com/news/lazarus-extended-attributes-macos/
- https://hackread.com/lazarus-group-macos-rustyattr-trojan-fake-job-pdfs/
- https://thehackernews.com/2024/11/new-rustyattr-malware-targets-macos.html
- https://www.rewterz.com/threat-advisory/lazarus-group-uses-new-rustyattr-malware-for-extended-attribute-abuse-to-target-macos-active-iocs

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: RustyAttr macOS Malware 

#### Root cause 
 The root cause behind the incident includes the exploitation of macOS extended file attributes to hide malicious code. This technique involves embedding a shell script within the extended attributes of files, effectively evading detection from standard security mechanisms. *The malicious apps use the Tauri framework to facilitate the attack and employ decoy PDF documents from a pCloud instance to evade detection and reduce user suspicion. Additionally, the Lazarus Group has been observed using command-and-control (C2) servers to fetch additional malicious scripts and has referenced previous campaigns like RustBucket malware from 2023. Group-IB has noted this activity and attributes it to Lazarus with moderate confidence.* (https://www.bleepingcomputer.com/news/security/hackers-use-macos-extended-file-attributes-to-hide-malicious-code/) *The report was observed on November 13, 2024.* (https://www.infosecurity-magazine.com/news/lazarus-extended-attributes-macos/) *The attack also involves fake job PDFs, leveraging a JavaScript file named 'preload.js' to interact with the hidden script within a custom extended attribute named 'test'.* (https://hackread.com/lazarus-group-macos-rustyattr-trojan-fake-job-pdfs/) *The Singaporean cybersecurity company, Group-IB, discovered that the malicious applications display decoy PDFs related to gaming projects and use HTML webpages rendered with WebView, while malicious JavaScript executes via a Rust backend.* (https://thehackernews.com/2024/11/new-rustyattr-malware-targets-macos.html) *Threat actors have been discovered using a novel method to smuggle a new malware known as RustyAttr by abusing extended attributes for macOS files. The malicious programs found by researchers are constructed using Tauri, a cross-platform desktop application framework, and signed with a leaked certificate that has since been revoked by Apple.* (https://www.rewterz.com/threat-advisory/lazarus-group-uses-new-rustyattr-malware-for-extended-attribute-abuse-to-target-macos-active-iocs) 

#### Threat actor/group/campaign 
 Lazarus Group (attributed with moderate confidence) 

#### Organization/industry/location 
 The specific targeted organizations or industries are not mentioned, but it is aligned with Lazarus� typical targets, which often include entities related to cryptocurrency investments. 

#### Start date � End date 
 Not explicitly stated in the report. *The campaign has been active since May 2024.* (https://hackread.com/lazarus-group-macos-rustyattr-trojan-fake-job-pdfs/) 

#### MITRE TTPs 
 ['T1059.004 (Command and Scripting Interpreter: Unix Shell)', 'T1190 (Exploit Public-Facing Application)', 'T1140 (Deobfuscate/Decode Files or Information)'] 

#### Impact 
 The exact number of impacted devices or the financial losses are not provided. However, the use of this sophisticated technique implies a significant risk to potentially large numbers of macOS users, particularly those involved in cryptocurrency investments. *The malicious files pass detection tests on Virus Total and are signed using leaked certificates, though Apple has since revoked them.* (https://www.bleepingcomputer.com/news/security/hackers-use-macos-extended-file-attributes-to-hide-malicious-code/) 

#### Mitigation Steps 
 ['Regularly update and patch macOS and all installed software to fix known vulnerabilities.', 'Use comprehensive security solutions that can analyze extended file attributes and detect hidden scripts.', 'Monitor system logs and use tools to check for unexpected extended attributes (`xattr` command in macOS).', 'Revoke any potentially compromised certificates and ensure apps are notarized by Apple.', "Educate users about the risks of downloading and running untrusted applications and files, particularly those related to cryptocurrency. *Keep Apple's Gatekeeper protections enabled to prevent unsigned or unnotarized applications from running.* (https://www.infosecurity-magazine.com/news/lazarus-extended-attributes-macos/)", '*Verify the source and legitimacy of job-related PDFs before downloading or executing them.* (https://hackread.com/lazarus-group-macos-rustyattr-trojan-fake-job-pdfs/)', '*Block all threat indicators at your respective controls. Search for indicators of compromise (IoCs) in your environment utilizing your respective security controls.* (https://www.rewterz.com/threat-advisory/lazarus-group-uses-new-rustyattr-malware-for-extended-attribute-abuse-to-target-macos-active-iocs)'] 

#### Detection Signature 
 {'Service': 'macOS file system', 'Port': 'N/A', 'Severity': 'High', 'Incident': 'RustyAttr macOS Malware', 'Signature name': 'Extended Attributes Malware Detection', 'Internal checks': ["Setting1: Check for files with suspicious or unexpected extended attributes using the 'xattr' command.", 'Setting2: Monitor for the execution of shell scripts from extended attributes.', 'Setting3: Ensure the integrity of app certificates and verify notarization status.'], 'External scanning': 'N/A (focus is on internal file system checks)'} 

#### IoCs:
- domain: support.cloudstore.business ([link](https://www.rewterz.com/threat-advisory/lazarus-group-uses-new-rustyattr-malware-for-extended-attribute-abuse-to-target-macos-active-iocs))

- domain: support.docsend.site ([link](same as above))

- ip: 104.168.165.203 ([link](same as above))

- ip: 104.168.157.45 ([link](same as above))

- hash_md5: 53b68b9304a0462761917608ca4e60e7 ([link](same as above))

- hash_md5: 3d14dd06d85f513dfa96d875fdcc0298 ([link](same as above))

- sha256: 7464850d7d6891418c503d0e1732812d7703d6c1fd5cf3c821f3c202786f9422 ([link](same as above))

- sha256: f3e6e8df132155daf1d428dff61f0ca53ecd02015a0abbe1ad237519ab3cb58e ([link](same as above))

- url: https://filedn.com/lY24cv0IfefboNEIN0I9gqR ([link](same as above))

- For more IoCs, please refer to the above links. 

#### The intention is to monitor and analyze the extended attributes of files within the macOS environment, educating users on safe practices, and ensuring that software is properly vetted and authenticated. 
 Enhanced report now includes specific details about the Tauri framework, decoy PDFs, and the use of pCloud for delivering malicious content. Additionally, information about the detection evasion on Virus Total and revoked certificates adds depth to the impact and mitigation steps. 


