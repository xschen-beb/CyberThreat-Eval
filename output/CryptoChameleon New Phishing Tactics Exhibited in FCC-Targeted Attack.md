Source: [https://www.lookout.com/threat-intelligence/article/cryptochameleon-fcc-phishing-kit](https://www.lookout.com/threat-intelligence/article/cryptochameleon-fcc-phishing-kit)

# CryptoChameleon New Phishing Tactics Exhibited in FCC-Targeted Attack

### Incident: CryptoChameleon: New Phishing Tactics Exhibited in FCC-Targeted Attack

#### Root cause: Sophisticated phishing kit mimicking legitimate SSO pages and leveraging multi-factor authentication (MFA) interception.

#### Impact: Over 100 victims, mostly cryptocurrency users and FCC employees, were tricked into divulging sensitive information such as usernames, passwords, OTP tokens, and photo IDs. The financial losses are potentially significant due to the nature of the targeted platforms (cryptocurrency exchanges and financial services).

#### Mitigation: 
1. **User Education and Awareness:** Train employees to recognize phishing attempts, especially those mimicking SSO pages.
2. **Enhanced Email Filtering:** Implement advanced email filtering solutions to detect and block phishing emails.
3. **Multi-Factor Authentication:** Encourage the use of hardware-based MFA tokens which are less susceptible to phishing.
4. **Domain Monitoring:** Regularly monitor for suspicious domain registrations similar to organizational domains.
5. **Security Audits:** Conduct regular security audits on authentication mechanisms and SSO implementations.
6. **Incident Response Plan:** Develop and test an incident response plan to quickly address phishing incidents.
7. **Browser Security:** Use browser security measures like anti-phishing features and browser extensions designed to detect phishing pages.

**Detailed Steps for Mitigation:**
1. **User Education and Awareness:**
   - Conduct regular training sessions and phishing simulations.
   - Distribute educational materials that highlight the characteristics of phishing attempts.

2. **Enhanced Email Filtering:**
   - Deploy advanced email security solutions capable of identifying and quarantining phishing emails.
   - Utilize AI/ML-based solutions for real-time detection and blocking of phishing emails.

3. **Multi-Factor Authentication:**
   - Transition to hardware-based MFA tokens like YubiKey.
   - Educate users on the importance of not sharing OTPs and recognizing suspicious requests.

4. **Domain Monitoring:**
   - Use domain monitoring services to track and alert on new domain registrations that are similar to your organization’s domain.
   - Actively report and take down phishing domains.

5. **Security Audits:**
   - Conduct periodic security reviews of SSO systems and authentication mechanisms.
   - Include phishing resistance testing in the audit scope.

6. **Incident Response Plan:**
   - Develop a comprehensive incident response plan tailored to phishing attacks.
   - Regularly test and update the plan to incorporate lessons learned from previous incidents.

7. **Browser Security:**
   - Encourage the use of browsers with built-in anti-phishing features.
   - Deploy browser extensions that help in identifying and blocking phishing sites.

#### Detection Signature:
- **Service:** Web Hosting Services (Hostwinds, Hostinger, RetnNet, QWARTA LLC, OOO Westcall Ltd)
- **Port:** Various (HTTP/HTTPS ports 80/443)
- **Severity:** Critical
- **Incident:** CryptoChameleon Phishing Campaign
- **Signature name:** “Phishing page mimicking FCC Okta”
- **Internal checks:**
  - Setting1: Monitor for suspicious domain registrations similar to organizational domains.
  - Setting2: Implement advanced email filtering solutions.
  - Setting3: Regularly audit SSO systems and authentication mechanisms.
- **External scanning:**
  - Monitor for new domain registrations and hosted phishing pages.
  - Use external threat intelligence feeds to detect phishing sites.

#### IoCs:
- **Command and Control servers:**
   - lookoutsucks[.]com
   - official-server[.]com
   - server694590423[.]tech
   - island-placid-bromine.glitch[.]me
   - circular-noon-farmhouse.glitch[.]me
   - talented-friendly-price.glitch[.]me
   - dflfmgsdokasdcpl[.]com
   - original-backend[.]com

- **Phishing websites:**
   - help-lastpass[.]com
   - 113712-coinbase[.]com
   - 113912-coinbase[.]com
   - 129045-coinbase[.]com
   - 142724-coinbase[.]com
   - 142746-coinbase[.]com
   - 142764-coinbase[.]com
   - 142786-coinbase[.]com
   - 145126-coinbase[.]com
   - 146282-coinbase[.]com
   - 146784-coinbase[.]com
   - 148942-coinbase[.]com
   - 1502759-ledger[.]com
   - 1519845-kraken[.]com
   - 157192-uphold[.]com
   - 157194-gemini[.]com
   - 16159867-coinbase[.]com
   - 16275-coinbase[.]com
   - 167243-coinbase[.]com
   - 17224652-coinbase[.]com
   - 17384624-coinbase[.]com
   - 173912-coinbase[.]com
   - 17412627-coinbase[.]com
   - 17512457-coinbase[.]com
   - 17512657-coinbase[.]com
   - 1751654-coinbase[.]com
   - 1751854-coinbase[.]com
   - 1751954-coinbase[.]com
   - 17591024-coinbase[.]com
   - 1759654-coinbase[.]com
   - 17612416-coinbase[.]com
   - 17612418-gemini[.]com
   - 17612412-coinbase[.]com
   - 17612486-coinbase[.]com
   - 17618412-coinbase[.]com
   - 17625-coinbase[.]com
   - 17682192-coinbase[.]com
   - 176822-coinbase[.]com
   - 176823-coinbase[.]com
   - 176824-coinbase[.]com
   - 17691-coinbase[.]com
   - 17825-coinbase[.]com
   - 17913-coinbase[.]com
   - 17916-coinbase[.]com
   - 185417-coinbase[.]com
   - 185421-coinbase[.]com
   - 18547-coinbase[.]com
   - 185614-coinbase[.]com
   - 185617-coinbase[.]com
   - 185914-coinbase[.]com
   - 185924-uphold[.]com
   - 187421-coinbase[.]com
   - 18925-coinbase[.]com
   - 191284-coinbase[.]com
   - 192854-gemini[.]com
   - 192856-coinbase[.]com
   - 195102-coinbase[.]com
   - 195127-coinbase[.]com
   - 19524624-coinbase[.]com
   - 19562-coinbase[.]com
   - 19582-coinbase[.]com
   - 195827-binance[.]com
   - 197287-coinbase[.]com
   - 83730493-coinbase[.]com
   - 90251-gmail[.]com
   - 90251-icloud[.]com
   - account-help-icloud[.]com
   - appie-pay[.]com
   - appleassist[.]org
   - applepayhelp[.]net
   - applepayhelp[.]org
   - blocked-coinbase[.]com
   - bofa-help[.]com
   - coinbase-login[.]com
   - coinbase-ticketsupport[.]com
   - coinbaseticketsupport[.]com
   - com-175691[.]help
   - com-83730493[.]help
   - com-fraud[.]management
   - com-ticket[.]info
   - compensation-coinbase[.]com
   - deposit-coinbase[.]com
   - finance-coinbase[.]com
   - firewall-coinbase[.]com
   - handle-coinbase[.]com
   - help-lastpass[.]com
   - indentity-coinbase[.]com
   - lockdown-coinbase[.]com
   - lockup-coinbase[.]com
   - login-nexo[.]com
   - nexotickets[.]com
   - officialbackupserver[.]com
   - original-backend[.]com
   - protection-kraken[.]com
   - receipt-coinbase[.]com
   - refunding-coinbase[.]com
   - reimburse-coinbase[.]com
   - reverts-coinbase[.]com
   - secureunlock-coinbase[.]com
   - securing-coinbase[.]com
   - swap-coinbase[.]com
   - ticketsupport-coinbase[.]com
   - transfers-kraken[.]com
   - unlock-kraken[.]com
   - verify-trezor[.]io
   - www-cb-wallet[.]com
   - www-cbwallet[.]com
   - www-coinbasewallet[.]com
   - www-help-apple[.]com
   - www-help-coinbase[.]com
   - bofa-help[.]com
   - suite-trezor[.]io
   - compensate-coinbase[.]com
   - 142784-coinbase[.]com
   - ss-icloud[.]com
   - 07159889-coinbase[.]com
   - 10195-coinbase[.]com
   - 11246-coinbase[.]com
   - 11247-coinbase[.]com
   - 11248-coinbase[.]com
   - 11258-coinbase[.]com
   - 11259-coinbase[.]com
   - 113912-coinbase[.]com
   - 11472-coinbase[.]com
   - 11923-coinbase[.]com
   - 11957-coinbase[.]com
   - 128147-coinbase[.]com
   - 12958-coinbase[.]com
   - 12984-okta[.]com
   - 12985-coinbase[.]com
   - 13130-coinbase[.]com
   - 13247-coinbase[.]com
   - 13247-icloud[.]com
   - 13267-coinbase[.]com
   - 146271510-coinbase[.]com
   - 146282-coinbase[.]com
   - 146284-coinbase[.]com
   - 147260-coinbase[.]com
   - 14765-coinbase[.]com
   - 14817582-coinbase[.]com
   - 14871904-coinbase[.]com
   - 14891902-coinbase[.]com
   - 1492864-coinbase[.]com
   - 158312-coinbase[.]com
   - 158372-coinbase[.]com
   - 158702-coinbase[.]com
   - 16171675-coinbase[.]com
   - 16171832-coinbase[.]com
   - 16178234-coinbase[.]com
   - 16178237-coinbase[.]com
   - 16178434-coinbase[.]com
   - 162178-coinbase[.]com
   - 162478-coinbase[.]com
   - 162782-coinbase[.]com
   - 162812-coinbase[.]com
   - 162814-coinbase[.]com
   - 16442580-coinbase[.]com
   - 16450107-coinbase[.]com
   - 16450207-coinbase[.]com
   - 16458207-coinbase[.]com
   - 16478202-coinbase[.]com
   - 164872942-coinbase[.]com
   - 16590-coinbase[.]com
   - 16594373-coinbase[.]com
   - 16624831-coinbase[.]com
   - 16642124-coinbase[.]com
   - 16642172-coinbase[.]com
   - 16642580-coinbase[.]com
   - 16642721-coinbase[.]com
   - 16642724-coinbase[.]com
   - 16642871-coinbase[.]com
   - 16642872-coinbase[.]com
   - 16712942-coinbase[.]com
   - 16718672-coinbase[.]com
   - 16728342-coinbase[.]com
   - 16728348-coinbase[.]com
   - 16728442-coinbase[.]com
   - 16728472-coinbase[.]com
   - 167285-coinbase[.]com
   - 16729042-coinbase[.]com
   - 16748272-coinbase[.]com
   - 16782942-coinbase[.]com
   - 16827420-coinbase[.]com
   - 16827423-coinbase[.]com
   - 16847145-coinbase[.]com
   - 16893924-coinbase[.]com
   - 17182-coinbase[.]com
   - 17255030-coinbase[.]com
   - 17259-kraken[.]com
   - 172486-coinbase[.]com
   - 17284652-coinbase[.]com
   - 17286-coinbase[.]com
   - 17334522-coinbase[.]com
   - 17334522-kraken[.]com
   - 17384522-coinbase[.]com
   - 173912-coinbase[.]com
   - 17494976-coinbase[.]com
   - 17512854-coinbase[.]com
   - 17512857-coinbase[.]com
   - 1751954-coinbase[.]com
   - 17525030-coinbase[.]com
   - 17529580-coinbase[.]com
   - 17614-coinbase[.]com
   - 17618412-coinbase[.]com
   - 17619-coinbase[.]com
   - 176284-coinbase[.]com
   - 17823920-coinbase[.]com
   - 178253-coinbase[.]com
   - 178294-coinbase[.]com
   - 17912-coinbase[.]com
   - 17914-coinbase[.]com
   - 17917-coinbase[.]com
   - 17954-coinbase[.]com
   - 17958-coinbase[.]com
   - 182043-coinbase[.]com
   - 18275-gemini[.]com
   - 18276-coinbase[.]com
   - 18290185-coinbase[.]com
   - 182967-coinbase[.]com
   - 18560-coinbase[.]com
   - 18571-coinbase[.]com
   - 185912-coinbase[.]com
   - 185914-coinbase[.]com
   - 18592176-coinbase[.]com
   - 18594162-coinbase[.]com
   - 18594962-coinbase[.]com
   - 18597162-coinbase[.]com
   - 18719562-coinbase[.]com
   - 1875290-coinbase[.]com
   - 1882730-coinbase[.]com
   - 18902-coinbase[.]com
   - 18903-coinbase[.]com
   - 189126-coinbase[.]com
   - 18952-coinbase[.]com
   - 192854-coinbase[.]com
   - 192856-coinbase[.]com
   - 19287-binance[.]com
   - 19572-coinbase[.]com
   - 195812-coinbase[.]com
   - 195826-coinbase[.]com
   - 1958262-coinbase[.]com
   - 195827-binance[.]com
   - 1958297-coinbase[.]com
   - 19582970-coinbase[.]com
   - 19582971-coinbase[.]com
   - 19583-coinbase[.]com
   - 19592653-coinbase[.]com
   - 197304-coinbase[.]com
   - 19730492-coinbase[.]com
   - 19764162-coinbase[.]com
   - 19803-coinbase[.]com
   - 201784289-coinbase[.]com
   - 210823644-coinbase[.]com
   - 21158-coinbase[.]com
   - 21509-coinbase[.]com
   - 25985-coinbase[.]com
   - 27699-coinbase[.]com
   - 28367-coinbase[.]com
   - 28676-coinbase[.]com
   - 29185-coinbase[.]com
   - 29195-coinbase[.]com
   - 2a-coinbase[.]com
   - 2b-coinbase[.]com
   - 2c-coinbase[.]com
   - 2f-coinbase[.]com
   - 2fas-coinbase[.]com
   - 2o-coinbase[.]com
   - 2r-coinbase[.]com
   - 2s-coinbase[.]com
   - 2sv-coinbase[.]com
   - 352134951-coinbase[.]com
   - 38468-coinbase[.]com
   - 39590-coinbase[.]com
   - 41260-coinbase[.]com
   - 427883-coinbase[.]com
   - 43017-coinbase[.]com
   - 47562-coinbase[.]com
   - 501
