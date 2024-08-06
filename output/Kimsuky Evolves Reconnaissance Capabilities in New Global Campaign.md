# Kimsuky Evolves Reconnaissance Capabilities in New Global Campaign

Incident: Kimsuky ReconShark Attack

Root cause: Spear-phishing emails leading to the download and execution of malicious macros in Microsoft Office documents.

Impact: The blog does not specify the exact number of devices or people impacted, nor does it provide details regarding financial losses.

Mitigation: 
1. Educate employees on recognizing and handling phishing emails.
2. Implement email filtering solutions to block malicious emails.
3. Disable macros in Microsoft Office by default.
4. Use endpoint protection to detect and block malicious activity.
5. Regularly update and patch software to minimize vulnerabilities.

Detailed Steps for mitigation:
1. **Employee Training:** Conduct regular training sessions to educate employees on identifying phishing emails and the dangers of opening attachments or links from unknown sources.
2. **Email Filtering:** Utilize advanced email filtering solutions that can detect and block phishing emails before they reach the end user. Solutions like SPF, DKIM, and DMARC can help verify email sources.
3. **Macro Settings:** Configure Microsoft Office to disable macros by default. Only allow macros to run from trusted locations or signed by trusted publishers.
4. **Endpoint Protection:** Deploy endpoint detection and response (EDR) solutions that can monitor and analyze endpoint activities to detect malicious behavior. Ensure these solutions are configured to block the execution of known malicious macros.
5. **Software Patching:** Implement a robust patch management process to ensure all software, especially Microsoft Office and operating systems, are up-to-date with the latest security patches.

Detection Signature:
Service: Microsoft Office (Word, Excel, etc.)
Port: Not applicable (local execution of macros)
Severity: Critical
Incident: Kimsuky ReconShark Attack
Signature name: “Malicious macro execution in Microsoft Office”
Internal checks:
   - Setting1: Macros should be disabled by default in Microsoft Office applications.
   - Setting2: Only allow macros from trusted locations or signed by trusted publishers.
   - Setting3: Monitor for the creation and execution of suspicious scripts (e.g., VBS, HTA, Batch) from Office files.
External scanning:
   - Not applicable

IoCs:
   - Domains: yonsei[.]lol, rfa[.]ink, mitmail[.]tech, newshare[.]online
   - URLs: Various endpoints listed in the blog (e.g., https[:]//rfa[.]ink/bio/r.php)
   - SHA1 Hashes: 86a025e282495584eabece67e4e2a43dca28e505 (Lure Doc), c8f54cb73c240a1904030eb36bb2baa7db6aeb01 (Macro)

The document provides a comprehensive list of IoCs, including specific URLs and domains used for command and control and payload delivery.
