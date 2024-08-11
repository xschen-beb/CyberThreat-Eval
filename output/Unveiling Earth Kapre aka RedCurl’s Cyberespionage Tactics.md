Source: [https://www.trendmicro.com/en_us/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html](https://www.trendmicro.com/en_us/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)

# Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics

Incident: Earth Kapre Cyberespionage Campaign

Root cause: Unauthorized execution of malicious code through the abuse of legitimate tools (PowerShell, curl, and Program Compatibility Assistant).

Impact: Numerous machines across multiple countries were infected, leading to potential data theft. Financial losses could vary depending on the nature and sensitivity of the stolen data and the cost of incident response and mitigation measures.

Mitigation: Implement comprehensive endpoint protection and monitoring, secure email gateways, and restrict the use of potentially abused tools.

Detailed Steps for mitigation:
1. **Endpoint Protection:**
   - Deploy advanced endpoint protection solutions like Trend Micro Apex One™ to detect and block malicious activities and fileless threats.
   
2. **Email Security:**
   - Use Trend Micro™ Deep Discovery™ Email Inspector to filter out phishing emails and malicious attachments before they reach users.
   
3. **Network Monitoring:**
   - Employ network intrusion detection systems (NIDS) to monitor for unusual outbound traffic and communications with known malicious IPs.
   
4. **Restrict Tool Usage:**
   - Limit the use of tools like PowerShell and curl to authenticated and authorized personnel only. Implement application whitelisting to prevent unauthorized execution of these tools.
   
5. **Patch Management:**
   - Regularly update and patch systems to fix known vulnerabilities that could be exploited by attackers.

6. **User Training:**
   - Conduct regular cybersecurity training for employees to recognize and avoid phishing attempts.

Detection Signature:
   Service: Windows operating system
   Port: 445 (SMB)
   Severity: Critical
   Incident: Earth Kapre Cyberespionage Campaign
   Signature name: “Suspicious PowerShell and Curl Activity”
   
   Internal checks:
       - Setting1: Monitor execution of PowerShell and curl commands. – Inside VMs
       - Setting2: Detect and alert on the creation of scheduled tasks by unauthorized users. – Inside VMs
       - Setting3: Monitor registry changes indicating Impacket SMB activity. – Inside VMs
   
   External scanning:
       - Detect outbound SMB connections, especially to unusual external IPs.
       - Monitor for HTTP requests to known malicious domains.

IoCs: 
- Domains:
  - preston[.]melaniebest[.]com
  - preslive[.]cn[.]alphastoned.pro
  - unipreg[.]tumsun[.]com
  - report[.]hkieca[.]com
- IPs:
  - 23[.]254[.]224[.]79
  - 198[.]252[.]101[.]86
- File paths:
  - C:\Windows\System32\ms.dll
  - C:\Windows\System32\ps.dll
  - C:\Users\<username>\AppData\Roaming\MUIService\pythonw.exe
  - C:\Windows\system32\config\systemprofile\AppData\Local\*.exe

By following these steps, organizations can bolster their defenses against similar cyberespionage campaigns and reduce the risk of data breaches.
