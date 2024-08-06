# Red Cross-Themed Phishing Attacks Distributing DangerAds and AtlasAgent Backdoors

### Incident: AtlasCross Exploits Red Cross Blood Drive Phishing for Cyberattack

**Root cause:** The root cause of this incident is a phishing document ("Blood Drive September 2023.docm") that exploits the vulnerability of users enabling macros in Microsoft Word documents. This macro subsequently downloads and executes malicious payloads (DangerAds and AtlasAgent).

**Impact:** The report does not specify the exact number of people or devices impacted, nor the financial losses incurred. However, given the sophisticated nature of the attack and the targeted scope, it is reasonable to infer that sensitive information from multiple individuals or entities associated with the Red Cross could have been compromised.

**Mitigation:** To mitigate such incidents, the following steps should be taken:
1. **Email Security:** Implement robust email filtering solutions to detect and block phishing emails.
2. **User Training:** Regularly train employees on the dangers of phishing and the importance of not enabling macros in suspicious documents.
3. **Macro Policies:** Configure Microsoft Office to disable macros by default and only allow macros from trusted locations.
4. **Endpoint Security:** Deploy advanced endpoint protection solutions that can detect and block malicious behaviors associated with macro-based attacks.
5. **Network Segmentation:** Segment network domains to contain potential in-domain penetration.
6. **Regular Analysis:** Conduct continuous threat exposure management and regular security assessments.

**Detection Signature:**
- **Service:** Microsoft Office (Word)
- **Port:** N/A (File-based attack)
- **Severity:** Critical
- **Incident:** AtlasCross Exploits Red Cross Blood Drive Phishing
- **Signature name:** “Malicious Macro Execution”
  - **Internal checks:**
    - **Setting1:** Macro settings should be configured to disable macros by default. – In Microsoft Office Group Policy
    - **Setting2:** Enable Attack Surface Reduction rules to block Office applications from creating child processes. – Endpoint Security Policy
    - **Setting3:** Monitor for the use of InstallUtil.exe by non-administrative users. – Endpoint Security Policy
  - **External scanning:** N/A (File-based attack)

**IoCs:**
- **Phishing Document:** 7195d7e4926a0a85fbe81e40ab7c0ca4
- **DangerAds Trojan:** f8bafe2ce6f11a32109abbab1c42e2cf
- **AtlasAgent Trojan:**
  - ca48431273dfcd2bd025e55f2de30635
  - ba85467ceff628be8b4f0e2da2a5990c
- **Domains:**
  - data.vectorse.com
  - activequest.goautodial.com
  - ops-ca.mioying.com
  - app.basekwt.com
  - secure.poliigon.com
  - engage.adaptqe.com
  - chat.thedresscodeapp.com
  - superapi-staging.mlmprotec.com
  - search.allaccountingcareers.com
  - order.staging.photobookworldwide.com
  - crm.cardabel.com
  - public.pusulait.com
- **RC4 key:** 5haFDov20qfZnyAw4QrtSgAATN7uEkVF
- **PDB path:** C:\Users\invokeops\Documents\Code\atlasagent\x64\Release\AtlasDLL.pdb
