Source: [https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a)

# StopRansomware BianLian Ransomware Group

Incident: BianLian Ransomware Attack

Root cause: Compromised Remote Desktop Protocol (RDP) credentials and exploitation of vulnerabilities in remote access services.

Impact: The blog does not specify the number of records, devices, or financial losses. The impact is on multiple U.S. and Australian critical infrastructure sectors and private enterprises, potentially causing significant financial, business, and reputational damage.

Mitigation: Implementing robust security measures for remote access and credential management.
 
**Detailed Steps for mitigation:**
1. **Audit Remote Access Tools:**
   - Identify and authorize remote access software on your network.
   - Monitor logs for unusual use of remote access software.
   - Use security software to detect memory-only instances of remote access software.

2. **Restrict Remote Desktop Services:**
   - Close unnecessary RDP ports.
   - Enforce account lockouts after failed login attempts.
   - Apply phishing-resistant multifactor authentication (MFA).
   - Log RDP login attempts.

3. **Disable Command-line and Scripting:**
   - Restrict PowerShell usage through Group Policy.
   - Update PowerShell to the latest version and uninstall older versions.
   - Enable enhanced PowerShell logging.

4. **Strengthen Credential Management:**
   - Place domain admin accounts in a protected users' group.
   - Implement Credential Guard for Windows systems.
   - Avoid storing plaintext credentials in scripts.
   - Implement time-based access for high-privilege accounts.

5. **Implement Backup and Recovery Plans:**
   - Maintain multiple copies of sensitive data in secure locations.
   - Use the 3-2-1 backup strategy.
   - Ensure all backups are encrypted and immutable.

6. **Network Segmentation and Monitoring:**
   - Segment networks to prevent ransomware spread.
   - Use network monitoring tools to detect abnormal activities.
   - Regularly update and enable real-time detection for antivirus software.

Detection Signature:
   - Service: Remote Desktop Protocol (RDP)
   - Port: 3389
   - Severity: Critical
   - Incident: BianLian Ransomware Attack
   - Signature name: “Unauthorized RDP Access”
   - Internal checks:
       - Setting1: RDP port (3389) should not be exposed to the Internet.
       - Setting2: RDP port (3389) should only be accessible within the internal network.
       - Setting3: Use MFA and strong password policies for RDP.
   - External scanning:
       - Port 3389 open
       - Detection of unauthorized RDP connections

IoCs:
   - IPs, Domains, and Hashes related to the BianLian ransomware group:
     - IPs: No specific IPs mentioned.
     - Domains: No specific domains mentioned.
     - Hashes:
         - def.exe: 7b15f570a23a5c5ce8ff942da60834a9d0549ea3ea9f34f900a09331325df893
         - encryptor.exe: 1fd07b8d1728e416f897bef4f1471126f9b18ef108eb952f4b75050da22e8e43
         - exp.exe: 0c1eb11de3a533689267ba075e49d93d55308525c04d6aff0d2c54d1f52f5500
         - system.exe: 40126ae71b857dd22db39611c25d3d5dd0e60316b72830e930fba9baf23973ce
