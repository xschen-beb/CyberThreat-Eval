Source: [https://www.sentinelone.com/labs/malvirt-net-virtualization-thrives-in-malvertising-attacks/](https://www.sentinelone.com/labs/malvirt-net-virtualization-thrives-in-malvertising-attacks/)

# MalVirt   .NET Virtualization Thrives in Malvertising Attacks

# Enriched Doc (enrihcments marked with *content*(link)): 
Incident: MalVirt | .NET Virtualization Thrives in Malvertising Attacks

Root cause: The root cause behind the incident includes the use of malvertising to distribute virtualized .NET malware loaders that employ significant anti-analysis and anti-detection techniques. The loaders, known as MalVirt, use the KoiVM virtualizing protector for obfuscation and the Windows Process Explorer driver for terminating processes.

Threat Actor/group/campaign: Unknown specific threat actor, but the campaign is named MalVirt, distributing Formbook family malware.

Organization/industry/location: Various organizations and individuals targeted through malicious advertising and search engine poisoning.

Start date – End date: The attack was observed and reported on February 2, 2023, ongoing at the time of writing.

MITRE TTPs: 
- T1027: Obfuscated Files or Information
- T1071.001: Application Layer Protocol: Web Protocols
- T1082: System Information Discovery
- T1059.001: Command and Scripting Interpreter: PowerShell
- T1112: Modify Registry
- T1134: Access Token Manipulation
- T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder

Impact: The exact number of people or devices impacted is not disclosed, but the malvertising campaign could potentially affect a large audience given the scale of Google search engine advertisements.

Mitigation: 
1. **User Awareness and Training**: Educate users to avoid clicking on suspicious advertisements and downloading software from untrusted sources.
2. **Ad Blocking**: Use ad-blocking browser extensions to reduce exposure to malicious ads.
3. **Endpoint Protection**: Deploy advanced endpoint protection solutions that can detect and block obfuscated malware.
4. **Email Filtering**: Implement email security solutions to detect and block phishing emails distributing malware payloads.
5. **Regular Audits**: Conduct regular security audits and assessments to identify and mitigate vulnerabilities.
6. **Patch Management**: Keep all systems and software up to date with the latest security patches.
7. **Network Segmentation**: Use network segmentation to limit malware spread within the organization.

Detection Signature:
Service: Web Browser (Google Chrome, Mozilla Firefox, etc.)
Port: 80, 443
Severity: Critical
Incident: MalVirt | .NET Virtualization Thrives in Malvertising Attacks
Signature name: “Malicious Advertisement Detection”
Internal checks:
- Setting1: Monitor DNS queries and HTTP requests for known malicious domains.
- Setting2: Use endpoint security solutions with capabilities to detect obfuscated .NET malware.
- Setting3: Check for unauthorized or suspicious driver installations and process terminations.
External scanning:
- Check for known malicious domains associated with MalVirt C2 traffic.
- Monitor for unexpected process creation and termination activities.

IoCs:
- SHA1: 15DB79699DCEF4EB5D731108AAD6F97B2DC0EC9C (MalVirt loader sample)
- SHA1: 655D0B6F6570B5E07834AA2DD8211845B4B59200 (0onfirm .NET assembly)
- SHA1: BC47E15537FA7C32DFEFD23168D7E1741F8477ED (Process Explorer driver)
- SHA1: 51582417D24EA3FEEBF441B8047E61CBE1BA2BF4 (Infostealer malware payload)
- Domains: 
    - www.togsfortoads[.]com
    - www.popimart[.]xyz
    - www.kajainterior[.]com
    - www.heji88.hj-88[.]com
    - www.headzees[.]com
    - www.in-snoqualmievalley[.]com
    - www.365heji[.]com
    - www.h3lpr3[.]store
    - www.graciesvoice[.]info
    - www.femfirst.co[.]uk
    - www.cistonewhobeliev[.]xyz
    - www.allspaceinfo[.]com
    - www.baldur-power[.]com
    - www.ohotechnologies[.]com
    - www.carlosaranguiz[.]dev
    - www.iidethakur[.]xyz
    - www.huifeng-tech[.]com 


# Related articles (describing the same threat) 
['https://www.sentinelone.com/labs/malvirt-net-virtualization-thrives-in-malvertising-attacks/']
