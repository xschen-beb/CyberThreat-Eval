# Nokoyawa Ransomware Attacks with Windows Zero-Day

Incident: Nokoyawa Ransomware Attacks with Windows Zero-Day

Root cause: Unpatched Windows CLFS (Common Log File System) elevation-of-privilege vulnerability (CVE-2023-28252)

Impact: Multiple small and medium-sized businesses across different regions (Middle East, North America, and Asia) were impacted. The financial losses are not explicitly stated in the document, but ransomware attacks typically result in significant costs related to data recovery, potential ransom payments, and business downtime.

Mitigation: Apply the security patch released by Microsoft for CVE-2023-28252 immediately. 
Detailed Steps for Mitigation:
1. Ensure that all systems running Windows Server 2003 R2, Vista, and later versions are updated with the April 11, 2023, Patch Tuesday updates.
2. Enable automatic updates to ensure future patches are applied promptly.
3. Implement strong access controls and limit user permissions to reduce the risk of privilege escalation.
4. Use behavior-based security solutions to detect and block exploit attempts.
5. Regularly back up critical data and verify the integrity of backups to ensure they can be restored in the event of a ransomware attack.
6. Conduct regular security training for employees to recognize and avoid phishing emails and other common attack vectors.

Detection Signature:
    Service: Microsoft Windows Common Log File System (CLFS)
    Port: Not applicable (local exploit)
    Severity: Critical
    Incident: CVE-2023-28252
    Signature name: “CLFS Elevation of Privilege Exploit”
    Internal checks:
        - Setting1: Ensure systems are patched with the latest security updates – In platform
        - Setting2: Monitor and restrict access to CLFS-related files and functions – Inside VMs
        - Setting3: Use behavior-based detection systems to monitor for unusual activity – Inside VMs
    External scanning:
        - Not applicable (local exploit)

IoCs:
Exploitation artifacts:
    - C:\Users\Public\.container*
    - C:\Users\Public\MyLog*.blf
    - C:\Users\Public\p_*

Hashes:
    - Exploit: 46168ed7dbe33ffc4179974f8bf401aa
    - CobaltStrike loaders:
        - 1e4dd35b16ddc59c1ecf240c22b8a4c4
        - f23be19024fcc7c8f885dfa16634e6e7
        - a2313d7fdb2f8f5e5c1962e22b504a17

CobaltStrike C2s:
    - vnssinc[.]com
    - qooqle[.]top
    - vsexec[.]com
    - devsetgroup[.]com

Nokoyawa ransomware:
    - 8800e6f1501f69a0a04ce709e9fa251c
