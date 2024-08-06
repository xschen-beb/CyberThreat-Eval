# Qakbot Being Distributed in Korea Through Email Hijacking

Incident: Qakbot Being Distributed in Korea Through Email Hijacking

Root cause: Malicious PDF files attached to hijacked emails

Impact: The impact details such as the number of devices, people impacted, and financial losses are not specified in the blog.

Mitigation: 
1. **Email Security Measures**:
   - Implement advanced email filtering solutions to detect and block malicious attachments and phishing emails.
   - Use email authentication protocols such as SPF, DKIM, and DMARC to prevent email spoofing and hijacking.
   
2. **User Training and Awareness**:
   - Conduct regular security awareness training for employees to recognize and avoid phishing attempts.
   - Encourage users to verify the authenticity of unexpected email attachments, especially from unknown sources.

3. **Endpoint Protection**:
   - Ensure all endpoints are equipped with up-to-date antivirus and anti-malware solutions.
   - Use advanced threat detection technologies that can identify and block malicious scripts and files.

4. **Network Security**:
   - Monitor network traffic for unusual activities that could indicate malware communication with external servers.
   - Implement intrusion detection and prevention systems (IDPS) to detect and respond to malicious activities on the network.

5. **Regular Updates and Patching**:
   - Keep all software, including operating systems and applications, updated to the latest versions to mitigate vulnerabilities exploited by malware.

Detection Signature:
   Service: Email (SMTP)
   Port: 25/587
   Severity: Critical
   Incident: Qakbot Email Hijacking
   Signature name: “Malicious PDF attachment in hijacked email”    
   Internal checks:
       - Setting1: Monitor for emails with PDF attachments containing suspicious content – In email server
       - Setting2: Identify emails with obfuscated script content in attachments – In email server
       - Setting3: Check for emails with abnormal reply patterns, especially those that seem irrelevant to the original email – In email server
   External scanning:
       - Unusual email traffic patterns
       - Presence of known malicious URLs or hash values in email attachments

IoCs:
- MD5: 
    - 19c1526182fe5ed0f1abfafc98d84df9
    - b57532c33d7fead3105e9312cb544e11
    - c9ab1cd04e796fd7f084a1dd2d40cc2d

- URLs:
    - http[:]//milleniuninformatica[.]com[.]br/Le9/jGjSkvEqmXp
    - https[:]//alzheimersdigest[.]net/ZKpva/55C63K
    - https[:]//antoinettegabriel[.]com/YuUE/RQwyJWR2jjc
    - https[:]//choicefaz[.]com[.]br/w1W2/4gPNeUm0J
    - https[:]//farmfutures[.]in/tlUtBc/IYj0K1

Additional IOCs are available on AhnLab TIP.
