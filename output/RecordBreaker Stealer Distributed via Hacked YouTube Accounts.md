# RecordBreaker Stealer Distributed via Hacked YouTube Accounts

Incident: RecordBreaker Stealer Distributed via Hacked YouTube Accounts

Root cause: Hacked YouTube accounts used for malware distribution.

Impact: Over 120,000 subscribers potentially exposed to malware. The financial losses could vary significantly depending on the data stolen and the extent of the cryptocurrency mining, but specific figures are not provided in the report.

Mitigation: Strengthen the security of YouTube accounts with multi-factor authentication and regular monitoring for suspicious activities.

Detailed Steps for mitigation:
1. **Enable Multi-Factor Authentication (MFA):**
   - Ensure all YouTube account holders enable MFA to add an additional layer of security.
   
2. **Regular Monitoring:**
   - Regularly monitor account activities for any suspicious behavior, such as unexpected uploads or changes in account settings.
   
3. **Educate Users:**
   - Conduct awareness programs for YouTube content creators about the risks of phishing attacks and the importance of using strong, unique passwords.
   
4. **Incident Response Plan:**
   - Develop and implement an incident response plan to quickly address and mitigate any breaches.

5. **Update Security Software:**
   - Ensure that all security software, including antivirus and malware protection, is updated to the latest versions to detect and prevent such malware infections.

Detection Signature:
Service: YouTube
Port: Not applicable
Severity: Critical
Incident: RecordBreaker Stealer Distribution
Signature name: “Hacked YouTube Account for Malware Distribution”
Internal checks:
  - Setting1: Monitor for unusual account activities, such as unexpected video uploads – In platform
  - Setting2: Ensure MFA is enabled for all accounts – In platform
  - Setting3: Regularly review and update security settings – In platform

External scanning:
  - Unusual video uploads
  - Links in video descriptions or comments leading to suspicious download pages

IoCs:
- MD5:
  - 116857ca1574a5a36da3bb0ddff32eac
  - 1cc87e637e55a2e6a88c745855423045
  - 803a1f3e984a9eaa56ac74a203096959
- URL:
  - http[:]//212[.]113[.]119[.]153/
  - http[:]//212[.]113[.]119[.]153/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/freebl3[.]dll
  - http[:]//212[.]113[.]119[.]153/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/mozglue[.]dll
  - http[:]//212[.]113[.]119[.]153/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/msvcp140[.]dll
  - http[:]//212[.]113[.]119[.]153/aN7jD0qO6kT5bK5bQ4eR8fE1xP7hL2vK/nss3[.]dll

Additional IOCs are available on AhnLab TIP.
