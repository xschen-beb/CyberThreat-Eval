Source: [https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection](https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection
- https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection/
- https://www.tanium.com/blog/qbot-malware-in-svg-files-cyber-threat-intelligence-roundup/
- https://www.scworld.com/brief/exploitation-of-svg-attachments-in-phishing-on-the-rise

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Phishing emails increasingly use SVG attachments to evade detection and distribute QBot malware 

#### Root cause 
 The root cause behind the incident is the use of SVG files in phishing emails, which can embed HTML and JavaScript code, enabling attackers to display phishing forms or deploy malware while evading detection by security software. *These attachments can be mistaken for official documents or requests for more information (https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection/). QBot malware uses SVG files to perform HTML smuggling and locally assemble a malicious payload on victims’ devices (https://www.tanium.com/blog/qbot-malware-in-svg-files-cyber-threat-intelligence-roundup/). MalwareHunterTeam discovered SVG attachments showing phony Excel spreadsheets with login forms that allowed data exfiltration, spoofing official information requests, and redirecting to phishing forms (https://www.scworld.com/brief/exploitation-of-svg-attachments-in-phishing-on-the-rise)*. 

#### Threat actor/group/campaign 
 Not specifically mentioned in the blog, but references to MalwareHunterTeam and Qbot malware campaigns. 

#### Organization/industry/location 
 General Internet users; no specific organization or industry is mentioned. 

#### Start date – End date 
 *November 17, 2024* (https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection/). 

#### MITRE TTPs 
 - T1566.002: Phishing: Spearphishing Link
- T1203: Exploitation for Client Execution
- T1059.007: Command and Scripting Interpreter: JavaScript 

#### Impact 
 Potential loss of credentials and malware infection for email recipients. *These phishing forms can steal credentials by displaying fake login forms, such as a fake Excel spreadsheet with a built-in login form (https://www.bleepingcomputer.com/news/security/phishing-emails-increasingly-use-svg-attachments-to-evade-detection/). QBot malware can hijack email threads, making the phishing emails appear more legitimate (https://www.tanium.com/blog/qbot-malware-in-svg-files-cyber-threat-intelligence-roundup/). SVG attachments can redirect to phishing forms* (https://www.scworld.com/brief/exploitation-of-svg-attachments-in-phishing-on-the-rise). 

#### Mitigation Steps 
 - Be cautious of unexpected email attachments, especially SVG files.
- Implement email filtering to block SVG attachments unless expected.
- Educate users to recognize and report phishing attempts.
- Use advanced threat detection solutions that can analyze SVG file contents.
- Employ endpoint protection solutions that can detect malicious scripts. 

#### Detection Signature 
 Service: Email security
Port: N/A (Email-based)
Severity: High
Incident: Phishing emails with SVG attachments
Signature name: “Phishing email with SVG attachment”
Internal checks:
- Check email filters for SVG attachments – Email server
- Analyze SVG attachments for embedded HTML and JavaScript – Email security appliance
External scanning:
- Monitor incoming emails for SVG attachments
- Analyze content of SVG attachments for phishing forms and malicious scripts 

#### IoCs:
- hash_sha256: ae08802026984b53438e1b3b2f2aa21839c165fae88493bfb8f31c4d064b7068 ([link](https://www.virustotal.com/gui/file/ae08802026984b53438e1b3b2f2aa21839c165fae88493bfb8f31c4d064b7068)) 

- hash_sha256: 0e857464f66465ad0308d8f779b2448a0a4575556e2cffee2e574ce99ddf18ad ([link](https://www.virustotal.com/gui/file/0e857464f66465ad0308d8f779b2448a0a4575556e2cffee2e574ce99ddf18ad)) 

- For more IoCs, please refer to the above links. 


