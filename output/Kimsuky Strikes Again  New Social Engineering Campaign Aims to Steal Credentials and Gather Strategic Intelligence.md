# Kimsuky Strikes Again  New Social Engineering Campaign Aims to Steal Credentials and Gather Strategic Intelligence

Incident: Kimsuky Social Engineering & Credential Theft Campaign

Root cause: Social engineering and phishing tactics, including the use of spoofed URLs and weaponized Office documents

Impact: The specific number of devices or people impacted and financial losses are not detailed in the report. However, the campaign targeted experts in North Korean affairs and stole Google and NK News subscription credentials, which could potentially affect numerous individuals and organizations within the non-government sector focusing on North Korea.

Mitigation: 
1. **User Awareness Training**: Educate users on recognizing phishing attempts, especially those involving spoofed URLs and unsolicited document review requests.
2. **Email Filtering**: Implement advanced email filtering solutions to detect and block phishing emails.
3. **Multi-Factor Authentication (MFA)**: Enforce MFA for accessing sensitive accounts to reduce the risk of credential theft.
4. **URL Filtering**: Use URL filtering to block access to known malicious domains.
5. **Regular Updates and Patching**: Ensure that all systems and applications are regularly updated to mitigate vulnerabilities exploited by malware like ReconShark.
6. **Incident Response Plan**: Develop and maintain an incident response plan to quickly address and mitigate phishing and malware attacks.

Detection Signature:
- **Service**: Web service (phishing websites, spoofed login pages)
- **Port**: 80/443 (commonly used for HTTP/HTTPS traffic)
- **Severity**: Critical
- **Incident**: Kimsuky Social Engineering & Credential Theft
- **Signature name**: “Kimsuky phishing attempt”
- **Internal checks**:
  - Setting1: Monitor email servers for signs of phishing emails and spoofed sender domains.
  - Setting2: Inspect URL clicks in emails for redirections to suspicious or known malicious sites.
  - Setting3: Validate email headers and sender information to detect spoofing attempts.
- **External scanning**:
  - Port (80/443) open: Scan for publicly accessible web services that may be impersonating legitimate sites.
  - Phishing URL detection: Identify domains and URLs used in phishing campaigns to block or monitor them.

IoCs:
- nknews[.]pro
- chad.ocarroll@nknews[.]pro
- membership@nknews[.]pro
- https[://]www.nknews[.]pro
- https[://]www.nknews[.]pro/config[.]php
- https[://]www.nknews[.]pro/ip/register/
- https[://]www.nknews[.]pro/ip/register/login[.]php
- https[://]staradvertiser.store/piece/ca[.]php
- https[://]staradvertiser.store/piece/r[.]php
- 162.0.209[.]27
- 4150B40C00D8AB2E960AA059159149AF3F9ADA09
- 7514FD9E5667FC5085373704FE2EA959258C7595
- 41E39162AE3A6370B1100BE2B35BB09E2CBE9782


