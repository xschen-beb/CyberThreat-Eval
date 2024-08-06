# Following The Lazarus Group By Tracking DeathNote Campaign

Incident: Lazarus Group DeathNote Campaign

Root cause: Exploitation of vulnerabilities in widely used software and strategic use of Trojanized documents and software.

Impact: The campaign targeted multiple sectors including cryptocurrency businesses, defense contractors, automotive, academic sectors, and IT companies. **Specific impact numbers and financial losses are not provided in the blog.**

Mitigation: Implementing comprehensive security measures to protect against such sophisticated APT attacks.
**Detailed Steps for mitigation:**
1. **Implement Multi-layered Defense:**
   - Use advanced endpoint protection and threat detection tools.
   - Employ network segmentation to limit lateral movement.
   - Deploy intrusion detection and prevention systems (IDPS).

2. **Secure Software and Applications:**
   - Regularly update and patch all software to fix known vulnerabilities.
   - Use application whitelisting to prevent the execution of unauthorized software.

3. **Improve Email and Document Security:**
   - Educate users on the risks of enabling macros in documents.
   - Implement email filtering to block malicious attachments and links.

4. **Enhance Monitoring and Logging:**
   - Enable detailed logging and monitor for suspicious activities.
   - Use SIEM (Security Information and Event Management) systems to correlate and analyze logs.

5. **Implement Strong Authentication:**
   - Use multi-factor authentication (MFA) for accessing sensitive systems.
   - Regularly update and enforce strong password policies.

6. **Conduct Regular Security Audits and Penetration Testing:**
   - Perform regular security assessments to identify and mitigate vulnerabilities.
   - Engage in red team exercises to simulate attacks and improve defense mechanisms.

Detection Signature:
- Service: PDF Reader, Word Processor, Remote Desktop Services, etc.
- Port: Various (as per the services exploited)
- Severity: Critical
- Incident: Lazarus Group DeathNote Campaign
- Signature name: “Suspicious Document or Software Execution”
- Internal checks:
   - Setting1: Monitor for execution of macros in documents.
   - Setting2: Detect creation and execution of executables from user directories.
   - Setting3: Monitor for suspicious command-line parameters used in legitimate software.
- External scanning:
   - Check for open ports and services vulnerable to exploitation.
   - Identify unusual traffic patterns indicative of C2 communication.

IoCs:
Malicious documents:
- 265f407a157ab0ed017dd18cae0352ae
- 7a73a2261e20bdb8d24a4fb252801db7
- 7a307c57ec33a23ce9b5c84659f133cc
- ced38b728470c63abcf4db013b09cff7
- 9121f1c13955506e33894ffd780940cd
- 50b2154de64724a2a930904354b5d77d
- 8a05f6b3f1eb25bcbceb717aa49999cd
- ee73a772b72a5f3393d4bf577fc48efe

Downloader:
- d1c652b4192857cb08907f0ba1790976
- 25b37c971fd7e9e50e45691aa86e5f0a
- 0493f40628995ae1b7e3ffacd675ba5f
- 8840f6d2175683c7ed8ac2333c78451a
- c278d6468896af3699e058786a8c3d62
- 9fd35bad075c2c70678c65c788b91bc3
- 59cb8474930ae7ea45b626443e01b66d
- 7af59d16cfd0802144795ca496e8111c
- cd5357d1045948ba62710ad8128ae282
- 77194024294f4fd7a4011737861cce3c
- e9d89d1364bd73327e266d673d6c8acf
- 0d4bdfec1e657d6c6260c42ffdbb8cab
- 5da86adeec6ce4556f477d9795e73e90
- 706e55af384e1d8483d2748107cbd57c

Manipulated Installer:
- dd185e2bb02b21e59fb958a4e12689a7

Installer:
- 4088946632e75498d9c478da782aa880

Injector:
- dc9244206e72a04d30eeadef23713778

Backdoor:
- 735afcd0f6821cbd3a2db510ea8feb22

Fetched template:
- 2efbe6901fc3f479bc32aaf13ce8cf12
- 65df11dea0c1d0f0304b376787e65ccb
- 43.dotm
- 0071b20d27a24ae1e474145b8efc9718
- 17.dotm
- 1f254dd0b85edd7e11339681979e3ad6
- 61.dotm

DeathNote downloader:
- f4b55da7870e9ecd5f3f565f40490996
- 2b02465b65024336a9e15d7f34c1f5d9
- 11fdc0be9d85b4ff1faf5ca33cc272ed
- f6d6f3580160cd29b285edf7d0c647ce
- 78d42cedb0c012c62ef5be620c200d43
- 92657b98c2b4ee4e8fa1b83921003c74
- 075fba0c098d86d9f22b8ea8c3033207
- 8fc7b0764541225e5505fa93a7376df4
- 7d204793e75bb49d857bf4dbc60792d3
- ca6658852480c70118feba12eb1be880
- c0a8483b836efdbae190cc069129d5c3
- 14d79cd918b4f610c1a6d43cadeeff7b
- 1bd0ca304cdecfa3bd4342b261285a72

Trojanized PDF viewer:
- cbc559ea38d940bf0b8307761ee4d67b
- da1dc5d41de5f241cabd7f79fbc407f5

BLINDINGCAN:
- b23b0de308e55cbf14179d59adee5fcb
- 64e5acf43613cd10e96174f36cb1d680

COPPERHEDGE Loader:
- a43bdc197d6a273102e90cdc0983b0b9
- 97336f5ce811d76b28e23280fa7320b5

Racket Downloader:
- b3a8c88297daecdb9b0ac54a3c107797
- b974bc9e6f375f301ae2f75d1e8b6783

Stealer:
- fe549a0185813e4e624104d857f9277b

Backdoor Loader:
- 7b8960e2a22c8321789f107a7b83aa59
- 0ac90c7ad1be57f705e3c42380cbcccd

Mimikatz Loader:
- adf0d4bbefccf342493e02538155e611
- d4d654c1b27ab90d2af8585052c77f33

ForestTiger (Backdoor):
- 97524091ac21c327bc783fa5ffe9cd66
- 9b09ebf52660a9d6deca21965ce52ca1

Trojanized PDF reader:
- 84cd4d896748e2d52e2e22d1a4b9ee46

No more IoCs found.
