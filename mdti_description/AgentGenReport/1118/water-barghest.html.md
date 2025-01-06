Source: [https://www.trendmicro.com/en_us/research/24/k/water-barghest.html](https://www.trendmicro.com/en_us/research/24/k/water-barghest.html)

## Related articles (describing the same threat) 
- https://www.trendmicro.com/en_us/research/24/k/water-barghest.html
- https://github.com/trendmicro/research/tree/main/botnet_ngioweb
- https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt
- https://blog.netmanageit.com/inside-water-barghests-rapid-exploit-to-market-strategy-for-iot-devices/
- https://securityonline.info/water-barghest-botnet-hijacks-20000-iot-devices-for-profit/
- https://malware.news/t/inside-water-barghest-s-rapid-exploit-to-market-strategy-for-iot-devices/88493
- https://pcper.com/2024/05/hackers-sharing-router-botnets-for-nefarious-purposes/

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Water Barghest IoT Device Exploitation 

#### Root cause 
 Exploitation of IoT devices via public Internet scan databases like Shodan and deployment of the Ngioweb malware, which runs in memory and connects to command-and-control servers using automated scripts *Your changes* (https://blog.netmanageit.com/inside-water-barghests-rapid-exploit-to-market-strategy-for-iot-devices/). 

#### Threat actor/group/campaign 
 Water Barghest; *state-level actors* (https://pcper.com/2024/05/hackers-sharing-router-botnets-for-nefarious-purposes/); *Pawn Storm* (https://pcper.com/2024/05/hackers-sharing-router-botnets-for-nefarious-purposes/); *Water Zmeu* (https://pcper.com/2024/05/hackers-sharing-router-botnets-for-nefarious-purposes/) 

#### Organization/industry/location 
 Not specified, but the botnet included over 20,000 IoT devices. 

#### Start date – End date 
 2018 – October 2024 (detailed timeline of operations provided) 

#### MITRE TTPs 
 {'T1200': 'Hardware Additions', 'T1133': 'External Remote Services', 'T1210': 'Exploitation of Remote Services', 'T1071': 'Application Layer Protocol', 'T1071.001': 'Web Protocols', 'T1573': 'Encrypted Channel'} 

#### Impact 
 Over 20,000 IoT devices compromised and monetized using *advanced automation and monetization techniques* (https://malware.news/t/inside-water-barghest-s-rapid-exploit-to-market-strategy-for-iot-devices/); devices include those from brands like Cisco, DrayTek, Fritz!Box, Linksys, Netgear, Synology, Tenda, Western Digital, and Zyxel. 

#### Mitigation Steps 
 {'1': 'Regularly update and patch IoT devices to mitigate known vulnerabilities.', '2': 'Do not expose IoT devices to incoming connections from the open Internet unless necessary.', '3': 'Use strong, unique passwords and enable multi-factor authentication where possible.', '4': 'Implement network segmentation to isolate IoT devices from sensitive networks.', '5': 'Monitor network traffic for unusual activity indicating potential compromise.', '6': 'Employ intrusion detection/prevention systems to identify and block malicious activity.', '7': 'Regularly audit IoT device configurations and apply best security practices.', '8': 'Use threat intelligence services to stay informed about new vulnerabilities and threats.'} 

#### Detection Signature 
 {'Service': 'IoT Devices', 'Severity': 'Critical', 'Incident': 'Water Barghest IoT Exploitation', 'Signature name': 'IoT Device Compromise by Ngioweb Malware', 'Internal checks': {'Setting1': 'Ensure IoT devices are not exposed to the Internet.', 'Setting2': 'Monitor for unusual processes and outbound connections.', 'Setting3': 'Regularly update firmware and apply patches.'}, 'External scanning': {'Open ports used by IoT devices': {}, 'Unusual outbound connections to C&C servers': {}}} 

#### IoCs:
- domain: ngioweb.su ([link](https://www.trendmicro.com)) 

- url: https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=Water%20Barghest ([link](https://www.trendmicro.com)) 

- url: https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=Water%20Barghest%E2%80%99s%20Rapid%20Exploit-to-Market%20Strategy%20for%20IoT%20Devices ([link](https://www.trendmicro.com)) 

- url: https://github.com/trendmicro/research/tree/main/botnet_ngioweb ([link](https://www.trendmicro.com)) 

- url: https://blog.talosintelligence.com/active-exploitation-of-cisco-ios-xe-software/ ([link](https://www.trendmicro.com)) 

- url: https://www.justice.gov/opa/pr/court-authorized-operation-disrupts-worldwide-botnet-used-peoples-republic-china-state ([link](https://www.trendmicro.com)) 

- url: https://www.justice.gov/opa/pr/justice-department-announces-actions-disrupt-advanced-persistent-threat-28-botnet-infected?utm_medium=email&utm_source=govdelivery ([link](https://www.trendmicro.com)) 

- url: https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html ([link](https://www.trendmicro.com)) 

- url: https://www.justice.gov/opa/pr/justice-department-conducts-court-authorized-disruption-botnet-controlled-russian ([link](https://www.trendmicro.com)) 

- url: https://www.trendmicro.com/en_us/research/24/e/router-roulette.html ([link](https://www.trendmicro.com)) 

- script: ngioweb_config_extractor.py ([link](https://github.com/trendmicro/research/tree/main/botnet_ngioweb)) 

- csv: ngioweb_malware.csv ([link](https://github.com/trendmicro/research/tree/main/botnet_ngioweb)) 

- domain_list: domains_0x00aa44f8.txt ([link](https://github.com/trendmicro/research/tree/main/botnet_ngioweb)) 

- domain_list: domains_0x05413238_request.js.txt ([link](https://github.com/trendmicro/research/tree/main/botnet_ngioweb)) 

- ip: 45.61.141.192 ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- ip: 67.220.85.145 ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- ip: 77.83.199.142 ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- ip: 79.141.162.154 ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: dnslookip.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: ipscoredns.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: nslookups.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: asdns.pp.ua ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: asdns2.pp.ua ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: ipwebinfo.net ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: ipinfocheck.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: whosedns.pp.ua ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: antigutation.info ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: antihicipate.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: disimunous.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: emelenalike.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: enidecikive.net ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: exagenafy.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: inoluvary.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: interocakate.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: macrofocafify.org ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: minixetepate.biz ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: misukumotist.info ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: monobimefist.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: prekudinish.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: prenurevaty.info ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: promexucate.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: recepatission.info ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: remalexation.name ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: semiridinution-postepudency.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: subonuker.name ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: ultradomafy.net ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: underuvukent.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- For more IoCs, please refer to the above links. 

#### Additional Information 
 {'Author': 'Daniel Bender *Your changes* (https://blog.netmanageit.com/inside-water-barghests-rapid-exploit-to-market-strategy-for-iot-devices/)', 'Exploitation Method': 'automated scripts *Your changes* (https://blog.netmanageit.com/inside-water-barghests-rapid-exploit-to-market-strategy-for-iot-devices/)', 'Attack Vector': 'zero-day exploit *Your changes* (https://blog.netmanageit.com/inside-water-barghests-rapid-exploit-to-market-strategy-for-iot-devices/)', 'Researchers': 'Trend Micro researchers *Your changes* (https://securityonline.info/water-barghest-botnet-hijacks-20000-iot-devices-for-profit/)', 'Flaw': 'Cisco IOS XE flaw *Your changes* (https://securityonline.info/water-barghest-botnet-hijacks-20000-iot-devices-for-profit/)', 'Marketplaces': 'residential proxy marketplaces *Your changes* (https://securityonline.info/water-barghest-botnet-hijacks-20000-iot-devices-for-profit/)', 'Similar Botnets': 'VPNFilter and Cyclops Blink *Your changes* (https://securityonline.info/water-barghest-botnet-hijacks-20000-iot-devices-for-profit/)'} 


