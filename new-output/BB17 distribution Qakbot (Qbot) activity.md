Source: [https://isc.sans.edu/diary/rss/29592](https://isc.sans.edu/diary/rss/29592)

# BB17 distribution Qakbot (Qbot) activity

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: BB17 distribution Qakbot (Qbot) activity 

 Root cause: The root cause was the use of malicious URLs tagged with BB17 to distribute Qakbot (Qbot) malware. Users were tricked into downloading a ZIP file containing a malicious disk image, which then executed a Qakbot DLL file using *rundll32.exe* (https://isc.sans.edu/diary/29592). *In January 2023, the threat actors began abusing OneNote attachments to deliver Qakbot malware using cURL and PowerShell commands.* (https://darktrace.com/fr/blog/qaknote-infections-a-network-based-exploration-of-varied-attack-paths). 

 Threat Actor/group/campaign: The threat actor or group behind the BB17-tagged distribution campaign is not explicitly mentioned, but it is associated with the distribution of Qakbot (Qbot) malware. 

 Organization/industry/location: Not specified in the report. The incident appears to be part of a broader campaign targeting multiple users. 

 Start date – End date: The infection was generated on 2023-02-28. 

 MITRE TTPs: ['T1071.001: Application Layer Protocol: Web Protocols', 'T1190: Exploit Public-Facing Application', 'T1071.004: Application Layer Protocol: DNS', 'T1105: Ingress Tool Transfer'] 

 Impact: The impact includes the compromise of systems through Qakbot malware, which can lead to data theft, credential harvesting, and further malware distribution. 

 Mitigation: ['Secure email gateways to prevent malicious attachments and links.', 'Implement URL filtering to block known malicious domains and URLs.', 'Educate employees about phishing and social engineering tactics.', 'Use endpoint protection solutions with behavioral analysis to detect malicious activities.', 'Regularly update and patch systems to prevent exploitation of vulnerabilities.', 'Use network segmentation to limit the spread of malware within a network.', 'Monitor network traffic for unusual patterns that could indicate malware activity.'] 

 Detailed Steps for Mitigation: ['Deploy advanced email security solutions that use machine learning to detect and block phishing attempts.', 'Implement web filtering tools to block access to known malicious sites and URLs.', 'Conduct regular cybersecurity training sessions for employees to recognize and report suspicious emails and links.', 'Ensure all systems and software are up to date with the latest security patches.', 'Use network segmentation to isolate critical systems and data from general user access.', 'Continuously monitor network traffic and set up alerts for unusual activities that could indicate malware infection.'] 

 Detection Signature: {'Service': 'HTTP', 'Port': '80, 443', 'Severity': 'Critical', 'Incident': 'Qakbot infection', 'Signature name': 'Qakbot URL access', 'Internal checks': ['Monitor for access to known Qakbot distribution URLs.', 'Inspect traffic for indicators of Qakbot payloads (ZIP, IMG, DLL).', 'Check for unusual DNS queries associated with Qakbot C2 domains.'], 'External scanning': ['Monitor for GET requests to Qakbot distribution URLs.', 'Detect traffic to known Qakbot C2 IP addresses and ports.']} 

 IoCs: {'Files': ['SHA256: 5fb714dfc9206ab4d188bf3c0cb35c44fbf5246f863c1efd5fdaecaa0891bd7a', 'SHA256: e62a7453020148080614f7bd81ae3c316b1655b60845606120a6d671c5aaac43', 'SHA256: 442420af4fc55164f5390ec68847bba4ae81d74534727975f47b7dd9d6dbdbe7'], 'URLs': ['hxxp://columbiahhc[.]com/UM.php?atu=2', 'hxxp://67.207.84[.]43/Gy0toZ0/2'], 'IP Addresses': ['64.151.228[.]124', '67.207.84[.]43', '80.47.61[.]240', '185.80.53[.]210', '23.111.114[.]52'], 'Domains': ['columbiahhc[.]com', 'openssl.org (legitimate domain for connectivity checks)', 'broadcom.com (legitimate domain for connectivity checks)', 'cisco.com (legitimate domain for connectivity checks)', 'google.com (legitimate domain for connectivity checks)', 'linkedin.com (legitimate domain for connectivity checks)', 'irs.gov (legitimate domain for connectivity checks)', 'microsoft.com (legitimate domain for connectivity checks)', 'oracle.com (legitimate domain for connectivity checks)', 'verisign.com (legitimate domain for connectivity checks)', 'xfinity.com (legitimate domain for connectivity checks)', 'yahoo.com (legitimate domain for connectivity checks)']} 

 Additional Information: *Brad Duncan* (https://isc.sans.edu/diary/29592) reported the infection after finding the URL on *VirusTotal* (https://isc.sans.edu/diary/29592). The Qakbot C2 server at 185.80.53[.]210 used a *self-signed certificate* (https://isc.sans.edu/diary/29592) with details including id-at-countryName=US and id-at-commonName=gifts.com, not associated with the actual gifts.com website. 


# Related articles (describing the same threat) 
['https://isc.sans.edu/diary/rss/29592', 'https://isc.sans.edu/diary/29592', 'https://darktrace.com/fr/blog/qaknote-infections-a-network-based-exploration-of-varied-attack-paths']
