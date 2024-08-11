Source: [https://www.cadosecurity.com/updates-to-legion-a-cloud-credential-harvester-and-smtp-hijacker/](https://www.cadosecurity.com/updates-to-legion-a-cloud-credential-harvester-and-smtp-hijacker/)

# Updates to Legion A Cloud Credential Harvester and SMTP Hijacker

**Incident: Legion Malware Update**

**Root cause:** Misconfigured web servers exposing environment variable files (.env).

**Impact:** The exact number of records or financial losses is not specified in the blog. However, given the nature of credential harvesting and SMTP hijacking, the impact could be substantial in terms of compromised accounts and potential abuse of cloud resources.

**Mitigation:** Secure web servers and cloud services by ensuring environment files are not publicly accessible and by avoiding storing sensitive credentials in these files.

**Detailed Steps for Mitigation:**
1. **Review Web Server Configuration:**
   - Ensure that environment variable files (.env) are not stored in publicly accessible directories.
   - Implement proper access controls and permissions.
   
2. **Use Secure Credential Storage:**
   - Avoid storing sensitive information in plain text within environment files.
   - Use secure vaults or secret management tools to store credentials.

3. **Regular Security Audits:**
   - Perform regular audits of your web server configurations.
   - Ensure that any changes to the web application do not expose sensitive files.

4. **Implement IAM Best Practices:**
   - Use least privilege principles for IAM roles and users.
   - Regularly review and rotate access keys and secrets.

5. **Monitor and Detect Anomalous Activity:**
   - Set up monitoring and alerts for suspicious activity, such as unauthorized IAM user creation.
   - Implement logging and review logs periodically for any signs of compromise.

**Detection Signature:**
   - **Service:** Web Server
   - **Port:** 80 (HTTP) / 443 (HTTPS)
   - **Severity:** Critical
   - **Incident:** Legion Malware Update
   - **Signature name:** “Publicly Accessible Environment Files”
   - **Internal checks:**
     - Setting1: Ensure environment files (.env) are not stored in web root directories. – In platform
     - Setting2: Ensure proper permissions are set for environment files. – Inside VMs
     - Setting3: Use secure storage solutions for sensitive credentials. – Inside VMs
   - **External scanning:**
     - Check for publicly accessible .env files.

**IoCs:**
   - **Filename:** og.py
   - **SHA256:** 6f059c2abf8517af136503ed921015c0cd8859398ece7d0174ea5bf1e06c9ada
   - **User Agents:**
     - Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
     - Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
     - Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
     - Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36
     - Mozilla/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36
     - Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0
     - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
     - Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36

By following the detailed steps for mitigation and monitoring for the provided IoCs, organizations can better protect themselves against the Legion malware and similar threats.
