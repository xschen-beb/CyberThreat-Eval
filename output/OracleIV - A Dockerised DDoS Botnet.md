# OracleIV - A Dockerised DDoS Botnet

Incident: OracleIV - A Dockerised DDoS Botnet

Root cause: Misconfigured Docker Engine API

Impact: 3,000 instances of the malicious Docker image pulled; specific financial losses or number of devices impacted not provided.

Mitigation: Secure the Docker Engine API with proper authentication and network configurations.

**Detailed Steps for mitigation:**

1. **Restrict API Access:**
   - Configure Docker Engine to listen only on localhost or a private network to prevent unauthorized access.
   - Use firewall rules to restrict access to the Docker Engine API to trusted IP addresses only.

2. **Enable Authentication:**
   - Enable TLS for the Docker Engine API to encrypt communications.
   - Use client certificates to authenticate API requests.

3. **Regular Security Audits:**
   - Periodically review and audit exposed services and their configurations.
   - Use automated tools to scan for exposed Docker Engine APIs.

4. **Monitor Docker Activity:**
   - Implement logging and monitoring solutions to track Docker API requests and container activity.
   - Set up alerts for suspicious activities, such as unexpected image pulls or container starts.

5. **Validate Docker Images:**
   - Only use trusted and verified Docker images from official or trusted sources.
   - Perform regular assessments of the images pulled from Dockerhub to check for signs of tampering.

Detection Signature:
- Service: Docker Engine API
- Port: 2375 (default port)
- Severity: Critical
- Incident: OracleIV - A Dockerised DDoS Botnet
- Signature name: “Docker Engine API publicly accessible”

**Internal checks:**
  - Setting1: Docker API port (2375) should not be exposed to the external Internet.
  - Setting2: Docker API port (2375) should not listen on external interfaces.
  - Setting3: Docker Engine API should secure with TLS and client certificates.

**External scanning:**
  - Port (2375) open
  - Docker Engine API accessible without authentication

IoCs:
- Filename SHA256 hashes:
  - `oracle.sh`: 5a76c55342173cbce7d1638caf29ff0cfa5a9b2253db9853e881b129fded59fb
  - `xmrig`: 20a0864cb7dac55c184bd86e45a6e0acbd4bb19aa29840b824d369de710b6152
  - `config.json`: 776c6ef3e9e74719948bdc15067f3ea77a0a1eb52319ca1678d871d280ab395c
- IP Address: 46[.]166[.]185[.]231
- Docker Image: robbertignacio328832/oracleiv_latest:latest
