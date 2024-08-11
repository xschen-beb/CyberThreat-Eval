Source: [https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)

# StopRansomware Play Ransomware

Incident: Play Ransomware

Root cause: Exploitation of known FortiOS and Microsoft Exchange vulnerabilities, and abuse of valid accounts.

Impact: Around 300 entities affected. The exact number of devices, people impacted, and financial losses were not mentioned.

Mitigation: 
1. **Implement a recovery plan**: Maintain multiple copies of sensitive data in physically separate, secure locations.
2. **Password policies**: Comply with NIST standards, use long, complex passwords stored in hashed format, and avoid password reuse.
3. **Multifactor authentication (MFA)**: Enable MFA for all services, especially webmail, VPN, and critical accounts.
4. **Patch management**: Regularly update all operating systems, software, and firmware, prioritizing known exploited vulnerabilities.
5. **Network segmentation**: Prevent ransomware spread by controlling traffic flows between subnetworks.
6. **Monitor network activity**: Use network monitoring tools to detect abnormal activity and potential ransomware traversal.
7. **Endpoint detection and response (EDR)**: Deploy tools to detect lateral movement and unusual network connections.
8. **Filter network traffic**: Prevent unknown origins from accessing remote services.
9. **Antivirus measures**: Keep antivirus software updated and enabled for real-time detection.
10. **Review accounts**: Regularly audit accounts with administrative privileges and configure access controls based on least privilege.
11. **Disable unused ports**: Minimize attack surface by disabling unnecessary ports.
12. **Email security**: Add banners to external emails and disable hyperlinks to reduce phishing risks.
13. **Time-based access**: Implement just-in-time access for admin-level accounts.
14. **Disable command-line and scripting**: Prevent privileged escalation and lateral movement.
15. **Offline backups**: Ensure backups are encrypted, immutable, and cover the entire data infrastructure.

Detection Signature:
- **Service**: Microsoft Exchange, FortiOS
- **Port**: Various (depending on specific vulnerabilities)
- **Severity**: Critical
- **Incident**: Play Ransomware
- **Signature name**: "Exploited FortiOS and Microsoft Exchange"
- **Internal checks**:
  - Setting1: Verify that Microsoft Exchange and FortiOS are updated with the latest patches.
  - Setting2: Ensure that external-facing services are configured securely.
  - Setting3: Implement strong password policies and MFA for all accounts.
- **External scanning**:
  - Check for open ports associated with known vulnerabilities.
  - Detect outdated FortiOS and Microsoft Exchange instances.

IoCs:
- **IP**: Not mentioned.
- **Domain**: Not mentioned.
- **Hash**: 
  - 453257c3494addafb39cb6815862403e827947a1e7737eb8168cd10522465deb
  - 47c7cee3d76106279c4c28ad1de3c833c1ba0a2ec56b0150586c7e8480ccae57
  - 75404543de25513b376f097ceb383e8efb9c9b95da8945fd4aa37c7b2f226212
  - 7a42f96599df8090cf89d6e3ce4316d24c6c00e499c8557a2e09d61c00c11986
  - 7a6df63d883bbccb315986c2cfb76570335abf84fafbefce047d126b32234af8
  - 7dea671be77a2ca5772b86cf8831b02bff0567bce6a3ae023825aa40354f8aca
  - c59f3c8d61d940b56436c14bc148c1fe98862921b8f7bad97fbc96b31d71193c
  - e652051fe47d784f6f85dc00adca1c15a8c7a40f1e5772e6a95281d8bf3d5c74
  - e8d5ad0bf292c42a9185bb1251c7e763d16614c180071b01da742972999b95da
