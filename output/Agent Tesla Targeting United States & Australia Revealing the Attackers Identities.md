# Agent Tesla Targeting United States & Australia Revealing the Attackers Identities

### Incident: Agent Tesla Targeting United States & Australia

**Root cause:**
Exploitation of unsecured email accounts and use of weakly protected servers, including misconfigured Plesk and Round Cube installations.

**Impact:**
62,000 emails were targeted, affecting numerous individuals and organizations across the USA and Australia. The potential financial losses could run into millions, considering the costs associated with data theft, system recovery, and potential legal liabilities.

**Mitigation:**
1. **Secure Email Accounts:**
   - Enforce strong password policies and multi-factor authentication (MFA) for all email accounts.
   - Regularly update and patch email servers and applications.

2. **Harden Server Configurations:**
   - Ensure proper configurations of Plesk and Round Cube, including setting strong administrative credentials and disabling unnecessary services.
   - Use firewalls to restrict access to management interfaces and critical services.

3. **Regular Monitoring and Auditing:**
   - Implement continuous monitoring of email traffic for signs of phishing and malware dissemination.
   - Conduct regular security audits of all systems and configurations.

4. **Employee Training:**
   - Conduct cybersecurity awareness training to educate employees on phishing and social engineering tactics.

5. **Endpoint Protection:**
   - Deploy comprehensive endpoint protection solutions to detect and block malware like Agent Tesla.

**Detailed Steps for Mitigation:**
1. **For Email Accounts:**
   - Implement MFA using apps like Google Authenticator or hardware tokens.
   - Regularly update passwords and enforce complexity requirements.
   - Monitor for unusual login activities and set up alerts.

2. **For Server Hardening:**
   - Change default admin URLs and ports for Plesk and Round Cube.
   - Regularly update server software to the latest versions.
   - Disable unused services and close unnecessary ports.
   - Use intrusion detection/prevention systems (IDS/IPS).

3. **Monitoring and Auditing:**
   - Use tools like SIEM (Security Information and Event Management) to correlate and analyze security logs.
   - Schedule periodic vulnerability assessments and penetration tests.
   - Implement email filtering solutions to detect and block spam and phishing emails.

**Detection Signature:**
- **Service:** Plesk, Round Cube
- **Port:** Common ports such as 80, 443, 8443 (Plesk); 25, 143, 993 (Round Cube)
- **Severity:** Critical
- **Incident:** Agent Tesla Campaign
- **Signature name:** “Plesk/Round Cube Misconfiguration”
- **Internal checks:**
  - Setting1: Plesk and Round Cube should be configured with strong administrative credentials and MFA enabled. – In platform
  - Setting2: Unused ports and services should be disabled and not exposed to the internet. – Inside VMs
  - Setting3: Regular updates and patches should be applied to all software. – Inside VMs
- **External scanning:**
  - Open and vulnerable ports (80, 443, 8443, 25, 143, 993) should be identified.
  - Check for default or weak credentials and lack of MFA.

**IoCs:**
- **IP addresses:**
  - 41.90.185.44
  - 91.215.152.7
  - 172.81.60.206
  - 192.236.236.35
  - 80.68.159.15

- **Domains:**
  - chserver.top
  - dllserver.top

- **Email addresses:**
  - support@chserver.top
  - support@dllserver.top
  - unlimitedsendertech@gmail.com
  - kmarshal101@hotmail.com

- **Hashes:**
  - 8ba55cc754638714764780542eefd629c55703ecf63ae20d5eb65b8c14d3e645
  - 87709f72683c5ffc166f348212b37aadb7943b5653419f2f0edf694fb50f1878
  - 691761d401a6650872d724c30b7ef5972e3792e9a2ba88fdca98b4312fb318d8
