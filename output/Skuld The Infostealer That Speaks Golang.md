# Skuld The Infostealer That Speaks Golang

Incident: Skuld Infostealer Incident

Root cause: Introduction and propagation of Skuld malware, which is written in Golang and leverages open-source tools to steal sensitive information.

Impact: Global impact with a specific example of data being stolen from Discord and web browsers, along with system files and cryptocurrency wallet information. **Exact number of devices and financial losses are not provided but include multiple global instances.**

Mitigation: Implement comprehensive endpoint security measures, including but not limited to:
1. **Update and patch management:** Regularly update all software and systems to patch known vulnerabilities.
2. **Endpoint Detection and Response (EDR):** Deploy an EDR solution to monitor and respond to threats in real-time.
3. **Network Segmentation:** Isolate critical systems from general network access to minimize lateral movement.
4. **User Training:** Conduct regular cybersecurity awareness training for users to recognize phishing attempts and suspicious activities.
5. **Strong Authentication:** Use multi-factor authentication (MFA) and strong, unique passwords for all access points.
6. **Application Whitelisting:** Only allow approved applications to execute on systems.
7. **Regular Audits:** Perform regular security audits and vulnerability assessments to identify and remediate potential weaknesses.

Detection Signature:
- Service: Discord, Chromium-based browsers, Gecko-based browsers
- Port: Not applicable (being stealthy and using regular application ports)
- Severity: Critical
- Incident: Skuld Infostealer
- Signature name: “Skuld Infostealer Detection”
  - Internal checks:
    - Setting1: Monitor for unauthorized modifications to %APPDATA%\BetterDiscord\data\betterdiscord.asar and %APPDATA%\DiscordTokenProtector\config.json.
    - Setting2: Detect and block unauthorized JavaScript injection attempts in Discord.
    - Setting3: Track and alert on unusual file compression and exfiltration activities.
  - External scanning:
    - Monitor for unusual traffic to Discord webhook URLs.
    - Monitor for connections to Gofile upload services.

IoCs: 

- **Hashes:**
  - MD5: 8df1e0135851d1a0b66fbaa9be282009
  - SHA1: 1b6523dc8dea8e2f29e8d55819ac75b94da9acbf
  - SHA256: d11efad7ebe520ccc9f682003d76ebfabd5d18b746a801fefbf04317f7ae7505

- **Discord webhooks:**
  - https://discord[.]com/api/webhooks/1101151106052145214/BIaHrwzWkurP1ifNTfI0S-nV_adpU3L7CtHkZgsoxNh0xWIhQpjX2fdzD9kB7BDNYQi7
  - https://discord[.]com/api/webhooks/963128514779959316/ruqcIVO-IzGEWVxFyDIITM7YCzbyrnmAu55FnFdc4inoDqbx2o3dSOjAkc1lGOf9ytAf
  - https://discord[.]com/api/webhooks/1101120631296237639/mesriMSa71vT7Vf_chsUKzwpQEbKiBcK1y1GiKUCoC360ZH8EuTmJQKMDSmB-LGAqbJw

- **IP addresses blocklist:**
  - 88.132.231.71
  - 95.25.204.90
  - 34.105.72.241
  - 34.85.243.241
  - ... (many more listed in the document)

No further IoCs found beyond those listed.

By addressing these points, organizations can significantly mitigate the risks associated with Skuld infostealer and protect sensitive data from being compromised.
