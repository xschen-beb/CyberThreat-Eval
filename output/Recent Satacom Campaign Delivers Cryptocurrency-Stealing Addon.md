Source: [https://securelist.com/satacom-delivers-cryptocurrency-stealing-browser-extension/109807/](https://securelist.com/satacom-delivers-cryptocurrency-stealing-browser-extension/109807/)

# Recent Satacom Campaign Delivers Cryptocurrency-Stealing Addon

**Incident: Satacom Campaign Delivers Cryptocurrency-Stealing Addon**

**Root Cause:** Exploitation of legitimate advertising plugins to distribute malware.

**Impact:** The campaign targets individual users globally, with significant infections reported in Brazil, Algeria, Turkey, Vietnam, Indonesia, India, Egypt, and Mexico. Financial losses would vary depending on the amount of cryptocurrency stolen from each victim's account.

**Mitigation:** 
1. **Ad Network Monitoring:** Enhance monitoring of ad networks to detect and block malicious ads.
2. **Browser Security:** 
    - Ensure browser extensions are only installed from official stores.
    - Regularly review installed browser extensions.
3. **Antivirus and Anti-Malware Software:** 
    - Use updated antivirus and anti-malware solutions to detect and block malicious files.
4. **User Education:** 
    - Educate users about the risks of downloading and installing software from untrusted sources.
    - Encourage the use of strong, unique passwords and enable multi-factor authentication on cryptocurrency accounts.

**Detailed Steps for Mitigation:**
1. **Ad Network Monitoring:** 
    - Collaborate with ad networks to improve their filtering mechanisms to detect and block malicious ads.
    - Regularly audit and review ad networks for compliance with security standards.
2. **Browser Security Enhancements:**
    - Implement policies that restrict the installation of browser extensions to those verified and available in official extension stores.
    - Schedule periodic reviews of installed browser extensions within the organization to ensure no unauthorized or malicious extensions are present.
3. **Antivirus and Anti-Malware Software Deployment:**
    - Deploy comprehensive antivirus and anti-malware solutions across all devices.
    - Ensure regular updates and scans are performed to detect and remove any malicious software.
4. **User Education Programs:**
    - Conduct regular training sessions on cybersecurity best practices.
    - Distribute educational materials on the dangers of downloading software from untrusted sources and how to recognize phishing attempts.
    - Promote the use of multi-factor authentication and password managers to secure cryptocurrency accounts.

**Detection Signature:**
- **Service:** Chromium-based browsers (Google Chrome, Brave, Opera)
- **Port:** Not applicable (browser-based threat)
- **Severity:** Critical
- **Incident:** Satacom Campaign Delivers Cryptocurrency-Stealing Addon
- **Signature name:** “Malicious browser extension installation”
- **Internal checks:**
    - **Setting1:** Ensure browser extension policies restrict installations to verified sources. – In platform
    - **Setting2:** Regularly review and audit installed browser extensions across all endpoints. – Inside VMs
    - **Setting3:** Implement browser security configurations to warn or block installations from untrusted sources. – Inside VMs
- **External scanning:**
    - **Check for the presence of malicious extensions:** Scan for known malicious extensions installed in browsers.
    - **Monitor for suspicious browser activities:** Alert on unusual browser behaviors indicative of malware activity, such as excessive redirection or unauthorized changes to browser settings.

**IoCs:**
- **Satacom files:**
    - 0ac34b67e634e49b0f75cf2be388f244
    - 1aa7ad7efb1b48a28c6ccf7b496c9cfd
    - 199017082159b23decdf63b22e07a7a1
- **Satacom DNS:**
    - dns-beast[.]com
    - don-dns[.]com
    - die-dns[.]com
- **Satacom C2:**
    - hit-mee[.]com
    - noname-domain[.]com
    - don-die[.]com
    - old-big[.]com
- **Hosted PS scripts:**
    - tchk-1[.]com
- **Malicious extension ZIP:**
    - a7f17ed79777f28bf9c9cebaa01c8d70
- **Malicious extension CC:**
    - you-rabbit[.]com
    - web-lox[.]com
- **Hosted Satacom installer ZIP files:**
    - ht-specialize[.]xyz
    - ht-input[.]cfd
    - ht-queen[.]cfd
    - ht-dilemma[.]xyz
    - ht-input[.]cfd
    - io-strength[.]cfd
    - fbs-university[.]xyz
    - io-previous[.]xyz
    - io-band[.]cfd
    - io-strength[.]cfd
    - io-band[.]cfd
    - can-nothing[.]cfd
    - scope-chat[.]xyz
    - stroke-chat[.]click
    - icl-surprise[.]xyz
    - new-high[.]click
    - shrimp-clock[.]click
    - oo-knowledge[.]xyz
    - oo-station[.]xyz
    - oo-blue[.]click
    - oo-strategy[.]xyz
    - oo-clearly[.]click
    - economy-h[.]xyz
    - medical-h[.]click
    - hospital-h[.]xyz
    - church-h[.]click
    - close-h[.]xyz
    - thousand-h[.]click
    - risk-h[.]xyz
    - current-h[.]click
    - fire-h[.]xyz
    - future-h[.]click
    - moment-are[.]xyz
    - himself-are[.]click
    - air-are[.]xyz
    - teacher-are[.]click
    - force-are[.]xyz
    - enough-are[.]xyz
    - education-are[.]click
    - across-are[.]xyz
    - although-are[.]click
    - punishment-chat[.]click
    - rjjy-easily[.]xyz
    - guy-seventh[.]cfd
- **Redirectors to Satacom installer:**
    - back-may[.]com
    - post-make[.]com
    - filesend[.]live
    - soft-kind[.]com
    - ee-softs[.]com
    - big-loads[.]com
    - el-softs[.]com
    - softs-labs[.]com
    - soft-make[.]com
    - soft-end[.]com
    - soon-soft[.]com
    - tip-want[.]click
    - get-loads[.]com
    - new-loads[.]com
    - file-send[.]live
    - filetosend-upload[.]net
    - file-send[.]cc

**Note:** Ensure to cross-check these IoCs with your threat intelligence and monitoring tools to detect and mitigate any potential infections.
