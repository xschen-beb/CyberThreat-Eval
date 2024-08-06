# Pandas with a Soul Chinese Espionage Attacks Against Southeast Asian Government Entities

**Incident:** Pandas with a Soul: Chinese Espionage Attacks Against Southeast Asian Government Entities

**Root cause:** Misconfigured use of spear-phishing emails with malicious RTF documents and lack of adequate network segmentation and endpoint security.

**Impact:** Multiple high-profile government entities in Southeast Asia, including Vietnam, Thailand, and Indonesia, were impacted. The exact financial losses are undisclosed, but the breach could potentially result in significant costs related to data breaches, espionage, and national security threats.

**Mitigation:**
- **Secure Email Gateways:** Implement advanced email filtering and anti-phishing solutions to detect and block spear-phishing emails.
- **Endpoint Protection:** Deploy advanced endpoint protection solutions with capabilities to detect and block malicious documents and payloads.
- **Network Segmentation:** Isolate critical network segments to contain breaches and prevent lateral movement.
- **User Training:** Conduct regular security awareness training for employees to recognize and report suspicious emails.
- **Incident Response:** Establish an incident response plan that includes immediate steps to contain and remediate detected breaches.
- **Regular Patching:** Ensure that all systems and applications are regularly patched to protect against known vulnerabilities.
- **Multi-Factor Authentication:** Implement multi-factor authentication (MFA) to protect against unauthorized access.

**Detailed Steps for Mitigation:**
1. **Deploy Email Filtering:**
   - Configure email filters to block or quarantine emails with suspicious attachments or links.
   - Use threat intelligence feeds to update email filters with the latest indicators of compromise (IoCs).

2. **Advanced Endpoint Protection:**
   - Install endpoint detection and response (EDR) tools on all critical systems.
   - Regularly update antivirus and antimalware definitions.

3. **Network Segmentation:**
   - Segment the network into isolated zones, ensuring sensitive data is only accessible to authorized users.
   - Use firewalls and access control lists (ACLs) to restrict traffic between network segments.

4. **Security Awareness Training:**
   - Conduct phishing simulation exercises to test employee awareness.
   - Provide training on recognizing phishing attempts and reporting them to the IT security team.

5. **Incident Response Plan:**
   - Develop and document an incident response plan.
   - Conduct regular drills to ensure the team is prepared to respond quickly to incidents.

6. **Regular Patching:**
   - Implement a patch management program.
   - Ensure that patches are tested and applied in a timely manner.

7. **Multi-Factor Authentication:**
   - Require MFA for all remote access and privileged accounts.
   - Educate users on the importance of MFA and how to use it.

**Detection Signature:**
- **Service:** HTTP/HTTPS
- **Port:** 80/443
- **Severity:** Critical
- **Incident:** Pandas with a Soul
- **Signature name:** “Soul Backdoor Network Activity”
- **Internal checks:**
  - Setting1: Ensure HTTP/HTTPS traffic from unknown origins is monitored.
  - Setting2: Check for unusual URL patterns and User-Agent strings in HTTP requests.
  - Setting3: Validate registry keys for unusual entries related to backdoor configurations.
- **External scanning:**
  - Port 80/443 open
  - Unusual HTTP/HTTPS requests with encoded parameters

**IoCs found:**
- **C&C servers:**
  - 45.76.190[.]210
  - 45.197.132[.]68
  - 45.197.133[.]23
  - 103.78.242[.]11
  - 103.159.132[.]96
  - 103.173.154[.]168
  - 103.213.247[.]48
  - 139.180.137[.]73
  - 139.180.138[.]49
  - 152.32.243[.]17
  - office.oiqezet[.]com
- **Hashes:**
  - Phishing documents:
    - 32a0f6276fea9fe5ee2ffda461494a24a5b1f163a300bc8edd3b33c9c6cc2d17
    - ca7f297dc04acad2fab04d5dc2de9475aed4186805f6c237c10b8f56b384cf30
    - 341dee709285286bc5ba94d14d1bce8a6416cb93a054bd183b501552a17ef314
    - 9d628750295f5cde72f16da02c430b5476f6f47360d008911891fdb5b14a1a01
    - 811a020b0f0bb31494f7fbe21893594cd44d90f77fcd1f257925c4ac5fabed43
    - b023e2b398d552aacb2233a6e08b4734c205ab6abf5382ec31e6d5aa7c71c1cb
  - External template (RoyalRoad RTF):
    - 81d9e75d279a953789cbbe9ae62ce0ed625b61d123fef8ffe49323a04fecdb3f
    - 12c1a4c6406ff378e8673a20784c21fb997180cd333f4ef96ed4873530baa8d3
    - f2779c63373e33fdbd001f336df36b01b0360cd6787c1cd29a6524cc7bcf1ffb
    - 7a7e519f82af8091b9ddd14e765357e8900522d422606aefda949270b9bf1a04
    - 4747e6a62fee668593ceebf62f441032f7999e00a0dfd758ea5105c1feb72225
    - 3541f3d15698711d022541fb222a157196b5c21be4f01c5645c6a161813e85eb
  - 5.t Downloader:
    - 0f9f85d41da21781933e33dddcc5f516c5ec07cc5b4cff53ba388467bc6ac3fd
    - 17f4a21e0e8c0ce958baf34e45a8b9481819b9b739f3e48c6ba9a6633cf85b0e
    - f8622a502209c18055a308022629432d82f823dd449abd9b17c61e363a890828
    - 1a15a35065ec7c2217ca6a4354877e6a1de610861311174984232ba5ff749114
    - 065d399f6e84560e9c82831f9f2a2a43a7d853a27e922cc81d3bc5fcd1adfc56
    - 1e18314390302cd7181b710a03a456de821ad85334acfb55f535d311dd6b3d65
    - c4500ad141c595d83f8dba52fa7a1456959fb0bc2ee6b0d0f687336f51e1c14e
    - 390e6820b2cc173cfd07bcebd67197c595f4705cda7489f4bc44c933ddcf8de6
  - SoulSearcher:
    - d1a6c383de655f96e53812ee1dec87dd51992c4be28471e44d7dd558585312e0
  - Soul Backdoor:
    - df5fe7ec6ecca27d3affc901cb06b27dc63de9ea8c97b87bc899a79eca951d60


