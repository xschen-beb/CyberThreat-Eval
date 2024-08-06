# MalVirt   .NET Virtualization Thrives in Malvertising Attacks

Incident: MalVirt Malvertising Campaign

Root cause: Exploitation of malvertising channels and obfuscated .NET virtualization techniques.

Impact: The specific number of people impacted and financial losses are not provided in the document. However, considering the widespread use of malvertising and the nature of the malware involved (Formbook/XLoader), the impact could potentially be significant, affecting numerous devices and resulting in substantial financial losses due to data theft and further malware staging.

Mitigation: 
1. **Secure Advertising Networks:**
   - Work closely with advertising networks to ensure the ads being served are legitimate. Implement stricter verification processes for advertisers.
2. **Advanced Threat Detection and Response:**
   - Deploy advanced endpoint detection and response (EDR) solutions that can identify and respond to sophisticated threats like MalVirt.
3. **User Awareness Training:**
   - Educate users about the risks of clicking on online ads and downloading software from untrusted sources.
4. **Network Security Enhancements:**
   - Implement network-level security measures, such as web filtering and intrusion detection/prevention systems (IDS/IPS), to block malicious traffic.
5. **Code Obfuscation Detection:**
   - Use advanced security tools capable of detecting obfuscated code and virtualized malware loaders.
6. **Regular Software Updates and Patching:**
   - Ensure all systems and security software are up-to-date with the latest patches and definitions.

Detection Signature:
  - Service: N/A (specific service not mentioned, but focus on .NET applications and virtualization techniques)
  - Port: N/A (networks and endpoints should be monitored)
  - Severity: Critical
  - Incident: MalVirt Malvertising Campaign
  - Signature name: “MalVirt Loader Detection”
  - Internal checks:
    - Setting1: Monitor for the presence of unexpected .NET assemblies and virtualization frameworks like KoiVM.
    - Setting2: Detect and alert on the loading of unsigned or suspiciously signed drivers, such as the Process Explorer driver.
    - Setting3: Monitor registry changes indicative of malware persistence mechanisms (e.g., service creation with names like TaskKill).
  - External scanning:
    - Monitor traffic to known malicious domains used for C2 communication.
    - Detect and block malvertising attempts and suspicious ad traffic patterns.

IoCs:
  - SHA1: 15DB79699DCEF4EB5D731108AAD6F97B2DC0EC9C
  - SHA1: 655D0B6F6570B5E07834AA2DD8211845B4B59200
  - SHA1: BC47E15537FA7C32DFEFD23168D7E1741F8477ED
  - SHA1: 51582417D24EA3FEEBF441B8047E61CBE1BA2BF4
  - Domain: www.togsfortoads[.]com
  - Domain: www.popimart[.]xyz
  - Domain: www.kajainterior[.]com
  - Domain: www.heji88.hj-88[.]com
  - Domain: www.headzees[.]com
  - Domain: www.in-snoqualmievalley[.]com
  - Domain: www.365heji[.]com
  - Domain: www.h3lpr3[.]store
  - Domain: www.graciesvoice[.]info
  - Domain: www.femfirst.co[.]uk
  - Domain: www.cistonewhobeliev[.]xyz
  - Domain: www.allspaceinfo[.]com
  - Domain: www.baldur-power[.]com
  - Domain: www.ohotechnologies[.]com
  - Domain: www.carlosaranguiz[.]dev
  - Domain: www.iidethakur[.]xyz
  - Domain: www.huifeng-tech[.]com
