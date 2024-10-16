Source: [https://www.malwarebytes.com/blog/threat-intelligence/2024/01/atomic-stealer-rings-in-the-new-year-with-updated-version](https://www.malwarebytes.com/blog/threat-intelligence/2024/01/atomic-stealer-rings-in-the-new-year-with-updated-version)

# Atomic Stealer Rings in the New Year with Updated Version

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Atomic Stealer rings in the new year with updated version 

 Root cause: The incident was primarily facilitated by the use of malvertising and compromised websites to distribute the Atomic Stealer malware. The updated version introduced payload encryption to bypass detection rules, obfuscate strings, and utilized XOR encoding to hide known strings *XOR encoding* (https://www.kandji.io/blog/amos-macos-stealer-analysis). *It also drops and uses a Python script to stay covert, combining Python with Apple Script to gather sensitive data* (https://www.bitdefender.com/blog/labs/when-stealers-converge-new-variant-of-atomic-stealer-in-the-wild/?srsltid=AfmBOoryTMQkycvGqtRDxcWc3dD0xmpB9bkON3ixOOFyKYgpsEL-cd2H). 

 Threat Actor/group/campaign: The campaign was carried out by the developers of Atomic Stealer (AMOS), a known stealer in the criminal underground. 

 Organization/industry/location: The primary targets were Mac users, and the campaign involved luring victims through fake advertisements and compromised sites. *A key ad account was traced to Belarus* (https://www.malwarebytes.com/blog/threat-intelligence/2023/09/atomic-macos-stealer-delivered-via-malvertising). 

 Start date – End date: The update and increased activity of Atomic Stealer were observed from mid to late December 2023, with a noted malvertising campaign in early January 2024. *Updated March 1, 2024* (https://www.kandji.io/blog/amos-macos-stealer-analysis). 

 MITRE TTPs: ['T1203: Exploitation for Client Execution', 'T1071.001: Application Layer Protocol - Web Protocols', 'T1027: Obfuscated Files or Information', 'T1081: Credentials in Files', 'T1074.001: Data Staged - Local Data Staging'] 

 Impact: The exact number of individuals affected is not specified, but the campaign involves significant exposure through Google search ads and compromised websites. *Google’s Ads Transparency Center revealed details about the ad sources* (https://www.malwarebytes.com/blog/threat-intelligence/2023/09/atomic-macos-stealer-delivered-via-malvertising). 

 Mitigation: ['Avoid downloading software from untrusted sources. Always download applications from the official websites.', 'Use a combination of web protection and antivirus software to prevent and detect malware.', 'Regularly update antivirus definitions and conduct routine scans.', 'Educate users about the risks of entering passwords on suspicious prompts and the dangers of downloading cracked software.', 'Implement ad-blocking solutions to mitigate exposure to malvertising.'] 

 Detection Signature: {'Service': 'Web Browser (Malvertising)', 'Port': 'N/A', 'Severity': 'Critical', 'Incident': 'Atomic Stealer distribution', 'Signature name': 'Atomic Stealer distribution via malvertising', 'Internal checks': ['Verify the source of software downloads and ensure they are from trusted repositories.', 'Monitor for unusual download and execution patterns, especially involving DMG files.'], 'External scanning': ['Block and monitor domains known for distributing malware (e.g., slack[.]trialap[.]com).']} 

 IoCs: {'Malvertising chain': ['ivchlo[.]gotrackier[.]com', 'red[.]seecho[.]net'], 'Decoy site': ['slack[.]trialap[.]com', '*trabingviews[.]com* (https://www.malwarebytes.com/blog/threat-intelligence/2023/09/atomic-macos-stealer-delivered-via-malvertising)'], 'FakeBat payload URL': ['slack[.]trialap[.]com/app/Slack-x86.msix'], 'FakeBat hash': ['49f12d913ad19d4608c1596cf24e7b6fff14975418f09e2c1ad37f231943fda3'], 'FakeBat C2': ['ads-strong[.]online'], 'Atomic Stealer payload URL': ['slack[.]trialap[.]com/app/Slack-Apps.dmg', '*app-downloads[.]org/tview.php* (https://www.malwarebytes.com/blog/threat-intelligence/2023/09/atomic-macos-stealer-delivered-via-malvertising)'], 'Atomic Stealer hash': ['18bc97e3f68864845c719754d2d667bb03f754f6e87428e33f9c763a8e6a704a'], 'C2': ['5.42.65[.]108', '*5.42.65.114* (https://www.bitdefender.com/blog/labs/when-stealers-converge-new-variant-of-atomic-stealer-in-the-wild/?srsltid=AfmBOoryTMQkycvGqtRDxcWc3dD0xmpB9bkON3ixOOFyKYgpsEL-cd2H)']} 

 Additional Details: {'AMOS Distribution': 'Telegram; $3,000 a month *Telegram*; *$3,000 a month* (https://www.kandji.io/blog/amos-macos-stealer-analysis)', '*Mach-O binaries are used as droppers, and the Python script collects browser data, crypto-wallet files, and local user password* (https://www.bitdefender.com/blog/labs/when-stealers-converge-new-variant-of-atomic-stealer-in-the-wild/?srsltid=AfmBOoryTMQkycvGqtRDxcWc3dD0xmpB9bkON3ixOOFyKYgpsEL-cd2H)': 'AMOS Stealer was previously linked to a Russian threat actor, confirmed by the C2 server address.'} 


# Related articles (describing the same threat) 
['https://www.malwarebytes.com/blog/threat-intelligence/2024/01/atomic-stealer-rings-in-the-new-year-with-updated-version', 'https://www.malwarebytes.com/blog/threat-intelligence/2023/09/atomic-macos-stealer-delivered-via-malvertising', 'https://www.kandji.io/blog/amos-macos-stealer-analysis', 'https://www.bitdefender.com/blog/labs/when-stealers-converge-new-variant-of-atomic-stealer-in-the-wild/?srsltid=AfmBOoryTMQkycvGqtRDxcWc3dD0xmpB9bkON3ixOOFyKYgpsEL-cd2H']
