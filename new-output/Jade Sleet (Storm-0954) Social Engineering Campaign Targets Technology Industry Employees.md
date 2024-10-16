Source: [https://github.blog/2023-07-18-security-alert-social-engineering-campaign-targets-technology-industry-employees/](https://github.blog/2023-07-18-security-alert-social-engineering-campaign-targets-technology-industry-employees/)

# Jade Sleet (Storm-0954) Social Engineering Campaign Targets Technology Industry Employees

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Social Engineering Campaign Targets Technology Industry Employees 

 Root cause: The root cause of this incident is a social engineering campaign exploiting the trust of technology industry employees. The threat actor uses fake personas on platforms like GitHub, LinkedIn, Slack, and Telegram to invite targets to clone and execute repositories containing malicious npm package dependencies. These packages act as first-stage malware to download and execute second-stage malware. *The attack chain starts with a `preinstall` hook using `sync-request` library* (https://blog.phylum.io/sophisticated-ongoing-attack-discovered-on-npm/). *The campaign involves TraderTraitor, linked to Lazarus Group, using AppleJeus malware* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-108a). *Phylum originally reported this campaign back in June* (https://news.ycombinator.com/item?id=36865060). *North Korea based threat actor using professional profiles and repository invitations* (https://cybersecuritynews.com/lazarus-hacker-group-targeting-developers/). 

 Threat Actor/group/campaign: Jade Sleet (Microsoft Threat Intelligence) / TraderTraitor (U.S. Cybersecurity and Infrastructure Security Agency - CISA) 

 Organization/industry/location: Technology firms, particularly those associated with blockchain, cryptocurrency exchanges, decentralized finance (DeFi) protocols, online gambling, and cybersecurity sectors. 

 Start date – End date: Not specified in the blog. *The attack was first discovered on June 11* (https://blog.phylum.io/sophisticated-ongoing-attack-discovered-on-npm/). 

 MITRE TTPs: ['T1071.001 - Application Layer Protocol: Web Protocols', 'T1193 - Spearphishing Attachment', 'T1203 - Exploitation for Client Execution', 'T1078 - Valid Accounts'] 

 Impact: The specific number of affected individuals or financial losses is not mentioned, but the campaign targets personal accounts of employees in the technology industry. 

 Mitigation: ['Be cautious of unsolicited invitations to clone or download repositories, especially from unknown sources.', 'Review your security logs for suspicious `action:repo.add_member` events.', 'Scrutinize dependencies and installation scripts for new packages or those making network connections.', "Contact your employer's cybersecurity department if targeted.", 'Reset or wipe potentially affected devices and change account passwords and sensitive credentials.'] 

 Detailed Steps for mitigation: ['Educate employees on recognizing social engineering tactics.', 'Implement multi-factor authentication (MFA) for all accounts.', 'Regularly monitor and review access logs for unusual activities.', 'Use endpoint protection solutions that can detect and block malicious software.', 'Regularly update and patch all software and systems to protect against known vulnerabilities.'] 

 Detection Signature: {'Service': 'npm', 'Port': 'Not applicable (npm packages)', 'Severity': 'Critical', 'Incident': 'social engineering campaign', 'Signature name': 'Suspicious npm package installation', 'Internal checks': ['Monitor for installation of packages listed as malicious.', 'Monitor for unusual network connections during npm package installations.'], 'External scanning': ['Check for domains associated with malicious activities listed in the indicators.']} 

 IoCs: {'Domains': ['npmjscloud[.]com', 'npmrepos[.]com', 'cryptopriceoffer[.]com', 'tradingprice[.]net', 'npmjsregister[.]com', 'bi2price[.]com', 'npmaudit[.]com', 'coingeckoprice[.]com'], 'Malicious npm packages': ['assets-graph', 'assets-table', 'audit-ejs', 'audit-vue', 'binance-prices', 'coingecko-prices', 'btc-web3', 'cache-react', 'cache-vue', 'chart-tablejs', 'chart-vxe', 'couchcache-audit', 'ejs-audit', 'elliptic-helper', 'elliptic-parser', 'eth-api-node', 'jpeg-metadata', 'other-web3', 'price-fetch', 'price-record', 'snykaudit-helper', 'sync-http-api', 'sync-https-api', 'tslib-react', 'tslib-util', 'ttf-metadata', 'vue-audit', 'vue-gws', 'vuewjs'], 'Malicious GitHub accounts': ['GalaxyStarTeam', 'Cryptowares', 'Cryptoinnowise', 'netgolden'], 'Malicious npm accounts': ['charlestom2023', 'eflodzumibreathbn', 'galaxystardev', 'garik.khasmatulin.76', 'hydsapprokoennl', 'leimudkegoraie3', 'leshakov-mikhail', 'linglidekili9g', 'mashulya.bakhromkina', 'mayvilkushiot', 'outmentsurehauw3', 'paupadanberk', 'pormokaiprevdz', 'podomarev.goga', 'teticseidiff51', 'toimanswotsuphous', 'ufbejishisol']} 

 Additional Details: {'Low-volume campaign': 'GitHub has identified a low-volume social engineering campaign targeting personal accounts of employees in technology firms *The changes* (https://github.blog/security/vulnerability-research/security-alert-social-engineering-campaign-targets-technology-industry-employees/).', 'North Korean objectives': 'The campaign is associated with a group operating in support of North Korean objectives *The changes* (https://github.blog/security/vulnerability-research/security-alert-social-engineering-campaign-targets-technology-industry-employees/). *Phylum reported many such attacks daily* (https://news.ycombinator.com/item?id=36865060).'} 


# Related articles (describing the same threat) 
['https://github.blog/2023-07-18-security-alert-social-engineering-campaign-targets-technology-industry-employees/', 'https://github.blog/security/vulnerability-research/security-alert-social-engineering-campaign-targets-technology-industry-employees/', 'https://blog.phylum.io/sophisticated-ongoing-attack-discovered-on-npm/', 'https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-108a', 'https://news.ycombinator.com/item?id=36865060', 'https://cybersecuritynews.com/lazarus-hacker-group-targeting-developers/']
