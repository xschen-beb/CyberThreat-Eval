# NoName057(16) – The Pro-Russian Hacktivist Group Targeting NATO

Incident: NoName057(16) DDoS Campaign Targeting NATO

Root cause: Misused public services and platforms (Telegram, GitHub) for coordination and tool distribution.

Impact: Multiple government organizations and critical infrastructures in NATO countries disrupted. Exact financial losses and number of impacted devices/people are not specified.

Mitigation: 
1. **Monitor and Report Abuse on Public Platforms**:
   - Regular monitoring of public platforms like Telegram and GitHub for malicious activities.
   - Report any abuse or suspicious activities to the platform's Trust & Safety teams promptly, as done with GitHub.

2. **Enhanced Network Security Measures**:
   - Implement robust DDoS protection solutions, such as rate limiting, Web Application Firewalls (WAF), and DDoS mitigation services.
   - Ensure continuous monitoring and anomaly detection to identify and respond to DDoS attacks in real-time.

3. **Public Awareness and Training**:
   - Conduct awareness programs for organizations about the potential misuse of public platforms for coordinating cyber attacks.
   - Train staff to recognize and report any suspicious activities or communications.

4. **Collaborate with Law Enforcement and CERT**:
   - Work closely with law enforcement and Computer Emergency Response Teams (CERT) to share intelligence and coordinate response efforts.
   - Follow procedures to notify relevant authorities, as done with the Czech CERT.

**Detailed Steps for Mitigation**:
1. **Platform Monitoring and Reporting**:
   - Regularly scan public platforms for mentions of your organization or related keywords.
   - Establish a reporting protocol for abuse to platform administrators.

2. **Network Security Enhancements**:
   - Deploy DDoS protection services at the network edge.
   - Configure firewalls and intrusion prevention systems to detect and block malicious traffic.
   - Use load balancers to distribute traffic and prevent single points of failure.

3. **Awareness and Training**:
   - Conduct regular training sessions on recognizing cyber threats.
   - Distribute guidelines and best practices for safe use of public platforms.
   - Encourage reporting of any suspicious activities to internal security teams.

4. **Collaboration with Authorities**:
   - Maintain an updated contact list of local and international CERTs.
   - Share threat intelligence with relevant authorities in a timely manner.
   - Participate in joint exercises and simulations to improve coordination.

Detection Signature:
- **Service**: GitHub, Telegram
- **Port**: Not applicable (platform-based)
- **Severity**: Critical
- **Incident**: NoName057(16) DDoS Campaign
- **Signature name**: “NoName057(16) Public Platform Abuse”
- **Internal checks**:
  - **Setting1**: Monitor GitHub repositories for malicious code or tools.
  - **Setting2**: Monitor Telegram channels for mentions of your organization or related keywords.
  - **Setting3**: Secure internal communication channels and educate staff on the risks of public platforms.
- **External scanning**:
  - **Check1**: Monitor public GitHub repositories for new commits related to known attack tools.
  - **Check2**: Regularly search for and report malicious Telegram channels and groups.

IoCs found:
- Hashes:
  - 94d7653ff2f4348ff38ff80098682242ece6c407
  - e786c3a60e591dec8f4c15571dbb536a44f861c5
  - c86ae9efcd838d7e0e6d5845908f7d09aa2c09f5
  - e78ac830ddc7105290af4c1610482a41771d753f
  - 09a3b689a5077bd89331acd157ebe621c8714a89
  - 8f0b4a8c8829a9a944b8417e1609812b2a0ebbbd
  - 717a034becc125e88dbc85de13e8d650bee907ea
  - ef7b0c626f55e0b13fb1dcf8f6601068b75dc205
  - b63ce73842e7662f3d48c5b6f60a47e7e2437a11
  - 5880d25a8fbe14fe7e20d2751c2b963c85c7d8aa
  - 78248539792bfad732c57c4eec814531642e72a0
  - 1dfc6f6c35e76239a35bfaf0b5a9ec65f8f50522

- IPs:
  - 2.57.122.82
  - 2.57.122.243
  - 109.107.181.130
  - 77.91.122.69
  - 31.13.195.87

- Domains:
  - tom56gaz6poh13f28[.]myftp.org
  - zig35m48zur14nel40[.]myftp.org

- Email:
  - 05716nnm@proton[.]me

- URLs:
  - hxxps://t[.]me/noname05716
  - hxxps://t[.]me/nn05716chat
  - hxxps://github[.]com/dddosia
  - dddosia[.]github.io
  - hxxps://github[.]com/kintechi341
