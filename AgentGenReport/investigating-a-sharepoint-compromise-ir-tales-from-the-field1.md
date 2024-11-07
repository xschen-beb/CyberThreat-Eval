Source: [https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field)

## Related articles (describing the same threat) 
- https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field
- https://github.com/rapid7/Rapid7-Labs/tree/main/Vql
- https://technijian.com/microsoft/microsoft-sharepoint-vulnerability-under-active-exploit/?srsltid=AfmBOori0xDV37eDpnMbLTresNmo0ViXf7Pab_oo3K1nY5gWy-VduJb1
- https://secureteam.co.uk/2024/10/23/critical-microsoft-sharepoint-vulnerability-cve-2024-38094-creates-remote-code-execution-threat/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: SharePoint Compromise 

#### Root cause 
 Exploitation of CVE-2024-38094 in Microsoft SharePoint, a high-severity deserialization flaw involving improper input validation when processing ASPX files, leading to unauthorized access and subsequent lateral movement across the network *Your changes* (https://secureteam.co.uk/2024/10/23/critical-microsoft-sharepoint-vulnerability-cve-2024-38094-creates-remote-code-execution-threat/). 

#### Threat actor/group/campaign 
 Not specified 

#### Organization/industry/location 
 Federal agencies *Your changes* (https://technijian.com/microsoft/microsoft-sharepoint-vulnerability-under-active-exploit/?srsltid=AfmBOori0xDV37eDpnMbLTresNmo0ViXf7Pab_oo3K1nY5gWy-VduJb1) 

#### Start date – End date 
 The attacker remained undetected for two weeks. 

#### MITRE TTPs 
 ['Initial Access: Exploit Public-Facing Application (T1190) - CVE-2024-38094: Microsoft SharePoint Remote Code Execution Vulnerability', 'Defense Evasion: Impair Defenses (T1562) - Using AV to disable or degrade security tools', 'Discovery: Account Discovery (T1087), File and Directory Discovery (T1083), Network Share Discovery (T1135)', 'Command and Control: Proxy (T1090) - Using Fast Reverse Proxy for outbound connection', 'Credential Access: OS Credential Dumping (T1003) - Using tools like Mimikatz', 'Persistence: Scheduled Task/Job (T1053) - Using scheduled tasks to execute the FRP tool'] 

#### Impact 
 Compromised the entire domain; specific records or financial losses not mentioned. Attackers could steal confidential data, spread malware, escalate privileges, disrupt business operations, and create backdoors *Your changes* (https://secureteam.co.uk/2024/10/23/critical-microsoft-sharepoint-vulnerability-cve-2024-38094-creates-remote-code-execution-threat/). 

#### Mitigation Steps 
 ['Secure the SharePoint instance by applying the latest security patches.', 'Implement multi-factor authentication for all administrative accounts.', 'Monitor and restrict the installation of unauthorized software.', 'Enhance logging and monitoring for suspicious activities.', 'Use Endpoint Detection and Response (EDR) solutions to monitor and block suspicious activities.', 'Regularly review and update security configurations and policies.', 'Limit user permissions to trusted users and regularly review permissions *Your changes* (https://secureteam.co.uk/2024/10/23/critical-microsoft-sharepoint-vulnerability-cve-2024-38094-creates-remote-code-execution-threat/).', 'Educate staff on phishing and social engineering tactics *Your changes* (https://secureteam.co.uk/2024/10/23/critical-microsoft-sharepoint-vulnerability-cve-2024-38094-creates-remote-code-execution-threat/).'] 

#### Detection Signature 
 {'Service': 'Microsoft SharePoint', 'Port': '80/443', 'Severity': 'Critical', 'Incident': 'SharePoint Compromise', 'Signature name': 'SharePoint RCE Exploit Detected', 'Internal checks': ['Setting1: Ensure SharePoint servers are patched.', 'Setting2: Monitor for unauthorized software installations.', 'Setting3: Audit logs for suspicious activity and unauthorized access.'], 'External scanning': ['Monitor HTTP/HTTPS traffic for unusual patterns.', 'Use network security tools to detect and block exploitation attempts.']} 

#### IoCs: 
- sha256: d3a6ed07bd3b52c62411132d060560f9c0c88ce183851f16b632a99b4d4e7581 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- sha256: 61c0810a23580cf492a6ba4f7654566108331e7a4134c968c2d6a05261b2d8a1 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- sha256: 95cc0b082fcfc366a7de8030a6325c099d8012533a3234edbdf555df082413c7 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- sha256: d18aa84b7bf0efde9c6b5db2a38ab1ec9484c59c5284c0bd080f5197bf9388b0 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- sha256: f618b09c0908119399d14f80fc868b002b987006f7c76adbcec1ac11b9208940 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- sha256: 95cc0b082fcfc366a7de8030a6325c099d8012533a3234edbdf555df082413c7 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- sha256: e451287843b3927c6046eaabd3e22b929bc1f445eec23a73b1398b115d02e4fb ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- sha256: 1beec8cecd28fdf9f7e0fc5fb9226b360934086ded84f69e3d542d1362e3fdf3 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- sha256: 6ce228240458563d73c1c3cbbd04ef15cb7c5badacc78ce331848f5431b406cc ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- sha256: acb5de5a69c06b7501f86c0522d10fefa9c34776c7535e937e946c6abfc9bbc6 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- ip: 54.255.89.118 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- ip: 18.195.61.200 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- log: POST /_vti_bin/client.svc/web/GetFolderByServerRelativeUrl('/BusinessDataMetadataCatalog/')/Files/add(url='/BusinessDataMetadataCatalog/BDCMetadata.bdcm ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- log: POST /_vti_bin/DelveApi.ashx/config/ghostfile93.aspx ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/)) 

- yaml: https://github.com/rapid7/Rapid7-Labs/tree/main/Vql/Sharepoint_CVE_2024_38094.yaml ([link](https://github.com/rapid7/Rapid7-Labs/tree/main/Vql/Sharepoint_CVE_2024_38094.yaml)) 

#### Additional Information 
 {'Reference': 'https://github.com/rapid7/Rapid7-Labs/tree/main/Vql', 'Proof-of-Concept (PoC)': 'Publicly available on GitHub *Your changes* (https://technijian.com/microsoft/microsoft-sharepoint-vulnerability-under-active-exploit/?srsltid=AfmBOori0xDV37eDpnMbLTresNmo0ViXf7Pab_oo3K1nY5gWy-VduJb1)', 'CISA KEV Catalog': 'Added CVE-2024-38094 *Your changes* (https://technijian.com/microsoft/microsoft-sharepoint-vulnerability-under-active-exploit/?srsltid=AfmBOori0xDV37eDpnMbLTresNmo0ViXf7Pab_oo3K1nY5gWy-VduJb1)', 'Patch Release in July 2024': 'Addressed CVE-2024-38094 *Your changes* (https://technijian.com/microsoft/microsoft-sharepoint-vulnerability-under-active-exploit/?srsltid=AfmBOori0xDV37eDpnMbLTresNmo0ViXf7Pab_oo3K1nY5gWy-VduJb1)', 'Federal agencies patch deadline November 12, 2024': '*Your changes* (https://secureteam.co.uk/2024/10/23/critical-microsoft-sharepoint-vulnerability-cve-2024-38094-creates-remote-code-execution-threat/)'} 


