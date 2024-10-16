Source: [https://blog.talosintelligence.com/yorotrooper-espionage-campaign-cis-turkey-europe/](https://blog.talosintelligence.com/yorotrooper-espionage-campaign-cis-turkey-europe/)

# Talos Uncovers Espionage Campaigns Targeting CIS Countries, Embassies and EU Health Care Agency

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: YoroTrooper Espionage Campaign 

 Root cause: The root cause behind the incident includes spear phishing attacks leveraging malicious shortcut files (LNKs) and decoy documents wrapped in malicious archives. The infection chain involves downloading and executing malicious HTA files leading to the deployment of various malware. 

 Threat Actor/group/campaign: YoroTrooper 

 Organization/industry/location: Government and energy organizations in CIS countries (Azerbaijan, Tajikistan, Kyrgyzstan), European Union health care agency, World Intellectual Property Organization (WIPO), and European embassies (including Azerbaijan and Turkmenistan). 

 Start date – End date: June 2022 – Present (Ongoing) 

 MITRE TTPs: ['T1071: Application Layer Protocol', 'T1203: Exploitation for Client Execution', 'T1078: Valid Accounts', 'T1027: Obfuscated Files or Information', 'T1059: Command and Scripting Interpreter', 'T1059.001: PowerShell', 'T1204: User Execution', 'T1056: Input Capture', 'T1105: Ingress Tool Transfer'] 

 Impact: The attack resulted in the compromise of credentials, browser histories, cookies, system information, and screenshots from multiple high-profile targets including government agencies and international organizations. 

 Mitigation: [{'Secure Email Gateway': ['Implement filters to block phishing emails and attachments.', 'Educate employees about the risks of phishing and how to identify suspicious emails.']}, {'Endpoint Protection': ['Use endpoint protection solutions that can detect and block malicious files and activities (e.g., Cisco Secure Endpoint).']}, {'Web Security': ['Deploy web security solutions to block access to malicious domains and websites (e.g., Cisco Secure Web Appliance).']}, {'Network Segmentation': ['Implement network segmentation to limit the spread of malware within the organization.']}, {'Regular Updates': ['Ensure all systems, including antivirus and antimalware software, are regularly updated with the latest security patches.']}, {'Multi-Factor Authentication (MFA)': ['Enforce multi-factor authentication to add an additional layer of security for user accounts.']}, {'Threat Intelligence': ['Leverage threat intelligence feeds to stay informed about emerging threats and Indicators of Compromise (IoCs).']}] 

 Detection Signature: {'Service': 'HTTP, HTTPS', 'Port': '80, 443', 'Severity': 'Critical', 'Incident': 'YoroTrooper Espionage Campaign', 'Signature name': 'Malicious HTA file execution', 'Internal checks': ['Monitor for unusual activity involving mshta.exe.', 'Check for the presence of LNK files that execute PowerShell commands.'], 'External scanning': ['Look for connections to known malicious domains and IP addresses associated with YoroTrooper.']} 

 IoCs: {'Malicious subdomains': ['mail[.]mfa[.]gov[.]kg[.]openingfile[.]net', 'akipress[.]news', 'maileecommission[.]inro[.]link', 'sts[.]mfa[.]gov[.]tr[.]mypolicy[.]top', 'industry[.]tj[.]mypolicy[.]top', 'mail[.]mfa[.]az-link[.]email', 'belaes[.]by[.]authentication[.]becloud[.]cc', 'belstat[.]gov[.]by[.]attachment-posts[.]cc', 'minsk[.]gov[.]by[.]attachment-posts[.]cc']} 

 Additional Information: *YoroTrooper likely consists of individuals from Kazakhstan based on their use of Kazakh currency and fluency in Kazakh and Russian. They rarely target Kazakh entities and have a defensive interest in the Kazakhstani state-owned email service*. YoroTrooper attempts to obfuscate the origin of their operations, employing VPN exit nodes in Azerbaijan (*link to new found document*). 


# Related articles (describing the same threat) 
['https://blog.talosintelligence.com/yorotrooper-espionage-campaign-cis-turkey-europe/', 'https://blog.talosintelligence.com/attributing-yorotrooper/']
