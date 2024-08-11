Source: [https://www.securityjoes.com/post/raspberry-robin-detected-itw-targeting-insurance-financial-institutes-in-europe](https://www.securityjoes.com/post/raspberry-robin-detected-itw-targeting-insurance-financial-institutes-in-europe)

# Raspberry Robin Detected ITW Targeting Insurance & Financial Institutes In Europe

**Incident: Raspberry Robin Attacks on Financial Institutes in Europe**

**Root cause:** The primary root cause is the use of a compromised QNAP server which is utilized by Raspberry Robin operators to host command-and-control (C2) infrastructure.

**Impact:** The blog does not provide specific numbers on the financial losses or the number of devices and people impacted. However, it mentions that the financial sector in Europe, particularly Spanish and Portuguese speaking organizations, were targeted.

**Mitigation:** 
1. **Secure QNAP Servers:**
   - Ensure that QNAP devices are not exposed to the internet unnecessarily.
   - Apply the latest firmware updates and security patches to QNAP devices.
   - Use strong, unique passwords for all user accounts and enable two-factor authentication (2FA) where possible.
   - Implement network segmentation to isolate QNAP devices from critical systems and sensitive data.

2. **Strengthen Endpoint Security:**
   - Deploy comprehensive endpoint detection and response (EDR) solutions to monitor for suspicious activities.
   - Regularly update antivirus and anti-malware signatures to detect and block known threats.

3. **Email and Web Security:**
   - Use advanced email filtering solutions to block malicious attachments and links.
   - Implement web filtering solutions to prevent access to known malicious domains.

4. **User Education and Awareness:**
   - Conduct regular training sessions to educate employees about phishing and malware risks.
   - Encourage users to report suspicious emails and attachments to the IT security team.

5. **Incident Response Plan:**
   - Develop and test an incident response plan to quickly contain and mitigate malware infections.
   - Maintain a list of critical assets and prioritize them for protection and response.

**Detection Signature:**
- **Service:** QNAP NAS
- **Port:** 8080
- **Severity:** Critical
- **Incident:** Raspberry Robin
- **Signature name:** “QNAP publicly accessible”
  - **Internal checks:**
    - Setting1: QNAP port (8080) should not be exposed on external Internet. – In platform
    - Setting2: QNAP port (8080) should not listen on the external Internet – Inside VMs
    - Setting3: QNAP device should secure with authentication credentials. – Inside VMs
  - **External scanning:**
    - Port (8080) open
    - QNAP no-pass-login

**IoCs:**
- IP: 85.56.236[.]45
- Malicious MSI installer hash: 29c9426776b62a4461b7a9237a971fb3c5fc3222acd303506a763aa1d314a157
- ZIP dropped by the malicious advertisement campaign: b11805162d3ae3d3c6635c240d004d1fe942a9cde25fb701c92a8e135d37d100
- Unpacked binary: ac7d57c011c1bf1b3158a64d4c91e1d5c54e8d05cdeb9d1fadcbb0c4d5103428
- JScript Encoded Dropper: 21122891977d9296eea86a8a292b2ba7677766a2085566a6e93ecf60f0ac6ee5
- Malicious advertisement redirector: hxxps://eu.adbison-redirect[.]com/click?payload=[JSON_BASE64]
- Abused Discord-related domain: hxxps://cdn.discordapp[.]com/attachments/[random_numeric]/[random_numeric_2]/File_Part.1.ZIP
- Raspberry Robin Yara Rule SHA256: d0a880123eb8671bc04dcf5f79e086e6a0338fbcd40a84af8ac59a7d7a323601


