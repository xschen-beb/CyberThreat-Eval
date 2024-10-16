Source: [https://www.malwarebytes.com/blog/threat-intelligence/2023/11/malvertiser-copies-pc-news-site-to-deliver-infostealer](https://www.malwarebytes.com/blog/threat-intelligence/2023/11/malvertiser-copies-pc-news-site-to-deliver-infostealer)

# Malvertiser Copies PC News Site to Deliver Infostealer

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Malvertiser copies PC news site to deliver infostealer 

 Root cause: Malvertising was used to distribute a malicious installer via a website that copied content from a legitimate PC news site. Users were tricked into downloading a malicious utility instead of legitimate software. *The payload is a digitally signed MSIX installer which contains a malicious PowerShell script, a loader known as FakeBat (aka EugenLoader)* (https://www.threatdown.com/blog/malvertiser-copies-pc-news-site-to-deliver-infostealer/; *Endpoint Security/Malware* (https://thehackernews.com/2023/11/new-malvertising-campaign-uses-fake.html)). *Malwarebytes analysts identified this campaign, involving trojanized CPU-Z via Google Ads, leading to Redline Stealer infections* (https://www.bleepingcomputer.com/news/security/google-ads-push-malicious-cpu-z-app-from-fake-windows-news-site/). 

 Threat Actor/group/campaign: The specific threat actor is unknown, but the campaign involved the use of malvertising to distribute infostealer malware. *The advertiser shows as Scott Cooper and is likely a compromised or fake identity* (https://www.threatdown.com/blog/malvertiser-copies-pc-news-site-to-deliver-infostealer/; *RedLine Stealer* (https://thehackernews.com/2023/11/new-malvertising-campaign-uses-fake.html)). 

 Organization/industry/location: Users of a legitimate Windows news portal (WindowsReport.com) and various software utilities like CPU-Z, Notepad++, Citrix, and VNC Viewer were targeted. *ThreatDown, powered by Malwarebytes, already detected the final infostealer payload and added coverage for the command and control servers* (https://www.threatdown.com/blog/malvertiser-copies-pc-news-site-to-deliver-infostealer/; *Google Ads* (https://thehackernews.com/2023/11/new-malvertising-campaign-uses-fake.html)). 

 Start date – End date: Not explicitly mentioned, but the blog was posted on November 8, 2023. 

 MITRE TTPs: ['T1071.001: Application Layer Protocol: Web Traffic', 'T1105: Ingress Tool Transfer', 'T1190: Exploit Public-Facing Application', 'T1204.002: User Execution: Malicious File'] 

 Impact: The exact number of people impacted is not specified, but it involves multiple users who searched for and downloaded the malicious software. Financial losses are not detailed. *In an enterprise environment, it may be wise to verify a file’s checksum to ensure it has not been tampered with by comparing its SHA256 hash sum with what is posted on the vendor’s website* (https://www.threatdown.com/blog/malvertiser-copies-pc-news-site-to-deliver-infostealer/; *Nitrogen campaign* (https://thehackernews.com/2023/11/new-malvertising-campaign-uses-fake.html)). 

 Mitigation: ['Use reputable and verified download sources.', 'Verify file checksums and digital signatures before executing downloads.', 'Implement ad-blocking solutions and security browser extensions to filter out malicious advertisements.', 'Educate users about the risks of downloading software from unverified sources.', 'Regularly update antivirus and anti-malware programs to detect and block malicious payloads like FakeBat and Redline Stealer.'] 

 Detection Signature: {'Service': 'Web Server (Malicious websites and advertisements)', 'Port': '80, 443', 'Severity': 'Critical', 'Incident': 'Malvertising campaign delivering infostealer', 'Signature name': 'Malvertising domain detection', 'Internal checks': ['Ensure that users are educated about safe download practices.', 'Implement network security solutions to monitor and block access to known malicious domains.'], 'External scanning': ['Monitor for access attempts to known malicious domains and payload URLs.']} 

 IoCs: {'Ad domains': ['argenferia[.]com', 'realvnc[.]pro', 'corporatecomf[.]online', 'cilrix-corp[.]pro', 'thecoopmodel[.]com', 'winscp-apps[.]online', 'wireshark-app[.]online', 'cilrix-corporate[.]online', 'workspace-app[.]online'], 'Payload URLs': ['thecoopmodel[.]com/CPU-Z-x86.msix', 'kaotickontracting[.]info/account/hdr.jpg', 'ivcgroup[.]in/temp/Citrix-x64.msix', 'robo-claim[.]site/order/team.tar.gpg', 'argenferia[.]com/RealVNC-x64.msix'], 'Payloads': ['55d3ed51c3d8f56ab305a40936b446f761021abfc55e5cc8234c98a2c93e99e1', '9acbf1a5cd040c6dcecbe4e8e65044b380b7432f46c5fbf2ecdc97549487ca88', '419e06194c01ca930ed5d7484222e6827fd24520e72bfe6892cfde95573ffa16', 'cf9589665615375d1ad22d3b84e97bb686616157f2092e2047adb1a7b378cc95'], 'C2s': ['11234jkhfkujhs[.]site', '11234jkhfkujhs[.]top', '94.131.111[.]240', '81.177.136[.]179']} 


# Related articles (describing the same threat) 
['https://www.malwarebytes.com/blog/threat-intelligence/2023/11/malvertiser-copies-pc-news-site-to-deliver-infostealer', 'https://www.threatdown.com/blog/malvertiser-copies-pc-news-site-to-deliver-infostealer/', 'https://thehackernews.com/2023/11/new-malvertising-campaign-uses-fake.html', 'https://www.bleepingcomputer.com/news/security/google-ads-push-malicious-cpu-z-app-from-fake-windows-news-site/']
