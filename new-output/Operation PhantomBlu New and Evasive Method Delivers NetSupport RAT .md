Source: [https://perception-point.io/blog/operation-phantomblu-new-and-evasive-method-delivers-netsupport-rat/](https://perception-point.io/blog/operation-phantomblu-new-and-evasive-method-delivers-netsupport-rat/)

# Operation PhantomBlu New and Evasive Method Delivers NetSupport RAT 

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Operation PhantomBlu: New and Evasive Method Delivers NetSupport RAT 

 Root cause: The root cause behind the incident includes the manipulation of OLE (Object Linking and Embedding) templates within Microsoft Office documents to execute malicious code. This technique leverages legitimate email services (SendInBlue) and social engineering to deliver a phishing email containing a password-protected Word document, which initiates a PowerShell script to deploy the NetSupport RAT. *This is the first observed instance of T1221 being used to deliver NetSupport RAT* (https://cybersecuritynews.com/operation-phantomblu/). 

 Threat Actor/group/campaign: The threat actors behind the PhantomBlu campaign. 

 Organization/industry/location: US-based organizations. 

 Start date – End date: Not specified in the document. 

 MITRE TTPs: ['Remote Access Software (T1219)', 'Windows Management Instrumentation (T1047)', 'Hide Artifacts: Hidden Files and Directories (T1564/003)', 'Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (T1547/001)', 'Hide Artifacts: Hidden Window (T1564/003)', 'Modify Registry (T1112)', 'Obfuscated Files or Information: Software Packing (T1406/002)', 'System Network Connections Discovery (T1049)', 'Template Injection (T1221)'] 

 Impact: Hundreds of employees in various US-based organizations were targeted. *The campaign included keylogging, file transfer, and lateral movement* (https://cybersecuritynews.com/operation-phantomblu/). 

 Mitigation: ['Educate employees on the risks associated with phishing and social engineering.', 'Implement advanced email filtering solutions to detect and block phishing emails.', 'Regularly update and patch software to mitigate vulnerabilities.', 'Disable OLE object execution in Office documents.', 'Restrict execution policies for PowerShell scripts.', 'Use anti-malware and endpoint detection and response (EDR) solutions to identify and block malicious activities.', 'Regularly review and monitor registry keys for unauthorized changes.'] 

 Detailed Steps for mitigation: {'Educate Employees': 'Conduct regular training on phishing awareness and safe email practices.', 'Email Filtering': 'Deploy advanced email security solutions that can detect and block phishing attempts.', 'Software Patching': 'Ensure all software, especially Microsoft Office, is up to date with the latest security patches.', 'Disable OLE Execution': 'Configure Office settings to disable OLE object execution or prompt users before executing them.', 'Restrict PowerShell': 'Implement PowerShell execution policies to only allow signed scripts.', 'Endpoint Security': 'Use EDR solutions to continuously monitor and respond to threats on endpoints.', 'Registry Monitoring': 'Utilize tools to monitor and alert on suspicious registry changes, particularly in auto-start locations.'} 

 Detection Signature: {'Service': 'Microsoft Office', 'Port': 'N/A', 'Severity': 'Critical', 'Incident': 'Operation PhantomBlu', 'Signature name': 'OLE Template Manipulation', 'Internal checks': {'Setting1': 'Disable OLE object execution in Office documents.', 'Setting2': 'Monitor for PowerShell script executions triggered by Office documents.', 'Setting3': 'Regularly review and audit registry keys for unauthorized entries.'}, 'External scanning': 'Monitor for phishing emails with suspicious OLE links or prompts for enabling editing.'} 

 IoCs: {'Hashes (SHA-256)': ['Email: 16e6dfd67d5049ffedb8c55bee6ad80fc0283757bc60d4f12c56675b1da5bf61', 'Docx: 1abf56bc5fbf84805ed0fbf28e7f986c7bb2833972793252f3e358b13b638bb1', 'Injected ZIP: 95898c9abce738ca53e44290f4d4aa4e8486398de3163e3482f510633d50ee6c', 'LNK file: d07323226c7be1a38ffd8716bc7d77bdb226b81fd6ccd493c55b2711014c0188', 'Final ZIP: 94499196a62341b4f1cd10f3e1ba6003d0c4db66c1eb0d1b7e66b7eb4f2b67b6', 'Client32.exe: 89f0c8f170fe9ea28b1056517160e92e2d7d4e8aa81f4ed696932230413a6ce1'], 'URLs and Hostnames': ['yourownmart[.]com/solar[.]txt', 'firstieragency[.]com/depbrndksokkkdkxoqnazneifidmyyjdpji[.]txt', 'yourownmart[.]com', 'firstieragency[.]com', 'parabmasale[.]com', 'tapouttv28[.]com'], 'IP Addresses': ['192[.]236[.]192[.]48', '173[.]252[.]167[.]50', '199[.]188[.]205[.]15', '46[.]105[.]141[.]54'], 'Others': ['Message ID contains: “sendinblue.com”', 'Return Path contains: “sender-sib.com”']} 


# Related articles (describing the same threat) 
['https://perception-point.io/blog/operation-phantomblu-new-and-evasive-method-delivers-netsupport-rat/', 'https://cybersecuritynews.com/operation-phantomblu/']
