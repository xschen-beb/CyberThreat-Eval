Source: [https://www.trendmicro.com/en_us/research/23/a/vice-society-ransomware-group-targets-manufacturing-companies.html](https://www.trendmicro.com/en_us/research/23/a/vice-society-ransomware-group-targets-manufacturing-companies.html)

# Vice Society Ransomware Group Targets Manufacturing Companies

Incident: Vice Society Ransomware Group Targets Manufacturing Companies

Root cause: Exploitation of compromised Remote Desktop Protocol (RDP) credentials and public-facing website vulnerabilities.

Impact: The ransomware attack led to significant data breaches and operational disruptions in manufacturing companies across Brazil, Argentina, Switzerland, and Israel. The financial loss details are not explicitly mentioned in the report.

Mitigation: 
1. **Strengthen RDP Security:**
   - Disable RDP if not needed.
   - Use strong, unique passwords for RDP accounts.
   - Implement multi-factor authentication (MFA) for RDP access.
   - Restrict RDP access using firewalls to allow only specific IP addresses.
   - Regularly update and patch RDP services and related software.

2. **Enhance Vulnerability Management:**
   - Conduct regular vulnerability assessments and penetration testing on public-facing websites and applications.
   - Apply security patches promptly to mitigate known vulnerabilities such as PrintNightmare.
   - Utilize web application firewalls (WAF) to protect against web-based attacks.

3. **Strengthen Endpoint Security:**
   - Deploy advanced endpoint protection solutions that include behavioral analysis and anomaly detection.
   - Regularly update antivirus and anti-malware software.
   - Implement application whitelisting to prevent unauthorized applications from executing.

4. **Implement Network Segmentation:**
   - Segregate critical systems and sensitive data from the rest of the network to limit lateral movement.
   - Utilize network access controls to enforce least privilege principles.

5. **Secure Backup Practices:**
   - Maintain regular, encrypted backups of critical data.
   - Store backups offline and test restore procedures regularly.

6. **Monitoring and Incident Response:**
   - Use Security Information and Event Management (SIEM) systems to monitor and analyze network traffic for signs of intrusion.
   - Establish and practice an incident response plan to quickly contain and remediate attacks.

Detection Signature:
- **Service:** Remote Desktop Protocol (RDP)
- **Port:** 3389
- **Severity:** Critical
- **Incident:** Vice Society Ransomware Attack
- **Signature name:** “RDP Brute-Force Detection”
  
Internal checks:
- **Setting1:** Ensure RDP port (3389) is not exposed on external Internet-facing interfaces.
- **Setting2:** RDP service should not listen on the external network interface.
- **Setting3:** RDP access should be secured with strong authentication mechanisms (e.g., MFA).

External scanning:
- **Port (3389) open:** Regularly scan for open RDP ports on the external network perimeter.
- **Brute-force login attempts:** Monitor failed login attempts to detect brute-force attacks.

IoCs: 
- Domain: 57thandnormal[.]com
- Email addresses: 
  - 876505846904@onionmail[.]org
  - 316186524106@onionmail[.]org
  - v-society.official@onionmail[.]org
- File paths:
  - C:\mnt\smile.exe 
  - C:\ProgramData\toolkiit\{redacted}\output\C\ $Recycle.Bin\{redacted}\$RY0DNVE.exe
  - C:\ProgramData\test.exe
  - C:\windows\temp\svchost.exe

These measures will help prevent, detect, and respond to potential ransomware attacks similar to those carried out by the Vice Society group.
