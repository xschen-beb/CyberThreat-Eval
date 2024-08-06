# Analysis of CLR SqlShell Used to Attack MS-SQL Servers

Incident: MS-SQL Server CLR SqlShell Attack

Root cause: Misconfigured MS-SQL server with weak password policy and publicly accessible ports.

Impact: Potentially thousands of devices impacted, specific financial losses are not detailed.

Mitigation: Implement strong password policies, regularly update and patch MS-SQL servers, restrict public access to MS-SQL server ports, and utilize security programs such as firewalls. 

Detailed Steps for mitigation:
1. **Password Policy**:
    - Implement and enforce a strong password policy with a mix of uppercase, lowercase, numbers, and special characters.
    - Ensure passwords are changed periodically.
    - Avoid using default or easily guessable passwords.

2. **Patch Management**:
    - Regularly update and patch MS-SQL servers to the latest version.
    - Monitor and apply security updates promptly.

3. **Network Security**:
    - Restrict access to MS-SQL server ports (1433) from the public internet.
    - Use firewalls to limit access to MS-SQL servers only to trusted IP addresses.
    - Configure VPNs for remote access to ensure only authenticated users can connect.

4. **Service Configuration**:
    - Disable unnecessary services and features like xp_cmdshell and OLE Automation Procedures unless absolutely required.
    - Ensure CLR integration is only enabled if necessary and monitor its usage.

5. **Monitoring and Detection**:
    - Regularly monitor logs for unusual activities, such as multiple failed login attempts or unfamiliar IP addresses accessing the server.
    - Implement intrusion detection systems (IDS) to alert on suspicious activities.

Detection Signature:
Service: MS-SQL
Port: 1433
Severity: Critical
Incident: MS-SQL Server CLR SqlShell Attack
Signature name: “MS-SQL publicly accessible”
Internal checks:
  - Setting1: MS-SQL port (1433) should not be exposed on external Internet. – In platform
  - Setting2: MS-SQL port (1433) should not listen on the external Internet – Inside VMs
  - Setting3: MS-SQL server should secure with strong authentication credentials. – Inside VMs
External scanning:
  - Port (1433) open
  - MS-SQL brute-force login attempts

IoCs:
- IPs: 
  - 54.36.10.73:1001
  - 88.214.26.9:13785
  - adminserver.online:1001
- URLs:
  - http[:]//c[.]getmoney[.]company/CLRV7/data[.]txt
  - http[:]//c[.]getmoney[.]company/CLRV7/ver[.]txt
- MD5 Hashes:
  - 012e607f99ecc5b108b292d72938456a
  - 130d2b07a1c4cde8f0804df9fa9622d4
  - 15c87480e0405b41f675222ef2bea95a
  - 17606de13187c780ad3bf6caf2d1bd8c
  - 1e92e397d0ad3d8006d99f81d913ffa1

Additional IOCs are available on AhnLab TIP.


