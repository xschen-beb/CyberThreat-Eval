Source: [https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/agent-teslas-new-ride-the-rise-of-a-novel-loader/](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/agent-teslas-new-ride-the-rise-of-a-novel-loader/)

# Agent Teslas New Ride The Rise of a Novel Loader

Incident: Agent Tesla's New Ride: The Rise of a Novel Loader

Root cause: Phishing email with a malicious loader attachment

Impact: The exact number of impacted devices and financial losses are not specified in the blog. However, given the nature of Agent Tesla, which is capable of data theft and credential exfiltration, the impact could be significant if deployed widely.

Mitigation: 
- Implement email filtering to block phishing emails.
- Use advanced threat detection systems to identify and block malicious attachments.
- Enforce strict access controls and application whitelisting to prevent unauthorized execution of unknown executables.
- Regularly update anti-malware signatures and employ behavioral analysis to detect and block polymorphic malware.
- Educate employees about phishing threats and safe email practices.

**Detailed Steps for mitigation:**
1. **Email Filtering**:
    - Deploy email security solutions (e.g., Secure Email Gateway) to scan and filter out phishing emails.
    - Implement DMARC, DKIM, and SPF to authenticate and secure email communications.

2. **Advanced Threat Detection**:
    - Use Endpoint Detection and Response (EDR) solutions to monitor and analyze endpoint activities.
    - Deploy network-based intrusion detection/prevention systems (IDS/IPS) to identify and block malicious payloads and C2 communications.

3. **Access Controls and Whitelisting**:
    - Enforce the principle of least privilege (PoLP) for user accounts and applications.
    - Implement application whitelisting to only allow pre-approved programs to execute.

4. **Regular Updates**:
    - Ensure all anti-malware and security software are up-to-date with the latest signatures and patches.
    - Regularly update the operating systems and applications to protect against known vulnerabilities.

5. **Employee Education**:
    - Conduct regular training sessions to educate employees about identifying phishing emails and safe email practices.
    - Simulate phishing attacks to assess and improve employee awareness and response.

Detection Signature:
Service: HTTP Proxy  
Port: 80  
Severity: Critical  
Incident: Agent Tesla Loader Deployment  
Signature name: “Agent Tesla Loader Email”    
Internal checks:
- Setting1: Ensure email gateway rules are in place to block suspicious attachments. – Email Security  
- Setting2: Monitor for execution of unknown .NET executables. – Endpoint Security  
- Setting3: Check for unauthorized AMSI bypass attempts. – Endpoint Security  

External scanning:
- Monitor for suspicious user-agent strings indicative of the loader's HTTP requests.
- Scan for traffic to known malicious URLs and IPs associated with Agent Tesla C2 infrastructure.

IoCs:
- Loader (Variant 1):
  - MD5: b69f65b999db695b27910689b7ed5cf0
  - SHA256: ab9cd59d789e6c7841b9d28689743e700d492b5fae1606f184889cc7e6acadcc
- Loader (Variant 2):
  - MD5: 38d6ebb40197248bc9149adeec8bd0e7
  - SHA256: a02388b5c352f13334f30244e9eedac3384bc2bf475d8bc667b0ce497769cc6a
- Packed Agent Tesla:
  - MD5: 2bd452c46a861e59ac151a749047863f, 63f802e47b78ec3d52fe6b403bad823f
  - SHA256: e3cb3a5608f9a8baf9c1da86324474739d6c33f8369cc3bb2fd8c79e919089c4, f74e1a37a218dc6fcfabeb1435537f709d742505505a11e4757fc7417e5eb962
- Unpacked Agent Tesla:
  - MD5: 3637aa1332b312fe77cc40b3f7adb8dc, 37b38ae2d99dd5beb08377d6cbd1bccd
  - SHA256: 3a1fe17d53a198f64051a449c388f54002e57995b529635758248dc4da7f5080, a3645f81079b19ff60386cb244696ea56f5418ae556fba4fd0afe77cfcb29211
- SMTP Exfiltration:
  - Sender email: merve@temikan[.]com[.]tr
  - Receiver email: frevillon[.]acsitec@proton[.]me
- Download URLs:
  - hxxps[://]artemis-rat[.]com/get/65f0e7dd5b705f429be16c65
  - hxxps[://]artemis-rat[.]com/get/65eb0afe3a680a9851f23712
- User-Agent:
  - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, killer Gecko) Chrome/58.0.3029.110 Safari/537.3
- List of Proxy Servers:
  - hxxps[://]github[.]com/TheSpeedX/PROXY-List/blob/master/hxxp[.]txt


