Source: [https://www.menlosecurity.com/blog/evilproxy-phishing-attack-strikes-indeed/](https://www.menlosecurity.com/blog/evilproxy-phishing-attack-strikes-indeed/)

# EvilProxy Phishing Attack Strikes Indeed

Incident: EvilProxy Phishing Attack Strikes Indeed

Root cause: Exploitation of an open redirection vulnerability on the job search platform "indeed.com"

Impact: The blog does not specify the exact number of records leaked or the financial losses incurred. However, it does mention that the campaign targeted C-suite employees and key executives across multiple sectors including Banking and Financial services, Insurance providers, Property Management and Real Estate, and Manufacturing in the United States.

Mitigation:
1. **Educate Users**: Conduct awareness sessions and training programs to help users recognize phishing attempts.
2. **Implement Phishing-Resistant MFA**: Use FIDO-based authentication like Yubikeys to provide strong, phishing-resistant multi-factor authentication.
3. **Verify Target URLs**: Ensure that users verify whether the target URLs are legitimate rather than assuming they are safe.
4. **Session Isolation Solutions**: Deploy solutions like HEAT Shield to protect users from zero-hour phishing attacks in real-time.

**Detailed Steps for mitigation:**
1. **Awareness Training**:
   - Regularly update employees on the latest phishing techniques.
   - Create simulated phishing campaigns to test and improve user awareness.

2. **Phishing-Resistant MFA**:
   - Implement FIDO-based MFA solutions across the organization.
   - Ensure that critical systems and applications enforce the use of these MFA solutions.

3. **URL Verification**:
   - Implement browser extensions or email gateways that can scan and verify URLs in real-time.
   - Educate users about checking the legitimacy of URLs manually, especially those received via email.

4. **Session Isolation**:
   - Deploy browser isolation technologies that can detect and prevent zero-hour phishing attacks.
   - Use AI-based detection models to analyze and block malicious web pages in real-time.
   - Ensure continuous monitoring and updating of the isolation technology to keep up with evolving threats.

Detection Signature:
- Service: Nginx (used to host phishing pages)
- Port: Typically 80 (HTTP) and 443 (HTTPS)
- Severity: Critical
- Incident: EvilProxy Phishing Attack
- Signature name: “EvilProxy Nginx Reverse Proxy”
- Internal checks:
  - Setting1: Nginx server configurations should be monitored for unauthorized changes.
  - Setting2: Ensure Nginx servers do not have open redirection vulnerabilities.
  - Setting3: Use WAF (Web Application Firewall) rules to detect and block malicious redirections.
- External scanning:
  - Scan for open ports (80, 443) on Nginx servers.
  - Check for open redirection in URLs hosted on these servers.

IoCs:
- **Domains**:
  - lmo[.]roxylvfuco[.]com[.]au
  - lmo[.]bartmfil[.]com
  - lmo[.]triperlid[.]com
  - roxylvfuco[.]com[.]au
  - earthscigrovp[.]com[.]au
  - mscr.earthscigrovp[.]com[.]au
  - vfuco.com[.]au
  - catalogsumut[.]com
  - ivonnesart[.]com
  - sheridanwyolibrary[.]org

- **IPs**:
  - 199.204.248.121
  - 193.239.85.29
  - 212.224.107.74
  - 206.189.190.128
  - 116.90.49.27
  - 85.187.128.19
  - 202.139.238.230

No further IoCs found in the document.
