Source: [https://asec.ahnlab.com/en/62853/](https://asec.ahnlab.com/en/62853/)

# Infostealer Disguised as Adobe Reader Installer

**Incident: Infostealer Disguised as Adobe Reader Installer**

**Root Cause:** Social engineering attack leveraging a fake Adobe Reader installer.

**Impact:** System compromise, potential data theft, and unauthorized access. The specific number of devices and financial losses are not detailed in the report.

**Mitigation:** 
1. **User Awareness and Training:**
   - Educate users on the risks of downloading and running files from unofficial sources.
   - Promote the practice of verifying the authenticity of software from trusted sources.

2. **Antivirus and Endpoint Protection:**
   - Ensure that antivirus and endpoint protection solutions are up to date and capable of detecting the mentioned signatures.
   - Implement behavior-based detection systems to identify and block suspicious activities.

3. **Application Whitelisting:**
   - Use application whitelisting to prevent unauthorized applications from running.

4. **System Hardening:**
   - Regularly update and patch software and operating systems.
   - Remove or restrict administrative privileges to reduce the risk of UAC bypass.

5. **Network Security:**
   - Implement network monitoring to detect and block communication with known malicious C2 servers.
   - Use web filtering to block access to malicious URLs.

6. **Incident Response:**
   - Prepare an incident response plan to quickly address and mitigate any detected compromises.
   - Regularly back up critical data and ensure backups are not connected to the primary network.

**Detection Signature:**
   - **Service:** Windows operating system components (msdt.exe, sdiagnhost.exe)
   - **Port:** N/A
   - **Severity:** Critical
   - **Incident:** Infostealer disguised as Adobe Reader installer
   - **Signature Name:** “Fake Adobe Reader Installer”
   - **Internal Checks:**
     - **Setting1:** Ensure msdt.exe is not misused for launching unauthorized processes.
     - **Setting2:** Monitor for unexpected creation of files in %TEMP% and %AppData% directories.
     - **Setting3:** Detect and alert on loading of unauthorized DLL files by sdiagnhost.exe.
   - **External Scanning:**
     - **Port (N/A):** Focus on identifying communications with known C2 domains.

**IoCs:**
   - **URLs:**
     - hxxps://blamefade.com[.]br/
     - hxxps://thinkforce.com[.]br/
   - **MD5 Hashes:**
     - 02b96e2079bbc151222bb5bd10a4be9d
     - 0eebfc748bc887a6ef5bade20ef9ca6b
     - 84526c50bc14838ddd97657db7c760ca
     - b24441f5249d173015dd0547d1654c6a

Additional IoCs can be found by subscribing to AhnLab TIP.
