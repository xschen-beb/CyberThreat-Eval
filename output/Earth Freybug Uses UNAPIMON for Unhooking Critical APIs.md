Source: [https://www.trendmicro.com/en_us/research/24/d/earth-freybug.html](https://www.trendmicro.com/en_us/research/24/d/earth-freybug.html)

# Earth Freybug Uses UNAPIMON for Unhooking Critical APIs

Incident: Earth Freybug Uses UNAPIMON for Unhooking Critical APIs

Root cause: Exploitation of legitimate processes and lack of proper process monitoring

Impact: Potential for significant data exfiltration and evasion of security controls. Specific financial losses and number of devices/people impacted are not detailed in the report.

Mitigation: 
1. Frequent password rotation and limiting admin account access.
2. Implement activity logging and regular audits of account activities.
3. Restrict admin privileges and enforce the principle of least privilege.
4. Strengthen endpoint detection and response (EDR) systems to detect API unhooking techniques.
5. Regularly update and patch systems to mitigate vulnerabilities in legitimate applications.

**Detailed Steps for Mitigation:**
1. **Password Management:**
   - Implement a policy for frequent password changes.
   - Use complex passwords and consider multi-factor authentication (MFA) for admin accounts.

2. **Access Control:**
   - Restrict admin privileges to essential personnel only.
   - Regularly review and audit account access rights.
   - Implement role-based access control (RBAC) to enforce the principle of least privilege.

3. **Activity Logging:**
   - Enable comprehensive logging on critical systems and processes.
   - Regularly review logs for unusual or unauthorized activities.

4. **Endpoint Security:**
   - Deploy advanced EDR solutions capable of detecting API unhooking and DLL hijacking.
   - Conduct regular threat hunting exercises to identify potential security gaps.

5. **System Updates and Patch Management:**
   - Ensure all systems and applications are up-to-date with the latest security patches.
   - Regularly scan for and mitigate vulnerabilities in external-facing servers.

Detection Signature:
   Service: Windows Task Scheduler (schtasks.exe)
   Port: Not applicable (local system process)
   Severity: Critical
   Incident: Earth Freybug API Unhooking
   Signature name: "API Unhooking Detection"
   Internal checks:
      - Setting1: Monitor creation of remote scheduled tasks via schtasks.exe.
      - Setting2: Detect and alert on injection of unknown code into legitimate processes like vmtoolsd.exe.
      - Setting3: Ensure critical processes have integrity checks to detect unauthorized modifications.
   External scanning:
      - Not applicable (focus on internal process monitoring)
      
IoCs: 
- Hash: 62ad0407a9cce34afb428dee972292d2aa23c78cbc1a44627cb2e8b945195bc2 (Trojan.Win64.UNAPIMON.ZTLB)
