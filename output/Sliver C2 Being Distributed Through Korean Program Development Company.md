Source: [https://asec.ahnlab.com/en/55652/](https://asec.ahnlab.com/en/55652/)

# Sliver C2 Being Distributed Through Korean Program Development Company

Incident: Sliver C2 Being Distributed Through Korean Program Development Company

Root cause: Compromise of the program development company's software distribution channels, allowing threat actors to distribute malware-laden installers signed with valid certificates from the company.

Impact: Exact number of devices and financial losses are not specified in the report. However, considering the distribution through widely used VPN and marketing software, the impact could potentially affect thousands of users and result in substantial financial losses due to data breaches and system compromises.

Mitigation: Implement stringent security measures for software distribution channels and ensure the integrity of distributed files. 
- **Detailed Steps for mitigation:**
  1. **Code and Certificate Security:**
     - Regularly audit and secure code-signing certificates.
     - Implement multi-factor authentication (MFA) for access to code-signing processes.
     - Rotate and revoke compromised certificates immediately.
  2. **Software Distribution Security:**
     - Use secure and trusted channels for software distribution.
     - Implement integrity checks (such as code signing) to ensure the authenticity of software updates.
  3. **Monitoring and Incident Response:**
     - Continuously monitor software distribution platforms for unauthorized changes.
     - Establish a rapid incident response plan to address potential compromises.
  4. **User Awareness and Education:**
     - Educate users on the importance of downloading software from verified sources.
     - Encourage users to verify digital signatures of downloaded installers.
  5. **Regular Security Reviews:**
     - Conduct regular security reviews and penetration testing of software distribution infrastructure.
     - Ensure compliance with best practices and industry standards for software security.

Detection Signature:
- Service: Go-based malware (Sliver C2, MeshAgent, etc.)
- Port: 443 (commonly used for HTTPS-based C2 communications)
- Severity: Critical
- Incident: Sliver C2 distribution
- Signature name: “Go-based Malware Installer Distribution”
- Internal checks:
  - Setting1: Ensure all software installers are verified and signed correctly.
  - Setting2: Regularly audit software distribution channels for unauthorized changes.
  - Setting3: Implement strict access controls and monitoring on code-signing infrastructure.
- External scanning:
  - Verify the authenticity of downloaded installers.
  - Check for unauthorized or suspicious network communications (e.g., to the C2 URLs mentioned).

IoCs:
- MD5 Hashes:
  - 10298c1ddae73915eb904312d2c6007d
  - 1906bf1a2c96e49bd8eba29cf430435f
  - 23f72ee555afcd235c0c8639f282f3c6
  - 27a24461bd082ec60596abbad23e59f2
  - 499f0d42d5e7e121d9a751b3aac2e3f8

- URLs:
  - hxxps://config.v6[.]army/sans.woff2
  - hxxps://panda.sect[.]kr
  - hxxps://speed.ableoil[.]net
  - hxxps://status.devq[.]workers.dev

Additional IOCs are available on AhnLab TIP.
