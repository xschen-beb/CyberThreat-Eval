Source: [https://asec.ahnlab.com/en/42554/](https://asec.ahnlab.com/en/42554/)

# Word Documents Disguised as Normal MS Office URLs Being Distributed - ASEC BLOG

Incident: Word Documents Disguised as Normal MS Office URLs Being Distributed

Root cause: Phishing attack utilizing cleverly disguised URLs resembling legitimate Microsoft Office URLs.

Impact: The exact number of records, devices, or people impacted is not specified. Financial losses are also not mentioned.

Mitigation: Educate users to verify the source of document files before opening them. Implement email and web filtering solutions that can detect and block malicious URLs. Regularly update antivirus and anti-malware software to detect the latest threats.

**Detailed Steps for Mitigation:**
1. **User Education and Awareness:**
   - Conduct training sessions for employees on recognizing phishing attacks.
   - Encourage verification of the sender and the legitimacy of attachments before opening them.

2. **Email and Web Filtering:**
   - Implement advanced email filtering solutions to detect and block phishing emails.
   - Use web filtering services to block access to malicious URLs.

3. **Regular Software Updates:**
   - Ensure all systems have updated antivirus and anti-malware software.
   - Regularly update operating systems and applications to patch vulnerabilities.

4. **Endpoint Protection:**
   - Deploy endpoint protection platforms (EPP) that can detect and respond to malware.
   - Use EDR (Endpoint Detection and Response) tools for continuous monitoring and investigation of suspicious activities.

5. **Incident Response Plan:**
   - Develop and maintain an incident response plan to handle security breaches.
   - Conduct regular drills to ensure the plan’s effectiveness and readiness.

Detection Signature:
   Service: HTTP
   Port: 80 (HTTP)
   Severity: Critical
   Incident: Malicious Word Document Distribution
   Signature name: “Disguised Malicious Office URLs”
   Internal checks:
      - Setting1: Monitor outgoing HTTP requests to known malicious domains.
      - Setting2: Implement URL filtering to block access to suspicious domains.
      - Setting3: Scan incoming email attachments for malicious content.
   External scanning:
      - Check for the presence of known malicious URLs in web traffic.
      - Identify and block domains with suspicious patterns.

IoCs:
   - MD5: d698fccf14f670595442155395f42642
   - URLs:
      - http[:]//offices[.]word-template[.]net/
      - http[:]//schemas[.]openxmlformat[.]org/
      - https[:]//ms-office[.]services/
      - https[:]//ms-offices[.]com/
