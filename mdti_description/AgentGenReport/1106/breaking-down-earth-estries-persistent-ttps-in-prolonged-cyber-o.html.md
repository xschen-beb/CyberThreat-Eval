Source: [https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-o.html](https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-o.html)

## Related articles (describing the same threat) 
- https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-o.html
- https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations/iocs-breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations.txt
- https://www.darkreading.com/cyberattacks-data-breaches/-apt-attacks-from-earth-estries-hit-govt-tech-with-custom-malware
- https://www.infosecurity-magazine.com/news/cyber-espionage-group-earth/
- https://candid.technology/earth-estries-targets-exchange-servers-network-tools-in-a-new-campaign/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: Earth Estries Cyber Operations 

#### Root cause 
 Exploitation of vulnerabilities in systems such as Microsoft Exchange servers and network adapter management tools (e.g., QConvergeConsole). 

#### Threat actor/group/campaign 
 Earth Estries (aka Salt Typhoon) 

#### Organization/industry/location 
 Governments and technology industries (targeted organizations) 

#### Start date – End date 
 Ongoing since at least 2020 

#### MITRE TTPs 
 - Initial Access: Exploiting Vulnerabilities (T1190), Valid Accounts (T1078)
- Execution: Command and Scripting Interpreter (T1059), Windows Management Instrumentation (T1047)
- Persistence: Create or Modify System Process (T1543), Boot or Logon Autostart Execution (T1547)
- Privilege Escalation: Abuse Elevation Control Mechanism (T1548)
- Defense Evasion: Obfuscated Files or Information (T1027), Deobfuscate/Decode Files or Information (T1140)
- Credential Access: Credential Dumping (T1003)
- Discovery: System Network Connections Discovery (T1049), System Information Discovery (T1082)
- Lateral Movement: Remote Services (T1021)
- Collection: Data from Local System (T1005)
- Exfiltration: Exfiltration Over C2 Channel (T1041)
- Command and Control: Application Layer Protocol (T1071) 

#### Impact 
 Compromised networks and systems, exfiltration of sensitive data including credentials and documents. 

#### Mitigation Steps 
 1. Secure external-facing services, especially email servers and web applications.
2. Patch known vulnerabilities promptly.
3. Implement robust credential management practices, including multifactor authentication.
4. Monitor network traffic for unusual activities.
5. Employ endpoint protection solutions to detect and block malware.
6. Conduct regular security assessments and audits. 

#### Detection Signature 
 Service: Microsoft Exchange, QConvergeConsole
Port: 443 (HTTPS), 8080 (HTTP for QConvergeConsole)
Severity: Critical
Incident: Earth Estries Attack
Signature name: “Microsoft Exchange Exploit”
Internal checks:
- Setting1: Microsoft Exchange servers should be up-to-date with security patches.
- Setting2: QConvergeConsole installations should be verified for configuration vulnerabilities.
- Setting3: Implement multifactor authentication for remote access.
External scanning:
- Detect open ports (443, 8080)
- Scan for known vulnerabilities in Microsoft Exchange and QConvergeConsole 

#### IoCs: 
- url: http://96.44.160.181/VXTR.txt ([link](https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-o.html)) 

- url: http://mail.ocac.org.pk/UNBCL.docx ([link](same as above)) 

- url: http://mail.ocac.org.pk/Portscan.docx ([link](same as above)) 

- url: http://mail.ocac.org.pk/SetupPlatform.docx ([link](same as above)) 

- url: http://mail.ocac.org.pk/UNBCL.docx ([link](same as above)) 

- url: https://api.anonfiles.com/upload ([link](same as above)) 

- url: https://file.io ([link](same as above)) 

- url: https://api.anonfiles.com/upload ([link](same as above)) 

- hash_md5: 11736212 ([link](same as above)) 

- hash_md5: 11736213 ([link](same as above)) 

- hash_sha256: 42d4eb7f04111631891379c5cce55480d2d9d2ef8feaf1075e1aed0c52df4bb9 ([link](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations/iocs-breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-operations.txt)) 

