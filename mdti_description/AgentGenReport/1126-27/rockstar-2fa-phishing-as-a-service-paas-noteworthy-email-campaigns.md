Source: [https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)

## Related articles (describing the same threat) 
- https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas
- https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident 
 Rockstar 2FA Phishing-as-a-Service (PaaS): Noteworthy Email Campaigns 

#### Root cause 
 The primary issue lies in the abuse of legitimate services to generate fully undetectable (FUD) links for phishing campaigns. Attackers exploit trusted platforms such as Microsoft OneDrive, OneNote, Dynamics 365 Customer Voice, Atlassian Confluence, Google Docs Viewer, and LiveAgent to host or redirect to malicious content. This exploitation allows them to bypass traditional security measures that rely on URL-based detection. *Additionally, QR phishing (quishing) techniques are used to encode URLs within QR codes, often bypassing traditional detection systems that focus on visible links* (https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns/). 

#### Threat actor/group/campaign 
 The campaign is attributed to the Rockstar 2FA Phishing-as-a-Service (PaaS) platform. Specific threat actors are not named in the report. 

#### Organization/industry/location 
 The targeted organizations are not explicitly mentioned, but the use of platforms like Microsoft OneDrive, Dynamics 365, and Atlassian Confluence suggests that businesses using these services are at risk. 

#### Start date – End date 
 The report was published on November 27, 2024. Specific attack dates are not provided. 

#### MITRE TTPs 
 ['T1071.001 (Application Layer Protocol: Web Protocols) – High confidence', 'T1566.002 (Phishing: Spearphishing Link) – High confidence', 'T1071.003 (Application Layer Protocol: Mail Protocols) – Medium confidence', 'T1566.001 (Phishing: Spearphishing Attachment) – Medium confidence', 'T1071.004 (Application Layer Protocol: Dynamic Data Exchange) – Medium confidence'] 

#### Impact 
 The exact impact in terms of the number of devices or financial losses is not detailed in the report. However, the campaign involves widespread phishing attacks leveraging trusted platforms, potentially affecting numerous users and organizations. *Furthermore, the use of stolen email threads and HTML obfuscation techniques help attackers evade detection and increase the phishing email's credibility* (https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns/). 

#### Mitigation Steps 
 ['Educate employees on recognizing phishing attempts, especially those involving legitimate services.', 'Implement robust email filtering solutions to detect and block phishing emails.', 'Utilize URL filtering to block access to known malicious sites.', 'Enable multi-factor authentication (MFA) for sensitive accounts and services.', 'Regularly update and patch all systems and applications to prevent exploitation of vulnerabilities.', 'Monitor for unusual account activity, especially those involving external file-sharing services.'] 

#### Detection Signature 
 {'Service': 'Microsoft OneDrive, Dynamics 365, Atlassian Confluence, Google Docs Viewer, LiveAgent', 'Port': 'Various (dependent on service)', 'Severity': 'Critical', 'Incident': 'Phishing using legitimate services', 'Signature name': 'Phishing via legitimate service abuse', 'Internal checks': ['Verify URLs in emails against known phishing databases.', 'Monitor for unusual creation of URL shortcut files in OneDrive.', 'Check for abnormal access patterns in OneNote and Dynamics 365.'], 'External scanning': ['Look for suspicious redirects involving legitimate services.', 'Identify unusual URL patterns and domains, especially those mimicking trusted services.']} 

