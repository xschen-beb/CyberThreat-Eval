Source: [https://www.welivesecurity.com/en/eset-research/eset-takes-part-global-operation-disrupt-grandoreiro-banking-trojan/](https://www.welivesecurity.com/en/eset-research/eset-takes-part-global-operation-disrupt-grandoreiro-banking-trojan/)

# ESET Takes Part in Global Operation to Disrupt the Grandoreiro Banking Trojan

Incident: Grandoreiro Banking Trojan Disruption

Root cause: Insecure hosting of Command and Control servers on cloud providers

Impact: Approximately 551 unique victims affected daily, leading to potential financial losses from compromised banking credentials and unauthorized transactions. The financial losses could be significant but are not detailed in the report.

Mitigation: Secure the hosting environment by implementing strict access controls and regular monitoring of server activities. Detailed steps for mitigation include:
- Use firewall rules to restrict access to C&C servers.
- Implement multi-factor authentication (MFA) for accessing cloud resources.
- Monitor and audit server activities regularly to detect any unauthorized access or configuration changes.
- Use endpoint detection and response (EDR) solutions to monitor for malware activity on victim machines.
- Educate users on phishing and social engineering tactics to reduce the initial compromise.

Detection Signature:
Service: No-IP Dynamic DNS
Port: Varies (commonly HTTP/HTTPS ports)
Severity: Critical
Incident: Unauthorized C&C server operation
Signature name: “No-IP Dynamic DNS usage for C&C”
Internal checks:
  - Setting1: Monitor for unusual domain resolutions associated with No-IP Dynamic DNS services.
  - Setting2: Implement network traffic analysis to detect communication with known malicious IPs.
  - Setting3: Use threat intelligence feeds to update C&C server blocklists regularly.
External scanning:
  - Monitor for newly registered No-IP domains.
  - Check for communication with known malicious domains/IPs.

IoCs:
Files:
- FB32344292AB36080F2D040294F17D39F8B4F3A8
- 08C7453BD36DE1B9E0D921D45AEF6D393659FDF5
- A99A72D323AB5911ADA7762FBC725665AE01FDF9
- 4CDF7883C8A0A83EB381E935CD95A288505AA8B8

Network:
- 20.237.166[.]161 (Azure, C&C server)
- 20.120.249[.]43 (Azure, C&C server)
- 52.161.154[.]239 (Azure, C&C server)
- 167.114.138[.]249 (OVH, C&C server)
- 66.70.160[.]251 (OVH, C&C server)
- 167.114.4[.]175 (OVH, C&C server)
- 18.215.238[.]53 (AWS, C&C server)
- 54.219.169[.]167 (AWS, C&C server)
- 3.144.135[.]247 (AWS, C&C server)
- 77.246.96[.]204 (VDSina, C&C server)
- 185.228.72[.]38 (Master da Web, C&C server)
- 62.84.100[.]225 (VDSina, Distribution server)
- 20.151.89[.]252 (Azure, Distribution server)

No IoCs found.
