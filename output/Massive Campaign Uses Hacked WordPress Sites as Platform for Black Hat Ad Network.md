# Massive Campaign Uses Hacked WordPress Sites as Platform for Black Hat Ad Network

Incident: WordPress Site Redirection Campaign

Root cause: Multiple vulnerabilities in WordPress themes and plugins leading to unauthorized modifications and malware injections.

Impact: Over 5,600 websites impacted with potential exposure of user traffic to malicious redirects and malware. Financial losses can vary widely based on the number of users affected, potential theft of credentials, and any resulting malware infections.

Mitigation: Secure WordPress installations by updating all themes and plugins, enforcing strong passwords, and regularly scanning for malware. Detailed Steps for mitigation include:

1. **Remove Injected Malware**:
    - Restore infected core WordPress files from the original package.
    - Scan for known malicious code patterns such as `fromCharCode(118,` and `eval(p1)`.

2. **Update Themes and Plugins**:
    - Update all themes and plugins to their latest versions.
    - Remove any unused or abandoned themes and plugins.

3. **Change Website Passwords**:
    - Change all passwords associated with the website, including FTP, WordPress admin, and database credentials.
    - Check for unauthorized users directly in the WordPress database.

4. **Remove Backdoors**:
    - Scan the entire website for backdoors, particularly for known patterns like the `wp-reset.php` backdoor example provided in the blog.
    - Implement file integrity monitoring to detect any unauthorized changes.

Detection Signature:
   - Service: WordPress
   - Port: 80/443 (HTTP/HTTPS)
   - Severity: Critical
   - Incident: Unauthorized WordPress site redirections
   - Signature name: “WordPress site redirection malware”
   - Internal checks:
      - Setting1: Index.php and common JavaScript files should not contain unexpected script tags or obfuscated code.
      - Setting2: Ensure no unauthorized modifications exist in core WordPress files.
      - Setting3: Verify plugins and themes are up-to-date and secure.
   - External scanning:
      - Detects unauthorized script injections and known malicious domains.
      - Identifies known malicious patterns like `String.fromCharCode` obfuscation.

IoCs:
- Domains: 
  - track[.]violetlovelines[.]com
  - way[.]specialblueitems[.]com
  - weatherplllatform[.]com
  - interestmoments[.]com
  - similarwebline[.]com
  - wholegrady[.]com
  - dusyguri[.]com
  - ezstat[.]ru
  - cdn.discordapp[.]com (for malicious payload delivery)
  
- IP Addresses:
  - 193.169.194.63
  - 194.135.30.40
  - 208.88.225.119
  - 62a00:1178:1:4b::17
  - 2607:fbe0:1:42::17

No file hashes provided in the blog.
