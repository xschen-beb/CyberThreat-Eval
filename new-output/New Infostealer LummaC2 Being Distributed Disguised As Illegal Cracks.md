Source: [https://asec.ahnlab.com/en/50594/](https://asec.ahnlab.com/en/50594/)

# New Infostealer LummaC2 Being Distributed Disguised As Illegal Cracks

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: LummaC2 Infostealer Distribution 

 Root cause: The incident is due to LummaC2 malware disguised as illegal software cracks and keygens, distributed via malicious websites, file-sharing services like MediaFire or MEGA, and *Discord CDN and API* (https://socradar.io/malware-analysis-lummac2-stealer/#:~:text=The%20LummaC2%20stealer%20begins%20its,extract%20data%20from%20specific%20applications.). 

 Threat Actor/group/campaign: The specific threat actor group is unidentified, but LummaC2 Stealer, available on the dark web, is distributed by various cybercriminals. 

 Organization/industry/location: General internet users searching for illegal software cracks and keygens. 

 Start date – End date: LummaC2 Stealer was first discovered on March 3, 2023, with additional distributions confirmed on March 12 and 20, 2023. 

 MITRE TTPs: ['T1193: Spearphishing Attachment', 'T1203: Exploitation for Client Execution', 'T1071: Application Layer Protocol (HTTP for C2 communication)', 'T1140: Deobfuscate/Decode Files or Information', '*T1609: Container API* (https://socradar.io/malware-analysis-lummac2-stealer/#:~:text=The%20LummaC2%20stealer%20begins%20its,extract%20data%20from%20specific%20applications.)'] 

 Impact: Potential theft of sensitive information, including browser data, cryptocurrency wallets, system information, email clients, and more. *LummaC2 v4.0 also features Anti-Sandbox Technique employing Trigonometry and Google Cookie Revival* (https://socradar.io/malware-analysis-lummac2-stealer/#:~:text=The%20LummaC2%20stealer%20begins%20its,extract%20data%20from%20specific%20applications.). 

 Mitigation: ['Avoid downloading software from untrusted sources or using illegal software cracks and keygens.', 'Use robust antivirus and anti-malware solutions to detect and block malicious files.', 'Implement network security measures to prevent access to known malicious domains and IPs.', 'Educate users about the risks of downloading and executing files from untrusted sources.', 'Regularly update software and apply security patches to reduce vulnerabilities.', '*Implement Digital Risk Protection (DRP) to monitor for exposed credentials* (https://www.reliaquest.com/blog/common-infostealers/).'] 

 Detection Signature: {'Service': 'HTTP', 'Port': 80, 'Severity': 'Critical', 'Incident': 'LummaC2 Infostealer Distribution', 'Signature name': 'LummaC2 Infostealer HTTP POST', 'Internal checks': ["Monitor for unusual HTTP POST requests to /c2sock with User-Agent 'TeslaBrowser/5.5'.", '*Perform dynamic analysis to detect Trigonometric Mouse Movement* (https://socradar.io/malware-analysis-lummac2-stealer/#:~:text=The%20LummaC2%20stealer%20begins%20its,extract%20data%20from%20specific%20applications.).'], 'External scanning': ['Identify and block communication with known malicious IPs and URLs associated with LummaC2 (e.g., http[:]//82[.]118[.]23[.]50/c2sock).']} 

 IoCs: {'MD5': ['3f4533e8364f96b90d7fcb413fc8b57c', '4589fa36cb0a7210fe79c9a02966a320', '86c8d08a436374893e2280e05aec2f26', '9355477f043a6c5c01fcb4cc6a2ea851', 'a4c1335750fa105529f1ddea90b54117'], 'URL': ['http[:]//82[.]118[.]23[.]50/c2sock', '*http[:]//195[.]123[.]226[.]91/c2sock* (https://socradar.io/malware-analysis-lummac2-stealer/#:~:text=The%20LummaC2%20stealer%20begins%20its,extract%20data%20from%20specific%20applications.)']} 

 *Additional Information*: LummaC2's unusual distribution methods and rising popularity among adversaries can be attributed to its high success rate and intuitive user interface. The number of LummaC2-obtained logs listed for sale increased by 110% from Q3 to Q4 2023. Additionally, LummaC2 makes extensive use of malware advertising to spread its payloads (https://www.reliaquest.com/blog/common-infostealers/). The primary author of the analysis is Joseph Keyes (https://www.reliaquest.com/blog/common-infostealers/). *LummaC2 now includes capabilities to restore expired Google cookies, use Anti-Sandbox techniques employing Trigonometry, and utilizes Discord CDN and API for distribution and control* (https://socradar.io/malware-analysis-lummac2-stealer/#:~:text=The%20LummaC2%20stealer%20begins%20its,extract%20data%20from%20specific%20applications.). 


# Related articles (describing the same threat) 
['https://asec.ahnlab.com/en/50594/', 'https://www.reliaquest.com/blog/common-infostealers/', 'https://socradar.io/malware-analysis-lummac2-stealer/#:~:text=The%20LummaC2%20stealer%20begins%20its,extract%20data%20from%20specific%20applications.']
