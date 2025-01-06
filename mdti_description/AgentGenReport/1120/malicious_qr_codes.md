Source: [https://blog.talosintelligence.com/malicious_qr_codes](https://blog.talosintelligence.com/malicious_qr_codes)

## Related articles (describing the same threat) 
- https://abnormalsecurity.com/blog/qr-code-phishing-attacks
- https://blog.talosintelligence.com/malicious_qr_codes
- https://www.infosecurity-magazine.com/news/60-emails-qr-codes-spam-malicious

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Malicious QR Codes Bypassing Anti-Spam Filters 

#### Root cause 
 *The primary root cause is the ability of QR codes to bypass anti-spam filters effectively. Most filters are not designed to detect and decode QR codes embedded within images, making it easier for malicious QR codes to reach users' inboxes. Additionally, the use of QR code art and QR codes constructed from Unicode characters further complicates detection. Cisco Talos states that 60% of QR code emails are spam* (https://blog.talosintelligence.com/malicious_qr_codes/) *and a smaller subset overtly malicious* (https://www.infosecurity-magazine.com/news/60-emails-qr-codes-spam-malicious/). *17% of attacks use QR codes* (https://abnormalsecurity.com/blog/qr-code-phishing-attacks).*The challenges are exacerbated by embedding QR codes in PDFs which bypass traditional detection methods and traffic generated on personal devices that evade corporate networks* (https://www.infosecurity-magazine.com/news/60-emails-qr-codes-spam-malicious/). 

#### Threat actor/group/campaign 
 *The threat actors involved are typically spammers and phishers who exploit the loophole in anti-spam filters to deliver malicious QR codes to users. These actors aim to use the QR codes for phishing, credential theft, and other malicious activities, including MFA phishing via QR codes* (https://blog.talosintelligence.com/malicious_qr_codes/). *89% of QR code attacks are credential phishing* (https://abnormalsecurity.com/blog/qr-code-phishing-attacks). 

#### Organization/industry/location 
 The incident targets a broad range of users across different organizations and industries globally, given the widespread use of QR codes in emails and other communication media. 

#### Start date � End date 
 The blog does not specify exact dates but discusses ongoing challenges and incidents related to malicious QR codes. The latest findings were written by Alessandro Mascellino, a Freelance Journalist, on November 20, 2024* (https://www.infosecurity-magazine.com/news/60-emails-qr-codes-spam-malicious/). 

#### MITRE TTPs 
 ['T1071.001 - Application Layer Protocol: Web Protocols (High confidence): Attackers use embedded QR codes to direct victims to phishing websites or malicious URLs.', 'T1204.002 - User Execution: Malicious File (Medium confidence): Users scan malicious QR codes from emails or documents, leading to compromise.', 'T1566.001 - Phishing: Spear Phishing Attachment (Medium confidence): QR codes in phishing emails aiming to harvest credentials or deliver malware.'] 

#### Impact 
 The impact includes a significant number of spam emails reaching users' inboxes, potential exposure to phishing attempts, and credential theft. The exact number of devices or people impacted is not specified. 

#### Mitigation Steps 
 ['Educate users on the risks associated with scanning unknown QR codes and encourage them to treat QR codes with the same caution as suspicious URLs.', 'Implement QR code scanning solutions that can decode and analyze the content before accessing it.', 'Use email security solutions capable of detecting and analyzing QR codes within emails.', 'Regularly update and configure anti-spam filters to recognize and handle QR codes.', 'Encourage users to use QR code decoders to inspect QR codes before scanning them with their devices.', '*Defang QR codes by obscuring data modules or removing position detection patterns* (https://blog.talosintelligence.com/malicious_qr_codes/).', "*Abnormal's AI-native detection enhances QR code threat detection* (https://abnormalsecurity.com/blog/qr-code-phishing-attacks)."] 

#### Detection Signature 
 {'Service': 'Email Security', 'Port': 'N/A (applies to email content)', 'Severity': 'High', 'Incident': 'Malicious QR Codes', 'Signature name': 'Malicious QR Code Detection', 'Internal checks': ['Email security solutions should scan and decode QR codes within email content.', 'Regular updates to anti-spam filters to detect new QR code patterns.', 'Educate users on identifying and reporting suspicious QR codes.', "*Abnormal's behavioral AI detection enhances threat detection* (https://abnormalsecurity.com/blog/qr-code-phishing-attacks)."], 'External scanning': ['Monitoring incoming emails for QR codes.', 'Analyzing decoded QR code content for malicious links or data.']} 

#### IoCs:
- No IoCs found.

- For more IoCs, please refer to the above links. 


