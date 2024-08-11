Source: [https://www.welivesecurity.com/en/eset-research/stealth-falcon-preying-middle-eastern-skies-deadglyph/](https://www.welivesecurity.com/en/eset-research/stealth-falcon-preying-middle-eastern-skies-deadglyph/)

# Stealth Falcon Preying Over Middle Eastern Skies with Deadglyph

Incident: Stealth Falcon Deadglyph Backdoor

Root cause: Infiltration through a sophisticated multi-stage shellcode downloader, likely initiated via user execution of a malicious CPL file.

Impact: The blog does not provide specific numbers on the records leaked, but it indicates that high-profile governmental entities in the Middle East were compromised for espionage purposes. The exact number of devices and people impacted, as well as financial losses, are not detailed in the document.

Mitigation: To mitigate the risks posed by Deadglyph and similar threats, the following steps should be implemented:
1. **User Awareness and Training**: Educate users about the dangers of executing unsolicited attachments or files, especially those with unusual extensions like `.cpl`.
2. **Endpoint Protection**: Deploy and maintain up-to-date endpoint protection solutions that can detect and block malicious activities, including the execution of unauthorized shellcode.
3. **Registry Monitoring**: Implement monitoring for suspicious registry changes, particularly those involving unusual keys and values indicative of persistence mechanisms.
4. **Network Segmentation**: Isolate critical systems and restrict their ability to communicate directly with the internet, reducing the risk of C&C communications.
5. **Environment Hardening**:
   - Disable unnecessary services and features such as WMI event subscriptions if not needed.
   - Use application whitelisting to prevent the execution of unauthorized programs.
6. **Regular Audits and Penetration Testing**: Conduct frequent security audits and penetration testing to identify and remediate potential vulnerabilities in the infrastructure.
7. **Patch Management**: Ensure all systems are up-to-date with the latest security patches to mitigate known vulnerabilities.

Detection Signature:
- **Service**: Windows Management Instrumentation (WMI), .NET Framework, HTTP(S) for C&C communication
- **Port**: 80, 443
- **Severity**: Critical
- **Incident**: Stealth Falcon Deadglyph Backdoor
- **Signature name**: "Deadglyph backdoor detection"
- **Internal checks** (see next):
    - **Setting1**: Monitor for unauthorized WMI event subscriptions – Inside VMs
    - **Setting2**: Detect registry modifications associated with Deadglyph's persistence mechanism – Inside VMs
    - **Setting3**: Monitor for the execution of rundll32 with suspicious DLLs – Inside VMs
- **External scanning** (see next):
    - **Port (80, 443) open**
    - **Communication with known C&C domains**

IoCs:
- **Files**:
    - SHA-1: C40F1F46D230A85F702DAA38CFA18D60481EA6C2 (pbrtl.dll, Registry Shellcode Loader)
    - SHA-1: 740D308565E215EB9B235CC5B720142428F540DB (Deadglyph Backdoor – Executor)
    - SHA-1: 1805568D8362A379AF09FD70D3406C6B654F189F (Deadglyph Backdoor – Orchestrator)
    - SHA-1: 9CB373B2643C2B7F93862D2682A0D2150C7AEC7E (Orchestrator Network module)
    - SHA-1: F47CB40F6C2B303308D9D705F8CAD707B9C39FA5 (Orchestrator Timer module)
    - SHA-1: 3D4D9C9F2A5ACEFF9E45538F5EBE723ACAF83E32 (Process creator module)
    - SHA-1: 3D2ACCEA98DBDF95F0543B7C1E8A055020E74960 (File reader module)
    - SHA-1: 4E3018E4FD27587BD1C566930AE24442769D16F0 (Info collector module)
    - SHA-1: 7F728D490ED6EA64A7644049914A7F2A0E563969 (First stage of shellcode downloader chain)
- **Certificates**:
    - Serial number: 00F0FB1390F5340CD2572451D95DB1D92D
    - Thumbprint: DB3614DAF58D041F96A5B916281EA0DC97AA0C29
    - Subject CN: RHM LIMITED
    - Subject O: RHM LIMITED
    - Subject L: St. Albans
    - Subject S: Hertfordshire
    - Subject C: GB
    - Email: rhm@rhmlimited[.]co.uk
    - Valid from: 2021-03-16 00:00:00
    - Valid to: 2022-03-16 23:59:59
- **C&C servers**:
    - IP: 185.25.50[.]60, Domain: chessandlinkss[.]com
    - IP: 135.125.78[.]187, Domain: easymathpath[.]com
    - IP: 45.14.227[.]55, Domain: joinushealth[.]com

MITRE ATT&CK Techniques:
- Resource Development: T1583.001 (Acquire Infrastructure: Domains), T1583.003 (VPS), T1587.001 (Develop Capabilities: Malware), T1588.003 (Obtain Capabilities: Code Signing Certificates)
- Execution: T1047 (WMI), T1059.003 (Command and Scripting Interpreter: Windows Command Shell), T1106 (Native API), T1204.002 (User Execution: Malicious File)
- Persistence: T1546.003 (Event Triggered Execution: WMI Event Subscription)
- Defense Evasion: T1027 (Obfuscated Files or Information), T1070.004 (Indicator Removal: File Deletion), T1112 (Modify Registry), T1134 (Access Token Manipulation), T1140 (Deobfuscate/Decode Files or Information), T1218.011 (System Binary Proxy Execution: Rundll32), T1480.001 (Execution Guardrails: Environmental Keying), T1562.001 (Impair Defenses: Disable or Modify Tools), T1620 (Reflective Code Loading)
- Discovery: T1007 (System Service Discovery), T1012 (Query Registry), T1016 (System Network Configuration Discovery), T1033 (System Owner/User Discovery), T1057 (Process Discovery), T1082 (System Information Discovery), T1518 (Software Discovery), T1518.001 (Security Software Discovery)
- Collection: T1005 (Data from Local System)
- Command and Control: T1071.001 (Application Layer Protocol: Web Protocols), T1090 (Proxy), T1573.001 (Encrypted Channel: Symmetric Cryptography)
- Exfiltration: T1041 (Exfiltration Over C2 Channel)

No additional IoCs found beyond what has been listed.
