Source: [https://blog.eclecticiq.com/inside-intelligence-center-financially-motivated-chinese-threat-actor-silkspecter-targeting-black-friday-shoppers#a3#new_tab](https://blog.eclecticiq.com/inside-intelligence-center-financially-motivated-chinese-threat-actor-silkspecter-targeting-black-friday-shoppers#a3#new_tab)

## Related articles (describing the same threat) 
- https://blog.eclecticiq.com/inside-intelligence-center-financially-motivated-chinese-threat-actor-silkspecter-targeting-black-friday-shoppers#a3#new_tab
- https://blog.eclecticiq.com/inside-intelligence-center-financially-motivated-chinese-threat-actor-silkspecter-targeting-black-friday-shoppers
- https://malpedia.caad.fkie.fraunhofer.de/actor/silkspecter
- https://thehackernews.com/2024/11/fake-discount-sites-exploit-black.html
- https://www.forbes.com/sites/zakdoffman/2024/11/18/new-chrome-safari-firefox-edge-warning-do-not-shop-on-these-websites/
- https://www.enterprisesecuritytech.com/post/chinese-cybercrime-group-silkspecter-targets-holiday-shoppers-with-sophisticated-fraud-campaign
- https://www.bleepingcomputer.com/news/security/fraud-network-uses-4-700-fake-shopping-sites-to-steal-credit-cards/
- https://gizmodo.com/beware-of-fake-sites-mimicking-black-friday-deals-researchers-say-2000525936

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Financially Motivated Chinese Threat Actor SilkSpecter Targeting Black Friday Shoppers 

#### Root cause 
 The root cause of the incident is the exploitation of legitimate payment processors like Stripe and the use of a Chinese Software as a Service (SaaS) platform named oemapps to create convincing fake e-commerce sites. *SilkSpecter also utilized Google Translate to dynamically adjust the website's language and enhance credibility* (https://blog.eclecticiq.com/inside-intelligence-center-financially-motivated-chinese-threat-actor-silkspecter-targeting-black-friday-shoppers). *The campaign deployed SEO poisoning to redirect users to fake e-commerce pages* (https://thehackernews.com/2024/11/fake-discount-sites-exploit-black.html). *A Content Delivery Network (CDN) hosted in China was used for hosting fraudulent imagery and components* (https://www.forbes.com/sites/zakdoffman/2024/11/18/new-chrome-safari-firefox-edge-warning-do-not-shop-on-these-websites/). *SilkSpecter operates nearly 4,700 fraudulent domains* (https://www.enterprisesecuritytech.com/post/chinese-cybercrime-group-silkspecter-targets-holiday-shoppers-with-sophisticated-fraud-campaign). *SilkSpecter impersonated well-known brands like Gardena and used top-level domains like .shop, .store, .vip, and .top to appear legitimate* (https://www.bleepingcomputer.com/news/security/fraud-network-uses-4-700-fake-shopping-sites-to-steal-credit-cards/). *Some of the websites run by SilkSpecter include ikea-euonline.com* (https://gizmodo.com/beware-of-fake-sites-mimicking-black-friday-deals-researchers-say-2000525936). 

#### Threat actor/group/campaign 
 SilkSpecter, a financially motivated Chinese threat actor. 

#### Organization/industry/location 
 E-commerce shoppers in Europe and the USA. 

#### Start date – End date 
 Early October 2024 – November 2024. 

#### MITRE TTPs 
 ['T1190: Exploit Public-Facing Application', 'T1071.001: Application Layer Protocol: Web Protocols', 'T1566.001: Phishing: Spearphishing Attachment', 'T1003: Credential Dumping', 'T1078: Valid Accounts', 'T1110: Brute Force', 'T1071.003: Application Layer Protocol: Mail Protocols'] 

#### Impact 
 The phishing campaign targeted victims' Cardholder Data (CHD), Sensitive Authentication Data (SAD), and Personally Identifiable Information (PII), leveraging the Black Friday shopping season to deceive victims into providing their sensitive information. *The campaign used OpenReplay, TikTok Pixel, and Meta Pixel to monitor attack effectiveness* (https://blog.eclecticiq.com/inside-intelligence-center-financially-motivated-chinese-threat-actor-silkspecter-targeting-black-friday-shoppers). *Victims' phone numbers were also collected to enable follow-on smishing and vishing attacks* (https://thehackernews.com/2024/11/fake-discount-sites-exploit-black.html). *There are upwards of 4,000 malicious domains associated with this campaign* (https://www.forbes.com/sites/zakdoffman/2024/11/18/new-chrome-safari-firefox-edge-warning-do-not-shop-on-these-websites/). *Chinese IP addresses were used in the campaign* (https://www.enterprisesecuritytech.com/post/chinese-cybercrime-group-silkspecter-targets-holiday-shoppers-with-sophisticated-fraud-campaign). *Phone numbers were stolen for voice or SMS phishing attacks* (https://www.bleepingcomputer.com/news/security/fraud-network-uses-4-700-fake-shopping-sites-to-steal-credit-cards/). *EclecticIQ warned that some of the information collected could be used to target victims with further attacks to compromise multi-factor authentication* (https://gizmodo.com/beware-of-fake-sites-mimicking-black-friday-deals-researchers-say-2000525936). 

#### Mitigation Steps 
 ["Monitor for URLs with themes like 'discount,' 'Black Friday,' or similar sales events.", 'Utilize shared IoCs to identify and track SilkSpecter’s phishing domains with specific indicators.', 'Set up monitoring rules for traffic communicating with specific ASNs linked to Chinese entities.', 'Use virtual cards for online purchases and enable spending limits and restrictions.', 'Educate users on recognizing phishing attempts and the importance of verifying URLs before entering sensitive information.', '*Avoid links in ads and social media* (https://www.enterprisesecuritytech.com/post/chinese-cybercrime-group-silkspecter-targets-holiday-shoppers-with-sophisticated-fraud-campaign).', '*Follow recommendations from CISA on securing shopping activities* (https://gizmodo.com/beware-of-fake-sites-mimicking-black-friday-deals-researchers-say-2000525936)'] 

#### Detection Signature 
 {'Service': 'Web Application', 'Port': '443 (HTTPS)', 'Severity': 'Critical', 'Incident': 'SilkSpecter Phishing Campaign', 'Signature name': 'Black Friday-themed Phishing Detection', 'Internal checks': ["URL Patterns: Monitor for URLs with 'discount,' 'Black Friday,' or similar sales events.", "Endpoint Patterns: Look for '/homeapi/collect' and domains incorporating 'trusttollsvg.'"], 'External scanning': 'Monitor network traffic for suspicious ASN numbers linked to Chinese entities.'} 

#### IoCs:
- hash_sha256: 587b05cd8d59f9820d2cf168b07d46b1519d12ee7a2f7062a2490da0a99ccb50 ([link](https://urlscan.io/)) 

- hash_sha256: 9a049fe87fe472bd6e2a9f361b78a64576be9f827f9668af69bec03f5cbef0da ([link](same as above)) 

- domain: northfaceblackfriday.shop ([link](https://www.eclecticiq.com/)) 

- domain: lidl-blackfriday-eu.shop ([link](same as above)) 

- domain: bbw-blackfriday.shop ([link](same as above)) 

- domain: llbeanblackfridays.shop ([link](same as above)) 

- domain: dopeblackfriday.shop ([link](same as above)) 

- domain: wayfareblackfriday.com ([link](same as above)) 

- domain: makitablackfriday.shop ([link](same as above)) 

- domain: blackfriday-shoe.top ([link](same as above)) 

- ip: 45.76.23.109 ([link](https://malpedia.caad.fkie.fraunhofer.de/actor/silkspecter)) 

- ip: 103.27.8.152 ([link](same as above)) 

- domain: ikeablackfriday.store ([link](https://thehackernews.com/2024/11/fake-discount-sites-exploit-black.html)) 

- domain: ikeablackfriday.vip ([link](same as above)) 

- domain: ikea-euonline.com ([link](https://gizmodo.com/beware-of-fake-sites-mimicking-black-friday-deals-researchers-say-2000525936)) 

- For more IoCs, please refer to the above links. 

#### Expert Insights and Recommendations 
 {'Expert': '*EclecticIQ threat researcher Arda Buyukkaya* (https://www.bleepingcomputer.com/news/security/fraud-network-uses-4-700-fake-shopping-sites-to-steal-credit-cards/), Max Gannon, Cyber Intelligence Team Manager at Cofense (https://www.enterprisesecuritytech.com/post/chinese-cybercrime-group-silkspecter-targets-holiday-shoppers-with-sophisticated-fraud-campaign)', 'Recommendations': ['Verify Website Authenticity', 'Avoid Links in Ads and Social Media', 'Monitor Financial Accounts', 'Activate Multi-Factor Authentication', '*Check for deals offering up to 80 percent off, as these are often used as phishing lures* (https://gizmodo.com/beware-of-fake-sites-mimicking-black-friday-deals-researchers-say-2000525936)']} 


