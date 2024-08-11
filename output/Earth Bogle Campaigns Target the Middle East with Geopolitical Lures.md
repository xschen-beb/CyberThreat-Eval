Source: [https://www.trendmicro.com/en_us/research/23/a/earth-bogle-campaigns-target-middle-east-with-geopolitical-lures.html](https://www.trendmicro.com/en_us/research/23/a/earth-bogle-campaigns-target-middle-east-with-geopolitical-lures.html)

# Earth Bogle Campaigns Target the Middle East with Geopolitical Lures

Incident: Earth Bogle: Campaigns Target the Middle East with Geopolitical Lures

Root cause: Compromised web servers and abuse of public cloud storage services

Impact: The exact number of impacted devices and financial losses are not detailed in the report. However, considering the widespread distribution across the Middle East and North Africa, it is implied that numerous individuals and organizations in these regions might be affected.

Mitigation: 
1. Secure web servers by ensuring they are regularly patched and monitored for unauthorized access.
2. Implement strict access controls and authentication mechanisms for public cloud storage services.
3. Educate users about the risks of opening suspicious files from untrusted sources, especially those related to sensational topics.
4. Employ advanced email filtering and malware detection solutions to identify and block malicious attachments and links.
5. Use multi-layered security solutions to detect, scan, and block malicious URLs and payloads.

Detailed Steps for mitigation:
- Ensure all web servers have the latest security patches and updates.
- Regularly audit and monitor web server logs for signs of compromise.
- Use robust access control policies, including multi-factor authentication (MFA), for accessing cloud storage services.
- Educate employees and users on recognizing phishing attempts and suspicious files.
- Implement and maintain an advanced email security solution to filter out malicious attachments and links.
- Employ endpoint protection solutions that can detect and prevent the execution of malicious scripts and payloads.
- Regularly back up data and ensure backups are isolated from the network to prevent ransomware from encrypting them.

Detection Signature:
Service: Web server (e.g., Apache, Nginx)
Port: 80, 443
Severity: Critical
Incident: Earth Bogle Campaign
Signature name: “Compromised web server distributing malware”
Internal checks:
    - Setting1: Ensure web server software is up to date. – In platform
    - Setting2: Monitor web server logs for unusual activity. – Inside VMs
    - Setting3: Implement access control measures on web server configuration files. – Inside VMs
External scanning:
    - Check for unusual outbound connections from the web server.
    - Scan for open and vulnerable ports that should not be exposed.

IoCs:
- CAB files with SHA256 hashes:
  - a7e2b399b9f0be7e61977b51f6d285f8d53bd4b92d6e11f74660791960b813da
  - 4985b6e286020de70f0b74d457c7e387463ea711ec21634e35bc46707dfe4c9b
- VBS script with SHA256 hash:
  - 6560ef1253f239a398cc5ab237271bddd35b4aa18078ad253fd7964e154a2580
- Second stage dropper with SHA256 hash:
  - 78ac9da347d13a9cf07d661cdcd10cb2ca1b11198e4618eb263aec84be32e9c8
- Malicious domain:
  - gpla[.]gov[.]ly

Download the full list of IOCs here: [link to IOCs file] (as mentioned in the blog, assuming there is a downloadable list available).
