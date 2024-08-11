Source: [https://www.microsoft.com/en-us/security/blog/2023/04/07/mercury-and-dev-1084-destructive-attack-on-hybrid-environment/](https://www.microsoft.com/en-us/security/blog/2023/04/07/mercury-and-dev-1084-destructive-attack-on-hybrid-environment/)

# MERCURY and DEV-1084 Destructive attack on hybrid environment

**Incident:** MERCURY and DEV-1084: Destructive attack on hybrid environment

**Root cause:** Exploitation of unpatched vulnerabilities in internet-facing devices and misuse of highly privileged credentials.

**Impact:** Destruction of on-premises and cloud resources, including server farms, virtual machines, storage accounts, and virtual networks. Financial losses could be substantial due to service downtime, data loss, and recovery efforts. The exact number of devices and people impacted is not specified.

**Mitigation:** Implement the following measures to mitigate similar attacks:
1. **Patch Management:**
   - Regularly update and patch all internet-facing devices and applications.
   - Apply security updates for known vulnerabilities like Log4j.

2. **Credential Hygiene:**
   - Implement strong credential hygiene practices.
   - Regularly rotate passwords, especially for highly privileged accounts.
   - Use multi-factor authentication (MFA) for all privileged accounts.

3. **Security Configurations:**
   - Disable unnecessary services and close unused ports.
   - Enable tamper protection to prevent antivirus tampering and misconfiguration.
   - Use Conditional Access policies to enforce compliant devices and trusted IP requirements.

4. **Monitoring and Detection:**
   - Enable continuous access evaluation to revoke access in real-time upon detecting risks.
   - Monitor for unusual activities by privileged accounts.
   - Use advanced threat detection tools like Microsoft 365 Defender and Microsoft Sentinel to identify suspicious activities.

5. **Incident Response Planning:**
   - Develop and regularly update an incident response plan.
   - Conduct regular security assessments and penetration tests.

**Detailed Steps for mitigation:**
1. **Patch Management:**
   - Ensure all systems are up to date with the latest patches and updates.
   - Use automated tools to deploy patches across the environment.

2. **Credential Hygiene:**
   - Implement least privilege access controls.
   - Use privileged access workstations (PAWs) for administrators.
   - Enforce password policies that require complex and unique passwords.

3. **Security Configurations:**
   - Enable tamper protection features in security solutions.
   - Configure Conditional Access policies in Azure AD.
   - Review and adjust firewall rules to minimize exposure of services.

4. **Monitoring and Detection:**
   - Enable and configure alerts in Microsoft 365 Defender and Microsoft Sentinel.
   - Set up advanced hunting queries to detect unusual activities.
   - Regularly review audit logs for suspicious activities.

5. **Incident Response Planning:**
   - Develop a comprehensive incident response plan.
   - Conduct tabletop exercises to test the effectiveness of the response plan.
   - Ensure backups are regularly performed and tested for integrity.

**Detection Signature:**
- **Service:** Apache Tomcat (for Log4j vulnerabilities), Azure AD Connect
- **Port:** 8080 (for Apache Tomcat), 443 (for Azure AD Connect)
- **Severity:** Critical
- **Incident:** Exploitation of unpatched vulnerabilities and misuse of privileged credentials
- **Signature name:** “Log4j vulnerability exploitation” and “Azure AD Connect compromise”
- **Internal checks:**
  - Setting1: Ensure all internet-facing devices are patched against known vulnerabilities.
  - Setting2: Monitor for suspicious activities involving privileged accounts.
  - Setting3: Ensure MFA is enabled for all privileged accounts.
- **External scanning:**
  - Port (8080) open for Apache Tomcat
  - Unpatched Log4j vulnerabilities
  - Suspicious activities involving Azure AD Connect

**IoCs:**
- IP addresses: 146.70.106[.]89, 194.61.121[.]86, 141.95.22[.]153, 193.200[.]16.3, 192.52.166[.]191, 45.56.162[.]111, 104.194.222[.]219, 192.169.6[.]88, 192.52.167[.]209, 46.249.35[.]243, 45.86.230[.]20
- Domains: vatacloud[.]com, pairing[.]rport[.]io, webstore4tech[.]uaenorth.cloudapp.azure[.]com

**No IoCs found:** No additional IoCs found beyond the ones listed above.
