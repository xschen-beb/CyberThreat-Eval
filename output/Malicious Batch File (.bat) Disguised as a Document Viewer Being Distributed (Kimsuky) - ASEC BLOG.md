# Malicious Batch File (.bat) Disguised as a Document Viewer Being Distributed (Kimsuky) - ASEC BLOG

Incident: Malicious Batch File (*.bat) Disguised as a Document Viewer Distributed by Kimsuky

Root cause: Distribution of malicious batch files (*.bat) disguised as document viewers via email.

Impact: The specific number of devices and people impacted is not provided. Financial losses are not detailed either. The primary impact includes unauthorized access to systems, execution of malicious scripts, and potential data exfiltration.

Mitigation: Implement email filtering and attachment scanning. Educate users on identifying phishing emails. Regularly update anti-malware definitions and conduct routine security audits.

Detailed Steps for Mitigation:
1. **Email Filtering and Scanning:**
   - Implement advanced email filtering solutions to detect and quarantine suspicious attachments.
   - Use sandboxing techniques to analyze the behavior of email attachments before they reach end-users.

2. **User Education:**
   - Conduct regular training sessions to educate users on identifying phishing emails and the dangers of opening attachments from unknown sources.
   - Provide examples and guidelines on verifying the legitimacy of email senders.

3. **Anti-Malware Updates:**
   - Ensure all anti-malware solutions are regularly updated with the latest definitions and patches.
   - Configure anti-malware solutions to perform real-time scanning of all files and attachments.

4. **Security Audits:**
   - Perform routine security audits to identify and remediate vulnerabilities in the network and systems.
   - Implement a robust incident response plan to quickly address any detected threats.

Detection Signature:
   Service: Email Gateway
   Port: 25 (SMTP)
   Severity: Critical
   Incident: Malicious Batch File (*.bat) Disguised as a Document Viewer
   Signature name: “Malicious Batch File Email Distribution”
   
   Internal checks:
   - Setting1: Scan all incoming email attachments for batch files (*.bat). – Email Gateway
   - Setting2: Quarantine emails with suspicious batch file attachments for further analysis. – Email Gateway
   - Setting3: Alert security teams upon detection of malicious batch file attachments. – Email Gateway

   External scanning:
   - Check for known malicious URLs used to distribute batch files.
   - Monitor network traffic for connections to suspicious domains.

IoCs:
MD5:
- 00119ed01689e76cb7f33646693ecd6a
- 7d79901b01075e29d8505e72d225ff52
- 8536d838dcdd026c57187ec2c3aec0f6
- a7ac7d100184078c2aa5645552794c19

URLs:
- hxxps://drive.google.com/file/d/1e41uC2ZTYvTc3CvS6wIKox22AGdP4nFB/view?usp=sharing
- hxxps://drive.google.com/file/d/1tI4J95-7HDGES8e6oHR-wu0cXD8wHPUc/view?usp=sharing
- hxxps://docs.google.com/document/d/1NJfvSpdku2PW3gwg0dnoELrlVp3CEGB4mtNIFE4bOVE/edit?usp=sharing
- hxxps://docs.google.com/document/d/1C3h0agp3E6Z4a9z-YxnMTgP3Fd9y8n2C/edit?rtpof=true&sd=true
- hxxps://drive.google.com/file/d/1rCws6IDhJvynpM3TOSv3IKGWNKXI5uH9/view?usp=sharing
- hxxp://joongang[.]site/pprb/sec/ca.php?na=dot_kasp.gif
- hxxp://joongang[.]site/pprb/sec/ca.php?na=reg0.gif
- hxxp://joongang[.]site/pprb/sec/ca.php?na=sh_ava.gif
- hxxps://joongang[.]site/pprb/sec/ca.php?na=sh_vb.gif
- hxxps://joongang[.]site/pprb/sec/ca.php?na=vbs.gif
- hxxps://joongang[.]site/pprb/sec/d.php?na=battmp
- hxxps://joongang[.]site/pprb/sec/t1.hta
- hxxps://joongang[.]site/pprb/sec/r.php
- http[:]//joongang[.]site/doc/
- http[:]//joongang[.]site/docx/
- http[:]//joongang[.]site/pprb/sec/
- http[:]//namsouth[.]com/gopprb/OpOpO/
- http[:]//staradvertiser[.]store/signal/

No additional IoCs found in the document.
