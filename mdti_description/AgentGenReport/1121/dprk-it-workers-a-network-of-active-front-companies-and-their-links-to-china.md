Source: [https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china](https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china)

## Related articles (describing the same threat) 
- https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
- https://thehackernews.com/2024/11/north-korean-front-companies.html
- https://www.justice.gov/opa/pr/justice-department-announces-court-authorized-action-disrupt-illicit-revenue-generation
- https://candid.technology/north-korean-shell-companies-found-impersonating-us-it-firms-to-fund-missiles
- https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: DPRK IT Workers Front Companies 

#### Root cause 
 The root cause of this incident is the deliberate impersonation and fraudulent operation of front companies by DPRK IT workers to evade international sanctions and generate revenue. These front companies appear as legitimate software and technology consulting businesses, often copying the online brands of actual firms. The deceptive tactics include using fake identities, forged credentials, and copied website content to secure contracts and launder earnings through cryptocurrencies or shadow banking systems. Additionally, facilitators play a crucial role in enabling these IT workers by providing essential services like laundering money and accessing international financial systems. The Wagemole campaign is part of this broader scheme. *The workers impersonate US-based software and technology consulting businesses to fund weapons of mass destruction and ballistic missile programs* (https://candid.technology/north-korean-shell-companies-found-impersonating-us-it-firms-to-fund-missiles/). 

#### Threat actor/group/campaign 
 The threat actors behind this incident are associated with the Democratic People's Republic of Korea (DPRK), specifically targeting global tech markets to fund state programs, including weapons development. The campaign is tracked as Wagemole by Palo Alto Networks Unit 42, and IT worker operations are identified as UNC5267 by Mandiant. 

#### Organization/industry/location 
 The attack targeted various global businesses within the software development, mobile applications, blockchain, and cryptocurrency sectors. Front companies are primarily based in China but linked to other regions like Russia, Southeast Asia, and Africa. Notable examples include China-based Yanbian Silverstar Network Technology Co. Ltd. and Russia-based Volasys Silver Star. The CL-STA-0237 activity cluster operates from Laos, and UNC5267 workers are mainly in China and Russia. *Newly discovered front companies include Independent Lab LLC, Shenyang Tonywang Technology LTD, and Tony WKJ LLC* (https://candid.technology/north-korean-shell-companies-found-impersonating-us-it-firms-to-fund-missiles/). 

#### Start date – End date 
 The documented activity includes websites active as early as November 2020, with significant law enforcement action taken by October 2023. *The US government seized control of four domains on October 10, 2024* (https://candid.technology/north-korean-shell-companies-found-impersonating-us-it-firms-to-fund-missiles/). 

#### MITRE TTPs 
 ['T1071.001 Application Layer Protocol: Web Protocols (Confidence: High)', 'T1190 Exploit Public-Facing Application (Confidence: High)', 'T1133 External Remote Services (Confidence: High)', 'T1078 Valid Accounts (Confidence: High)', 'T1071.003 Application Layer Protocol: Mail Protocols (Confidence: Medium)'] 

#### Impact 
 Multiple global businesses were deceived, potentially leading to legal violations, reputational damage, intellectual property theft, and malware implantation. The exact number of records or financial losses is not specified. The BeaverTail malware was used in recent phishing attacks. UNC5267 operations resulted in $6.8 million in revenue from compromised identities. 

#### Mitigation Steps 
 ['Implement stringent vetting processes for contractors and suppliers.', 'Verify the authenticity of business partners using multiple verification methods.', 'Monitor for suspicious activities and enforce strict cybersecurity policies.', 'Conduct regular audits and reviews of business relationships.', 'Educate employees about the risks of fraudulent entities and how to identify them.', 'Use multi-factor authentication and secure communication channels.'] 

#### Detection Signature 
 {'Service': 'Web Hosting Services (InterServer, NameCheap, Asia Web Services Ltd)', 'Port': 'Not specified, but typically HTTP (80) and HTTPS (443)', 'Severity': 'High', 'Incident': 'DPRK IT Worker Front Companies', 'Signature name': 'Suspicious Business Identity', 'Internal checks': ['Verify the business registration and address of contractors – In platform', 'Check for copied website content and logos – Inside VMs', 'Validate email addresses against known fraudulent patterns – Inside VMs'], 'External scanning': ['Monitor for domains registered recently or with suspicious hosting histories', 'Identify and flag hosting patterns common to DPRK IT worker front companies']} 

#### IoCs:
- domain: inditechlab.com ([link](https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/)) 

- ip: 174.138.181.198 ([link](https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/)) 

- domain: tonywangtech.com ([link](https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/)) 

- domain: wkjllc.com ([link](https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/)) 

- domain: hopanatech.com ([link](https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/)) 

- ip: 180.235.135.177 ([link](https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/)) 

- domain: huguotechltd.com ([link](https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/)) 

- ip: 103.15.29.44 ([link](https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/)) 

- email: tonywkj@hopana.com ([link](https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/)) 

- domain: 17 website domains ([link](https://www.justice.gov/opa/pr/justice-department-announces-court-authorized-action-disrupt-illicit-revenue-generation)) 

- usd: $1.5 million ([link](https://www.justice.gov/opa/pr/justice-department-announces-court-authorized-action-disrupt-illicit-revenue-generation)) 

- ip: 103.244.174.154 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 104.129.55.3 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 104.206.40.138 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 104.223.97.2 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 104.223.98.2 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 104.243.33.74 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 104.250.148.58 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 109.82.113.75 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 113.227.237.46 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 119.155.190.202 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 123.190.56.214 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 155.94.255.2 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 174.128.251.99 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 18.144.99.240 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 184.12.141.109 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 192.119.10.67 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 192.119.11.250 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 192.74.247.161 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 198.135.49.154 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 198.2.228.20 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 198.23.148.18 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 199.115.99.34 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 204.188.232.195 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 207.126.89.11 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 208.68.173.244 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 23.105.155.2 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 23.237.32.34 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 3.15.4.158 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 37.19.199.133 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 37.19.221.228 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 37.43.225.43 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 38.140.49.92 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 38.42.94.148 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 42.84.228.232 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 5.244.93.199 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 50.39.182.185 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 51.39.228.134 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 54.200.217.128 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 60.20.1.234 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 66.115.157.242 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 67.129.13.170 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 67.82.9.140 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 68.197.75.194 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 70.39.103.3 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 71.112.196.114 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 71.112.196.115 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 72.193.13.228 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 74.222.20.18 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 74.63.233.50 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- ip: 98.179.96.75 ([link](https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat)) 

- For more IoCs, please refer to the above links. 

#### Latest Actions 
 The United States seized 17 website domains used by DPRK IT workers to defraud businesses and fund weapons programs. These seizures were conducted under a U.S. court order from the Eastern District of Missouri. Approximately $1.5 million in illicit revenue was seized in 2022 and 2023. The FBI played a significant role in these actions. The cluster CL-STA-0237 operates from Laos and is part of the UNC5267 operations. *The coordinated action involved Homeland Security Investigations, the Defense Criminal Investigative Service, and the United States Postal Inspection Service* (https://candid.technology/north-korean-shell-companies-found-impersonating-us-it-firms-to-fund-missiles/). 

#### paste IoC
IoC Type	IoC Value	Source Link
domain	inditechlab.com	https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/
ip	174.138.181.198	https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/
domain	tonywangtech.com	https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/
domain	wkjllc.com	https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/
domain	hopanatech.com	https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/
ip	180.235.135.177	https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/
domain	huguotechltd.com	https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/
ip	103.15.29.44	https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/
email	tonywkj@hopana.com	https://www.sentinelone.com/labs/dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china/
domain	17 website domains	https://www.justice.gov/opa/pr/justice-department-announces-court-authorized-action-disrupt-illicit-revenue-generation
usd	$1.5 million	https://www.justice.gov/opa/pr/justice-department-announces-court-authorized-action-disrupt-illicit-revenue-generation
ip	103.244.174.154	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	104.129.55.3	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	104.206.40.138	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	104.223.97.2	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	104.223.98.2	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	104.243.33.74	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	104.250.148.58	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	109.82.113.75	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	113.227.237.46	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	119.155.190.202	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	123.190.56.214	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	155.94.255.2	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	174.128.251.99	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	18.144.99.240	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	184.12.141.109	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	192.119.10.67	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	192.119.11.250	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	192.74.247.161	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	198.135.49.154	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	198.2.228.20	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	198.23.148.18	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	199.115.99.34	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	204.188.232.195	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	207.126.89.11	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	208.68.173.244	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	23.105.155.2	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	23.237.32.34	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	3.15.4.158	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	37.19.199.133	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	37.19.221.228	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	37.43.225.43	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	38.140.49.92	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	38.42.94.148	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	42.84.228.232	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	5.244.93.199	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	50.39.182.185	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	51.39.228.134	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	54.200.217.128	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	60.20.1.234	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	66.115.157.242	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	67.129.13.170	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	67.82.9.140	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	68.197.75.194	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	70.39.103.3	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	71.112.196.114	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	71.112.196.115	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	72.193.13.228	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	74.222.20.18	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	74.63.233.50	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat
ip	98.179.96.75	https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat

