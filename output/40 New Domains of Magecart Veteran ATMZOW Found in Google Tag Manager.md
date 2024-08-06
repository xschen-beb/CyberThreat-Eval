# 40 New Domains of Magecart Veteran ATMZOW Found in Google Tag Manager

Incident: Magecart Skimming Campaign via Google Tag Manager

Root cause: Misuse of Google Tag Manager to inject malicious scripts.

Impact: 327 websites infected with credit card skimming malware. Potential exposure of sensitive user data, including credit card information, could lead to financial losses for both users and affected businesses. The exact financial impact is difficult to quantify without specific data on the number of affected transactions and the value of the stolen data.

Mitigation: 
1. **Regular Script Audits:**
   - Review all scripts loaded via Google Tag Manager to ensure they are legitimate.
   - Remove any unfamiliar or suspicious scripts immediately.

2. **Enhanced Security Practices:**
   - Implement Content Security Policy (CSP) to restrict the sources from which scripts can be loaded.
   - Use Subresource Integrity (SRI) to ensure that only authorized scripts are executed.

3. **Monitoring and Alerts:**
   - Set up monitoring tools to detect and alert on changes to Google Tag Manager containers.
   - Use web application firewalls (WAF) to detect and block malicious requests.

4. **User Education:**
   - Educate website administrators on the importance of verifying third-party scripts.
   - Provide guidelines on securing Google Tag Manager accounts, such as using strong, unique passwords and enabling two-factor authentication (2FA).

5. **Immediate Response Plan:**
   - Have an incident response plan in place to quickly address any detected compromises.
   - Engage with cybersecurity experts for thorough investigation and cleanup.

Detection Signature:
Service: Google Tag Manager
Port: Not applicable (web service)
Severity: Critical
Incident: Magecart Skimming
Signature name: “Malicious GTM Container”
Internal checks:
- Setting1: Regularly audit Google Tag Manager containers for unauthorized scripts.
- Setting2: Implement CSP and SRI.
- Setting3: Enable 2FA on Google Tag Manager accounts.
External scanning:
- Monitor for external scripts loading from unfamiliar domains.
- Set up alerts for changes in Google Tag Manager configurations.

IoCs: 
- Domains: gtm-statistlc[.]com, gooqle-analytics[.]com, webstatlstics[.]com, and the list of 40 new domains such as cdn.sketchinsightswatch[.]com, cdn.colorpalettemetrics[.]com, etc.
- IP addresses: 31.220.21[.]211, 31.220.21[.]240, 62.72.7[.]89, 62.72.7[.]90

No additional IoCs found.

By following these mitigation steps and continuously monitoring for suspicious activities, businesses can reduce the risk of similar incidents and protect their users' sensitive information.
