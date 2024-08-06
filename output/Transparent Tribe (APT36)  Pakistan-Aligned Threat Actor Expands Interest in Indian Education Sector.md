# Transparent Tribe (APT36)  Pakistan-Aligned Threat Actor Expands Interest in Indian Education Sector

Incident: Transparent Tribe (APT36) Expands Interest in Indian Education Sector

Root cause: Phishing emails with malicious Office documents staging Crimson RAT

Impact: Potentially hundreds of devices and individuals impacted, primarily within the Indian education sector. The financial losses could include costs related to malware removal, system restoration, and potential data breaches. **Detailed financial loss estimation is not provided in the source document.**

Mitigation: 
1. **Email Filtering and Awareness**:
   - Implement robust email filtering solutions to block phishing emails.
   - Conduct regular security awareness training for staff and students on recognizing phishing emails and malicious attachments.

2. **Macro Security**:
   - Disable macros in Microsoft Office by default and only allow them for trusted documents.
   - Use group policies to manage macro settings in an enterprise environment.

3. **File Scanning and Sandboxing**:
   - Utilize advanced malware detection solutions that can sandbox and scan Office documents before they are opened.
   - Regularly update antivirus and anti-malware definitions to detect and block the latest threats.

4. **Network Segmentation**:
   - Segment the network to limit the spread of malware and to isolate critical systems from endpoints prone to phishing attacks.

5. **Endpoint Protection**:
   - Deploy endpoint detection and response (EDR) solutions to identify and mitigate suspicious activities like unauthorized registry changes and unusual process executions.

6. **Patch Management**:
   - Ensure all systems are up to date with the latest security patches from software vendors.

Detection Signature:
```
Service: Microsoft Office
Port: N/A (The attack vector is primarily via email)
Severity: Critical
Incident: Transparent Tribe (APT36) targeting Indian education sector
Signature name: “Malicious Office Documents with Crimson RAT”
Internal checks:
    - Setting1: Microsoft Office macro settings should be disabled by default – In platform
    - Setting2: Monitor for unusual registry changes under \SOFTWARE\Microsoft\Windows\CurrentVersion\Run – Inside VMs
    - Setting3: Use EDR solutions to detect and block the execution of known malicious Office macros and OLE embedded content. – Inside VMs
External scanning:
    - Scan email attachments for known IoCs related to Crimson RAT
    - Monitor network traffic for connections to known C2 domains (e.g., richa-sharma.ddns[.]net)
```

IoCs:
```
SHA1 Hashes:
- 738d31ceca78ffd053403d3b2bc15847682899a0 (Malicious document)
- 9ed39c6a3faab057e6c962f0b2aaab07728c5555 (Malicious document)
- af6608755e2708335dc80961a9e634f870aecf3c (Malicious document)
- e000596ad65b2427d7af3313e5748c2e7f37fba7 (Malicious document)
- fd46411b315beb36926877e4b021721fcd111d7a (Malicious document)
- 516db7998e3bf46858352697c1f103ef456f2e8e (Crimson RAT)
- 842f55579db786e46b20f7a7053861170e1c0c5e (Crimson RAT)
- 87e0ea08713a746d53bef7fb04632bfcd6717fa9 (Crimson RAT)
- 911226d78918b303df5110704a8c8bb599bcd403 (Crimson RAT)
- 973cb3afc7eb47801ff5d2487d2734ada6b4056f (Crimson RAT)

Domains:
- richa-sharma.ddns[.]net (C2 server)
- cloud-drive[.]store (Malware hosting location)
- drive-phone[.]online (Malware hosting location)
- s1.fileditch[.]ch (Malware hosting location)
```

