Source: [https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field)

## Related articles (describing the same threat) 
- https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field
- https://github.com/testanull/MS-SharePoint-July-Patch-RCE-PoC/tree/main
- https://foresiet.com/blog/understanding-sharepoint-remote-code-execution-exploits
- https://vulnera.com/newswire/microsoft-sharepoint-remote-code-execution-vulnerability-exploited-in-corporate-network-breach/
- https://www.qualys.com/research/security-alerts/2024-07-09/microsoft/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: SharePoint Compromise 

#### Root cause 
 The root cause was the exploitation of vulnerabilities (CVE-2024-38094, *CVE-2024-38024, CVE-2024-38023* (https://github.com/testanull/MS-SharePoint-July-Patch-RCE-PoC/tree/main)) within an on-premise SharePoint server, allowing remote code execution (RCE). *These exploits involved specific scripts (poc_filtered.py, poc_specific.py, poc_sub.py) leveraging weaknesses in SharePoint's handling of user inputs and server-side functionalities* (https://foresiet.com/blog/understanding-sharepoint-remote-code-execution-exploits). *Vulnerabilities CVE-2024-38020 and CVE-2024-38021, affecting Office 2021 Retail, Office 2019 Retail, Office 2016 Retail, were also part of the exploitation* (https://www.qualys.com/research/security-alerts/2024-07-09/microsoft/). 

#### Threat actor/group/campaign 
 The specific threat actor or group responsible is unknown. 

#### Organization/industry/location 
 The affected organization is not mentioned. 

#### Start date – End date 
 The attack went undetected for two weeks before the investigation began. *The blog discussing the incident was posted on 11 Jul 2024* (https://foresiet.com/blog/understanding-sharepoint-remote-code-execution-exploits). 

#### MITRE TTPs 
 ['Initial Access: Exploit Public-Facing Application (T1190)', 'Defense Evasion: Impair Defenses (T1562)', 'Discovery: Account Discovery (T1087), File and Directory Discovery (T1083), Network Share Discovery (T1135)', 'Command and Control: Proxy (T1090)', 'Credential Access: OS Credential Dumping (T1003)', 'Persistence: Scheduled Task/Job (T1053)'] 

#### Impact 
 The impact includes domain compromise and installation of malicious binaries to facilitate lateral movement and credential harvesting. *The attacker installed Horoung Antivirus, creating a conflict that disabled security defenses, and allowed for the installation of Impacket for lateral movement. Mimikatz was used for credential harvesting, FRP for remote access, and scheduled tasks for persistence* (https://vulnera.com/newswire/microsoft-sharepoint-remote-code-execution-vulnerability-exploited-in-corporate-network-breach/). 

#### Mitigation Steps 
 ['Patch Management: Ensure SharePoint server is patched to the latest version to mitigate CVE-2024-38094, *CVE-2024-38024, and CVE-2024-38023* (https://github.com/testanull/MS-SharePoint-July-Patch-RCE-PoC/tree/main).', 'Monitor and Harden Exchange Accounts: Regularly audit service accounts and ensure they have minimum necessary privileges.', 'Implement Security Monitoring: Deploy comprehensive monitoring solutions such as InsightIDR and Managed Detection and Response to detect suspicious activities.', 'Incident Response Preparedness: Establish and maintain an incident response plan to quickly address breaches.', 'Security Tooling: Avoid installation of unauthorized software and regularly update endpoint security solutions.'] 

#### Detection Signature 
 {'Service': 'SharePoint', 'Port': 'Typically 80 (HTTP) or 443 (HTTPS)', 'Severity': 'Critical', 'Incident': 'SharePoint Compromise', 'Signature name': '"CVE-2024-38094 Exploitation Attempt"', 'Internal checks': ['Setting1: Ensure SharePoint servers are not exposed to the internet without proper security controls.', 'Setting2: Regularly review and update security patches on SharePoint servers.', 'Setting3: Ensure logging and monitoring are enabled on SharePoint servers.'], 'External scanning': ["Look for POST requests indicating exploitation: POST /_vti_bin/client.svc/web/GetFolderByServerRelativeUrl('/BusinessDataMetadataCatalog/')/Files/add(url='/BusinessDataMetadataCatalog/BDCMetadata.bdcm", 'Check for webshell activity: POST /_vti_bin/DelveApi.ashx/config/ghostfile93.aspx']} 

#### IoCs: 
- hash_sha256: d3a6ed07bd3b52c62411132d060560f9c0c88ce183851f16b632a99b4d4e7581 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- hash_sha256: 61c0810a23580cf492a6ba4f7654566108331e7a4134c968c2d6a05261b2d8a1 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- hash_sha256: 95cc0b082fcfc366a7de8030a6325c099d8012533a3234edbdf555df082413c7 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- hash_sha256: d18aa84b7bf0efde9c6b5db2a38ab1ec9484c59c5284c0bd080f5197bf9388b0 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- hash_sha256: f618b09c0908119399d14f80fc868b002b987006f7c76adbcec1ac11b9208940 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- hash_sha256: e451287843b3927c6046eaabd3e22b929bc1f445eec23a73b1398b115d02e4fb ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- hash_sha256: 1beec8cecd28fdf9f7e0fc5fb9226b360934086ded84f69e3d542d1362e3fdf3 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- hash_sha256: 6ce228240458563d73c1c3cbbd04ef15cb7c5badacc78ce331848f5431b406cc ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- hash_sha256: acb5de5a69c06b7501f86c0522d10fefa9c34776c7535e937e946c6abfc9bbc6 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- ip: 54.255.89.118 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- ip: 18.195.61.200 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

#### Additional Information 
 For a detailed PoC, refer to *the video link* (https://youtu.be/u8mccaakISw) 


