Source: [https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine)

## Related articles (describing the same threat) 
- https://www.darkreading.com/threat-intelligence/chinese-apt-gelsemium-wolfsbane-linux-variant
- https://www.infosecurity-magazine.com/news/linux-malware-wolfsbane-firewood
- https://informationsecuritybuzz.com/unmasking-wolfsbane-new-linux-weapon
- https://www.welivesecurity.com/2021/06/09/gelsemium-when-threat-actors-go-gardening
- https://thehackernews.com/2024/11/chinese-apt-gelsemium-targets-linux.html
- https://therecord.media/china-hackers-linux-malware-target
- https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine
- https://github.com/eset/malware-ioc/tree/master/gelsemium
- https://www.helpnetsecurity.com/2024/11/21/linux-backdoors-wolfsbane-firewood

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: WolfsBane and Firewood Linux Backdoors by Gelsemium APT Group 

#### Root cause 
 The root cause behind this incident is the exploitation of vulnerabilities in internet-facing systems, particularly those running on Linux. The attackers utilized webshells to gain initial access and maintain persistence, along with custom backdoors and rootkits for evasion and data exfiltration. The trend of APT groups focusing on Linux malware is becoming more noticeable due to improvements in Windows security (https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/). The Gelsemium group also utilized supply-chain attacks to distribute their malware (https://www.welivesecurity.com/2021/06/09/gelsemium-when-threat-actors-go-gardening/). They exploited vulnerabilities in Java Web applications to access Apache Tomcat servers (https://www.darkreading.com/threat-intelligence/chinese-apt-gelsemium-wolfsbane-linux-variant). The emergence of WolfsBane and FireWood underscores the need for enhanced security measures across all platforms, especially Linux (https://www.infosecurity-magazine.com/news/linux-malware-wolfsbane-firewood/). The attack chain includes a modified open-source userland rootkit (https://informationsecuritybuzz.com/unmasking-wolfsbane-new-linux-weapon/). Hackers likely exploited an unknown web application vulnerability (https://therecord.media/china-hackers-linux-malware-target). WolfsBane is part of a simple loading chain consisting of the dropper, launcher, and backdoor (https://www.helpnetsecurity.com/2024/11/21/linux-backdoors-wolfsbane-firewood/). *The attackers also used a modified BEURK userland rootkit and a usbdev.ko kernel driver for hiding processes and running commands* (https://thehackernews.com/2024/11/chinese-apt-gelsemium-targets-linux.html). 

#### Threat actor/group/campaign 
 Gelsemium APT Group, a China-aligned threat actor known for cyberespionage activities. 

#### Organization/industry/location 
 The victims are likely entities in Eastern Asia and the Middle East, as the samples were uploaded from Taiwan, the Philippines, and Singapore. The group also targeted governments, universities, electronics manufacturers, and religious organizations (https://www.welivesecurity.com/2021/06/09/gelsemium-when-threat-actors-go-gardening/). 

#### Start date – End date 
 The samples were uploaded to VirusTotal in March 2023 (https://thehackernews.com/2024/11/chinese-apt-gelsemium-targets-linux.html). 

#### MITRE TTPs 
 ['T1583.001 (Acquire Infrastructure: Domains) - High confidence', 'T1583.004 (Acquire Infrastructure: Server) - High confidence', 'T1587.001 (Develop Capabilities: Malware) - High confidence', 'T1059.004 (Command-Line Interface: Unix Shell) - High confidence', 'T1037.004 (Boot or Logon Initialization Scripts: RC Scripts) - High confidence', 'T1543.002 (Create or Modify System Process: Systemd Service) - High confidence', 'T1574.006 (Hijack Execution Flow: Dynamic Linker Hijacking) - High confidence', 'T1547.013 (Boot or Logon Autostart Execution: XDG Autostart Entries) - High confidence', 'T1546.004 (Event Triggered Execution: .bash_profile and .bashrc) - High confidence', 'T1548.001 (Abuse Elevation Control Mechanism: Setuid and Setgid) - High confidence', 'T1070.004 (Indicator Removal: File Deletion) - High confidence', 'T1070.006 (Indicator Removal: Timestomp) - High confidence', 'T1070.009 (Indicator Removal: Clear Persistence) - High confidence', 'T1564.001 (Hide Artifacts: Hidden Files and Directories) - High confidence', 'T1222.002 (File Permissions Modification: Linux and Mac File and Directory Permissions Modification) - High confidence', 'T1027.009 (Obfuscated Files or Information: Embedded Payloads) - High confidence', 'T1014 (Rootkit) - High confidence', 'T1036.005 (Masquerading: Match Legitimate Name or Location) - High confidence', 'T1082 (System Information Discovery) - High confidence', 'T1083 (File and Directory Discovery) - High confidence', 'T1056 (Input Capture) - High confidence', 'T1041 (Exfiltration Over C2 Channel) - High confidence', 'T1574.004 (Hijack Execution Flow: LD_PRELOAD) - High confidence (https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)'] 

#### Impact 
 The exact number of records or financial losses is not disclosed, but the incident involves significant cyberespionage activities targeting sensitive data such as system information, user credentials, and specific files. The attackers utilized additional tools, including a modified SSH client and privilege escalation utility (https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/). They also deployed the Chrommme backdoor and OwlProxy module during their operations (https://www.welivesecurity.com/2021/06/09/gelsemium-when-threat-actors-go-gardening/). Additionally, Firewood backdoor, featuring a kernel-level rootkit, was used (https://www.darkreading.com/threat-intelligence/chinese-apt-gelsemium-wolfsbane-linux-variant). Both malware strains employ advanced obfuscation techniques, complicating detection and analysis (https://www.infosecurity-magazine.com/news/linux-malware-wolfsbane-firewood/). ESET's analysis revealed other tools in the archives, including webshells (https://informationsecuritybuzz.com/unmasking-wolfsbane-new-linux-weapon/). Additionally, FireWood may be shared among multiple China-aligned state hackers, while WolfsBane is a custom tool (https://therecord.media/china-hackers-linux-malware-target). FireWood is connected to a backdoor tracked as Project Wood, used in Operation TooHash (https://www.helpnetsecurity.com/2024/11/21/linux-backdoors-wolfsbane-firewood/). *The campaign was reported by Ravie Lakshmanan* (https://thehackernews.com/2024/11/chinese-apt-gelsemium-targets-linux.html). 

#### Mitigation Steps 
 ['Secure web applications by regularly updating and patching them to prevent vulnerabilities.', 'Implement robust endpoint detection and response (EDR) solutions.', 'Disable unnecessary services and ensure strong authentication mechanisms are in place.', 'Monitor network traffic for unusual activities and potential C2 communications.', 'Regularly audit system configurations and permissions to detect unauthorized changes.', 'Deploy security solutions capable of detecting rootkit activities and hidden files.'] 

#### Detection Signature 
 {'Service': 'Apache Tomcat (example based on the report context)', 'Port': '8080 (example based on common usage)', 'Severity': 'Critical', 'Incident': 'WolfsBane Linux Backdoor', 'Signature name': '“Apache Tomcat webshell detection”', 'Internal checks': ['Verify the integrity of web application files.', 'Monitor for unauthorized changes to .jsp files.', 'Check for unusual processes or network activities originating from the web server.'], 'External scanning': ['Scan for the presence of common webshell patterns in .jsp files.', 'Monitor for unusual HTTP POST requests with encoded payloads.']} 

#### IoCs:
- hash_sha1: 0FEF89711DA11C550D3914DEBC0E663F5D2FB86C ([link](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)) 

- hash_sha1: 44947903B2BC760AC2E736B25574BE33BF7AF40B ([link](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)) 

- hash_sha1: 0AB53321BB9699D354A032259423175C08FEC1A4 ([link](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)) 

- hash_sha1: 8532ECA04C0F58172D80D8A446AE33907D509377 ([link](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)) 

- hash_sha1: B2A14E77C96640914399E5F46E1DEC279E7B940F ([link](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)) 

- hash_sha1: 209C4994A42AF7832F526E09238FB55D5AAB34E5 ([link](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)) 

- hash_sha1: F43D4D46BAE9AD963C2EB05EF43E90AA3A5D88E3 ([link](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)) 

- hash_sha1: FD601A54BC622C041DF0242662964A7ED31C6B9C ([link](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)) 

- hash_sha1: 9F7790524BD759373AB57EE2AAFA6F5D8BCB918A ([link](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)) 

- hash_sha1: 238C8E8EB7A732D85D8A7F7CA40B261D8AE4183D ([link](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/)) 

- domain: dsdsei.com ([link](No link provided)) 

- domain: asidomain.com ([link](No link provided)) 

- ip: 149.248.14.53 ([link](No link provided)) 

- ip: 210.209.72.180 ([link](No link provided)) 

- domain: 4vw37z.cn ([link](No link provided)) 

- domain: acro.ns1.name ([link](No link provided)) 

- domain: domain.dns04.com ([link](No link provided)) 

- domain: info.96html.com ([link](No link provided)) 

- domain: microsoftservice.dns1.us ([link](No link provided)) 

- domain: pctftp.otzo.com ([link](No link provided)) 

- domain: sitesafecdn.hopto.org ([link](No link provided)) 

- domain: traveltime.hopto.org ([link](No link provided)) 

- domain: www.sitesafecdn.dynamic-dns.net ([link](No link provided)) 

- domain: www.travel.dns04.com ([link](No link provided)) 

- For more IoCs, please refer to the above links. 

#### paste IoC
IoC Value
0FEF89711DA11C550D3914DEBC0E663F5D2FB86C
44947903B2BC760AC2E736B25574BE33BF7AF40B
0AB53321BB9699D354A032259423175C08FEC1A4
8532ECA04C0F58172D80D8A446AE33907D509377
B2A14E77C96640914399E5F46E1DEC279E7B940F
209C4994A42AF7832F526E09238FB55D5AAB34E5
F43D4D46BAE9AD963C2EB05EF43E90AA3A5D88E3
FD601A54BC622C041DF0242662964A7ED31C6B9C
9F7790524BD759373AB57EE2AAFA6F5D8BCB918A
238C8E8EB7A732D85D8A7F7CA40B261D8AE4183D
dsdsei.com
asidomain.com
149.248.14.53
210.209.72.180
4vw37z.cn
acro.ns1.name
domain.dns04.com
info.96html.com
microsoftservice.dns1.us
pctftp.otzo.com
sitesafecdn.hopto.org
traveltime.hopto.org
www.sitesafecdn.dynamic-dns.net
www.travel.dns04.com

