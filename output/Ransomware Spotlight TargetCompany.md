# Ransomware Spotlight TargetCompany

Incident: TargetCompany Ransomware Attack

Root cause: Vulnerable Microsoft SQL Server and public-facing database servers

Impact: 269 attempted attacks detected, primarily affecting enterprises in the manufacturing, retail, and telecommunications industries across various Asian countries. Financial losses and exact number of devices/people impacted are not given in the provided document.

Mitigation: 
1. **Audit and Inventory**:
    - Take an inventory of assets and data.
    - Identify authorized and unauthorized devices and software.
    - Audit event and incident logs.

2. **Configure and Monitor**:
    - Manage hardware and software configurations.
    - Grant admin privileges and access only when necessary.
    - Monitor network ports, protocols, and services.
    - Activate security configurations on network infrastructure devices like firewalls and routers.
    - Establish a software allowlist to execute only legitimate applications.

3. **Patch and Update**:
    - Conduct regular vulnerability assessments.
    - Perform patching for operating systems and applications.
    - Update software and applications to their latest versions.

4. **Protect and Recover**:
    - Implement data protection, backup, and recovery measures.
    - Enable multifactor authentication (MFA).

5. **Secure and Defend**:
    - Employ sandbox analysis to block malicious emails.
    - Deploy the latest versions of security solutions across email, endpoint, web, and network layers.
    - Discover early signs of an attack, such as the presence of suspicious tools in the system.
    - Use advanced detection technologies powered by AI and machine learning.

6. **Train and Test**:
    - Regularly train and assess employees' security skills.
    - Conduct red-team exercises and penetration tests.

Detection Signature:
- Service: Microsoft SQL Server
- Port: 1433
- Severity: Critical
- Incident: TargetCompany Ransomware
- Signature name: "MS SQL Server Brute-Force Attack"
- Internal checks:
    - Setting1: Ensure SQL Server port (1433) is not exposed to the external Internet.
    - Setting2: SQL Server should not listen on external Internet.
    - Setting3: Enforce strong authentication credentials for SQL Server.
- External scanning:
    - Port (1433) open
    - SQL Server brute-force attempts detected

IoCs:
- IP: 80[.]66[.]75[.]25
- Domains: hxxp://80[.]66[.]75[.]25/pl-Thjct_Rfxmtgam[.]bmp
- Hash: $myuserprofile$\desktop\911.exe SHA1:539c228b6b332f5aa523e5ce358c16647d8bbe57
- Other: Various registry keys and PowerShell scripts as detailed in the provided document.

No additional IoCs found beyond those specified in the document provided.
