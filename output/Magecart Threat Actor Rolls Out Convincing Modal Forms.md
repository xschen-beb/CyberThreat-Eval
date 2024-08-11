Source: [https://www.malwarebytes.com/blog/threat-intelligence/2023/04/kritec-art](https://www.malwarebytes.com/blog/threat-intelligence/2023/04/kritec-art)

# Magecart Threat Actor Rolls Out Convincing Modal Forms

Incident: Magecart Modal Form Skimmer

Root cause: Injection of malicious JavaScript into PrestaShop CMS

Impact: Potentially thousands of users' credit card information stolen. The exact number of devices or people impacted and financial losses are not specified in the report.

Mitigation: Secure the PrestaShop CMS and JavaScript inclusions.
- **Detailed Steps for mitigation:**
  1. **Update PrestaShop CMS**: Ensure that all software, including the CMS, plugins, and themes, are up-to-date with the latest security patches.
  2. **Regular Security Audits**: Conduct regular security audits and code reviews of the website to identify and remove any unauthorized modifications.
  3. **Content Security Policy (CSP)**: Implement a robust CSP to restrict the sources from which scripts can be loaded.
  4. **Web Application Firewall (WAF)**: Deploy a WAF to detect and block malicious activities, including script injections.
  5. **Authentication and Access Controls**: Strengthen authentication mechanisms and limit access to the website’s backend to authorized personnel only.
  6. **Monitoring and Logging**: Continuously monitor and log activities on the website to detect any unusual behavior or unauthorized changes.
  7. **User Education**: Educate users on recognizing phishing attempts and the importance of verifying the legitimacy of payment pages.

Detection Signature:
  - Service: PrestaShop CMS
  - Port: 80/443 (HTTP/HTTPS)
  - Severity: Critical
  - Incident: Magecart Modal Form Skimmer
  - Signature name: "Magecart modal form skimmer"
  - Internal checks:
    - Setting1: Verify that no unauthorized JavaScript is included in the website files – In platform
    - Setting2: Ensure that all third-party scripts are loaded from trusted sources – Inside VMs
    - Setting3: Regularly audit and review JavaScript files and inclusions in the CMS – Inside VMs
  - External scanning:
    - Check for unauthorized or unexpected JavaScript inclusions
    - Verify the legitimacy of payment forms and modal pop-ups

IoCs:
- **Domain names**:
  - genlytec[.]us
  - shumtech[.]shop
  - zapolmob[.]sbs
  - daichetmob[.]sbs
  - interytec[.]shop
  - pyatiticdigt[.]shop
  - stacstocuh[.]quest
- **IP addresses**:
  - 195.242.110[.]172
  - 195.242.110[.]83
  - 195.242.111[.]146
  - 45.88.3[.]201
  - 45.88.3[.]63
