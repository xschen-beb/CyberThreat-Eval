Source: [https://www.bleepingcomputer.com/news/security/qnap-addresses-critical-flaws-across-nas-router-software](https://www.bleepingcomputer.com/news/security/qnap-addresses-critical-flaws-across-nas-router-software)

## Related articles (describing the same threat) 
- https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908
- https://www.qnap.com/en-au/security-advisory/qsa-24-44
- https://vuldb.com?id.285886
- https://www.cvedetails.com/cve/CVE-2024-38644
- https://www.bleepingcomputer.com/news/security/qnap-addresses-critical-flaws-across-nas-router-software
- https://securityonline.info/critical-vulnerabilities-in-qnap-notes-station-3-update-now-to-protect-your-data
- https://www.qnap.com/en-us/security-advisory/qsa-24-36
- http://nvd.nist.gov/vuln/detail/CVE-2024-38644
- https://www.quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident 
 QNAP Critical Flaws in NAS and Router Software 

#### Root cause 
 Multiple critical vulnerabilities in QNAP NAS and router software, including: - **CVE-2024-38643**: Missing authentication in Notes Station 3, a critical function vulnerability allowing unauthorized access (CVSS v4 score: 9.3, critical) *Your changes* (https://securityonline.info/critical-vulnerabilities-in-qnap-notes-station-3-update-now-to-protect-your-data/). - **CVE-2024-38645**: SSRF vulnerability in Notes Station 3 allowing server-side manipulation (CVSS v4 score: 9.3, critical) *Your changes - CWE-918, impacts confidentiality, integrity, and availability, exploit price $0-$5k* (https://vuldb.com/?id.285886). - **CVE-2024-48860**: OS command injection in QuRouter 2.4.x allowing remote code execution (CVSS v4 score: 9.5, critical). - **CVE-2024-38644**: Command injection and unauthorized data access in Notes Station 3 allowing remote authenticated attackers to execute commands (CVSS v4 score: 8.7) *Your changes - CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N* (http://nvd.nist.gov/vuln/detail/CVE-2024-38644). - *Your changes - Exploit prediction scoring system (EPSS) score for CVE-2024-38644 is 0.04%* (https://www.cvedetails.com/cve/CVE-2024-38644/). - **CVE-2024-38646**: Command injection and unauthorized data access in Notes Station 3 (CVSS v4 scores: 8.7, 8.4). - **CVE-2024-48861**: Less severe command injection in QuRouter. - **CVE-2024-38647**: Information exposure in QNAP AI Core (CVSS v4 score: 8.7). - **CVE-2024-48862**: Link-following flaw in QuLog Center (CVSS v4 scores: 7.7). - **CVE-2024-50396**, **CVE-2024-50397**: Improper handling of format strings in QTS and QuTS Hero (CVSS v4 scores: 7.7, 8.4). - *Your changes - Other impacted products include Photo Station and Media Streaming Add-on* (https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908) - *Release date: November 23, 2024* (https://www.qnap.com/en-us/security-advisory/qsa-24-36) - *Affected products: Notes Station 3 version 3.9.x* (https://www.qnap.com/en-us/security-advisory/qsa-24-36); *QuRouter 2.4.x* (https://www.qnap.com/en-au/security-advisory/qsa-24-44) - *Fixed version: Notes Station 3 version 3.9.7 and later* (https://www.qnap.com/en-us/security-advisory/qsa-24-36); *QuRouter 2.4.3.106 and later* (https://www.qnap.com/en-au/security-advisory/qsa-24-44) - *Your changes - CWE-77: Improper Neutralization of Special Elements used in a Command ('Command Injection')* (https://www.cvedetails.com/cve/CVE-2024-38644/) - *Your changes - CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')* (https://www.cvedetails.com/cve/CVE-2024-38644/) - *Acknowledgements: Thomas Fady* (https://www.qnap.com/en-us/security-advisory/qsa-24-36); *Midnight Blue / PHP Hooligans* (https://www.qnap.com/en-au/security-advisory/qsa-24-44). 

#### Threat actor/group/campaign 
 Not specified 

#### Organization/industry/location 
 QNAP users, primarily in businesses utilizing NAS and secure routers. *Your changes - Industrial IoT, smart cities, healthcare sectors* (https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908). *Your changes - Opportunistic targeting* (https://www.quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3/) 

#### Start date � End date 
 November 25, 2024 (disclosure date) 

#### MITRE TTPs 
 - T1190: Exploit Public-Facing Application (CVSS v4 score: 9.3, critical) - High confidence - T1203: Exploitation for Client Execution (CVSS v4 score: 9.5, critical) - High confidence - T1071: Application Layer Protocol (SSRF vulnerability) - Moderate confidence - T1070: Indicator Removal on Host (Command injection) - Moderate confidence - T1040: Network Sniffing (Information exposure) - Moderate confidence *Your changes - T1068: Exploitation for Privilege Escalation* (https://www.quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3/) *Your changes - T1078: Valid Accounts* (https://www.quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3/) *Your changes - T1059: Command and Scripting Interpreter* (https://www.quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3/) 

#### Impact 
 Potential unauthorized access, remote code execution, information exposure, data theft, and manipulation of sensitive data. *Your changes - This is the second patch within a year for certain products, including QTS and QuTS Hero* (https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908). *Your changes - Data exposure* (https://www.quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3/) 

#### Mitigation Steps 
 - Update QNAP Notes Station 3 to version 3.9.7 or later. - Go to QNAP Notes Station 3 settings. - Check for updates and install the latest version. - Update QuRouter to version 2.4.3.106. - Log in to QuRouter and go to Firmware. - Select 'Update now' and click 'Apply' to install the latest version. - Update QNAP AI Core to version 3.4.1 or later. - Update QuLog Center to version 1.7.0.831 or later. - Update QTS to version 5.2.1.2930 and QuTS Hero to version h5.2.1.2929. - Access the respective application settings. - Check for updates and install the latest versions. - Ensure QNAP devices are not directly accessible from the internet. Deploy behind a VPN for remote access. - Configure firewall settings to block external access. - Set up a VPN for secure remote connections. 

#### Detection Signature 
 - Service: QNAP NAS, QuRouter - Port: Various (dependent on specific service configurations) - Severity: Critical - Incident: QNAP Critical Flaws - Signature name: 'QNAP vulnerability exploitation attempt' - Internal checks: - Setting1: Ensure QNAP software is up to date. � In platform - Setting2: Verify QNAP devices are not exposed to the external internet. � Inside VMs - Setting3: Configure QNAP applications to use strong authentication mechanisms. � Inside VMs - External scanning: - Monitor for known vulnerabilities in QNAP devices. - Scan for unauthorized access attempts and command injection patterns. *Your changes - Monitor for opportunistic targeting* (https://www.quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3/) 

#### IoCs:
- url: https://www.qnap.com/en-uk/security-advisory/qsa-24-44 ([link](https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908)) 
Not found for url https://www.qnap.com/en-uk/security-advisory/qsa-24-44 in VT. 

- url: https://www.qnap.com/en-uk/security-advisory/qsa-24-39 ([link](https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908)) 
Not found for url https://www.qnap.com/en-uk/security-advisory/qsa-24-39 in VT. 

- url: https://www.qnap.com/en-uk/security-advisory/qsa-24-40 ([link](https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908)) 
Not found for url https://www.qnap.com/en-uk/security-advisory/qsa-24-40 in VT. 

- url: https://www.qnap.com/en-uk/security-advisory/qsa-24-47 ([link](https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908)) 
Not found for url https://www.qnap.com/en-uk/security-advisory/qsa-24-47 in VT. 

- url: https://www.qnap.com/en-uk/security-advisory/qsa-24-43 ([link](https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908)) 
Not found for url https://www.qnap.com/en-uk/security-advisory/qsa-24-43 in VT. 

- hash_sha1: CVE-2024-38643 ([link](https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908)) 
Not found for hash_sha1 CVE-2024-38643 in VT. 

- hash_sha1: CVE-2024-38644 ([link](https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908)) 
Not found for hash_sha1 CVE-2024-38644 in VT. 

- hash_sha1: CVE-2024-38645 ([link](https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908)) 
Not found for hash_sha1 CVE-2024-38645 in VT. 

- hash_sha1: CVE-2024-38646 ([link](https://www.govinfosecurity.com/qnap-systems-fixes-bugs-in-qurouter-notes-station-3-a-26908)) 
Not found for hash_sha1 CVE-2024-38646 in VT. 

- url: https://www.qnap.com/en/security-advisory/qsa-24-36 ([link](http://nvd.nist.gov/vuln/detail/CVE-2024-38644)) 
Not found for url https://www.qnap.com/en/security-advisory/qsa-24-36 in VT. 

- url: https://www.qnap.com/en-us/security-advisory/qsa-24-36 ([link](https://www.qnap.com/en-us/security-advisory/qsa-24-36)) 
Not found for url https://www.qnap.com/en-us/security-advisory/qsa-24-36 in VT. 

- url: https://www.qnap.com/en-us/security-advisory/qsa-24-40 ([link](https://www.bleepingcomputer.com/news/security/qnap-addresses-critical-flaws-across-nas-router-software)) 
Not found for url https://www.qnap.com/en-us/security-advisory/qsa-24-40 in VT. 

- url: https://www.qnap.com/en-us/security-advisory/qsa-24-43 ([link](https://www.bleepingcomputer.com/news/security/qnap-addresses-critical-flaws-across-nas-router-software)) 
Not found for url https://www.qnap.com/en-us/security-advisory/qsa-24-43 in VT. 

- domain: securityonline.info ([link](https://securityonline.info/critical-vulnerabilities-in-qnap-notes-station-3-update-now-to-protect-your-data)) 

- email: nvd@nist.gov ([link](http://nvd.nist.gov/vuln/detail/CVE-2024-38644)) 
Not found for email nvd@nist.gov in VT. 

- email: soc@us-cert.gov ([link](http://nvd.nist.gov/vuln/detail/CVE-2024-38644)) 
Not found for email soc@us-cert.gov in VT. 

- domain: quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3/ ([link](https://www.quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3)) 
Not found for domain quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3/ in VT. 

- url: https://www.heise.de/en/news/Multiple-software-vulnerabilities-jeopardize-Qnap-NAS-10172887.html ([link](https://www.quorumcyber.com/threat-intelligence/urgent-security-alert-qnap-unveils-critical-vulnerabilities-in-notes-station-3)) 
Not found for url https://www.heise.de/en/news/Multiple-software-vulnerabilities-jeopardize-Qnap-NAS-10172887.html in VT. 

- For more IoCs, please refer to the above links. 

#### paste IoC
securityonline.info

