# Stealth Soldier Backdoor Used in Targeted Espionage Attacks in North Africa

### Incident: Stealth Soldier Backdoor Used in Targeted Espionage Attacks in North Africa

**Root Cause:** The root cause of this incident is the exploitation of targeted spear-phishing campaigns to deliver the Stealth Soldier backdoor malware. The malware utilizes a complex infection chain that includes social engineering, downloader mechanisms, and multi-stage payloads. 

**Impact:** The impact of this incident involves unauthorized surveillance activities on targeted devices, including file exfiltration, screen and microphone recording, keystroke logging, and stealing browser information. The exact number of impacted devices and financial losses are not provided in the report.

**Mitigation:** 
1. **Employee Training:** Conduct regular training sessions to educate employees about phishing attacks and how to recognize and report them.
2. **Email Filtering:** Implement robust email filtering solutions to detect and block phishing emails before they reach end users.
3. **Software Updates:** Ensure all systems and software are up to date with the latest security patches.
4. **Endpoint Protection:** Deploy advanced endpoint protection solutions that can detect and block unauthorized activities such as keystroke logging and unauthorized access to microphones and cameras.
5. **Network Segmentation:** Use network segmentation to limit the movement of malware within the network.
6. **Monitoring and Response:** Set up continuous monitoring systems to detect anomalies and unauthorized activities. Have an incident response plan in place to act quickly if a breach is detected.

**Detection Signature:**
- **Service:** Web Server (C&C Communication)
- **Port:** Various (HTTP/HTTPS ports like 80, 443)
- **Severity:** Critical
- **Incident:** Stealth Soldier Backdoor
- **Signature Name:** “Stealth Soldier C&C Communication”
- **Internal Checks:**
  - Ensure all network connections to known C&C servers are blocked.
  - Monitor for unusual outbound traffic to suspicious domains.
  - Check for the presence of malicious files like "MSDataV5.16945.exe," "MSCheck.exe," and "pwls.dll" on endpoints.
- **External Scanning:**
  - Scan for open ports associated with suspicious outbound connections.
  - Check for connections to known malicious IP addresses and domains.

**IoCs:**
- **Domains:**
  - filestoragehub[.]live
  - customjvupdate[.]live
  - filecloud[.]store
  - webmailogemail[.]com
  - loglivemail[.]com
  - 2096[.]website

- **IPs:**
  - 185.125.230.216
  - 185.125.230.116
  - 94.156.33.228
  - 94.156.33.229
  - 185.125.230.224
  - 185.125.230.220

- **Hashes:**
  - 2cad816abfe4d816cf5ecd81fb23773b6cfa1e85b466d5e5a48112862ceb3efb
  - 05db5e180281338a95e43a211f9791bd53235fca1d07c00eda0be7fdc3f6a9bc
  - b9e9b93e99d1a8fe172d70419181a74376af8188dcb03249037d4daea27f110e
  - d57fc4e8c14da6404bdcb4e0e6ac79104386ffbd469351c2a720a53a52a677db
  - e7794facf887a20e08ed9855ac963573549809d373dfe4a287d1dae03bffc59f
  - 8c09a804f408f7f9edd021d078260a47cf513c3ce339c75ebf42be6e9af24946
  - df6a44551c7117bc2bed2158829f2d0472358503e15d58d21b0b43c4c65ff0b4
  - e546d48065ff8d7e9fef1d184f48c1fd5e90eb0333c165f217b0fb574416354f
  - a43ababe103fdce14c8aa75a00663643bf5658b7199a30a8c5236b0c31f08974
  - c0b75fd1118dbb86492a3fc845b0739d900fbbd8e6c979b903267d422878dbc6
  - cb90a9e5d8b8eb2f81ecdbc6e11fba27a3dde0d5ac3d711b43a3370e24b8c90a
  - d6655e106c5d85ffdce0404b764d81b51de54447b3bb6352c5a0038d2ce19885
  - b94257b4c1fac163184b2d6047b3d997100dadf98841800ec9219ba75bfd5723
  - 7bfe2a03393184d9239c90d018ca2fdccc1d4636dfb399b3a71ea6d5682c92bd

This analysis should help in understanding the root cause, impact, detection, and mitigation of the Stealth Soldier backdoor malware incident.
