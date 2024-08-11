Source: [https://www.trendmicro.com/en_us/research/23/h/targetcompany-ransomware-abuses-fud-obfuscator-packers.html](https://www.trendmicro.com/en_us/research/23/h/targetcompany-ransomware-abuses-fud-obfuscator-packers.html)

# TargetCompany Ransomware Abuses FUD Obfuscator Packers

Incident: TargetCompany Ransomware Abuses FUD Obfuscator Packers

Root cause: Exploitation of vulnerable SQL servers

Impact: Not specified in the document, but could potentially impact numerous devices, individuals, and organizations. Financial losses could include ransom payments, data recovery costs, and business interruption expenses.

Mitigation:
1. **Secure SQL Servers:**
   - Ensure SQL servers are up-to-date with the latest security patches.
   - Disable unnecessary SQL services and ports.
   - Implement firewall rules to restrict access to SQL servers.
   - Use strong, unique passwords and implement multi-factor authentication.
   - Regularly audit and monitor SQL server logs for suspicious activities.

2. **Enhance Endpoint Protection:**
   - Deploy advanced endpoint protection solutions that include behavior monitoring and machine learning to detect obfuscated malware.
   - Regularly update antivirus and anti-malware definitions.

3. **Network Security Measures:**
   - Implement network segmentation to limit the spread of malware.
   - Use intrusion detection and prevention systems (IDPS) to detect and block exploitation attempts.
   - Employ network access controls to restrict unauthorized access to critical systems.

4. **User Awareness and Training:**
   - Conduct regular training sessions to educate users on phishing and social engineering attacks.
   - Encourage users to report suspicious activities immediately.

5. **Backup and Recovery:**
   - Maintain regular backups of critical data and ensure that backups are stored securely and offline.
   - Test backup and recovery procedures regularly to ensure data integrity and quick restoration in case of an incident.

Detection Signature:
Service: Microsoft SQL Server
Port: 1433
Severity: Critical
Incident: TargetCompany Ransomware Abuses FUD Obfuscator Packers
Signature name: “SQL Server Exploitation”
Internal checks:
   - Setting1: SQL port (1433) should not be exposed on the external Internet. – In platform
   - Setting2: SQL port (1433) should not listen on the external Internet – Inside VMs
   - Setting3: SQL Server should secure with authentication credentials – Inside VMs
External scanning:
   - Port (1433) open
   - SQL Server default login attempts

IoCs:
- _hxxp://80.66.75[.]37/drtse.exe
- _hxxp://185.209.230[.]21:8080/lighting.exe
- _hxxp://80.66.75.37/Ayhhny.exe
- _hxxp://80.66.75[.]37/lawer.exe
- _hxxp://80.66.75[.]37/Bwarp.exe
- _hxxp://185.209.230[.]21:8080/Auptxums.bat

These URLs and IP addresses are indicators of compromise (IoCs) associated with the initial download attempts for the Remcos RAT and TargetCompany ransomware.
