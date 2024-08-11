Source: [https://news.sophos.com/en-us/2023/07/26/into-the-tank-with-nitrogen/](https://news.sophos.com/en-us/2023/07/26/into-the-tank-with-nitrogen/)

# Into the Tank with Nitrogen

Incident: Nitrogen Initial Access Malware Campaign

Root cause: Malicious advertising (malvertising) and impersonation of legitimate software distribution sites

Impact: Several organizations in the technology and non-profit sectors in North America were targeted. The financial losses and number of devices or people impacted are not specified in the document.

Mitigation: 
1. **Secure Browsing Practices:**
   - Use ad-blocking extensions or run browsers with built-in ad-blocking capabilities.
   - Opt for ad-blockers that block “non-intrusive advertising.”

2. **Restrict Mounting Virtual File Systems:**
   - Consider restricting the capability to mount virtual file systems via Group Policy Objects (GPO).
   - Disable auto-mounting of disk image files such as .iso files.

3. **Awareness and Training:**
   - Educate users about suspicious websites and phishing indicators, such as urgency, misspellings, and poor grammar.
   
4. **Credential Management:**
   - Avoid storing credentials within the Registry.
   - Ensure that any stored credentials have limited permissions.

5. **Enhanced Detection Solutions:**
   - Implement comprehensive detection solutions to identify unauthorized access and follow-on activity.
   - Utilize memory detections for Cobalt Strike components to flag further compromise tactics.

Detailed Steps for Mitigation:
1. **Ad-blocking Configuration:**
   - Install an ad-blocker like uBlock Origin or use browser-integrated ad-blocking features.
   - Configure the ad-blocker to block intrusive ads.

2. **Group Policy Configuration:**
   - Open Group Policy Management Console (GPMC).
   - Navigate to User Configuration > Administrative Templates > System > Removable Storage Access.
   - Enable the policy “Deny write access to removable storage devices.”

3. **User Training Programs:**
   - Develop and execute phishing awareness training.
   - Periodically send simulated phishing emails to test and improve user vigilance.

4. **Registry Credential Search:**
   - Use scripts or tools like `reg query` to search for sensitive information stored in the Registry.
   - Regularly audit and clean up any discovered credentials.

5. **Detection and Response Enhancement:**
   - Deploy advanced endpoint protection solutions like Sophos Intercept X.
   - Regularly update threat intelligence feeds and detection rules.
   - Conduct regular penetration tests and vulnerability assessments.

Detection Signature:
   Service: Python Package (specifically trojanized versions)
   Port: Various (depends on C2 communication protocols - TCP, TCP over SSL, HTTP, HTTPS)
   Severity: Critical
   Incident: Nitrogen Initial Access Campaign
   Signature name: “Nitrogen package installation and C2 communication”
   Internal checks:
      - Setting1: Monitor for suspicious Python package installations – Endpoint/Server
      - Setting2: Check for unauthorized scheduled tasks and registry run keys – Endpoint/Server
      - Setting3: Look for unusual network traffic patterns indicative of C2 communication – Network monitoring
   External scanning:
      - Detect HTTP(S) traffic to known malicious C2 domains and IPs
      - Look for unusual TCP/SSL traffic patterns

IoCs:
   - Domain: softwareinteractivo[.]com, winsccp[.]com, mypondsoftware[.]com, tresize[.]com
   - IP: 104.234.119[.]16, 172.86.123[.]127
   - Hashes and filenames available on Sophos GitHub repository as per the document.

No additional specific IoCs found within the provided document.
