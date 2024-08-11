Source: [https://www.malwarebytes.com/blog/threat-intelligence/2023/07/socgholish-copycat-delivers-netsupport-rat](https://www.malwarebytes.com/blog/threat-intelligence/2023/07/socgholish-copycat-delivers-netsupport-rat)

# FakeSG Enters the FakeUpdates Arena to Deliver NetSupport RAT

Incident: FakeSG enters the ‘FakeUpdates’ arena to deliver NetSupport RAT

Root cause: Compromised WordPress websites

Impact: Potentially thousands of users impacted globally, exact financial losses are unknown.

Mitigation: Secure WordPress sites, monitor for suspicious activity, and educate users. Detailed steps for mitigation include:
1. Regularly update WordPress and its plugins to the latest versions.
2. Implement strong, unique passwords and two-factor authentication for all user accounts.
3. Conduct regular security audits and vulnerability assessments.
4. Use a reputable security plugin to monitor and protect against suspicious activities.
5. Educate users on recognizing phishing attempts and fake update prompts.

Detection Signature:
- Service: WordPress
- Port: 80/443 (HTTP/HTTPS)
- Severity: Critical
- Incident: FakeSG campaign
- Signature name: “Compromised WordPress hosting FakeUpdates”
- Internal checks:
  - Setting1: Ensure WordPress core, themes, and plugins are up to date.
  - Setting2: Ensure file permissions are correctly set to prevent unauthorized access.
  - Setting3: Monitor logs for unusual login attempts or file modifications.
- External scanning:
  - Detect unusual traffic patterns or large data transfers.
  - Scan for known malicious domains or IP addresses involved in FakeSG campaigns.

IoCs:
- FakeSG infrastructure:
  - 178.159.37[.]73
  - google-analytiks[.]com
  - googletagmanagar[.]com
  - updateadobeflash[.]website
- Internet shortcut:
  - pietrangelo[.]it/wp-content/uploads/2014/05/Install%20Updater%20(V104.25.151)-stable[.]url
  - ishahcouture[.]com/wp-content/uploads/2021/01/Install%20Updater%20(v102.22.145)[.]url
  - safetyofficer[.]pk/wp-content/uploads/2019/02/Install%20Updater%20(V106.21.845)-stable(w).url
- WebDav launcher:
  - 206[.]71[.]148[.]110
  - 85[.]217[.]144[.]63
  - 206[.]71[.]148[.]110/Downloads/launcher-upd[.]hta
  - 85[.]217[.]144[.]63/Downloads/updater-install-brsw[.]hta
  - 85[.]217[.]144[.]63/Downloads/installer-msi[.]hta
  - 85[.]217[.]144[.]63/Downloads/msi-installupd[.]hta
  - 85[.]217[.]144[.]63/Downloads/updater-install(win-macOs)[.]hta
- NetSupport RAT:
  - pietrangelo[.]it/wp-content/uploads/2014/04/BranScale[.]zip
  - pietrangelo[.]it/wp-content/uploads/2014/04/client32[.]exe
  - ishahcouture[.]com/wp-content/uploads/2020/03/ActiveGlucol[.]zip
  - renovationpro[.]us/wp-content/uploads/2021/01/b_brsw_installupd(msi-v542.00.17)[.]zip
  - sochilicious[.]com/wp-content/uploads/2020/11/BRSW_installupd_win7-81_V205510_Win10_V2051500[.]zip
  - safetyofficer[.]pk/wp-content/uploads/2018/04/HomeTires.zip
  - safetyofficer[.]pk/wp-content/uploads/2018/04/client32.exe
- NetSupport RAT C2:
  - 94[.]158[.]247[.]27

MITRE ATT&CK techniques:
- Execution: T1059 (Command and Scripting Interpreter), T1059.001 (Powershell), T1059.003 (Windows Command Shell)
- Privilege escalation: T1548 (Abuse Elevation Control Mechanism), T1548.002 (Bypass User Account Control)
- Defense evasion: T1564 (Hide Artifacts), T1218 (System Binary Proxy Execution), T1027 (Obfuscated Files or Information), T1112 (Modify Registry), T1548 (Abuse Elevation Control Mechanism), T1140 (Deobfuscate/Decode Files or Information)
- Discovery: T1082 (System Information Discovery)
- C&C: T1071 (Application Layer Protocol), T1571 (Non-Standard Port)

No additional IoCs found.
