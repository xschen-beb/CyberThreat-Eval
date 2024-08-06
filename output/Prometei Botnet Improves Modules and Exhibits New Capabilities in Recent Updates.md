# Prometei Botnet Improves Modules and Exhibits New Capabilities in Recent Updates

**Incident: Prometei Botnet Infection**

**Root cause: Exploitation of vulnerabilities in Windows and Linux systems, including the BlueKeep vulnerability (CVE-2019-0708) and the use of weak or default credentials for lateral movement and spread.**

**Impact: Approximately 10,000 infected systems worldwide. Financial losses may include costs for incident response, system restoration, and potential lost revenue from compromised systems and mined cryptocurrency. Exact financial losses are not detailed.**

**Mitigation:**
1. **Patch Management:**
   - Ensure all systems, especially those running older versions of Windows, are up-to-date with the latest security patches.
   - Specifically, address the BlueKeep vulnerability (CVE-2019-0708) by applying relevant patches from Microsoft.

2. **Credential Management:**
   - Enforce strong, unique passwords across all systems and services.
   - Implement multi-factor authentication (MFA) to provide an additional layer of security.

3. **Network Security:**
   - Segregate networks to limit lateral movement of potential infections.
   - Implement robust firewall rules to restrict unnecessary inbound and outbound traffic.

4. **Detection and Response:**
   - Deploy endpoint detection and response (EDR) solutions to monitor and mitigate suspicious activities.
   - Regularly review network traffic for unusual patterns, such as unexpected DNS queries or abnormal PowerShell commands.

5. **File Integrity Monitoring:**
   - Implement file integrity monitoring (FIM) to detect unauthorized changes to critical system files and directories.

6. **User Awareness Training:**
   - Educate users about phishing and social engineering tactics to reduce the risk of initial infection vectors.

**Detailed Steps for Mitigation:**
1. **Patch Management:**
   - Schedule and enforce regular patching cycles for all operating systems and applications.
   - Use automated tools to deploy patches and verify their successful installation.

2. **Credential Management:**
   - Implement a password management policy that requires regular password changes and prohibits reuse of old passwords.
   - Use tools like password managers to generate and store complex passwords securely.

3. **Network Security:**
   - Configure firewalls to block unused ports and restrict traffic based on the principle of least privilege.
   - Use network segmentation to isolate critical assets and reduce the attack surface.

4. **Detection and Response:**
   - Integrate SIEM (Security Information and Event Management) with EDR to correlate and analyze security events.
   - Conduct regular threat hunting exercises to proactively identify potential indicators of compromise (IoCs).

5. **File Integrity Monitoring:**
   - Deploy FIM solutions to monitor key system directories and alert on unauthorized changes.
   - Regularly review FIM logs and investigate any anomalies.

6. **User Awareness Training:**
   - Conduct regular security awareness training sessions for employees.
   - Use simulated phishing campaigns to educate users on recognizing malicious emails and links.

**Detection Signature:**
   - **Service:** Apache Webserver, PowerShell, SMB, SSH
   - **Port:** Varies (e.g., 80 for HTTP, 443 for HTTPS, 445 for SMB, 22 for SSH)
   - **Severity:** Critical
   - **Incident:** Prometei Botnet Infection
   - **Signature name:** “Prometei Botnet Activity”
   - **Internal checks:**
     - **Setting1:** Ensure all systems are patched against known vulnerabilities, including BlueKeep (CVE-2019-0708).
     - **Setting2:** Monitor for unauthorized PowerShell execution and SMB communication.
     - **Setting3:** Secure all systems with strong authentication credentials and MFA.
   - **External scanning:**
     - **Port (varies):** Open ports associated with Apache Webserver, SMB, and SSH.
     - **Prometei Indicators:** Presence of known Prometei files and processes (e.g., sqhost.exe, nethelper.exe).

**IoCs:**
- **IP Addresses:**
  - 103.65.236.53
  - 221.120.144.101
  - 177.73.237.55

- **File Hashes:**
  - No specific hashes provided.

- **Domains:**
  - xinchaodbcdbh[.]org
  - xinchaodbcdbh[.]com
  - xinchaoabcdcf[.]org
  - xinchaocecclk[.]org
  - xinchaocecclk[.]net

- **Monero Wallet:**
  - 4A1txQ9L8h8NqF4EtGsZDP5vRN3yTVKynbkyP1jvCiDajNLPepPbBdrbaqBu8fCTcFEFdCtgbekSsTf17B1MhyE2AKCEyfR

**No additional IoCs found in the document beyond those listed.**
