# BlueNoroff  How DPRK’s macOS RustBucket Seeks to Evade Analysis and Detection

**Incident:** BlueNoroff | DPRK’s macOS RustBucket Malware Campaign

**Root cause:** Multi-stage malware campaign targeting macOS users with sophisticated evasion and detection techniques.

**Impact:** The impact of the RustBucket campaign includes the compromise of an unspecified number of macOS devices. The exact financial losses and number of individuals or organizations affected were not detailed in the report.

**Mitigation:** 
- **User Education and Awareness:** Train users to recognize and avoid phishing and social engineering tactics that could lead to the execution of malicious payloads.
- **Endpoint Protection:** Deploy advanced endpoint protection solutions like SentinelOne to detect and block malware attempts dynamically.
- **Regular Updates and Patching:** Ensure all systems and software are up-to-date with the latest security patches to mitigate vulnerabilities that malware might exploit.
- **Restrict Permissions:** Limit user permissions to prevent unauthorized changes to critical system directories.
- **Network Segmentation:** Implement network segmentation to limit the spread of malware within the organization.
- **Monitor and Analyze Logs:** Regularly monitor and analyze system logs for unusual activities or indicators of compromise (IoCs).
- **Incident Response Plan:** Have a robust incident response plan in place to quickly address and mitigate malware infections.

**Detailed Steps for Mitigation:**
1. **User Education:** Conduct regular training sessions and phishing simulation exercises to educate users about common tactics used by attackers.
2. **Deploy Endpoint Protection:**
   - Install and configure advanced endpoint protection tools such as SentinelOne to provide real-time protection and behavior analysis.
3. **Regular Software Updates:**
   - Schedule and enforce regular updates and patches for all software and operating systems.
4. **Permission Management:**
   - Implement least privilege access controls and regularly review user permissions.
5. **Network Security:**
   - Design network architecture with segmentation to contain the spread of potential infections.
6. **Log Monitoring:**
   - Set up centralized log management and SIEM systems to detect and alert on suspicious activities.
7. **Incident Response:**
   - Develop and test an incident response plan, ensuring quick isolation and remediation of infected systems.

**Detection Signature:**
- **Service:** macOS
- **Port:** N/A (focus is on malware behavior rather than a specific service port)
- **Severity:** Critical
- **Incident:** RustBucket Malware Campaign
- **Signature name:** “RustBucket multi-stage malware detection”
- **Internal checks:**
  - **Setting1:** Monitor for execution of AppleScript (.app) files that lack user interfaces.
  - **Setting2:** Detect and alert on the creation of hidden files in the `/Users/Shared/` directory.
  - **Setting3:** Monitor for shell commands that download and execute files from unknown sources.
- **External scanning:**
  - **Indicator:** Presence of known malicious hashes for RustBucket variants.
  - **Behavior:** Detect anomalous network traffic patterns indicative of command-and-control communication.

**IoCs:**
- **Hashes:**
  - Stage 2 Mach-Os: 
    - 0df7e1d3b3d54336d986574441778c827ff84bf2, 
    - 27b101707b958139c32388eb4fd79fcd133ed880,
    - 338af1d91b846f2238d5a518f951050f90693488, 
    - 5304031dc990790a26184b05b3019b2c5fa7022a, 
    - 72167ec09d62cdfb04698c3f96a6131dceb24a9c,
    - 7f9694b46227a8ebc67745e533bc0c5f38fdfa59, 
    - 963a86aab1e450b03d51628797572fe9da8410a2, 
    - 9676f0758c8e8d0e0d203c75b922bcd0aeaa0873, 
    - a7f5bf893efa3f6b489efe24195c05ff87585fe3,
    - ac08406818bbf4fe24ea04bfd72f747c89174bdb, 
    - acf1b5b47789badb519ff60dc93afa9e43bbb376,
    - b02922869e86ad06ff6380e8ec0be8db38f5002b,
    - d5971e8a3e8577dbb6f5a9aad248c842a33e7a26, 
    - e0e42ac374443500c236721341612865cd3d1eec, 
    - e275deb68cdff336cb4175819a09dbaf0e1b68f6,
    - ed4f16b36bc47a701814b63e30d8ea7a226ca906,
    - fd1cef5abe3e0c275671916a1f3a566f13489416
  - Stage 3 Version A Mach-Os:
    - 182760cbe11fa0316abfb8b7b00b63f83159f5aa, 
    - 3cc19cef767dee93588525c74fe9c1f1bf6f8007,
    - 831dc7bc4a234907d94a889bcb60b7bedf1a1e13,
    - 8e7b4a0d9a73ec891edf5b2839602ccab4af5bdf
  - Stage 3 Version B Mach-Os:
    - 14165777bc48b49eb1fa9ad8fe3cb553565c26c2,
    - 69f24956fb75beb9b93ef974d873914500e35601,
    - 8a1b32ab8c2a889985e530425ae00f4428c575cc,
    - 8f7da0348001461fc5a1da99b89c571050de0aff,
    - a973d201c23b68c5d25ba8447b04f090c20bf6d4,
    - b74702c9b82f23ebf76805f1853bc72236bee57c,
    - cd8f41b91e8f1d8625e076f0a161e46e32c62bbf
  - Malicious PDFs:
    - 469236d0054a270e117a2621f70f2a494e7fb823,
    - 574bbb76ef147b95dfdf11069aaaa90df968e542,
    - 7e69cb4f9c37fad13de85e91b5a05a816d14f490,
    - 7f8f43326f1ce505a8cd9f469a2ded81fa5c81be,
    - be234cb6819039d6a1d3b1a205b9f74b6935bbcc,
    - e7158bb75adf27262ec3b0f2ca73c802a6222379
  - Stage 1 Applications (.zip):
    - 0738687206a88ecbee176e05e0518effa4ca4166,
    - 0be69bb9836b2a266bfd9a8b93bb412b6e4ce1be,
    - 5933f1a20117d48985b60b10b5e42416ac00e018,
    - 7a5d57c7e2b0c8ab7d60f7a7c7f4649f33fea8aa,
    - 7e1870a5b24c78a5e357568969aae3a5e7ab857d,
    - 89301dfdc5361f1650796fecdac30b7d86c65122,
    - 9121509d674091ce1f5f30e9a372b5dcf9bcd257,
    - 9a5f6a641cc170435f52c6a759709a62ad5757c7,
    - a1a85cba1bc4ac9f6eafc548b1454f57b4dff7e0,
    - ca59874172660e6180af2815c3a42c85169aa0b2,
    - d9f1392fb7ed010a0ecc4f819782c179efde9687,
    - e2bcdfbda85c55a4d6070c18723ba4adb7631807
  - AppleScript main.scpt:
    - dabb4372050264f389b8adcf239366860662ac52

- **Domains:**
  - cloud[.]dnx.capital
  - crypto.hondchain[.]com

- **File Paths:**
  - $TMPDIR/ErrorCheck.zip
  - /Users/Shared/1.zip
  - /Users/Shared/Internal PDF Viewer.app
  - /Users/Shared/.pd
  - ~/Library/Metadata/System Update
  - ~/Library/LaunchAgents/com.apple.systemupdate.plist
