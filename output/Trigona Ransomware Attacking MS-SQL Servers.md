# Trigona Ransomware Attacking MS-SQL Servers

Incident: Trigona Ransomware Attacking MS-SQL Servers

Root cause: Poorly managed MS-SQL servers with simple account credentials and externally exposed connections.

Impact: The exact number of records and devices impacted is not provided in the document. However, given the nature of ransomware attacks, it can lead to significant data loss, operational disruptions, and potential financial losses due to ransom payments and recovery costs.

Mitigation: 
1. **Strengthen Account Credentials**:
   - Use complex, unique passwords for MS-SQL accounts.
   - Change passwords periodically.
2. **Restrict External Access**:
   - Configure firewalls to restrict access to MS-SQL servers from external networks.
   - Ensure MS-SQL servers are not exposed to the internet.
3. **Enable Authentication and Authorization**:
   - Implement multi-factor authentication (MFA) for accessing MS-SQL servers.
   - Regularly review and update user permissions.
4. **Regular Updates and Patching**:
   - Keep MS-SQL server software and operating systems up-to-date with the latest security patches.
5. **Monitoring and Logging**:
   - Monitor login attempts and set up alerts for suspicious activities.
   - Regularly review security logs for signs of unauthorized access or malware installation.
6. **Disable Unnecessary Features**:
   - Disable the xp_cmdshell command if not needed.
   - Limit the use of CLR assemblies to trusted code only.

Detection Signature:
Service: MS-SQL
Port: 1433 (default MS-SQL port)
Severity: Critical
Incident: Trigona Ransomware Attacking MS-SQL Servers
Signature name: “MS-SQL publicly accessible”
Internal checks:
   - Setting1: MS-SQL port (1433) should not be exposed on external Internet.
   - Setting2: MS-SQL port (1433) should not listen on the external Internet – Inside VMs.
   - Setting3: MS-SQL server should secure with complex authentication credentials – Inside VMs.
External scanning:
   - Port (1433) open.
   - Weak or simple passwords.

IoCs:
- IPs or domains: hxxp://3x55o3u2b7cjs54eifja5m3ottxntlubhjzt6k6htp5nrocjmsxxh7ad[.]onion/
- MD5 hashes:
  - 1cece45e368656d322b68467ad1b8c02
  - 1e71a0bb69803a2ca902397e08269302
  - 46b639d59fea86c21e5c4b05b3e29617
  - 530967fb3b7d9427552e4ac181a37b9a
  - 5db23a2c723cbceabec8d5e545302dc4
