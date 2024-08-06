# Identification and Disruption of QakBot Infrastructure

Incident: QakBot Infrastructure Disruption

Root cause: The QakBot infrastructure, a modular botnet and malware variant, persisted due to its ability to constantly evolve and evade detection. Its reliance on compromised credentials and hosting providers that ignored abuse complaints facilitated its widespread impact.

Impact: Thousands of devices globally were impacted, particularly within the Financial Services, Emergency Services, and Commercial Facilities Sectors, and the Election Infrastructure Subsector. While exact financial losses are not specified, the costs could include data breaches, ransomware payments, and operational disruptions.

Mitigation:
1. **Implement a recovery plan**: Maintain and retain multiple copies of sensitive data and servers in a physically separate, segmented, and secure location.
2. **Password management**: Require all accounts with password logins to comply with NIST’s standards. This includes using longer passwords, storing them in hashed format, adding password user “salts,” avoiding reusing passwords, implementing account lockouts for multiple failed login attempts, and avoiding frequent password changes.
3. **Use phishing-resistant MFA**: Especially for remote access and access to sensitive data repositories. Implement MFA for webmail, VPNs, and accounts that manage backups.
4. **Keep systems updated**: Regularly update all operating systems, software, and firmware.
5. **Network segmentation**: Prevent the spread of ransomware by controlling traffic flows and restricting adversary lateral movements.
6. **Implement network monitoring tools**: Use tools that log and report all network traffic, including lateral movement activity.
7. **Enable real-time antivirus detection**: Ensure all hosts have updated and real-time antivirus software.
8. **Audit and configure access controls**: Regularly review domain controllers, servers, workstations, and active directories for new and unrecognized accounts.
9. **Disable unused ports and command-line activities**: This helps prevent privilege escalation and lateral movement by threat actors.
10. **Regular secure system backups**: Create known good copies of all device configurations and store them off-network in physically secure locations.
11. **Time-based access**: Implement time-based access methods for admin-level accounts.

Detection Signature:
Service: Windows OS (focus on registry and file paths)
Port: N/A
Severity: Critical
Incident: QakBot infection
Signature name: “QakBot persistence mechanisms”
Internal checks:
  - Setting1: Monitor for changes to registry keys like `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
  - Setting2: Check for unusual files in `C:\Users\<user>\AppData\Roaming\Microsoft\`
  - Setting3: Look for encrypted registry configurations in `HKEY_CURRENT_USER\Software\Microsoft\`
External scanning:
  - IP addresses associated with QakBot C2 servers
  - Unusual network traffic patterns

IoCs:
- IPs affiliated with QakBot infections:
  - 85.14.243[.]111
  - 51.38.62[.]181
  - 51.38.62[.]182
  - 185.4.67[.]6
  - 62.141.42[.]36
  - 87.117.247[.]41
  - 89.163.212[.]111
  - 193.29.187[.]57
  - 193.201.9[.]93
  - 94.198.50[.]147
  - 94.198.50[.]210
  - 188.127.243[.]130
  - 188.127.243[.]133
  - 94.198.51[.]202
  - 188.127.242[.]119
  - 188.127.242[.]178
  - 87.117.247[.]41
  - 190.2.143[.]38
  - 51.161.202[.]232
  - 51.195.49[.]228
  - 188.127.243[.]148
  - 23.236.181[.]102
  - 45.84.224[.]23
  - 46.151.30[.]109
  - 94.103.85[.]86
  - 94.198.53[.]17
  - 95.211.95[.]14
  - 95.211.172[.]6
  - 95.211.172[.]7
  - 95.211.172[.]86
  - 95.211.172[.]108
  - 95.211.172[.]109
  - 95.211.198[.]177
  - 95.211.250[.]97
  - 95.211.250[.]98
  - 95.211.250[.]117
  - 185.81.114[.]188
  - 188.127.243[.]145
  - 188.127.243[.]147
  - 188.127.243[.]193
  - 188.241.58[.]140
  - 193.29.187[.]41


