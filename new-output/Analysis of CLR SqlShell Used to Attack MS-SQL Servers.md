Source: [https://asec.ahnlab.com/en/52479/](https://asec.ahnlab.com/en/52479/)

# Analysis of CLR SqlShell Used to Attack MS-SQL Servers

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: MS-SQL Servers Compromised Using CLR SqlShell *and targeted by Mallox ransomware via PureCrypter* (https://blog.sekoia.io/mallox-ransomware-affiliate-leverages-purecrypter-in-microsoft-sql-exploitation-campaigns/) 

 Root cause: Misconfigured MS-SQL servers with simple passwords and public visibility on the internet, allowing threat actors to exploit them via brute force or dictionary attacks. *The 'sa' account was specifically targeted with weak passwords* (https://blog.sekoia.io/mallox-ransomware-affiliate-leverages-purecrypter-in-microsoft-sql-exploitation-campaigns/). 

 Threat Actor/group/campaign: Various, including LemonDuck, MyKings, ShadowForce, Kingminer, *and Mallox ransomware affiliates leveraging PureCrypter* (https://blog.sekoia.io/mallox-ransomware-affiliate-leverages-purecrypter-in-microsoft-sql-exploitation-campaigns/). 

 Organization/industry/location: The incident affects any organization using poorly managed MS-SQL servers. 

 Start date – End date: Not specified. The report covers ongoing threats. 

 MITRE TTPs: ['T1078: Valid Accounts', 'T1071: Application Layer Protocol', 'T1059: Command and Scripting Interpreter', 'T1071.001: Web Protocols', 'T1059.005: Command and Scripting Interpreter: Visual Basic', 'T1059.003: Command and Scripting Interpreter: Windows Command Shell', 'T1059.001: Command and Scripting Interpreter: PowerShell'] 

 Impact: Compromised MS-SQL servers leading to installation of CoinMiners, ransomware, proxyware, and other malware. Financial losses and resource theft are implied but not quantified. *Specifically, Mallox ransomware deployment via PureCrypter was observed, leading to potential data encryption and exfiltration* (https://blog.sekoia.io/mallox-ransomware-affiliate-leverages-purecrypter-in-microsoft-sql-exploitation-campaigns/). 

 Mitigation: [{'Secure MS-SQL Server Configuration': ['Use complex, strong passwords and change them regularly.', 'Disable unnecessary features such as xp_cmdshell and OLE automation.', 'Ensure MS-SQL servers are not publicly accessible unless absolutely necessary.', 'Apply the principle of least privilege for SQL accounts.']}, {'Regular Patching': 'Keep MS-SQL servers and associated systems updated with the latest security patches.'}, {'Network Security': ['Implement firewalls and access controls to restrict unauthorized access.', 'Use network security monitoring to detect suspicious activity.']}, {'Authentication and Authorization': ['Enable multi-factor authentication (MFA) for accessing SQL servers.', 'Regularly audit user accounts and permissions.']}, {'Monitoring and Response': ['Deploy security information and event management (SIEM) systems to monitor and respond to suspicious activities.', 'Conduct regular security assessments and penetration testing.']}] 

 Detection Signature: {'Service': 'MS-SQL', 'Port': 1433, 'Severity': 'Critical', 'Incident': 'Unauthorized MS-SQL Access', 'Signature name': 'MS-SQL brute force attempt detected', 'Internal checks': ['Ensure MS-SQL port (1433) is not exposed to the external Internet.', 'Monitor for failed login attempts and unusual login patterns.', '*Track connections from IP addresses in AS208091, associated with XHost Internet Solution* (https://blog.sekoia.io/mallox-ransomware-affiliate-leverages-purecrypter-in-microsoft-sql-exploitation-campaigns/).', 'Check for the presence of suspicious CLR assemblies or unusual jobs in SQL Agent.'], 'External scanning': ['Port (1433) open', 'Multiple failed login attempts', 'Presence of unauthorized CLR assemblies']} 

 IoCs: {'MD5': ['012e607f99ecc5b108b292d72938456a', '130d2b07a1c4cde8f0804df9fa9622d4', '15c87480e0405b41f675222ef2bea95a', '17606de13187c780ad3bf6caf2d1bd8c', '1e92e397d0ad3d8006d99f81d913ffa1'], 'URL': ['http[:]//54[.]36[.]10[.]73[:]1001/', 'http[:]//88[.]214[.]26[.]9[:]13785/', 'http[:]//adminserver[.]online[:]1001/', 'http[:]//c[.]getmoney[.]company/CLRV7/data[.]txt', 'http[:]//c[.]getmoney[.]company/CLRV7/ver[.]txt']} 


# Related articles (describing the same threat) 
['https://asec.ahnlab.com/en/52479/', 'https://blog.sekoia.io/mallox-ransomware-affiliate-leverages-purecrypter-in-microsoft-sql-exploitation-campaigns/']
