Source: [https://yoroi.company/research/money-ransomware-the-latest-double-extortion-group/](https://yoroi.company/research/money-ransomware-the-latest-double-extortion-group/)

# Money Ransomware The Latest Double Extortion Group

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Money Ransomware: The Latest Double Extortion Group 

 Root cause: The incident's root cause is a targeted ransomware attack utilizing a human-operated intrusion approach. This involves manually accessing and exfiltrating data before encrypting it, indicating that systems were likely compromised through tactics such as phishing, credential theft, or exploiting unpatched vulnerabilities. 

 Threat Actor/group/campaign: Money Ransomware Group 

 Organization/industry/location: The Bangladesh National Airport was specifically mentioned as a victim, along with other high-profile targets like *Micro-Star International (MSI) and PharMerica* (https://www.avertium.com/resources/threat-reports/the-money-message-group-a-new-ransomware-threat). 

 Start date – End date: March 2023 – ongoing as of the blog post date (April 13, 2023) 

 MITRE TTPs: ['T1078: Valid Accounts (use of compromised credentials)', 'T1070: Indicator Removal on Host (removing shadow copies)', 'T1082: System Information Discovery (identifying directories and processes)', 'T1560: Archive Collected Data (exfiltrating data)', 'T1486: Data Encrypted for Impact (encrypting data)', 'T1047: Windows Management Instrumentation (WMIC for stopping services)', 'T1021: Remote Services (propagating through network shares using WNetAddConnection2W)'] 

 Impact: The blog does not specify the exact number of records leaked, but given the ransomware's double extortion method, sensitive data was both stolen and encrypted, impacting the Bangladesh National Airport significantly. *Money Message demanded a $4 million ransom from MSI* (https://www.avertium.com/resources/threat-reports/the-money-message-group-a-new-ransomware-threat). 

 Mitigation: ['Regularly update and patch software to close known vulnerabilities.', 'Employ robust endpoint security solutions, including EDR (Endpoint Detection and Response) systems.', 'Implement and enforce multi-factor authentication (MFA) to reduce the risk of credential theft.', 'Conduct regular security awareness training for employees to recognize phishing and social engineering tactics.', 'Deploy network segmentation to limit the spread of ransomware within the organization.', 'Regularly back up data and ensure backups are stored offline and tested for integrity.', 'Monitor network traffic for unusual activity that may indicate the presence of ransomware or other threats.'] 

 Detection Signature: {'Service': 'Windows Management Instrumentation (WMI)', 'Port': 'N/A (WMI operates over different ports, commonly 135)', 'Severity': 'Critical', 'Incident': 'Money Ransomware', 'Signature name': 'Money Ransomware Activity Detected', 'Internal checks': ['Monitor for the execution of vssadmin.exe and the deletion of shadow copies.', 'Monitor for unusual process terminations, especially related to security software.', 'Monitor for the creation of new services or the stopping of critical services.'], 'External scanning': ['Monitor for unusual login attempts, especially with compromised domain accounts.']} 

 IoCs: {'Hash': ['bbdac308d2b15a4724de7919bf8e9ffa713dea60ae3a482417c44c60012a654b']} 

 *Additional Information*: *Source: Yoroi Company; Slogan: Defence belongs to humans; Update Frequency: hourly* (https://yoroi.company/research/money-ransomware-the-latest-double-extortion-group/feed/) *The group targets victims globally, including an Asian airline and a $1 billion pharmacy network* (https://www.avertium.com/resources/threat-reports/the-money-message-group-a-new-ransomware-threat). 


# Related articles (describing the same threat) 
['https://yoroi.company/research/money-ransomware-the-latest-double-extortion-group/', 'https://yoroi.company/research/money-ransomware-the-latest-double-extortion-group/feed/', 'https://www.avertium.com/resources/threat-reports/the-money-message-group-a-new-ransomware-threat', 'https://unit42.paloaltonetworks.com/unit42-ransomware-threat-report-2023/']
