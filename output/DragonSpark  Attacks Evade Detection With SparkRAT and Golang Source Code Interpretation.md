Source: [https://www.sentinelone.com/labs/dragonspark-attacks-evade-detection-with-sparkrat-and-golang-source-code-interpretation/](https://www.sentinelone.com/labs/dragonspark-attacks-evade-detection-with-sparkrat-and-golang-source-code-interpretation/)

# DragonSpark  Attacks Evade Detection With SparkRAT and Golang Source Code Interpretation

Incident: DragonSpark | Attacks Evade Detection with SparkRAT and Golang Source Code Interpretation

Root cause: Misconfigured MySQL database servers and vulnerable web servers

Impact: Multiple organizations in East Asia were affected. The exact financial losses and the number of impacted devices or individuals were not specified.

Mitigation: Harden MySQL database servers and web servers against unauthorized access.
- Secure MySQL servers:
  1. Ensure MySQL servers are not exposed directly to the Internet.
  2. Enable strong authentication mechanisms.
  3. Regularly update MySQL to the latest version.
  4. Implement network segmentation to limit access.
  5. Apply firewall rules to restrict access to MySQL servers.

- Secure web servers:
  1. Regularly update web servers to patch vulnerabilities.
  2. Use web application firewalls (WAF) to protect against SQL injection and other web-based attacks.
  3. Regularly conduct security audits and vulnerability assessments.
  4. Employ secure coding practices to protect against cross-site scripting (XSS) and other injection flaws.
  5. Monitor for unauthorized changes and access.

Detection Signature:
Service: MySQL  
Port: 3306  
Severity: Critical  
Incident: DragonSpark Attacks  
Signature name: “MySQL publicly accessible”  
Internal checks:  
  - Setting1: MySQL port (3306) should not be exposed on external Internet. – In platform  
  - Setting2: MySQL port (3306) should not listen on the external Internet – Inside VMs  
  - Setting3: MySQL server should secure with authentication credentials. – Inside VMs  

External scanning:  
  - Port (3306) open
  - MySQL no-pass-login

IoCs:
- Hashes:
  - ShellCode_Loader: 83130d95220bc2ede8645ea1ca4ce9afc4593196
  - m6699.exe: 14ebbed449ccedac3610618b5265ff803243313d
  - SparkRAT: 2578efc12941ff481172dd4603b536a3bd322691
- IP Addresses/Domains:
  - C2 server network endpoint for ShellCode_Loader: 103.96.74[.]148:8899
  - C2 server network endpoint for SparkRAT: 103.96.74[.]148:6688
  - C2 server network endpoint for m6699.exe: 103.96.74[.]148:6699
  - C2 server IP address for China Chopper: 104.233.163[.]190
  - Staging URL for ShellCode_Loader: hxxp://211.149.237[.]108:801/py.exe
  - Staging URL for m6699.exe: hxxp://211.149.237[.]108:801/m6699.exe
  - Staging URL for SparkRAT: hxxp://43.129.227[.]159:81/c.exe
  - Staging URL for GotoHTTP: hxxp://13.213.41.125:9001/go.exe
  - Staging URL for ShellCode_Loader: hxxp://www.bingoplanet[.]com[.]tw/images/py.exe
  - Staging URL for ShellCode_Loader: hxxps://www.moongallery.com[.]tw/upload/py.exe
  - Staging URL for ShellCode_Loader: hxxp://www.holybaby.com[.]tw/api/ms.exe
