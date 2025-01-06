Source: [https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection](https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection
- https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection/
- https://www.darkreading.com/threat-intelligence/flexible-structure-zip-archives-exploited-hide-malware-undetected
- https://cybersecuritynews.com/hackers-employ-zip-file-concatenation/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: ZIP File Concatenation Technique to Evade Detection 

#### Root cause 
 The root cause behind the incident is the exploitation of how different ZIP parsers and archive managers handle concatenated ZIP files. Threat actors create multiple separate ZIP archives, hiding malicious payloads in one of them, and then concatenate these files. Depending on the ZIP parser used, the malicious payload may remain hidden from detection. *Attackers also deliver a variant of the SmokeLoader Trojan hidden in malicious attachments delivered via phishing* (https://www.darkreading.com/threat-intelligence/flexible-structure-zip-archives-exploited-hide-malware-undetected). *Phishing email disguised as a shipping notification contains an attachment SHIPPING_INV_PL_BL_pdf.rar, which appears to be a RAR file but is actually a concatenated ZIP archive with a malicious executable SHIPPING_INV_PL_BL_pdf.exe* (https://cybersecuritynews.com/hackers-employ-zip-file-concatenation/). 

#### Threat actor/group/campaign 
 Not specified 

#### Organization/industry/location 
 Windows users (general targeting) 

#### Start date – End date 
 November 10, 2024 (discovered date) 

#### MITRE TTPs 
 ['T1204 (User Execution)', 'T1059.001 (Command and Scripting Interpreter: PowerShell)', 'T1566 (Phishing)'] 

#### Impact 
 Potential for widespread malicious payload delivery without detection. No specific number of records or devices affected is provided. 

#### Mitigation Steps 
 ['Use security solutions that support recursive unpacking to detect concatenated ZIP files.', 'Treat emails attaching ZIP or other archive file types with suspicion.', 'Implement filters in critical environments to block ZIP and other related file extensions.', 'Regularly update and patch ZIP parsing and archive management tools to handle concatenated files correctly.', 'Educate users about the risks of opening unexpected or suspicious email attachments.'] 

#### Detection Signature 
 {'Service': 'ZIP parsers (7zip, WinRAR, Windows File Explorer)', 'Port': 'Not applicable', 'Severity': 'High', 'Incident': 'Malicious ZIP file concatenation', 'Signature name': 'Concatenated ZIP file detection', 'Internal checks': ['Ensure security solutions support recursive unpacking.', 'Implement email filtering for suspicious attachments.', 'Regularly update ZIP parsing tools.'], 'External scanning': ['Detect emails with concatenated ZIP files.', 'Monitor for unusual ZIP parsing behavior.']} 

#### IoCs: No IoCs found. The attack was spotted by Perception Point, involving AutoIt scripting language and a fake shipping notice disguised as a RAR archive. *The phishing attack starts with an email marked with 'High Importance' and includes an attachment, SHIPPING_INV_PL_BL_pdf.rar, which is actually a concatenated zip file containing a variant of the Trojan malware family SmokeLoader. The malicious executable SHIPPING_INV_PL_BL_pdf.exe is revealed by WinRAR.* (https://www.darkreading.com/threat-intelligence/flexible-structure-zip-archives-exploited-hide-malware-undetected) (https://cybersecuritynews.com/hackers-employ-zip-file-concatenation/). 


