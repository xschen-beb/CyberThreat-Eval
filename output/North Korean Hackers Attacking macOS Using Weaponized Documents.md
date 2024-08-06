# North Korean Hackers Attacking macOS Using Weaponized Documents

### Incident: North Korean Hackers Attacking macOS Using Weaponized Documents

**Root cause:** Exploitation of social engineering and delivery of malicious payloads through weaponized documents and disguised applications.

**Impact:** The specific number of records or devices impacted is not detailed, but given the nature of the attacks involving multiple stages and persistent threats, it can be inferred that a significant number of macOS users, especially those involved in blockchain and cryptocurrency sectors, are impacted. Financial losses would involve costs associated with data breaches, loss of intellectual property, mitigation efforts, and potential ransom payments.

**Mitigation:** 
1. **User Awareness and Training:**
   - Educate users on identifying phishing attempts and social engineering tactics.
   - Implement regular security training sessions to reinforce safe practices.

2. **Application Hardening:**
   - Ensure all applications, particularly those such as Discord, are up-to-date with the latest security patches.
   - Disable unnecessary features and services to reduce the attack surface.

3. **Endpoint Protection:**
   - Deploy comprehensive endpoint protection solutions that can detect and block malicious activities.
   - Utilize behavior-based detection systems to identify unusual activities on macOS endpoints.

4. **Network Security:**
   - Implement network monitoring to detect and block communications to known C2 servers.
   - Use DNS filtering to block access to malicious domains such as those mentioned (e.g., docs-send.online, tp-globa.xyz).

5. **File Integrity Monitoring:**
   - Use tools to monitor and alert on changes to critical files and directories such as /Applications/Discord.app/Contents/MacOS/.

6. **Multi-Factor Authentication (MFA):**
   - Enforce MFA for all critical systems and services to add an additional layer of security.

7. **Incident Response Planning:**
   - Develop and regularly update incident response plans to handle breaches involving malware and persistent threats.
   - Conduct regular tabletop exercises to test the effectiveness of the incident response plan.

**Detection Signature:**
   - **Service:** Discord
   - **Port:** N/A (focus on file paths and network indicators)
   - **Severity:** Critical
   - **Incident:** North Korean macOS Malware Campaign
   - **Signature name:** “macOS Weaponized Document Attack”
   - **Internal checks:**
     - **Setting1:** Monitor /Applications/Discord.app/Contents/MacOS/ for unauthorized modifications.
     - **Setting2:** Check for the presence of suspicious files like .log, appname, and MacOS.tmp.
     - **Setting3:** Ensure that critical system directories such as /Users/Shared/ are not used for unauthorized executables.
   - **External scanning:**
     - **Network Communications:** Monitor for outbound connections to domains and IPs listed as IoCs.
     - **File Integrity:** Scan for known malicious file hashes and signatures related to SUGARLOADER, HLOADER, and KANDYKORN.

**IoCs:**
- **File Hashes:**
  - SUGARLOADER: d28830d87fc71091f003818ef08ff0b723b3f358
  - HLOADER: 43f987c15ae67b1183c4c442dc3b784faf2df090
  - KANDYKORN RAT: 26ec4630b4d1116e131c8e2002e9a3ec7494a5cf46ac6dc34fc164525e6f7886c8ed5a79654f3fd362267b88fa6393bc1f1eeb778e4da6b564b7011e8d5d214c490eae8f61325839fcc17277e514301e8f6c52d7e82fbfdead3d66ad8c52b372cc9e8b189f97edbc1454ef66d6095f979502d17067215a9dac336c5082c2606ab8c3fb023949dfc0db2064d5c45f514a252632cb3851fe45bed34b175370d594ce3705baf097cd95f8f696f330372dd00996d29ae244ff1d8e66558a443610200476f98f653b8519e68bfa72a4b4289a4cc688e81f9282b1f78ebc1fe77270ac0ea05496dd5a2fbccba3e24eb9b863d9
  - ObjCShell: 79337ccda23c67f8cfd9f43a6d3cf05fd01d1588
  - SecurePDF Viewer: a1a8a855f64a6b530f5116a3785a693d78ec09c0e275deb68cdff336cb4175819a09dbaf0e1b68f6
  - Crypto-assets: 09ade0cb777f4a4e0682309a4bc1d0f7d4d7a0365c93052713f317431bf232a2894658a3a4ebfad9884cebf1ad0e65f4da60c04bc31f62f796f90d79be903ded39cbc8332cefd9ebbe7a66d95e9d6522
  - Downloader: 060a5d189ccf3fc32a758f1e218f814f6ce81744
  - Remotely-hosted AppleScript: 3c887ece654ea46b1778d3c7a8a6a7c7c7cfa61cc806c7006950dea6c20d3d2800fe46d9350266b6
- **Network Communications:**
  - http[:]//docs-send.online/getBalance/usdt/ethereum
  - https[:]//drive.google[.]com/file/d1KW5nQ8MZccug6Mp4QtKyWLT3HIZzHNIL2
  - http[:]//on-global[.]xyz/Of56cYsfVV8/OJITWH2WFx/Jy5S7hSx0K/fP7saoiPBc/A%3D%3D
  - http[:]//tp-globa[.]xyz/OdhLca1mLUp/lZ5rZPxWsh/7yZKYQI43S/fP7savDX6c/bfC
  - http[:]//swissborg[.]blog/zxcv/bnm
  - 23.254.226[.]90
  - 104.168.214[.]151
  - 142.11.209[.]144
  - 192.119.64[.]43
- **File Paths:**
  - /Applications/Discord.app/Contents/MacOS/.log
  - /Applications/Discord.app/Contents/MacOS/appname
  - /Library/Caches/com.apple.safari.ck
  - /tmp/tempXXXXXX
  - /Users/Shared/.pld
  - /Users/Shared/.pw
  - /Users/Shared/.sld
