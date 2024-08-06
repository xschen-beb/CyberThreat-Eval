# Infected Text Editors Load Backdoor into MacOS

Incident: Infected Text Editors Load Backdoor into macOS

Root cause: Malvertising leading to the download of compromised text editor installers that included backdoor payloads.

Impact: Users downloading the infected versions of Notepad++ and VNote from the malicious links on the search engine were impacted. The exact number of users and financial losses are not provided in the blog.

Mitigation: 
1. **Avoid downloading software from search engine ads**: Users should always download software from the official website of the software vendor rather than through ads or search results.
2. **Verify the download source**: Always check the URL to ensure it matches the official site.
3. **Use security software**: Employ reputable security software to detect and block malicious downloads and backdoors.
4. **Update and patch software**: Regularly update all software to the latest versions to mitigate vulnerabilities.
5. **Educate users**: Provide awareness training to users about the risks of downloading software from unverified sources.

Detailed Steps for mitigation:
1. **Implement DNS Filtering**: Use DNS filtering solutions to block access to known malicious domains such as `vnote-1321786806[.]cos[.]ap-hongkong[.]myqcloud[.]com`, `dns[.]transferusee[.]com`, and `update[.]transferusee[.]com`.
2. **Enforce Application Whitelisting**: Only allow the execution of applications that are pre-approved, blocking unknown or unauthorized software.
3. **Conduct Regular Audits and Scans**: Perform regular vulnerability assessments and malware scans on systems to detect and mitigate threats.
4. **Deploy Endpoint Detection and Response (EDR)**: Use EDR solutions to monitor and respond to suspicious activities on endpoints.
5. **Secure Software Supply Chain**: Ensure that all software vendors follow secure development practices and provide checksums or signed binaries that users can verify.

Detection Signature:
- **Service**: HTTP(S) server
- **Port**: 80, 443
- **Severity**: Critical
- **Incident**: Malvertising leading to backdoor installation
- **Signature name**: “Malicious software download link”
- **Internal checks**:
    - Setting1: Ensure that endpoints do not download executables from unverified sources. – Inside VMs
    - Setting2: Implement application control to block execution of unknown binaries. – Inside VMs
    - Setting3: Conduct DNS filtering to block access to known malicious domains. – In platform
- **External scanning**:
    - Port (80, 443) open on malicious domains
    - HTTP(S) requests to known malicious URLs

IoCs:
- MD5 Hashes:
    - 43447f4c2499b1ad258371adff4f503f (DPysMac64)
    - 00fb77b83b8ab13461ea9dd27073f54f (Notepad‐‐v2.0.0-mac_x64_12.3.dmg)
    - 5ece6281d57f16d6ae773a16f83568db (Notepad‐‐-x86_64.AppImage)
    - 6ace1e014863eee67ab1d2d17a33d146 (NotePad‐‐)
    - 47c9fec1a949e160937dd9f9457ec689 (NotePad‐‐)
- Domains:
    - dns[.]transferusee[.]com
    - update[.]transferusee[.]com/onl/mac/
    - update[.]transferusee[.]com/onl/lnx/
    - update[.]transferusee[.]com/DPysMac64
    - update[.]transferusee[.]com/DPysMacM1
    - vnote[.]info
    - vnote[.]fuwenkeji[.]cn
    - vnotepad[.]com
    - vnote-1321786806[.]cos[.]ap-hongkong[.]myqcloud[.]com

This detailed analysis and mitigation plan should help in securing systems against similar threats in the future.
