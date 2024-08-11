Source: [https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-263a](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-263a)

# StopRansomware Snatch Ransomware

Incident: Snatch Ransomware Attack

Root Cause: Exploitation of weaknesses in Remote Desktop Protocol (RDP) and use of compromised credentials.

Impact: The exact number of records or devices impacted and the financial losses are not specified in the report. However, Snatch threat actors have targeted a wide range of critical infrastructure sectors, including the Defense Industrial Base (DIB), Food and Agriculture, and Information Technology sectors.

Mitigation: Secure the Remote Desktop Protocol (RDP) and compromised credentials. Detailed Steps for mitigation include:

1. **Audit and Restrict Remote Access:**
   - Audit the network for systems using RDP.
   - Close unused RDP ports.
   - Implement strict access controls for RDP.
   - Enforce account lockouts after a specified number of failed attempts.
   - Apply phishing-resistant multifactor authentication (MFA).
   - Log RDP login attempts.

2. **Monitor and Control Execution of Software:**
   - Implement application controls to manage and control execution of software, including allowlisting remote access programs.
   - Prevent installation and execution of unauthorized software.

3. **Enhance Credential Security:**
   - Place domain admin accounts in the protected users’ group.
   - Refrain from storing plaintext credentials in scripts.
   - Implement time-based access for admin-level accounts.
   - Comply with NIST's standards for password policies, including longer passwords and password managers.

4. **Backup and Data Recovery:**
   - Maintain offline backups of data and regularly maintain backup and restoration.
   - Ensure all backup data is encrypted and immutable.

5. **Patch Management:**
   - Keep all operating systems, software, and firmware up to date.
   - Prioritize patching known exploited vulnerabilities.

6. **Network Segmentation:**
   - Segment networks to prevent the spread of ransomware.
   - Control traffic flows and restrict adversary lateral movement.

7. **Endpoint Detection and Response (EDR):**
   - Use EDR tools to detect lateral connections.
   - Regularly update and enable real-time detection for antivirus software.

8. **Disable Unused Ports and Protocols:**
   - Disable unused ports and protocols.

9. **User Account Management:**
   - Review domain controllers, servers, workstations, and active directories for unrecognized accounts.
   - Audit user accounts with administrative privileges and apply the principle of least privilege.

Detection Signature:
   Service: Remote Desktop Protocol (RDP)
   Port: 3389
   Severity: Critical
   Incident: Snatch Ransomware Attack
   Signature name: “RDP Brute Force Detected”
   Internal checks:
      - Setting1: RDP port (3389) should not be exposed on external Internet.
      - Setting2: RDP access should be limited to specific IPs.
      - Setting3: RDP should be secured with multifactor authentication.
   External scanning:
      - Port (3389) open
      - Multiple failed login attempts

IoCs:
- Email Domains: sezname[.]cz, cock[.]li, airmail[.]cc, tutanota[.]com, mail[.]fr, keemail[.]me, protonmail[.]com, swisscows[.]email
- Email Addresses: sn.tchnews.top@protonmail[.]me, funny385@swisscows[.]email, funny385@proton[.]me, russellrspeck@seznam[.]cz, russellrspeck@protonmail[.]com, Mailz13MoraleS@proton[.]me, datasto100@tutanota[.]com, snatch.vip@protonmail[.]com
- TOX Messaging IDs: CAB3D74D1DADE95B52928E4D9DFC003FF5ADB2E082F59377D049A91952E8BB3B419DB2FA9D3F, 7229828E766B9058D329B2B4BC0EDDD11612CBCCFA4811532CABC76ACF703074E0D1501F8418, 83E6E3CFEC0E4C8E7F7B6E01F6E86CF70AE8D4E75A59126A2C52FE9F568B4072CA78EF2B3C97, 0FF26770BFAEAD95194506E6970CC1C395B04159038D785DE316F05CE6DE67324C6038727A58
- Folder Creation: C:\$SysReset
- Filenames and SHA-256 Hashes: Several listed in the document.
- Commands: Several listed in the document.
- Registry Keys: Several listed in the document.
- System Log Changes: Several listed in the document.
- Mutexes Created: Several listed in the document.

This analysis should help understand the nature of the Snatch ransomware attack and provide steps for mitigation and detection.
