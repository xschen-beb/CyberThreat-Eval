# Analysis Of The CloudWizard APT Framework

Incident: CloudWizard APT Framework

Root cause: Misconfigured Windows service running a malicious DLL

Impact: Highly targeted espionage campaign affecting individuals and organizations in Ukraine, including diplomatic and research institutions. Financial losses are difficult to estimate but could be significant given the sensitive nature of the compromised information.

Mitigation: Harden Windows services and executables with enhanced security policies and monitoring.

**Detailed Steps for Mitigation:**
1. **Service Hardening:**
   - Verify and control the permissions of Windows services to prevent unauthorized modifications.
   - Regularly audit services running on critical systems to identify suspicious or unauthorized services.
  
2. **Executable and DLL Control:**
   - Implement application whitelisting to ensure only trusted executables and DLLs run on the system.
   - Monitor for the creation of suspicious paths like `C:\ProgramData\Apparition Storage\syncobjsup.dll`.

3. **Encryption and Communication Security:**
   - Use strong encryption protocols and ensure proper implementation to avoid vulnerabilities.
   - Regularly update cryptographic libraries to the latest versions to mitigate known issues.

4. **Network Security:**
   - Restrict network access to known and trusted sources.
   - Monitor and log outbound connections to detect unauthorized external communications, especially to cloud storage services.

5. **Endpoint Detection and Response (EDR):**
   - Deploy EDR solutions to detect and respond to suspicious activities such as the creation of unusual services or unauthorized DLL injections.

6. **User Training and Awareness:**
   - Educate users on recognizing phishing attempts and the importance of reporting suspicious activities.
   - Conduct regular security drills and training sessions to keep cybersecurity awareness high.

Detection Signature:
- **Service:** Windows Service (syncobjsup)
- **Port:** N/A (focus on service and DLL activity)
- **Severity:** Critical
- **Incident:** CloudWizard APT
- **Signature name:** “Suspicious Windows service detected”
- **Internal checks:**
  - **Setting1:** Monitor and restrict permissions on Windows services.
  - **Setting2:** Regularly audit services for unauthorized configurations.
  - **Setting3:** Implement policies to control DLL execution paths.
- **External scanning:**
  - **Service Name:** syncobjsup
  - **DLL Path:** `C:\ProgramData\Apparition Storage\syncobjsup.dll`

IoCs:
- **MD5 Hashes:**
  - NSIS installer: 0edd23bbea61467f144d14df2a5a043e
  - Loader (syncobjsup.dll): a2050f83ba2aa1c4c95567a5ee155dca
  - Orchestrator (Main.dll): 0ca329fe3d99acfaf209cea559994608
- **SHA256 Hashes:**
  - NSIS installer: 177f1216b55058e30a3ce319dc1c7a9b1e1579ea3d009ba965b18f795c1071a4
  - Loader (syncobjsup.dll): 041e4dcdc0c7eea5740a65c3a15b51ed0e1f0ebd6ba820e2c4cd8fa34fb891a2
  - Orchestrator (Main.dll): 11012717a77fe491d91174969486fbaa3d3e2ec7c8d543f9572809b5cf0f2119
- **Domains and IPs:**
  - 91.228.147[.]23
  - curveroad[.]com
