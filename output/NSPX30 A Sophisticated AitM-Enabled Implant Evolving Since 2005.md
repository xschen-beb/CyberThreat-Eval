# NSPX30 A Sophisticated AitM-Enabled Implant Evolving Since 2005

Incident: NSPX30 Adversary-in-the-Middle Attack

Root cause: Deployment of a sophisticated AitM-enabled implant (NSPX30) through hijacked update mechanisms of legitimate software.

Impact: The specific number of records or financial losses is not mentioned, but the incident impacted multiple devices and individuals, including:
- Unidentified individuals in China, Japan, and the United Kingdom.
- A high-profile public research university in the United Kingdom.
- A large manufacturing and trading company in China.
- The office in China of a Japanese corporation in the engineering and manufacturing vertical.

Mitigation: To mitigate a similar incident, follow these detailed steps:
1. **Secure Software Update Mechanisms**:
   - Ensure all software updates are transferred over encrypted channels (e.g., HTTPS).
   - Implement digital signatures for software updates to verify their authenticity.
2. **Network Security**:
   - Monitor and secure network appliances like routers and gateways against vulnerabilities.
   - Regularly update firmware and apply patches to network devices.
3. **Endpoint Security**:
   - Deploy endpoint protection solutions that can detect and block suspicious activities related to packet interception.
   - Implement and enforce the use of application whitelisting to prevent unauthorized software from executing.
4. **User Awareness and Training**:
   - Educate users about the risks of AitM attacks and the importance of verifying update sources.
5. **Regular Audits and Monitoring**:
   - Conduct regular security audits of your network and systems to identify potential vulnerabilities.
   - Monitor network traffic for unusual patterns that may indicate packet interception or other malicious activities.
6. **Incident Response Plan**:
   - Develop and maintain an incident response plan to quickly address and mitigate any detected intrusions or compromises.

Detection Signature:
   - **Service**: Legitimate software update mechanisms like Tencent QQ, WPS Office, Sogou Pinyin
   - **Port**: Varies (commonly HTTP/HTTPS ports like 80, 443)
   - **Severity**: Critical
   - **Incident**: NSPX30 Adversary-in-the-Middle Attack
   - **Signature name**: “NSPX30 deployment via hijacked updates”
   - **Internal checks**:
     - Setting1: Ensure all software updates are fetched over HTTPS.
     - Setting2: Verify the integrity of downloaded update files using digital signatures.
     - Setting3: Monitor endpoint activities for suspicious network requests and file executions.
   - **External scanning**:
     - Monitor network traffic for unencrypted HTTP requests that should be using HTTPS.
     - Identify and alert on responses to update requests that do not match expected patterns (e.g., unexpected payloads).

IoCs:
- **Files**:
  - SHA-1: 625BEF5BD68F75624887D732538B7B01E3507234 (minibrowser_shell.dll)
  - SHA-1: 43622B9573413E17985B3A95CBE18CFE01FADF42 (comx3.dll)
  - SHA-1: 240055AA125BD31BF5BA23D6C30133C5121147A5 (msnsp.dll)
  - SHA-1: 308616371B9FF5830DFFC740318FD6BA4260D032 (mshlp.dll)
  - SHA-1: 796D05F299F11F1D78FBBB3F6E1F497BC3325164 (comx3.dll.txt)
  - SHA-1: 82295E138E89F37DD0E51B1723775CBE33D26475 (WIN.cfg)
  - SHA-1: 44F50A81DEBF68F4183EAEBC08A2A4CD6033DD91 (msfmtkl.dat)
  - SHA-1: DB6AEC90367203CAAC9D9321FDE2A7F2FE2A0FB6 (c001.dat)
  - SHA-1: 9D74FE1862AABAE67F9F2127E32B6EFA1BC592E9 (c002.dat)
  - SHA-1: 8296A8E41272767D80DF694152B9C26B607D26EE (c003.dat)
  - SHA-1: 8936BD9A615DD859E868448CABCD2C6A72888952 (a010.dat)
  - SHA-1: AF85D79BC16B691F842964938C9619FFD1810C30 (b011.dat)
  - SHA-1: ACD6CD486A260F84584C9FF7409331C65D4A2F4A (b010.dat)
- **Network**:
  - IP: 104.193.88[.]123 (www.baidu[.]com)
  - IP: 183.134.93[.]171 (dl_dir.qq[.]com)

MITRE ATT&CK techniques:
- T1587.001: Develop Capabilities: Malware
- T1195: Supply Chain Compromise
- T1059.001: Command and Scripting Interpreter: PowerShell
- T1059.003: Command and Scripting Interpreter: Windows Command Shell
- T1059.005: Command and Scripting Interpreter: Visual Basic
- T1106: Native API
- T1574: Hijack Execution Flow
- T1546: Event Triggered Execution
- T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- T1140: Deobfuscate/Decode Files or Information
- T1562.001: Impair Defenses: Disable or Modify Tools
- T1070.004: Indicator Removal: File Deletion
- T1070.009: Indicator Removal: Clear Persistence
- T1202: Indirect Command Execution
- T1036.005: Masquerading: Match Legitimate Name or Location
- T1112: Modify Registry
- T1027: Obfuscated Files or Information
- T1027.009: Obfuscated Files or Information: Embedded Payloads
- T1218.011: System Binary Proxy Execution: Rundll32
- T1557: Adversary-in-the-Middle
- T1555: Credentials from Password Stores
- T1083: File and Directory Discovery
- T1012: Query Registry
- T1518: Software Discovery
- T1082: System Information Discovery
- T1016: System Network Configuration Discovery
- T1049: System Network Connections Discovery
- T1033: System Owner/User Discovery
- T1056.001: Input Capture: Keylogging
- T1560.002: Archive Collected Data: Archive via Library
- T1123: Audio Capture
- T1119: Automated Collection
- T1074.001: Data Staged: Local Data Staging
- T1113: Screen Capture
- T1071.001: Application Layer Protocol: Web Protocols
- T1071.004: Application Layer Protocol: DNS
- T1132.001: Data Encoding: Standard Encoding
- T1001: Data Obfuscation
- T1095: Non-Application Layer Protocol
- T1090: Proxy
- T1020: Automated Exfiltration
- T1030: Data Transfer Size Limits
- T1048.003: Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted Non-C2 Protocol

No additional IoCs found in the document.
