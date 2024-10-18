Source: [https://www.reversinglabs.com/blog/r77-rootkit-typosquatting-npm-threat-research](https://www.reversinglabs.com/blog/r77-rootkit-typosquatting-npm-threat-research)

# Typosquatting Campaign Delivers r77 Rootkit via npm

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Typosquatting campaign delivers r77 rootkit via npm 

 Root cause: The root cause includes typosquatting to create a malicious npm package (`node-hide-console-windows`) that mimics a legitimate one (`node-hide-console-window`). The malicious package, with bad code in the `index.js` file, was designed to download and execute malware, including the r77 rootkit and DiscordRAT, from the npm repository * (https://cybersecuritynews.com/malicious-npm-package-deliver-r77-rootkit/). 

 Threat Actor/group/campaign: The specific threat actor or group is not identified in the report, but cybersecurity researchers at ReversingLabs unveiled the campaign * (https://cybersecuritynews.com/malicious-npm-package-deliver-r77-rootkit/). 

 Organization/industry/location: The campaign targeted developers using the npm package repository, potentially affecting various organizations and industries globally. 

 Start date – End date: The attack began at the end of August 2023 and was reported on October 4, 2023. 

 MITRE TTPs: ['T1071.001: Application Layer Protocol: Web Protocols', 'T1190: Exploit Public-Facing Application', 'T1189: Drive-by Compromise', 'T1213: Data from Information Repositories'] 

 Impact: The malicious npm package was downloaded approximately 700 times, potentially affecting numerous developers and their applications. The package included DiscordRAT 2.0, enabling attackers to control infected hosts. *The npm security team removed the package and published a placeholder to protect users* (https://www.npmjs.com/package/node-hide-console-windows) * (https://cybersecuritynews.com/malicious-npm-package-deliver-r77-rootkit/). 

 Mitigation: [{'Secure npm package usage': ['Always verify the package name and publisher before installing.', 'Use automated tools to scan for typosquatting and other malicious behaviors in packages.']}, {'Monitor and analyze npm packages': ['Implement a Software Composition Analysis (SCA) tool to continuously monitor open-source dependencies.', 'Regularly update and patch dependencies to the latest secure versions.']}, {'Enhance access controls': ['Limit the creation and publication of npm packages to verified and trusted accounts.', 'Use multi-factor authentication (MFA) for npm accounts.']}, {'Incident response and recovery': ['Remove the malicious package immediately from all systems.', 'Conduct a thorough investigation to identify and mitigate any further impact.', 'Notify affected users and provide guidance on removing the malicious package and securing their systems.']}] 

 Detection Signature: {'Service': 'npm', 'Port': 'N/A (web-based service)', 'Severity': 'Critical', 'Incident': 'Typosquatting campaign delivers r77 rootkit via npm', 'Signature name': 'Malicious npm package detection', 'Internal checks': [{'Setting1': 'Verify package names and publishers. – In development environments'}, {'Setting2': 'Monitor npm package installation logs for unusual activity. – In development environments'}, {'Setting3': 'Scan npm packages for malicious code and behaviors. – In development environments'}], 'External scanning': ['Unusual network traffic to external servers after npm package installation.', 'Detection of known malicious behaviors (e.g., execution of DiscordRAT 2.0, r77 rootkit).'], '10 versions': "The malicious package had ten published versions matching the legitimate package's version history * (https://cybersecuritynews.com/malicious-npm-package-deliver-r77-rootkit/)."} 

 IoCs: {'npm packages': [{'node-hide-console-windows': ['SHA1: cbb162d0623ff74925ecd4cfff7faef87bf45efd, af0dbb3f13dc432924092783fe30433c24b3c929, 54ea32fa0c81c4da247121aa3c9aaf218b9e27f9, c24c666979267304ed42748153301fdadf46d40e, f58431d141672cde5df4dfa82cb02f1df35fe6b8, 6cc6f76d75887485e0614e74acb2fb5c5bc55628, 74a3f8f5bf9ceefd95ad7102de9049250d501369, 08e4acca3c4a87c90141fc9ef90fe7974e4bccf3, d40b6f93acb2b88a88a42f9fc4163ec4449b68e6, b93898d08b3b6263a168bf9f13a5aa05761ab6c4']}], 'Second stage payloads': ['SHA1: 1563b5814b7dd655892a80be3a6cc740dad282a3, 43feaf19f1a7410358ab8cd51f00b2446d62e798']} 

 Conclusion: Identification and proactive measures against such typosquatting attacks are crucial in maintaining the integrity and security of software supply chains. *Researchers with Fortinet's FortiGuard Labs found dozens of info-stealing packages in the npm registry, including those exfiltrating Kubernetes configurations and SSH keys* (https://securityboulevard.com/2023/10/two-campaigns-drop-malicious-packages-into-npm/). 


# Related articles (describing the same threat) 
['https://www.reversinglabs.com/blog/r77-rootkit-typosquatting-npm-threat-research', 'https://www.npmjs.com/package/node-hide-console-windows', 'https://cybersecuritynews.com/malicious-npm-package-deliver-r77-rootkit/', 'https://securityboulevard.com/2023/10/two-campaigns-drop-malicious-packages-into-npm/']
