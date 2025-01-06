Source: [https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)

## Related articles (describing the same threat) 
- https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas
- https://www.bridewell.com/insights/blogs/detail/analysing-widespread-microsoft365-credential-harvesting-campaign
- https://hackread.com/storm-1575-threat-actor-new-login-panels-phishing-infrastructure

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident 
 Rockstar 2FA Phishing-as-a-Service (PaaS) 

#### Root cause 
 The incident uses a Phishing-as-a-Service (PaaS) platform named Rockstar 2FA, facilitating adversary-in-the-middle (AiTM) phishing attacks. This platform intercepts user credentials and session cookies to bypass multi-factor authentication (MFA). The Rockstar 2FA kit mimics legitimate login pages, primarily targeting Microsoft 365 (O365) users, allowing attackers to harvest 2FA cookies and bypass protections. *The platform shares infrastructure with DadSec and Phoenix Panel* (https://hackread.com/storm-1575-threat-actor-new-login-panels-phishing-infrastructure/). *The threat actors utilize the Dadsec platform and Cyber Panel for hosting credential harvesting pages, leveraging Domain Generated Algorithm (DGA) domains and Cloudflare to mask malicious infrastructure* (https://www.bridewell.com/insights/blogs/detail/analysing-widespread-microsoft365-credential-harvesting-campaign). 

#### Threat actor/group/campaign 
 The threat actor behind this campaign is tracked by Microsoft as Storm-1575, an emerging or unidentified threat cluster responsible for high volumes of phishing campaigns. *Storm-1575 frequently rebrands its infrastructure, recently deploying new login panels* (https://hackread.com/storm-1575-threat-actor-new-login-panels-phishing-infrastructure/). 

#### Organization/industry/location 
 The primary targets of these campaigns are Microsoft user accounts, with a focus on Microsoft 365 (O365) login pages. The attacks have affected users across multiple sectors and regions, without targeting a specific group. 

#### Start date – End date 
 The phishing campaign increased significantly from May 2024, with a notable rise in August 2024, and continues as of November 26, 2024. 

#### MITRE TTPs 
 {'- T1566.001': 'Spear Phishing Attachment (High confidence)', '- T1566.002': 'Spear Phishing Link (High confidence)', '- T1071.001': 'Application Layer Protocol - Web Protocols (Medium confidence)', '- T1071.002': 'Application Layer Protocol - DNS (Medium confidence)', '- T1071.004': 'Application Layer Protocol - Email Protocols (Medium confidence)', '- T1098.001': 'Account Manipulation - Additional Email Delegate Permissions (Medium confidence)', '- T1189': 'Drive-by Compromise (Medium confidence)'} 

#### Impact 
 The campaign has led to large-scale phishing attacks with the potential for extensive credential theft and session hijacking. Specific financial losses or the number of affected individuals are not detailed, but the scale suggests significant impact. 

#### Mitigation Steps 
 {'1': 'Implement and enforce strong MFA policies that are resistant to AiTM attacks, such as hardware-based tokens or app-based authenticators.', '2': 'Regularly educate users about phishing threats and how to recognize suspicious emails and links.', '3': 'Utilize advanced email filtering solutions to detect and block phishing attempts.', '4': 'Monitor for abnormal or suspicious login activities and implement automated responses to potential breaches.', '5': 'Deploy web application firewalls (WAF) and other security measures to detect and block malicious activities.'} 

#### Detection Signature 
 {'Service': 'Web Application', 'Port': 'Various (depending on the phishing sites)', 'Severity': 'Critical', 'Incident': 'Phishing-as-a-Service (PaaS) - Rockstar 2FA', 'Signature name': '“Rockstar 2FA AiTM Phishing Campaign”', 'Internal checks': {'Setting1': 'Monitor for abnormal login attempts and session hijacking activities.', 'Setting2': 'Identify and block known phishing domains and URLs.', 'Setting3': 'Implement threat intelligence feeds to detect and block PaaS-related activities.'}, 'External scanning': {'Monitor': 'for the presence of known Rockstar 2FA-related phishing domains.', 'Check': 'for unusual web traffic patterns indicative of phishing activities.'}} 

#### IoCs:
- domain: curiosolucky.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: senderbulk.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: docsend.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: googlevoicesecrets.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: shorturl.at ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: https://urlscan.io/search/#stats.requests%3A%3C20%20AND%20(filename%3Aemail-decode.min.js%20OR%20filename%3Acrypto-js.min.js)%20AND%20page.title.keyword%3A%2F(%5Ba-z%5C-%20%5D*%20)%3F(Auto%7CAutomobile%7CAutomotive%7CCar%7CClassic%7CMotorcar%7CRace%7CRetro%7CRoadster%7CSpeed%7CSupe ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas/ ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas/ in VT. 

- url: https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas/?hs_amp=true ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas/?hs_amp=true in VT. 

- url: https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rss.xml ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rss.xml in VT. 

- url: https://www.trustwave.com/en-us/company/newsroom/news/trustwave-and-cybereason-merge-to-form-global-mdr-powerhouse-for-unparalleled-cybersecurity-value/ ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/en-us/company/newsroom/news/trustwave-and-cybereason-merge-to-form-global-mdr-powerhouse-for-unparalleled-cybersecurity-value/ in VT. 

- url: https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/template_assets/81597466170/1727892386937/marketplace/GiantFocal/Hatch/css/main.min.css ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/template_assets/81597466170/1727892386937/marketplace/GiantFocal/Hatch/css/main.min.css in VT. 

- url: https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/template_assets/82152213034/1732213578769/Trustwave_Theme_by_CC/child.min.css ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/template_assets/82152213034/1732213578769/Trustwave_Theme_by_CC/child.min.css in VT. 

- url: https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/template_assets/173343932468/1732648315918/Trustwave_Theme_by_CC/css/pages/blog-details.min.css ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/template_assets/173343932468/1732648315918/Trustwave_Theme_by_CC/css/pages/blog-details.min.css in VT. 

- url: https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/module_assets/128102279083/1729705714101/module_128102279083_Global-Header.min.css ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/module_assets/128102279083/1729705714101/module_128102279083_Global-Header.min.css in VT. 

- url: https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/module_assets/170112427927/1732642282107/module_170112427927_promotional-interrupter.min.css ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/module_assets/170112427927/1732642282107/module_170112427927_promotional-interrupter.min.css in VT. 

- url: https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/module_assets/174286900499/1732635335790/module_174286900499_blog-featured-resources.min.css ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/module_assets/174286900499/1732635335790/module_174286900499_blog-featured-resources.min.css in VT. 

- url: https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/module_assets/170221997576/1727346015970/module_170221997576_related-offerings.min.css ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/module_assets/170221997576/1727346015970/module_170221997576_related-offerings.min.css in VT. 

- url: https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/module_assets/128101228672/1730829013313/module_128101228672_Global-Footer.min.css ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url https://www.trustwave.com/hs-fs/hub/21158977/hub_generated/module_assets/128101228672/1730829013313/module_128101228672_Global-Footer.min.css in VT. 

- email: admin@example.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for email admin@example.com in VT. 

- ip: 93.123.73.210 ([link](https://www.bridewell.com/insights/blogs/detail/analysing-widespread-microsoft365-credential-harvesting-campaign)) 

- domain: 1e0yq0dnmzxs8ato15f0.15cl6.ru ([link](https://www.bridewell.com/insights/blogs/detail/analysing-widespread-microsoft365-credential-harvesting-campaign)) 

- domain: xmpmczxnljxtr4opmtd7.w6u56.ru ([link](https://www.bridewell.com/insights/blogs/detail/analysing-widespread-microsoft365-credential-harvesting-campaign)) 

- ip: 4 associated IP addresses ([link](https://hackread.com/storm-1575-threat-actor-new-login-panels-phishing-infrastructure)) 
Not found for ip 4 associated IP addresses in VT. 

- For more IoCs, please refer to the above links. 

#### paste IoC
curiosolucky.com
senderbulk.com
docsend.com
googlevoicesecrets.com
shorturl.at
https://urlscan.io/search/#stats.requests%3A%3C20%20AND%20(filename%3Aemail-decode.min.js%20OR%20filename%3Acrypto-js.min.js)%20AND%20page.title.keyword%3A%2F(%5Ba-z%5C-%20%5D*%20)%3F(Auto%7CAutomobile%7CAutomotive%7CCar%7CClassic%7CMotorcar%7CRace%7CRetro%7CRoadster%7CSpeed%7CSupe
93.123.73.210
1e0yq0dnmzxs8ato15f0.15cl6.ru
xmpmczxnljxtr4opmtd7.w6u56.ru

