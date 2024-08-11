Source: [https://blog.google/threat-analysis-group/zimbra-0-day-used-to-steal-email-data-from-government-organizations/](https://blog.google/threat-analysis-group/zimbra-0-day-used-to-steal-email-data-from-government-organizations/)

# Zimbra 0-Day Used to Steal Email Data From Government Organizations

**Incident:** Zimbra 0-day Exploit Targeting International Government Organizations

**Root cause:** Reflected Cross-Site Scripting (XSS) vulnerability in Zimbra Collaboration (CVE-2023-37580)

**Impact:** At least four different campaigns targeting government organizations in Greece, Moldova, Tunisia, Vietnam, and Pakistan. The specific number of devices, people impacted, and financial losses are not detailed in the report.

**Mitigation:** 
1. **Immediate Actions:**
   - Apply the official patch for CVE-2023-37580 released on July 25, 2023.
   - Escalate the contents of the `st` parameter to prevent script execution.

2. **Long-term Actions:**
   - Conduct regular code audits, especially for XSS vulnerabilities.
   - Monitor open-source repositories for early detection of security fixes and vulnerabilities.
   - Implement security measures to safeguard against XSS attacks, such as Content Security Policy (CSP) and input validation.
   - Educate users on phishing awareness to avoid clicking on suspicious links.

**Detection Signature:**

- **Service:** Zimbra Collaboration
- **Port:** 443 (HTTPS)
- **Severity:** Critical
- **Incident:** Zimbra 0-day Exploit
- **Signature name:** "Zimbra CVE-2023-37580 XSS Vulnerability"
- **Internal checks:**
  - Setting1: Ensure Zimbra Collaboration is updated to the latest version.
  - Setting2: Verify that the `st` parameter is properly escaped.
  - Setting3: Implement XSS protection measures in Zimbra configuration.
- **External scanning:**
  - Check for the presence of vulnerable Zimbra versions.
  - Scan for exploit patterns in URLs, especially those containing scripts.
  - Monitor traffic for suspicious activity involving known exploit domains.

**IoCs:**
1. https://obsorth.opwtjnpoc[.]ml/pQyMSCXWyBWJpIos.js
2. https://applicationdevsoc[.]com/zimbraMalwareDefender/zimbraDefender.js
3. https://applicationdevsoc[.]com/tndgt/auth.js
4. ntcpk[.]org
