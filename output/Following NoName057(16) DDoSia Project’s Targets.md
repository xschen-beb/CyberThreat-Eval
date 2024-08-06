# Following NoName057(16) DDoSia Project’s Targets

Incident: NoName057(16) DDoSia Project

Root cause: Usage of a sophisticated DDoS toolkit

Impact: Targeted multiple websites across various countries, including government agencies, media, and private companies. Financial losses and operational disruptions are likely significant but unspecified. The blog highlights that 486 different websites were impacted.

Mitigation: 
1. **Enhance DDoS Protection**:
    - Implement DDoS protection services like Cloudflare, Akamai, or AWS Shield.
    - Use rate limiting and traffic filtering to mitigate the impact of DDoS attacks.

2. **Network Security Measures**:
    - Ensure all servers and services are behind firewalls and properly configured.
    - Employ network segmentation to isolate critical services.

3. **Monitoring and Incident Response**:
    - Continuously monitor network traffic for abnormal patterns.
    - Set up an incident response plan specifically addressing DDoS attacks.
    - Regularly update and patch systems to prevent exploitation.

4. **Threat Intelligence Sharing**:
    - Join threat intelligence sharing platforms to stay updated on new threats.
    - Share IoCs with other organizations to collectively improve security postures.

Detection Signature:
   Service: Nginx
   Port: 80, 443
   Severity: Critical
   Incident: NoName057(16) DDoSia Project
   Signature name: “DDoSia C2 communication”
   Internal checks:
      - Setting1: Ensure Nginx server is configured to limit connection rates.
      - Setting2: Configure Nginx to log and alert on high rates of POST requests.
      - Setting3: Use reverse proxies to filter malicious traffic.
   External scanning:
      - Port (80, 443) open
      - High volume of POST requests detected

IoCs:
- SHA256 sums of DDoSia malware samples:
  - d_linux_amd64: 761075da6b30bb2bcbb5727420e86895b79f7f6f5cebdf90ec6ca85feb78e926
  - d_linux_arm: fae9b6df2987b25d52a95d3e2572ea578f3599be88920c64fd2de09d1703890a
  - d_mac_amd64: 8e1769763253594e32f2ade0f1c7bd139205275054c9f5e57fefd8142c75441f
  - d_mac_arm64: 9a1f1c491274cf5e1ecce2f77c1273aafc43440c9a27ec17d63fa21a89e91715
  - d_windows_amd64.exe: 726c2c2b35cb1adbe59039193030f23e552a28226ecf0b175ec5eba9dbcd336e
  - d_windows_arm64.exe: 7e12ec75f0f2324464d473128ae04d447d497c2da46c1ae699d8163080817d38
- C2 IP: 94[.]140.114.239
