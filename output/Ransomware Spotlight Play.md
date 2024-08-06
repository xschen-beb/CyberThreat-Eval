# Ransomware Spotlight Play

Incident: Play Ransomware Attacks

Root cause: Exploitation of multiple vulnerabilities including ProxyNotShell, OWASSRF, and Microsoft Exchange Server RCE, along with the use of valid but compromised accounts and exposed RDP servers.

Impact: 110 organizations compromised, predominantly small-sized businesses across various industries such as IT, transportation, and construction. The financial losses are not explicitly mentioned, but the disruption and potential costs of data recovery and system restoration can be significant.

Mitigation: 
1. **Audit and Inventory:**
   - Inventory all assets and data.
   - Identify authorized and unauthorized devices and software.
   - Review event and incident logs regularly.

2. **Configure and Monitor:**
   - Manage hardware and software configurations.
   - Grant admin privileges and access sparingly.
   - Monitor network ports, protocols, and services.
   - Activate security configurations on network infrastructure devices.
   - Establish a software allowlist for legitimate applications.

3. **Patch and Update:**
   - Regularly assess vulnerabilities.
   - Apply patches or virtual patches for operating systems and applications promptly.
   - Update all software to their latest versions.

4. **Protect and Recover:**
   - Implement robust data protection, backup, and recovery measures.
   - Enable multifactor authentication (MFA).
   - Employ sandbox analysis to block malicious emails.
   - Deploy advanced security solutions across all system layers (email, endpoint, web, network).

5. **Detection:**
   - Use advanced detection technologies powered by AI and machine learning.
   - Detect early signs of an attack, such as the presence of suspicious tools.

6. **Train and Test:**
   - Regularly train employees on security skills.
   - Conduct red-team exercises and penetration tests.

Detection Signature:
   - **Service:** Microsoft Exchange Server, FortiOS SSL VPN
   - **Port:** 443 (common for HTTPS and SSL VPN)
   - **Severity:** Critical
   - **Incident:** Play Ransomware
   - **Signature name:** “Play ransomware initial access”
   
   Internal checks:
   - Setting1: Ensure Microsoft Exchange Server and FortiOS SSL VPN are patched for known vulnerabilities.
   - Setting2: RDP should not be exposed to the Internet.
   - Setting3: Enforce strong passwords and MFA on all accounts.

   External scanning:
   - Port 443 open.
   - Check for vulnerable Exchange Server and FortiOS configurations.

IoCs: "No IoCs found" in the provided document. However, the article mentions that specific indicators might vary per attack and refers to the Trend Micro Vision One Hunting Query for further details.

By implementing these mitigation steps and monitoring for the detection signature, organizations can significantly reduce the risk of falling victim to Play ransomware and similar threats.
