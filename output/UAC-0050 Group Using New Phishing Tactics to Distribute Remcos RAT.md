# UAC-0050 Group Using New Phishing Tactics to Distribute Remcos RAT

Incident: UAC-0050 Remcos RAT: Pipe Method Used for Evasion in Ukraine Attack

Root cause: The root cause of the incident is the successful deployment of a phishing attack, which led to the execution of a malicious .lnk file. This file initiated a chain of events involving various scripts and payloads, ultimately resulting in the installation of Remcos RAT on the target systems.

Impact: The specific number of devices or individuals impacted is not stated in the document. However, the attack targeted Ukrainian government agencies, which could imply a significant impact on national security and operations. Financial losses are not detailed in the report.

Mitigation: 
1. Implement advanced email filtering solutions to detect and block phishing emails before they reach end-users.
2. Educate employees and users about the dangers of phishing and the importance of not clicking on suspicious links or attachments.
3. Utilize network monitoring tools to identify unusual communication patterns that may indicate the presence of remote access tools.
4. Regularly review and secure system configurations to ensure unnecessary services and startup entries are disabled or closely monitored.
5. Deploy endpoint detection and response (EDR) solutions that can identify and block malicious activities, including process injections and the use of pipes for data transfer.
6. Use behavioral analysis tools to detect anomalies that may indicate attempts by RATs to establish persistence or communicate with command and control servers.
7. Implement strict access controls and authentication mechanisms to limit the execution of scripts and payloads.

Detection Signature:
Service: Windows Operating System (specifically focusing on PowerShell, MSHTA, and cmd.exe)
Port: Not applicable (focus on process and script execution rather than network ports)
Severity: Critical
Incident: UAC-0050 Remcos RAT: Pipe Method Used for Evasion
Signature name: “Remcos RAT deployment via malicious .lnk file”
Internal checks:
  - Setting1: Monitor for the execution of .lnk files that initiate downloads or script executions.
  - Setting2: Detect the use of MSHTA.exe to run scripts from URLs.
  - Setting3: Identify the use of PowerShell to download and execute encoded or obfuscated scripts.
External scanning:
  - No specific port scanning required; focus on monitoring process execution and script activities.

IoCs:
- File Names and Hashes:
  - Lnk file: 56154fedaa70a3e58b7262b7c344d30a
  - 6.hta: 9b777d69b018701ec5ad19ae3f06553f
  - ofer.docx: 74865c6c290488bd5552aa905c02666c
  - word_update.exe: 7c05cfed156f152139a6b1f0d48b5cc1
  - fmTask_dbg.exe: 7c05cfed156f152139a6b1f0d48b5cc1
  - Remcos: 0b2d0eb5af93a3355244e1319e3de9da
  
- Related Hashes:
  - Lnk: 7f87d36c989a11edf0de9af392891d89
  - Lnk: f5ee6aa31c950dfe55972e50e02201d3
  - Lnk: 5c734bb1e41fab9c7b2dabd06e27bc7b
  - shablon.hta: 1c3e1e0319dc6aa24166d5e2aaaec675
  - zayava.docx: 818beece85ecd90d413782dd51d939b1
  - Ps1: 8158b43f745e0e7a519458b0150e1b61
  - Ps1: f71ef85824f906856cb3d2205058bdd2
  - Ps1: 8bebea01d914a3c3a2d876417f7d1d54
  - Remcos: b1f8484ee01a7730938210ea6e851888
  
- URLs:
  - cluster00<X>[.]ovh[.]net
  - 194[.]87.31[.]229
  - 46[.]249.58[.]40
  - new-tech-savvy[.]com/6.hta
  - new-tech-savvy[.]com/5[.]hta
  - new-tech-savvy[.]com/algo[.]hta
  - new-tech-savvy[.]com/shablon[.]hta
  - new-tech-savvy[.]com/word_update[.]exe
  - new-tech-savvy[.]com/zayava[.]docx
  - new-tech-savvy[.]com/ofer[.]docx
