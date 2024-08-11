Source: [https://www.netskope.com/blog/evasive-phishing-campaign-steals-cloud-credentials-using-cloudflare-r2-and-turnstile](https://www.netskope.com/blog/evasive-phishing-campaign-steals-cloud-credentials-using-cloudflare-r2-and-turnstile)

# Evasive Phishing Campaign Steals Cloud Credentials Using Cloudflare R2 and Turnstile

### Incident: Evasive Phishing Campaign Steals Cloud Credentials Using Cloudflare R2 and Turnstile

**Root cause:** Abuse of Cloudflare R2 for hosting phishing pages and Cloudflare Turnstile for CAPTCHA evasion.

**Impact:** The blog does not specify the exact number of people or devices impacted, nor the financial losses incurred. However, the phishing campaign targeted Microsoft login credentials and other cloud app credentials, potentially impacting a large number of users in North America and Asia, especially in the technology, financial services, and banking sectors.

**Mitigation:** 
1. **Secure Object Storage Services:**
   - Configure Cloudflare R2 and similar services to restrict public access to sensitive objects.
   - Utilize access controls and policies to ensure only authorized users can access specific resources.

2. **Enhanced Detection Mechanisms:**
   - Use machine learning and threat intelligence to detect and block phishing attempts.
   - Implement URL filtering policies to identify and block malicious domains and subdomains.

3. **User Education:**
   - Educate users to verify URLs manually and avoid clicking on suspicious links.
   - Promote awareness about phishing techniques and safe browsing practices.

4. **Advanced Security Tools:**
   - Deploy Remote Browser Isolation (RBI) to add an extra layer of security for browsing high-risk categories.
   - Utilize bot detection libraries like Fingerprint BotD to identify and block automated access to sensitive pages.

**Detailed Steps for Mitigation:**
1. **Configure Cloudflare R2:**
   - Restrict public access to buckets and objects unless absolutely necessary.
   - Use access policies to provide granular control over who can see and interact with your data.

2. **Enhance Security Policies:**
   - Implement a comprehensive URL filtering policy to block known phishing and scam sites.
   - Use threat protection policies to inspect all web content and identify unknown phishing pages using signatures, threat intelligence, and machine learning.

3. **Deploy Security Technologies:**
   - Use Remote Browser Isolation (RBI) technology for accessing websites that pose higher risks.
   - Integrate bot detection libraries like Fingerprint BotD to prevent automated tools from accessing the site.

4. **User Training and Awareness:**
   - Conduct regular phishing awareness training sessions.
   - Encourage users to type in URLs directly rather than following links from emails or search engines.

**Detection Signature:**
   - **Service:** Cloudflare R2
   - **Port:** 443 (HTTPS)
   - **Severity:** Critical
   - **Incident:** Phishing Campaign
   - **Signature name:** “Cloudflare R2 Phishing Page”
   - **Internal checks:**
      - Setting1: Public access to Cloudflare R2 buckets should be restricted.
      - Setting2: URL patterns matching `pub-<32_alphanumeric_string>.r2.dev` should be monitored.
      - Setting3: Implement CAPTCHA and bot detection to verify human users.
   - **External scanning:**
      - Open Port 443
      - URLs with the pattern `pub-<32_alphanumeric_string>.r2.dev`
      - Use of Cloudflare Turnstile for CAPTCHA evasion

**IoCs:**
- **URLs:**
  - hxxps://pub-de2f439c6744426586c7612824c1bac2.r2[.]dev/index.html?pu=hxxps://pub-7e0ea6c6ac8c439a840ed31912409dc9.r2[.]dev/index.html
  - hxxp://pub-1f6ee74386dc4dc98c226f8a56f8e8c1.r2[.]dev/office.html
  - hxxp://pub-9f884b1d186548eea381cab00a0f702c.r2[.]dev/emailverification.html
  - hxxp://pub-c6542b65e10b483d9136554aa9cb05e8.r2[.]dev/passwordverification.html
  - hxxp://pub-ca01b8d361b540ce8256226365665de0.r2[.]dev/index2.html
  - hxxp://pub-a0f9c6938a374a2089f6fad1e6e85d1b.r2[.]dev/index2.html
  - hxxp://pub-5431347746b0455bb6f7dbc419a23952.r2[.]dev/oeip.html
  - hxxp://pub-e4b5beda27a847fc9ff07bdb23b36563.r2[.]dev/Dropbox-Business.html
  - hxxp://pub-7e28a526d64340e89715cafd3ffddee3.r2[.]dev/alocate.html
  - hxxp://pub-dc7d3a6ae1254ac4b7b0a0873ef10ed1.r2[.]dev/login.html
  - hxxp://pub-43c8427c1735476fb4e6b1b456757e0a.r2[.]dev/index2.html
  - hxxp://pub-48d3a24bafe348799aa16e3fbd5ead78.r2[.]dev/001zzz.html
  - hxxp://pub-5705d571c53847759ca1e27912b57837.r2[.]dev/authr.html
  - hxxp://pub-b889ecc576cd47b8a7dae94590568f86.r2[.]dev/keep.html
  - hxxp://pub-d0a002d03d4d4468a1a3a4788d44d971.r2[.]dev/apps.html
  - hxxp://pub-1abd9bef283343da8c867e32a56a6050.r2[.]dev/link.html
  - hxxp://pub-4b8c37d5f65746878138f2a1665fc704.r2[.]dev/chi.html
  - hxxp://pub-9b0c4b61dcdb4349b13b6e0f0902a227.r2[.]dev/OWAOutlook.html
  - hxxp://pub-16d24eae069c40dcb335224f9555d849.r2[.]dev/diom.html
  - hxxp://pub-19b440b384f449bc8f30a86a5f3c6049.r2[.]dev/code.html
  - hxxp://pub-2b0fffc523034ccc9ffa6fb26d5462e5.r2[.]dev/setting.html
  - hxxp://pub-50137e365ae14a91ad215a40f880bad1.r2[.]dev/link.html
  - hxxp://pub-6502dddebdc447ed9023277db681dd94.r2[.]dev/vm3.html
  - hxxp://pub-d3ef7b90634c41c2aea65d57a1da514f.r2[.]dev/dashworkers.html
  - hxxp://pub-d1729d90c762460c9395a066038cdaf9.r2[.]dev/backgroundfull.html
  - hxxp://pub-51b3ca6392244b5bb14982b7ddf92f27.r2[.]dev/gaames.html
  - hxxp://pub-c27949832b64423ab5f75bafdf57ba92.r2[.]dev/authe.html
  - hxxp://pub-00268bd240fc441cb2f8557a6961d87d.r2[.]dev/verywebmail.html
  - hxxp://pub-b2955bd5cc5a447cba7f9017e8915538.r2[.]dev/webmail.html
  - hxxp://pub-93bd771473c24746860b98ace628fe91.r2[.]dev/ourteam.html
  - hxxp://pub-28dfeb6275f8415ba3e6b97dfff9ccfc.r2[.]dev/0012823733.html
  - hxxp://pub-9008e63dbf464532acb4ebdafa3bfb86.r2[.]dev/S3M6S5.html
  - hxxp://pub-1b0adb2146a640a0b0ec2645f84b6a9a.r2[.]dev/shaaa.html
  - hxxp://pub-7c6128fbcd6a4ed3a12554f7446ffe16.r2[.]dev/inslo.htm
  - hxxp://pub-4054e7f05a57459e88c44b940037f4fb.r2[.]dev/wnnslo.htm
  - hxxp://pub-1df03b95474e44baa86a0a11a33527d0.r2[.]dev/welcome.html
  - hxxp://pub-5d09e89ff38240f2b559297a9206beea.r2[.]dev/auth.html
  - hxxp://pub-9064d4445dc3440599c3d2cab66301d9.r2[.]dev/verication.html
  - hxxp://pub-a8f7a7bdbbef4c7aa377b495dabb19ff.r2[.]dev/saved.html
  - hxxp://pub-c8dc8d57c6e24653a737a5acb81893ee.r2[.]dev/office365.html
  - hxxp://pub-b0879d66c06e4547a6fe4d002fc9f88e.r2[.]dev/xtrst.html
  - hxxp://pub-c92a4cf1fb774dd79b9c7d32023ab3fa.r2[.]dev/llo.html
  - hxxp://pub-1cd83eaf4a66425d86fb1e8f37610be0.r2[.]dev/index.html
  - hxxp://pub-7e71a0ecd46d4dc0ac25e43cbb595918.r2[.]dev/index.html
  - hxxp://pub-44c085b5c63b4a438aed0cd194363508.r2[.]dev/index2.html
  - hxxp://pub-f488d77bc04a4676ad79ee159fe7d8c5.r2[.]dev/index2.html
  - hxxp://pub-3b2c4103dbe84e8081aa257826f25d54.r2[.]dev/noon.html
  - hxxp://pub-62c47a7a8e0a4ca293b31ee18b2baf43.r2[.]dev/EmailVerification.html
  - hxxp://pub-887adfef303443cc97eee0e66e6d6dbc.r2[.]dev/nick.html
  - hxxp://pub-fbf017af618541b3a76abd75f8dab1b7.r2[.]dev/new.html
  - hxxp://pub-ecff9b63c2c1497bbcbe5d573900b143.r2[.]dev/oml.html
  - hxxp://pub-0e459479bb894ae6a3446ba7783965b0.r2[.]dev/docusign%20encrypted.htm
  - hxxp://pub-3a226c66bcda41e4bbeec4790c71c89c.r2[.]dev/lanx_sl1.htm
  - hxxp://pub-5c8b0c206b484f208b18e2c09e806156.r2[.]dev/HX-ADFS_9.html
  - hxxp://pub-cc4afac7b0304f62946883c1b996ddc3.r2[.]dev/bookingmail.html
  - hxxp://pub-5c0aa65f5f224858a03e429b595c1811.r2[.]dev/dropbox-sign-in.html
  - hxxp://pub-422f33674c4b4fe182123a25dbb97378.r2[.]dev/secu3.html
  - hxxp://pub-b2955bd5cc5a447cba7f9017e8915538.r2[.]dev/micr@s0ft.html
  - hxxp://pub-62d1a4086e2a4406ae5e1a788e7a019b.r2[.]dev/action.html
  - hxxp://pub-dda005a462634fea953ace187610f4c7.r2[.]dev/nexc.html
  - hxxp://pub-54efd4aa11884bfb834031d41082f502.r2[.]dev/res.html
  - hxxp://pub-45f4523b469c4ea18afe1c70ebaabeda.r2[.]dev/index.html
  - hxxp://pub-9eaf08966d54441789d558bfe758e12c.r2[.]dev/Diceyencode.html
  - hxxp://pub-b08c2d9bbe594efba55b1b8d4009a382.r2[.]dev/sam365.html
  - hxxp://pub-99eed73366de4872bbe331bbbfb758cf.r2[.]dev/email.html
