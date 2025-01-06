Source: [https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field](https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field)

## Related articles (describing the same threat) 
- https://www.rapid7.com/blog/post/2024/10/30/investigating-a-sharepoint-compromise-ir-tales-from-the-field
- https://github.com/testanull/MS-SharePoint-July-Patch-RCE-PoC/tree/main
- https://foresiet.com/blog/understanding-sharepoint-remote-code-execution-exploits
- https://technijian.com/microsoft/microsoft-sharepoint-vulnerability-under-active-exploit/?srsltid=AfmBOoq_zcjOCPNaH6-agi19kmST0awP5SKjrqNudfm8lAqMm4LpliRJ
- https://secureteam.co.uk/2024/10/23/critical-microsoft-sharepoint-vulnerability-cve-2024-38094-creates-remote-code-execution-threat/
- https://vulnera.com/newswire/microsoft-sharepoint-remote-code-execution-vulnerability-exploited-in-corporate-network-breach/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: SharePoint Compromise 

#### Root cause 
 Exploitation of CVE-2024-38094 vulnerability in an on-premise SharePoint server, *CVE-2024-38024 and CVE-2024-38023* (https://github.com/testanull/MS-SharePoint-July-Patch-RCE-PoC/tree/main). The vulnerability, a deserialization flaw, has a CVSS score of 7.2 and is listed in the CISA KEV Catalog, highlighting its active exploitation and critical nature (https://technijian.com/microsoft/microsoft-sharepoint-vulnerability-under-active-exploit/?srsltid=AfmBOoq_zcjOCPNaH6-agi19kmST0awP5SKjrqNudfm8lAqMm4LpliRJ). *The flaw stems from improper input validation when processing ASPX files and requires minimal user interaction to exploit* (https://secureteam.co.uk/2024/10/23/critical-microsoft-sharepoint-vulnerability-cve-2024-38094-creates-remote-code-execution-threat/). *The attacker utilized a publicly disclosed SharePoint proof-of-concept exploit to install a webshell, compromised a Microsoft Exchange service account with domain administrator privileges, and installed the Horoung Antivirus which disabled security defenses* (https://vulnera.com/newswire/microsoft-sharepoint-remote-code-execution-vulnerability-exploited-in-corporate-network-breach/). 

#### Threat actor/group/campaign 
 Unknown 

#### Organization/industry/location 
 Not specified 

#### Start date – End date 
 Two weeks prior to the investigation start (October 30, 2024) 

#### MITRE TTPs 
 - Initial Access: Exploit Public-Facing Application (T1190)
- Defense Evasion: Impair Defenses (T1562)
- Discovery: Account Discovery (T1087), File and Directory Discovery (T1083), Network Share Discovery (T1135)
- Command and Control: Proxy (T1090)
- Credential Access: OS Credential Dumping (T1003)
- Persistence: Scheduled Task/Job (T1053) 

#### Impact 
 Compromised entire domain, unauthorized access to sensitive information. *Attackers can run arbitrary code, steal confidential data, spread malware, escalate privileges, disrupt business operations, and create backdoors* (https://secureteam.co.uk/2024/10/23/critical-microsoft-sharepoint-vulnerability-cve-2024-38094-creates-remote-code-execution-threat/). *They also used Mimikatz for credential harvesting, Impacket for lateral movement, and attempted to destroy third-party backups but failed* (https://vulnera.com/newswire/microsoft-sharepoint-remote-code-execution-vulnerability-exploited-in-corporate-network-breach/). 

#### Mitigation Steps 
 1. Patch SharePoint to the latest version to prevent exploitation of CVE-2024-38094, *CVE-2024-38024, and CVE-2024-38023* (https://github.com/testanull/MS-SharePoint-July-Patch-RCE-PoC/tree/main).
2. Implement multi-factor authentication (MFA) for all administrative accounts.
3. Monitor and restrict the installation of unapproved software.
4. Utilize endpoint detection and response (EDR) tools to detect and mitigate suspicious activities.
5. Regularly review and audit access logs, especially for domain administrators and service accounts.
6. Conduct regular vulnerability assessments and penetration testing.
7. Ensure continuous monitoring and logging of all critical systems and services using SIEM tools.
*8. Limit user permissions to trusted individuals, regularly review and revoke as necessary.
9. Educate staff on phishing and social engineering tactics to prevent credential theft* (https://secureteam.co.uk/2024/10/23/critical-microsoft-sharepoint-vulnerability-cve-2024-38094-creates-remote-code-execution-threat/). *10. Apply SharePoint updates from June 2024 onwards to mitigate ongoing exploitation* (https://vulnera.com/newswire/microsoft-sharepoint-remote-code-execution-vulnerability-exploited-in-corporate-network-breach/). 

#### Detection Signature 
 Service: Microsoft SharePoint
Port: 80/443 (HTTP/HTTPS)
Severity: Critical
Incident: SharePoint Compromise
Signature name: “Exploitation of CVE-2024-38094”
Internal checks:
    - Setting1: Ensure SharePoint is patched with the latest security updates.
    - Setting2: Monitor for unauthorized software installations, especially on critical servers.
    - Setting3: Implement and enforce strong password policies and MFA for all administrative accounts.
External scanning:
    - Monitor for unusual or unauthorized GET and POST requests to SharePoint endpoints.
    - Detect and investigate any unauthorized access attempts or use of known malicious tools. 

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

#### Additional Info 
 *PoC Video* (https://youtu.be/u8mccaakISw)
*Foresiet's detailed breakdown of exploits* (https://foresiet.com/blog/understanding-sharepoint-remote-code-execution-exploits). 


