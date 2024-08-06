# npm Package Found Delivering Sophisticated RAT

Incident: npm Package Found Delivering Sophisticated RAT

Root cause: Malicious npm package ("oscompatible") utilizing DLL search order hijacking and other sophisticated techniques.

Impact: While the exact number of impacted devices and users is not specified in the blog, the financial losses could be significant given the potential for stolen data, unauthorized access, and the resource costs associated with mitigation and recovery.

Mitigation: 
1. **Audit and Monitor Dependencies:**
   - Regularly audit npm packages and dependencies for known vulnerabilities and malicious behavior.
   - Use tools like npm audit and automated risk detection platforms similar to Phylum’s.

2. **Implement Strict Access Controls:**
   - Ensure that only trusted and necessary packages are used in projects.
   - Restrict admin privileges and monitor for unauthorized privilege escalation attempts.

3. **Code Signing and Verification:**
   - Verify the authenticity of packages using digital signatures.
   - Cross-check the validity of code signing certificates and reject packages with revoked or suspicious certificates.

4. **Environment Hardening:**
   - Isolate development environments to limit the impact of compromised packages.
   - Regularly update and patch systems to minimize vulnerabilities.

5. **Behavioral Analysis:**
   - Implement behavioral detection mechanisms to identify unusual activities, such as unauthorized network communications or unexpected privilege escalations.

6. **User Education:**
   - Educate developers about the risks associated with third-party packages and the importance of scrutinizing dependencies.

Detailed Steps for mitigation:
- **Step 1:** Regularly update and maintain a list of approved npm packages.
- **Step 2:** Use security tools to scan for vulnerabilities and malicious behavior in npm packages.
- **Step 3:** Enforce the use of Multi-Factor Authentication (MFA) and least privilege principles for all administrative accounts.
- **Step 4:** Implement network segmentation to limit the lateral movement of malware.
- **Step 5:** Conduct regular security training and awareness programs for developers.
- **Step 6:** Set up continuous monitoring and alerting for suspicious activities in the development environment.

Detection Signature:
Service: npm
Port: Not applicable
Severity: Critical
Incident: npm Package Found Delivering Sophisticated RAT
Signature name: “Malicious npm Package Detection”
Internal checks:
  - Setting1: Monitor for packages that include executable binaries and DLL files.
  - Setting2: Validate the integrity and authenticity of npm packages before use.
  - Setting3: Ensure that packages do not request unnecessary privileged operations.
External scanning:
  - Check for packages with revoked code signing certificates.
  - Monitor for unusual network traffic to suspicious domains.

IoCs found:
- Packages: `oscompatible` (versions 2.3.4, 2.3.3, 2.3.2)
- Hashes:
  - 3712af5f9bfbcdbc4fdd6e2831425b39b0eb3aab1c6d61c004fe96d3a57f21f5
  - d2952e57023848a37fb0f21f0dfb38c9000f610ac2b00c2f128511dfd68bde04
- Domain: kdark1[.]com
- IP: 172.64.149.23
