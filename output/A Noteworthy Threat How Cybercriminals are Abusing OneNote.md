# A Noteworthy Threat How Cybercriminals are Abusing OneNote

Incident: Abuse of OneNote for Malware Delivery

Root cause: Exploitation of OneNote document capabilities to embed malicious scripts and executables, bypassing common security protections like 'Protected View' and 'Mark-of-the-Web'.

Impact: Potentially large-scale compromise of systems, with the delivery of various malware strains including AsyncRAT, Qakbot, and Remcos RAT, leading to data theft and unauthorized remote access. The exact number of devices or financial losses is not detailed in the blog.

Mitigation:
1. **User Awareness and Training**: Train users to recognize phishing emails and suspicious attachments, especially those with a sense of urgency or unexpected content.
2. **Email Filtering and Scanning**: Implement advanced email filtering solutions that can detect and block malicious OneNote attachments.
3. **Endpoint Protection**: Ensure endpoint protection solutions can detect and respond to the execution of scripts and obfuscated code from OneNote files.
4. **Policy Enforcement**: Enforce strict policies on the execution of scripts and PowerShell commands, and restrict the use of OneNote attachments from untrusted sources.
5. **Regular Updates and Patches**: Keep systems and security solutions up to date with the latest patches and threat intelligence to recognize and block new attack vectors.

Detection Signature:
Service: OneNote
Port: N/A
Severity: Critical
Incident: OneNote Malware Delivery
Signature name: “OneNote malicious script execution”
Internal checks:
  - Setting1: Implement monitoring to detect execution of batch scripts and PowerShell from OneNote documents.
  - Setting2: Monitor for unusual activity such as multiple emails with OneNote attachments being sent or received.
  - Setting3: Ensure endpoint protection policies include blocking or alerting on execution of scripts from OneNote files.
External scanning:
  - Check for emails containing OneNote attachments from unknown or suspicious sources.
  - Analyze email content for embedded scripts and executables.

IoCs:
- AsyncRAT
  - ce7a8a6a8fdc7846b9022a746c39a00a6eb4d19c
  - Invoice #10974543.one
  - a2bbfb23b51cb1f2bb213dfe410601bc7fa53875
  - skyy.bat
  - 7a0ccfb531bdc864a87bd47ce4af91e4243d9c9b
  - loader d2fd7053dc13293a02851cb74837d0788dc1d159
  
- Qakbot
  - 1523e0e1f454e480e6e2f8c0282d3fa6ed589059
  - 372068.one
  - 9ff9c3c674cfd13e2ed6199815d5f1287cd95ff2
  - Open.Bat
  - hxxp://198[.]44[.]140[.]78/210/184/187737.dat
  
- Remcos RAT
  - 360c70c00d6c2804b3b64f53ef2b68a7e9d79016
  - Property List.one
  - adb39f9a5f7d82e3886f551418344761f1e668df
  - Kgthldmuaxrymp.exe (Modiloader)
  - hxxps[://]tottenham02[.]duckdns[.]org/Kgthldmuaxr
  - 162[.]247[.]153[.]39

Please take immediate steps to secure your systems against these emerging threats.
