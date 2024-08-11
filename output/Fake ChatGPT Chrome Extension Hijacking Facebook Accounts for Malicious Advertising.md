Source: [https://labs.guard.io/fakegpt-new-variant-of-fake-chatgpt-chrome-extension-stealing-facebook-ad-accounts-with-4c9996a8f282](https://labs.guard.io/fakegpt-new-variant-of-fake-chatgpt-chrome-extension-stealing-facebook-ad-accounts-with-4c9996a8f282)

# Fake ChatGPT Chrome Extension Hijacking Facebook Accounts for Malicious Advertising

**Incident:** FakeGPT Chrome Extension Hijacking Facebook Ad Accounts

**Root cause:** Malicious Chrome extension exploiting browser and Facebook API vulnerabilities.

**Impact:** Thousands of Facebook ad accounts hijacked, including high-profile business accounts. The exact number of devices and individuals impacted is not specified, but thousands of daily installs are noted. Financial losses are incurred due to unauthorized ad spend and potential loss of business reputation.

**Mitigation:** 
1. **Immediate Actions:**
   - Remove the malicious extension from the Chrome Web Store (already done as of March 9, 2023).
   - Notify affected users and advise them to remove the extension from their browsers.

2. **For Users:**
   - Remove the "Quick access to Chat GPT" extension from your browser.
   - Change Facebook account passwords and enable two-factor authentication (2FA).
   - Review and remove any unauthorized Facebook applications with admin permissions.
   - Monitor Facebook ad accounts for any unauthorized activity.

3. **For Facebook and Google:**
   - Enhance review processes for Chrome extensions and Facebook applications to detect and prevent similar malicious activities.
   - Implement stricter API call monitoring and validation mechanisms to detect abnormal behavior.
   - Educate users about the risks of installing extensions and apps from unverified sources.

4. **For Security Teams:**
   - Conduct regular audits of browser extensions and Facebook applications used within the organization.
   - Implement endpoint protection that can detect and block malicious browser extensions.
   - Use security monitoring tools to detect unusual API calls or unauthorized ad spending.

**Detailed Steps for Mitigation:**
   - **For Users:**
     1. Go to Chrome settings and navigate to Extensions.
     2. Locate the “Quick access to Chat GPT” extension and click Remove.
     3. Change Facebook account passwords.
     4. Enable two-factor authentication (2FA) on Facebook.
     5. Review Facebook app permissions and remove any suspicious apps.

   - **For Facebook/Google:**
     1. Review extension and application submission policies to include additional security checks.
     2. Implement automated tools to scan for malicious behavior in extensions and applications.
     3. Increase user awareness through notifications and educational campaigns.

   - **For Organizations:**
     1. Deploy endpoint protection solutions to monitor and block malicious browser extensions.
     2. Conduct regular security training for employees on recognizing phishing and malicious software.
     3. Implement policies to restrict installation of unapproved extensions and applications.

**Detection Signature:**

- **Service:** Chrome Browser Extension
- **Port:** N/A
- **Severity:** Critical
- **Incident:** FakeGPT Chrome Extension Hijacking Facebook Ad Accounts
- **Signature name:** “Malicious Chrome Extension”
- **Internal checks:**
  - Ensure only approved extensions are installed – In platform
  - Regular audit of installed extensions – Inside User Devices
  - Monitor for unauthorized Facebook Graph API calls – Inside Network
- **External scanning:**
  - Detect and block known malicious extension IDs (e.g. kgnddmccicfibljeodejjmekeiilkfhk)
  - Monitor network traffic for connections to known C2 domains (e.g., api2[.]openai-service[.]workers[.]dev)

**IoCs:**
- **Original Facebook Post and Pages:**
  - https://www[.]facebook[.]com/chatgpt.google/videos/719341863011965/
  - https://www[.]facebook[.]com/chatgpt.google/
- **Extension IDs:**
  - kgnddmccicfibljeodejjmekeiilkfhk (latest)
  - coegmjlpjblmfpcnleenkhggdebdcphk
  - oboofekcjiojcpcehaldjhjfhcienopme
- **C2 Servers:**
  - api2[.]openai-service[.]workers[.]dev
  - df3233[.]workers[.]dev
  - xfks[.]workers[.]dev
- **C2 API Calls:**
  - api2[.]openai-service[.]workers[.]dev/api/add-data-account
  - api2[.]openai-service[.]workers[.]dev/api/add-business-manager
  - api2[.]openai-service[.]workers[.]dev/api/add-pages
  - api2[.]openai-service[.]workers[.]dev/api/add-ads-manager
  - api2[.]openai-service[.]workers[.]dev/api/update-data-login-account
- **Facebook app IDs:**
  - 1348564698517390 (portal)
  - 1174099472704185 (Messenger Kids for iOS - active)
- **Facebook Graph API calls in use:**
  - graph[.]facebook[.]com/v12.0/me/businesses?
  - graph[.]facebook[.]com/v12.0/me/business/adaccount/limits?
  - graph[.]facebook[.]com/v13.0/me/facebook_pages?
  - graph[.]facebook[.]com/v12.0/me/adaccounts?
  - graph[.]facebook[.]com/v12.0/v14.0/act_{account_id}?
  - graph[.]facebook[.]com/ads/adbuilder
  - graph[.]facebook[.]com/me/?fields=id,name,birthday,email&access_token=
  - graph[.]facebook[.]com/v2.6/device/login_status?
  - graph[.]facebook[.]com/auth/create_session_for_app?
  - graph[.]facebook[.]com/v2.6/device/login?
  - graph[.]facebook[.]com/graphql
  - www[.]facebook[.]com/ajax/bootloader-endpoint/?modules=AdsLWIDescribeCustomersContainer.react
  - www[.]facebook[.]com/ajax/oauth/device.php
  - www[.]facebook[.]com/v2.0/dialog/oauth/confirm/
  - www[.]facebook[.]com/dialog/oauth
  - www[.]facebook[.]com/oauth/device/authorize
  - www[.]facebook[.]com/api/graphql/
- **Other:**
  - https://lumtest[.]com/myip.json
