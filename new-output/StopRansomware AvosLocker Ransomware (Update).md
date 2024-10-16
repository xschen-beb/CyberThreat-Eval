Source: [https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-284a](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-284a)

# StopRansomware AvosLocker Ransomware (Update)

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: AvosLocker Ransomware Attack 

 Root cause: The root cause behind the incident is the exploitation of remote access tools and legitimate software by AvosLocker affiliates. The vulnerable/misconfigured services include:
- Remote system administration tools (Splashtop Streamer, Tactical RMM, PuTTy, AnyDesk, PDQ Deploy, Atera Agent)
- Use of custom PowerShell and batch scripts for lateral movement and privilege escalation, and credential harvesting using *Lazagne and Mimikatz* (https://www.hipaajournal.com/cisa-fbi-avoslocker-ransomware-cybersecurity-advisory/)
- Use of legitimate Windows tools (PsExec, Nltest)
- Open-source networking tunneling tools (Ligolo, Chisel)
- Webshells for network access
*Use of adversary emulation frameworks Cobalt Strike and Sliver for command and control* (https://www.bleepingcomputer.com/news/security/fbi-shares-avoslocker-ransomware-technical-details-defense-tips/) 

 Threat Actor/group/campaign: AvosLocker Ransomware (operating under a ransomware-as-a-service (RaaS) model), engaging in *exfiltration-based extortion* (https://www.hipaajournal.com/cisa-fbi-avoslocker-ransomware-cybersecurity-advisory/) 

 Organization/industry/location: Multiple critical infrastructure sectors in the United States, including *government, financial services, and critical manufacturing* (https://www.scworld.com/news/fbi-cisa-warn-critical-infrastructure-organizations-about-avoslocker-ransomware) 

 Start date – End date: Not specified (mentioned as recent as May 2023) 

 MITRE TTPs: - External Remote Services (T1133)
- Command and Scripting Interpreter: PowerShell (T1059.001)
- Command and Scripting Interpreter: Windows Command Shell (T1059.003)
- Windows Management Instrumentation (T1047)
- Protocol Tunneling (T1572)
- Credentials from Password Stores (T1555)
- Server Software Component: Web Shell (T1505.003) 

 Impact: The exact number of impacted records is not specified, but the ransomware affected organizations across multiple critical infrastructure sectors. 

 Mitigation: To protect against AvosLocker ransomware, the following steps should be taken: 
1. Secure remote access tools by implementing application controls and allowlisting remote access programs.
2. Strictly limit the use of RDP and other remote desktop services. Apply best practices like closing unused RDP ports, enforcing account lockouts, applying phishing-resistant MFA, and logging RDP login attempts.
3. Disable command-line and scripting activities and permissions.
4. Restrict the use of PowerShell and update it to the latest version. Enable enhanced PowerShell logging.
5. Configure the Windows Registry to require User Account Control (UAC) approval for any PsExec operations.
6. Disable File and Printer sharing services or use strong passwords/Active Directory authentication if required.
7. Implement a recovery plan with multiple offline backups.
8. Require all accounts with password logins to comply with NIST standards for password policies and enforce phishing-resistant multifactor authentication.
9. Keep all operating systems, software, and firmware up to date, especially patching known exploited vulnerabilities.
10. Segment networks to prevent ransomware spread and use network monitoring tools to detect abnormal activity.
11. Install, regularly update, and enable real-time detection for antivirus software.
12. Disable unused ports and add email banners to emails received from outside the organization.
13. Ensure all backup data is encrypted and immutable.
*14. Implement YARA rules to detect malware disguised as legitimate tools* (https://www.bleepingcomputer.com/news/security/fbi-shares-avoslocker-ransomware-technical-details-defense-tips/). 

 Detection Signature: Service: Remote system administration tools (Splashtop Streamer, Tactical RMM, PuTTy, AnyDesk, PDQ Deploy, Atera Agent)
Port: Multiple (including port 443 for NetMonitor.exe)
Severity: Critical
Incident: AvosLocker Ransomware Attack
Signature name: “Remote Access Tools and Protocol Tunneling”
Internal checks:
- Ensure remote access tools are allowlisted and unauthorized tools are blocked.
- Secure PowerShell usage with group policies and enable enhanced logging.
- Verify that webshells are not present on web servers.
External scanning:
- Scan for open ports commonly used by remote access tools.
- Detect use of protocol tunneling tools like Ligolo and Chisel.
*15. Monitor for the presence of NetMonitor.exe to ensure it is not acting as a reverse proxy* (https://www.bleepingcomputer.com/news/security/fbi-shares-avoslocker-ransomware-technical-details-defense-tips/). 

 IoCs: Files and Tools:
- psscriptpolicytest_im2hdxqi.g0k.ps1 (MD5: 829f2233a1cd77e9ec7de98596cd8165)
- psscriptpolicytest_lysyd03n.o10.ps1 (MD5: 6ebd7d7473f0ace3f52c483389cab93f)
- psscriptpolicytest_1bokrh3l.2nw.ps1 (MD5: 10ef090d2f4c8001faadb0a833d60089)
- psscriptpolicytest_nvuxllhd.fs4.ps1 (MD5: 8227af68552198a2d42de51cded2ce60)
- psscriptpolicytest_2by2p21u.4ej.ps1 (MD5: 9d0b3796d1d174080cdfdbd4064bea3a)
- psscriptpolicytest_te5sbsfv.new.ps1 (MD5: af31b5a572b3208f81dbf42f6c143f99)
- psscriptpolicytest_v3etgbxw.bmm.ps1 (MD5: 1892bd45671f17e9f7f63d3ed15e348e)
- psscriptpolicytest_fqa24ixq.dtc.ps1 (MD5: cc68eaf36cb90c08308ad0ca3abc17c1)
- psscriptpolicytest_jzjombgn.sol.ps1 (MD5: 646dc0b7335cffb671ae3dfd1ebefe47)
- psscriptpolicytest_rdm5qyy1.phg.ps1 (MD5: 609a925fd253e82c80262bad31637f19)
- psscriptpolicytest_endvm2zz.qlp.ps1 (MD5: c6a667619fff6cf44f447868d8edd681)
- psscriptpolicytest_s1mgcgdk.25n.ps1 (MD5: 3222c60b10e5a7c3158fd1cb3f513640)
- psscriptpolicytest_xnjvzu5o.fta.ps1 (MD5: 90ce10d9aca909a8d2524bc265ef2fa4)
- psscriptpolicytest_satzbifj.oli.ps1 (MD5: 44a3561fb9e877a2841de36a3698abc0)
- psscriptpolicytest_grjck50v.nyg.ps1 (MD5: 5cb3f10db11e1795c49ec6273c52b5f1)
- psscriptpolicytest_0bybivfe.x1t.ps1 (MD5: 122ea6581a36f14ab5ab65475370107e)
- psscriptpolicytest_bzoicrns.kat.ps1 (MD5: c82d7be7afdc9f3a0e474f019fb7b0f7)
- BEACON.PS1 (SHA256: e68f9c3314beee640cc32f08a8532aa8dcda613543c54a83680c21d7cd49ca0f)
- Encoded PowerShell script (SHA256: ad5fd10aa2dc82731f3885553763dfd4548651ef3e28c69f77ad035166d63db7)
- Encoded PowerShell script (SHA256: 48dd7d519dbb67b7a2bb2747729fc46e5832c30cafe15f76c1dbe3a249e5e731)
- PowerShell backdoor (SHA1: 2d1ce0231cf8ff967c36bbfc931f3807ddba765c)
*16. NetMonitor.exe (reverse proxy malware)* (https://www.bleepingcomputer.com/news/security/fbi-shares-avoslocker-ransomware-technical-details-defense-tips/).
*17. FileZilla and Rclone for data exfiltration* (https://www.hipaajournal.com/cisa-fbi-avoslocker-ransomware-cybersecurity-advisory/). 

 Email Addresses: - keishagrey994@outlook[.]com 

 Virtual Currency Wallets: - a6dedd35ad745641c52d6a9f8da1fb09101d152f01b4b0e85a64d21c2a0845ee
- bfacebcafff00b94ad2bff96b718a416c353a4ae223aa47d4202cdbc31e09c92
- 418748c1862627cf91e829c64df9440d19f67f8a7628471d4b3a6cc5696944dd
- bc1qn0u8un00nl6uz6uqrw7p50rg86gjrx492jkwfn 


# Related articles (describing the same threat) 
['https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-284a', 'https://www.bleepingcomputer.com/news/security/fbi-shares-avoslocker-ransomware-technical-details-defense-tips/', 'https://www.scworld.com/news/fbi-cisa-warn-critical-infrastructure-organizations-about-avoslocker-ransomware', 'https://www.hipaajournal.com/cisa-fbi-avoslocker-ransomware-cybersecurity-advisory/']
