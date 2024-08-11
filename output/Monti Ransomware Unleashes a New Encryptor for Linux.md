Source: [https://www.trendmicro.com/en_us/research/23/h/monti-ransomware-unleashes-a-new-encryptor-for-linux.html](https://www.trendmicro.com/en_us/research/23/h/monti-ransomware-unleashes-a-new-encryptor-for-linux.html)

# Monti Ransomware Unleashes a New Encryptor for Linux

Incident: Monti Ransomware Attack on Linux Systems

Root cause: Vulnerable Linux systems with insufficient security measures

Impact: Legal and government sectors targeted, exact number of devices and financial losses not specified.

Mitigation: 
1. Implement multifactor authentication (MFA) to prevent attackers from moving laterally within the network.
2. Follow the 3-2-1 backup rule: Create three copies of your data, store them in two different formats, and keep one copy offsite.
3. Employ advanced security solutions such as Trend Vision One™, Trend Cloud One™ – Workload Security, Trend Micro™ Deep Discovery™ Email Inspector, and Trend Micro Apex One™.
4. Regularly update and patch systems to close vulnerabilities that ransomware can exploit.

Detection Signature:
    Service: OpenSSH (or another SSH service)
    Port: Commonly 22 (but can vary)
    Severity: Critical
    Incident: Monti Ransomware Activity
    Signature name: “Monti Ransomware Indicators”
    Internal checks:
        - Setting1: Ensure OpenSSH service is configured securely – In platform
        - Setting2: Verify that SSH port (22) is not exposed to the Internet unless absolutely necessary – Inside VMs
        - Setting3: Enforce strong, unique passwords and use MFA for SSH access – Inside VMs
    External scanning:
        - Port (22) open
        - Indicators of compromise related to Monti ransomware

IoCs:
    Hashes:
        - f1c0054bc76e8753d4331a881cdf9156dd8b812a
        - a0c9dd3f3e3d0e2cd5d1da06b3aac019cdbc74ef
    URLs:
        - hxxp://monti5o7lvyrpyk26lqofnfvajtyqruwatlfaazgm3zskt3xiktudwid[.]onion
        - hxxp://mblogci3rudehaagbryjznltdp33ojwzkq6hn2pckvjq33rycmzczpid[.]onion

By adhering to these mitigation steps and detection signatures, organizations can better protect themselves from ransomware attacks like Monti.
