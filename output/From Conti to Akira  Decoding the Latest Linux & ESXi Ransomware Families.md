# From Conti to Akira  Decoding the Latest Linux & ESXi Ransomware Families

Incident: Conti to Akira Ransomware Attacks

Root cause: Exploitation of vulnerabilities in ESXi, weak credentials, and lack of multi-factor authentication (MFA)

Impact: The report does not specify the exact number of records leaked or financial losses. However, the impact includes compromised critical business operations and services due to the encryption of virtual machines in various industries such as education, finance, manufacturing, real estate, and medical sectors.

Mitigation: 
1. **Secure ESXi Servers**:
   - Ensure all ESXi servers are updated to the latest version to patch known vulnerabilities.
   - Implement strong, unique passwords for all accounts and disable default accounts if possible.
   - Enforce the use of multi-factor authentication (MFA) for accessing ESXi and related management services.
2. **Network Segmentation**:
   - Segment the network to limit access to ESXi management interfaces from untrusted networks.
   - Use firewall rules to restrict access to management ports to only trusted IP addresses.
3. **Regular Backups**:
   - Implement a robust backup strategy that includes regular backups of critical virtual machines and data.
   - Ensure backups are stored offline or in a separate network segment to prevent them from being encrypted by ransomware.
4. **Monitoring and Detection**:
   - Deploy intrusion detection systems (IDS) and intrusion prevention systems (IPS) to monitor for unusual activities and potential exploits.
   - Regularly review logs for signs of unauthorized access or exploitation attempts.
5. **Employee Training**:
   - Educate employees about phishing attacks and safe online practices to avoid falling victim to social engineering tactics.
   - Conduct regular security awareness training sessions.

Detection Signature:
   - Service: VMware ESXi
   - Port: 902, 443 (commonly used for ESXi management)
   - Severity: Critical
   - Incident: Conti to Akira Ransomware Attacks
   - Signature name: “ESXi Exploitation Attempt”
   - Internal checks:
     - Setting1: Ensure ESXi management ports (902, 443) are not exposed to the external Internet.
     - Setting2: Verify that ESXi management interfaces are only accessible from trusted IP addresses.
     - Setting3: Ensure ESXi servers are secured with strong, unique passwords and MFA.
   - External scanning:
     - Port (902, 443) open
     - No MFA enabled

IoCs:
- MONTI Locker File Hashes:
  - a0c9dd3f3e3d0e2cd5d1da06b3aac019cdbc74ef
  - f1c0054bc76e8753d4331a881cdf9156dd8b812a
- Akira File Hash:
  - 9180ea8ba0cdfe0a769089977ed8396a68761b40
- Trigona File Hashes:
  - 0144800f67ef22f25f710d181954869f1d11d471
  - 55f47e767dd5fdd1a54a0b777b00ffb473acd329
  - 62e4537a0a56de7d4020829d6463aa0b28843022
- Abyss Locker File Hash:
  - 40ceb71d12954a5e986737831b70ac669e8b439e
