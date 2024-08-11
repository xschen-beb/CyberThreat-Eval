Source: [https://www.sentinelone.com/labs/chinese-entanglement-dll-hijacking-in-the-asian-gambling-sector/](https://www.sentinelone.com/labs/chinese-entanglement-dll-hijacking-in-the-asian-gambling-sector/)

# Chinese Entanglement  DLL Hijacking in the Asian Gambling Sector

### Incident: Chinese Entanglement | DLL Hijacking in the Asian Gambling Sector

**Root Cause:** Vulnerable executables for DLL hijacking

**Impact:** The scope of the impact is not fully detailed in the provided document. The specific number of devices, people impacted, or financial losses are not mentioned.

**Mitigation:**
1. **Update Vulnerable Software:**
   - Ensure all software such as Adobe Creative Cloud, Microsoft Edge, and McAfee VirusScan are updated to versions that are not susceptible to DLL hijacking.
   
2. **Code Signing Certificate Management:**
   - Regularly audit and monitor the use of code-signing certificates.
   - Implement stringent access controls and protections against certificate theft.
   
3. **Network Segmentation and Firewalls:**
   - Implement network segmentation to isolate critical systems from potential entry points.
   - Use firewalls to restrict and monitor traffic to and from known malicious C2 domains and IP addresses.

4. **Endpoint Protection:**
   - Deploy endpoint detection and response (EDR) solutions to monitor for and block suspicious activities, such as unauthorized DLL loading.
   
5. **User Training:**
   - Conduct regular training sessions to educate users on phishing and malware risks to minimize the chances of initial compromise.
   
6. **Regular Security Audits:**
   - Perform regular security audits and vulnerability assessments to identify and rectify potential security weaknesses.

**Detection Signature:**
- **Service:** Cobalt Strike
- **Port:** 8443
- **Severity:** Critical
- **Incident:** DLL Hijacking in the Asian Gambling Sector
- **Signature name:** “Cobalt Strike C2 Communication”

**Internal checks:**
  - **Setting1:** Ensure that executables are not vulnerable to DLL hijacking. – Inside VMs
  - **Setting2:** Monitor for unauthorized signing certificates. – Inside VMs
  - **Setting3:** Check for unexpected network traffic to known C2 domains and IP addresses. – In platform

**External scanning:**
  - **Port (8443) open**
  - **C2 domains and IP addresses**

**IoCs:**
- **Domains:**
  - duckducklive[.]top
  - www.100helpchat[.]com
  - live100heip[.]com

- **IP Addresses:**
  - 8.218.31[.]103
  - 47.242.72[.]118
  - 47.242.159[.]242

- **File Hashes (SHA1):**
  - 09f82b963129bbcc6d784308f0d39d8c6b09b293
  - 1a11aa4bd3f2317993cfe6d652fbe5ab652db151
  - 32b545353f4e968dc140c14bc436ce2a91aacd82
  - 4b79016d11910e2a59b18275c786682e423be4b4
  - 559b4409ff3611adaae1bf03cbadaa747432521b
  - 57bbc5fcfd97d25edb9cce7e3dc9180ee0df7111
  - 6e9592920cdce90a7c03155ef8b113911c20bb3a
  - 76bf5ab6676a1e01727a069cc00f228f0558f842
  - 88c353e12bd23437681c79f31310177fd476a846
  - 957e313abaf540398af47af367a267202a900007

- **Second-Stage Data URLs:**
  - https[://]agenfile.oss-ap-southeast-1[.]aliyuncs.com/agent_source/temp1/cefhelper.zip
  - https[://]agenfile.oss-ap-southeast-1.aliyuncs.com/agent_source/temp2/agent_bak.zip
  - https[://]agenfile.oss-ap-southeast-1.aliyuncs.com/agent_source/temp3/adobe_helper.zip
  - https[://]codewavehub.oss-ap-southeast-1.aliyuncs[.]com/org/com/file/CodeVerse.zip