#### IoCs:
- url: hxxps://www.curiosolucky.com/dos/ ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: hxxps://magenta-melodious-garnet.glitch.me/public/rc.htm ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: hxxps://link.trustpilot.com/ls/click?upn=u001.u9-NN-jLZCX2YnHXPQ1lM4gqkGMqJbqpuJx-FSxHxK-HK5blCjdqA4sTpFhMxVuvd4F2C_ytJ-BU3wnk2t0HzMc51nsdI5jCvjlH5KkDNOR5oq1uEJItlkSMD-0mdF-2B0td2onmiDV9xpRWw-dvTM3A0wCvdsiFkF1kSdgdFrVAE78L337Qo3s56Gk0s6E6DwCfNIKl8bRli5iK2LUC2ldGxjFPYGCigbeEgNBwg1dcBwOOCSSMKGEAZxhwoFvF5-m5JIsTGsZgQlFDpHLis00H4SRzSjnDGYeia8OxbZOi3NmC9Zu0y59gc0DEENkQqz3vpJLxuDhLJpYJpzgnl5FKcj4hKsjfHYOBYWFlwHMrDBS4Cvh4Jej-zpBQsqkaAsezwGEEHqB22DcDQgay2Cm-bbwAcZMOxqHcQjy3nz6aJyACCXDZkVr8P3iPKgjlqDjbsFb-BJ-uUIiNGVhLp1-3wvR6hrzO1bA127bZ68-bmxJz7ux0F5Htfv1SipEoRgLt6VWovRUTbAmRMRtZHvPS49KRBqCjzSnmChbhoVriyoBm5l9IeUaV5raA4vZxPckk3vcYaVa0xmCZLDFC14eTimJvqIk1CqOPtji8DUcs3pyfer4J-Fk-3D ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url hxxps://link.trustpilot.com/ls/click?upn=u001.u9-NN-jLZCX2YnHXPQ1lM4gqkGMqJbqpuJx-FSxHxK-HK5blCjdqA4sTpFhMxVuvd4F2C_ytJ-BU3wnk2t0HzMc51nsdI5jCvjlH5KkDNOR5oq1uEJItlkSMD-0mdF-2B0td2onmiDV9xpRWw-dvTM3A0wCvdsiFkF1kSdgdFrVAE78L337Qo3s56Gk0s6E6DwCfNIKl8bRli5iK2LUC2ldGxjFPYGCigbeEgNBwg1dcBwOOCSSMKGEAZxhwoFvF5-m5JIsTGsZgQlFDpHLis00H4SRzSjnDGYeia8OxbZOi3NmC9Zu0y59gc0DEENkQqz3vpJLxuDhLJpYJpzgnl5FKcj4hKsjfHYOBYWFlwHMrDBS4Cvh4Jej-zpBQsqkaAsezwGEEHqB22DcDQgay2Cm-bbwAcZMOxqHcQjy3nz6aJyACCXDZkVr8P3iPKgjlqDjbsFb-BJ-uUIiNGVhLp1-3wvR6hrzO1bA127bZ68-bmxJz7ux0F5Htfv1SipEoRgLt6VWovRUTbAmRMRtZHvPS49KRBqCjzSnmChbhoVriyoBm5l9IeUaV5raA4vZxPckk3vcYaVa0xmCZLDFC14eTimJvqIk1CqOPtji8DUcs3pyfer4J-Fk-3D in VT. 

- url: hxxps://docsend.com/view/q6f7ukbdeviagha2 ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: hxxps://cloudflare-kol.github.io/out/red.html?url=aHR0cHM6Ly9zaG9ydHVybC5hdC80SlZnbg== ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: hxxps://r.g.bing.com/bam/ac?!&daydream=vasectomy&u=a1aHR0cHM6Ly9jeWJlcm5leGlsbHVtby56YS5jb20vVFZOUHIv== ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 
Not found for url hxxps://r.g.bing.com/bam/ac?!&daydream=vasectomy&u=a1aHR0cHM6Ly9jeWJlcm5leGlsbHVtby56YS5jb20vVFZOUHIv== in VT. 

- url: hxxps://ctrk.klclick3.com/l/01J5V2NHDC0KB0P8B51Z9PCPZS_0 ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: hxxps://googlevoicesecrets.com/EHkslw5/auth/?_kx=lKiN48B6FuEu_OYp2PJPXw.Sdgjsn ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: hxxps://semi-zcmp.maillist-manage.com/click/1122f15d012c0933f/1122f15d012c08f77?utm_source=aynures-newsletter.beehiiv.com&utm_medium=newsletter&utm_campaign=yes-my-gee&_bhlid=c1191c405e82c32c645acb82f875fdd8fad29209 ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: hxxps://involucrases.sa.com/ ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: hxxps://callcenter838685d0747612ac193e85fcb5ae45287b09e8a0mailvoice.s3.us-east-2.amazonaws.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: hxxps://pub-fe581134d7ae4857a97443270a27e0fa.r2.dev/0nedrive.html ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: hxxps://docsecureatt-docdrive-filedoc.pages.dev/ ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: curiosolucky.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: senderbulk.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: docsend.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: shorturl.at ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: googlevoicesecrets.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: sa.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: packinqsystems.de ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- domain: pages.dev ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas)) 

