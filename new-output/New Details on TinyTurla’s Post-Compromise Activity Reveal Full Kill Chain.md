Source: [https://blog.talosintelligence.com/tinyturla-full-kill-chain/](https://blog.talosintelligence.com/tinyturla-full-kill-chain/)

# New Details on TinyTurla’s Post-Compromise Activity Reveal Full Kill Chain

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: TinyTurla Post-Compromise Activity 

 Root cause: The root cause of the incident was the initial compromise of systems within a European non-governmental organization's network by the Turla espionage group. They exploited the systems by adding exclusions to antivirus software like *Microsoft Defender* (https://gbhackers.com/tinyturla-evolved-ttps-stealth-attacks), establishing persistence via malicious services, and using tools like TinyTurla-NG, *Chisel open-source attack framework* (https://duo.com/decipher/tinyturla-ng-backdoor-has-big-capabilities), batch files for service creation, and PowerShell commands. The attackers engaged in data exfiltration and *credential harvesting* (https://duo.com/decipher/tinyturla-ng-backdoor-has-big-capabilities). 

 Threat Actor/group/campaign: Turla (Russian espionage group) in coordination with *Cisco Talos* (https://gbhackers.com/tinyturla-evolved-ttps-stealth-attacks) 

 Organization/industry/location: *European non-governmental organization (NGO) in collaboration with CERT.NGO* (https://blog.talosintelligence.com/tinyturla-ng-tooling-and-c2/) 

 Start date – End date: October 2023 – January 2024 

 MITRE TTPs: ['T1562.001: Impair Defenses: Disable or Modify Tools', 'T1543.003: Create or Modify System Process: Windows Service', 'T1573.002: Encrypted Channel: Asymmetric Cryptography', 'T1041: Exfiltration Over C2 Channel'] 

 Impact: Multiple systems within the NGO's network were compromised, leading to data exfiltration and potential exposure of sensitive information. 

 Mitigation: ['Regularly update antivirus and endpoint protection solutions to detect and block known malware.', 'Implement strict access controls and network segmentation to limit lateral movement.', 'Monitor and audit registry changes, especially those related to antivirus exclusions and service creation.', 'Use behavioral analytics to detect anomalous activities such as unauthorized service creation or unexpected network traffic.', 'Deploy multi-factor authentication (MFA) to secure access to sensitive systems.', 'Conduct regular security training and awareness programs for employees.'] 

 Detailed Steps for mitigation: ['**Update Antivirus**: Ensure antivirus definitions and endpoint protection software are up-to-date to detect known threats.', '**Access Controls**: Implement role-based access controls and network segmentation to limit access to critical systems.', '**Registry Monitoring**: Use tools to monitor and audit registry changes, focusing on keys related to antivirus exclusions and service creation.', '**Behavioral Analytics**: Deploy solutions that analyze user and system behavior to detect anomalies.', '**MFA Deployment**: Implement multi-factor authentication for accessing sensitive systems and data.', '**Security Training**: Regularly train employees on security best practices and phishing awareness.'] 

 Detection Signature: {'Service': 'Windows Defender, Windows Service', 'Port': 'Not applicable', 'Severity': 'Critical', 'Incident': 'TinyTurla Post-Compromise Activity', 'Signature name': '“Windows Defender Exclusions Modified” & “Unauthorized Windows Service Creation”', 'Internal checks': {'Setting1': 'Monitor registry key `HKLM\\SOFTWARE\\Microsoft\\Windows Defender\\Exclusions\\Paths` for unauthorized exclusions – In platform', 'Setting2': 'Monitor registry key `HKLM\\SYSTEM\\CurrentControlSet\\services` for unauthorized service creation – Inside VMs', 'Setting3': 'Conduct regular audits of service creation and configuration – Inside VMs'}, 'External scanning': {'Monitor network traffic for unusual patterns indicative of data exfiltration (e.g., Chisel tool usage)': 'https://blog.talosintelligence.com/tinyturla-ng-tooling-and-c2/', 'Use SIEM tools to correlate logs and detect unauthorized access patterns': 'https://blog.talosintelligence.com/tinyturla-ng-tooling-and-c2/'}} 

 IoCs: {'Hashes': ['267071df79927abd1e57f57106924dd8a68e1c4ed74e7b69403cdcdf6e6a453b', 'd6ac21a409f35a80ba9ccfe58ae1ae32883e44ecc724e4ae8289e7465ab2cf40', 'ad4d196b3d85d982343f32d52bffc6ebfeec7bf30553fa441fd7c3ae495075fc', '13c017cb706ef869c061078048e550dba1613c0f2e8f2e409d97a1c0d9949346', 'b376a3a6bae73840e70b2fa3df99d881def9250b42b6b8b0458d0445ddfbc044'], 'Domains': ['hanagram[.]jp', 'thefinetreats[.]com', 'caduff-sa[.]ch', 'jeepcarlease[.]com', 'buy-new-car[.]com', 'carleasingguru[.]com'], 'IP Addresses': ['91[.]193[.]18[.]120']} 


# Related articles (describing the same threat) 
['https://blog.talosintelligence.com/tinyturla-full-kill-chain/', 'https://blog.talosintelligence.com/tinyturla-ng-tooling-and-c2/', 'https://duo.com/decipher/tinyturla-ng-backdoor-has-big-capabilities', 'https://gbhackers.com/tinyturla-evolved-ttps-stealth-attacks/']
