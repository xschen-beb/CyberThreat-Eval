Source: [https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html](https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html)

# Black Basta-Affiliated Water Curupira’s Pikabot Spam Campaign

### Incident: Black Basta-Affiliated Water Curupira’s Pikabot Spam Campaign

**Root cause:** Usage of Pikabot loader malware in phishing campaigns, exploiting email-based social engineering techniques.

**Impact:** Potentially widespread, as phishing campaigns can target and impact thousands of individuals and devices. Specific numbers of affected devices and financial losses are not provided.

**Mitigation:** Implement comprehensive email security measures, user education, and multi-layered endpoint protection.
**Detailed Steps for Mitigation:**
1. **User Education and Awareness:**
   - Conduct regular training sessions for employees on recognizing phishing emails.
   - Encourage users to hover over links to verify destinations before clicking.
   - Advise users to verify the sender’s identity and email content before opening any attachments.

2. **Email Security:**
   - Deploy advanced email security solutions such as Trend Micro™ Deep Discovery™ Email Inspector.
   - Employ custom sandboxing and advanced analysis techniques to block malicious emails.

3. **Endpoint Protection:**
   - Use endpoint protection solutions like Trend Micro Apex One™ for automated threat detection and response.
   - Ensure endpoints are protected against advanced threats, including fileless malware and ransomware.

4. **Network Security:**
   - Implement network detection and response solutions to identify and mitigate suspicious network activities.
   - Regularly update and patch operating systems and software to safeguard against known vulnerabilities.

5. **Backup and Recovery:**
   - Maintain regular backups of important data in secure, external locations.
   - Ensure backup systems are not connected to primary networks to prevent ransomware from affecting backups.

**Detection Signature:**
- **Service:** Email (Phishing detection systems)
- **Port:** N/A (Email-based attack)
- **Severity:** Critical
- **Incident:** Black Basta-Affiliated Water Curupira’s Pikabot Spam Campaign
- **Signature name:** “Pikabot phishing email detection”
- **Internal checks:**
  - Setting1: Verify email filters and spam detection rules – Email Security Systems
  - Setting2: Monitor for suspicious email activity and thread-hijacking patterns – SOC Monitoring
  - Setting3: Validate attachment types and enforce strict policies on executable attachments – Email Security Policies
- **External scanning:**
  - Check for known malicious email domains and IPs
  - Monitor for trends in phishing email patterns and techniques

**IoCs:**
- IP addresses:
  - 70[.]34[.]209[.]101
  - 137[.]220[.]55[.]190
  - 139[.]180[.]216[.]25
  - 154[.]61[.]75[.]156
  - 154[.]92[.]19[.]139
  - 158[.]247[.]253[.]155
  - 172[.]233[.]156[.]100

For further details, please refer to the provided blog content.
