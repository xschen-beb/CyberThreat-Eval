Source: [https://www.malwarebytes.com/blog/threat-intelligence/2023/04/kritec-art](https://www.malwarebytes.com/blog/threat-intelligence/2023/04/kritec-art)

# Magecart Threat Actor Rolls Out Convincing Modal Forms

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Magecart threat actor rolls out convincing modal forms 

 Root cause: The root cause behind the incident is the injection of a malicious JavaScript skimmer into websites using the PrestaShop CMS. The skimmer uses a fraudulent modal designed to steal credit card information by mimicking the legitimate payment process of the compromised sites. *The skimmer code is heavily obfuscated with base64* (https://www.bleepingcomputer.com/news/security/hackers-swap-stealth-for-realistic-checkout-forms-to-steal-credit-cards/). *The skimmer also impersonates legitimate third-party vendors like Google Tag Manager as an evasion technique* (https://thehackernews.com/2023/04/attention-online-shoppers-dont-be.html). 

 Threat Actor/group/campaign: Magecart (including the specific campaign using the Kritec skimmer first detected in March 2022) 

 Organization/industry/location: The affected industries are e-commerce stores, including a Parisian travel accessory store, e-commerce sites in Denmark and Finland, and several other e-commerce sites in different languages (e.g., Dutch and Finnish stores) *The changes* (https://blog.koddos.net/hackers-hijack-online-stores-to-display-fake-payment-forms-and-steal-credit-cards/). 

 Start date – End date: Not explicitly mentioned, but the article indicates the campaign was ongoing and has been tracked in recent months (as of April 2023). 

 MITRE TTPs: ['T1071.001: Application Layer Protocol: Web Protocols', 'T1557: Adversary-in-the-Middle', 'T1608.003: Stage Capabilities: Web Shell'] 

 Impact: Multiple e-commerce sites compromised, with unknown specific numbers of records or financial losses. *The skimmer drops a cookie on users to prevent loading the malicious modal again on the same or another site* (https://www.bleepingcomputer.com/news/security/hackers-swap-stealth-for-realistic-checkout-forms-to-steal-credit-cards/). *Jerome Segura, director of threat intelligence at Malwarebytes, noted the skimmer looks more authentic than the original payment page* (https://thehackernews.com/2023/04/attention-online-shoppers-dont-be.html). 

 Mitigation: ['Regularly audit and monitor your web applications and third-party scripts loaded on your website.', 'Implement Content Security Policy (CSP) to restrict the sources from which scripts can be loaded.', 'Use Subresource Integrity (SRI) to ensure that fetched resources (scripts, styles) are delivered without unexpected manipulation.', 'Employ a web application firewall (WAF) to detect and block common threats.', 'Regularly update and patch CMS and plugins to prevent exploitation of known vulnerabilities.', 'Educate employees about the importance of validating third-party integrations and the potential risks of skimmers.'] 

 Detailed Steps for mitigation: ['Conduct regular security reviews and audits of your website, including all third-party components.', 'Implement CSP headers to restrict script sources:', "Content-Security-Policy: script-src 'self' https://trusted.cdn.com;", 'Use SRI for external resources:', "<script src='https://trusted.cdn.com/script.js' integrity='sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/ux7+S/9cC5Q6+3P3pLsF6B6cQ+Yl/2z' crossorigin='anonymous'></script>", 'Deploy and configure a WAF to filter and monitor HTTP traffic to and from your web application.', 'Regularly update the CMS, plugins, and all software components to the latest versions.', 'Train employees on recognizing and mitigating web skimmer threats.'] 

 Detection Signature: {'Service': 'PrestaShop CMS', 'Port': '80/443', 'Severity': 'Critical', 'Incident': 'Magecart Credit Card Skimming', 'Signature name': '“Magecart Skimmer Detection”', 'Internal checks': ['Setting1: Regularly audit JavaScript files loaded on the checkout page.', 'Setting2: Regularly monitor the integrity of the payment process flow.', 'Setting3: Implement and monitor CSP and SRI to detect unauthorized script loads.'], 'External scanning': ['Detect unauthorized JavaScript files being loaded (e.g., [name of store]-loader.js).', 'Monitor for external domains and IPs associated with skimmers.']} 

 IoCs: {'Domain names': ['genlytec[.]us', 'shumtech[.]shop', 'zapolmob[.]sbs', 'daichetmob[.]sbs', 'interytec[.]shop', 'pyatiticdigt[.]shop', 'stacstocuh[.]quest'], 'IP addresses': ['195.242.110[.]172', '195.242.110[.]83', '195.242.111[.]146', '45.88.3[.]201', '45.88.3[.]63'], 'YARA rule': 'rule kritecloader\n{\n    strings:\n        $string = "\'fetchModul\'"\n        $string2 = "\'setAttribu\'"\n        $string3 = "\'contentWin\'"\n        $string4 = "\'zIndex\'"\n    condition:\n        all of them\n}'} 

 No additional IoCs found beyond those listed above.:  


# Related articles (describing the same threat) 
['https://www.malwarebytes.com/blog/threat-intelligence/2023/04/kritec-art', 'https://blog.koddos.net/hackers-hijack-online-stores-to-display-fake-payment-forms-and-steal-credit-cards/', 'https://www.bleepingcomputer.com/news/security/hackers-swap-stealth-for-realistic-checkout-forms-to-steal-credit-cards/', 'https://thehackernews.com/2023/04/attention-online-shoppers-dont-be.html']
