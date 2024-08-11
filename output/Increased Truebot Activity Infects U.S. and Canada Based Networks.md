Source: [https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-187a](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-187a)

# Increased Truebot Activity Infects U.S. and Canada Based Networks

Incident: Increased Truebot Activity Infects U.S. and Canada Based Networks

Root cause: Exploitation of CVE-2022-31199 in Netwrix Auditor application

Impact: Several U.S. and Canada-based networks were compromised, affecting an unknown number of devices and users. The financial losses could be significant due to data exfiltration and potential ransom demands, but exact figures are not provided in the report.

Mitigation: Secure the Netwrix Auditor application and other affected systems.
**Detailed Steps for mitigation:**
1. **Apply patches to CVE-2022-31199**:
   - Update Netwrix Auditor to version 10.5.
   - Ensure the application is used only on internally facing networks as recommended by Netwrix.
 
2. **Reduce the threat of malicious actors using remote access tools**:
   - Implement application controls and allowlisting.
   - Limit the use of RDP and other remote desktop services.
   - Enforce account lockouts and apply phishing-resistant MFA.
   - Log RDP login attempts and restrict PowerShell usage.
   - Update Windows PowerShell to the latest version and enable enhanced logging.

3. **Reduce the threat of credential compromise**:
   - Place domain admin accounts in the protected users’ group.
   - Implement Credential Guard for Windows 10 and Server 2016.
   - Refrain from storing plaintext credentials in scripts.
   - Implement time-based access for admin-level accounts.

4. **Additional mitigations**:
   - Disable File and Printer sharing services if not needed.
   - Maintain offline backups of data and regularly update them.
   - Require compliance with NIST standards for password management.
   - Segment networks to prevent the spread of ransomware.
   - Implement tools for detecting abnormal network activity.
   - Enable real-time detection for antivirus software on all hosts.
   - Disable unused ports and consider adding email banners for external emails.
   - Ensure backup data is encrypted and immutable.

Detection Signature:
- **Service**: Netwrix Auditor
- **Port**: Not specified (likely to be the default port used by the application)
- **Severity**: Critical
- **Incident**: Truebot malware activity
- **Signature name**: “Netwrix Auditor CVE-2022-31199 exploitation”
- **Internal checks**:
  - Setting1: Ensure Netwrix Auditor is updated to version 10.5.
  - Setting2: Confirm Netwrix Auditor is not exposed to the external Internet.
  - Setting3: Verify that remote access tools are properly allowlisted and monitored.
- **External scanning**:
  - Check for open ports used by Netwrix Auditor.
  - Scan for signs of CVE-2022-31199 exploitation attempts.

IoCs:
- **IP**: 193.3.19[.]173 (Russia), 45.182.189[.]71 (Panama), 92.118.36[.]199, among others.
- **Domain**: https[:]//snowboardspecs[.]com, https[:]//corporacionhardsoft[.]com, https[:]//essadonio.com, among others.
- **URL**: https[:]//snowboardspecs[.]com/nae9v, https[:]//essadonio.com/538332[.]php, among others.
- **File**: Document_16654[.]exe, C:\Intel\RuntimeBroker[.]exe, among others.
- **MD5 Hash**: 6164e9d297d29aa8682971259da06848, among others.
- **SHA256 Hash**: 7d75244449fb5c25d8f196a43a6eb9e453652b2185392376e7d44c21bd8431e7, among others.

For a complete list of IoCs, please refer to the tables provided in the original report.
