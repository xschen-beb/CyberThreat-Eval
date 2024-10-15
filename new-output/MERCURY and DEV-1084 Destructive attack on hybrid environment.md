Source: [https://www.microsoft.com/en-us/security/blog/2023/04/07/mercury-and-dev-1084-destructive-attack-on-hybrid-environment/](https://www.microsoft.com/en-us/security/blog/2023/04/07/mercury-and-dev-1084-destructive-attack-on-hybrid-environment/)

# MERCURY and DEV-1084 Destructive attack on hybrid environment

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: MERCURY and DEV-1084: Destructive attack on hybrid environment 

 Root cause: Exploitation of unpatched vulnerabilities (e.g., Log4j 2) in internet-facing devices, followed by lateral movement and privilege escalation using compromised credentials. 

 Threat Actor/group/campaign: MERCURY (linked to Iranian government, also known as MuddyWater, Boggy Serpens, Earth Vetala, and Cobalt Ulster) and DEV-1084 (now tracked as Mango Sandstorm and Storm-1084, respectively), presenting as DarkBit for obfuscation. *MuddyWater* (https://cyware.com/news/new-dev-1084-group-linked-with-muddywater-carries-out-destructive-attacks-8a8bda38). 

 Organization/industry/location: Not explicitly mentioned in the document. 

 Start date – End date: Attack observed in April 2023. 

 MITRE TTPs: ['Initial Access: Exploitation of Public-Facing Application (T1190)', 'Persistence: Create Account (T1136), Web Shell (T1505.003)', 'Privilege Escalation: OS Credential Dumping (T1003)', 'Defense Evasion: Disabling Security Tools (T1562)', 'Credential Access: Credentials from Password Stores (T1555)', 'Discovery: System Network Configuration Discovery (T1016)', 'Lateral Movement: Remote Services (T1021), Remote Service Session Hijacking (T1563)', 'Collection: Data from Local System (T1005)', 'Command and Control: Application Layer Protocol (T1071.001)'] 

 Impact: Destruction of cloud resources including server farms, virtual machines, storage accounts, and virtual networks. Email impersonation and potential data exfiltration. *Access via Exchange Web Services* (https://cyware.com/news/new-dev-1084-group-linked-with-muddywater-carries-out-destructive-attacks-8a8bda38). 

 Mitigation: ['Secure on-prem environment with strong credential hygiene and tamper protection.', 'Enable Conditional Access policies and continuous access evaluation in Azure AD.', 'Regularly apply security patches and updates to all systems.', 'Implement least privilege access and multifactor authentication (MFA) for all accounts.', 'Monitor and audit logs for suspicious activity and implement advanced threat detection solutions like Microsoft 365 Defender and Microsoft Sentinel.'] 

 Detailed Steps for mitigation: {'Secure On-Prem Environment': ['Enable tamper protection in Microsoft Defender for Endpoint.', 'Regularly review and update security policies and Group Policy Objects (GPOs).', 'Deploy and maintain security patches for all hardware and software.'], 'Secure Azure AD Environment': ['Enable Conditional Access policies to enforce device compliance and trusted IP address requirements.', 'Enable continuous access evaluation to revoke access in real-time based on user condition changes.', 'Regularly monitor Azure AD logs for unusual activities, such as unfamiliar sign-in properties.'], 'Implement Advanced Threat Detection': ['Use Microsoft 365 Defender and Microsoft Sentinel for real-time threat detection and response.', 'Configure alerts and detection rules for signs of compromise, such as unusual resource deletions or privilege escalation activities.']} 

 Detection Signature: {'Service': 'Azure AD', 'Severity': 'Critical', 'Incident': 'Unauthorized Access and Destruction of Cloud Resources', 'Signature name': 'Suspicious Azure resource deletions', 'Internal checks': ['Ensure Conditional Access policies are enabled.', 'Monitor activity logs for unusual sign-ins and actions by privileged accounts.', 'Review and restrict permissions of service accounts regularly.'], 'External scanning': ['Monitor for external IP addresses associated with known threat actors.', 'Detect unauthorized OAuth applications and administrative consent actions.']} 

 IoCs: ['9107be160f7b639d68fe3670de58ed254d81de6aec9a41ad58d91aa814a247ff (DEV-1084 ransom payload)', '80bd00c0f6d5e39b542ee6e9b67b1eef97b2dbc6ec6cae87bf5148f1cf18c260 (DEV-1084 batch script)', '8dd9773c24703e803903e7a5faa088c2df9a4b509549e768f29276ef86ef96ae (DEV-1084 batch script)', '486eb80171c086f4d184423ed7e79303ad7276834e5e5529b199f8ae5fc661f2 (DEV-1084 batch script)', 'IPs: 194.61.121[.]86, 141.95.22[.]153, 193.200[.]16.3, 192.52.166[.]191, 45.56.162[.]111, 104.194.222[.]219, 192.169.6[.]88, 192.52.167[.]209, 146.70.106[.]89', 'Domains: vatacloud[.]com, webstore4tech[.]uaenorth.cloudapp.azure[.]com'] 

 Additional Information: {'Tools': ['*Rport tool* (https://cyware.com/news/new-dev-1084-group-linked-with-muddywater-carries-out-destructive-attacks-8a8bda38)', '*AADInternals tool* (https://www.logpoint.com/en/blog/compromises-in-azure-ad-through-aad-connect/)'], 'Accounts': ['*highly privileged account* (https://www.logpoint.com/en/blog/compromises-in-azure-ad-through-aad-connect/)'], 'Roles': ['*Global Administrator role* (https://www.logpoint.com/en/blog/compromises-in-azure-ad-through-aad-connect/)']} 


# Related articles (describing the same threat) 
['https://www.microsoft.com/en-us/security/blog/2023/04/07/mercury-and-dev-1084-destructive-attack-on-hybrid-environment/', 'https://cyware.com/news/new-dev-1084-group-linked-with-muddywater-carries-out-destructive-attacks-8a8bda38', 'https://www.logpoint.com/en/blog/compromises-in-azure-ad-through-aad-connect/']
