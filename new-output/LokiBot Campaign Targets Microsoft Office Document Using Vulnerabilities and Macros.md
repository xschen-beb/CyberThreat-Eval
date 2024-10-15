Source: [https://www.fortinet.com/blog/threat-research/lokibot-targets-microsoft-office-document-using-vulnerabilities-and-macros](https://www.fortinet.com/blog/threat-research/lokibot-targets-microsoft-office-document-using-vulnerabilities-and-macros)

# LokiBot Campaign Targets Microsoft Office Document Using Vulnerabilities and Macros

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: LokiBot Campaign Targets Microsoft Office Document Using Vulnerabilities and Macros 

 Root cause: The root cause behind the incident includes the exploitation of known remote code execution vulnerabilities in Microsoft Office documents, specifically CVE-2021-40444 and CVE-2022-30190 (Follina). These vulnerabilities allowed attackers to embed malicious macros within Microsoft documents, which, when executed, dropped the LokiBot malware onto the victim's system. *FortiGuard Labs* (https://hackread.com/lokibot-malware-malicious-macros-word-docs/) discovered the campaign and revealed the use of *Cuttly URL shortener* (https://hackread.com/lokibot-malware-malicious-macros-word-docs/) to redirect to *GoFile cloud file-sharing* (https://hackread.com/lokibot-malware-malicious-macros-word-docs/). *Ankura Consulting Group, LLC* (https://www.lexology.com/library/detail.aspx?g=ee99f093-c472-431d-9c20-04dc6898bd14) noted that one document contained an *embedded link within an XML file* while another used a *VBA script to download an injector*. 

 Threat Actor/group/campaign: Likely cybercriminals using LokiBot malware. Specific threat actor/group not mentioned. 

 Organization/industry/location: *Healthcare sector* (https://www.hhs.gov/sites/default/files/lokibot-malware-analyst-note-tlpclear.pdf); Windows users globally. 

 Start date – End date: The campaign was identified in May 2023. 

 MITRE TTPs: - T1203 (Exploitation for Client Execution)
- T1059.005 (Command and Scripting Interpreter: Visual Basic)
- T1071 (Application Layer Protocol)
- T1027 (Obfuscated Files or Information)
- T1055 (Process Injection)
- T1070 (Indicator Removal on Host) 

 Impact: Control and collection of sensitive information from a victim’s device, including *data exfiltration* (https://www.hhs.gov/sites/default/files/lokibot-malware-analyst-note-tlpclear.pdf). The exact number of impacted devices or financial losses is not mentioned. 

 Mitigation: - Keep Microsoft Office applications and Windows operating systems updated with the latest security patches.
- Disable macros in Microsoft Office documents by default and only enable them if absolutely necessary and from trusted sources.
- Use advanced endpoint protection solutions like FortiGuard to detect and block malware.
- Educate users on the risks of opening documents from unknown sources and clicking on suspicious links.
- Implement network security measures to block access to known malicious C2 servers and IP addresses. 

 Detection Signature: - Service: Microsoft Office
- Severity: Critical
- Incident: LokiBot Campaign
- Signature name: “Malicious Macro in Microsoft Office Document”
- Internal checks:
    - Setting1: Ensure macros are disabled by default in Microsoft Office applications.
    - Setting2: Regularly scan for known vulnerabilities (CVE-2021-40444, CVE-2022-30190) and apply patches.
    - Setting3: Monitor for unusual Office document behavior such as new processes being spawned.
- External scanning:
    - Scan for vulnerable versions of Microsoft Office.
    - Monitor for communication with known malicious C2 servers. 

 IoCs: - C2: 95[.]164[.]23[.]2
- Files:
    - 17d95ec93678b0a73e984354f55312dda9e6ae4b57a54e6d57eb59bcbbe3c382
    - 23982d2d2501cfe1eb931aa83a4d8dfe922bce06e9c327a9936a54a2c6d409ae
    - 9eaf7231579ab0cb65794043affb10ae8e4ad8f79ec108b5302da2f363b77c93
    - da18e6dcefe5e3dac076517ac2ba3fd449b6a768d9ce120fe5fc8d6050e09c55
    - 2e3e5642106ffbde1596a2335eda84e1c48de0bf4a5872f94ae5ee4f7bffda39
    - 80f4803c1ae286005a64ad790ae2d9f7e8294c6e436b7c686bd91257efbaa1e5
    - 21675edce1fdabfee96407ac2683bcad0064c3117ef14a4333e564be6adf0539
    - 4a23054c2241e20aec97c9b0937a37f63c30e321be01398977e13228fa980f29. 

 Additional Information: *TLP:WHITE* (https://www.hhs.gov/sites/default/files/lokibot-malware-analyst-note-tlpclear.pdf). *Lure images of Word error* (https://www.lexology.com/library/detail.aspx?g=ee99f093-c472-431d-9c20-04dc6898bd14) were used to trick users into enabling editing. 


# Related articles (describing the same threat) 
['https://www.fortinet.com/blog/threat-research/lokibot-targets-microsoft-office-document-using-vulnerabilities-and-macros', 'https://www.hhs.gov/sites/default/files/lokibot-malware-analyst-note-tlpclear.pdf', 'https://hackread.com/lokibot-malware-malicious-macros-word-docs/', 'https://www.lexology.com/library/detail.aspx?g=ee99f093-c472-431d-9c20-04dc6898bd14']
