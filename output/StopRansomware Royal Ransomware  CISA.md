Source: [https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a)

# StopRansomware Royal Ransomware  CISA

### Incident: Royal Ransomware Attack

**Root cause:** Phishing emails leading to malware installation.

**Impact:** Over 350 known victims worldwide, with ransomware demands exceeding $275 million USD.

**Mitigation:** Implement comprehensive security measures including multifactor authentication, regular software updates, and network segmentation. Detailed steps include:

1. **Implement a recovery plan:**
   - Maintain multiple copies of sensitive data in secure locations.
   - Regularly verify the integrity of backups.

2. **Enforce strong password policies:**
   - Require passwords of at least 8 characters.
   - Use industry-recognized password managers.
   - Implement multi-factor authentication.

3. **Regularly update all software and systems:**
   - Apply patches for known vulnerabilities promptly.

4. **Segmentation of networks:**
   - Control traffic and restrict adversary lateral movement.

5. **Monitor and detect abnormal activity:**
   - Use network monitoring tools to log and report all network traffic, including lateral movements.

6. **Apply least privilege principle:**
   - Audit user accounts with administrative privileges.
   - Disable unused ports and services.

7. **Disable command-line and scripting activities:**
   - Prevent threat actors from running utilities that allow privilege escalation or lateral movement.

8. **Maintain offline backups:**
   - Ensure backups are encrypted and immutable.

**Detection Signature:**

- **Service:** Remote Desktop Protocol (RDP)
- **Port:** 3389
- **Severity:** Critical
- **Incident:** Royal Ransomware 
- **Signature name:** “RDP publicly accessible”
- **Internal checks:**
  - **Setting1:** RDP port (3389) should not be exposed on external Internet. – In platform
  - **Setting2:** RDP port (3389) should not listen on the external Internet – Inside VMs
  - **Setting3:** RDP access should be secured with multi-factor authentication. – Inside VMs
- **External scanning:**
  - Port (3389) open
  - RDP no-pass-login

**IoCs:**

- **IPs:**
  - 102.157.44[.]105
  - 105.158.118[.]241
  - 105.69.155[.]85
  - 113.169.187[.]159
  - 134.35.9[.]209
  - 139.195.43[.]166
  - 139.60.161[.]213
  - 148.213.109[.]165
  - 163.182.177[.]80
  - 181.141.3[.]126
  - 181.164.194[.]228
  - 185.143.223[.]69
  - 186.64.67[.]6
  - 186.86.212[.]138
  - 190.193.180[.]228
  - 196.70.77[.]11
  - 197.11.134[.]255
  - 197.158.89[.]85
  - 197.204.247[.]7
  - 197.207.181[.]147
  - 197.207.218[.]27
  - 197.94.67[.]207
  - 23.111.114[.]52
  - 41.100.55[.]97
  - 41.107.77[.]67
  - 41.109.11[.]80
  - 41.251.121[.]35
  - 41.97.65[.]51
  - 42.189.12[.]36
  - 45.227.251[.]167
  - 5.44.42[.]20
  - 61.166.221[.]46
  - 68.83.169[.]91
  - 81.184.181[.]215
  - 82.12.196[.]197
  - 98.143.70[.]147
  - 140.82.48[.]158
  - 147.135.36[.]162
  - 147.135.11[.]223
  - 152.89.247[.]50
  - 172.64.80[.]1
  - 179.43.167[.]10
  - 185.7.214[.]218
  - 193.149.176[.]157
  - 193.235.146[.]104
  - 209.141.36[.]116
  - 45.61.136[.]47
  - 45.8.158[.]104
  - 5.181.234[.]58
  - 5.188.86[.]195
  - 77.73.133[.]84
  - 89.108.65[.]136
  - 94.232.41[.]105
  - 47.87.229[.]39

- **Domains:**
  - sombrat[.]com
  - gororama[.]com
  - softeruplive[.]com
  - altocloudzone[.]live
  - ciborkumari[.]xyz
  - myappearinc[.]com
  - parkerpublic[.]com
  - pastebin.mozilla[.]org/Z54Vudf9/raw
  - tumbleproperty[.]com
  - myappearinc[.]com/acquire/draft/c7lh0s5jv

- **Hashes:**
  - 8A983042278BC5897DBCDD54D1D7E3143F8B7EAD553B5A4713E30DEFFDA16375
  - 8a99353662ccae117d2bb22efd8c43d7169060450be413af763e8ad7522d2451
  - be030e685536eb38ba1fec1c90e90a4165f6641c8dc39291db1d23f4ee9fa0b1
  - B8C4AEC31C134ADBDBE8AAD65D2BCB21CFE62D299696A23ADD9AA1DE082C6E20
  - 4a9dde3979c2343c024c6eeeddff7639be301826dd637c006074e04a1e4e9fe7
  - 4cd00234b18e04dcd745cc81bb928c8451f6601affb5fa45f20bb11bfb5383ce
  - 08c6e20b1785d4ec4e3f9956931d992377963580b4b2c6579fd9930e08882b1c
  - f8cff7082a936912baf2124d42ed82403c75c87cb160553a7df862f8d81809ee
  - d47d4b52e75e8cf3b11ea171163a66c06d1792227c1cf7ca49d7df60804a1681
  - 216047C048BF1DCBF031CF24BD5E0F263994A5DF60B23089E393033D17257CB5
  - 19896A23D7B054625C2F6B1EE1551A0DA68AD25CDDBB24510A3B74578418E618
  - 585b05b290d241a249af93b1896a9474128da969
  - 41a79f83f8b00ac7a9dd06e1e225d64d95d29b1d
  - a84ed0f3c46b01d66510ccc9b1fc1e07af005c60
  - c96154690f60a8e1f2271242e458029014ffe30a
  - 65dc04f3f75deb3b287cca3138d9d0ec36b8bea0
  - 82f1f72f4b1bfd7cc8afbe6d170686b1066049bc7e5863b51aa15ccc5c841f58
  - 74d81ef0be02899a177d7ff6374d699b634c70275b3292dbc67e577b5f6a3f3c
  - 342B398647073159DFA8A7D36510171F731B760089A546E96FBB8A292791EFEE
