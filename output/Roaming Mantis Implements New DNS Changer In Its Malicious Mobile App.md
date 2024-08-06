# Roaming Mantis Implements New DNS Changer In Its Malicious Mobile App

Incident: Roaming Mantis DNS Changer

Root cause: Vulnerable Wi-Fi Routers and Android Malware

Impact: The number of impacted devices and financial losses are not explicitly mentioned in the document. However, the report shows that this malware has affected multiple regions and includes thousands of APK downloads in Japan (24,645), Austria (7,354), France (7,246), etc. Financial losses could be significant due to the subsequent phishing and credential theft.

Mitigation: 
- **Secure Wi-Fi Routers**:
  - Change default admin credentials on Wi-Fi routers.
  - Regularly update router firmware to patch security vulnerabilities.
  - Disable remote management features if not needed.
  - Implement strong, unique passwords and consider using WPA3 for Wi-Fi security.
  - Limit admin access to trusted devices only.

- **Secure Android Devices**:
  - Advise users to download apps only from trusted sources like Google Play Store.
  - Regularly update Android OS and apps to the latest versions.
  - Use reputable mobile security solutions to detect and block malware.

Detection Signature:
Service: Wi-Fi Router (various models, especially those by EFM Networks)
Port: 80 (HTTP), 443 (HTTPS)
Severity: Critical
Incident: Roaming Mantis DNS Changer
Signature name: “Wi-Fi Router DNS Changer Vulnerability”
Internal checks:
  - Setting1: Ensure default admin credentials are changed.
  - Setting2: Firmware should be updated to the latest version.
  - Setting3: Remote management features should be disabled if not necessary.
External scanning:
  - Check for open HTTP/HTTPS ports on the router.
  - Test if the router is using default login credentials.

IoCs:
- MD5 of Wroba.o:
  - 2036450427a6f4c39cd33712aa46d609
  - 8efae5be6e52a07ee1c252b9a749d59f
  - 95a9a26a95a4ae84161e7a4e9914998c
  - ab79c661dd17aa62e8acc77547f7bd93
  - d27b116b21280f5ccc0907717f2fd596
  - f9e43cc73f040438243183e1faf46581

- Domains of landing pages:
  - 1hy5.cwdqh[.]com
  - 3.wubmh[.]com
  - 3y.tmztp[.]com
  - 53th.xgunq[.]com
  - 5c2d.zgngu[.]com
  - 5.hmrgt[.]com
  - 8.ondqp[.]com
  - 9v.tbeew[.]com
  - d.vbmtu[.]com
  - g.dguit[.]com
  - j.vbrui[.]com
  - k.uvqyo[.]com
  - kwdd.cehsg[.]com
  - mh.mgtnv[.]com
  - o.wgvpd[.]com
  - r48.bgxbm[.]com
  - t9o.qcupn[.]com
  - vj.nrgsd[.]com
  - w3.puvmw[.]com
  - xtc9.rvnbg[.]com
  - y.vpyhc[.]com

- IPs of landing pages:
  - 103.80.134[.]40
  - 103.80.134[.]41
  - 103.80.134[.]42
  - 103.80.134[.]48
  - 103.80.134[.]49
  - 103.80.134[.]50
  - 103.80.134[.]51
  - 103.80.134[.]52
  - 103.80.134[.]53
  - 103.80.134[.]54
  - 134.122.137[.]14
  - 134.122.137[.]15
  - 134.122.137[.]16
  - 199.167.138[.]36
  - 199.167.138[.]38
  - 199.167.138[.]39
  - 199.167.138[.]40
  - 199.167.138[.]41
  - 199.167.138[.]43
  - 199.167.138[.]44
  - 199.167.138[.]45
  - 199.167.138[.]48
  - 199.167.138[.]49
  - 199.167.138[.]51
  - 199.167.138[.]52
  - 27.124.36[.]32
  - 27.124.36[.]34
  - 27.124.36[.]52
  - 27.124.39[.]241
  - 27.124.39[.]242
  - 27.124.39[.]243
  - 91.204.227[.]131
  - 91.204.227[.]132
  - 91.204.227[.]144
  - 91.204.227[.]145
  - 91.204.227[.]146

- Rogue DNS:
  - 193.239.154[.]15
  - 193.239.154[.]16
  - 193.239.154[.]17
  - 193.239.154[.]18
  - 193.239.154[.]22

- Hardcoded malicious accounts of vk.com to obtain live rogue DNS servers:
  - id728588947

- Providing live rogue DNS servers:
  - 107.148.162[.]237:26333/sever.ini

- Suspicious accounts/pages of some legitimate services for obtaining C2s:
  - http://m.vk[.]com/id668999378?act=info
  - http://m.vk[.]com/id669000526?act=info
  - http://m.vk[.]com/id669000956?act=info
  - http://m.vk[.]com/id674309800?act=info
  - http://m.vk[.]com/id674310752?act=info
  - http://m.vk[.]com/id730148259?act=info
  - http://m.vk[.]com/id730149630?act=info
  - http://m.vk[.]com/id761343811?act=info
  - http://m.vk[.]com/id761345428?act=info
  - http://m.vk[.]com/id761346006?act=info
  - https://www.youtube[.]com/channel/UCP5sKzxDLR5yhO1IB4EqeEg/about
  - https://docs.google[.]com/document/d/1s0n64k12_r9MglT5m9lr63M5F3e-xRyaMeYP7rdOTrA/mobilebasic
  - https://docs.google[.]com/document/d/1IIB6hhf_BB1DaxzC1aNfLEG1K97LsPsN55AT5pFWYKo/mobilebasic

- C&C:
  - 91.204.227[.]32
  - 91.204.227[.]33
  - 92.204.255[.]173
  - 91.204.227[.]39
  - 118.160.36[.]14
  - 198.144.149[.]131
