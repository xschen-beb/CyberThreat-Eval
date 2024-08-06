# Apple Crimeware  Massive Rust Infostealer Campaign Aiming for macOS Sonoma Ahead of Public Release

**Incident: Apple Crimeware | Massive Rust Infostealer Campaign**

**Root cause:** Distribution of malware via fake blockchain game websites targeting macOS users.

**Impact:** The exact number of impacted devices and financial losses are not provided. However, the malware is capable of stealing crypto wallets and stored passwords, indicating potentially significant financial loss and impact on numerous users.

**Mitigation:** 
1. **User Awareness and Education:**
   - Educate users about the risks of downloading software from untrusted sources.
   - Promote awareness about phishing and social engineering tactics.

2. **Endpoint Protection:**
   - Use advanced endpoint protection solutions like SentinelOne to detect and prevent the execution of known malware variants.

3. **Authentication and Privilege Management:**
   - Encourage the use of strong, unique passwords and two-factor authentication.
   - Limit the use of administrative privileges to reduce the risk of malware gaining elevated access.

4. **Regular Updates and Patching:**
   - Ensure all systems and software, including macOS, are regularly updated to the latest versions.
   - Apply security patches promptly to mitigate vulnerabilities.

5. **Network Security Measures:**
   - Implement network segmentation to limit the spread of malware.
   - Use intrusion detection and prevention systems to monitor and block malicious traffic.

**Detailed Steps for mitigation:**
1. **Educate and Train Users:**
   - Conduct regular training sessions on cybersecurity best practices.
   - Distribute awareness materials about the risks of fake software and phishing.

2. **Deploy Endpoint Protection:**
   - Install and configure endpoint protection solutions on all devices.
   - Enable real-time protection and automatic updates to ensure the latest threat intelligence is applied.

3. **Implement Strict Privilege Controls:**
   - Review and minimize administrative privileges across all user accounts.
   - Use tools to manage and monitor privilege escalations.

4. **Patch Management:**
   - Establish a routine patch management process for all software and systems.
   - Use automated tools to deploy patches and updates promptly.

5. **Network Security Configuration:**
   - Segment networks to isolate critical systems and sensitive data.
   - Configure firewalls and intrusion detection systems to monitor and block suspicious activities.

**Detection Signature:**
- **Service:** macOS
- **Port:** Not specified (focus on the application layer for this type of malware)
- **Severity:** Critical
- **Incident:** Realst Infostealer
- **Signature name:** “Realst Infostealer Detection”
- **Internal checks:**
  - **Setting1:** Monitor for unauthorized access to keychain databases.
  - **Setting2:** Detect the execution of unfamiliar or suspicious scripts and binaries.
  - **Setting3:** Monitor for attempts to exfiltrate data to known malicious IP addresses.
- **External scanning:**
  - **IP Addresses:** 
    - 77.91.84[.]110
    - 167.172.103[.]83
  - **Domains:** Not specified

**IoCs:**
- IPs:
  - 77.91.84[.]110
  - 167.172.103[.]83
- Team Identifier:
  - C46287MB25
- Bundle Identifier:
  - com.launcher.dev
- SHA1 Hashes of Mach-O Files:
  - Multiple hashes listed in the blog (e.g., 144665cb2e5d65c88579aa4391cebbc116842536, 087b3bf372928279d547fb6bb0ab656717fa8c4b)
- Observed MITRE TTPs:
  - T1033 System Owner/User Discovery (whoami)
  - T1059 Command and Scripting Interpreter (osascript)
  - T1070.004 File Deletion (rmdir)
  - T1082 System Information Discovery (sw_vers)
  - T1083 File and Directory Discovery (dirname, basename)
  - T1553 Bypass or Subvert Trust Controls (xattr)
  - T1620 Reflective Code Loading (execv, fork)
  - T1562 Disable or Modify Tools (sleep, waitpid)
  - T1639.001 Exfiltration Over Unencrypted Non-C2 Protocol (tcp, http)

No additional IoCs found beyond those mentioned in the blog.
