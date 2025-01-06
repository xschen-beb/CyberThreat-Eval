Source: [https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform](https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform)

## Related articles (describing the same threat) 
- https://talosintelligence.com/vulnerability_reports/TALOS-2024-1965
- https://talosintelligence.com/vulnerability_reports/TALOS-2024-1970
- https://talosintelligence.com/vulnerability_reports/TALOS-2024-1964
- https://www.cybersecurity-help.cz/vdb/SB2024081395
- https://nvd.nist.gov/vuln/detail/CVE-2024-38186
- https://talosintelligence.com/vulnerability_reports/TALOS-2024-1971
- https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform
- https://nvd.nist.gov/vuln/detail/CVE-2024-38184
- https://talosintelligence.com/vulnerability_reports/TALOS-2024-1966
- https://nvd.nist.gov/vuln/detail/CVE-2024-38185
- https://talosintelligence.com/vulnerability_reports/TALOS-2024-1969

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident 
 Vulnerabilities in ClipSp, the driver at the core of Windows’ Client License Platform 

#### Root cause 
 Multiple vulnerabilities including signature bypass (CVE-2024-38184), out-of-bounds read vulnerabilities (CVE-2024-38185, CVE-2024-38187), License Update Field Type 0xD3 and License Update Field Type 0xCC (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1971) (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1969, https://talosintelligence.com/vulnerability_reports/TALOS-2024-1970), license update privilege escalation (CVE-2024-38186) (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1966), elevation of privileges, and sandbox escape due to inadequate validation and improper handling of input data in ClipSp (clipsp.sys) driver, affecting SPCallServerHandleUpdateLicense function and SPCallServerHandleClepKdf function (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1969). *Additionally, a Windows Kernel-Mode Driver Elevation of Privilege Vulnerability (CVE-2024-38184) with a CVSS 3.1 score of 7.8 has been identified, which affects various Windows versions up to specific build numbers and includes CWE-822 (Untrusted Pointer Dereference)* (https://nvd.nist.gov/vuln/detail/CVE-2024-38185) (https://nvd.nist.gov/vuln/detail/CVE-2024-38184). *CWE-367: TOCTOU race condition is associated with CVE-2024-38186* (https://nvd.nist.gov/vuln/detail/CVE-2024-38186). *Exploitation vector: Local* (https://www.cybersecurity-help.cz/vdb/SB2024081395). 

#### Threat actor/group/campaign 
 No specific threat actor identified. 

#### Organization/industry/location 
 Users of Windows 10 and 11 systems, including Microsoft Windows 11 Pro 23H2 and Microsoft Windows 11 Pro 24H2 Insider Preview (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1969). *Affected versions also include Windows 10 (up to build 10.0.14393.7159), Windows 11 (up to build 10.0.22631.3880), Windows Server 2016, 2019, and 2022 editions* (https://nvd.nist.gov/vuln/detail/CVE-2024-38185) (https://nvd.nist.gov/vuln/detail/CVE-2024-38184). *Newly identified affected configurations include Windows 10 versions 1607, 1809, 21H2, 22H2; Windows 11 versions 21H2, 22H2, 23H2; and Windows Server 2022 23H2* (https://nvd.nist.gov/vuln/detail/CVE-2024-38186). *CPE2.3 identifier for Windows* (https://www.cybersecurity-help.cz/vdb/SB2024081395). 

#### Start date – End date 
 Discovered and reported in 2024. 

#### MITRE TTPs 
 ['T1574.006: Hijack Execution Flow: Dynamic Linker Hijacking (Medium confidence)', 'T1055.012: Process Injection: Process Hollowing (Medium confidence)', 'T1068: Exploitation for Privilege Escalation (High confidence)', 'T1203: Exploitation for Client Execution (High confidence)'] 

#### Impact 
 Potential for privilege escalation, sandbox escape, denial of service (DoS) (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1971), and unauthorized access to system functionalities and data. 

#### Mitigation Steps 
 ['Apply patches and updates provided by Microsoft to address the identified vulnerabilities.', 'Implement strict validation checks for input data to prevent bypass of signature checks.', 'Use secure coding practices to avoid out-of-bound read and write vulnerabilities.', 'Regularly review and update system policies to ensure they align with security best practices.'] 

#### Detection Signature 
 {'Service': 'ClipSp', 'Port': 'N/A', 'Severity': 'Critical', 'Incident': 'Vulnerabilities in ClipSp', 'Signature name': '“ClipSp Vulnerability Detection”', 'Internal checks': ['Ensure ClipSp driver is updated to the latest version – In platform/OS update management', 'Regularly scan for signs of privilege escalation attempts – Inside VMs', 'Monitor for unusual RPC calls to ClipSp functionalities – Inside VMs'], 'External scanning': ['Scan for specific vulnerability signatures in ClipSp driver', 'Monitor for exploit attempts targeting ClipSp vulnerabilities']} 

#### Additional Information 
 An attacker can use the NtQuerySystemInformation function call (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1965) to trigger these vulnerabilities, specifically with a type 0x1 license blob (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1965). The DeviceLicenseInstall function is particularly affected by these vulnerabilities, and the license files are stored in the HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\{7746D80F-97E0-4E26-9543-26B41FC22F79}\{A25AE4F2-1B96-4CED-8007-AA30E9B1A218} key (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1966). Discovered by Philippe Laulheret of Cisco Talos (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1969). CWE-125 - Out-of-bounds Read (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1969). CVSSv3 Score 6.8 (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1970). ExHandleSPCall2 function (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1970). SystemPolicyInformation class and Warbird encryption are involved in the handling of license-related data (https://talosintelligence.com/vulnerability_reports/TALOS-2024-1971). *Microsoft Corporation and CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H are referenced in the NVD CVE-2024-38185* (https://nvd.nist.gov/vuln/detail/CVE-2024-38185). *Microsoft Corporation and CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H are also referenced in the NVD CVE-2024-38186* (https://nvd.nist.gov/vuln/detail/CVE-2024-38186). *Public exploit not available for these vulnerabilities* (https://www.cybersecurity-help.cz/vdb/SB2024081395). 

#### IoCs:
- hash_md5: 254d91c3b82854956cefcc26f7ca91fa ([link](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1966)) 

- email: soc@us-cert.gov ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38184)) 

- url: https://talosintelligence.com/vulnerability_reports/TALOS-2024-1970 ([link](https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform)) 

- email: soc@us-cert.gov ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38186)) 

