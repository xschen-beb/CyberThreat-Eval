# New Horabot Campaign Targets the Americas

Incident: Horabot Campaign Targeting the Americas

Root cause: Misconfigured Amazon Web Services (AWS) Elastic Compute Cloud (EC2) instance and vulnerable PowerShell scripting.

Impact: Multiple organizations across various business verticals affected, predominantly targeting users in Mexico and other Spanish-speaking countries in the Americas. Financial losses and the number of impacted devices/people are not specified in the provided document.

Mitigation: 
1. **Secure AWS EC2 Instance:**
   - Ensure EC2 instances are not publicly accessible unless absolutely necessary.
   - Implement strong authentication methods (e.g., multi-factor authentication) for accessing AWS instances.
   - Regularly audit and update security groups and access control lists to minimize exposure.

2. **PowerShell Security:**
   - Disable PowerShell scripting for non-administrative users.
   - Implement PowerShell script block logging and transcription to monitor for suspicious activities.
   - Use Constrained Language Mode for PowerShell to limit the capabilities of scripts.

3. **Email and Spam Protection:**
   - Implement advanced email filtering solutions to detect and block phishing attempts.
   - Educate users on recognizing phishing emails and safe email practices.
   - Use email authentication mechanisms like DKIM, SPF, and DMARC to prevent email spoofing.

4. **Endpoint Protection:**
   - Deploy and maintain endpoint detection and response (EDR) solutions to identify and mitigate malware infections.
   - Regularly update antivirus and anti-malware software to detect the latest threats.

5. **Network Security:**
   - Use intrusion detection/prevention systems (IDS/IPS) to monitor network traffic for suspicious activities.
   - Implement network segmentation to limit the spread of malware within the organization.

Detection Signature:
- Service: Amazon EC2 (AWS)
- Port: Various (depends on the service configuration)
- Severity: Critical
- Incident: Horabot Campaign
- Signature name: “AWS EC2 Publicly Accessible”
  - Internal checks:
    - Setting1: Ensure AWS EC2 instances are not publicly accessible unless necessary.
    - Setting2: Implement VPC security groups and network ACLs to limit access.
    - Setting3: Use AWS IAM roles and policies to enforce least privilege access.
  - External scanning:
    - Check for publicly accessible EC2 instances using tools like AWS Trusted Advisor.
    - Monitor for unauthorized access attempts and unusual activities in AWS CloudTrail logs.

IoCs:
IP addresses:
- 185[.]45[.]195[.]226
- 216[.]238[.]70[.]224
- 139[.]177[.]193[.]74

Domains:
- tributaria[.]website
- m9b4s2[.]site
- wiqp[.]xyz
- ckws[.]info
- amarte[.]store

SSL Certificates:
- 03b6b83943ec043082a8614186921afa306b
- 03eeab4d2874f31ee662ea7f602b73b05633

URLs:
- hxxp[://]216[.]238[.]70[.]224/20/t/e/m.zip
- hxxp[://]tributaria[.]website/esp/12/151222/up/up
- hxxps[://]facturacionmarzo[.]cloud/e/archivos[.]pdf[.]html
