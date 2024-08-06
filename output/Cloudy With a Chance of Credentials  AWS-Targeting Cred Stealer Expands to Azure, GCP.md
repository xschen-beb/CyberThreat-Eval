# Cloudy With a Chance of Credentials  AWS-Targeting Cred Stealer Expands to Azure, GCP

### Incident: Cloudy With a Chance of Credentials Leak

**Root Cause:** Misconfigured Docker instances exposing sensitive services.

**Impact:** 
- **Devices/People Impacted:** The exact number of affected devices and individuals is not specified, but it involves multiple organizations using AWS, Azure, and GCP cloud services.
- **Financial Losses:** Unspecified, but potential losses could be significant considering the access to cloud credentials and subsequent misuse.

**Mitigation:** 
1. **Secure Docker Instances:**
   - Ensure Docker daemons are not exposed to the internet unless absolutely necessary.
   - Regularly update and patch Docker instances to mitigate vulnerabilities.
   - Restrict access using firewalls and network segmentation.
   - Implement proper authentication mechanisms for Docker services.

2. **Credential Management:**
   - Rotate cloud credentials regularly and use least privilege principles.
   - Use environment variable management tools to avoid storing credentials in code or configuration files.

3. **Monitoring and Auditing:**
   - Continuously monitor access logs and network traffic for suspicious activities.
   - Implement anomaly detection systems to identify unusual access patterns.

4. **Incident Response and Recovery:**
   - Develop and test an incident response plan.
   - Ensure backups are in place and can be quickly restored in case of a breach.

**Detailed Steps for Mitigation:**
1. **Docker Security:**
   - **Disable Docker remote API:** Edit the Docker service configuration to bind Docker daemon to the local interface only.
   - **Configure firewall rules:** Ensure that only trusted IP addresses can access the Docker service.
   - **Enable Docker Content Trust:** To ensure all images are signed and verified before running.

2. **Patch Management:**
   - Regularly apply security updates and patches to Docker, Kubernetes, and cloud services.
   - Automate patch management to ensure timely updates.

3. **Network Segmentation:**
   - Isolate critical systems and services within separate network segments.
   - Use Virtual Private Clouds (VPCs) and configure security groups to restrict access.

4. **Credential Rotation:**
   - Use automated tools to rotate credentials periodically.
   - Remove hardcoded credentials from scripts and configuration files.

5. **Monitoring and Alerts:**
   - Integrate cloud security monitoring tools like AWS CloudTrail, Azure Security Center, and GCP Cloud Security Command Center.
   - Set up alerts for any unusual activities, such as multiple failed login attempts or access from unusual locations.

**Detection Signature:**
- **Service:** Docker
- **Port:** 2375/2376
- **Severity:** Critical
- **Incident:** Cloud Credentials Leak
- **Signature name:** “Docker publicly accessible”
- **Internal checks:**
  - **Setting1:** Docker daemon should not be exposed on the external Internet.
  - **Setting2:** Docker daemon should not listen on the external Internet.
  - **Setting3:** Docker services should be secured with proper authentication credentials.
- **External scanning:**
  - **Port (2375/2376) open**
  - **Docker daemon accessible without authentication**

**IoCs:**
- **SHA1 Hashes:**
  - `0e1805fd9efa6a1c3fe9adb3f34373a9dcc7fe19` (run.sh)
  - `18d28ac44c5501f1768f0fc155ad38aa56610881` (chattr ELF binary)
  - `27414df2f9a687db65d2bc5fed011a1f0f550417` (aws.sh v3)
  - `2ed9517159b89af2518cf65a93f3377dea737138` (UPX-packed Golang ELF binary)
  - `37cb34a044c70d1acea5a3a91580b7bfc2a8e687` (Tsunami ELF binary)
  - `3d6aaed47135090326780727fef57ce1c1573aa2` (tmate.sh)
  - `5611cb5676556410981eefab70d0e2aced01dbc5` (aws.sh v2)
  - `6123bbca11385f9a02f888b21a59155242a96aba` (user.sh)
  - `61da5d358df2e99ee174b22c4899dbbf903c76f0` (aws.sh v5)
  - `63fe964140907470427e035bdba5230f6a302056` (b.sh)
  - `654be7302f4a3638929fe5e67f6f2739a1801b07` (clean.sh)
  - `828960576e182ec3206f457a263f25ee0531edbb` (curl.full)
  - `863bf9617f82c9c595cc9b09e84a346a306060c2` (dAPIpwn embedded script)
  - `8802f1bf8f83e354f14686fe79b5018cd36eb77f` (aws.sh v6)
  - `ac78d5c763e460db2137999b67b921e471a55e11` (aws.sh v4)
  - `b13d62f15868900ab22c9429effdfb7939563926` (aws.sh v7)
  - `c9edc82bc3ac344981231965bedec300fec31b1f` (xc3.sh)
  - `d79970f66a56f69667284c4c937f666758200ab4` (grab.sh)
  - `dba0dcb8378d84abc8f7bf897825dd4f23e20e04` (data.sh)
  - `eb3dff13ed97670e06649e8daaa6e4ab655477f6` (aws.sh v1)
  - `f437aeac3721a0038c936bab5a2ac1ccdb0cf222` (int.sh)
- **Domains:**
  - `ap-northeast-1.compute.internal.anondns.net`
  - `everlost.anondns.net`
  - `silentbob.anondns.net`
  - `everfound.anondns.net`
- **IPv4s:**
  - `207.154.218.221`
  - `45.9.148.108`
- **URLs:**
  - `http[:]//silentbob.anondns.net/bin/chattr`
  - `http[:]//silentbob.anondns.net/bin/a`
  - `http[:]//silentbob.anondns.net/cmd/grab.sh`
  - `http[:]//silentbob.anondns.net/cmd/clean.sh`
  - `http[:]//silentbob.anondns.net/cmd/aws.sh`
  - `http[:]//silentbob.anondns.net/cmd/xc3.sh`
  - `http[:]//silentbob.anondns.net/bin/sysfix/curl.full`
  - `http[:]//silentbob.anondns.net/bin/chattr`
  - `http[:]//silentbob.anondns.net/insert/gscat.php`
  - `http[:]//silentbob.anondns.net/insert/tmate.php`

The detection and mitigation strategies outlined can help organizations to prevent and respond to such credential-stealing campaigns effectively.
