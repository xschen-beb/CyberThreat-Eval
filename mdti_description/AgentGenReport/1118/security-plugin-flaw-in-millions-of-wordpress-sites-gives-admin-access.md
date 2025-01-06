Source: [https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access](https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access
- https://www.wordfence.com/blog/2024/11/really-simple-security-vulnerability/
- https://www.wordfence.com/threat-intel/vulnerabilities/detail/really-simple-security-free-pro-and-pro-multisite-900-9111-authentication-bypass
- https://wordpress.org/plugins/really-simple-ssl/advanced/
- https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access/
- https://nvd.nist.gov/vuln/detail/CVE-2024-10924
- https://www.govinfosecurity.com/wordpress-plugin-vulnerability-threatens-4-million-sites-a-26843
- https://www.ionix.io/blog/cve-2024-10924-explained-security-plugin-flaw-in-millions-of-wordpress-sites/
- https://thehackernews.com/2024/11/urgent-critical-wordpress-plugin.html

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Security Plugin Flaw in WordPress Sites 

#### Root cause 
 The root cause behind the incident is an improper handling of user authentication in the 'Really Simple Security' plugin's two-factor REST API actions. Specifically, the function 'check_login_and_get_user()' did not appropriately reject invalid 'login_nonce' values, allowing for an authentication bypass. *This affects versions 9.0.0 to 9.1.1.1* (https://www.wordfence.com/threat-intel/vulnerabilities/detail/really-simple-security-free-pro-and-pro-multisite-900-9111-authentication-bypass). *CWE-288: Authentication Bypass Using an Alternate Path or Channel* (https://nvd.nist.gov/vuln/detail/CVE-2024-10924). *Function 'authenticate_and_redirect()' allows bypass* (https://www.govinfosecurity.com/wordpress-plugin-vulnerability-threatens-4-million-sites-a-26843). *Issue with two-factor authentication mechanism* (https://www.ionix.io/blog/cve-2024-10924-explained-security-plugin-flaw-in-millions-of-wordpress-sites/) 

#### Threat actor/group/campaign 
 Not specified, but the flaw could be exploited by any remote attacker. *Automated scripts for exploitation* (https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access/) 

#### Organization/industry/location 
 Websites using the 'Really Simple Security' plugin (WordPress platform). *4,000,000 websites affected* (https://www.wordfence.com/blog/2024/11/really-simple-security-vulnerability/). *Formerly known as Really Simple SSL* (https://www.ionix.io/blog/cve-2024-10924-explained-security-plugin-flaw-in-millions-of-wordpress-sites/) 

#### Start date � End date 
 Discovered on November 6, 2024, and fixed by November 14, 2024. *WordPress.org forced updates* (https://www.govinfosecurity.com/wordpress-plugin-vulnerability-threatens-4-million-sites-a-26843). *Responsible disclosure* (https://thehackernews.com/2024/11/urgent-critical-wordpress-plugin.html) 

#### MITRE TTPs 
 ['T1078: Valid Accounts', 'T1078.003: Valid Accounts: Local Accounts', 'T1212: Exploitation for Credential Access'] 

#### Impact 
 Potentially over 3,500,000 websites are exposed to the vulnerability, allowing remote attackers to gain full administrative access. *CVSS score 9.8 (Critical)* (https://www.wordfence.com/blog/2024/11/really-simple-security-vulnerability/). *CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H* (https://nvd.nist.gov/vuln/detail/CVE-2024-10924). *Large-scale automated attack* (https://www.govinfosecurity.com/wordpress-plugin-vulnerability-threatens-4-million-sites-a-26843) 

#### Mitigation Steps 
 ['Ensure that the Really Simple Security plugin is updated to version 9.1.2 or higher.', 'Verify that auto-updates are enabled for the plugin.', 'For Pro version users with expired licenses, manually update to 9.1.2.', 'Hosting providers should enforce plugin updates and scan databases for vulnerable versions. *Verify updates to latest version* (https://www.govinfosecurity.com/wordpress-plugin-vulnerability-threatens-4-million-sites-a-26843). *Hosting providers force-update plugin* (https://www.ionix.io/blog/cve-2024-10924-explained-security-plugin-flaw-in-millions-of-wordpress-sites/)'] 

#### Detection Signature 
 { 'Service': 'WordPress', 'Port': '80/443 (HTTP/HTTPS)', 'Severity': 'Critical', 'Incident': 'Exploitation of Really Simple Security plugin vulnerability', 'Signature name': 'WordPress Really Simple Security Authentication Bypass', 'Internal checks': { 'Setting1': 'Verify plugin version is 9.1.2 or higher.', 'Setting2': 'Ensure 'login_nonce' verification is correctly implemented.'}, 'External scanning': { 'Check for outdated versions of the plugin.': 'Monitor for unusual login attempts or administrative access.'} 

#### IoCs 
- No IoCs found. 

#### Affected Software 
 {'Really Simple Security': '9.0.0 - 9.1.1.1', 'Really Simple Security Pro': '9.0.0 - 9.1.1.1', 'Really Simple Security Pro Multisite': '9.0.0 - 9.1.1.1'} 

#### Researcher 
 Istv�n M�rton *Wordfence* (https://www.wordfence.com/threat-intel/vulnerabilities/detail/really-simple-security-free-pro-and-pro-multisite-900-9111-authentication-bypass) *Bill Toulas* (https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access/) *Prajeet Nair* (https://www.govinfosecurity.com/wordpress-plugin-vulnerability-threatens-4-million-sites-a-26843) *Nethanel Gelernter* (https://www.ionix.io/blog/cve-2024-10924-explained-security-plugin-flaw-in-millions-of-wordpress-sites/) *Ravie Lakshmanan* (https://thehackernews.com/2024/11/urgent-critical-wordpress-plugin.html) 

#### Additional Info 
 {'WordPress version': '5.9 or higher', 'PHP version': '7.4 or higher', 'Contributors': 'Rogier Lankhorst, Mark, Hessel de Jong, vicocotea, Marcel Santing, Jan-Willem', 'WordPress.org stats': '3,500,000 potentially exposed sites (https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access/)', 'References': ['https://plugins.trac.wordpress.org/browser/really-simple-ssl/tags/9.1.1.1/security/wordpress/two-fa/class-rsssl-two-factor-on-board-api.php#L277', 'https://plugins.trac.wordpress.org/browser/really-simple-ssl/tags/9.1.1.1/security/wordpress/two-fa/class-rsssl-two-factor-on-board-api.php#L278', 'https://plugins.trac.wordpress.org/browser/really-simple-ssl/tags/9.1.1.1/security/wordpress/two-fa/class-rsssl-two-factor-on-board-api.php#L67', 'https://plugins.trac.wordpress.org/changeset/3188431/really-simple-ssl'], 'WPLMS Learning Management System': 'CVE-2024-10470 (https://thehackernews.com/2024/11/urgent-critical-wordpress-plugin.html)'} 


