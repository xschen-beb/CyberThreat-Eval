# SmoothOperator  Ongoing Campaign Trojanizes 3CXDesktopApp in Supply Chain Attack

**Incident:** 3CX SmoothOperator | 3CXDesktopApp Supply Chain Attack

**Root cause:** Compromised code signing certificate used to sign trojanized installers

**Impact:** The specific number of records or devices impacted is not provided. However, considering 3CX's claim of 600,000 customer companies with 12 million daily users, the potential impact is substantial. Financial losses could include costs related to incident response, customer notification, and potential regulatory fines.

**Mitigation:** Revoke and reissue compromised code signing certificates, conduct a thorough security audit of the software development and distribution pipeline, and implement stringent controls for code signing processes.

**Detailed Steps for mitigation:**
1. **Revoke compromised certificates:** Immediately revoke the compromised code signing certificates to prevent further use.
2. **Issue new certificates:** Issue new, securely managed certificates.
3. **Audit the pipeline:** Conduct a comprehensive security audit of the software development and distribution pipeline to identify and address vulnerabilities.
4. **Implement stringent controls:** Enforce stringent controls around the code signing process, including multi-factor authentication and restricted access.
5. **User communication:** Notify affected users and provide guidance on how to check for and remove compromised versions of the software.
6. **Update detection signatures:** Update antivirus and endpoint detection systems with new signatures to detect and block the trojanized installers.
7. **Continuous monitoring:** Implement continuous monitoring of the software development environment to detect any unauthorized changes.

**Detection Signature:**
   - **Service:** 3CXDesktopApp
   - **Port:** Not specified in the report
   - **Severity:** Critical
   - **Incident:** 3CX SmoothOperator
   - **Signature name:** "3CXDesktopApp trojanized installer"
   - **Internal checks:**
     - **Setting1:** Verify the integrity of installed 3CXDesktopApp instances using known good hashes.
     - **Setting2:** Monitor for unusual network activity from 3CXDesktopApp instances.
     - **Setting3:** Ensure that only signed and verified installers are used in the software deployment process.
   - **External scanning:**
     - Check for known malicious URLs and IPs associated with the campaign.
     - Monitor for communications with command and control servers.

**IoCs:**
- **URLs:**
  - github[.]com/IconStorages/images
  - https://www.3cx[.]com/blog/event-trainings/
  - https://akamaitechcloudservices[.]com/v2/storage
  - https://azureonlinestorage[.]com/azure/storage
  - https://msedgepackageinfo[.]com/microsoft-edge
  - https://glcloudservice[.]com/v1/console
  - https://pbxsources[.]com/exchange
  - https://msstorageazure[.]com/window
  - https://officestoragebox[.]com/api/session
  - https://visualstudiofactory[.]com/workload
  - https://azuredeploystore[.]com/cloud/services
  - https://msstorageboxes[.]com/office
  - https://officeaddons[.]com/technologies
  - https://sourceslabs[.]com/downloads
  - https://zacharryblogs[.]com/feed
  - https://pbxcloudeservices[.]com/phonesystem
  - https://pbxphonenetwork[.]com/voip
  - https://msedgeupdate[.]net/Windows
  - https://sbmsa[.]wiki/blog/_insert
- **Emails:**
  - cliego.garcia@proton[.]me
  - philip.je@proton[.]me
- **SHA-1 Hashes:**
  - cad1120d91b812acafef7175f949dd1b09c6c21a
  - bf939c9c261d27ee7bb92325cc588624fca75429
  - 20d554a80d759c50d6537dd7097fed84dd258b3e
- **File Paths:**
  - ~/Library/Application Support/3CXDesktop App/.main_storage
  - ~/Library/Application Support/3CXDesktop App/UpdateAgent

**No IoCs found** in other contexts.
