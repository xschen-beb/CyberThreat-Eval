Source: [https://www.reliaquest.com/blog/gootloader-infection-credential-access/](https://www.reliaquest.com/blog/gootloader-infection-credential-access/)

# Goot to Loot—How a Gootloader Infection Led to Credential Access - ReliaQuest

**Incident:** Gootloader Infection Leading to Credential Access

**Root cause:** Initial access via SEO poisoning and execution of malicious JavaScript files.

**Impact:** Potential unauthorized access to sensitive credentials and data exfiltration. Specific financial losses and the number of impacted devices/people are not detailed in the report.

**Mitigation:** 
1. **User Awareness Training:** Educate employees on the risks of clicking on suspicious links and the importance of verifying the source of information.
2. **Endpoint Protection:** Ensure endpoint detection and response (EDR) systems are in place and capable of detecting and mitigating such malware.
3. **Network Segmentation:** Segment critical systems to limit lateral movement within the network.
4. **Regular Patching:** Keep systems and applications up to date with the latest security patches.
5. **Disable Unnecessary Services:** Disable services like Windows Script Host (wscript.exe) if not required.
6. **Monitoring and Logging:** Implement robust logging and monitoring solutions to detect unusual activities promptly.

**Detailed Steps for Mitigation:**
1. **Educate Users:**
    - Conduct regular training sessions on phishing and SEO poisoning tactics.
    - Encourage users to report suspicious activities.
2. **Implement Endpoint Protection:**
    - Deploy advanced EDR solutions across all endpoints.
    - Regularly update EDR signatures and ensure proper configuration.
3. **Network Segmentation:**
    - Isolate critical systems from the rest of the network.
    - Use firewalls and access controls to limit access to sensitive areas.
4. **Apply Security Patches:**
    - Regularly update operating systems and applications.
    - Automate the update process where possible.
5. **Disable Unnecessary Services:**
    - Evaluate the necessity of services like wscript.exe in your environment.
    - Disable or restrict access to such services if not required.
6. **Enhance Monitoring and Logging:**
    - Implement SIEM solutions to aggregate and analyze logs.
    - Regularly review logs for signs of compromise.

**Detection Signature:**
- **Service:** Windows Script Host (wscript.exe)
- **Port:** N/A (executed locally)
- **Severity:** Critical
- **Incident:** Gootloader Infection Leading to Credential Access
- **Signature name:** “Suspicious Wscript Execution”
- **Internal checks:**
    - **Setting1:** Monitor execution of wscript.exe and cscript.exe.
    - **Setting2:** Alert on the creation of scheduled tasks with unusual names.
    - **Setting3:** Detect PowerShell commands executing Base64 encoded payloads.
- **External scanning:**
    - **Port:** N/A (focus on internal telemetry)
    - **Indicators:** Unusual scheduled tasks, Base64 encoded PowerShell commands, and network connections to known malicious domains.

**IoCs:**
- **IPs:**
    - 94[.]156[.]189[.]36
    - 217[.]145[.]84[.]64
    - 167[.]172[.]154[.]244
    - 66[.]33[.]211[.]237
- **Domains:**
    - salamancaespectacular[.]com/what-is-the-difference-between-legal-ruled-and-wide-ruled-paper
    - hxxps://emailbuilder[.]a6uat[.]co[.]uk/download[.]php
    - hxxps://wildlife[.]org/xmlrpc[.]php
    - hxxps://spinomenal[.]com/xmlrpc[.]php
    - hxxps://airjust[.]de/xmlrpc[.]php
    - hxxps://maharat-rt[.]com/xmlrpc[.]php
    - hxxps://jocarsa[.]com/xmlrpc[.]php
    - hxxp://ddman-vpn.ddns[.]net/wordpress/xmlrpc[.]php
    - hxxps://gahar[.]ir/xmlrpc[.]php
    - hxxps://anevaz[.]com[.]br/xmlrpc[.]php
    - hxxps://pornmagazine[.]club/xmlrpc[.]php
    - hxxps://phone[.]do/xmlrpc[.]php
    - hxxps://demo[.]petsure[.]com/xmlrpc[.]php
    - hxxps://docs[.]vrent[.]techvill[.]net/xmlrpc[.]php
    - cacommerciallaw[.]com
    - eu9[.]richhost[.]eu
- **Files:**
    - Lead-based Paint[.]js
    - what is the difference between legal ruled and wide ruled paper 29094[.]js
    - What
