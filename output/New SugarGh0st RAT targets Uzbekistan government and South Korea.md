Source: [https://blog.talosintelligence.com/new-sugargh0st-rat/](https://blog.talosintelligence.com/new-sugargh0st-rat/)

# New SugarGh0st RAT targets Uzbekistan government and South Korea

Incident: SugarGh0st RAT Campaign Targeting Uzbekistan Government and South Korea

Root cause: Exploited Windows Shortcut (LNK) file and malicious JavaScript for RAT deployment

Impact: The exact number of devices or individuals impacted and financial losses are not specified.

Mitigation:
1. **Email Security**:
    - Implement robust email filtering to detect and block phishing emails.
    - Educate employees on recognizing and avoiding phishing attempts.
    - Use email security solutions like Cisco Secure Email.

2. **Endpoint Security**:
    - Deploy comprehensive endpoint security solutions like Cisco Secure Endpoint.
    - Regularly update antivirus and anti-malware definitions to detect new threats.
    - Use multi-factor authentication (MFA) to secure access.

3. **Network Security**:
    - Monitor network traffic for unusual patterns that may indicate C2 communication.
    - Use firewalls and intrusion detection/prevention systems (IDS/IPS) to block malicious traffic.
    - Implement secure web gateways like Cisco Umbrella to block access to malicious domains.

4. **System Hardening**:
    - Regularly update and patch all software, especially operating systems and applications.
    - Disable unnecessary features and services to reduce the attack surface.
    - Use application whitelisting to prevent the execution of unauthorized software.

5. **Incident Response**:
    - Establish an incident response plan to quickly identify, contain, and remediate security incidents.
    - Conduct regular security assessments and penetration testing to identify vulnerabilities.

Detailed Steps for Mitigation:
1. **Email Filtering**:
    - Configure email gateways to filter out emails with suspicious attachments (e.g., RAR, LNK files).
    - Implement DKIM, DMARC, and SPF to reduce email spoofing.

2. **Endpoint Protection**:
    - Deploy Cisco Secure Endpoint and ensure it is configured to detect and block SugarGh0st RAT and other malware.
    - Enable real-time threat detection and response capabilities.

3. **Network Monitoring**:
    - Use Cisco Secure Firewall and other network security tools to monitor for and block C2 communication attempts.
    - Regularly review network logs for signs of unauthorized access or data exfiltration.

4. **System Updates and Patches**:
    - Apply security patches and updates as soon as they become available.
    - Use automated patch management tools to ensure timely updates.

5. **User Training**:
    - Conduct regular security awareness training sessions for employees.
    - Provide guidelines on how to identify and report phishing emails.

Detection Signature:
- Service: Windows Script Host (cscript), rundll32.exe
- Port: Not applicable (focus on file execution and network communication patterns)
- Severity: Critical
- Incident: SugarGh0st RAT Infection
- Signature name: “Malicious Windows Shortcut and JavaScript Execution”
- Internal checks:
    - Setting1: Monitor for execution of cscript.exe and rundll32.exe with suspicious parameters.
    - Setting2: Detect creation of new registry keys related to persistence mechanisms.
    - Setting3: Identify the presence of unauthorized DLLs in system directories.
- External scanning:
    - Monitor DNS queries and network traffic to known malicious domains (e.g., login[.]drive-google-com[.]tk).
    - Detect unusual outbound connections to unknown or suspicious IP addresses.

IoCs:
- Domains: login[.]drive-google-com[.]tk, account[.]drive-google-com[.]tk
- File names: ctfmon.bat, MSADOCG.DLL, DPLAY.LIB, libeay32.dll
- Registry Key: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\CTFMON.exe

Additional detection and prevention can be configured using tools like Snort with specific rules (e.g., Snort SIDs 62647) and ClamAV with updated signatures related to SugarGh0st.
