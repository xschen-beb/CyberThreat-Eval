# Eastern Asian Android Assault - FluHorse

**Incident:** Eastern Asian Android Assault - FluHorse

**Root cause:** Use of open-source frameworks (Flutter) for developing malicious applications and distribution via email lures.

**Impact:** The malware targeted various sectors in Eastern Asian markets, including transportation, banking, and dating services, affecting thousands of users. Financial losses and the exact number of affected devices are not detailed but could be significant given the widespread distribution and the nature of stolen data (credentials, credit card information, 2FA codes).

**Mitigation:** Educate users on the dangers of opening links from unknown emails, install applications only from trusted sources, and employ mobile security solutions like Check Point’s Harmony Mobile for real-time malware detection and blocking.

**Detailed Steps for Mitigation:**
1. **User Education:**
   - Conduct regular training sessions to educate users on identifying phishing emails.
   - Encourage users to verify the sender's email address and check for discrepancies in URLs before clicking links.

2. **Application Source Verification:**
   - Advise users to download apps only from official app stores and trusted developers.
   - Implement verification mechanisms to ensure applications are downloaded from legitimate sources.

3. **Mobile Security Solutions:**
   - Deploy mobile security solutions like Check Point’s Harmony Mobile to detect and block malicious apps.
   - Enable on-device network protection to filter and block malicious network traffic.

4. **Email Filtering:**
   - Use advanced email filtering solutions to detect and block phishing emails at the gateway.
   - Implement sandboxing techniques to analyze and quarantine suspicious attachments and links.

5. **Permissions Management:**
   - Regularly review and manage app permissions on mobile devices to ensure minimal access is granted.
   - Use mobile device management (MDM) solutions to enforce permission policies and monitor app behavior.

**Detection Signature:**
   - **Service:** HTTP/HTTPS
   - **Port:** 80/443
   - **Severity:** Critical
   - **Incident:** FluHorse
   - **Signature name:** “FluHorse C&C Communication”
   - **Internal checks:**
      - Setting1: Monitor for unusual HTTP/HTTPS traffic patterns to domains like fetc-net[.]com.
      - Setting2: Check for apps requesting excessive permissions such as SMS access.
      - Setting3: Identify and block apps using Flutter that mimic high-profile legitimate applications.

   - **External scanning:**
      - Port 80/443 open
      - Detect data exfiltration patterns consistent with FluHorse behavior (e.g., user credentials, SMS interception).

**IoCs:**
   - **Hashes:**
     - 0a577ee60ca676e49add6f266a1ee8ba5434290fa8954cc35f87546046008388
     - 2e18c919ad53a66622e404a96cbde15f237a7bfafed1c0896b6b7e289bc230d6
     - 416e22d6b85d6633d1da000058efb3cd597b8b7df5d77a6c3456464d65a775b3
     - 74008170fc5de4d40bcc97b8e2c6fbdb01889805c6ca456fd08134881cad0d2c
     - 8b591b5488dab8adb485ea55197148d6b39715da562537c7d8b1a79cd3639510
     - 910707dd041c13f3379115bdf93bb4984ac20b9ecafd59f93e5089ab3a141e67
     - 9220752302e2bca0002ea701c772b2f2306831711b1c323157ef2573f176821a
     - d78fa2c475ea08f90ef6b189d2a3fddc9ead86ae43df272e9083f92f7a47aabe
     - d8a777b050ba27eeb41c0035f3477882d7eafc56edfcbe1e8cef05a7e85c8b9e
     - de86b0fbbd343f3fc5bb6c19a067a6f063b423132e19c6004c7b696ea1fe0c7d
     - 2811f0426f23a7a3b6a8d8bb7e1bcd79e495026f4dcdc1c2fd218097c98de684
     - 659f69d660179d0e8a5f4c2850c51a05529e0ef06ac739ca6f61fe470917ee96
     - e54a2581545477882a1b7c1f9cbb74fb2aa97fcf1ee8b097c8085302ed6fbf36

   - **Domains:**
     - info1.yelove.xyz
     - jp.yelove.xyz
     - h5.yelove.xyz
     - api.vpbankem.com
     - api.fetctw.xyz
     - api.fetc-net.com
     - api.usadmin-3.top
     - www.pcdstl.com
     - h5.spusp.xyz
