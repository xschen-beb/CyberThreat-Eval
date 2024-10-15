Source: [https://blog.talosintelligence.com/ra-group-ransomware/](https://blog.talosintelligence.com/ra-group-ransomware/)

# Newly Identified RA Group Compromises Companies in U.S. and South Korea With leaked Babuk Source Code

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: RA Group Ransomware Attack 

 Root cause: The root cause behind the incident is the use of the leaked Babuk ransomware source code by the RA Group. The RA Group has customized the Babuk ransomware to target specific victims, including providing unique ransom notes and executing specific encryption and deletion commands. *Custom encryption algorithms are employed* (https://www.hivepro.com/wp-content/uploads/2023/05/RA-Groups-Custom-Ransomware-Hits-US-South-Korea_TA2023230.pdf). The exact vulnerable entry points have not been detailed, but likely involve exploitation of vulnerable or misconfigured network services, software vulnerabilities, or phishing attacks. *RDP is a known attack vector* (https://www.hivepro.com/wp-content/uploads/2023/05/RA-Groups-Custom-Ransomware-Hits-US-South-Korea_TA2023230.pdf). 

 Threat Actor/group/campaign: RA Group 

 Organization/industry/location: *The targeted victims include three organizations in the U.S. and one in South Korea across several business verticals, including manufacturing, wealth management, insurance providers, and pharmaceuticals. The group is rapidly expanding its operations* (https://industrialcyber.co/vulnerabilities/ra-group-hackers-target-us-south-korean-organizations-using-leaked-babuk-ransomware-source-code/). 

 Start date – End date: The attack was first observed on April 22, 2023, with further victims reported on April 27 and April 28, 2023. 

 MITRE TTPs: ['T1059.001: Command and Scripting Interpreter: PowerShell', 'T1486: Data Encrypted for Impact', 'T1112: Modify Registry', 'T1070.004: Indicator Removal on Host: File Deletion', 'T1105: Ingress Tool Transfer', 'T1021.002: Remote Services: SMB/Windows Admin Shares'] 

 Impact: The exact number of records leaked has not been provided, but the attack includes exfiltration and potential sale of sensitive data from at least four organizations. *The RA Group's darknet site lists victim names, URLs, and itemized stolen data for sale* (https://therecord.media/ra-ransomware-group-using-leaked-code). The group employs double extortion tactics, increasing the chances of victims paying the ransom (https://industrialcyber.co/vulnerabilities/ra-group-hackers-target-us-south-korean-organizations-using-leaked-babuk-ransomware-source-code/). 

 Mitigation: ['Regularly update and patch systems and software to close known vulnerabilities.', 'Use multi-factor authentication (MFA) to reduce the risk of unauthorized access.', 'Implement robust email filtering to block phishing attempts.', 'Regularly backup data and ensure backups are stored securely and are not accessible from the main network.', 'Employ network segmentation to limit the spread of ransomware.', 'Train employees on recognizing phishing attacks and the importance of cybersecurity hygiene.', 'Implement endpoint detection and response (EDR) solutions to identify and mitigate malicious activities promptly.', 'Use advanced threat detection tools such as Cisco Secure Endpoint, Cisco Secure Firewall, and Cisco Secure Malware Analytics.', 'Deploy Cisco Secure Web Appliance to block risky sites and unknown threats (https://www.cisco.com/c/en/us/products/security/web-security-appliance/index.html).'] 

 Detection Signature: {'Service': 'SMB', 'Port': 445, 'Severity': 'Critical', 'Incident': 'Unauthorized access and encryption activity', 'Signature name': 'RA Group Ransomware Activity', 'Internal checks': ['File modifications/deletions on network shares – Inside VMs', 'Unauthorized execution of vssadmin.exe – Inside VMs', "Creation of ransom notes with filenames 'How To Restore Your Files.txt' – Inside VMs"], 'External scanning': ['Unusual network traffic to known malicious IP addresses or domains (e.g., gofile[.]io) – Network perimeter', 'Unauthorized SMB traffic – Network perimeter']} 

 IoCs: The document refers to IoCs available at a specific link, but they are not listed directly in the provided content. The link to the IoCs is [here](https://github.com/Cisco-Talos/IOCs/blob/main/2023/05/ra-group-ransomware.txt). 

 Integration and Deployment: Utilize Cisco Talos for sophisticated global threat intelligence (https://www.cisco.com/c/en/us/products/security/web-security-appliance/index.html) and consider deploying on Amazon Web Services (AWS) or Microsoft Azure (https://www.cisco.com/c/en/us/products/security/web-security-appliance/index.html) for scalable, cloud-based defense. 

 *Additional Information*: ["Encrypted files have the extension '.GAGUP' (https://therecord.media/ra-ransomware-group-using-leaked-code).", 'Victims have three days to respond before data leak (https://therecord.media/ra-ransomware-group-using-leaked-code).', 'The qTox messaging application is used to contact RA Group operators (https://therecord.media/ra-ransomware-group-using-leaked-code).', 'Critical infrastructure sectors like manufacturing and pharmaceuticals are targeted (https://industrialcyber.co/vulnerabilities/ra-group-hackers-target-us-south-korean-organizations-using-leaked-babuk-ransomware-source-code/).', '*Recent attacks on critical infrastructure highlight vulnerabilities and the need for public-private collaboration as addressed in the National Cybersecurity Strategy* (https://industrialcyber.co/vulnerabilities/ra-group-hackers-target-us-south-korean-organizations-using-leaked-babuk-ransomware-source-code/).', '*The group uses Tor for communication* (https://www.hivepro.com/wp-content/uploads/2023/05/RA-Groups-Custom-Ransomware-Hits-US-South-Korea_TA2023230.pdf).'] 


# Related articles (describing the same threat) 
['https://blog.talosintelligence.com/ra-group-ransomware/', 'https://www.cisco.com/c/en/us/products/security/web-security-appliance/index.html', 'https://therecord.media/ra-ransomware-group-using-leaked-code', 'https://industrialcyber.co/vulnerabilities/ra-group-hackers-target-us-south-korean-organizations-using-leaked-babuk-ransomware-source-code/', 'https://www.hivepro.com/wp-content/uploads/2023/05/RA-Groups-Custom-Ransomware-Hits-US-South-Korea_TA2023230.pdf']
