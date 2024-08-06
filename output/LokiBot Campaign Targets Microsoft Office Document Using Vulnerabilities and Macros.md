# LokiBot Campaign Targets Microsoft Office Document Using Vulnerabilities and Macros

Incident: LokiBot Campaign Targets Microsoft Office Document

Root cause: Exploitation of known vulnerabilities (CVE-2021-40444 and CVE-2022-30190) and malicious macros in Microsoft Office documents.

Impact: Control and collection of sensitive information from victim’s Windows devices. The exact number of impacted devices and financial losses are not specified.

Mitigation: 
1. Patch and update all Microsoft Office applications to the latest versions to mitigate known vulnerabilities like CVE-2021-40444 and CVE-2022-30190.
2. Disable macros in Microsoft Office by default and only enable them for trusted documents.
3. Implement robust email filtering and scanning solutions to detect and block malicious attachments.
4. Educate users about the risks of opening attachments from unknown or untrusted sources.
5. Use endpoint protection solutions to detect and block malware such as LokiBot.
6. Regularly update antivirus definitions and use advanced threat protection services.

Detailed Steps for mitigation:
1. **Patch Management**:
   - Ensure all systems are updated with the latest security patches, especially for Microsoft Office applications.
   - Use automated patch management solutions to keep software up-to-date.

2. **Macro Security**:
   - Open Microsoft Office applications.
   - Go to File > Options > Trust Center > Trust Center Settings.
   - Select "Macro Settings" and choose "Disable all macros with notification" or "Disable all macros except digitally signed macros."

3. **Email Filtering**:
   - Implement advanced email security solutions to scan attachments and links for malicious content.
   - Use sandboxing technology to analyze suspicious attachments in a controlled environment.

4. **User Education**:
   - Conduct regular training sessions to educate users about phishing and the dangers of opening attachments from unknown sources.
   - Provide guidelines on how to recognize suspicious emails and report them to the IT department.

5. **Endpoint Protection**:
   - Deploy endpoint protection solutions across all devices in the network.
   - Configure the solutions to automatically update and perform regular scans.

6. **Advanced Threat Protection**:
   - Use services like FortiGuard to block known malicious IPs, domains, and files.
   - Regularly review threat intelligence feeds to stay updated on new threats.

Detection Signature:
   Service: Microsoft Office
   Port: N/A (exploited via document vulnerabilities and macros)
   Severity: Critical
   Incident: LokiBot Campaign
   Signature name: “Malicious Office Document Vulnerability Exploits”
   Internal checks:
       - Setting1: Ensure that all Microsoft Office applications are updated to the latest versions.
       - Setting2: Macros should be disabled by default in all Office applications.
       - Setting3: Implement and enforce email filtering policies.
   External scanning:
       - Scan for known malicious attachments and links in incoming emails.
       - Monitor network traffic for connections to known malicious C2 servers.

IoCs:
   - C2: 95[.]164[.]23[.]2
   - Files:
     - 17d95ec93678b0a73e984354f55312dda9e6ae4b57a54e6d57eb59bcbbe3c382
     - 23982d2d2501cfe1eb931aa83a4d8dfe922bce06e9c327a9936a54a2c6d409ae
     - 9eaf7231579ab0cb65794043affb10ae8e4ad8f79ec108b5302da2f363b77c93
     - da18e6dcefe5e3dac076517ac2ba3fd449b6a768d9ce120fe5fc8d6050e09c55
     - 2e3e5642106ffbde1596a2335eda84e1c48de0bf4a5872f94ae5ee4f7bffda39
     - 80f4803c1ae286005a64ad790ae2d9f7e8294c6e436b7c686bd91257efbaa1e5
     - 21675edce1fdabfee96407ac2683bcad0064c3117ef14a4333e564be6adf0539
     - 4a23054c2241e20aec97c9b0937a37f63c30e321be01398977e13228fa980f29
