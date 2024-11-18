Source: [https://www.malware-traffic-analysis.net/2024/11/14/index.html](https://www.malware-traffic-analysis.net/2024/11/14/index.html)

## Related articles (describing the same threat) 
- https://www.malware-traffic-analysis.net/2024/11/14/index.html
- https://www.linkedin.com/posts/unit42_raspberryrobin-activity-7262916467707265024-5p8f/
- https://gurucul.com/latest-threats/raspberry-robin-infection-chain-uses-webdav-server/
- https://malware.news/t/2024-11-14-raspberry-robin-infection-using-webdav-server/88459
- https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2024-11-14-IOCs-for-Raspberry-Robin-activity.txt

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Raspberry Robin infection using WebDAV server 

#### Root cause 
 The root cause behind the incident is the exploitation of a WebDAV server to distribute a malicious DLL via a malicious HTA file. *Embedded third-party ads; Initial zip downloads* (https://gurucul.com/latest-threats/raspberry-robin-infection-chain-uses-webdav-server/) *210; 2z.si; ssl; https://bit.ly/3O9XMwA; https://www.malware-traffic-analysis.net/2024/11/14/index.html; *ae2bc3bf.bright-witted.skin; 39eacf27.concurrences.makeup; aee0f533.deoppilant.monster; bff7ca72.deoppilant.monster; 76f2f947.dogtrotted.cyou; 5b20be63.free-handedness.yachts; 7fd6f7f7.luminosity.lol; add1acc4.luminosity.lol; 24306d7b.malalignment.bond; 555248d6.noncancerous.beauty; 9d5d9876.rhinophidae.bond; 80910c15.simple-life.lol; b896c64b.simple-life.lol; d0fddb88.simple-life.lol; eb175142.simple-life.lol; 7c7eb2e6.sulphamidic.mom; 1ba7e0c7.summer-breathing.motorcycles; 52a124a7.summer-breathing.motorcycles; a570fa56.summer-breathing.motorcycles; c7e3e877.summer-breathing.motorcycles; f3612111.summer-breathing.motorcycles; c47fabc0.superaccumulate.mom; 312fe387.unfoolishly.christmas; 9973914b.uteromaniacal.makeup; 11355b83.viticulture.rest; 2c64bb87.viticulture.rest; a74a8d08.viticulture.rest* (https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2024-11-14-IOCs-for-Raspberry-Robin-activity.txt). *Related malware includes MalBot, JinxLoader, Formbook/XLoader, Cerberus (ex-Amnesia)* (https://malware.news/t/2024-11-14-raspberry-robin-infection-using-webdav-server/88459). 

#### Threat actor/group/campaign 
 Raspberry Robin malware campaign 

#### Organization/industry/location 
 Not specified 

#### Start date – End date 
 2024-11-14 (specific event date) 

#### MITRE TTPs 
 {'T1190': 'Exploit Public-Facing Application', 'T1071': 'Application Layer Protocol', 'T1059.001': 'PowerShell', 'T1105': 'Ingress Tool Transfer'} 

#### Impact 
 The exact number of records or devices impacted is not specified. However, the infection involves the spread of the Raspberry Robin malware, which can lead to unauthorized access and potential data breaches. *High impact; traceable back to late October 2024* (https://gurucul.com/latest-threats/raspberry-robin-infection-chain-uses-webdav-server/). 

#### Mitigation Steps 
 {'1': 'Secure the WebDAV server by ensuring it is not publicly accessible unless necessary.', '2': 'Implement strong authentication mechanisms for accessing the WebDAV server.', '3': 'Regularly update and patch all software to address known vulnerabilities.', '4': 'Monitor traffic for unusual patterns indicative of malware activity.', '5': 'Educate staff on the risks of opening unknown or suspicious email attachments.'} 

#### Detection Signature 
 {'Service': 'WebDAV', 'Port': '80, 443 (typical ports for HTTP/HTTPS)', 'Severity': 'Critical', 'Incident': 'Raspberry Robin malware infection', 'Signature name': 'Raspberry Robin WebDAV infection', 'Internal checks': {'1': 'Verify that WebDAV servers are not publicly accessible without proper authentication – In platform', '2': 'Check that WebDAV servers only allow authenticated and authorized access – Inside VMs', '3': 'Ensure that WebDAV servers are patched and updated regularly – Inside VMs'}, 'External scanning': {'1': 'Scan for WebDAV services exposed on ports 80 and 443', '2': 'Monitor for unusual traffic patterns associated with WebDAV servers'}} 

#### IoCs:
- URL 

- Domain 

- For more IoCs, please refer to the above links. 


