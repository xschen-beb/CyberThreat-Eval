Source: [https://www.huntandhackett.com/blog/turkish-espionage-campaigns](https://www.huntandhackett.com/blog/turkish-espionage-campaigns)

# Turkish Espionage Campaigns in the Netherlands

Incident: Turkish Espionage Campaigns in the Netherlands

Root cause: Compromised cPanel accounts and use of publicly accessible GitHub repositories for malicious code

Impact: Multiple organizations targeted, including telecommunication, media, ISPs, and IT service providers. Specific numbers of devices and financial losses are not detailed.

Mitigation: 
1. Deploy Endpoint Detection and Response (EDR) solutions and monitor systems for network connections, executed processes, file creation/modification/deletion, and account activity.
2. Store log files in a central location with sufficient storage capacity for historical forensic investigation purposes.
3. Enforce a password policy with adequate complexity requirements for specific accounts and use a secrets management system.
4. Limit logon attempts on accounts to reduce the chance of successful brute force attacks.
5. Enable two-factor authentication (2FA) on all externally exposed accounts.
6. Keep software up to date to reduce the number of vulnerabilities in externally exposed systems.
7. Reduce the number of systems accessible over the internet using SSH; implement SSH-logon rate limits where necessary.
8. Implement egress network filtering to prevent unauthorized processes such as reverse shells from sending network traffic to disallowed IP addresses.

Detection Signature:
Service: cPanel
Port: 2083 (HTTPS for cPanel)
Severity: Critical
Incident: Unauthorized access and usage of cPanel accounts
Signature name: “cPanel unauthorized access”
Internal checks:
  - Setting1: cPanel should not be accessible from external IP addresses without proper authorization – In platform
  - Setting2: Monitor cPanel login attempts and logins from unfamiliar IP addresses – Inside VMs
  - Setting3: Ensure cPanel accounts use strong, unique passwords and 2FA – Inside VMs
External scanning:
  - Port (2083) open
  - Unfamiliar IP addresses accessing cPanel

IoCs found:
1. IP-address: 82.102.19[.]88 (VPN provider used by Sea Turtle to log on to a cPanel account)
2. IP-address: 62.115.255[.]163 (VPN provider used by Sea Turtle to log on to a cPanel account)
3. IP-address: 193.34.167[.]245 (Used to log on to a cPanel account and download the source code of SnappyTCP malware)
4. Domain name: forward.boord[.]info (Used by SnappyTCP to establish a command-and-control channel)
5. SHA-1 hash: f1a4abd70f8e56711863f9e7ed0a4a865267ec7 (Modified version of the tool Socat used by Sea Turtle)

No additional IoCs found.
