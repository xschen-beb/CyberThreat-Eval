# Operation Tainted Love  Chinese APTs Target Telcos in New Attacks

### Incident: Operation Tainted Love | Chinese APTs Target Telcos in New Attacks

**Root Cause:** Vulnerable/Misconfigured Microsoft Exchange Server

**Impact:** The blog does not provide specific details on the number of records leaked, devices, people impacted, or financial losses.

**Mitigation:** Secure the Microsoft Exchange server with authentication credentials and apply necessary security patches.
- **Detailed Steps for Mitigation:**
  1. **Patch Management:**
     - Regularly update Microsoft Exchange servers with the latest security patches and updates.
  
  2. **Webshell Detection and Removal:**
     - Scan for and remove any unauthorized webshells on the server.
     - Utilize security tools to detect the presence of webshells and unusual command executions.
  
  3. **Access Control:**
     - Implement strong authentication mechanisms, including multi-factor authentication (MFA).
     - Use least privilege principles to limit access.

  4. **Network Segmentation:**
     - Segment network to limit lateral movement.
     - Implement strict access controls to sensitive segments.
  
  5. **Monitoring and Logging:**
     - Enable and monitor security logs to detect suspicious activities.
     - Utilize Security Information and Event Management (SIEM) tools to correlate and analyze log data.
  
  6. **Endpoint Security:**
     - Deploy endpoint detection and response (EDR) solutions to detect and mitigate malware infections.
  
  7. **Incident Response Plan:**
     - Develop and regularly update an incident response plan.
     - Conduct regular drills to ensure readiness.

**Detection Signature:**
  - **Service:** Microsoft Exchange Server
  - **Port:** 443 (HTTPs)
  - **Severity:** Critical
  - **Incident:** Tainted Love
  - **Signature name:** "Unauthorized Webshell Execution on Exchange"
  - **Internal Checks:**
    - **Setting1:** Microsoft Exchange Server should not allow unauthorized webshells – Inside VMs
    - **Setting2:** Check for unauthorized file modifications in C:\MS_DATA – Inside VMs
    - **Setting3:** Ensure strong authentication mechanisms are in place – Inside VMs
  - **External Scanning:**
    - **Port (443) open**
    - **Presence of known webshell signatures**

**IoCs:**
- **SHA1 Hashes:**
  - f54a41145b732d47d4a2b0a1c6e811ddcba48558 (pc.exe)
  - 1c405ba0dd99d9333173a8b44a98c6d029db8178 (AddSecurityPackage64.dll (unpatched))
  - df4bd177b40dd66f3efb8d6ea39459648ffd5c0e (AddSecurityPackage64.dll (patched))
  - 814f980877649bc67107d9e27e36fba677cad4e3 (pc.dll)
  - 508408edda49359247edc7008762079c5ba725d9 (getHashFlsa64.dll (unpatched))
  - 97a7f1a36294e5525310f121e1b98e364a22e64d (getHashFlsa64.dll (patched))

No additional IoCs found.