- hash_sha256: 95062728536f23b1335756ae1a1d68f1df22d58594ece9998cae6b73772fd49f ([link](same as above)) 

- hash_sha256: 6a4de5c7787e212dea5f033f8f7cd39aefc93e7c83c8564dc2204813e8e76ff2 ([link](same as above)) 

- hash_sha256: 27042218e8d1a0491525b35a6dc2fc0737841bcaed65b751e78769eadeda9751 ([link](same as above)) 

- hash_sha256: c32156a7de42a61f5d584e82dfbced690d23fd72080024c14a9143e5f20f0ad8 ([link](same as above)) 

- hash_sha256: a298031b1c28f11f00d3b9f6311fbfae881d6c789e70c4bc5e6ccdf8165b94c6 ([link](same as above)) 

- hash_sha256: cdde7878ed0529f9ef3ad58aa3084f1df6e2fb371807b15539187539b060fed2 ([link](same as above)) 

- hash_sha256: 6f274955b1fb58cc9a60476bc5a9cd9d54c962cc29e73db41b7786148cb74505 ([link](same as above)) 

- hash_sha256: 09abc579097b0bd8d115702bb1eeb546d2401373c83385a52386ad4243f945e8 ([link](same as above)) 

- hash_sha256: 292f70bff5717608c289f4146febcc06a2c5d8192529a8c51e18ec0f7b44d1cf ([link](same as above)) 

- hash_sha256: cd8630f8e07e16203195f563457a84beb08112fcbb4d9ee1056a788174cf8f6b ([link](same as above)) 

- hash_sha256: 98ddf03ca6ade4770cc06ac8034b3468bd94094f5813d28b74885e5ca6958895 ([link](same as above)) 

- hash_sha256: 03365cce37db511fdfaf8d77a14f806a2d822a111aa8cc032b5b341c0b0064a5 ([link](same as above)) 

- hash_sha256: 1378bde3aee0057ca2a5854fee4d184479491ec624a3bbf215098afaa6b82299 ([link](same as above)) 

- hash_sha256: b17660d1a4c0258739024187497be0b11530791d1307d9e5556f04f0ac58d42f ([link](same as above)) 

- hash_sha256: b450311b5fc4333b26955f7c709ca61fcfdba168f1a8839a93979a892a8c22cc ([link](same as above)) 

- hash_sha256: 39f1c7095e1db05944eeda08a2e1c1b8c513ea581bfc0cb36ad106e3a8f38b5f ([link](same as above)) 

- hash_sha256: 0c8c0b2837fbb9c15da1bfb904ed3f3903e2d4d49c999394068f274b014a09dd ([link](same as above)) 

- hash_sha256: a113c637bb81f9bbd39731672b242a8da5915ef4b5e93d72cc9a7454b5e120bd ([link](same as above)) 

- hash_sha256: 4aeaa0d954268d4fc7179ec7578258c3459ee95b82698363e0cafb700c05181a ([link](same as above)) 

- hash_sha256: d0575b3ced944dc627d047c60f23d25bd3aa0c4deab69f784b9a80aae50fbd7b ([link](same as above)) 

- hash_sha256: 25b9fdef3061c7dfea744830774ca0e289dba7c14be85f0d4695d382763b409b ([link](same as above)) 

- hash_sha256: 6d64643c044fe534dbb2c1158409138fcded757e550c6f79eada15e69a7865bc ([link](same as above)) 

- ip: 103.159.133.209 ([link](same as above)) 

- ip: 45.192.178.208 ([link](same as above)) 

- ip: 38.54.71.140 ([link](same as above)) 

- ip: 103.159.133.205 ([link](same as above)) 

- ip: 103.103.131.40 ([link](same as above)) 

- ip: 103.15.28.228 ([link](same as above)) 

- ip: 154.220.3.17 ([link](same as above)) 

- ip: 156.255.2.202 ([link](same as above)) 

