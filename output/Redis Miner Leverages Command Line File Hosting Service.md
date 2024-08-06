# Redis Miner Leverages Command Line File Hosting Service

Incident: Redis Miner Leverages Command Line File Hosting Service

Root cause: Misconfigured Redis instance

Impact: The blog does not specify the exact number of devices, people impacted, or financial losses. Generally, cryptojacking can lead to significant financial losses due to increased power consumption and potential damage to hardware from overuse.

Mitigation: Secure Redis instances with authentication credentials and restrict access to trusted IP addresses.
- **Detailed Steps for mitigation:**
  1. **Enable Redis Authentication:**
     - Edit the Redis configuration file (`redis.conf`) to set a strong password with the `requirepass` directive.
     - Example: `requirepass YourStrongPassword`
  2. **Restrict Network Access:**
     - Bind Redis to the loopback interface or a specific internal IP by setting the `bind` directive in `redis.conf`.
     - Example: `bind 127.0.0.1`
  3. **Configure Firewall Rules:**
     - Use firewall rules to restrict access to the Redis port (default 6379) to trusted IP addresses.
     - Example: `sudo ufw allow from <trusted-ip> to any port 6379`
  4. **Disable Dangerous Commands:**
     - Rename or disable dangerous commands such as `CONFIG`, `SHUTDOWN`, and `FLUSHALL` in `redis.conf`.
     - Example: `rename-command CONFIG ""`
  5. **Monitor and Update:**
     - Regularly monitor Redis logs for suspicious activity and keep the software up to date with security patches.

Detection Signature:
- **Service:** Redis
- **Port:** 6379
- **Severity:** Critical
- **Incident:** Redis Miner Leverages Command Line File Hosting Service
- **Signature name:** “Redis publicly accessible”
  - **Internal checks:**
    - Setting1: Redis port (6379) should not be exposed on external Internet. – In platform
    - Setting2: Redis port (6379) should not listen on the external Internet – Inside VMs
    - Setting3: Redis server should secure with authentication credentials. – Inside VMs
  - **External scanning:**
    - Port (6379) open
    - Redis no-pass-login

IoCs:
- **Files:**
  - SHA-256 .cmd: 202ce93435f78009995f57eded544959884258f96d178173a54eee47f16e8834
  - SHA-256 .dat: c43191f98eb5b5ef792e19089317e4ec411c696c3bf501b17f27bfad4b75eb1e
- **URLs:**
  - hxxps://transfer[.]sh/mtKUQC/run[.]sh
  - hxxps://transfer[.]sh/QQcudu/tmp[.]fDGJW8BfMC
