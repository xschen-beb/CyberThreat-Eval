Source: [https://www.malware-traffic-analysis.net/2024/11/14/index.html](https://www.malware-traffic-analysis.net/2024/11/14/index.html)

## Related articles (describing the same threat) 
- https://www.malware-traffic-analysis.net/2024/11/14/index.html
- https://www.linkedin.com/posts/unit42_raspberryrobin-activity-7262916467707265024-5p8f/
- https://gurucul.com/latest-threats/raspberry-robin-infection-chain-uses-webdav-server/
- https://darktrace.com/blog/the-early-bird-catches-the-worm-darktraces-hunt-for-raspberry-robin
- https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2024-11-14-IOCs-for-Raspberry-Robin-activity.txt

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Raspberry Robin infection using WebDAV server 

#### Root cause 
 The root cause behind the incident is the exploitation of a WebDAV server to host and distribute the Raspberry Robin malware DLL. Victims download a zip archive, extract it, and double-click an HTA file, which loads and runs the DLL from the WebDAV share. *We identified a unique infection chain pattern distributing Raspberry Robin, traceable back to late October 2024. We suspect the initial zip downloads are distributed via embedded third-party ads on various sites attempting to monetize traffic. These zip archives and the extracted HTA files all share the same root name* (https://gurucul.com/latest-threats/raspberry-robin-infection-chain-uses-webdav-server/). *The Raspberry Robin worm, also known as 'QNAP worm,' was first discovered at the end of 2023 but has artifacts dating back to 2019. It uses infected USB drives as an initial infection vector, often spreading through legitimate Windows processes like msiexec.exe to connect to C2 endpoints* (https://darktrace.com/blog/the-early-bird-catches-the-worm-darktraces-hunt-for-raspberry-robin). 

#### Threat actor/group/campaign 
 Raspberry Robin (Malware family) 

#### Organization/industry/location 
 Not explicitly mentioned, but it targets organizations that fall victim to the malware infection. 

#### Start date – End date 
 2024-11-14 (The specific date of the documented infection) 

#### MITRE TTPs 
 ['T1071.001: Application Layer Protocol: Web Protocols', 'T1105: Ingress Tool Transfer', 'T1204.002: User Execution: Malicious File', 'T1036.004: Masquerading: Masquerade Task or Service', '*T1090.003: Command and Control: Multi-hop Proxy* (https://darktrace.com/blog/the-early-bird-catches-the-worm-darktraces-hunt-for-raspberry-robin)', '*T1210: Exploitation of Remote Services* (https://darktrace.com/blog/the-early-bird-catches-the-worm-darktraces-hunt-for-raspberry-robin)', '*T1041: Exfiltration over C2 Channel* (https://darktrace.com/blog/the-early-bird-catches-the-worm-darktraces-hunt-for-raspberry-robin)'] 

#### Impact 
 Potential for sensitive data exfiltration, network compromise, and further malware spread within the infected network. High impact due to unique infection chain pattern. 

#### Mitigation Steps 
 ['Secure WebDAV servers with strong authentication and access controls.', 'Monitor network traffic for unusual patterns, particularly HTTP/HTTPS traffic to unknown WebDAV servers.', 'Implement email and endpoint security solutions to detect and block malicious attachments and scripts.', 'Regularly update and patch all software to protect against known vulnerabilities.', 'Educate employees about the risks of opening unknown attachments and downloading files from untrusted sources.'] 

#### Detection Signature 
 {'Service': 'WebDAV', 'Port': '80, 443 (common ports for HTTP/HTTPS)', 'Severity': 'High', 'Incident': 'Raspberry Robin infection', 'Signature name': 'WebDAV malicious file transfer', 'Internal checks': ['Setting1: Monitor for unexpected WebDAV traffic.', 'Setting2: Check for unauthorized use of HTA files and script executions.', 'Setting3: Validate that network security devices can inspect and block malicious WebDAV traffic.'], 'External scanning': ['Port (80, 443) open', 'WebDAV server hosting malicious files']} 

#### IoCs:
- url: https://www.linkedin.com/posts/unit42_raspberryrobin-activity-7262916467707265024-5p8f/ ([link](blog)) 

- url: https://x.com/Unit42_Intel/status/1857150852114649216 ([link](blog)) 

- url: http://www.malware-traffic-analysis.net/2024/11/14/index.html ([link](fresh malware samples)) 

- hostname: vqdn.net ([link](C2 Server)) 

- hostname: mwgq.net ([link](C2 Server)) 

- hostname: wak.rocks ([link](C2 Server)) 

- hostname: o7car.com ([link](C2 Server)) 

- hostname: 6t.nz ([link](C2 Server)) 

- hostname: fcgz.net ([link](Possible C2 Server)) 

- hostname: d0.wf ([link](C2 Server)) 

- hostname: e0.wf ([link](C2 Server)) 

- hostname: c4z.pl ([link](C2 Server)) 

- hostname: 5g7.at ([link](C2 Server)) 

- hostname: 5ap.nl ([link](C2 Server)) 

- hostname: 4aw.ro ([link](C2 Server)) 

- hostname: 0j.wf ([link](C2 Server)) 

- hostname: f0.tel ([link](C2 Server)) 

- hostname: h0.pm ([link](C2 Server)) 

- hostname: y0.pm ([link](C2 Server)) 

- hostname: 5qy.ro ([link](C2 Server)) 

- hostname: g3.rs ([link](C2 Server)) 

- hostname: 5qe8.com ([link](C2 Server)) 

- hostname: 4j.pm ([link](C2 Server)) 

- hostname: m0.yt ([link](C2 Server)) 

- hostname: zk4.me ([link](C2 Server)) 

- ip: 59.15.11.49 ([link](Likely C2 Server)) 

- ip: 82.124.243.57 ([link](C2 Server)) 

- ip: 114.32.120.11 ([link](Likely C2 Server)) 

- ip: 203.186.28.189 ([link](Likely C2 Server)) 

- ip: 70.124.238.72 ([link](C2 Server)) 

- ip: 73.6.9.83 ([link](Likely C2 Server)) 

- For more IoCs, please refer to the above links. 