- ip: 103.103.128.121 ([link](same as above)) 

- ip: 162.19.135.182 ([link](same as above)) 

- domain: cdglobalclouds.com ([link](same as above)) 

- domain: broadmediacloud.com ([link](same as above)) 

- domain: zmail.broadmediacloud.com ([link](same as above)) 

- domain: www.nodtecloud.com ([link](same as above)) 

- domain: mail2-0da8aa1c.oxcdntech.com ([link](same as above)) 

- domain: helpdesk.athenatechlabs.com ([link](same as above)) 

- domain: supports.flarecastdns.com ([link](same as above)) 

- domain: ns.starkaero.com ([link](same as above)) 

- domain: pay.johannesburghotel.net ([link](same as above)) 

- domain: kidshomeworkabc.global.ssl.fastly.net ([link](same as above)) 

- domain: ap.missmichiko.com ([link](same as above)) 

- domain: portal.sppokemon.com ([link](same as above)) 

- domain: svn.truecdnnetwork.com ([link](same as above)) 

- domain: lync.realtxholdem.com ([link](same as above)) 

- domain: globalnetzone.b-cdn.net ([link](same as above)) 

- domain: amazoncdns.com ([link](same as above)) 

- domain: www.euphemismscase.site ([link](same as above)) 

- domain: www.dbacloudsupport.com ([link](same as above)) 

- domain: www.cloudshappen.com ([link](same as above)) 

- domain: www.amazoncdns.com ([link](same as above)) 

- domain: supports.dbacloudsupport.com ([link](same as above)) 

- domain: ssl3.awsdns-531.com ([link](same as above)) 

- domain: soffice.offices-analytics.com ([link](same as above)) 

- domain: services.offices-analytics.com ([link](same as above)) 

- domain: resource.offices-analytics.com ([link](same as above)) 

- domain: redsquare.redcrossco.com ([link](same as above)) 

- domain: portal.techmersion.com ([link](same as above)) 

- domain: portal.cdglobalclouds.com ([link](same as above)) 

- domain: opengl.cloudshappen.com ([link](same as above)) 

- domain: ns108.cloudshappen.com ([link](same as above)) 

- domain: ns101.awsdns-531.com ([link](same as above)) 

- domain: ms119.newsfreecloud.com ([link](same as above)) 

- domain: ms101.cloudshappen.com ([link](same as above)) 

- domain: mail.euphemismscase.site ([link](same as above)) 

- domain: llnw-dd.awsdns-531.com ([link](same as above)) 

- domain: images.dbacloudsupport.com ([link](same as above)) 

- domain: helpdesk.cloudshappen.com ([link](same as above)) 

- domain: helpdesk.athenatechlabs.com ([link](same as above)) 

- domain: global.techmersion.com ([link](same as above)) 

- domain: ge.huseinhbz.click ([link](same as above)) 

- domain: ftp.techmersion.com ([link](same as above)) 

- domain: euphemismscase.site ([link](same as above)) 

- domain: emv1.techmersion.com ([link](same as above)) 

- domain: emv1.cdglobalclouds.com ([link](same as above)) 

- domain: de.huseinhbz.click ([link](same as above)) 

- domain: credits.offices-analytics.com ([link](same as above)) 

- domain: cloudsrv.cloudfrontsrv.com ([link](same as above)) 

- domain: cdn181.awsdns-531.com ([link](same as above)) 

- domain: cdn101.cloudflaresrv.com ([link](same as above)) 

- domain: cdglobalclouds.com ([link](same as above)) 

- domain: cas04.awsdns-531.com ([link](same as above)) 

- domain: cachecloud.cloudflaresrv.com ([link](same as above)) 

- domain: cache10.newsfreecloud.com ([link](same as above)) 

- domain: c11r.awsdns-531.com ([link](same as above)) 

- domain: blog.techmersion.com ([link](same as above)) 

- domain: auth.boxlibraries.com ([link](same as above)) 

- For more IoCs, please refer to the above links. 


