Source: [https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack](https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack
- https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/
- https://techcrunch.com/2024/11/11/amazon-confirms-employee-data-stolen-after-hacker-claims-moveit-breach/
- https://www.infostealers.com/article/massive-moveit-vulnerability-breach-hacker-leaks-employee-data-from-amazon-mcdonalds-hsbc-hp-and-potentially-1000-other-companies/
- https://www.forbes.com/sites/larsdaniel/2024/11/11/amazon-confirms-data-breach-exposed-2800000-lines-of-employee-data/
- https://www.theverge.com/2024/11/11/24293817/amazon-employee-emails-phone-numbers-moveit-data-breach

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Amazon Employee Data Breach 

#### Root cause 
 The root cause of the incident was a security vulnerability in the MOVEit Transfer secure file transfer platform, identified as CVE-2023-34362 (https://www.infostealers.com/article/massive-moveit-vulnerability-breach-hacker-leaks-employee-data-from-amazon-mcdonalds-hsbc-hp-and-potentially-1000-other-companies/), used by a third-party service provider, which was exploited by the Clop ransomware gang. *The breach stemmed from a property management vendor* (https://www.forbes.com/sites/larsdaniel/2024/11/11/amazon-confirms-data-breach-exposed-2800000-lines-of-employee-data/). 

#### Threat actor/group/campaign 
 Nam3L3ss (associated with the Clop ransomware gang) 

#### Organization/industry/location 
 Amazon (Retail/Technology, USA) 

#### Start date – End date 
 The data breach occurred in May 2023. *The leaked information dates back to last year* (https://www.theverge.com/2024/11/11/24293817/amazon-employee-emails-phone-numbers-moveit-data-breach). 

#### MITRE TTPs 
 ['T1190: Exploit Public-Facing Application', 'T1078: Valid Accounts', 'T1003: Credential Dumping', 'T1071: Application Layer Protocol'] 

#### Impact 
 Approximately 2.8 million records of Amazon employee data were leaked, including names, contact information, building locations, and email addresses. No sensitive information such as Social Security numbers or financial details were accessed (https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/). *The data leak was published on notorious hacking site BreachForums* (https://techcrunch.com/2024/11/11/amazon-confirms-employee-data-stolen-after-hacker-claims-moveit-breach/). *The breach affected 25 major organizations, exposing cost center codes and organizational structures* (https://www.infostealers.com/article/massive-moveit-vulnerability-breach-hacker-leaks-employee-data-from-amazon-mcdonalds-hsbc-hp-and-potentially-1000-other-companies/). *The exposed dataset includes desk phone numbers* (https://www.forbes.com/sites/larsdaniel/2024/11/11/amazon-confirms-data-breach-exposed-2800000-lines-of-employee-data/). *The incident is part of a larger campaign that has impacted over 2,000 organizations, exposing data of more than 62 million individuals* (https://www.forbes.com/sites/larsdaniel/2024/11/11/amazon-confirms-data-breach-exposed-2800000-lines-of-employee-data/). *Other affected entities include BBC, British Airways, Sony, and the US Department of Energy* (https://www.theverge.com/2024/11/11/24293817/amazon-employee-emails-phone-numbers-moveit-data-breach). 

#### Mitigation Steps 
 ['Ensure all third-party service providers are following robust security practices and regularly patching vulnerabilities.', 'Implement a comprehensive third-party risk management program to continuously monitor and assess the security posture of vendors.', 'Use encrypted communication channels for data transfers and ensure all sensitive data is encrypted at rest and in transit.', 'Implement multi-factor authentication (MFA) and strong password policies for all accounts.', 'Conduct regular security awareness training for employees and vendors on phishing and other social engineering attacks.', 'Monitor network traffic and logs for unusual activity and implement intrusion detection/prevention systems.'] 

#### Detection Signature 
 {'Service': 'MOVEit Transfer', 'Port': 443, 'Severity': 'Critical', 'Incident': 'Unauthorized access to MOVEit Transfer', 'Signature name': 'MOVEit Transfer Exploit Detection', 'Internal checks': ['Ensure MOVEit Transfer software is up-to-date with the latest security patches.', 'Verify that only authorized users have access to MOVEit Transfer.', 'Implement logging and monitoring to detect abnormal access patterns.'], 'External scanning': ['Scan for open port 443 and unauthorized access attempts on MOVEit Transfer.', 'Monitor for signs of exploitation attempts against MOVEit Transfer vulnerability.']} 

#### IoCs: No IoCs found. 

#### Additional Information 
 ['Amazon spokesperson Adam Montgomery confirmed the breach and that only work contact information was accessed (https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/).', 'The data leak was published on a hacking forum (https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/).', 'Nam3L3ss also leaked data from AWS and Azure buckets, affecting multiple other companies (https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/).', 'Other companies impacted include Lenovo, HP, TIAA, Schwab, HSBC, Delta, and MetLife, among others (https://www.bleepingcomputer.com/news/security/amazon-confirms-employee-data-breach-after-vendor-hack/).', '*Amazon noted that the unnamed third-party vendor doesn’t have access to sensitive data such as Social Security numbers or financial information and said the vendor had fixed the security vulnerability responsible for the data breach* (https://techcrunch.com/2024/11/11/amazon-confirms-employee-data-stolen-after-hacker-claims-moveit-breach/).', "*The threat actor claimed to have more than 2.8 million lines of data and stated 'What you have seen so far is less than .001% of the data I have'* (https://techcrunch.com/2024/11/11/amazon-confirms-employee-data-stolen-after-hacker-claims-moveit-breach/).", '*Hudson Rock researchers verified the authenticity of the leaked data by cross-referencing emails with LinkedIn profiles and Infostealer infections* (https://www.infostealers.com/article/massive-moveit-vulnerability-breach-hacker-leaks-employee-data-from-amazon-mcdonalds-hsbc-hp-and-potentially-1000-other-companies/).', '*The breach underscores the importance of vendor risk management despite the vulnerability being patched in 2023* (https://www.forbes.com/sites/larsdaniel/2024/11/11/amazon-confirms-data-breach-exposed-2800000-lines-of-employee-data/).', '*Amazon and AWS systems remain secure* (https://www.theverge.com/2024/11/11/24293817/amazon-employee-emails-phone-numbers-moveit-data-breach).'] 


