Source: [https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/microsoft-tech-support-scams-invade-azure-cloud-services
- https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Sad Announcement Email Tech Support Scam 

#### Root cause 
 The root cause of this incident is a phishing email campaign that exploits social engineering tactics to deceive recipients into clicking malicious links. The emails are designed to appear as if they come from people the recipient knows, containing deceptive subject lines and messages that lure the recipient into clicking on links that lead to tech support scam websites. *Researchers observed these scams increasingly moving towards the Microsoft Azure cloud platform for ease of deployment and inexpensive web hosting. The Azure App Services feature allows mass deployment of websites onto the azurewebsites.net domain* (https://www.bleepingcomputer.com/news/security/microsoft-tech-support-scams-invade-azure-cloud-services/). 

#### Threat actor/group/campaign 
 The specific threat actor or group behind this campaign is not identified, but they are cybercriminals specializing in tech support scams. *MalwareHunterTeam and JayTHL have discovered close to 600 websites hosted on the Azure App Services platform* (https://www.bleepingcomputer.com/news/security/microsoft-tech-support-scams-invade-azure-cloud-services/). 

#### Organization/industry/location 
 The campaign mainly targeted individuals in the US, Ireland, UK, India, and Italy. No specific organization or industry is targeted; the attack aims at the general public. 

#### Start date – End date 
 The first report of this campaign dates back to February 5, 2024. The ongoing nature of the campaign suggests it is still active. 

#### MITRE TTPs 
 ['T1566.002 Phishing: Spearphishing Link (High Confidence)', 'T1071.001 Application Layer Protocol: Web Protocols (Medium Confidence)', 'T1204.001 User Execution: Malicious Link (High Confidence)', 'T1589.002 Gather Victim Identity Information: Email Addresses (High Confidence)', 'T1078.003 Valid Accounts: Local Accounts (Medium Confidence)'] 

#### Impact 
 The impact of this campaign is primarily financial loss and potential identity theft for individuals who fall victim to the scam. The exact number of affected individuals is unknown. 

#### Mitigation Steps 
 ['Educate users about recognizing phishing attempts and the importance of verifying email senders.', 'Implement email filtering solutions to block known malicious domains and suspicious emails.', 'Use security software with anti-phishing capabilities to detect and block phishing attempts.', 'Encourage users to report suspicious emails to their IT department or security team.', 'Regularly update and patch software to protect against known vulnerabilities.'] 

#### Detection Signature 
 {'Service': 'Email', 'Port': 'N/A (Email-based)', 'Severity': 'High', 'Incident': 'Sad Announcement Email Scam', 'Signature name': '“Sad Announcement Email Phishing”', 'Internal checks': ["Setting1: Check for emails with subject lines containing 'Sad announcement' and variations.", 'Setting2: Analyze email content for phrases commonly used in the scam, such as references to old photos or shared images.', 'Setting3: Monitor for emails spoofed to appear from known contacts but originating from unusual domains.'], 'External scanning': ['Block and monitor domains known to be associated with this scam campaign:', 'hytsiysx.com', 'vdicedohf.com', 'rmldxkff.com', 'ramahteen.com', 'dexfyerd.com', 'unrgagceso.com', 'vohdsniuz.com', 'mbafwnds.com', 'hhesdeh.com', 'enexoo.com']} 

#### IoCs:
- domain: gjsqr.hytsiysx.com ([link](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)) 

- domain: tmdlod.vdicedohf.com ([link](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)) 

- domain: gtfhq.rmldxkff.com ([link](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)) 

- domain: pdbh.ramahteen.com ([link](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)) 

- domain: owwiu.dexfyerd.com ([link](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)) 

- domain: roix.unrgagceso.com ([link](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)) 

- domain: yrlbi.vohdsniuz.com ([link](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)) 

- domain: uqjk.mbafwnds.com ([link](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)) 

- domain: vjdbd.hhesdeh.com ([link](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)) 

- domain: mbjzo.enexoo.com ([link](https://www.malwarebytes.com/blog/news/2024/11/sad-announcement-email-leads-to-tech-support-scam)) 

- For more IoCs, please refer to the above links. 


