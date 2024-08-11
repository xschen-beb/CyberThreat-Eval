Source: [https://yoroi.company/research/money-ransomware-the-latest-double-extortion-group/](https://yoroi.company/research/money-ransomware-the-latest-double-extortion-group/)

# Money Ransomware The Latest Double Extortion Group

### Incident: Money Ransomware Attack

#### Root cause: Human-operated intrusion and exploitation of compromised credentials

#### Impact: 
- **Number of Devices/People Impacted:** Two victims as of the time of writing, including the Bangladesh National Airport.
- **Financial Losses:** Not explicitly mentioned in the blog, but typically involves ransom amounts demanded by attackers, costs of system downtime, loss of data, and recovery expenses.

#### Mitigation: 
- **Secure Access Controls:** Implement robust authentication mechanisms, including multi-factor authentication (MFA), to prevent unauthorized access.
- **Regular Updates and Patching:** Ensure that all systems and software are regularly updated with the latest security patches.
- **Network Segmentation:** Segregate critical systems and sensitive data to limit the spread of ransomware.
- **Endpoint Protection:** Deploy advanced endpoint protection solutions that can detect and respond to ransomware activities.
- **Regular Backups:** Maintain regular, secure, and offline backups of critical data to enable recovery in case of an attack.
- **Employee Training:** Conduct regular training sessions to educate employees on recognizing phishing and social engineering attacks.
- **Network Monitoring:** Implement continuous network monitoring to detect and respond to suspicious activities.

**Detailed Steps for Mitigation:**
1. **Authentication and Access Control:**
    - Implement MFA for all remote access and sensitive operations.
    - Regularly review and update access permissions to ensure the principle of least privilege.
2. **System Updates:**
    - Schedule regular patch management processes to ensure all systems are up-to-date.
    - Deploy automated tools to manage and verify patch deployment.
3. **Network Segmentation:**
    - Use firewalls and VLANs to separate critical systems and data from other parts of the network.
    - Implement strict access controls between segments.
4. **Endpoint Protection:**
    - Deploy EDR (Endpoint Detection and Response) solutions to detect and mitigate suspicious behavior.
    - Regularly update anti-malware software and enable real-time protection.
5. **Regular Backups:**
    - Schedule regular backups of all critical data.
    - Store backups offline and test them periodically to ensure data integrity.
6. **Employee Training:**
    - Conduct regular cybersecurity awareness training.
    - Use simulated phishing exercises to reinforce training.
7. **Network Monitoring:**
    - Implement SIEM (Security Information and Event Management) solutions for real-time monitoring.
    - Set up alerts for unusual activities and conduct regular threat hunting exercises.

#### Detection Signature:
- **Service:** Windows API (WNetAddConnection2W)
- **Port:** Not specified (typically uses port 445 for SMB connections)
- **Severity:** Critical
- **Incident:** Money Ransomware Attack
- **Signature name:** “Unauthorized Network Access - WNetAddConnection2W”
- **Internal checks:**
    - **Setting1:** Monitor and restrict the use of WNetAddConnection2W API calls.
    - **Setting2:** Review access logs for unusual login attempts and network connections.
    - **Setting3:** Ensure domain accounts are protected with strong passwords and MFA.
- **External scanning:**
    - **Port 445 open:** Ensure only necessary systems have port 445 open and restrict access.
    - **Unauthorized access attempts:** Monitor for unauthorized access attempts using compromised credentials.

#### IoCs:
- **IP:** Not provided in the blog.
- **Domain:** Not provided in the blog.
- **Hash:**
    - bbdac308d2b15a4724de7919bf8e9ffa713dea60ae3a482417c44c60012a654b

#### Yara Rule:
```yara
rule money_ransomware {
    meta:
        author = "Yoroi Malware ZLab"
        description = "Rule for Money Ransomware"
        last_updated = "2023-03-28"
        tlp = "WHITE"
        category = "informational"
    strings:
        $1 = { 68 ?? ?? ?? ?? 68 ?? ?? ?? ?? c7 45 e8 00 00 00 00 ff 15 ?? ?? ?? ?? 50 ff 15 ?? ?? ?? ?? 8b f0 85 f6 0f 84 ?? ?? ?? ?? eb ?? 8b 4d e0 8b 01 ff 50 04 89 45 e4 8d 45 e4 50 83 ec 08 8b c4 c7 00 ?? ?? ?? ?? c7 40 04 3e 00 00 00 e8 ?? ?? ?? ?? 83 c4 0c b8 ?? ?? ?? ?? c3 }
        $2 = {8d 47 30 3b c6 74 ?? 8b c8 e8 ?? ?? ?? ?? 8b 0e 89 4f 30 8b 46 04 89 47 34 8b 46 08 89 47 38 c7 06 00 00 00 00 c7 46 04 00 00 00 00 c7 46 08 00 00 00 00 8d ?? 14 ff ff ff e8 ?? ?? ?? ??}
    condition:
        uint16(0) == 0x5A4D and ($1 or $2)
}
```

### Summary:
The Money Ransomware group utilizes compromised credentials and API calls to propagate and encrypt sensitive data within networks. Mitigation involves securing access controls, regular updates, endpoint protection, network monitoring, and employee training. The provided Yara rule and detection signature can assist in identifying and responding to such threats.
