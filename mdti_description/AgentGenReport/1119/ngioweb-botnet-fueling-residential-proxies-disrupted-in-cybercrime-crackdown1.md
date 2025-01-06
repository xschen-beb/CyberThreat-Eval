Source: [https://www.bleepingcomputer.com/news/security/ngioweb-botnet-fueling-residential-proxies-disrupted-in-cybercrime-crackdown](https://www.bleepingcomputer.com/news/security/ngioweb-botnet-fueling-residential-proxies-disrupted-in-cybercrime-crackdown)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/ngioweb-botnet-fueling-residential-proxies-disrupted-in-cybercrime-crackdown
- https://www.bleepingcomputer.com/news/security/ngioweb-botnet-fueling-residential-proxies-disrupted-in-cybercrime-crackdown/
- https://blog.lumen.com/one-sock-fits-all-the-use-and-abuse-of-the-nsocks-botnet/
- https://thehackernews.com/2024/11/ngioweb-botnet-fuels-nsocks-residential.html
- https://cyberscoop.com/proxy-services-cybercrime-ngioweb-botnet-nsocks/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: Ngioweb Botnet Disruption 

#### Root cause 
 The root cause behind the incident is the exploitation of vulnerable or discontinued web application libraries and devices, including products from Zyxel, Reolink, Alpha Technologies, and *Netgear routers* (https://www.bleepingcomputer.com/news/security/ngioweb-botnet-fueling-residential-proxies-disrupted-in-cybercrime-crackdown/). The botnet also leverages around 15 exploits for various n-day vulnerabilities to gain initial access. *Black Lotus Labs identified the botnet's architecture and its loader C2 node at 103.172.92.148* (https://blog.lumen.com/one-sock-fits-all-the-use-and-abuse-of-the-nsocks-botnet/). *The botnet employs a two-tiered architecture with a loader network comprising 15-20 nodes* (https://thehackernews.com/2024/11/ngioweb-botnet-fuels-nsocks-residential.html). *The botnet heavily consists of SOHO routers and IoT devices* (https://cyberscoop.com/proxy-services-cybercrime-ngioweb-botnet-nsocks/). 

#### Threat actor/group/campaign 
 The Ngioweb botnet is operated by an unknown cybercriminal group. Additionally, nation-state hackers (APT28/Fancy Bear/Pawn Storm/Forest Blizzard) have also abused the botnet. *Muddled Libra and VN5Socks have also been tied to the botnet* (https://blog.lumen.com/one-sock-fits-all-the-use-and-abuse-of-the-nsocks-botnet/). *The financially motivated threat actor Water Barghest is also involved* (https://thehackernews.com/2024/11/ngioweb-botnet-fuels-nsocks-residential.html). *Palo Alto Networks’ Unit 42 and Trend Micro have linked various groups to the botnet* (https://cyberscoop.com/proxy-services-cybercrime-ngioweb-botnet-nsocks/). 

#### Organization/industry/location 
 The botnet targets devices globally, with proxies scattered across 180 countries. *Two-thirds of these proxies are based in the U.S.* (https://thehackernews.com/2024/11/ngioweb-botnet-fuels-nsocks-residential.html). *Security experts at Spur and ShadowServer foundation assisted in the takedown* (https://cyberscoop.com/proxy-services-cybercrime-ngioweb-botnet-nsocks/). 

#### Start date – End date 
 The Ngioweb botnet was first observed in 2017, with significant activity noted since late 2022. The disruption efforts were reported on November 19, 2024. 

#### MITRE TTPs 
 ['T1071.001: Application Layer Protocol: Web Protocols', 'T1071.004: Application Layer Protocol: DNS', 'T1090.002: Proxy: External Proxy', 'T1105: Ingress Tool Transfer', 'T1219: Remote Access Software'] 

#### Impact 
 The botnet provided at least 80% of the 35,000 proxies used by the NSOCKS proxy service, which facilitated various malicious activities, including DDoS attacks, hiding malware traffic, credential stuffing, and phishing. *45% of the bots in Ngioweb are sold to NSOCKS through the Shopsocks5 network* (https://www.bleepingcomputer.com/news/security/ngioweb-botnet-fueling-residential-proxies-disrupted-in-cybercrime-crackdown/). *The monetization process can take as little as 10 minutes* (https://thehackernews.com/2024/11/ngioweb-botnet-fuels-nsocks-residential.html). *Proxies can be obtained through a Google search and cryptocurrency payment* (https://cyberscoop.com/proxy-services-cybercrime-ngioweb-botnet-nsocks/). 

#### Mitigation Steps 
 ['Regularly update and patch all web application libraries and devices to mitigate known vulnerabilities.', 'Implement network segmentation to limit the spread of infections.', 'Use intrusion detection and prevention systems to monitor and block suspicious traffic.', 'Employ DNS filtering to block access to known malicious domains.', 'Secure devices with strong authentication mechanisms and disable unused services.', 'Collaborate with industry partners to share threat intelligence and block traffic to and from known C2 nodes.'] 

#### Detection Signature 
 {'Service': 'Web Application Libraries (Zyxel, Reolink, Alpha Technologies)', 'Port': 'Various (depending on the specific service)', 'Severity': 'Critical', 'Incident': 'Ngioweb Botnet', 'Signature name': 'Ngioweb Botnet Activity', 'Internal checks': ['Setting1: Ensure all web application libraries are up-to-date with the latest security patches.', 'Setting2: Monitor for unusual traffic patterns indicative of botnet activity.', 'Setting3: Implement strong authentication and access controls on all devices.'], 'External scanning': ['Monitor for connections to known C2 domains generated by the DGA.', 'Check for DNS TXT records used by the botnet to prevent sinkholing.']} 

#### IoCs: 
- domain: nsocks.net ([link](https://www.bleepingcomputer.com/news/security/ngioweb-botnet-fueling-residential-proxies-disrupted-in-cybercrime-crackdown/)) 

- domain: nsocks.com ([link](https://www.bleepingcomputer.com/news/security/ngioweb-botnet-fueling-residential-proxies-disrupted-in-cybercrime-crackdown/)) 

- ip: 103.172.92.148 ([link](https://blog.lumen.com/one-sock-fits-all-the-use-and-abuse-of-the-nsocks-botnet/)) 

- domain: ngioweb.su ([link](https://thehackernews.com/2024/11/ngioweb-botnet-fuels-nsocks-residential.html)) 

- For more IoCs, please refer to the above links. 


