# Typosquatting Campaign Delivers r77 Rootkit via npm

Incident: Typosquatting campaign delivers r77 rootkit via npm

Root cause: Typosquatting on npm repository

Impact: Approximately 700 downloads of the malicious package. Specific impact on devices, people, and financial losses is unclear from the report.

Mitigation: Implement stringent security measures for npm package management.
- Detailed Steps for Mitigation:
  1. Educate developers about the risks of typosquatting and encourage careful scrutiny of package names.
  2. Implement automated tools to scan npm packages for suspicious activities or behaviors.
  3. Enforce strict policies for npm package usage, including verifying the authenticity of package sources.
  4. Regularly audit and review all third-party packages used in development to ensure they are legitimate and safe.
  5. Use security platforms designed to monitor and analyze software supply chains for early detection of malicious activities.

Detection Signature:
- Service: npm
- Port: N/A (since it's a package management issue, not a network service issue)
- Severity: Critical
- Incident: Typosquatting campaign on npm
- Signature name: “Malicious npm package detected”
  - Internal checks:
    - Setting1: Ensure npm packages are sourced from trusted registries.
    - Setting2: Implement monitoring of npm package usage within development environments.
    - Setting3: Secure npm registry accounts with strong authentication mechanisms.
  - External scanning:
    - Monitor public npm repositories for newly published packages with names similar to popular packages.
    - Check for the presence of known malicious signatures in npm packages.

IoCs:
- npm packages:
  - node-hide-console-windows 1.5.7: cbb162d0623ff74925ecd4cfff7faef87bf45efd
  - node-hide-console-windows 1.5.6: af0dbb3f13dc432924092783fe30433c24b3c929
  - node-hide-console-windows 1.5.4: 54ea32fa0c81c4da247121aa3c9aaf218b9e27f9
  - node-hide-console-windows 1.4.4: c24c666979267304ed42748153301fdadf46d40e
  - node-hide-console-windows 1.3.4: f58431d141672cde5df4dfa82cb02f1df35fe6b8
  - node-hide-console-windows 1.2.4: 6cc6f76d75887485e0614e74acb2fb5c5bc55628
  - node-hide-console-windows 1.2.3: 74a3f8f5bf9ceefd95ad7102de9049250d501369
  - node-hide-console-windows 1.2.2: 08e4acca3c4a87c90141fc9ef90fe7974e4bccf3
  - node-hide-console-windows 1.1.2: d40b6f93acb2b88a88a42f9fc4163ec4449b68e6
  - node-hide-console-windows 1.1.0: b93898d08b3b6263a168bf9f13a5aa05761ab6c4
- Second stage payloads:
  - SHA1: 1563b5814b7dd655892a80be3a6cc740dad282a3
  - SHA1: 43feaf19f1a7410358ab8cd51f00b2446d62e798

Additional IoCs:
- Bot token: MTEzNTM5NDcwMTk3ODEwODAxNg.GtdDHG.Aaj0Z8_IKQtFSG2p6VIQeDqNBvd-PkLeTD8WnE
- Guild ID: 1140853704396902591
