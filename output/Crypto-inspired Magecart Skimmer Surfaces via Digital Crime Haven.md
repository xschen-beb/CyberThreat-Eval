# Crypto-inspired Magecart Skimmer Surfaces via Digital Crime Haven

### Incident: Crypto-inspired Magecart skimmer surfaces via digital crime haven

**Root cause:** Compromised e-commerce sites via Mr.SNIFFA skimmer framework and misconfigured hosting on DDoS-Guard infrastructure.

**Impact:** The blog does not provide a specific number of records or financial losses. However, given the nature of the incident, it could potentially impact thousands of e-commerce customers, leading to significant financial losses per individual affected by stolen credit card data.

**Mitigation:**
1. **Secure Web Hosting:**
   - Ensure e-commerce websites are hosted on reputable providers with stringent security measures.
   - Avoid using hosting services known for supporting malicious activities.
2. **Implement Web Application Firewalls (WAF):**
   - Use WAF to detect and block malicious traffic targeting web applications.
3. **Regular Security Audits:**
   - Conduct regular security audits and vulnerability assessments on all web applications and supporting infrastructure.
4. **Code Reviews:**
   - Regularly review and update application code to identify and fix vulnerabilities.
5. **Secure JavaScript:**
   - Implement Content Security Policy (CSP) to limit the sources from which scripts can be loaded.
6. **Monitor for Skimmers:**
   - Use security tools to monitor for the presence of skimmers on websites.
7. **User Awareness:**
   - Educate users to recognize signs of fraudulent payment forms and report suspicious activities.

**Detection Signature:**
- **Service:** Web Hosting
- **Port:** 80/443
- **Severity:** Critical
- **Incident:** Mr.SNIFFA skimmer on e-commerce sites
- **Signature name:** “Mr.SNIFFA skimmer detected”
    - **Internal checks:**
        - Setting1: Regularly scan and audit web application code for skimmer scripts.
        - Setting2: Configure alerting mechanisms for unauthorized changes to JavaScript and CSS files.
        - Setting3: Implement strict access controls and logging for all web server activities.
    - **External scanning:**
        - Scan for unusual obfuscation techniques in JavaScript and CSS files.
        - Monitor for unauthorized external links and scripts loaded on the site.

**IoCs:**
- **Domains:**
  - hxxps://saylor2xbtc[.]com/vqK4Pq
  - hxxps://elon2xmusk[.]com/jquery[.]min[.]js
  - hxxps://2xdepp[.]com/stylesheet[.]css
  - 3houzz[.]com
- **IP Addresses:**
  - 185[.]178[.]208[.]174
  - 185[.]178[.]208[.]181
  - 185[.]178[.]208[.]190
  - 185[.]149[.]120[.]19
  - 185[.]149[.]120[.]47
  - 185[.]149[.]120[.]67
  - 185[.]149[.]120[.]77
  - 185[.]149[.]120[.]89
  - 185[.]149[.]120[.]95
  - 185[.]149[.]120[.]107
  - 185[.]149[.]120[.]9
  - 185[.]149[.]120[.]123
  - 185[.]149[.]120[.]133
  - 185[.]149[.]120[.]61
  - 185[.]236[.]228[.]114

By implementing these mitigation steps and detection signatures, you can significantly reduce the risk of such skimmer attacks on your e-commerce platforms.
