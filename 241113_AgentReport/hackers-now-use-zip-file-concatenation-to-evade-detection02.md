Source: [https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection](https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection
- https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection/
- https://perception-point.io/blog/evasive-concatenated-zip-trojan-targets-windows-users/
- https://www.darkreading.com/threat-intelligence/flexible-structure-zip-archives-exploited-hide-malware-undetected
- https://www.techradar.com/pro/security/windows-machines-are-being-targeted-with-zip-file-workaround
- https://www.techmonitor.ai/cybersecurity/perception-point-new-zip-file-concatenation-exploit/

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Hackers now use ZIP file concatenation to evade detection 

#### Root cause 
 The root cause includes exploitation of different methods ZIP parsers and archive managers handle concatenated ZIP files. This allows malicious payloads to be hidden within seemingly benign compressed archives. *Perception Point discovered a concatenated ZIP archive hiding a trojan during a phishing attack involving a fake shipping notice. The malware utilized AutoIt scripting language to automate malicious tasks. Additionally, the trojan was identified as a variant leveraging AutoIt to execute various malicious activities. The attack targeted ZIP readers such as 7zip, WinRAR, Windows File Explorer, and Winzip, exploiting their different behaviors in handling concatenated archives. Perception Point’s Recursive Unpacker algorithm was highlighted for effectively detecting such threats. A specific variant of the malware, the SmokeLoader Trojan, was found hidden in the attachment SHIPPING_INV_PL_BL_pdf.exe* (https://www.darkreading.com/threat-intelligence/flexible-structure-zip-archives-exploited-hide-malware-undetected). *The attack involved phishing emails warning of a pending invoice or undelivered parcel, tricking victims into downloading and running the malicious attachment. Perception Point also identified another variant hidden in SHIPPING_INV_PL_BL_pdf.rar, which posed risks such as ransomware and banking trojans* (https://www.techmonitor.ai/cybersecurity/perception-point-new-zip-file-concatenation-exploit/). 

#### Threat actor/group/campaign 
 Not specified in the report. 

#### Organization/industry/location 
 Targeted at Windows users (general public). 

#### Start date – End date 
 First reported on November 10, 2024. 

#### MITRE TTPs 
 ['T1071.001: Application Layer Protocol - Web Protocols', 'T1566.001: Phishing - Spearphishing Attachment'] 

#### Impact 
 Potential for undetected malware execution on affected systems. The specific number of records or financial losses is not mentioned. 

#### Mitigation Steps 
 ['Use security solutions that support recursive unpacking to detect concatenated ZIP files.', 'Treat emails attaching ZIPs or other archive file types with suspicion.', 'Implement filters in critical environments to block file extensions related to ZIP and RAR files.', 'Educate users on the risks of opening attachments from unknown or untrusted sources.', 'Regularly update antivirus and endpoint security solutions to recognize and handle such evasion techniques.', 'Consider sandboxing email attachments to detect suspicious behavior before allowing access.'] 

#### Detection Signature 
 {'Service': 'Email Gateway, Endpoint Security', 'Port': 'Not applicable', 'Severity': 'Critical', 'Incident': 'ZIP file concatenation-based evasion', 'Signature name': 'Concatenated ZIP file detection', 'Internal checks': {'Setting1': 'Enable recursive unpacking for ZIP files in antivirus/endpoint security solutions.', 'Setting2': 'Monitor and alert on multi-part ZIP files.', 'Setting3': 'Block or quarantine emails with suspicious or concatenated ZIP attachments.'}, 'External scanning': {'Monitor email traffic for suspicious attachments.': 'Scan attachments for concatenated ZIP files and alert on detection.'}} 

#### IoCs:
- * 

- S 

- m 

- o 

- k 

- e 

- L 

- o 

- a 

- d 

- e 

- r 

-   

- T 

- r 

- o 

- j 

- a 

- n 

- ; 

-   

- S 

- H 

- I 

- P 

- P 

- I 

- N 

- G 

- _ 

- I 

- N 

- V 

- _ 

- P 

- L 

- _ 

- B 

- L 

- _ 

- p 

- d 

- f 

- . 

- e 

- x 

- e 

- ; 

-   

- S 

- H 

- I 

- P 

- P 

- I 

- N 

- G 

- _ 

- I 

- N 

- V 

- _ 

- P 

- L 

- _ 

- B 

- L 

- _ 

- p 

- d 

- f 

- . 

- r 

- a 

- r 

- * 

-   

- ( 

- h 

- t 

- t 

- p 

- s 

- : 

- / 

- / 

- w 

- w 

- w 

- . 

- d 

- a 

- r 

- k 

- r 

- e 

- a 

- d 

- i 

- n 

- g 

- . 

- c 

- o 

- m 

- / 

- t 

- h 

- r 

- e 

- a 

- t 

- - 

- i 

- n 

- t 

- e 

- l 

- l 

- i 

- g 

- e 

- n 

- c 

- e 

- / 

- f 

- l 

- e 

- x 

- i 

- b 

- l 

- e 

- - 

- s 

- t 

- r 

- u 

- c 

- t 

- u 

- r 

- e 

- - 

- z 

- i 

- p 

- - 

- a 

- r 

- c 

- h 

- i 

- v 

- e 

- s 

- - 

- e 

- x 

- p 

- l 

- o 

- i 

- t 

- e 

- d 

- - 

- h 

- i 

- d 

- e 

- - 

- m 

- a 

- l 

- w 

- a 

- r 

- e 

- - 

- u 

- n 

- d 

- e 

- t 

- e 

- c 

- t 

- e 

- d 

- , 

-   

- h 

- t 

- t 

- p 

- s 

- : 

- / 

- / 

- w 

- w 

- w 

- . 

- t 

- e 

- c 

- h 

- m 

- o 

- n 

- i 

- t 

- o 

- r 

- . 

- a 

- i 

- / 

- c 

- y 

- b 

- e 

- r 

- s 

- e 

- c 

- u 

- r 

- i 

- t 

- y 

- / 

- p 

- e 

- r 

- c 

- e 

- p 

- t 

- i 

- o 

- n 

- - 

- p 

- o 

- i 

- n 

- t 

- - 

- n 

- e 

- w 

- - 

- z 

- i 

- p 

- - 

- f 

- i 

- l 

- e 

- - 

- c 

- o 

- n 

- c 

- a 

- t 

- e 

- n 

- a 

- t 

- i 

- o 

- n 

- - 

- e 

- x 

- p 

- l 

- o 

- i 

- t 

- / 

- ) 

- . 

- For more IoCs, please refer to the above links. 


