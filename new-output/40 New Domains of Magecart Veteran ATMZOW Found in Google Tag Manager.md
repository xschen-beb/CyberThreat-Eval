Source: [https://blog.sucuri.net/2023/12/40-new-domains-of-magecart-veteran-atmzow-found-in-google-tag-manager.html](https://blog.sucuri.net/2023/12/40-new-domains-of-magecart-veteran-atmzow-found-in-google-tag-manager.html)

# 40 New Domains of Magecart Veteran ATMZOW Found in Google Tag Manager

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Magecart ATMZOW Skimmer in Google Tag Manager 

 Root cause: The root cause behind the incident includes the exploitation of Google Tag Manager (GTM) by hackers who injected malicious scripts into trusted GTM containers. The attackers leveraged the trust and widespread use of GTM scripts to plant credit card skimmers on eCommerce websites, especially those using Magento. *Sucuri researchers* (https://cybersecuritynews.com/hackers-planting-credit-card-skimmers/#:~:text=Hackers%20enjoy%20Google%20Tag%20Manager,and%20build%20a%20new%20container.) have analyzed the malicious code’s *new obfuscation methods*, increasing the challenge of detecting these scripts. 

 Threat Actor/group/campaign: Magecart group, specifically the ATMZOW skimmer campaign. 

 Organization/industry/location: Primarily eCommerce websites using Magento, location unspecified but known to be widespread. 

 Start date – End date: The malicious GTM containers were active throughout 2023, with notable activity detected in November and later months. 

 MITRE TTPs: ['T1190: Exploit Public-Facing Application', 'T1071: Application Layer Protocol (HTTP/HTTPS)', 'T1027: Obfuscated Files or Information', 'T1566: Phishing', 'T1056: Input Capture'] 

 Impact: 327+ websites compromised, with credit card information and potentially other sensitive user data stolen. 

 Mitigation: ['Regularly audit and review all GTM containers and scripts included on the website.', 'Implement security measures to detect and block suspicious GTM containers.', 'Use Content Security Policy (CSP) to restrict the domains from which scripts can be loaded.', 'Ensure that third-party scripts are hosted on a secure CDN or directly on your server.', 'Employ a web application firewall (WAF) to filter out malicious traffic.', 'Educate users and administrators about recognizing and responding to suspicious activity in GTM.'] 

 Detailed Steps for mitigation: {'1. **Audit GTM Containers**': ['Regularly check and verify all GTM containers and scripts on the site.', 'Remove any GTM containers/scripts that are not recognized or authorized.'], '2. **Implement CSP**': ['Configure Content Security Policy to allow scripts only from trusted domains.', '```', "Content-Security-Policy: script-src 'self' https://trusted.cdn.com;", '```'], '3. **Secure Hosting**': ['Host third-party scripts on a secure content delivery network (CDN) or directly on your server to ensure integrity and availability.'], '4. **Deploy WAF**': ['Use a Web Application Firewall to detect and block malicious traffic and unauthorized script injections.'], '5. **Employee Training**': ['Conduct regular training sessions for employees to identify and report suspicious activities in GTM and other parts of the website infrastructure.']} 

 Detection Signature: {'Service': 'Google Tag Manager (GTM)', 'Port': 'Not applicable (web-based service)', 'Severity': 'Critical', 'Incident': 'Magecart ATMZOW Skimmer', 'Signature name': '“Suspicious GTM Container Detected”', 'Internal checks': ['Ensure all GTM containers are verified and authorized.', 'Regularly review the scripts and variables used within GTM containers.'], 'External scanning': ['Monitor for GTM containers using non-trusted domains.', 'Use tools like URLScan to identify malicious GTM containers.']} 

 IoCs: [{'GTM Containers': ['GTM-WJ6S9J6', 'GTM-TVKQ79ZS', 'GTM-NTV2JTB4', 'GTM-MX7L8F2M']}, {'Malicious Domains': ['gtm-statistlc[.]com', 'gooqle-analytics[.]com', 'webstatlstics[.]com', '31.220.21[.]211', '31.220.21[.]240', '62.72.7[.]89', '62.72.7[.]90']}, {'Example Malicious Domains from recent campaign': ['cdn.sketchinsightswatch[.]com', 'cdn.colorpalettemetrics[.]com', 'cdn.artisticpatterndata[.]com', 'cdn.visualartexplorer[.]com', 'cdn.picturedataminer[.]com', '*40 new domains* (https://cybersecuritynews.com/hackers-planting-credit-card-skimmers/#:~:text=Hackers%20enjoy%20Google%20Tag%20Manager,and%20build%20a%20new%20container.)']}] 

 Additional Info: ['*The first word of the domains is always related to art* (https://cybersecuritynews.com/hackers-planting-credit-card-skimmers/#:~:text=Hackers%20enjoy%20Google%20Tag%20Manager,and%20build%20a%20new%20container.)'] 

 Conclusion: By following the mitigation steps and using the provided detection signatures and IoCs, organizations can better protect themselves from similar attacks and promptly respond to any signs of compromise. 


# Related articles (describing the same threat) 
['https://blog.sucuri.net/2023/12/40-new-domains-of-magecart-veteran-atmzow-found-in-google-tag-manager.html', 'https://cybersecuritynews.com/hackers-planting-credit-card-skimmers/#:~:text=Hackers%20enjoy%20Google%20Tag%20Manager,and%20build%20a%20new%20container.']
