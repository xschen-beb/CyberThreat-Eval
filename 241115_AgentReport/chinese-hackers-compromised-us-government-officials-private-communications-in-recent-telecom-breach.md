Source: [https://www.bleepingcomputer.com/news/security/chinese-hackers-compromised-us-government-officials-private-communications-in-recent-telecom-breach](https://www.bleepingcomputer.com/news/security/chinese-hackers-compromised-us-government-officials-private-communications-in-recent-telecom-breach)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/chinese-hackers-compromised-us-government-officials-private-communications-in-recent-telecom-breach
- https://www.bleepingcomputer.com/news/security/chinese-hackers-compromised-us-government-officials-private-communications-in-recent-telecom-breach/
- https://content.govdelivery.com/accounts/USDHSCISA/bulletins/3c1b400
- https://www.bleepingcomputer.com/news/security/us-says-chinese-hackers-breached-multiple-telecom-providers/
- https://www.techtarget.com/searchsecurity/news/366615490/CISA-FBI-confirm-China-breached-telecommunication-providers
- https://www.telecomstechnews.com/news/chinese-hackers-breach-telcos-espionage-campaign/
- https://www.reuters.com/technology/cybersecurity/china-affiliated-actors-compromised-networks-multiple-telecom-companies-us-says-2024-11-13/
- https://www.aljazeera.com/news/2024/11/14/us-says-china-linked-hackers-behind-significant-cyberespionage-campaign
- https://www.infosecurity-magazine.com/news/telecom-hack-exposes-us-officials/
- https://cybelangel.com/us-telecom-salt-typhoon-cyber-assault-china/

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: US Govt Officials� Communications Compromised in Recent Telecom Hack 

#### Root cause 
 The attackers exploited vulnerabilities and possibly misconfigured security settings within the networks of multiple U.S. broadband providers. 

#### Threat actor/group/campaign 
 Salt Typhoon (also known as Earth Estries, FamousSparrow, Ghost Emperor, UNC2286), a Chinese hacking group linked to China's Ministry of State Security (MSS); *PRC-affiliated actors; Volt Typhoon Chinese threat group (https://www.bleepingcomputer.com/news/security/chinese-hackers-compromised-us-government-officials-private-communications-in-recent-telecom-breach/)*; *China-linked hackers stole surveillance data (https://www.reuters.com/technology/cybersecurity/china-affiliated-actors-compromised-networks-multiple-telecom-companies-us-says-2024-11-13/)*; *Flax Typhoon hacking campaign involving malicious software (https://www.aljazeera.com/news/2024/11/14/us-says-china-linked-hackers-behind-significant-cyberespionage-campaign)*; *APT40 (https://cybelangel.com/us-telecom-salt-typhoon-cyber-assault-china/)*. 

#### Organization/industry/location 
 U.S. government officials and telecommunications companies, including AT&T, Verizon, and Lumen Technologies; *Canada-targeted agencies and departments, including federal political parties, the Senate, and the House of Commons (https://www.bleepingcomputer.com/news/security/chinese-hackers-compromised-us-government-officials-private-communications-in-recent-telecom-breach/)*; *commercial telecommunication service providers, other potential U.S. targets alerted by FBI and CISA (https://www.bleepingcomputer.com/news/security/us-says-chinese-hackers-breached-multiple-telecom-providers/)*; *China Telecom (https://www.telecomstechnews.com/news/chinese-hackers-breach-telcos-espionage-campaign/)*; *US mobile phone provider Verizon compromised (https://www.aljazeera.com/news/2024/11/14/us-says-china-linked-hackers-behind-significant-cyberespionage-campaign)*. 

#### Start date � End date 
 The specific start date is unknown, but the attackers maintained access for 'months or longer'. 

#### MITRE TTPs 
 ['T1078: Valid Accounts', 'T1566: Phishing', 'T1071: Application Layer Protocol', 'T1059: Command and Scripting Interpreter', 'T1048: Exfiltration Over Alternative Protocol'] 

#### Impact 
 Compromise of 'private communications' of government officials, theft of customer call records, and access to systems used for court-authorized network wiretapping requests; *collection of vast amounts of internet traffic from ISPs (https://www.bleepingcomputer.com/news/security/chinese-hackers-compromised-us-government-officials-private-communications-in-recent-telecom-breach/)*; *exfiltration of data for law enforcement requests, targeted U.S. critical infrastructure (https://www.techtarget.com/searchsecurity/news/366615490/CISA-FBI-confirm-China-breached-telecommunication-providers)*; *breach of high-ranking national security officials' phone lines (https://www.telecomstechnews.com/news/chinese-hackers-breach-telcos-espionage-campaign/)*; *telephones belonging to then-presidential and vice presidential candidates Donald Trump and JD Vance, and Kamala Harris's 2024 presidential campaign phones (https://www.reuters.com/technology/cybersecurity/china-affiliated-actors-compromised-networks-multiple-telecom-companies-us-says-2024-11-13/)*; *theft of technological and government data (https://www.aljazeera.com/news/2024/11/14/us-says-china-linked-hackers-behind-significant-cyberespionage-campaign)*; *impacting 68% of American wireless traffic (https://cybelangel.com/us-telecom-salt-typhoon-cyber-assault-china/)*. 

#### Mitigation Steps 
 ['Conduct thorough security audits and penetration testing on telecom networks to identify and patch vulnerabilities.', 'Implement multi-factor authentication (MFA) to prevent unauthorized access.', 'Monitor network traffic for unusual activity and set up alerts for potential breaches.', 'Ensure robust logging and monitoring of access to sensitive systems.', 'Regularly update and patch all systems, especially those handling sensitive information.', 'Train staff on recognizing and avoiding phishing attacks and other social engineering tactics.', 'Implement network segmentation to limit the access of critical systems and data.'] 

#### Detection Signature 
 {'Service': 'Telecom Infrastructure', 'Port': 'Various ports involved in telecom data transmission', 'Severity': 'Critical', 'Incident': 'Telecom network breach', 'Signature name': 'Telecom Network Breach Detection', 'Internal checks': ['Setting1: Ensure all telecom infrastructure systems are up-to-date with the latest security patches.', 'Setting2: Monitor access logs for unusual login patterns or locations.', 'Setting3: Implement and review firewall rules to restrict unauthorized access.'], 'External scanning': ['Monitor for unauthorized access attempts from known threat actor IPs.', 'Scan for open ports that should not be publicly accessible.']} 

#### IoCs:
No IoCs found.

#### Additional Information 
 FBI and CISA joint statement; commercial telecommunications infrastructure; broad and significant cyber espionage campaign; CISAMedia@mail.cisa.dhs.gov (https://content.govdelivery.com/accounts/USDHSCISA/bulletins/3c1b400); *FBI and CISA proactive alerts and technical assistance to potential victims, collaboration among U.S. government agencies to mitigate threats (https://www.bleepingcomputer.com/news/security/us-says-chinese-hackers-breached-multiple-telecom-providers/)*; *targeting of U.S. critical infrastructure, including water and energy sectors for at least five years by compromising SOHO routers (https://www.techtarget.com/searchsecurity/news/366615490/CISA-FBI-confirm-China-breached-telecommunication-providers)*; *insights from Nexusguard Director Donny Chong; (https://www.telecomstechnews.com/news/chinese-hackers-breach-telcos-espionage-campaign/)*; *investigation by the Department of Homeland Security's Cyber Safety Review Board (https://www.reuters.com/technology/cybersecurity/china-affiliated-actors-compromised-networks-multiple-telecom-companies-us-says-2024-11-13/)*; *FBI's September report on Flax Typhoon campaign (https://www.aljazeera.com/news/2024/11/14/us-says-china-linked-hackers-behind-significant-cyberespionage-campaign)*; *US federal government multi-agency team formed to address the hack; reported by Kevin Poireault (https://www.infosecurity-magazine.com/news/telecom-hack-exposes-us-officials/)*; *Wall Street Journal report on September 26, 2024 (https://cybelangel.com/us-telecom-salt-typhoon-cyber-assault-china/)*. 


