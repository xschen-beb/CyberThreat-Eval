Source: [https://research.checkpoint.com/2023/from-albania-to-the-middle-east-the-scarred-manticore-is-listening/](https://research.checkpoint.com/2023/from-albania-to-the-middle-east-the-scarred-manticore-is-listening/)

# From Albania to the Middle East The Scarred Manticore is Listening

**Incident:** Scarred Manticore Espionage Campaign

**Root Cause:** Vulnerable and misconfigured Internet-facing Windows servers

**Impact:** The campaign targeted high-profile organizations across the Middle East, including government, military, telecommunications, IT service providers, financial organizations, and NGOs. While specific figures on the number of devices, people impacted, and financial losses are not provided in the blog, such espionage campaigns typically have severe implications involving significant data breaches and potential financial damages running into millions of dollars.

**Mitigation:** 
1. **Secure Internet-facing Windows Servers:**
   - **Use Strong Authentication:** Implement multi-factor authentication (MFA) for accessing Windows servers.
   - **Update and Patch Systems:** Regularly update and patch Windows servers to fix any known vulnerabilities.
   - **Monitor for Unusual Activity:** Set up continuous monitoring to detect and respond to suspicious activities.
   - **Disable Unnecessary Services:** Disable any unnecessary services that could be exploited.
   
2. **Harden HTTP.sys and IIS Configurations:**
   - **Restrict HTTP.sys Access:** Limit the use of HTTP.sys to only necessary applications and ensure it is properly configured and monitored.
   - **Configure IIS Securely:** Ensure IIS is securely configured and does not expose unnecessary endpoints.

3. **Network Segmentation:**
   - **Isolate Critical Systems:** Segment the network to ensure critical systems are isolated from potentially compromised systems.

4. **Deploy Endpoint Protection:**
   - **Install Advanced Threat Protection:** Use solutions like Check Point Harmony Endpoint to detect and protect against advanced threats.

**Detailed Steps for Mitigation:**
1. **Implement Strong Authentication:**
   - Configure multi-factor authentication (MFA) for all administrative accounts accessing Windows servers.
2. **Regular Updates and Patches:**
   - Schedule regular patch management cycles to ensure all Windows servers are up to date with the latest security patches.
3. **Continuous Monitoring:**
   - Deploy security information and event management (SIEM) systems to monitor and analyze logs for unusual activities.
   - Define alert thresholds for specific behaviors indicative of an attack (e.g., unusual HTTP.sys interactions).
4. **Disable Unnecessary Services:**
   - Conduct an audit of all running services and disable those not required for the server’s primary function.
5. **Restrict HTTP.sys Access:**
   - Use firewall rules and network access control lists (ACLs) to restrict access to HTTP.sys.
6. **Harden IIS Configuration:**
   - Follow best practices for IIS hardening, including disabling unused modules and ensuring secure configurations.
7. **Network Segmentation:**
   - Use VLANs and subnets to isolate critical infrastructure and limit lateral movement in case of a breach.
8. **Deploy Endpoint Protection:**
   - Install advanced endpoint protection solutions to detect and block malware, including memory-resident and shellcode-based threats.

**Detection Signature:**
- **Service:** Windows HTTP.sys Driver
- **Port:** 80, 443 (HTTP/HTTPS)
- **Severity:** Critical
- **Incident:** Scarred Manticore Espionage Campaign
- **Signature name:** “HTTP.sys Direct Interaction”
- **Internal checks:**
    - Setting1: HTTP.sys should not be accessible from the external Internet – In platform
    - Setting2: HTTP.sys should be properly configured and monitored – Inside VMs
    - Setting3: Windows servers should not have unnecessary services running – Inside VMs
- **External scanning:**
    - Port (80, 443) open
    - Direct interaction with HTTP.sys detected

**IoCs:**
- daa362f070ba121b9a2fa3567abc345edcde33c54cabefa71dd2faad78c10c33
- f4639c63fb01875946a4272c3515f005d558823311d0ee4c34896c2b66122596
- 2097320e71990865f04b9484858d279875cf5c66a5f6d12c819a34e2385da838
- 67560e05383e38b2fcc30df84f0792ad095d5594838087076b214d849cde9542
- 4f6351b8fb3f49ff0061ee6f338cd1af88893ed20e71e211e8adb6b90e50a3b8
- f6c316e2385f2694d47e936b0ac4bc9b55e279d530dd5e805f0d963cb47c3c0d
- 1485c0ed3e875cbdfc6786a5bd26d18ea9d31727deb8df290a1c00c780419a4e
- 8578bff36e3b02cc71495b647db88c67c3c5ca710b5a2bd539148550595d0330
- c5b4542d61af74cf7454d7f1c8d96218d709de38f94ccfa7c16b15f726dc08c0
- 9117bd328e37be121fb497596a2d0619a0eaca44752a1854523b8af46a5b0ceb
- e1ad173e49eee1194f2a55afa681cef7c3b8f6c26572f474dec7a42e9f0cdc9d
- a2598161e1efff623de6128ad8aafba9da0300b6f86e8c951e616bd19f0a572b
- 7495c1ea421063845eb8f4599a1c17c105f700ca0671ca874c5aa5aef3764c1c
- 6f0a38c9eb9171cd323b0f599b74ee571620bc3f34aa07435e7c5822663de605
- 3875ed58c0d42e05c83843b32ed33d6ba5e94e18ffe8fb1bf34fd7dedf3f82a7
- 1146b1f38e420936b7c5f6b22212f3aa93515f3738c861f499ed1047865549cb
- b71aa5f27611a2089a5bbe34fd1aafb45bd71824b4f8c2465cf4754db746aa79
- da450c639c9a50377233c0f195c3f6162beb253f320ed57d5c9bb9c7f0e83999
