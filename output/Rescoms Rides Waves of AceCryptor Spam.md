Source: [https://www.welivesecurity.com/en/eset-research/rescoms-rides-waves-acecryptor-spam/](https://www.welivesecurity.com/en/eset-research/rescoms-rides-waves-acecryptor-spam/)

# Rescoms Rides Waves of AceCryptor Spam

**Incident: Rescoms rides waves of AceCryptor spam**

**Root cause:** The root cause of the incident was the use of AceCryptor by threat actors to pack and distribute Rescoms RAT (Remote Access Trojan) through spam campaigns.

**Impact:** Over 42,000 ESET users were protected from AceCryptor-packed malware in H2 2023. **The financial losses are not explicitly mentioned in the report.**

**Mitigation:** Secure email systems against phishing attacks and improve endpoint security to detect and block malware. Additionally, implement the following detailed steps for mitigation:

1. **Email Security Enhancements:**
   - Implement robust email filtering to detect and quarantine suspicious emails.
   - Use DMARC, DKIM, and SPF protocols to prevent email spoofing.
   - Regularly update and train employees on phishing identification and response.

2. **Endpoint Protection:**
   - Deploy comprehensive endpoint protection solutions that can detect and block malware like AceCryptor.
   - Ensure all systems are up-to-date with the latest security patches.

3. **Network Security:**
   - Monitor network traffic for unusual activities that could indicate malware communication.
   - Implement network segmentation to limit the spread of infections.

4. **Incident Response Plan:**
   - Develop and regularly update an incident response plan to quickly mitigate the impact of detected malware.
   - Conduct regular security audits and vulnerability assessments.

**Detection Signature:**
- **Service:** AceCryptor
- **Port:** N/A (Delivered via email attachments)
- **Severity:** Critical
- **Incident:** Rescoms RAT distribution
- **Signature name:** “AceCryptor-packed malware”
- **Internal checks:**
  - **Setting1:** Email servers should block attachments with executable files. – In platform
  - **Setting2:** Monitor and alert on any unexpected outbound connections from endpoints. – Inside VMs
  - **Setting3:** Ensure email systems are configured with DMARC, DKIM, and SPF. – Inside VMs
- **External scanning:**
  - **Unusual email traffic patterns**
  - **Presence of known malicious attachment signatures**

**IoCs:**
- **SHA-1 Hashes:**
  - 7D99E7AD21B54F07E857FC06E54425CD17DE3003
  - 7DB6780A1E09AEC6146ED176BD6B9DF27F85CFC1
  - 7ED3EFDA8FC446182792339AA14BC7A83A272F85
  - 9A6C731E96572399B236DA9641BE904D142F1556
  - 57E4EB244F3450854E5B740B95D00D18A535D119
  - 178C054C5370E0DC9DF8250CA6EFBCDED995CF09
  - 394CFA4150E7D47BBDA1450BC487FC4B970EDB35
  - 3734BC2D9C321604FEA11BF550491B5FDA804F70
  - 71076BD712C2E3BC8CA55B789031BE222CFDEEA7
  - 667133FEBA54801B0881705FF287A24A874A400B
  - AF021E767E68F6CE1D20B28AA1B36B6288AFFFA5
  - BB6A9FB0C5DA4972EFAB14A629ADBA5F92A50EAC
  - D2FF84892F3A4E4436BEDC221102ADBCAC3E23DC
  - DB87AA88F358D9517EEB69D6FAEE7078E603F23C
  - EF2106A0A40BB5C1A74A00B1D5A6716489667B4C
  - FAD97EC6447A699179B0D2509360FFB3DD0B06BF
  - FB8F64D2FEC152D2D135BBE9F6945066B540FDE5

- **MITRE ATT&CK techniques:**
  - **Tactic:** Reconnaissance
    - **ID:** T1589.002
    - **Name:** Gather Victim Identity Information: Email Addresses
  - **Tactic:** Resource Development
    - **ID:** T1586.002
    - **Name:** Compromise Accounts: Email Accounts
  - **Tactic:** Initial Access
    - **ID:** T1566
    - **Name:** Phishing
  - **Tactic:** Execution
    - **ID:** T1204.002
    - **Name:** User Execution: Malicious File
  - **Tactic:** Credential Access
    - **ID:** T1555.003
    - **Name:** Credentials from Password Stores: Credentials from Web Browsers

The document provides a comprehensive overview of the incident, its impact, and necessary mitigation steps, ensuring a thorough response to the threat.
