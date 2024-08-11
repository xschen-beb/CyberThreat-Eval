Source: [https://www.zscaler.com/blogs/security-research/janelarat-repurposed-bx-rat-variant-targeting-latam-fintech](https://www.zscaler.com/blogs/security-research/janelarat-repurposed-bx-rat-variant-targeting-latam-fintech)

# JanelaRAT Repurposed BX Rat Variant Targeting LATAM FinTech

Incident: JanelaRAT Campaign Targeting LATAM FinTech

Root cause: Exploitation of DLL side-loading and dynamic DNS services to establish C2 channels.

Impact: Financial and personal information targeting users in LATAM FinTech sector. The specific number of devices or financial losses is not mentioned.

Mitigation: 
- Implement advanced threat detection and response mechanisms.
- Conduct regular audits and monitoring for unusual activity, especially focusing on financial data access.
- Apply patches and updates to legitimate software to prevent exploitation of known vulnerabilities.
- Employ strict network segmentation to minimize the impact of a breach.
- Use multi-factor authentication (MFA) to secure sensitive systems and accounts.

Detailed Steps for mitigation:
1. **Audit and Monitoring:**
   - Regularly audit system and network logs for unusual activities.
   - Implement endpoint detection and response (EDR) solutions to monitor for suspicious behaviors like DLL side-loading or unauthorized registry changes.
   
2. **Software Patching:**
   - Ensure all legitimate software (like VMWare and Microsoft applications) are up-to-date with the latest security patches to prevent exploitation of known vulnerabilities.
   
3. **Network Segmentation:**
   - Segment networks to isolate critical systems and data, reducing the lateral movement of threats.
   - Implement strict access controls and monitor network traffic for anomalies.
   
4. **Multi-Factor Authentication:**
   - Enforce the use of MFA for accessing sensitive systems and data to add an additional layer of security.
   
5. **Employee Training:**
   - Regularly train employees on recognizing phishing attempts and proper handling of ZIP files from unknown sources.
   
6. **Threat Intelligence:**
   - Leverage threat intelligence feeds to stay updated on the latest threats and vulnerabilities relevant to the FinTech sector.

Detection Signature:
    Service: HTTP Server
    Port: 3001
    Severity: Critical
    Incident: JanelaRAT
    Signature name: “JanelaRAT C2 Communication”
    Internal checks:
        - Setting1: Monitor for unusual GET requests to dynamic DNS domains.
        - Setting2: Watch for unauthorized changes to the Windows registry, especially for RunKeys.
        - Setting3: Alert on DLL side-loading activities from legitimate executables.
    External scanning:
        - Port (3001) open
        - Unusual outbound HTTP requests to dynamic DNS domains

IoCs:
- MD5 hashes of malicious VBScripts and DLLs.
- Malicious URLs: `http://zimbawhite[.]is-certified[.]com:3001/clientes/[1-44]`
- Malicious IP addresses: `191.96.224.215`, `192.99.169.240`, `191.96.79.24`, `167.88.168.132`, `102.165.46.28`, `189.89.15.37`
- Domains used for C2 communication: `cnt-blackrock.geekgalaxy.com`, `aigodmoney009.access.ly`, `freelascdmx979.couchpotatofries.org`, etc.

No further IoCs found in the document beyond those listed.


