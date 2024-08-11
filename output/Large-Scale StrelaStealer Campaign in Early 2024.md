Source: [https://unit42.paloaltonetworks.com/strelastealer-campaign/](https://unit42.paloaltonetworks.com/strelastealer-campaign/)

# Large-Scale StrelaStealer Campaign in Early 2024

**Incident:** Large-Scale StrelaStealer Campaign in Early 2024

**Root cause:** Spear phishing emails with malicious ZIP file attachments

**Impact:** Over 100 organizations across the EU and U.S. impacted. Specific financial losses are not detailed in the report.

**Mitigation:** Implement Advanced Threat Prevention and enhance email security measures.
- **Detailed Steps for Mitigation:**
  1. **Email Filtering:** Deploy advanced email filtering solutions to detect and block malicious attachments.
  2. **User Training:** Conduct regular security awareness training for employees to recognize phishing attempts.
  3. **Endpoint Protection:** Install and maintain up-to-date endpoint protection solutions that can detect and mitigate threats like StrelaStealer.
  4. **Network Security:** Use Next-Generation Firewalls with advanced threat prevention features, such as DNS Security and URL Filtering, to block malicious C2 domains and IPs.
  5. **Cloud Security:** Deploy Prisma Cloud Defender agents on cloud-based Windows VMs to ensure protection against malicious binaries.
  6. **Incident Response:** Have a proactive incident response plan in place and engage with services like Unit 42 Incident Response team for both proactive assessments and emergency response.

**Detection Signature:**
  - **Service:** Email client (Outlook, Thunderbird)
  - **Port:** Not applicable (email-based attack)
  - **Severity:** Critical
  - **Incident:** Large-Scale StrelaStealer Campaign
  - **Signature name:** “StrelaStealer Email Campaign”
  - **Internal checks:**
    - **Setting1:** Ensure email filtering for malicious attachments is enabled and updated.
    - **Setting2:** Regularly update and patch email clients and associated software.
    - **Setting3:** Enforce multi-factor authentication for email access.
  - **External scanning:**
    - **Indicator1:** Detection of known malicious email attachment signatures.
    - **Indicator2:** Monitoring for specific malicious payloads (e.g., JScript files, DLL payloads).

**IoCs:**
- **SHA256 Hashes:**
  - 0d2d0588a3a7cff3e69206be3d75401de6c69bcff30aa1db59d34ce58d5f799a
  - e6991b12e86629b38e178fef129dfda1d454391ffbb236703f8c026d6d55b9a1
  - f95c6817086dc49b6485093bfd370c5e3fc3056a5378d519fd1f5619b30f3a2e
  - aea9989e70ffa6b1d9ce50dd3af5b7a6a57b97b7401e9eb2404435a8777be054
  - b8e65479f8e790ba627d0deb29a3631d1b043160281fe362f111b0e080558680
  - 3189efaf2330177d2817cfb69a8bfa3b846c24ec534aa3e6b66c8a28f3b18d4b
  - 544887bc3f0dccb610dd7ba35b498a03ea32fca047e133a0639d5bca61cc6f45
- **C2 Server:**
  - 193[.]109[.]85[.]231

**No additional IoCs found**.
