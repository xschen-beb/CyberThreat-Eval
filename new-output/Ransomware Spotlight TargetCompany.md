Source: [https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-targetcompany](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-targetcompany)

# Ransomware Spotlight TargetCompany

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Ransomware Spotlight: TargetCompany 

 Root cause: The root cause includes exploitation of vulnerabilities in public-facing applications (CVE-2019-1069 and CVE-2020-0618), misconfigured database servers, and lack of proper security on MS SQL Servers. 

 Threat Actor/group/campaign: The ransomware group, known as TargetCompany (also referred to as Fargo, Mallox, and Xollam), has also been linked to an affiliate named 'vampire' *The changes* (https://www.bleepingcomputer.com/news/security/linux-version-of-targetcompany-ransomware-focuses-on-vmware-esxi/). The group operates a Ransomware-as-a-Service (RaaS) model *The changes* (https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/exposed-and-encrypted-inside-a-mallox-ransomware-attack/#:~:text=Mallox%20ransomware%2C%20also%20known%20as,systems%20and%20VMware%20ESXi%20environments.). 

 Organization/industry/location: TargetCompany ransomware targets industries including manufacturing, retail, telecommunications, IT, apparel, fashion, and automobiles, focusing on enterprises in the Asia-Pacific region, followed by Europe and the Middle East. New attacks have been observed in Taiwan, South Korea, Thailand, and India *The changes* (https://www.bleepingcomputer.com/news/security/linux-version-of-targetcompany-ransomware-focuses-on-vmware-esxi/). 

 Start date – End date: First detected in June 2021 and continues to be active as of the latest report in June 2023. 

 MITRE TTPs: - Initial Access: T1190 - Exploit Public-Facing Application
- Execution: T1059.001 - Command and Scripting Interpreter: PowerShell, T1047 - Windows Management Instrumentation, T1059.003 - Command and Scripting Interpreter: Windows Command Shell
- Persistence: T1547.001 - Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder, T1574.010 - Hijack Execution Flow: Services File Permissions Weakness, T1543.003 - Windows Service
- Defense Evasion: T1222.001 - Windows File and Directory Permissions Modification, T1036.005 - Masquerading: Match Legitimate Name or Location, T1127.001 - Trusted Developer Utilities Proxy Execution: MSBuild, T1218 - System Binary Proxy Execution, T1070.004 - Indicator Removal on Host, T1562.001 - Impair Defenses: Disable or Modify Tools, T1112 - Modify Registry, T1620 - Reflective Code Loading, T1070.004 - Indicator Removal: File Deletion
- Discovery: T1567 - Exfiltration Over Web Service, T1082 - System Language Discovery, T1049 - System Network Connections Discovery
- Credential Access: T1003.001 - OS Credential Dumping: LSASS Memory
- Command and Control: T1071.001 - Application Layer Protocol: Web Protocols
- Lateral Movement: T1570 - Lateral Tool Transfer
- Impact: T1489 - Service Stop, T1486 - Data Encrypted, T1490 - Inhibit System Recovery 

 Impact: 269 attempted attacks detected from March 2022 to April 2023, affecting numerous organizations and industries with significant operational disruptions and potential financial losses. The new Linux variant encrypts files in VMware ESXi environments *The changes* (https://www.bleepingcomputer.com/news/security/linux-version-of-targetcompany-ransomware-focuses-on-vmware-esxi/). The ransomware employs a double extortion tactic and operates a dark web leak site to pressure victims *The changes* (https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/exposed-and-encrypted-inside-a-mallox-ransomware-attack/#:~:text=Mallox%20ransomware%2C%20also%20known%20as,systems%20and%20VMware%20ESXi%20environments.). 

 Mitigation: 1. **Audit and Inventory:**
   - Take inventory of assets and data.
   - Identify authorized and unauthorized devices and types of software.
   - Audit event and incident logs.
2. **Configure and Monitor:**
   - Manage hardware and software configurations.
   - Grant admin privileges and access only when necessary.
   - Monitor network ports, protocols, and services.
   - Activate security configurations on network infrastructure devices.
   - Establish a software allowlist.
3. **Patch and Update:**
   - Conduct regular vulnerability assessments.
   - Perform patching or virtual patching for operating systems and applications.
   - Update software and applications to their latest versions.
4. **Protect and Recover:**
   - Implement data protection, backup, and recovery measures.
   - Enable multifactor authentication (MFA).
5. **Secure and Defend:**
   - Employ sandbox analysis to block malicious emails.
   - Deploy the latest versions of security solutions to all layers of the system.
   - Discover early signs of an attack.
   - Use advanced detection technologies.
6. **Train and Test:**
   - Regularly train and assess employees’ security skills.
   - Conduct red-team exercises and penetration tests. 

 Detection Signature: Service: Microsoft SQL Server
Port: 1433 (default for MS SQL Server)
Severity: Critical
Incident: TargetCompany
Signature name: “MS SQL Server Vulnerability Exploitation”
Internal checks:
   - Ensure MS SQL Server is not publicly accessible.
   - Validate that xp_cmdshell is disabled.
   - Ensure SQL Server is updated with the latest security patches.
External scanning:
   - Port (1433) open
   - Detect any suspicious connections or commands executed via xp_cmdshell 

 IoCs: - No specific IoCs found in the document, but a link to detailed IoCs is provided:
  [TargetCompany IoCs](https://documents.trendmicro.com/assets/txt/ransomware-spotlight-TargetCompany-terminated-IOCs-rwdW7GY.txt). The new Linux variant uses IP addresses traced to an ISP provider in China *The changes* (https://www.bleepingcomputer.com/news/security/linux-version-of-targetcompany-ransomware-focuses-on-vmware-esxi/). Shodan was used to find vulnerable systems *The changes* (https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/exposed-and-encrypted-inside-a-mallox-ransomware-attack/#:~:text=Mallox%20ransomware%2C%20also%20known%20as,systems%20and%20VMware%20ESXi%20environments.). 


# Related articles (describing the same threat) 
['https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-targetcompany', 'https://www.bleepingcomputer.com/news/security/linux-version-of-targetcompany-ransomware-focuses-on-vmware-esxi/', 'https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/exposed-and-encrypted-inside-a-mallox-ransomware-attack/#:~:text=Mallox%20ransomware%2C%20also%20known%20as,systems%20and%20VMware%20ESXi%20environments.']
