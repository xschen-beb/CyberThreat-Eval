# Tailing Big Head Ransomware’s Variants, Tactics, and Impact

**Incident: Big Head Ransomware Variants Analysis**

**Root cause:** The root cause of the Big Head ransomware outbreaks is the distribution of malware through malvertisements disguised as fake Windows updates and fake Word installers.

**Impact:** The blog does not provide a specific number of impacted devices or financial losses. However, given the nature of ransomware, it can be assumed that it has the potential to impact a significant number of devices and cause substantial financial damage due to data encryption and ransom demands.

**Mitigation:** 
1. **User Education:** Train users to recognize phishing attempts and malvertisements.
2. **Email Filtering:** Implement robust email filtering to block malicious emails.
3. **Software Updates:** Ensure that all software updates come from official sources.
4. **Antivirus and EDR Solutions:** Deploy and maintain up-to-date antivirus and endpoint detection and response (EDR) solutions.
5. **Regular Backups:** Implement a regular backup strategy and ensure backups are stored offline or in a secure, separate network.
6. **Network Segmentation:** Segment networks to limit the spread of ransomware.
7. **Application Whitelisting:** Implement application whitelisting to prevent unauthorized applications from executing.

**Detailed Steps for mitigation:**
1. **Educate Employees:** Conduct regular training on how to spot phishing attempts and suspicious downloads.
2. **Email Security:** Configure email gateways to filter out malicious attachments and links.
3. **Patch Management:** Regularly update and patch all systems and software to mitigate known vulnerabilities.
4. **Deploy Security Solutions:** Use advanced threat protection tools, such as EDR and antivirus software, and ensure they are regularly updated.
5. **Backup Strategy:** Establish a comprehensive backup policy, perform regular backups, and test restoration processes periodically.
6. **Network Controls:** Implement network segmentation and access controls to contain the spread of ransomware in case of an infection.
7. **Application Controls:** Use application whitelisting to allow only trusted software to run on the network.
8. **Incident Response Plan:** Develop and regularly update an incident response plan to quickly respond to and mitigate ransomware attacks.

**Detection Signature:**
- **Service:** Windows-based systems
- **Port:** Not specified (Typically, ransomware does not rely on specific open ports but can exploit various services)
- **Severity:** Critical
- **Incident:** Big Head Ransomware
- **Signature name:** “Big Head ransomware infection”
- **Internal checks:**
  - **Setting1:** Ensure all software updates are verified and come from official sources. – In platform
  - **Setting2:** Regularly scan for unauthorized applications and processes – Inside VMs
  - **Setting3:** Implement and enforce the use of strong, unique passwords and multi-factor authentication – Inside VMs
- **External scanning:**
  - Monitor for indicators of compromise (IoCs) related to Big Head ransomware
  - Check for unusual outbound network traffic that could indicate communication with command and control servers

**IoCs:**
- **Sample Hashes:**
  - SHA256: 6d27c1b457a34ce9edfb4060d9e04eb44d021a7b03223ee72ca569c8c4215438
  - SHA256: 2a36d1be9330a77f0bc0f7fdc0e903ddd99fcee0b9c93cb69d2f0773f0afd254
  - SHA256: 25294727f7fa59c49ef0181c2c8929474ae38a47b350f7417513f1bacf8939ff

- **URLs:**
  - hxxps[:]//t[.]me/[REDACTED]_69
  - hxxps[:]//github[.]com/[REDACTED]_69

- **Emails:**
  - Specific contact emails found in the ransom notes

**Note:** Always refer to up-to-date threat intelligence feeds and your cybersecurity tools' documentation for the latest IoCs and detection rules.
