Source: [https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-trigona](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-trigona)

# Ransomware Spotlight Trigona

Incident: Trigona Ransomware Attack

Root cause: Exploitation of CVE-2021-40539 in Zoho ManageEngine ADSelfService Plus and brute-force attacks on compromised Microsoft SQL (MSSQL) Servers.

Impact: 33 organizations compromised, targeting various industries such as finance, government, technology, retail, and more. Financial losses and the number of impacted devices/people can vary widely depending on the size of the ransoms paid and the operational disruptions caused.

Mitigation: 
1. **Patch and Update Systems Regularly**: Ensure that all software, especially public-facing applications like Zoho ManageEngine ADSelfService Plus, are updated regularly to mitigate known vulnerabilities.
2. **Strengthen Authentication Mechanisms**: Implement multi-factor authentication (MFA) and strong password policies to prevent brute-force attacks on MSSQL servers.
3. **Network Segmentation**: Segment networks to limit the spread of ransomware and isolate critical systems.
4. **Regular Backups**: Maintain regular, encrypted backups and ensure they are stored offline or in a separate network segment.
5. **Incident Response Plan**: Develop and regularly update an incident response plan that includes steps for responding to ransomware attacks.
6. **Employee Training**: Conduct regular training for employees on recognizing phishing attempts and other social engineering tactics.
7. **Endpoint Protection**: Deploy advanced endpoint protection solutions that can detect and mitigate ransomware activities.
8. **Monitor Vulnerabilities**: Use vulnerability assessment tools to monitor and address potential weaknesses within the system infrastructure.

Detection Signature:
- **Service**: Zoho ManageEngine ADSelfService Plus, Microsoft SQL (MSSQL) Server
- **Port**: MSSQL (1433), ADSelfService Plus (varies based on configuration)
- **Severity**: Critical
- **Incident**: Trigona Ransomware Attack
- **Signature name**: “Zoho ManageEngine ADSelfService Plus CVE-2021-40539” and “MSSQL brute-force attack”
  - **Internal checks**:
    - **Setting1**: Ensure Zoho ManageEngine ADSelfService Plus is updated to the latest version. – In platform
    - **Setting2**: Monitor and limit access to MSSQL server ports (1433) to trusted IP addresses only. – Inside VMs
    - **Setting3**: Enforce strong password policies and MFA for MSSQL servers. – Inside VMs
  - **External scanning**:
    - **Port (1433) open**
    - **Zoho ManageEngine ADSelfService Plus vulnerable version detected**

IoCs: 
- No specific IoCs found in the provided document. However, the document suggests that indicators such as file names, registry keys, and specific IP addresses used by Trigona ransomware could be used for detection purposes.

**Example Indicators**:
- File paths: "*._locked", "*available_for_trial*._locked", "*\\how_to_decrypt.txt"
- Process paths: "*\\mshta.exe", "*\\how_to_decrypt.hta"
- Registry keys: "*\\Run\\*", "*\\how_to_decrypt.hta"

These IoCs should be used as a reference to create specific detection rules in your security monitoring systems.
