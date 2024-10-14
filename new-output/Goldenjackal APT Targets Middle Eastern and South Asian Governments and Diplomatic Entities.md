Source: [https://securelist.com/goldenjackal-apt-group/109677/](https://securelist.com/goldenjackal-apt-group/109677/)

# Goldenjackal APT Targets Middle Eastern and South Asian Governments and Diplomatic Entities

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: GoldenJackal APT and its malicious toolset 

 Root cause: The root cause includes exploiting the Follina vulnerability in Microsoft Office and using compromised WordPress websites as Command and Control (C2) servers. Attackers spread malware through fake Skype installers and malicious Word documents. *GoldenJackal also targeted air-gapped systems using custom toolsets like GoldenHowl, GoldenRobo, and GoldenDealer* (https://www.welivesecurity.com/en/eset-research/mind-air-gap-goldenjackal-gooses-government-guardrails/). *ESET researchers noted the use of USB-based infiltration* (https://www.infosecurity-magazine.com/news/goldenjackal-exploits-air-gapped/). *JackalControl is a Trojan that allows attackers to remotely manipulate the targeted machine* (https://www.pcrisk.com/removal-guides/26816-jackal-malware). 

 Threat Actor/group/campaign: GoldenJackal APT 

 Organization/industry/location: Government and diplomatic entities in the Middle East, South Asia, and *Europe* (https://www.welivesecurity.com/en/eset-research/mind-air-gap-goldenjackal-gooses-government-guardrails/). 

 Start date – End date: Active since 2019, with ongoing activities observed up to mid-2023 and *March 2024* (https://www.welivesecurity.com/en/eset-research/mind-air-gap-goldenjackal-gooses-government-guardrails/). 

 MITRE TTPs: ['T1193: Spearphishing Attachment', 'T1071: Application Layer Protocol', 'T1105: Ingress Tool Transfer', 'T1047: Windows Management Instrumentation', 'T1059.003: Command and Scripting Interpreter: Windows Command Shell'] 

 Impact: Focused on high-profile government or diplomatic entities, implying a potential high impact on sensitive information. 

 Mitigation: ['Regularly update and patch systems to mitigate known vulnerabilities such as Follina.', 'Use endpoint protection solutions that detect and block malicious documents and executables.', 'Implement network segmentation to limit the lateral movement of attackers.', 'Use multi-factor authentication to secure access to systems and services.', 'Conduct regular security awareness training to recognize phishing attempts.', 'Monitor and audit system and network activities for suspicious behaviors.'] 

 Detection Signature: {'Service': 'Apache, Nginx (compromised WordPress sites)', 'Port': '80, 443', 'Severity': 'Critical', 'Incident': 'GoldenJackal APT', 'Signature name': 'Compromised WordPress as C2', 'Internal checks': ['Verify the integrity of WordPress installations and plugins.', 'Ensure WordPress is up-to-date with the latest security patches.', 'Monitor for unauthorized changes in the WordPress directory.'], 'External scanning': ['Identify WordPress sites with outdated versions.', 'Detect unusual HTTP/HTTPS traffic patterns indicative of C2 communication.']} 

 IoCs: {'MD5 hashes': {'JackalControl': ['5ed498f9ad6e74442b9b6fe289d9feb3', 'a5ad15a9115a60f15b7796bc717a471d', 'c6e5c8bd7c066008178bc1fb19437763', '4f041937da7748ebf6d0bbc44f1373c9', 'eab4f3a69b2d30b16df3d780d689794c', '8c1070f188ae87fba1148a3d791f2523'], 'JackalSteal': 'c05999b9390a3d8f4086f6074a592bc2', 'JackalWorm': '5de309466b2163958c2e12c7b02d8384', 'JackalPerInfo': 'a491aefb659d2952002ef20ae98d7465', 'JackalScreenWatcher': '1072bfeee89e369a9355819ffa39ad20'}, 'Legitimate compromised websites': ['hxxp://abert-online[.]de/meeting/plugins[.]php', 'hxxp://acehigh[.]host/robotx[.]php', 'hxxp://assistance[.]uz/admin/plugins[.]php', 'hxxp://cnom[.]sante[.]gov[.]ml/components/com_avreloaded/views/popup/tmpl/header[.]php', 'hxxp://info[.]merysof[.]am/plugins/search/content/plugins[.]php']} 

 Additional Info: {'LastBuildDate': '*Mon, 22 May 2023 14:30:14 +0000* (https://securelist.com/goldenjackal-apt-group/109677/feed/)', 'Generator': '*WordPress v6.5.5* (https://securelist.com/goldenjackal-apt-group/109677/feed/)', 'UpdateFrequency': '*Hourly* (https://securelist.com/goldenjackal-apt-group/109677/feed/)', 'UpdatePeriod': '*1* (https://securelist.com/goldenjackal-apt-group/109677/feed/)'} 

 *Potential Origins*: The group's tools bear similarities to those used by Russian-speaking groups, particularly noted in the usage of 'transport_http' in GoldenHowl (https://www.infosecurity-magazine.com/news/goldenjackal-exploits-air-gapped/). 


# Related articles (describing the same threat) 
['https://securelist.com/goldenjackal-apt-group/109677/', 'https://securelist.com/goldenjackal-apt-group/109677/feed/', 'https://www.welivesecurity.com/en/eset-research/mind-air-gap-goldenjackal-gooses-government-guardrails/', 'https://www.infosecurity-magazine.com/news/goldenjackal-exploits-air-gapped/', 'https://www.pcrisk.com/removal-guides/26816-jackal-malware']
