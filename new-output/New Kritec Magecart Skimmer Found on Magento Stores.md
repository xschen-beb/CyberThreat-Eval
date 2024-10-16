Source: [https://www.malwarebytes.com/blog/threat-intelligence/2023/03/new-kritec-skimmer](https://www.malwarebytes.com/blog/threat-intelligence/2023/03/new-kritec-skimmer)

# New Kritec Magecart Skimmer Found on Magento Stores

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: New Kritec Magecart skimmer found on Magento stores 

 Root cause: The incident was due to the presence of unsecured and vulnerable Magento stores that were exploited by threat actors. The root cause includes:
- Lack of proper security measures on Magento stores.
- Usage of compromised and malicious scripts such as the Kritec skimmer.
- Abuse of Cloudflare services to conceal the malicious infrastructure.
- *Usage of Google Tag Manager (GTM) to hide the skimmer* (https://social.cyware.com/news/new-kritec-skimming-malware-found-targeting-magento-stores-469974ed). 

 Threat Actor/group/campaign: Kritec threat actor (specific group not identified). 

 Organization/industry/location: The victims are e-commerce websites utilizing Magento for their online stores. 

 Start date – End date: The specific dates of the attacks are not mentioned, but the blog post was published on March 22, 2023. 

 MITRE TTPs: - T1071.001: Application Layer Protocol: Web Protocols
- T1003: Credential Dumping
- T1071.004: Application Layer Protocol: DNS
- T1059.007: Command and Scripting Interpreter: JavaScript 

 Impact: The impact includes the theft of credit card information from compromised Magento stores. The exact number of records or financial losses was not specified. *Stolen card details are sent twice—via WebSocket and POST request* (https://social.cyware.com/news/new-kritec-skimming-malware-found-targeting-magento-stores-469974ed). 

 Mitigation: 1. **Update and Patch Management**: Ensure Magento and all related plugins are up-to-date with the latest security patches.
2. **Web Application Firewall (WAF)**: Deploy a WAF to filter out malicious traffic.
3. **Security Monitoring**: Implement continuous monitoring for unusual activities and unauthorized changes.
4. **Content Security Policy (CSP)**: Use CSP headers to prevent unauthorized JavaScript from executing.
5. **Regular Security Audits**: Conduct regular security audits and vulnerability assessments.
6. **Secure Configuration**: Ensure proper and secure configuration of web servers and applications.
7. **Incident Response Plan**: Develop and maintain an incident response plan to quickly address any breaches. 

 Detection Signature: - **Service**: Web application (Magento)
- **Port**: 443 (HTTPS)
- **Severity**: Critical
- **Incident**: Magecart skimming attack
- **Signature name**: “Magecart skimmer detected”
  - **Internal checks**:
      - Setting1: Monitor JavaScript inclusions and detect unauthorized scripts.
      - Setting2: Check for unexpected changes in web pages, especially payment pages.
      - Setting3: Validate all third-party scripts and ensure they come from trusted sources.
  - **External scanning**:
      - Detect malicious domains and IPs known for skimming activities.
      - Monitor for suspicious POST requests to unknown or external endpoints. 

 IoCs: - WebSocket Skimmer: cloud-cdn[.]org
- Kritec skimmer domains:
  - kritec[.]pics
  - vitalmob[.]pics
  - flowit[.]pics
  - flagmob[.]quest
  - entrydelt[.]sbs
  - sanpatech[.]shop
  - prijetech[.]shop
  - nebiltech[.]shop
  - kruktech[.]shop
  - lavutele[.]yachts
  - tochdigital[.]pics
  - smestech[.]shop
  - klstech[.]shop
  - shotsmob[.]sbs
  - gemdigit[.]pics
  - nevomob[.]quest
  - vuroselec[.]quest
  - apexit[.]yachts
  - sorotele[.]yachts
  - bereelec[.]quest
  - apexit[.]yachts/apex[.]min[.]js
  - vuroselec[.]quest/dych[.]min[.]js
  - nevomob[.]quest/elan-loader[.]js
  - gemdigit[.]pics/wpp-loader[.]js
  - gemdigit[.]pics/sun-loader[.]js
  - klstech[.]shop/opencart-cache-worker[.]min[.]js
  - tochdigital[.]pics/digital[.]min[.]js
  - vitalmob[.]pics/pre-loader[.]js
  - Additional IOCs from Sucuri:
    - ukatec[.]pics/uk.min.js
    - gretit[.]yachts/lazy.min.js
    - ledeehub[.]shop/hub.min.js
    - rithdigit[.]cyou/ik-loader.js
    - kouelec[.]cyou/postcodeanywhere.js
    - pracelec[.]yachts/excl-tax.js
    - accotech[.]quest/lazysize.min.js
    - paunit[.]pics/dlab.js
    - defimob[.]bar/slide.js
    - screenmet[.]sbs/map.js
    - shokomob[.]sbs
    - regtech[.]sbs
    - oumymob[.]shop
    - nujtec[.]shop
    - cloveselec[.]quest 


# Related articles (describing the same threat) 
['https://www.malwarebytes.com/blog/threat-intelligence/2023/03/new-kritec-skimmer', 'https://social.cyware.com/news/new-kritec-skimming-malware-found-targeting-magento-stores-469974ed']
