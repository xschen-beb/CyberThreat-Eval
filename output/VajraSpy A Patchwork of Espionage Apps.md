Source: [https://www.welivesecurity.com/en/eset-research/vajraspy-patchwork-espionage-apps/](https://www.welivesecurity.com/en/eset-research/vajraspy-patchwork-espionage-apps/)

# VajraSpy A Patchwork of Espionage Apps

### Incident: VajraSpy Espionage Campaign

**Root cause:** Malicious Android applications distributed through Google Play and VirusTotal.

**Impact:** 1,400 installs on Google Play, 148 compromised devices geolocated in Pakistan and India. Financial losses are not specified in the document.

**Mitigation:** 
1. **Application Review and Vetting:** Ensure thorough vetting and security analysis of applications before they are allowed on Google Play.
2. **User Education:** Educate users about the dangers of downloading applications through unsolicited links and the importance of verifying app sources.
3. **Regular Audits:** Conduct regular audits of applications available on Google Play to detect and remove potentially harmful applications promptly.
4. **Permission Management:** Encourage users to be cautious about granting permissions to apps, especially those that request access to sensitive data.
5. **Firebase Security:** Ensure that Firebase servers used by applications are securely configured to prevent unauthorized access.

**Detailed Steps for Mitigation:**
1. **Implement Strict Vetting Processes:** 
    - Develop a stringent app review process that includes static and dynamic analysis to identify malicious behavior.
    - Use machine learning models trained on known malware signatures to assist in the detection of harmful apps.

2. **User Education Campaigns:**
    - Launch awareness campaigns to educate users about the risks of downloading apps from untrusted sources and clicking on links in unsolicited messages.
    - Provide clear guidelines on how to verify the authenticity of apps on Google Play.

3. **Conduct Regular Audits:**
    - Regularly scan and audit apps on Google Play using advanced security tools to detect and remove any malicious applications.
    - Partner with cybersecurity firms to get updated threat intelligence and incorporate it into the audit process.

4. **Permission Management:**
    - Encourage users to review and manage app permissions regularly.
    - Implement features that alert users when an app requests excessive permissions that are not aligned with its core functionality.

5. **Firebase Security Configuration:**
    - Ensure Firebase databases are configured with appropriate security rules to prevent unauthorized access.
    - Regularly update and patch Firebase servers to close any security vulnerabilities.

**Detection Signature:**
- **Service:** Firebase
- **Port:** N/A (Firebase uses HTTPS over port 443)
- **Severity:** Critical
- **Incident:** VajraSpy Espionage Campaign
- **Signature name:** “Firebase malicious activity detection”
- **Internal checks:**
    - Setting1: Ensure Firebase databases are configured with access control rules. – In platform
    - Setting2: Monitor Firebase logs for unusual activity or data access patterns. – Inside VMs
    - Setting3: Regularly review and update Firebase security rules. – Inside VMs
- **External scanning:**
    - Monitor for known malicious Firebase URLs or domains.
    - Scan for Firebase instances with publicly accessible databases.

**IoCs:**
- **Files:**
    - BAF6583C54FC680AA6F71F3B694E71657A7A99D0: com.hello.chat
    - 846B83B7324DFE2B98264BAFAC24F15FD83C4115: com.chit.chat
    - 5CFB6CF074FF729E544A65F2BCFE50814E4E1BD8: com.meeete.org
    - 1B61DC3C2D2C222F92B84242F6FCB917D4BC5A61: com.nidus.no
    - BCD639806A143BD52F0C3892FA58050E0EEEF401: com.rafaqat.news
    - 137BA80E443610D9D733C160CCDB9870F3792FB8: com.tik.talk
    - 5F860D5201F9330291F25501505EBAB18F55F8DA: com.wave.chat
    - 3B27A62D77C5B82E7E6902632DA3A3E5EF98E743: com.priv.talk
    - 44E8F9D0CD935D0411B85409E146ACD10C80BF09: com.glow.glow
    - 94DC9311B53C5D9CC5C40CD943C83B71BD75B18A: com.letsm.chat
    - E0D73C035966C02DF7BCE66E6CE24E016607E62E: com.nionio.org
    - 235897BCB9C14EB159E4E74DE2BC952B3AD5B63A: com.qqc.chat
    - 8AB01840972223B314BF3C9D9ED3389B420F717F: com.yoho.talk
- **Network:**
    - **IP:** 34.120.160[.]131, 35.186.236[.]207, 160.20.147[.]67
    - **Domain:** hello-chat-c47ad-default-rtdb.firebaseio[.]com, chit-chat-e9053-default-rtdb.firebaseio[.]com, meetme-abc03-default-rtdb.firebaseio[.]com, chatapp-6b96e-default-rtdb.firebaseio[.]com, tiktalk-2fc98-default-rtdb.firebaseio[.]com, wave-chat-e52fe-default-rtdb.firebaseio[.]com, privchat-6cc58-default-rtdb.firebaseio[.]com, glowchat-33103-default-rtdb.firebaseio[.]com, letschat-5d5e3-default-rtdb.firebaseio[.]com, quick-chat-1d242-default-rtdb.firebaseio[.]com, yooho-c3345-default-rtdb.firebaseio[.]com, rafaqat-d131f-default-rtdb.asia-southeast1.firebasedatabase[.]app

**No IoCs found** for hashes or additional IP addresses not listed above.
