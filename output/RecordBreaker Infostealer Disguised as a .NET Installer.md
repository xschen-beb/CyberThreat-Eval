# RecordBreaker Infostealer Disguised as a .NET Installer

Incident: RecordBreaker Infostealer Disguised as a .NET Installer

Root cause: Users downloading and executing software from untrusted sources, leading to the infection of their systems with malware disguised as legitimate software.

Impact: Potentially thousands of users impacted, leading to the theft of sensitive information such as login credentials, financial details, and personal data. Financial losses could be substantial but are difficult to quantify without specific figures.

Mitigation: 
1. **User Education:** Educate users to avoid downloading and using illegal tools such as cracks or keygens and to only use installers from trusted and official sources.
2. **Enhanced Security Measures:**
   - Implement robust endpoint protection solutions that can detect and block malicious activities.
   - Utilize advanced threat detection systems that can identify and mitigate unusual behaviors, such as the execution of unauthorized PowerShell commands.
3. **Network Security:**
   - Monitor network traffic for unusual outbound connections to known malicious IP addresses or domains.
   - Implement network segmentation to limit the spread of malware within the network.

**Detailed Steps for Mitigation:**
1. **Endpoint Protection:**
   - Deploy and maintain up-to-date antivirus and anti-malware solutions on all endpoints.
   - Use endpoint detection and response (EDR) tools to identify and respond to threats in real-time.

2. **User Training:**
   - Conduct regular security awareness training for users, emphasizing the risks of downloading and running software from untrusted sources.
   - Provide guidelines on identifying phishing and scam attempts.

3. **Network Monitoring:**
   - Configure network monitoring tools to alert on suspicious connections to known malicious IPs or domains.
   - Implement firewall rules to block outbound connections to identified malicious IP addresses and domains.

4. **Incident Response:**
   - Develop and maintain an incident response plan to quickly address and contain malware infections.
   - Regularly test the incident response plan through tabletop exercises and simulations.

Detection Signature:
- Service: Windows PowerShell
- Port: N/A (Local Execution)
- Severity: Critical
- Incident: RecordBreaker Infostealer
- Signature name: “RecordBreaker Infostealer Activity”
- Internal checks:
  - Setting1: Monitor for unauthorized execution of PowerShell commands.
  - Setting2: Detect the presence of common indicators of virtualization environment scans.
  - Setting3: Monitor for the download and execution of executables from untrusted sources.
- External scanning:
  - N/A (Internal activity detection)

IoCs:
- IPs:
  - 89.185.85[.]117
  - 94.142.138[.]74
  - 77[.]91[.]73[.]11
  - 78[.]46[.]248[.]198
  - 79[.]137[.]202[.]161
  - 79[.]137[.]203[.]217
  - 85[.]192[.]40[.]245

- URLs:
  - http://89.185.85[.]117/bmlupdate.exe
  - hxxps://download.visualstudio.microsoft[.]com/download/pr/1f5af042-d0e4-4002-9c59-9ba66bcf15f6/124d2afe5c8f67dfa910da5f9e3db9c1/ndp472-kb4054531-web.exe
  - http[:]//77[.]91[.]73[.]11[:]2705/
  - http[:]//78[.]46[.]248[.]198/
  - http[:]//79[.]137[.]202[.]161/7yd0ymt74ny7qbuk/Pangl[.]exe
  - http[:]//79[.]137[.]203[.]217/
  - http[:]//85[.]192[.]40[.]245/fol1paf2nyg0/bn1[.]exe

- MD5 Hashes:
  - 9fed0b55798d1ffd9b44820b3fec080c
  - 0c34e053a1641c0f48f7cac16b743a82
  - 0c819835aa1289985c5292f48e7c1f24
  - 14eb67caa2c8c5e312e1bc8804f7135f
  - 19e491dfe1ab656f715245ec9401bdd1
  - 21a8a6cfa229862eedc12186f0139da0

Additional IoCs can be found on AhnLab TIP.
