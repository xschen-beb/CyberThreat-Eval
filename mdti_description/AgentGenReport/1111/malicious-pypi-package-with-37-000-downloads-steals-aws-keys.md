Source: [https://www.bleepingcomputer.com/news/security/malicious-pypi-package-with-37-000-downloads-steals-aws-keys](https://www.bleepingcomputer.com/news/security/malicious-pypi-package-with-37-000-downloads-steals-aws-keys)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/malicious-pypi-package-with-37-000-downloads-steals-aws-keys
- https://www.bleepingcomputer.com/news/security/malicious-pypi-package-with-37-000-downloads-steals-aws-keys/
- https://socket.dev/blog/malicious-python-package-typosquats-fabric-ssh-library
- https://thehackernews.com/2024/11/malicious-pypi-package-fabrice-found.html
- https://hackread.com/fabrice-malware-pypi-steal-aws-credentials-3-years/
- https://medium.com/@ikhaleelkhan/beware-of-the-malicious-python-package-fabrice-how-typosquatting-is-stealing-aws-credentials-8ce1c126e062

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: Malicious PyPI package with 37,000 downloads steals AWS keys 

#### Root Cause 
 The root cause is the presence of a malicious package named 'fabrice' on the Python Package Index (PyPI). This package, designed to steal Amazon Web Services (AWS) credentials, leveraged typosquatting by mimicking the legitimate and popular 'fabric' package developed by bitprophet. The package executes OS-specific scripts for Windows and Linux, such as 'linuxThread' and 'winThread', to download and run malicious payloads. *The package was identified by the security firm 'Socket', which specializes in identifying risks in open-source code* (https://medium.com/@ikhaleelkhan/beware-of-the-malicious-python-package-fabrice-how-typosquatting-is-stealing-aws-credentials-8ce1c126e062). The package stores payloads in hidden directories and downloads encoded payloads for persistence. On Windows, it uses VBScript to run hidden Python scripts. The package first appeared in March 2021 and was detected in November 2024. 

#### Threat Actor/Group/Campaign 
 Not explicitly mentioned, but the actors behind the 'fabrice' package. 

#### Organization/Industry/Location 
 The victims are developers who downloaded the 'fabrice' package from PyPI. 

#### Start Date – End Date 
 The 'fabrice' package has been present since 2021 and was detected in November 2024. 

#### MITRE TTPs 
 ['T1071.001: Application Layer Protocol - Web Protocols', 'T1027: Obfuscated Files or Information', 'T1195.001: Supply Chain Compromise - Compromise Software Dependencies and Development Tools', 'T1552.001: Unsecured Credentials - Credentials In Files'] 

#### Impact 
 37,000 downloads leading to potential exposure of AWS credentials. The package sets up hidden directories and downloads encoded payloads for persistence. Specific scripts like 'per.sh' on Linux and 'd.py' on Windows are used to execute malicious commands using base64-encoded variables 'vv' and 'zz' for persistence. The package downloads a malicious executable 'chrome.exe' and sets up scheduled tasks to run every 15 minutes. Stolen credentials are sent to a server located in Paris, operated by M247, a VPN service provider. The data exfiltration uses 'boto3.Session()' to extract AWS credentials. 

#### Mitigation Steps 
 ['Regularly audit and verify the integrity of packages downloaded from repositories like PyPI.', 'Use tools designed to detect and block malicious packages (e.g., Socket Security).', 'Implement and enforce AWS Identity and Access Management (IAM) policies to manage permissions and monitor access to AWS resources.', 'Ensure proper security configurations and regular updates of security tools and protocols.', 'Educate developers about the risks of typosquatting and the importance of verifying package sources.'] 

#### Detection Signature 
 {'Service': 'PyPI', 'Severity': 'Critical', 'Incident': "Malicious PyPI package 'fabrice'", 'Signature Name': 'Malicious PyPI package detection', 'Internal checks': ['Verify package names and sources before downloading.', 'Conduct regular security audits on installed packages.'], 'External scanning': ['Monitor network traffic for unusual data exfiltration to suspicious IPs or domains.', 'Use tools to scan and detect malicious code within the packages.']} 

#### IoCs: 
- ip: 89.44.9.227 ([link](https://socket.dev/blog/malicious-python-package-typosquats-fabric-ssh-library)) 

- url: http://github.com/apps/socket-security ([link](https://socket.dev/blog/malicious-python-package-typosquats-fabric-ssh-library)) 

- vpn_server: M247 in Paris ([link](https://socket.dev/blog/malicious-python-package-typosquats-fabric-ssh-library)) 

- For more IoCs, please refer to the above links. 

#### Additional Details 
 *The analysis was conducted by Khaleel Khan, a cybersecurity researcher with 18 years of experience in state government and corporate sectors* (https://medium.com/@ikhaleelkhan/beware-of-the-malicious-python-package-fabrice-how-typosquatting-is-stealing-aws-credentials-8ce1c126e062). 


