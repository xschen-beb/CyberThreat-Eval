# Behind the Scenes Unveiling the Hidden Workings of Earth Preta

### Incident: Earth Preta APT Campaign

**Root cause:** Spear-phishing campaigns and the use of malware droppers

**Impact:** Various government entities, telecommunications industries, and individuals across APAC, Western Asia, and Eastern Europe. Financial losses are not specified, but the nature of the targets (government and critical infrastructure) implies substantial potential impact.

**Mitigation:** 
1. **Email Security Enhancement:**
   - Implement advanced email filtering solutions to detect and block spear-phishing attempts.
   - Educate employees on recognizing and reporting suspicious emails.
2. **Endpoint Protection:**
   - Deploy robust endpoint detection and response (EDR) solutions to identify and mitigate malware infections.
   - Regularly update antivirus and anti-malware software.
3. **Network Segmentation:**
   - Segment critical networks to contain potential breaches and limit lateral movement.
4. **Access Controls:**
   - Enforce strict access controls and multi-factor authentication (MFA) for all users, especially those with high-level privileges.
   - Regularly review and update access permissions.
5. **Incident Response Plans:**
   - Develop and regularly update incident response plans to quickly address and remediate security incidents.
6. **Threat Intelligence Sharing:**
   - Participate in threat intelligence sharing communities to stay informed about the latest TTPs used by threat actors like Earth Preta.

**Detection Signature:**
   - **Service:** HTTP Server
   - **Port:** Typically 80 or 443 (HTTP/HTTPS)
   - **Severity:** Critical
   - **Incident:** Spear-phishing and malware deployment
   - **Signature name:** “Earth Preta Spear-phishing and Malware Campaign”
   - **Internal checks:**
     - **Setting1:** Identify and monitor unusual outbound traffic from internal email servers to external IPs.
     - **Setting2:** Monitor for unusual file downloads and execution from email clients.
   - **External scanning:**
     - **Port 80/443:** Open and actively serving content
     - **Indicators of phishing attacks:** High volume of emails with suspicious attachments or links

**IoCs:**
- **Domains/IPs:**
  - http://80[.]85[.]156[.]232/fav/tw1
  - http://80[.]85[.]156[.]240/fav/sWjp
  - http://80[.]85[.]156[.]151/fav/eeAll
  - http://103[.]159[.]132[.]91/fav/trteamC
  - https://sa2il[.]johnsimde[.]xyz/f/LV
  - https://iot[.]johnsimde[.]xyz/f/TR
  - https://rewards[.]roshan[.]af/aspnet_client/gdrive.htm

- **Files:**
  - Documents.rar
  - Note-2.7z
  - Note-1.rar

- **Malware Samples:**
  - QMAGENT (MQsTTang)
  - MIROGO (TinyNote)
  - TONEDROP dropper
  - TONEINS and TONESHELL malware

- **Email Indicators:**
  - Spear-phishing emails with Google Drive links or similar spoofed download sites.

**No IoCs found.** (Note: The document mentions the availability of IoCs in an appendix, but they are not included in the provided text.)

By implementing these mitigation measures and detection mechanisms, organizations can better protect themselves against sophisticated APT campaigns like those conducted by Earth Preta.
