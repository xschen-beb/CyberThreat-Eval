# X-Force Uncovers Global NetScaler Gateway Credential Harvesting Campaign

Incident: NetScaler Gateway Credential Harvesting Campaign

Root cause: Exploitation of CVE-2023-3519 in unpatched NetScaler Gateways.

Impact: Nearly 600 unique victim IP addresses compromised with concentrations in the United States and Europe. The financial losses and the exact number of individuals impacted are not specified in the report.

Mitigation: 
- Apply the latest patches and updates for NetScaler devices to mitigate CVE-2023-3519.
- Implement strong access controls and authentication mechanisms for NetScaler Gateways.
- Regularly audit and monitor NetScaler configurations and access logs for signs of exploitation or unauthorized modifications.
- Secure the NetScaler devices by changing all passwords and certificates stored in configuration files as part of incident remediation.
- Utilize tools to analyze logs within ".gz" archives and ensure logs are not lost due to circular logging configurations.

**Detailed Steps for mitigation:**
1. **Patch Management:**
   - Ensure all NetScaler devices are updated with the latest security patches provided by Citrix.
2. **Access Control:**
   - Implement multi-factor authentication (MFA) for accessing NetScaler Gateways.
   - Restrict access to NetScaler administrative interfaces to trusted IP addresses only.
3. **Configuration Audits:**
   - Regularly review and audit NetScaler configuration files (`/flash/nsconfig/keys/updated/*`, `/nsconfig/ns.conf`) for unauthorized changes.
4. **Log Monitoring:**
   - Monitor access logs (`/var/log/httpaccess.log`, `/var/log/httperror.log`, `/var/log/httpaccess-vpn.log`) for suspicious activity, especially POST/GET requests and anomalous PHP files.
   - Use tools like `zgrep` to search within compressed log files.
5. **Credential and Certificate Management:**
   - Change all passwords and certificates stored in NetScaler configuration files as part of comprehensive incident remediation.
6. **Incident Response:**
   - Follow CISA and X-Force recommendations for evidence collection and analysis, ensuring device logs and crash files (`/var/core/<number>/NSPPE*`) are preserved and reviewed.

Detection Signature:
Service: NetScaler Gateway
Port: 443 (HTTPS)
Severity: Critical
Incident: NetScaler Gateway Credential Harvesting Campaign
Signature name: “NetScaler Gateway CVE-2023-3519 Exploitation”
Internal checks:
  - Setting1: Ensure NetScaler Gateway is updated to the latest firmware. – In platform
  - Setting2: Verify access controls and restrict administrative interface access to trusted IPs. – Inside VMs
  - Setting3: Implement and enforce multi-factor authentication for NetScaler Gateway access. – Inside VMs
External scanning:
  - Port (443) open
  - Unpatched NetScaler Gateway version
  - Presence of modified `index.html` file with references to remote JavaScript files.

IoCs:
- Domains: 
  - jscloud[.]ink
  - jscloud[.]live
  - jscloud[.]biz
  - jscdn[.]biz
  - cloudjs[.]live
  - cloud-js[.]cloud

No additional IoCs (such as IP addresses or file hashes) were provided in the report.
