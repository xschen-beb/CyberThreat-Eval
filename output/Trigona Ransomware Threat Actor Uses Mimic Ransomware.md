# Trigona Ransomware Threat Actor Uses Mimic Ransomware

Incident: Trigona Ransomware Threat Actor Uses Mimic Ransomware

Root cause: Poorly managed and externally exposed MS-SQL servers with simple account credentials

Impact: Thousands of MS-SQL servers potentially compromised, leading to data encryption and theft. Financial losses can vary significantly depending on the affected organization's data sensitivity and the extent of the ransomware spread.

Mitigation: 
1. Enforce strong password policies: Ensure that all MS-SQL servers use complex, unique passwords that are changed regularly.
2. Restrict access: Use firewalls and other security measures to limit access to MS-SQL servers from external networks.
3. Regular updates: Keep MS-SQL server software and all related tools up to date with the latest security patches.
4. Enable multi-factor authentication (MFA): Add an extra layer of security to the authentication process.
5. Monitor and log: Implement comprehensive logging and monitoring to identify suspicious activities early.
6. Disable unnecessary features: Turn off unused services and utilities like BCP if they are not needed.
7. Educate staff: Regularly train IT staff on security best practices and emerging threats.
8. Backup strategy: Maintain regular, secure backups of essential data to minimize the impact of a ransomware attack.

Detection Signature:
Service: MS-SQL Server  
Port: 1433  
Severity: Critical  
Incident: Trigona/Mimic Ransomware  
Signature name: “MS-SQL exposed with weak credentials”  
Internal checks:  
- Setting1: Ensure MS-SQL port (1433) is not exposed to the external Internet unless necessary – In platform  
- Setting2: MS-SQL port (1433) should not listen on the external Internet – Inside VMs  
- Setting3: MS-SQL server should use strong, complex passwords – Inside VMs  
External scanning:  
- Port (1433) open
- Detect weak or default credentials

IoCs: 
- Emails: farusbig@tutanota[.]com, getmydata@list.ru
- URL: hxxp://znuzuy4hkjacew5y2q7mo63hufhzzjtsr2bkjetxqjibk4ctfl7jghyd[.]onion/
- IP: 2.57.149[.]233
- File hashes: 
  - 3e26e778a4d28003686596f988942646
  - 6d44f8f3c1608e5958b40f9c6d7b6718
  - a02157550bc9b491fd03cad394ccdfe7
  - a24bac9071fb6e07e13c52f65a093fce
  - a6e2722cff3abb214dc1437647964c57
