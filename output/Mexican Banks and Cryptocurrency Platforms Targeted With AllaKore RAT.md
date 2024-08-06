# Mexican Banks and Cryptocurrency Platforms Targeted With AllaKore RAT

Incident: Mexican Banks and Cryptocurrency Platforms Targeted With AllaKore RAT

Root cause: Spear-phishing and drive-by downloads delivering a modified remote access tool (RAT)

Impact: The campaign has targeted large Mexican companies with gross revenues over $100M USD across various industries including Retail, Agriculture, Public Sector, Manufacturing, Transportation, Commercial Services, Capital Goods, and Banking. The exact number of devices and individuals impacted is not provided, but the financial losses could be substantial given the nature of the attack targets.

Mitigation: Implement multi-layered security measures to protect against spear-phishing and drive-by downloads. This includes:

1. **Email Filtering and Security**:
    - Implement advanced email filtering solutions to detect and block spear-phishing emails.
    - Use DMARC, DKIM, and SPF protocols to authenticate email senders.

2. **Endpoint Security**:
    - Deploy endpoint detection and response (EDR) solutions to monitor and respond to malicious activities.
    - Ensure all endpoints have up-to-date antivirus and anti-malware software.

3. **Network Security**:
    - Use intrusion detection and prevention systems (IDPS) to monitor network traffic for suspicious activities.
    - Segment networks to limit the spread of malware.
    - Implement strict access controls and network segmentation.

4. **User Training and Awareness**:
    - Conduct regular security awareness training for employees to recognize and report phishing attempts.
    - Simulate phishing attacks to test and improve employee vigilance.

5. **Patch Management**:
    - Regularly update and patch all software and systems to protect against known vulnerabilities.

6. **Multi-Factor Authentication (MFA)**:
    - Implement MFA for all critical systems and services to add an additional layer of security.

Detection Signature:
- **Service**: .NET downloader, customized AllaKore RAT
- **Port**: Not specified, but typically HTTP/HTTPS (80/443) for C2 communication
- **Severity**: Critical
- **Incident**: Mexican Banks and Cryptocurrency Platforms Targeted With AllaKore RAT
- **Signature name**: “AllaKore RAT infection”
- **Internal checks**:
    - Setting1: Monitor for known .NET downloader hashes and behaviors.
    - Setting2: Check for unusual PowerShell script execution on endpoints.
    - Setting3: Monitor for unauthorized remote access attempts via RAT.
- **External scanning**:
    - Monitor for C2 communication with known malicious domains and IPs.
    - Scan for unauthorized outbound connections to IPs used by the threat actor.

IoCs:
- **Hashes**:
    - 21b7319ae748c43e413993ad57e8d08c
    - 942865d0c76b71a075b21525bd32a1ceca830071e5c61123664bd332c7a8de2a
    - e5447d258c5167db494e6f2a297a9be8
    - bf26025974c4cbbea1f6150a889ac60f66cfd7d758ce3761604694b0ceaa338d
    - 2c84d115a74d2e9d00a14f19eb7f8129
    - 2843582FE32E015479717DA8BF27F0919B246A39495C6D6E00AC7ECA8B1D789C
    - aa11bedc627f4ba588d444b977880ade
    - 6d516a96d6aa39dd9fc2d745ea39658c52ab56d62ef7a56276e2e050d916e19f
    - and many more listed in the document.

- **Domains**:
    - flapawer[.]com
    - chaucheneguer[.]com
    - hhplaytom[.]com
    - zulabra[.]com
    - uperrunplay[.]com
    - uplayground[.]online
    - and many more listed in the document.

- **IPs**:
    - 192.119.99[.]234
    - 192.119.99[.]235
    - 192.119.99[.]236
    - 192.119.99[.]237
    - 192.119.99[.]238
    - 23.236.143[.]214
    - 23.254.138[.]211
    - 23.254.202[.]85
    - 23.254.136[.]60

Detailed steps for mitigation should be tailored to the specific environment and include regular audits, monitoring, and updates to security policies and procedures.

No further IoCs found beyond those listed in the document.
