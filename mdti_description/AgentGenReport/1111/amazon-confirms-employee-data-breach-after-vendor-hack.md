Source: [https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack](https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack
- https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/
- https://www.cyberdaily.au/security/11335-moveit-vulnerability-sees-amazon-mcdonalds-hsbc-and-more-employee-data-leaked
- https://socradar.io/moveit-data-leak-exposes-employee-data-of-amazon-hsbc-more-what-you-need-to-know/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: Amazon Employee Data Breach 

#### Root cause 
 The root cause was a security vulnerability in a third-party service provider used by Amazon. The vulnerability, CVE-2023-34362, was exploited during the MOVEit attacks *The vulnerability, CVE-2023-34362, was exploited* (https://www.cyberdaily.au/security/11335-moveit-vulnerability-sees-amazon-mcdonalds-hsbc-and-more-employee-data-leaked). *Exploited by various threat actors, including Clop and LockBit* (https://socradar.io/moveit-data-leak-exposes-employee-data-of-amazon-hsbc-more-what-you-need-to-know/). 

#### Threat actor/group/campaign 
 The attack was carried out by the threat actor known as Nam3L3ss, who used data stolen from Amazon's third-party vendor systems. The Clop ransomware gang was responsible for the initial wave of data theft attacks *The Clop ransomware gang was behind a wave of data theft attacks* (https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/). *Nam3L3ss posted the data on BreachForums* (https://socradar.io/moveit-data-leak-exposes-employee-data-of-amazon-hsbc-more-what-you-need-to-know/). 

#### Organization/industry/location 
 The primary victim was Amazon, specifically their employee data. Other companies affected include Lenovo, HP, TIAA, Schwab, HSBC, Delta, McDonald's, Metlife, Leidos, and more. *Additional victims include Cardinal Health, Fidelity, U.S. Bank, and Canada Post* (https://socradar.io/moveit-data-leak-exposes-employee-data-of-amazon-hsbc-more-what-you-need-to-know/). 

#### Start date – End date 
 The data breach occurred in May 2023. *The breaches were assessed to have occurred around May 31, 2023* (https://socradar.io/moveit-data-leak-exposes-employee-data-of-amazon-hsbc-more-what-you-need-to-know/). 

#### MITRE TTPs 
 ['T1190: Exploit Public-Facing Application (Exploitation of a zero-day vulnerability in the MOVEit Transfer platform)', 'T1078: Valid Accounts (Use of valid credentials to access data)', 'T1071: Application Layer Protocol (Use of the MOVEit Transfer platform to exfiltrate data)'] 

#### Impact 
 Over 2.8 million lines of Amazon employee data were leaked, affecting millions of employees. Other organizations also had employee data leaked, with varying numbers of employees impacted. *The breach exposed names, contact information, building locations, and email addresses* (https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/). *Amazon's dataset contained internal department codes and job titles, while HSBC’s dataset included user IDs and location details* (https://socradar.io/moveit-data-leak-exposes-employee-data-of-amazon-hsbc-more-what-you-need-to-know/). 

#### Mitigation Steps 
 ['1. **Patch Vulnerabilities**: Ensure that all third-party service providers and internal systems are patched with the latest security updates, particularly those related to the MOVEit Transfer platform.', '2. **Security Audits**: Conduct regular security audits of third-party service providers to identify and remediate potential vulnerabilities.', '3. **Access Control**: Limit the access of third-party service providers to only necessary data, and implement strict access control measures.', '4. **Monitoring and Detection**: Implement robust monitoring and detection mechanisms to identify any unauthorized access or data exfiltration attempts.', '5. **Incident Response Plan**: Develop and maintain an incident response plan to quickly respond to data breaches and mitigate their impact.'] 

#### Detection Signature 
 {'Service': 'MOVEit Transfer', 'Port': '443 (Typically used for HTTPS traffic)', 'Severity': 'Critical', 'Incident': 'Data Exfiltration via MOVEit Transfer', 'Signature name': '“MOVEit Transfer Exploitation”', 'Internal checks': ['Setting1: Ensure MOVEit Transfer software is updated to the latest version.', 'Setting2: Restrict access to the MOVEit Transfer platform to authorized users only.', 'Setting3: Enable logging and monitoring of all activities on the MOVEit Transfer platform.'], 'External scanning': ['Check for exposed MOVEit Transfer services on the internet.', 'Monitor for unusual data transfer activities.']} 

#### IoCs: ['No IoCs found.'] 

#### Noteworthy Details 
 Amazon spokesperson Adam Montgomery confirmed that Amazon and AWS systems remain secure, and the breached vendor has patched the security vulnerability. Nam3L3ss has over 250TB of archived databases from various sources, including exposed AWS and Azure buckets *Nam3L3ss has over 250TB of archived databases* (https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/). FBI, CISA, and NSA revealed most exploited vulnerabilities of 2023 *FBI, CISA, and NSA reveal most exploited vulnerabilities of 2023* (https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/). Hudson Rock confirmed the authenticity of leaked data by cross-referencing emails with LinkedIn profiles *Hudson Rock confirmed the authenticity of leaked data* (https://www.cyberdaily.au/security/11335-moveit-vulnerability-sees-amazon-mcdonalds-hsbc-and-more-employee-data-leaked). Nam3L3ss claimed to have '1,000 releases coming' and stated they are preparing a write-up for Hudson Rock *Nam3L3ss claimed to have '1,000 releases coming'* (https://www.cyberdaily.au/security/11335-moveit-vulnerability-sees-amazon-mcdonalds-hsbc-and-more-employee-data-leaked). *Nam3L3ss described themselves as a 'watcher, not hacker' targeting misconfigured cloud services* (https://socradar.io/moveit-data-leak-exposes-employee-data-of-amazon-hsbc-more-what-you-need-to-know/). 


