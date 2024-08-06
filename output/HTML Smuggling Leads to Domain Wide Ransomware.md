# HTML Smuggling Leads to Domain Wide Ransomware

Incident: HTML Smuggling Leads to Domain Wide Ransomware

Root cause: HTML Smuggling via email delivering password-protected ZIP files containing ISO files that deployed IcedID malware.

Impact: The report does not specify the exact number of devices or individuals impacted, nor does it provide specific financial losses. However, the deployment of Nokoyawa ransomware resulted in widespread encryption of systems across the domain, likely causing significant operational disruption and potential financial loss due to downtime and recovery costs.

Mitigation: 
- Implement email security solutions to detect and block malicious attachments and links.
- Educate users on the risks of opening unsolicited email attachments or links.
- Disable the execution of macros from files obtained via email.
- Utilize endpoint protection solutions capable of detecting and blocking malicious payloads like IcedID.
- Monitor for and block the use of HTML smuggling techniques.
- Regularly update and patch systems to prevent exploitation of known vulnerabilities.
- Restrict administrative privileges to only necessary users.
- Implement network segmentation to limit lateral movement.
- Employ robust backup solutions and regularly test recovery procedures.
- Deploy multi-factor authentication (MFA) for all remote access.

Detailed Steps for mitigation:
1. **Email Security:**
   - Implement advanced email filtering solutions such as Secure Email Gateways (SEGs).
   - Enable attachment sandboxing to detect and block potentially harmful files.
   - Configure email systems to block or quarantine emails with executable content inside archive files.

2. **User Education:**
   - Conduct regular phishing awareness training for employees.
   - Use phishing simulation tools to test and improve user awareness.

3. **Macro Policies:**
   - Configure Group Policy to disable macros in Office files received via email.
   - Use Office 365 Advanced Threat Protection to block macro-enabled files from unknown or untrusted sources.

4. **Endpoint Security:**
   - Deploy Endpoint Detection and Response (EDR) solutions to detect and respond to malicious activity.
   - Regularly update antivirus and anti-malware software to the latest versions.

5. **Network Monitoring:**
   - Implement Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS).
   - Monitor network traffic for unusual patterns indicative of HTML smuggling or C2 communications.

6. **Administrative Privileges:**
   - Enforce the principle of least privilege (PoLP) for user accounts.
   - Regularly review and audit administrative accounts and their privileges.

7. **Network Segmentation:**
   - Segment critical infrastructure from end-user workstations.
   - Use firewalls to control and limit internal network traffic.

8. **Backups:**
   - Perform regular backups of critical data.
   - Store backups in an isolated and secure location.
   - Regularly test backup restoration processes.

9. **Multi-Factor Authentication:**
   - Require MFA for all remote access to the network and critical systems.
   - Use MFA solutions that support push notifications or hardware tokens.

Detection Signature:
- **Service:** HTTP/HTTPS
- **Port:** 80/443
- **Severity:** Critical
- **Incident:** HTML Smuggling Leads to Domain Wide Ransomware
- **Signature name:** “HTML Smuggling Detected”
- **Internal checks:**
  - Setting1: Monitor for unusual email attachments and links. – In Email Gateway
  - Setting2: Detect and alert on base64 encoded blobs in HTML files. – In Web Proxy/Firewall
  - Setting3: Identify and block execution of unauthorized LNK files. – In Endpoint Security
- **External scanning:**
  - Monitor for outbound connections to known IcedID and Cobalt Strike C2 servers.
  - Detect and alert on the use of HTML smuggling techniques.

IoCs:
- IPs:
  - 78.128.113[.]154
  - 5.8.18[.]242
  - 5.255.103[.]16
  - 159.89.12[.]125

- Domains:
  - trentonkaizerfak[.]com
  - questdisar[.]com
  - pikchayola[.]pics

- File Hashes:
  - 1.dll: 9740f2b8aeacc180d32fc79c46333178
  - 8c11812d-65fd-48ee-b650-296122a21067.zip: 4f4231ca9e12aafac48a121121c6f940
  - adfind.bat: ebf6f4683d8392add3ef32de1edf29c4
  - k.exe: 40c9dc2897b6b348da88b23deb0d3952
  - netscan.exe: 16ef238bc49b230b9f17c5eadb7ca100
  - p.bat: 385d21c0438f5b21920aa9eb894740d2
  - psexec.exe: c590a84b8c72cf18f35ae166f815c9df
  - pimpliest_kufic.png: 49524219dbd2418e3afb4e49e5f1805e
  - redacted-invoice-10.31.22.html: c8bdc984a651fa2e4f1df7df1118178b
  - templates544.png: 14f37c8690dda318f9e9f63196169510

- SSL Certificates:
  - Subject: O=Internet Widgits Pty Ltd, ST=Some-State, C=AU, CN=localhost
  - Issuer: O=Internet Widgits Pty Ltd, ST=Some-State, C=AU, CN=localhost
  - Not Before: 2022-10-09T09:36:33Z
  - Not After: 2023-10-09T09:36:33Z

  - Subject: CN=, OU=, O=, L=, ST=, C=
  - Issuer: CN=, OU=, O=, L=, ST=, C=
  - Not Before: 2015-05-20T18:26:24Z
  - Not After: 2025-05-17T18:26:24Z
