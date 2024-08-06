# Don’t Throw a Hissy Fit; Defend Against Medusa

### Incident: Medusa Ransomware Attack

**Root cause:** Exploitation of a vulnerable external-facing web server leading to the deployment of web shells.

**Impact:** The ransomware attack encrypted files and deleted all VMs from the Hyper-V storage as well as local and cloud backups. The exact number of impacted devices or people and financial losses were not stated in the blog.

**Mitigation:** 
1. **Patch Management:** Regularly update and patch all software, especially those exposed to the internet.
2. **Web Application Security:** Harden web applications and employ web application firewalls (WAFs) to detect and block malicious traffic.
3. **Endpoint Security:** Implement robust endpoint protection solutions that can detect and block malicious scripts and executables.
4. **Network Segmentation:** Segment the network to limit the spread of malware.
5. **Multi-Factor Authentication (MFA):** Enforce MFA for all remote access and administrative accounts.
6. **Backup Solutions:** Regularly back up data and store backups offline or in a secure, isolated environment.
7. **Security Training:** Conduct regular security awareness training for employees to recognize phishing and other social engineering tactics.

**Detailed Steps for Mitigation:**
1. **Update Systems:** Ensure all systems, including web servers, are regularly updated with the latest security patches.
2. **Web Application Firewalls (WAFs):** Deploy WAFs to filter and monitor HTTP/HTTPS requests to web applications.
3. **Endpoint Detection and Response (EDR):** Implement EDR solutions to detect and respond to malicious activities on endpoints.
4. **Network Segmentation:** Divide the network into segments to contain potential breaches.
5. **Regular Backups:** Perform regular backups and verify the integrity of backup files. Store backups offline or in a separate, secure network.
6. **Multi-Factor Authentication:** Implement MFA for accessing critical systems and administrative accounts.
7. **Employee Training:** Provide ongoing training for employees on recognizing phishing attempts and other cyber threats.
8. **Incident Response Plan:** Develop and regularly update an incident response plan to quickly respond to security incidents.

**Detection Signature:**
- **Service:** Windows Management Instrumentation (WMI), PowerShell
- **Port:** N/A (specific to internal services)
- **Severity:** Critical
- **Incident:** Medusa Ransomware Execution
- **Signature name:** “Unauthorized PowerShell and WMI Activity”
- **Internal checks:**
  - **Setting1:** Monitor for unauthorized PowerShell execution with encoded commands.
  - **Setting2:** Monitor WMI activity for unexpected remote executions.
  - **Setting3:** Ensure antivirus and endpoint protection systems are not disabled.
- **External scanning:**
  - **Port:** N/A
  - **Unauthorized PowerShell Execution:** Look for Base64 encoded PowerShell commands.
  - **Service Modification:** Monitor for changes in Windows Defender settings and the installation of unauthorized services.

**IoCs:**
- Domains: webhook[.]site, bashupload[.]com, tmpfiles[.]org
- IP: 134.195.88[.]27:80
- SHA256 Hashes:
  - 8e8db098c4feb81d196b8a7bf87bb8175ad389ada34112052fedce572bf96fd6 (trust.exe/Mimikatz)
  - 3e7529764b9ac38177f4ad1257b9cd56bc3d2708d6f04d74ea5052f6c12167f2 (JAVA_V01.exe)
  - f6ddd6350741c49acee0f7b87bff7d3da231832cb79ae7a1c7aa7f1bc473ac30 (testy.exe/gmer_th.exe)
  - 63187dac3ad7f565aaeb172172ed383dd08e14a814357d696133c7824dcc4594 (JAVA_V02.exe)
  - 781cf944dc71955096cc8103cc678c56b2547a4fe763f9833a848b89bf8443c6 (Sophos.exe)
- File Paths:
  - C:\Users\Sophos.exe
  - C:\Users\admin\Desktop\ (trust.exe, JAVA_V01.exe, testy.exe, gmer_th.exe, JAVA_V02.exe)
  - C:\ProgramData\JWrapper-Remote Access\
  - C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Temporary ASP.NET Files\<APPLICATION NAME>\<HASH>\<HASH>
  - C:\Windows\PSEXESVC.exe
  - C:\Users\<USERS>\AppData\Local\Temp\LAdHW.sys
  - C:\Windows\AdminArsenal\PDQDeployRunner\service-1\PDQDeployRunner-1.exe
  - C:\Users\<USER>\AppData\Local\Temp\2\gaze.exe
  - C:\Windows\System32\gaze.exe

**No IoCs found** beyond those listed above.
