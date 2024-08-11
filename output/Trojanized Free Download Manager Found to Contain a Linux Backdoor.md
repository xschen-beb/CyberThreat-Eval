Source: [https://securelist.com/backdoored-free-download-manager-linux-malware/110465/](https://securelist.com/backdoored-free-download-manager-linux-malware/110465/)

# Trojanized Free Download Manager Found to Contain a Linux Backdoor

Incident: Trojanized Free Download Manager found to contain a Linux backdoor

Root cause: Supply chain attack involving a compromised Debian repository

Impact: Potentially hundreds of thousands of devices affected globally, as indicated by the widespread discussion on social networks and forums. Financial losses are difficult to estimate but could be significant due to data theft, system compromise, and potential follow-up attacks on stolen credentials and information.

Mitigation: 
1. **Verification of Software Sources:** Ensure that all software packages are downloaded from verified and trusted sources. Always verify checksums and digital signatures of downloaded packages.
2. **Regular Audits:** Conduct regular security audits of software repositories and implement stringent access controls to prevent unauthorized changes.
3. **Endpoint Security:** Deploy and maintain comprehensive endpoint security solutions capable of detecting and preventing malware infections.
4. **Network Monitoring:** Implement DNS monitoring to detect and block suspicious domains and unusual traffic patterns.
5. **User Education:** Educate users about the risks of downloading software from untrusted sources and the importance of verifying download links.

**Detailed Steps for mitigation:**
1. **Checksum Verification:**
    - Always check the SHA-256 or MD5 checksums of downloaded files against those provided by the official source.
2. **Repository Security:**
    - Implement multi-factor authentication (MFA) and role-based access control (RBAC) for repository maintenance.
    - Regularly audit access logs and repository contents for unauthorized changes.
3. **Endpoint Protection:**
    - Install and configure Linux-compatible endpoint protection software to detect and mitigate threats.
    - Enable regular scans and real-time protection features.
4. **Network Security:**
    - Monitor and analyze DNS traffic for unusual patterns and block known malicious domains.
    - Deploy intrusion detection/prevention systems (IDS/IPS) to monitor network traffic for signs of compromise.
5. **User Training:**
    - Conduct regular training sessions on cybersecurity best practices.
    - Provide guides on how to verify software integrity and report suspicious activities.

Detection Signature:
- Service: HTTP/HTTPS
- Port: 80/443
- Severity: Critical
- Incident: Trojanized Free Download Manager
- Signature name: “Infected FDM package download”
- Internal checks: 
    - Setting1: Ensure all downloaded packages are verified against known good checksums.
    - Setting2: Monitor cron jobs for unexpected entries.
    - Setting3: Ensure no unauthorized binaries are found in /var/tmp/ or similar directories.
- External scanning:
    - Suspicious DNS queries to fdmpkg[.]org
    - Unusual outbound connections to 172.111.48[.]101

IoCs:
- Domains:
    - 2c9bf1811ff428ef9ec999cc7544b43950947b0f.u.fdmpkg[.]org
    - c6d76b1748b67fbc21ab493281dd1c7a558e3047.u.fdmpkg[.]org
    - 0727bedf5c1f85f58337798a63812aa986448473.u.fdmpkg[.]org
    - c3a05f0dac05669765800471abc1fdaba15e3360.u.fdmpkg[.]org
    - deb.fdmpkg[.]org
    - fdmpkg[.]org
- IP Address:
    - 172.111.48[.]101
- File checksums:
    - b77f63f14d0b2bde3f4f62f4323aad87194da11d71c117a487e18ff3f2cd468d (Malicious Debian Package)
    - 2214c7a0256f07ce7b7aab8f61ef9cbaff10a456c8b9f2a97d8f713abd660349 (crond backdoor)
    - 93358bfb6ee0caced889e94cd82f6f417965087203ca9a5fce8dc7f6e1b8a3ea (bs backdoor)
    - d73be6e13732d365412d71791e5eb1096c7bb13d6f7fd533d8c04392ca0b69b5 (atd uploader)
- File paths:
    - /etc/cron.d/collect
    - /var/tmp/crond
    - /var/tmp/bs
    - /var/tmp/atd

This information should help in understanding the issue, detecting it if present in your systems, and taking preventive measures to mitigate the risk.
