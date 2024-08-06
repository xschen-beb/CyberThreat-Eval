# Botnet Fenix New Botnet Going After Tax Payers in Mexico and Chile

Incident: Botnet Fenix: New botnet going after tax payers in Mexico and Chile

Root cause: Exploitation of vulnerable WordPress engines and creation of typosquatting domains

Impact: Thousands of tax-paying individuals in Mexico and Chile potentially impacted. Financial losses include stolen credentials, unauthorized access to sensitive information, and possible monetary theft.

Mitigation: Strengthen web security measures and user education. **Detailed Steps for mitigation:**

1. **Secure WordPress Installations:**
   - Regularly update WordPress to the latest version.
   - Use security plugins to detect and mitigate vulnerabilities.
   - Implement strong authentication measures (e.g., 2FA).

2. **Domain Monitoring and Takedown:**
   - Monitor for typosquatting domains and initiate takedown processes for fraudulent domains.
   - Use threat intelligence services to stay informed about new phishing domains.

3. **User Education:**
   - Educate users to recognize phishing attempts and avoid downloading software from untrusted sources.
   - Promote the use of official government portals and verify URLs before entering sensitive information.

4. **Implement Security Tools:**
   - Deploy endpoint protection solutions to detect and block malicious downloads.
   - Use network monitoring tools to identify and block suspicious traffic.

5. **Incident Response Plan:**
   - Develop and regularly update an incident response plan to quickly address breaches.
   - Conduct regular security audits and simulations to ensure preparedness.

Detection Signature:
   Service: WordPress
   Port: 80/443 (HTTP/HTTPS)
   Severity: Critical
   Incident: Botnet Fenix
   Signature name: “Exposed WordPress vulnerabilities”
   Internal checks:
      - Setting1: WordPress version should be up-to-date. – In platform
      - Setting2: Security plugins should be active and up-to-date. – Inside VMs
      - Setting3: Strong authentication measures (e.g., 2FA) should be enabled. – Inside VMs
   External scanning:
      - Outdated WordPress versions
      - Presence of known vulnerabilities

IoCs found:
   Hashes:
      - B10B9F1F286F7AE29D9E87C5391D3653
      - 500B1C312163009FEFEC3F8FE7861258
      - 594804AA21887EE9D7B1B888F482D60C
      - 1C50C6D0AEAF8071F528B76B1AB242FE
      - D80F1780BB24E7ECDAB8A262744BCCB7
      - 1BE0606640D645DDBFB2FBDFF53CA918
      - 7631660BDCF74B95B5806328A7668CAB
      - EAFF13D6C89CE0E2A7632BD811045C35
      - EA68E0CC90A88315526704BAE1CA8B4A
      - B262B36C3B09EBEAB66C95E121BE4C73
      - 6F0B4018DA4AA0887B5AA879CE315543
      - 7FE97D4E29E17F39E343A9EF5FDE03CA
   
   URLs:
      - file[:]\\139[.]162[.]73[.]58@80\SuECWRPQ\SAT_Herramienta_Seguridad[.]jse
      - file[:]\\139[.]162[.]73[.]58@80\YtmpEoBw\Herramienta_de_Seguridad_SII[.]jse
      - hxxps[:]//fja[.]com[.]mx/wp-contents/execution[.]php?tag=russian
      - hxxps[:]//fja[.]com[.]mx/wp-contents/init[.]php?id=1
      - hxxps[:]//www[.]grafoce[.]com/scripts/index[.]php?id=2
      - hxxps[:]//www[.]grafoce[.]com/wp-contents/execution[.]php?tag=russian
      - hxxps[:]//russiancl[.]top/bramx/7684jasdtg[.]xls
      - hxxps[:]//russiancl[.]top/bramx/post[.]php
      - hxxps[:]//russiancl[.]top/bramx/ot[.]crypt
      - hxxps[:]//russiancl[.]top/bramx/proxy[.]crypt
      - hxxps[:]//russiancl[.]top/bramx/steal[.]crypt
   
   Domains:
      - 2repuvegobmx[.]com.mx
      - annydesk.website
      - citasatmx2023[.]lat
      - citas-sat2023[.]com.mx
      - citas-satmx[.]com
      - citas-sregob-mexico[.]com
      - consultacurp-gobmx[.]com.mx
      - consultacurp-gobmx[.]com[.]mx
      - fja[.]com[.]mx
      - grafoce[.]com
      - lbci-seguro[.]com
      - mexico-curp[.]com
      - russiancl[.]top
      - siii-chile[.]com
      - sre-curpmexico[.]com
      - tramites-sat[.]com.mx
      - whatsapp.website
   
   IP Addresses:
      - 207.210.228[.]67
      - 139.162.73[.]58
      - 80.66.64[.]154
   
   Filenames:
      - SII_Seguro_XXXXXX.zip
      - Herramienta Seguridad SII.url
      - AT_herramienta_XXXXXX.zip
      - SAT_Herramienta_Seguridad.jse
      - b262b36c3b09ebeab66c95e121be4c73
      - 7684jasdtg.xls
      - B10B9F1F286F7AE29D9E87C5391D3653
      - ot.crypt
      - 500B1C312163009FEFEC3F8FE7861258
      - proxy.crypt
      - 594804AA21887EE9D7B1B888F482D60C
      - steal.crypt
      - 1C50C6D0AEAF8071F528B76B1AB242FE
      - pay.txt
