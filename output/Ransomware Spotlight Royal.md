Source: [https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-royal](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-royal)

# Ransomware Spotlight Royal

**Incident: Royal Ransomware Attacks**

**Root cause: Inadequate defensive measures against callback phishing and exploitation of remote desktop software vulnerabilities.**

**Impact:**
- 764 attack attempts detected across multiple industries.
- 90 organizations successfully infiltrated.
- Ransom demands ranging from $250,000 to $2 million.
- Financial losses can vary significantly depending on the ransom paid or the cost of recovery from the attacks.

**Mitigation:**
1. **Audit and Inventory:**
   - Take an inventory of all assets and data within the organization.
   - Identify and document authorized and unauthorized devices and software.
   - Regularly audit event and incident logs for any suspicious activity.

2. **Configuration and Monitoring:**
   - Manage hardware and software configurations to ensure security policies are enforced.
   - Limit admin privileges and access to employees based on their roles.
   - Monitor network ports, protocols, and services for unusual activity.
   - Enable security configurations on network infrastructure devices such as firewalls and routers.
   - Establish a software allowlist to ensure only legitimate applications are executed.

3. **Patching and Updates:**
   - Conduct regular vulnerability assessments.
   - Apply patches or virtual patching for operating systems and applications promptly.
   - Update all software and applications to their latest versions.

4. **Protection and Recovery:**
   - Implement robust data protection, backup, and recovery measures.
   - Enable multifactor authentication (MFA) for all critical systems.
   - Employ sandbox analysis to block malicious emails and downloads.
   - Deploy security solutions to all layers of the system (email, endpoint, web, network).

5. **Training and Testing:**
   - Regularly train employees on cybersecurity best practices and phishing awareness.
   - Conduct red-team exercises and penetration tests to identify and rectify vulnerabilities.

6. **Advanced Detection:**
   - Use advanced detection technologies powered by AI and machine learning to identify early signs of an attack.
   - Monitor for the presence of suspicious tools and behaviors in the system.

**Detection Signature:**
   - **Service:** Remote Desktop Protocol (RDP), Cobalt Strike, Qakbot.
   - **Port:** Various, commonly used for RDP (3389), HTTP/S (80, 443).
   - **Severity:** Critical
   - **Incident:** Unauthorized remote access and malware deployment.
   - **Signature name:** “Remote Desktop Exploitation”
   
     **Internal checks:**
       - **Setting1:** Ensure RDP ports are not exposed to the external internet unless necessary.
       - **Setting2:** Ensure RDP services are secured with strong passwords and MFA.
       - **Setting3:** Monitor for the installation of unauthorized remote desktop software.

     **External scanning:**
       - Identify open RDP ports (3389) and other relevant ports.
       - Detect the presence of Cobalt Strike and Qakbot communication.

**IoCs:**
- No specific IoCs found in the provided document, but general indicators include unusual network activity, presence of known malicious tools (e.g., PsExec, NetScan, Cobalt Strike), and unauthorized remote desktop connections.

By implementing these mitigation steps and detection measures, organizations can significantly reduce the risk of falling victim to Royal ransomware attacks and enhance their overall cybersecurity posture.
