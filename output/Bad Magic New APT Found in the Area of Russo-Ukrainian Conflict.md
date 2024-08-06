# Bad Magic New APT Found in the Area of Russo-Ukrainian Conflict

Incident: CommonMagic and PowerMagic Malware Attack

Root cause: Spear phishing attacks leading to the installation of PowerMagic backdoor and CommonMagic framework.

Impact: Various government, agriculture, and transportation organizations in the Donetsk, Lugansk, and Crimea regions were compromised. The financial and personal impact is not explicitly mentioned in the blog but can be inferred to be significant given the sectors involved and the geopolitical context.

Mitigation: Implement robust email filtering and user education to detect and avoid spear phishing attacks. Use advanced endpoint detection and response (EDR) solutions to identify and mitigate such malware infections. 
**Detailed Steps for mitigation:**
1. **Email Filtering and User Education:**
    - Implement email security solutions that can detect and block phishing attempts.
    - Conduct regular training sessions to educate users about the risks of spear phishing and how to identify suspicious emails.

2. **Endpoint Detection and Response:**
    - Deploy EDR solutions to monitor endpoints for malicious activities and potential compromises.
    - Ensure regular updating and patching of all systems to close known vulnerabilities.

3. **Network Security:**
    - Use network segmentation to limit the spread of malware within the organization.
    - Implement intrusion detection systems (IDS) and intrusion prevention systems (IPS) to detect and block malicious network activities.

4. **Access Management:**
    - Enforce the principle of least privilege to ensure users have only the access necessary to perform their duties.
    - Implement multi-factor authentication (MFA) to add an extra layer of security.

5. **Incident Response Plan:**
    - Develop and regularly update an incident response plan to quickly address security breaches.
    - Conduct regular drills to ensure the response team is prepared to handle real incidents.

Detection Signature:
   Service: Windows Installer (msiexec.exe)
   Port: N/A (as it involves file execution and malware download)
   Severity: Critical
   Incident: CommonMagic and PowerMagic Malware Attack
   Signature name: “PowerMagic MSI Execution”
   Internal checks:
       - Setting1: Monitor for unexpected executions of msiexec.exe with remote URLs – In endpoint security solutions.
       - Setting2: Check for the presence of suspicious LNK files with double extensions – In file monitoring systems.
       - Setting3: Look for the creation of unusual scheduled tasks like WindowsActiveXTaskTrigger – In system monitoring tools.
   External scanning:
       - Monitor network traffic for connections to known malicious IPs and domains listed in IoCs.
       - Check for outbound connections to OneDrive and Dropbox used in an unusual manner.

IoCs:
- IP: 185.166.217[.]184
- Domains: webservice-srv[.]online, webservice-srv1[.]online
- Hashes:
  - Lure archives: 
    - 0a95a985e6be0918fdb4bfabf0847b5a
    - ecb7af5771f4fe36a3065dc4d5516d84
    - 765f45198cb8039079a28289eab761c5
    - ebaf3c6818bfc619ca2876abd6979f6d
    - 1032986517836a8b1f87db954722a33f
    - 1de44e8da621cdeb62825d367693c75e
  - PowerMagic installer: fee3db5db8817e82b1af4cedafd2f346
  - PowerMagic dropper: bec44b3194c78f6e858b1768c071c5db
  - PowerMagic loader: 8c2f5e7432f1e6ad22002991772d589b
  - PowerMagic backdoor: 1fe3a2502e330432f3cf37ca7acbffac
  - CommonMagic loader: ce8d77af445e3a7c7e56a6ea53af8c0d
  - CommonMagic cryptography module: 9e19fe5c3cf3e81f347dd78cf3c2e0c2
  - CommonMagic network communication module: 7c0e5627fd25c40374bc22035d3fadd8
