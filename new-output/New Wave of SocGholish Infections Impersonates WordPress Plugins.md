Source: [https://blog.sucuri.net/2024/03/new-wave-of-socgholish-infections-impersonates-wordpress-plugins.html](https://blog.sucuri.net/2024/03/new-wave-of-socgholish-infections-impersonates-wordpress-plugins.html)

# New Wave of SocGholish Infections Impersonates WordPress Plugins

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: New Wave of SocGholish Infections Impersonates WordPress Plugins 

 Root cause: Compromised wp-admin credentials and installation of malicious plugins impersonating legitimate WordPress plugins. 

 Threat Actor/group/campaign: SocGholish malware campaign, *Evil Corp* (https://redcanary.com/threat-detection-report/threats/socgholish/) 

 Organization/industry/location: WordPress websites (specific organization/industry/location not mentioned) 

 Start date – End date: October 2023 – March 2024, *peak in March 2023* (https://redcanary.com/threat-detection-report/threats/socgholish/) 

 MITRE TTPs: ['T1071.001: Application Layer Protocol: Web Protocols', 'T1203: Exploitation for Client Execution', 'T1190: Exploit Public-Facing Application', 'T1059.007: Command and Scripting Interpreter: JavaScript'] 

 Impact: Over 2,800 detections in the current year, significant increase from 1,400 detections in the previous year. 

 Mitigation: ['Secure your wp-admin panel by using strong and unique passwords.', 'Regularly update your WordPress core, plugins, and themes to the latest versions.', 'Enable automatic updates for plugins and themes whenever possible.', 'Employ a regular backup system to ensure data recovery in case of an incident.', 'Implement a website firewall to block malicious traffic and patch known vulnerabilities.', 'Avoid downloading and installing plugins and themes from unofficial sources.', 'Monitor access logs for unusual login attempts and plugin installations.'] 

 Detailed Steps for mitigation: ['Change all wp-admin passwords to strong, unique passwords.', 'Update the WordPress core, plugins, and themes to the latest versions.', 'Enable automatic updates in the WordPress admin dashboard.', 'Set up a regular backup schedule and ensure backups are stored securely.', 'Install and configure a reputable website firewall.', 'Remove any plugins or themes not obtained from official sources.', 'Regularly review access logs for any suspicious activity.', 'Educate users on the importance of downloading updates only from official sources.'] 

 Detection Signature: {'Service': 'WordPress', 'Port': '80, 443', 'Severity': 'Critical', 'Incident': 'SocGholish Malware Infection', 'Signature name': 'Malicious WordPress Plugin Installation', 'Internal checks': ['Monitor for unauthorized login attempts to wp-admin.', 'Alert on the installation of plugins from non-official sources.', 'Monitor wp_postmeta table for suspicious script tags.'], 'External scanning': ['Scan for malicious JavaScript loaded from known SocGholish domains.', 'Monitor network traffic for connections to known malicious domains.']} 

 IoCs: ['whitedrill[.]org', 'libertariancounterpoint[.]com', 'stake[.]libertariancounterpoint[.]com', 'eeatgoodx[.]com', 'gitbrancher[.]com', 'funcallback[.]com', 'asyncfunctionapi[.]com', 'IPs: 67.20.113.11, 185.158.251.240, 83.69.236.128, 81.94.150.21'] 

 No additional IoCs found:  

 Adversary: *TA569* (https://redcanary.com/threat-detection-report/threats/socgholish/) 

 Initial access method: *Drive-by-download* (https://redcanary.com/threat-detection-report/threats/socgholish/) 

 New information: ['*Fake update alerts, Cobalt Strike framework, code injection in werfault.exe* (https://secure.wphackedhelp.com/blog/fakeupdates-socgholish-malware/)', '*AsyncRAT, BOINC, rzegzwre[.]top, Rosettahome[.]top* (https://securityaffairs.com/166030/malware/socgholish-used-deliver-asyncrat.html)'] 


# Related articles (describing the same threat) 
['https://blog.sucuri.net/2024/03/new-wave-of-socgholish-infections-impersonates-wordpress-plugins.html', 'https://redcanary.com/threat-detection-report/threats/socgholish/', 'https://secure.wphackedhelp.com/blog/fakeupdates-socgholish-malware/', 'https://securityaffairs.com/166030/malware/socgholish-used-deliver-asyncrat.html']
