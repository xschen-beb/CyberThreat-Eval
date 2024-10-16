Source: [https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-royal](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-royal)

# Ransomware Spotlight Royal

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Royal Ransomware Attack 

 Root Cause: The root cause behind the incident appears to be the exploitation of vulnerabilities through phishing (callback phishing scams), and the use of various tools like QakBot, *BATLOADER infection* (https://unit42.paloaltonetworks.com/royal-ransomware/), and Cobalt Strike to disable security defenses and gain unauthorized access. The attackers used both new and existing techniques to bypass security measures, including the intermittent encryption tactic *and the unique partial encryption approach* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a). 

 Threat Actor/group/campaign: Royal Ransomware group, an offshoot of the Conti group, initially dubbed Zeon ransomware before rebranding *to BlackSuit ransomware* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a). The group operates as a private entity and has an *active Twitter account named 'LockerRoyal'* (https://unit42.paloaltonetworks.com/royal-ransomware/). 

 Organization/industry/location: The primary targets were organizations in the United States, with additional targets in Brazil, Mexico, Malaysia, and the United Kingdom. Industries affected included transportation, manufacturing, technology, education, healthcare, and government organizations. 

 Start date – End date: The Royal ransomware group was first reported in September 2022 and has been active since, with notable activity observed up until January 2023 *and rebranded as BlackSuit through June 2023* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a). 

 MITRE TTPs: {'Initial Access': 'T1566 - Phishing (callback phishing scams)', 'Execution': 'T1059 - Command and Scripting Interpreter, PsEXEC *and use of legitimate tools* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a)', 'Defense Evasion': 'T1562.001 - Impair Defenses: Disable or Modify Tools, T1112 - Modify Registry', 'Discovery': 'T1069 - Permission Groups Discovery: Domain groups, T1018 - Remote System Discovery', 'Exfiltration': 'T1567 - Exfiltration Over Web Service', 'Lateral Movement': 'T1570 - Lateral Tool Transfer', 'Command and Control': 'T1095 - Non-Application Layer Protocol', 'Impact': 'T1490 - Inhibit System Recovery, T1486 - Data Encrypted for Impact'} 

 Impact: The impact included the encryption of files, deletion of shadow copies, and exfiltration of sensitive information *with data exfiltration and extortion tactics* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a). Ransom demands ranged from $250,000 to over $2 million. Specific numbers of affected records or financial losses were not provided. 

 Mitigation: {'Audit and Inventory': {'- Take an inventory of assets and data.': '', '- Identify authorized and unauthorized devices and software.': '', '- Audit event and incident logs.': ''}, 'Configure and Monitor': {'- Manage hardware and software configurations.': '', '- Grant admin privileges and access only when necessary to an employee’s role.': '', '- Monitor network ports, protocols, and services.': '', '- Activate security configurations on network infrastructure devices.': '', '- Establish a software allowlist that only executes legitimate applications.': ''}, 'Patch and Update': {'- Conduct regular vulnerability assessments.': '', '- Perform patching or virtual patching for operating systems and applications.': '', '- Update software and applications to their latest versions.': ''}, 'Protect and Recover': {'- Implement data protection, backup, and recovery measures.': '', '- Enable multifactor authentication (MFA).': ''}, 'Secure and Defend': {'- Employ sandbox analysis to block malicious emails.': '', '- Deploy the latest versions of security solutions to all layers of the system.': '', '- Discover early signs of an attack using advanced detection technologies like AI and machine learning.': ''}, 'Train and Test': {'- Regularly train and assess employees’ security skills.': '', '- Conduct red-team exercises and penetration tests.': ''}} 

 Detection Signature: {'Service': 'Remote Desktop Software (e.g., RDP, TeamViewer)', 'Port': 'Various, depending on the tool used (e.g., RDP - 3389)', 'Severity': 'Critical', 'Incident': 'Unauthorized remote access', 'Signature name': 'Unauthorized Remote Desktop Access', 'Internal checks': {'- RDP should not be exposed externally.': '', '- Use of remote desktop software should be limited and monitored.': '', '- Ensure strong authentication mechanisms are in place.': ''}, 'External scanning': {'- Monitor for unusual remote desktop access attempts.': '', '- Identify and respond to unauthorized remote desktop software installations.': ''}} 

 IoCs: IoCs for this article can be found [here](https://documents.trendmicro.com/assets/txt/ransomware-spotlight-royal-ioc-cJShnGz.txt). 

 The detailed steps provided above should help in detecting, mitigating, and responding to potential threats posed by the Royal ransomware group.: The detailed steps provided above should help in detecting, mitigating, and responding to potential threats posed by the Royal ransomware group. 


# Related articles (describing the same threat) 
['https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-royal', 'https://www.trendmicro.com/en_us/research/22/l/conti-team-one-splinter-group-resurfaces-as-royal-ransomware-wit.html', 'https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a', 'https://unit42.paloaltonetworks.com/royal-ransomware/']
