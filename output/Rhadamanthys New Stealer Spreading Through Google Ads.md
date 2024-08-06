# Rhadamanthys New Stealer Spreading Through Google Ads

Incident: Rhadamanthys Stealer Spread Through Google Ads

Root cause: Phishing websites and spam email campaigns

Impact: The exact number of records or financial losses is not provided. However, the incident involves multiple users who were tricked into downloading malware, potentially compromising sensitive personal and financial information.

Mitigation: 
1. Educate users on identifying phishing emails and suspicious websites.
2. Implement email filtering solutions to detect and block spam emails.
3. Use URL filtering to block access to known malicious websites.
4. Enforce multi-factor authentication (MFA) to add an extra layer of security.
5. Keep software and systems updated with the latest security patches.
6. Use reputable antivirus and endpoint protection solutions.
7. Monitor network traffic for unusual activities and potential data exfiltration.

Detailed Steps for Mitigation:
1. **User Education**:
   - Conduct regular security awareness training.
   - Provide examples of phishing emails and explain how to verify the authenticity of emails and links.

2. **Email Filtering**:
   - Deploy an advanced email filtering solution to detect and block malicious attachments and links.
   - Enable features like sandboxing to safely analyze email attachments before they reach users.

3. **URL Filtering**:
   - Implement web filtering solutions to block access to known malicious domains and URLs.
   - Regularly update the list of blocked URLs based on threat intelligence feeds.

4. **Multi-Factor Authentication (MFA)**:
   - Enforce MFA for all user accounts, especially for accessing sensitive systems and data.
   - Use authentication apps or hardware tokens for MFA instead of SMS-based methods.

5. **Software Updates**:
   - Enable automatic updates for all software and operating systems.
   - Regularly review and apply security patches to close vulnerabilities.

6. **Antivirus and Endpoint Protection**:
   - Install and maintain reputable antivirus software on all endpoints.
   - Use endpoint detection and response (EDR) solutions to monitor and respond to threats.

7. **Network Monitoring**:
   - Monitor network traffic for unusual patterns that may indicate data exfiltration or command and control (C2) communications.
   - Use intrusion detection/prevention systems (IDS/IPS) to detect and block malicious activities.

Detection Signature:
   Service: Web Server
   Port: 80/443 (HTTP/HTTPS)
   Severity: Critical
   Incident: Rhadamanthys Stealer Spread Through Google Ads
   Signature name: “Phishing Website Detected”
   Internal checks:
      - Setting1: Identify and block known phishing domains – In firewall/proxy settings.
      - Setting2: Monitor DNS queries for known malicious domains – Inside network monitoring tools.
      - Setting3: Implement HTTPS filtering to inspect encrypted traffic – Inside network security appliances.
   External scanning:
      - URLs associated with phishing websites.
      - Presence of malware executables on the web server.

IoCs:
   - a31f222fc283227f5e7988d1ad9c0aecd66d58bb7b4d8518ae23e110308dbf91
   - 7bdbd180c081fa63ca94f9c22c457376
   - 9f1f11a708d393e0a4109ae189bc64f1f3e312653dcf317a2bd406f18ffcc507
   - 2915b3f8b703eb744fc54c81f4a9c67f
   - c67b03c0a91eaefffd2f2c79b5c26a2648b8d3c19a22cadf35453455ff08ead0
   - CVE-2024-21887
   - CVE-2023-46805
   - CVE-2017-11882
   - CVE-2024-21893
   - CVE-2021-44228
   - bluestacks-install[.]com
   - zoomus-install[.]com
   - install-zoom[.]com
   - install-anydesk[.]com
   - install-anydeslk[.]com
   - zoom-meetings-install[.]com
   - zoom-meetings-download[.]com
   - anydleslk-download[.]com
   - zoomvideo-install[.]com
   - zoom-video-install[.]com
   - istaller-zoom[.]com
   - noteepad.hasankahrimanoglu[.]com[.]tr
