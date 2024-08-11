Source: [https://asec.ahnlab.com/en/51908/](https://asec.ahnlab.com/en/51908/)

# CoinMiner (KONO DIO DA) Distributed to Linux SSH Servers

Incident: "KONO DIO DA" CoinMiner Distributed to Linux SSH Servers

Root cause: Poorly managed and unsecured SSH services

Impact: The specific number of devices, people impacted, and the financial losses are not provided in the document. However, the general impact includes unauthorized access to Linux SSH servers, potential data theft, and usage of system resources for coin mining, which can result in significant operational and financial losses for affected organizations.

Mitigation: 
- Secure SSH services by following these detailed steps:
  1. **Use Strong Passwords**: Ensure all accounts, especially administrative ones, use strong, complex passwords that are regularly updated.
  2. **Disable Root Login**: Configure SSH to disallow root login by setting `PermitRootLogin no` in the SSH configuration file (`/etc/ssh/sshd_config`).
  3. **Implement Two-Factor Authentication (2FA)**: Use multi-factor authentication to add an extra layer of security.
  4. **Limit SSH Access**: Restrict SSH access to specific IP addresses using firewall rules.
  5. **Change Default SSH Port**: Change the default SSH port (22) to a non-standard port to reduce the risk of automated attacks.
  6. **Use SSH Key Authentication**: Prefer SSH key-based authentication over password authentication and store private keys securely.
  7. **Regularly Update and Patch Systems**: Ensure all systems are up-to-date with the latest security patches and updates.
  8. **Monitor and Log SSH Access**: Use intrusion detection systems (IDS) and log monitoring tools to detect and alert on suspicious SSH activities.
  9. **Disable Unnecessary Services**: Disable any unused services to minimize the attack surface.

Detection Signature:
  - Service: SSH
  - Port: 22 (or a custom non-standard port if changed)
  - Severity: Critical
  - Incident: Unauthorized SSH Access and CoinMiner Installation
  - Signature name: "Unauthorized SSH Access and CoinMiner Installation"
  - Internal checks:
    - Setting1: Ensure SSH port (22 or custom) is not exposed to the external Internet without strict controls – In platform
    - Setting2: Ensure SSH port (22 or custom) does not listen on external Internet without proper firewall rules – Inside VMs
    - Setting3: Enforce the use of strong authentication credentials and/or SSH keys for SSH access – Inside VMs
  - External scanning:
    - Port (22 or custom) open
    - Detect brute-force login attempts and unauthorized access attempts

IoCs:
- IPs: 23.224.232[.]68, 46.41.150[.]129, 141.95.19[.]91, 2.58.149[.]237
- URLs: 
  - http[:]//141[.]95[.]19[.]91[:]8080/xri/config[.]json
  - http[:]//141[.]95[.]19[.]91[:]8080/xri/xri
  - http[:]//2[.]58[.]149[.]237[:]6972/hoze
  - http[:]//2[.]58[.]149[.]237[:]6972/xri2[.]tar
  - http[:]//46[.]41[.]150[.]129/[.]bo/am
- FQDNs: init[.]sh, root[.]sh, uninstall[.]sh
- MD5 Hashes: 
  - 1192697ed3d2302bec3ee828c154e300
  - 1932d2e4081f6dd5c8b32d29b1ab5caf
  - 1db93cb95e409769561efb66e4fd5c72
  - 20ac8a45d129e3ce3444494d9672692c
  - 254784ca05bdd3928d7889d0ea3195ab

Additional IOCs are available on AhnLab TIP.
