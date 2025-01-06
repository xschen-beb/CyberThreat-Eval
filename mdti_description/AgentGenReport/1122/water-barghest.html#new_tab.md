Source: [https://www.trendmicro.com/en_us/research/24/k/water-barghest.html#new_tab](https://www.trendmicro.com/en_us/research/24/k/water-barghest.html#new_tab)

## Related articles (describing the same threat) 
- https://www.darkreading.com/cloud-security/water-barghest-sells-hijacked-iot-devices-proxy-botnet-misuse
- https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt
- https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/YARArules-Water_Barghest.txt
- https://www.trendmicro.com/en_us/research/24/k/water-barghest.html#new_tab
- https://gurucul.com/latest-threats/inside-water-barghests-rapid-exploit-to-market-strategy-for-iot-devices
- https://github.com/trendmicro/research/tree/main/botnet_ngioweb
- https://www.trendmicro.com/en_us/research/24/k/water-barghest.html
- https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Water Barghest IoT Device Exploit and Monetization Campaign 

#### Root cause 
 The root cause behind the Water Barghest incident is the exploitation of vulnerabilities in IoT devices, which were sourced from public internet scan databases like Shodan. These vulnerabilities were either n-days or zero-days. The compromised devices were then rapidly enlisted for sale on a residential proxy marketplace. *Water Barghest used automated scripts, often running on VPS, to find and exploit these vulnerabilities* (https://www.trendmicro.com/en_us/research/24/k/water-barghest.html). *The group also utilized cryptocurrency for anonymous transactions, removing financial traceability* (https://www.darkreading.com/cloud-security/water-barghest-sells-hijacked-iot-devices-proxy-botnet-misuse). *Nsocks sells the compromised devices as residential proxies* (https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later). 

#### Threat actor/group/campaign 
 Water Barghest, a cybercriminal group. 

#### Organization/industry/location 
 The victims of this campaign are IoT device owners worldwide, including residential and potentially small business users. *Compromised devices included SOHO routers used by businesses* (https://www.darkreading.com/cloud-security/water-barghest-sells-hijacked-iot-devices-proxy-botnet-misuse). *Targets also include Linear eMerge, Zyxel routers, and Neato vacuums* (https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later). 

#### Start date – End date 
 The Water Barghest botnet operations have been ongoing for more than five years, with significant activities noted from 2018 to 2024. 

#### MITRE TTPs 
 {'T1078': 'Valid Accounts (Confidence: High) - The attackers exploited valid accounts or vulnerabilities to access IoT devices.', 'T1210': 'Exploitation of Remote Services (Confidence: High) - The actors used automated scripts to exploit vulnerabilities in IoT devices.', 'T1095': 'Non-Application Layer Protocol (Confidence: Medium) - The botnet used command-and-control servers to manage the compromised devices.', 'T1071': 'Application Layer Protocol (Confidence: Medium) - The malware communicated with C&C servers using HTTP/HTTPS.', 'T1486': "Data Encrypted for Impact (Confidence: Low) - Although not directly encrypting data, the malware's configuration was encrypted to avoid detection."} 

#### Impact 
 Over 20,000 IoT devices were compromised and monetized by Water Barghest. The financial impact is difficult to quantify but includes potential losses from stolen bandwidth and privacy breaches. *The monetization process, from initial infection to proxy sale, can take as little as 10 minutes* (https://www.trendmicro.com/en_us/research/24/k/water-barghest.html). *Impact assessed as Medium on November 22, 2024* (https://gurucul.com/latest-threats/inside-water-barghests-rapid-exploit-to-market-strategy-for-iot-devices/). *Compromised devices were sold to state-sponsored actors for cyber-espionage* (https://www.darkreading.com/cloud-security/water-barghest-sells-hijacked-iot-devices-proxy-botnet-misuse). 

#### Mitigation Steps 
 {'1': 'Secure IoT devices by ensuring they are not exposed to the internet unless absolutely necessary.', '2': 'Regularly update IoT devices with the latest security patches.', '3': 'Use strong, unique passwords for IoT devices and enable multi-factor authentication if available.', '4': 'Monitor network traffic for unusual activity that could indicate compromised devices.', '5': 'Use network segmentation to limit the impact of a compromised device.'} 

#### Detection Signature 
 {'Service': 'IoT Devices', 'Port': 'Various (dependent on IoT device)', 'Severity': 'Critical', 'Incident': 'Water Barghest Exploit and Monetization Campaign', 'Signature name': 'IoT Device Compromise', 'Internal checks': {'Setting1': 'IoT device management ports should not be exposed on the external internet.', 'Setting2': 'IoT devices should have updated firmware and security patches.', 'Setting3': 'IoT devices should be configured with strong authentication credentials.'}, 'External scanning': {'Public IPs of IoT devices exposed.': 'Shodan or other internet scan services showing IoT devices with vulnerabilities.'}} 

#### IoCs:
- domain: ngioweb.su ([link](https://www.trendmicro.com/en_us/research/24/k/water-barghest.html)) 

- hash_sha256: db1f96b20679f9fb9cbd96b242ab8530102c0105b64c83c3ae544f87594a6fa9 ([link](https://www.trendmicro.com/en_us/research/24/k/water-barghest.html)) 

- ip: 195.154.43.182 ([link](https://www.trendmicro.com/en_us/research/24/k/water-barghest.html)) 

- url: http://ultradomafy.net/jquery.js ([link](https://www.trendmicro.com/en_us/research/24/k/water-barghest.html)) 

- hash_sha256: c91795b59248562e44d6c07526c7ab89dfe45344293703a94a3ae5ff02eab5a4 ([link](https://www.trendmicro.com/en_us/research/24/k/water-barghest.html)) 

- hash_sha256: 0221d333 ([link](https://www.trendmicro.com/en_us/research/24/k/water-barghest.html)) 

- domain: domains_0x00aa44f8.txt ([link](https://github.com/trendmicro/research/tree/main/botnet_ngioweb)) 

- domain: domains_0x05413238_request.js.txt ([link](https://github.com/trendmicro/research/tree/main/botnet_ngioweb)) 

- domain: domains_0x221d333_jquery.js.txt ([link](https://github.com/trendmicro/research/tree/main/botnet_ngioweb)) 

- domain: domains_0x2241d23_metric.txt ([link](https://github.com/trendmicro/research/tree/main/botnet_ngioweb)) 

- domain: domains_0x56edc15_piwik.js.txt ([link](https://github.com/trendmicro/research/tree/main/botnet_ngioweb)) 

- ip: 45.61.141.192 ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- ip: 67.220.85.145 ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- ip: 77.83.199.142 ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- ip: 79.141.162.154 ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- ip: 95.169.180.227 ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: dnslookip.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: ipscoredns.com ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/water-barghest/IOClist-Water_Barghest.txt)) 

- domain: misukumotist.info ([link](https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later)) 

- domain: exagenafy.com ([link](https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later)) 

- domain: prenurevaty.info ([link](https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later)) 

- domain: monobimefist.com ([link](https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later)) 

- domain: Remalexation.name ([link](https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later)) 

- ip: 141.98.82.229 ([link](https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later)) 

- ip: 91.227.77.217 ([link](https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later)) 

- ip: 154.7.253.113 ([link](https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later)) 

- ip: 216.107.139.52 ([link](https://levelblue.com/blogs/labs-research/ngioweb-remains-active-7-years-later)) 

- For more IoCs, please refer to the above links. 

#### Additional Information 
 {'YARA Rules': 'YARA rules for Water Barghest include conditions on ELF files and AES keys in the .data section with specific signatures.', 'Signatures': [{'rule_name': 'ngioweb_4B87', 'author': 'Fernando Merces @ Trend Micro FTR', 'description': 'AES key in the beginning for the .data section', 'date': '2024-07-04', 'key': '4B877DFA470E2943C0F6E1C967B0BF3B5B642E0050F5076F787A76BC40EBC6FE'}, {'rule_name': 'ngioweb_76EB', 'author': 'Fernando Merces @ Trend Micro FTR', 'description': 'AES key in the beginning for the .data section', 'date': '2024-07-04', 'key': '76EBEBBADA54D5B32CC77D7C7D2AA54053BA9E8934907F90C1ED1EB8A17AFE6A'}, {'rule_name': 'ngioweb_DB1F', 'author': 'Fernando Merces @ Trend Micro FTR', 'description': 'AES key in the beginning for the .data section', 'date': '2024-03-29', 'key': 'DB1F96B20679F9FB9CBD96B242AB8530102C0105B64C83C3AE544F87594A6FA9'}, {'rule_name': 'ngioweb_DDB3', 'author': 'Fernando Merces @ Trend Micro FTR', 'description': 'AES key in the beginning for the .data section', 'date': '2024-03-29', 'key': 'DDB3D94E5F0396220E6D60144F99C2A65E0472BE5B20812CC9A01F833592FB6B'}]} 

#### paste IoC
IoC Value
ngioweb.su
db1f96b20679f9fb9cbd96b242ab8530102c0105b64c83c3ae544f87594a6fa9
195.154.43.182
http://ultradomafy.net/jquery.js
c91795b59248562e44d6c07526c7ab89dfe45344293703a94a3ae5ff02eab5a4
0221d333
domains_0x00aa44f8.txt
domains_0x05413238_request.js.txt
domains_0x221d333_jquery.js.txt
domains_0x2241d23_metric.txt
domains_0x56edc15_piwik.js.txt
45.61.141.192
67.220.85.145
77.83.199.142
79.141.162.154
95.169.180.227
dnslookip.com
ipscoredns.com
misukumotist.info
exagenafy.com
prenurevaty.info
monobimefist.com
Remalexation.name
141.98.82.229
91.227.77.217
154.7.253.113
216.107.139.52

