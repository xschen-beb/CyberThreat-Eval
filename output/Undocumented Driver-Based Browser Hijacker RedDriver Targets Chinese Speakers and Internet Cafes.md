# Undocumented Driver-Based Browser Hijacker RedDriver Targets Chinese Speakers and Internet Cafes

Incident: RedDriver Browser Hijacker Targeting Chinese Speakers

Root cause: Exploitation of the Windows Filtering Platform (WFP) via an undocumented malicious driver (RedDriver) that uses HookSignTool to bypass driver-signing policies.

Impact: The exact number of devices and people affected are not mentioned in the blog, but it appears to target Chinese-speaking users and internet cafes, potentially affecting a significant number of users in that demographic. Financial losses are not detailed.

Mitigation: Implement multiple layers of security controls to prevent the execution and spread of malicious drivers like RedDriver.

Detailed Steps for mitigation:
1. **Endpoint Protection**:
   - Deploy advanced endpoint protection solutions like Cisco Secure Endpoint to detect and prevent the execution of suspicious drivers.
   - Regularly update antivirus and anti-malware solutions to recognize and block known threats.

2. **Network Security**:
   - Utilize network security appliances like Cisco Secure Firewall to monitor and block malicious traffic.
   - Implement strict network segmentation to limit the spread of malware within the network.

3. **Certificate Management**:
   - Revoke and monitor certificates used for driver signing to prevent misuse.
   - Educate development teams about the risks of using forged certificates.

4. **System Hardening**:
   - Ensure that systems are configured to enforce strict driver-signing policies.
   - Regularly apply security patches and updates to all systems and software.

5. **User Education and Awareness**:
   - Educate users, especially those in internet cafes, about the risks of downloading and executing untrusted software.
   - Encourage the use of multi-factor authentication (MFA) to secure user accounts.

6. **Incident Response Preparedness**:
   - Establish an incident response plan to quickly identify and mitigate threats.
   - Conduct regular security audits and penetration testing to identify and address vulnerabilities.

Detection Signature:
   Service: Windows Filtering Platform (WFP)
   Port: N/A
   Severity: Critical
   Incident: RedDriver Browser Hijacker
   Signature name: “RedDriver detection”
   Internal checks:
      - Setting1: Ensure that only signed drivers are allowed to run.
      - Setting2: Monitor for the presence of suspicious drivers and certificates.
      - Setting3: Enforce strict driver-signing policies within the operating system.
   External scanning:
      - Monitor network traffic for unusual patterns or connections to known C2 domains.
      - Scan for the presence of root certificates silently installed by malicious drivers.

IoCs:
   - Domains:
     - poilcy[.]itosha[.]top
     - newport[.]tofu77[.]top
     - workpoilcy.zhedwe[.]top
     - reserve.itosha[.]top
     - file[.]zhedwe[.]top
     - red[.]zhedwe[.]top
     - aireport[.]umpteen[.]top
     - q5y2qclsk18[.]malaji[.]top
     - laomao[.]run

   - IP addresses:
     - 47.109.63.172
     - 8.137.97.186
     - 47.109.66.222
     - 47.109.33.213
     - 103.91.208.32
     - 47.109.73.113
     - 47.108.76.161
     - 47.108.64.162

   - File hashes:
     - DnfClientShell32 - 5a13091832ef2fd837c33acb44b97c37d4f1f412f31f093faf0ce83dcd7c314e
     - DnfClient - 9e59eba805c361820d39273337de070efaf2bf804c6ea88bbafc5f63ce3028b1
     - ReflectiveLoader32 - c96320c7b57adf6f73ceaf2ae68f1661c2bfab9d96ffd820e3cfc191fcdf0a9b
