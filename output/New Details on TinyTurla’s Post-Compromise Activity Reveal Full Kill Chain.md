Source: [https://blog.talosintelligence.com/tinyturla-full-kill-chain/](https://blog.talosintelligence.com/tinyturla-full-kill-chain/)

# New Details on TinyTurla’s Post-Compromise Activity Reveal Full Kill Chain

Incident: TinyTurla Post-Compromise Activities

Root cause: Misconfigured Windows services and lack of proper anti-virus exclusions.

Impact: The specific number of devices, people impacted, and financial losses are not mentioned in the blog.

Mitigation: Apply security best practices on Windows services and anti-virus configurations to prevent unauthorized modifications.
  - Ensure all Windows services are properly configured and monitored.
  - Regularly update and patch all systems to prevent exploitation of known vulnerabilities.
  - Implement strong anti-virus policies that prevent unauthorized exclusions or modifications.
  - Use network segmentation to limit lateral movement within the network.
  - Implement multi-factor authentication (MFA) to secure access to critical systems.

Detailed Steps for mitigation:
  1. Audit and review all Windows services, ensuring that only required services are running and configured securely.
  2. Regularly update all anti-virus definitions and configurations, and ensure they are protected from unauthorized changes.
  3. Implement strict network segmentation to contain potential breaches and limit the movement of attackers within the network.
  4. Deploy multi-factor authentication (MFA) for all critical systems and services.
  5. Monitor network traffic for unusual activities, such as unauthorized data exfiltration attempts or unexpected remote connections.
  6. Utilize endpoint detection and response (EDR) solutions to identify and mitigate threats in real-time.
  7. Conduct regular security training and awareness programs for employees to recognize and report suspicious activities.

Detection Signature:
  Service: Windows Remote Management (WinRM)
  Port: 5985, 5986
  Severity: Critical
  Incident: TinyTurla Post-Compromise Activities
  Signature name: “Unauthorized WinRM Connections”
  Internal checks:
    - Setting1: Ensure WinRM ports (5985, 5986) are not exposed to the external Internet. – In platform
    - Setting2: Verify that WinRM ports (5985, 5986) are not listening on the external Internet. – Inside VMs
    - Setting3: Ensure WinRM service is secured with authentication credentials and limited to authorized users. – Inside VMs
  External scanning:
    - Port (5985, 5986) open
    - Unsecured WinRM connections

IoCs:
  Hashes:
    - 267071df79927abd1e57f57106924dd8a68e1c4ed74e7b69403cdcdf6e6a453b
    - d6ac21a409f35a80ba9ccfe58ae1ae32883e44ecc724e4ae8289e7465ab2cf40
    - ad4d196b3d85d982343f32d52bffc6ebfeec7bf30553fa441fd7c3ae495075fc
    - 13c017cb706ef869c061078048e550dba1613c0f2e8f2e409d97a1c0d9949346
    - b376a3a6bae73840e70b2fa3df99d881def9250b42b6b8b0458d0445ddfbc044

  Domains:
    - hanagram[.]jp
    - thefinetreats[.]com
    - caduff-sa[.]ch
    - jeepcarlease[.]com
    - buy-new-car[.]com
    - carleasingguru[.]com

  IP Addresses:
    - 91[.]193[.]18[.]120
