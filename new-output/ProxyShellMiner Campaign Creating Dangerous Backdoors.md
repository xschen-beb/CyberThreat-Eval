Source: [https://blog.morphisec.com/proxyshellminer-campaign](https://blog.morphisec.com/proxyshellminer-campaign)

# ProxyShellMiner Campaign Creating Dangerous Backdoors

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: ProxyShellMiner Campaign 

 Root cause: The root cause behind the incident is the exploitation of known vulnerabilities in Microsoft Exchange servers, specifically CVE-2021-34473 and CVE-2021-34523, enabling unauthorized access and control over the servers. These vulnerabilities allowed the threat actors to deploy the ProxyShellMiner malware. 

 Threat Actor/group/campaign: Likely an unidentified group leveraging ProxyShell vulnerabilities to deploy crypto miners. 

 Organization/industry/location: Targeted organizations are those running unpatched Microsoft Exchange servers, potentially spanning multiple industries. 

 Start date – End date: May 2022 – December 2022 (based on the compromised server usage dates) 

 MITRE TTPs: ['T1190: Exploit Public-Facing Application', 'T1047: Windows Management Instrumentation', 'T1059.001: PowerShell', 'T1071.001: Web Protocols', 'T1027: Obfuscated Files or Information', 'T1569.002: Service Execution'] 

 Impact: Mining cryptocurrency on organizational networks, leading to system performance degradation, increased power consumption, equipment overheating, and potential for further malicious activities such as ransomware deployment. 

 Mitigation: {'1. **Apply Security Patches**': 'Ensure that the latest security updates are applied to Microsoft Exchange servers, specifically targeting CVE-2021-34473 and CVE-2021-34523.', 'Steps': ['Identify all Exchange servers in the environment.', "Download and apply the relevant updates from Microsoft's official site.", 'Verify the patch installation and monitor for any issues.'], '2. **Implement Defense-in-Depth**': {'Use Automated Moving Target Defense (AMTD)': 'To prevent ProxyShellMiner from accessing runtime memory by constantly morphing the environment and setting decoy traps.', 'Steps': ['Deploy AMTD technology across the network.', 'Integrate with existing security tools (NGAV, EPP, and EDR/XDR).', 'Monitor and fine-tune the settings to ensure optimal protection.']}, '3. **Monitor and Secure NETLOGON Folder**': {'Steps': ['Regularly audit the NETLOGON folder for unauthorized files or changes.', 'Implement access controls to limit who can modify the folder.']}, '4. **Enhance Logging and Monitoring**': {'Steps': ['Enable detailed logging on Exchange servers.', 'Use SIEM (Security Information and Event Management) solutions to correlate and analyze log data.', 'Set up alerts for suspicious activities.']}} 

 Detection Signature: {'Service': 'Microsoft Exchange', 'Port': '443 (used for HTTPS connections to Exchange servers)', 'Severity': 'Critical', 'Incident': 'ProxyShellMiner Exploitation', 'Signature name': 'ProxyShell vulnerabilities exploited', 'Internal checks': ['Ensure Exchange servers are patched against CVE-2021-34473 and CVE-2021-34523.', 'Monitor for abnormal changes in the NETLOGON folder.', 'Validate PowerShell scripts and commands executed on Exchange servers.'], 'External scanning': ['Identify unpatched Exchange servers.', 'Look for signs of compromise related to ProxyShell vulnerabilities.']} 

 IoCs: {'Domains': ['mail.shaferglazer[.]com', 'mail.ghmproperties[.]com', 'mail.itseasy[.]com', 'mail.techniservinc[.]com'], 'Hashes': ['936d851d95e621dfb220bed06011e6fac0019dba7f2e601f47764301f5ce60e9', '93430f789cc8397d6476597c54665caf3e2eaedbf90b3faa96bda207bfef0d80', 'b3bb2131d7f2bfe9243462330662c17001644298bcba42f59ee3fd305af02b80', 'e86d39fb3a97910aa31fea95f82b2b3d567074639312862b4eba3e1f5525e7a7'], 'and others listed in the blog.': '*Over 20,000 vulnerable servers* (https://www.bleepingcomputer.com/tag/proxyshell/); *CISA urgent alert* (https://www.bleepingcomputer.com/tag/proxyshell/); *Electoral Commission breach* (https://www.bleepingcomputer.com/tag/proxyshell/).'} 


# Related articles (describing the same threat) 
['https://blog.morphisec.com/proxyshellminer-campaign', 'https://www.bleepingcomputer.com/tag/proxyshell/']
