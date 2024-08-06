# StopRansomware Phobos Ransomware

**Incident:** Phobos Ransomware Attack

**Root cause:** Insecure Remote Desktop Protocol (RDP) configurations and exploitation of known vulnerabilities.

**Impact:** Multiple municipal and county governments, emergency services, educational institutions, public healthcare, and critical infrastructure entities were affected. Financial losses amounted to several million U.S. dollars. The exact number of devices and people impacted is not specified in the document, but it is implied to be substantial given the variety of targeted sectors.

**Mitigation:** 
1. **Secure RDP:**
   - Close unused RDP ports.
   - Enforce account lockouts after a specified number of failed login attempts.
   - Implement phishing-resistant multifactor authentication (MFA).
   - Log RDP login attempts.
2. **Apply Patches:**
   - Regularly update systems to remediate known vulnerabilities.
3. **Implement EDR Solutions:**
   - Deploy Endpoint Detection and Response (EDR) solutions to monitor and disrupt malicious activities.
4. **Application Controls:**
   - Use application allowlisting to manage and control execution of software, preventing installation and execution of unauthorized remote access tools.
5. **Network Segmentation:**
   - Segment networks to prevent the spread of ransomware and restrict adversary lateral movement.
6. **Password Policies:**
   - Implement strong password policies with at least 15 characters.
   - Store passwords in hashed format and avoid plaintext credentials in scripts.
   - Implement time-based access for admin-level accounts.
7. **Backups:**
   - Maintain offline backups and regularly test backup and restoration processes.
   - Ensure backup data is encrypted and immutable.
8. **Antivirus and Real-Time Detection:**
   - Install and regularly update antivirus software.
   - Enable real-time detection on all hosts.
9. **Disable Unused Ports and Protocols:**
   - Regularly audit and disable unnecessary ports and protocols.

**Detection Signature:**
- **Service:** Remote Desktop Protocol (RDP)
- **Port:** 3389
- **Severity:** Critical
- **Incident:** Phobos Ransomware
- **Signature name:** "Insecure RDP Configuration"
- **Internal checks:**
  - **Setting1:** RDP port (3389) should not be exposed on external Internet.
  - **Setting2:** RDP port (3389) should not listen on the external Internet.
  - **Setting3:** Secure RDP connections with multifactor authentication.
- **External scanning:**
  - **Port (3389) open**
  - **RDP brute-force attempts detected**

**IoCs:**
- **IP Addresses:**
  - 194.165.16[.]4
  - 45.9.74[.]14
  - 147.78.47[.]224
  - 185.202.0[.]111
  
- **Domains:**
  - adstat477d[.]xyz
  - demstat577d[.]xyz
  - serverxlogs21[.]xyz
  
- **Email Addresses:**
  - AlbetPattisson1981@protonmail[.]com
  - henryk@onionmail[.]org
  - atomicday@tuta[.]io
  - info@fobos[.]one
  
- **File Hashes (SHA-256):**
  - 0000599cbc6e5b0633c5a6261c79e4d3d81005c77845c6b0679d854884a8e02f
  - 7451be9b65b956ee667081e1141531514b1ec348e7081b5a9cd1308a98eec8f0
  - 518544e56e8ccee401ffa1b0a01a10ce23e49ec21ec441c6c7c3951b01c1b19c
  - 9215550ce3b164972413a329ab697012e909d543e8ac05d9901095016dd3fc6c

**No additional IoCs found** beyond those listed above.
