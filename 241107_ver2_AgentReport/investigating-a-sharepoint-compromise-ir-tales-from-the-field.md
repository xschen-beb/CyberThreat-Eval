Source: [https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field)

## Related articles (describing the same threat) 
- https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field
- https://foresiet.com/blog/understanding-sharepoint-remote-code-execution-exploits
- https://ogma.in/mitigating-cve-2024-38094-microsoft-sharepoint-remote-code-execution-vulnerability
- https://www.darkreading.com/vulnerabilities-threats/microsoft-sharepoint-vuln-active-exploit

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: SharePoint Compromise 

#### Root cause 
 *Exploitation of CVE-2024-38094, CVE-2024-38024, and CVE-2024-38023 vulnerabilities in an on-premise SharePoint server, allowing remote code execution* (https://foresiet.com/blog/understanding-sharepoint-remote-code-execution-exploits). *The core issue lies in deserialization of untrusted data (CWE-502), leading to arbitrary code execution with a CVSS score of 7.2* (https://ogma.in/mitigating-cve-2024-38094-microsoft-sharepoint-remote-code-execution-vulnerability; https://www.darkreading.com/vulnerabilities-threats/microsoft-sharepoint-vuln-active-exploit). 

#### Threat actor/group/campaign 
 Unknown 

#### Organization/industry/location 
 Not specified 

#### Start date – End date 
 The attacker remained undetected for two weeks before the investigation started. 

#### MITRE TTPs 
 ['Initial Access: Exploit Public-Facing Application (T1190)', 'Defense Evasion: Impair Defense (T1562)', 'Discovery: Account Discovery (T1087), File and Directory Discovery (T1083), Network Share Discovery (T1135)', 'Command and Control: Proxy (T1090)', 'Credential Access: OS Credential Dumping (T1003)', 'Persistence: Scheduled Task/Job (T1053)'] 

#### Impact 
 Compromise of the entire domain, potential exposure of sensitive data, and disabling of security defenses. 

#### Mitigation Steps 
 ['Patch SharePoint servers to the latest version to address CVE-2024-38094, CVE-2024-38024, and CVE-2024-38023 vulnerabilities.', 'Implement network segmentation to limit lateral movement within the network.', '*Implement strong access control policies to limit user privileges and restrict unauthorized access to critical SharePoint resources* (https://foresiet.com/blog/understanding-sharepoint-remote-code-execution-exploits).', '*Deploy intrusion detection systems (IDS), web application firewalls (WAFs), and comprehensive logging to detect and respond to suspicious activities* (https://foresiet.com/blog/understanding-sharepoint-remote-code-execution-exploits).', 'Use strong, unique passwords for service accounts and avoid granting excessive privileges.', 'Monitor and audit authentication logs and event logs for signs of suspicious activity.', 'Ensure all security tools are regularly updated and properly configured.', 'Conduct regular security training for staff to recognize and respond to phishing and other attack vectors.', 'Implement multi-factor authentication (MFA) for all user accounts, especially privileged accounts.', 'Regularly review and update security policies and incident response procedures.', 'Deploy endpoint detection and response (EDR) solutions to monitor and respond to suspicious activities in real-time.', '*Implement secure coding practices, including proper input validation and sanitization, to protect against deserialization vulnerabilities* (https://ogma.in/mitigating-cve-2024-38094-microsoft-sharepoint-remote-code-execution-vulnerability).', '*Conduct regular security audits and vulnerability assessments to ensure systems are up-to-date and compliant with security best practices* (https://ogma.in/mitigating-cve-2024-38094-microsoft-sharepoint-remote-code-execution-vulnerability).', '*Apply the latest fixes by November 12, as required for Federal Civilian Executive Branch (FCEB) agencies* (https://www.darkreading.com/vulnerabilities-threats/microsoft-sharepoint-vuln-active-exploit).'] 

#### Detection Signature 
 {'Service': 'Microsoft SharePoint', 'Port': '80/443 (HTTP/HTTPS)', 'Severity': 'Critical', 'Incident': 'SharePoint Compromise', 'Signature name': '“SharePoint CVE-2024-38094, CVE-2024-38024, CVE-2024-38023 Exploitation”', 'Internal checks': {'Setting1': 'Ensure SharePoint servers are patched to the latest version. – In platform', 'Setting2': 'Monitor and audit SharePoint logs for suspicious GET and POST requests. – Inside VMs', 'Setting3': 'Implement proper authentication and authorization mechanisms for SharePoint services. – Inside VMs'}, 'External scanning': {'Port (80/443) open': True, 'Detection of specific exploitation patterns in HTTP logs': True}} 

#### IoCs:
- hash_sha256: d3a6ed07bd3b52c62411132d060560f9c0c88ce183851f16b632a99b4d4e7581 ([link](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field/))

- hash_sha256: 61c0810a23580cf492a6ba4f7654566108331e7a4134c968c2d6a05261b2d8a1 ([link](same as above))

- hash_sha256: 95cc0b082fcfc366a7de8030a6325c099d8012533a3234edbdf555df082413c7 ([link](same as above))

- hash_sha256: d18aa84b7bf0efde9c6b5db2a38ab1ec9484c59c5284c0bd080f5197bf9388b0 ([link](same as above))

- hash_sha256: f618b09c0908119399d14f80fc868b002b987006f7c76adbcec1ac11b9208940 ([link](same as above))

- hash_sha256: e451287843b3927c6046eaabd3e22b929bc1f445eec23a73b1398b115d02e4fb ([link](same as above))

- hash_sha256: 1beec8cecd28fdf9f7e0fc5fb9226b360934086ded84f69e3d542d1362e3fdf3 ([link](same as above))

- hash_sha256: 6ce228240458563d73c1c3cbbd04ef15cb7c5badacc78ce331848f5431b406cc ([link](same as above))

- hash_sha256: acb5de5a69c06b7501f86c0522d10fefa9c34776c7535e937e946c6abfc9bbc6 ([link](same as above))

- ip: 54.255.89.118 ([link](same as above))

- ip: 18.195.61.200 ([link](same as above))


