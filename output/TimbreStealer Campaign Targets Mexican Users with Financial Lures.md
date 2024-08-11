Source: [https://blog.talosintelligence.com/timbrestealer-campaign-targets-mexican-users/](https://blog.talosintelligence.com/timbrestealer-campaign-targets-mexican-users/)

# TimbreStealer Campaign Targets Mexican Users with Financial Lures

Incident: TimbreStealer Campaign

Root Cause: Phishing emails leading to the download and execution of the TimbreStealer malware.

Impact: The campaign targets users in Mexico, specifically luring them with tax-related themes. The exact number of devices and people impacted is not specified, but multiple IP addresses, domains, and malware samples indicate a potentially wide-reaching impact.

Mitigation: 
1. **Enhance Email Security:** Implement advanced email filtering solutions to detect and block phishing emails.
2. **User Awareness Training:** Conduct regular training sessions to educate users about phishing attacks and how to recognize them.
3. **Endpoint Protection:** Deploy endpoint security solutions that include anti-malware, anti-phishing, and behavior analysis features.
4. **Network Segmentation:** Segment the network to limit the spread of malware if a device is compromised.
5. **Regular Updates and Patch Management:** Ensure that all systems and applications are regularly updated and patched to prevent exploitation of known vulnerabilities.
6. **Multi-Factor Authentication (MFA):** Implement MFA to add an additional layer of security for user authentication.
7. **Incident Response Plan:** Develop and regularly update an incident response plan to quickly react to security incidents.

Detection Signature:
- **Service:** WebDAV (used as a vector for downloading malware)
- **Port:** 80 (HTTP), 443 (HTTPS)
- **Severity:** Critical
- **Incident:** TimbreStealer Campaign
- **Signature name:** “WebDAV phishing download”
- **Internal checks:**
  - **Setting1:** WebDAV service should be monitored for unusual activity – In platform
  - **Setting2:** Ensure WebDAV is not used for unauthorized file downloads – Inside VMs
  - **Setting3:** WebDAV service should operate under strict authentication – Inside VMs
- **External scanning:**
  - Port (80, 443) open
  - Unusual WebDAV download activity

IoCs:
- **IPs:**
  - 24[.]199[.]98[.]128
  - 159[.]89[.]50[.]225
  - 104[.]131[.]169[.]252
  - 104[.]131[.]67[.]109
  - 137[.]184[.]108[.]251
  - 137[.]184[.]115[.]230
  - 138[.]197[.]34[.]162
  - 142[.]93[.]50[.]216
  - 143[.]244[.]144[.]166
  - 143[.]244[.]160[.]115
  - 146[.]190[.]208[.]30
  - 157[.]230[.]238[.]116
  - 157[.]245[.]8[.]79
  - 159[.]223[.]96[.]160
  - 159[.]89[.]226[.]127
  - 159[.]89[.]90[.]109
  - 162[.]243[.]171[.]207
  - 167[.]71[.]24[.]13
  - 167[.]71[.]245[.]175
  - 167[.]71[.]246[.]120
  - 192[.]241[.]141[.]137
  - 24[.]144[.]96[.]15
  - 5[.]55[.]65[.]159
  - 64[.]225[.]29[.]249

- **Domains:**
  - trilivok[.]com
  - chidoriland[.]com
  - manderlyx[.]com
  - bailandolambada[.]com
  - 0[.]solucionegos[.]top
  - auditoria38[.]meinastrohoroskop[.]com
  - auditoria42[.]altavista100[.]com
  - auditoria67[.]mariageorgina[.]com
  - auditoria7[.]miramantolama[.]com
  - auditoria82[.]taoshome4sale[.]com
  - auditoria84[.]meinastrohoroskop[.]com
  - auditoria88[.]mariageorgina[.]com
  - auditoria89[.]venagard[.]com
  - auditoria92[.]venagard[.]com
  - auditoria93[.]serragrandreunion[.]com
  - comprobante14[.]miramantolama[.]com
  - comprobante2[.]marcialledo[.]com
  - comprobante27[.]mariageorgina[.]com
  - comprobante27[.]serragrandreunion[.]com
  - comprobante27[.]servicioslocomer[.]online
  - comprobante45[.]altavista100[.]com
  - comprobante51[.]meinastrohoroskop[.]com
  - comprobante63[.]serragrandreunion[.]com
  - comprobante68[.]portafoliocfdi[.]com
  - comprobante70[.]miramantolama[.]com
  - comprobante75[.]meinastrohoroskop[.]com
  - comprobante80[.]serragrandreunion[.]com
  - comprobante91[.]servicioslocomer[.]online
  - comprobante93[.]venagard[.]com
  - cumplimiento19[.]altavista100[.]com
  - cumplimiento35[.]solucionegos[.]top
  - cumplimiento39[.]meinastrohoroskop[.]com
  - cumplimiento43[.]commerxion[.]buzz
  - cumplimiento47[.]solucionegos[.]top
  - cumplimiento48[.]callarlene[.]net
  - cumplimiento56[.]timbradoelectronico[.]com
  - cumplimiento72[.]serragrandreunion[.]com
  - cumplimiento81[.]paulfenelon[.]com
  - cumplimiento91[.]miramantolama[.]com
  - cumplimiento94[.]meinastrohoroskop[.]com
  - cumplimiento98[.]serragrandreunion[.]com
  - factura10[.]miramantolama[.]com
  - factura20[.]facturascorporativas[.]com
  - factura20[.]solunline[.]top
  - factura34[.]changjiangys[.]net
  - factura4[.]servicioslocomer[.]online
  - factura40[.]miramantolama[.]com
  - factura44[.]servicioslocales[.]online
  - factura46[.]facturasfiel[.]com
  - factura49[.]marcialledo[.]com
  - factura50[.]callarlene[.]net
  - factura59[.]altavista100[.]com
  - factura7[.]taoshome4sale[.]com
  - factura71[.]servicioslomex[.]online
  - factura72[.]serragrandreunion[.]com
  - factura73[.]mariageorgina[.]com
  - factura81[.]altavista100[.]com
  - factura90[.]changjiangys[.]net
  - factura91[.]servicioslocomer[.]online
  - folio24[.]serragrandreunion[.]com
  - folio24[.]spacefordailyrituals[.]com
  - folio47[.]marcialledo[.]com
  - folio53[.]mariageorgina[.]com
  - folio60[.]callarlene[.]net
  - folio75[.]taoshome4sale[.]com
  - folio75[.]venagard[.]com
  - folio76[.]miramantolama[.]com
  - folio83[.]altavista100[.]com
  - folio89[.]changjiangys[.]net
  - folio90[.]servicioslocomer[.]online
  - folio99[.]solunline[.]top
  - pdf21[.]changjiangys[.]net
  - pdf33[.]venagard[.]com
  - pdf34[.]solucionpiens[.]top
  - pdf39[.]facturasonlinemx[.]com
  - pdf43[.]marcialledo[.]com
  - pdf49[.]marcialledo[.]com
  - pdf50[.]changjiangys[.]net
  - pdf57[.]visual8298[.]top
  - pdf59[.]venagard[.]com
  - pdf63[.]paulfenelon[.]com
  - pdf65[.]verificatutramite[.]com
  - pdf70[.]mariageorgina[.]com
  - pdf81[.]photographyride[.]com
  - pdf85[.]miramantolama[.]com
  - pdf93[.]venagard[.]com
  - pdf98[.]solunline[.]top
  - portal27[.]marcialledo[.]com
  - portal34[.]solunline[.]top
  - portal48[.]solucionpiens[.]top
  - portal50[.]solucionegos[.]top
  - portal55[.]solucionegos[.]top
  - portal63[.]paulfenelon[.]com
  - portal70[.]solunline[.]top
  - portal80[.]changjiangys[.]net
  - portal86[.]serragrandreunion[.]com
  - portal90[.]meinastrohoroskop[.]com
  - portal92[.]solucionpiens[.]top
  - suscripcion0[.]venagard[.]com
  - suscripcion10[.]solunline[.]xyz
  - suscripcion24[.]facturasonlinemx[.]com
  - suscripcion24[.]venagard[.]com
  - suscripcion32[.]servicioslocomer[.]online
  - suscripcion38[.]eagleservice[.]buzz
  - suscripcion38[.]mariageorgina[.]com
  - suscripcion57[.]changjiangys[.]net
  - suscripcion65[.]g1ooseradas[.]buzz
  - suscripcion84[.]taoshome4sale[.]com
  - suscripcion95[.]servicioslomex[.]online
  - timbrado0[.]meinastrohoroskop[.]com
  - timbrado11[.]verificatutramite[.]com
  - timbrado16[.]taoshome4sale[.]com
  - timbrado17[.]marcialledo[.]com
  - timbrado17[.]mariageorgina[.]com
  - timbrado2[.]serviciosna[.]top
  - timbrado2[.]solucionegos[.]top
  - timbrado33[.]meinastrohoroskop[.]com
  - timbrado42[.]mariageorgina[.]com
  - timbrado54[.]changjiangys[.]net
  - timbrado6[.]meinastrohoroskop[.]com
  - timbrado73[.]mariageorgina[.]com
  - timbrado74[.]callarlene[.]net
  - timbrado74[.]mexicofacturacion[.]com
  - timbrado80[.]paulfenelon[.]com
  - timbrado84[.]miramantolama[.]com
  - timbrado90[.]porcesososo[.]online
  - timbrado96[.]paulfenelon[.]com
  - validacion22[.]hb56[.]cc

**Hashes:**
- 600d085638335542de1c06a012ec9d4c56ffe0373a5f61667158fc63894dde9f (Downloader)
- 883674fa4c562f04685a2b733747e4070fe927e1db1443f9073f31dd0cb5e215 (Region check and redirect)
- b1b85c821a7f3b5753becbbfa19d2e80e7dcbd5290d6d831fb07e91a21bdeaa7 CFDI_930209.zip
- e04cee863791c26a275e0c06620ea7403c736f8cafbdda3417f854ae5d81a49f FACTURA_560208.zip
- aa187a53e55396238e97638032424d68ba2402259f2b308c9911777712b526af FAC_560208_ATR890126GK2.url
- 66af21ef63234c092441ec33351df0f829f08a2f48151557eb7a084c6275b791 FAC_930209_FME140910KI4.url
