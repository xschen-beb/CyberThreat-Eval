# Threat Actors Abuse Cloud Infrastructure in Targeted Telco Attacks

Incident: WIP26 Espionage | Threat Actors Abuse Cloud Infrastructure in Targeted Telco Attacks

Root cause: Abuse of public cloud infrastructure for C2 purposes

Impact: The blog does not provide specific numbers of impacted devices or financial losses. However, it indicates a significant risk to telecommunication providers in the Middle East, potentially affecting sensitive data and high-value network hosts.

Mitigation: Secure email and cloud service interactions, implement strict access controls, and monitor for unusual activity.
- **Detailed Steps for Mitigation:**
  1. **Email Security:**
     - Implement multi-factor authentication (MFA) for all email accounts.
     - Regularly update and review email filtering rules to block phishing attempts.
     - Educate employees on recognizing phishing and spear-phishing attacks.
  2. **Cloud Service Security:**
     - Regularly audit cloud service configurations for misconfigurations.
     - Implement strict access controls and least privilege principles.
     - Monitor cloud service logs for unusual activities such as unauthorized access or data transfer.
  3. **Endpoint Security:**
     - Deploy advanced endpoint protection solutions that include behavioral analysis to detect and block malicious activity.
     - Regularly update endpoint protection software and apply patches to all systems.
  4. **Network Security:**
     - Use network segmentation to limit access to sensitive data and high-value systems.
     - Implement intrusion detection and prevention systems (IDPS) to monitor network traffic for signs of compromise.
  5. **Incident Response:**
     - Develop and regularly update an incident response plan.
     - Conduct regular drills to ensure readiness in the event of a security breach.

Detection Signature:
- **Service:** Microsoft 365 Mail, Google Firebase, Dropbox, Microsoft Azure
- **Port:** Various (common HTTP/HTTPS ports: 80, 443)
- **Severity:** Critical
- **Incident:** WIP26
- **Signature name:** “Cloud Service Abuse for C2”
- **Internal checks:**
  - Setting1: Ensure emails from unknown sources containing links or attachments are flagged or quarantined.
  - Setting2: Monitor cloud service access logs for unusual activity, such as access from unfamiliar IP addresses or unusual times.
  - Setting3: Enforce the use of strong authentication mechanisms for accessing cloud services.
- **External scanning:**
  - Look for public cloud instances being used as C2 servers (monitor traffic to/from known malicious IPs/domains).
  - Scan for unusual data transfer patterns to/from cloud services.

IoCs:
- SHA-1
  - B8313A185528F7D4F62853A44B64C29621627AE7 (PDFelement.exe malware loader)
  - 8B95902B2C444BCDCCB8A481159612777F82BAD1 (CMD365 sample - Update.exe)
  - 3E10A3A2BE17DCF8E79E658F7443F6C3C51F8803 (CMD365 sample - EdgeUpdater.exe)
  - A7BD58C86CF6E7436CECE692DA8F78CEB7BA56A0 (CMDEmber sample - Launcher.exe)
  - 6B5F7659CE48FF48F6F276DC532CD458BF15164C (CMDEmber sample - Update.exe)
- Domain
  - https://gmall-52fb5-default-rtdb.asia-southeast1.firebasedatabase[.]app/
  - https://go0gle-service-default-rtdb.firebaseio[.]com
- URL
  - https://graph.microsoft[.]com/beta/users/3517e816-6719-4b16-9b40-63cc779da77c/mailFolders
  - https://www.dropbox[.]com/s/6a8u8wlpvv73fe4/
  - https://www.dropbox[.]com/s/hbc5yz8z116zbi9/
  - https://socialmsdnmicrosoft.azurewebsites[.]net/AAA/
  - https://socialmsdnmicrosoft.azurewebsites[.]net/ABB/
  - https://socialmsdnmicrosoft.azurewebsites[.]net/AMA/
  - https://socialmsdnmicrosoft.azurewebsites[.]net/AS/
  - https://akam.azurewebsites[.]net/api/File/Upload
- IP address
  - 193.29.56[.]122
