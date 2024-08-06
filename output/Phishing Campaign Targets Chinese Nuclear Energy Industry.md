# Phishing Campaign Targets Chinese Nuclear Energy Industry

### Incident: Phishing Campaign Targets Chinese Nuclear Energy Industry

**Root cause:** Phishing emails containing malicious RAR attachments with CHM and Excel payloads.

**Impact:** Potential exposure and compromise of sensitive information within the Chinese nuclear energy industry. The exact number of devices, people impacted, and financial losses are not specified.

**Mitigation:** 
1. **Email Filtering and Security Awareness:**
   - Implement advanced email filtering solutions to detect and block phishing emails.
   - Conduct regular security awareness training for employees to recognize phishing attempts.
   
2. **Attachment Handling Policies:**
   - Block or restrict email attachments, especially RAR, CHM, and Excel files from unknown senders.
   - Use sandbox environments to analyze suspicious attachments before allowing them into the network.

3. **Endpoint Protection:**
   - Deploy endpoint protection solutions to detect and block malicious activities related to CHM and Excel exploits.
   - Regularly update and patch software, including Microsoft Office and Windows components.

4. **Network Segmentation and Monitoring:**
   - Segment critical systems and sensitive data from the rest of the network.
   - Monitor network traffic for unusual activities, such as frequent connections to known malicious domains.

**Detection Signature:**
- **Service:** Microsoft Office, Windows Task Scheduler, PowerShell
- **Port:** N/A (focus on file and process monitoring)
- **Severity:** Critical
- **Incident:** Phishing Campaign Targets Chinese Nuclear Energy Industry
- **Signature name:** “Phishing Campaign with CHM and Excel Exploits”
- **Internal checks:**
  - Setting1: Monitor for execution of PowerShell scripts and msiexec from suspicious sources.
  - Setting2: Monitor for the creation of unusual scheduled tasks.
  - Setting3: Detect and alert on the opening of CHM and Excel files containing macros or exploits.
- **External scanning:**
  - Monitor for connections to known malicious domains (qwavemediaservice[.]net, mirzadihatti[.]com, coauthcn[.]com).

**IoCs:**
- **File Hashes (SHA256):**
  - 5f663f15701f429f17cc309d10ca03ee00fd20f733220cc9d2502eff5d0cd1a1 (Email)
  - eb7aebded5549f8b006e19052e0d03dc9095c75a800897ff14ef872f18c8650e (Email)
  - cac239cf09a6a5bc1f9a3b29141336773c957d570212b97f73e13122fe032179 (Email)
  - 8d2f6b0d7a6a06708593cc64d9187878ea9d2cc3ae9a657926aa2a8522b93f74 (Email)
  - 33905e2db3775d2e8e75c61e678d193ac2bab5b5a89d798effbceb9ab202d799 (Email)
  - 5c85194ade91736a12b1eeeb13baa0b0da88c5085ca0530c4f1d86342170b3bc (Email)
  - Ef4fb1dc3d1ca5ea8a88cd94596722b93524f928d87dff0d451d44da4e9181f1 (Email)
  - b2566755235c1df3371a7650d94339e839efaa85279656aa9ab4dc4f2d94bbfa (RAR)
  - 33a20950e7f4b2191706ddf9089f1e91be1e5384cca00a57cf6b58056f70c96b (RAR)
  - 7e7e90b076ef3ea4ef8ed4ef14fb599a2acb15d9ce00c78e5949186da1e355cf (RAR)
  - 07504fcef717e6b74ed381e94eab5a9140171572b5572cda87b275e3873c8a88 (XLS)
  - 06b4c1f46845cee123b2200324a3ebb7fdbea8e2c6ef4135e3f943bd546a2431 (CHM)
  - ded0635c5ef9c3d63543abc36a69b1176875dba84ca005999986bd655da3a446 (CHM)

- **Network:**
  - qwavemediaservice[.]net
  - mirzadihatti[.]com
  - coauthcn[.]com
