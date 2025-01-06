Source: [https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users](https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users)

## Related articles (describing the same threat) 
- https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users
- https://www.bleepingcomputer.com/news/security/fake-bitwarden-ads-on-facebook-push-info-stealing-chrome-extension/
- https://cyberinsider.com/facebook-ads-target-bitwarden-users-with-malicious-chrome-extension/
- https://hackread.com/facebook-malvertising-malware-via-fake-bitwarden/

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Malicious Facebook Ad Campaign Targeting Bitwarden Users 

#### Root cause 
 Exploitation of Meta's advertising platform to deliver malicious ads that redirect users to a phishing page mimicking the Chrome Web Store, prompting installation of a browser extension packaged as a ZIP file via Google Drive link *ZIP file via Google Drive link* (https://cyberinsider.com/facebook-ads-target-bitwarden-users-with-malicious-chrome-extension/). *The campaign uses deceptive Facebook ads designed to look like legitimate security updates for Bitwarden, creating a sense of urgency* (https://hackread.com/facebook-malvertising-malware-via-fake-bitwarden/). 

#### Threat actor/group/campaign 
 Unknown threat actor group exploiting Meta's platform and impersonating Bitwarden. 

#### Organization/industry/location 
 Bitwarden users, specifically targeting consumers aged 18 to 65 across Europe. 

#### Start date – End date 
 November 3, 2024 – Present (ongoing campaign) 

#### MITRE TTPs 
 ['T1071.001: Application Layer Protocol - Web Protocols', 'T1071.002: Application Layer Protocol - File Transfer Protocols', 'T1190: Exploit Public-Facing Application', 'T1189: Drive-by Compromise', 'T1566.001: Phishing - Spear Phishing Attachment', 'T1566.002: Phishing - Spear Phishing Link'] 

#### Impact 
 Thousands of users affected, potential for global expansion, leading to personal data theft and financial losses for individuals and businesses. *The extension's main script, background.js, activates immediately after installation and harvests sensitive data, focusing on Facebook accounts and business assets. It gathers IP address and geolocation data, and extracts personal and business information from Facebook using Graph API* (https://cyberinsider.com/facebook-ads-target-bitwarden-users-with-malicious-chrome-extension/) (https://hackread.com/facebook-malvertising-malware-via-fake-bitwarden/). 

#### Mitigation Steps 
 ['Verify Extension Updates: Always update extensions through official browser stores.', 'Scrutinize Ads and Links: Be cautious of sponsored ads on social media.', 'Check Extension Permissions: Review permissions before installing or updating extensions.', 'Enable Security Features: Use browser security settings and disable Developer Mode when not in use.', 'Report Suspicious Ads: Report misleading or malicious ads on social media platforms.', 'Use a Security Solution: Utilize reliable security solutions like Bitdefender Total Security to detect and block malicious links and unauthorized extensions.', '*Ignore Ads Promoting Extension Updates: Chrome extensions automatically update through official sources* (https://www.bleepingcomputer.com/news/security/fake-bitwarden-ads-on-facebook-push-info-stealing-chrome-extension/).'] 

#### Detection Signature 
 {'Service': 'Facebook Ad Platform', 'Port': 'N/A (Web-based service)', 'Severity': 'Critical', 'Incident': 'Malicious Facebook Ad Campaign', 'Signature name': 'Malicious Facebook Ad Campaign', 'Internal checks': ['Monitor for suspicious permissions in browser extensions.', 'Detect obfuscated functions like chrome.runtime.onInstalled.addListener.', 'Identify calls to graph.facebook.com APIs.', '*Monitor for excessive browser extension permissions, such as access to cookies and network requests, which can indicate malicious extensions.* (https://cyberinsider.com/facebook-ads-target-bitwarden-users-with-malicious-chrome-extension/)'], 'External scanning': ['Monitor for unauthorized sideloading of browser extensions.', 'Detect redirects to phishing pages mimicking the Chrome Web Store.']} 

#### IoCs:
- url: https://api.ipify.org ([link](https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users)) 

- url: https://freeipapi.com ([link](https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users)) 

- url: https://facebook.com ([link](https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users)) 

- url: https://graph.facebook.com ([link](https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users)) 

- url: https://www.messenger.com/t/102488646283695?ref=blogapp.bitdefender.com ([link](https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users)) 

- url: https://api.whatsapp.com/send?phone=19548585275&ref=blogapp.bitdefender.com ([link](https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users)) 

- url: https://www.bitdefender.com/solutions/scamio.html?ref=blogapp.bitdefender.com ([link](https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users)) 

- url: https://bitdefend.me/ScamioDiscord ([link](https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users)) 

- url: chromewebstoredownload.com ([link](https://www.bleepingcomputer.com/news/security/fake-bitwarden-ads-on-facebook-push-info-stealing-chrome-extension/)) 

- url: Google Script URL ([link](https://cyberinsider.com/facebook-ads-target-bitwarden-users-with-malicious-chrome-extension/)) 

- For more IoCs, please refer to the above links. 


