Source: [https://securityintelligence.com/x-force/hive0051-malicious-operations-enabled-dns-fluxing/](https://securityintelligence.com/x-force/hive0051-malicious-operations-enabled-dns-fluxing/)

# Hive0051’s Large Scale Malicious Operations Enabled by Synchronized Multi-Channel DNS Fluxing

Incident: Hive0051 Multi-Channel DNS Fluxing Operations

Root cause: Advanced multi-channel DNS fluxing and obfuscated multi-stage malware

Impact: 1,027 devices infected in a single 24-hour period. The financial losses are not specified in the report.

Mitigation:  
1. **Secure DNS Infrastructure:**
   - Implement DNS security measures to detect and block fast-fluxing domains.
   - Use DNS-based threat intelligence to identify and block malicious domains.
   
2. **Enhance Email Security:**
   - Deploy advanced email filtering to detect and block phishing emails containing malicious .XHTML, .HTA, .LNK files.
   - Conduct regular employee training on phishing awareness.

3. **Endpoint Protection:**
   - Ensure anti-virus and anti-malware solutions are up to date.
   - Monitor for suspicious processes such as `wscript.exe` and `powershell.exe` with specific arguments.
   - Use endpoint detection and response (EDR) tools to detect fileless malware and registry persistence.

4. **Network Monitoring:**
   - Monitor for suspicious network traffic, especially connections to Telegram and Telegraph services.
   - Implement anomaly detection systems to identify unusual DNS queries and fast-fluxing patterns.

Detailed Steps for mitigation:
   - **DNS Security:**
     - Use DNS security solutions to filter and block fast-fluxing domains.
     - Regularly update DNS blacklists with threat intelligence feeds.
   
   - **Email Security:**
     - Deploy secure email gateways with advanced phishing detection capabilities.
     - Conduct phishing simulation exercises to train employees.
   
   - **Endpoint Protection:**
     - Deploy and regularly update anti-virus and anti-malware solutions.
     - Configure endpoint protection to alert on the execution of `wscript.exe` and `powershell.exe` with suspicious arguments.
     - Use EDR tools to monitor and respond to fileless malware activities.
   
   - **Network Monitoring:**
     - Implement intrusion detection/prevention systems (IDS/IPS) to monitor for malicious network traffic.
     - Set up alerts for connections to known malicious IPs and domains.
     - Use network traffic analysis tools to detect anomalies.

Detection Signature:
   - Service: DNS
   - Port: 53
   - Severity: Critical
   - Incident: Hive0051 Multi-Channel DNS Fluxing
   - Signature name: “DNS Fast-Flux Detection”
   - Internal checks:
     - Setting1: Monitor DNS queries for high-frequency changes in IP addresses.
     - Setting2: Detect DNS queries to known malicious domains or patterns.
     - Setting3: Implement DNS rate limiting to prevent abuse.
   - External scanning:
     - Frequent DNS resolution changes.
     - DNS queries to Telegram and Telegraph services.

IoCs:
   - Domains:
     - blakurin[.]ru
     - acaenaso[.]ru
     - antarcticos[.]ru
     - garibdo[.]ru
   - IP addresses: Not specified in the document, but historical DNS records of mentioned domains can be referenced.

No additional IoCs found in the document beyond the specified domains.