- email: soc@us-cert.gov ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38185)) 

- url: https://talosintelligence.com/vulnerability_reports/TALOS-2024-1968 ([link](https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform)) 

- url: https://talosintelligence.com/vulnerability_reports/TALOS-2024-1971 ([link](https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform)) 

- url: https://www.talosintelligence.com/vulnerability_reports/TALOS-2024-1964 ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38184)) 

- url: https://talosintelligence.com/vulnerability_reports/TALOS-2024-1965 ([link](https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform)) 

- email: nvd@nist.gov ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38184)) 

- url: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38185 ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38185)) 

- email: nvd@nist.gov ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38186)) 

- url: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38184 ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38184)) 

- hash_md5: 7746D80F-97E0-4E26-9543-26B41FC22F79 ([link](https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform)) 

- email: nvd@nist.gov ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38185)) 

- url: https://www.talosintelligence.com/vulnerability_reports/TALOS-2024-1966 ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38186)) 

- url: https://talosintelligence.com/vulnerability_reports/TALOS-2024-1966 ([link](https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform)) 

- url: https://www.talosintelligence.com/vulnerability_reports/TALOS-2024-1965 ([link](https://nvd.nist.gov/vuln/detail/CVE-2024-38185)) 

- url: https://talosintelligence.com/vulnerability_reports/TALOS-2024-1969 ([link](https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform)) 

- url: https://www.microsoft.com/en-us/windows/windows-11 ([link](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1970)) 

- url: https://www.microsoft.com/en-us/windows/windows-11 ([link](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1971)) 

- url: https://www.microsoft.com/en-us/windows/windows-11 ([link](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1969)) 

- For more IoCs, please refer to the above links. 

#### paste IoC
254d91c3b82854956cefcc26f7ca91fa
soc@us-cert.gov
https://talosintelligence.com/vulnerability_reports/TALOS-2024-1970
soc@us-cert.gov
soc@us-cert.gov
https://talosintelligence.com/vulnerability_reports/TALOS-2024-1968
https://talosintelligence.com/vulnerability_reports/TALOS-2024-1971
https://www.talosintelligence.com/vulnerability_reports/TALOS-2024-1964
https://talosintelligence.com/vulnerability_reports/TALOS-2024-1965
nvd@nist.gov
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38185
nvd@nist.gov
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38184
7746D80F-97E0-4E26-9543-26B41FC22F79
nvd@nist.gov
https://www.talosintelligence.com/vulnerability_reports/TALOS-2024-1966
https://talosintelligence.com/vulnerability_reports/TALOS-2024-1966
https://www.talosintelligence.com/vulnerability_reports/TALOS-2024-1965
https://talosintelligence.com/vulnerability_reports/TALOS-2024-1969
https://www.microsoft.com/en-us/windows/windows-11
https://www.microsoft.com/en-us/windows/windows-11
https://www.microsoft.com/en-us/windows/windows-11