- url: https://[TenantName]-my.sharepoint.com/personal/[UserPrincipalName] ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 
Not found for url https://[TenantName]-my.sharepoint.com/personal/[UserPrincipalName] in VT. 

- url: https://1drv.ms/o/s!Ar8dxVBUvGlGiIgzb0_10Zq_e9ysmQ ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 
Not found for url https://1drv.ms/o/s!Ar8dxVBUvGlGiIgzb0_10Zq_e9ysmQ in VT. 

- url: https://emea.dcv.ms/5IgHbcWiml ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 

- url: https://[redacted].atlassian.net/wiki/external/ZWQxMzM2MDdmMTEwNDk5NDgwZGNlZDJkZmNkOTE4ZmY ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 
Not found for url https://[redacted].atlassian.net/wiki/external/ZWQxMzM2MDdmMTEwNDk5NDgwZGNlZDJkZmNkOTE4ZmY in VT. 

- url: https://[redacted].ladesk.com/XXXXXXX-SECURE-BUSINESS-DOCUMENTS ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 
Not found for url https://[redacted].ladesk.com/XXXXXXX-SECURE-BUSINESS-DOCUMENTS in VT. 

- url: https://weathered-waterfall-4976.tekot88473.workers.dev/?e=&lt;email&gt; ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 
Not found for url https://weathered-waterfall-4976.tekot88473.workers.dev/?e=&lt;email&gt; in VT. 

- url: https://luthschoenmode.nl/winkel/generated/arull.php?7104797967704b536932307466507a53784b7a4d37494c79704b7a4d73723053744f314 ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 
Not found for url https://luthschoenmode.nl/winkel/generated/arull.php?7104797967704b536932307466507a53784b7a4d37494c79704b7a4d73723053744f314 in VT. 

- url: https://www.arceva.site/uploads/images/24_01/pbcmc.php?0096797967704b53693230746376793079703145334f7953394e7964524c7a732f564b38 ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 
Not found for url https://www.arceva.site/uploads/images/24_01/pbcmc.php?0096797967704b53693230746376793079703145334f7953394e7964524c7a732f564b38 in VT. 

- domain: 54774675.rainblessings.pages.dev ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 

- domain: saluminyum.com ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 

- domain: vilug-onteroi.com.pl ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 

- domain: lifestreamtechho.ru ([link](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/rockstar-2fa-phishing-as-a-service-paas-noteworthy-email-campaigns)) 

- For more IoCs, please refer to the above links. 

#### paste IoC
hxxps://www.curiosolucky.com/dos/
hxxps://magenta-melodious-garnet.glitch.me/public/rc.htm
hxxps://docsend.com/view/q6f7ukbdeviagha2
hxxps://cloudflare-kol.github.io/out/red.html?url=aHR0cHM6Ly9zaG9ydHVybC5hdC80SlZnbg==
hxxps://ctrk.klclick3.com/l/01J5V2NHDC0KB0P8B51Z9PCPZS_0
hxxps://googlevoicesecrets.com/EHkslw5/auth/?_kx=lKiN48B6FuEu_OYp2PJPXw.Sdgjsn
hxxps://semi-zcmp.maillist-manage.com/click/1122f15d012c0933f/1122f15d012c08f77?utm_source=aynures-newsletter.beehiiv.com&utm_medium=newsletter&utm_campaign=yes-my-gee&_bhlid=c1191c405e82c32c645acb82f875fdd8fad29209
hxxps://involucrases.sa.com/
hxxps://callcenter838685d0747612ac193e85fcb5ae45287b09e8a0mailvoice.s3.us-east-2.amazonaws.com
hxxps://pub-fe581134d7ae4857a97443270a27e0fa.r2.dev/0nedrive.html
hxxps://docsecureatt-docdrive-filedoc.pages.dev/
curiosolucky.com
senderbulk.com
docsend.com
shorturl.at
googlevoicesecrets.com
sa.com
packinqsystems.de
pages.dev
https://emea.dcv.ms/5IgHbcWiml
54774675.rainblessings.pages.dev
saluminyum.com
vilug-onteroi.com.pl
lifestreamtechho.ru

