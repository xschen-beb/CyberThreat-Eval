# Rilide A New Malicious Browser Extension for Stealing Cryptocurrencies

**Incident:** Rilide: A New Malicious Browser Extension for Stealing Cryptocurrencies

**Root cause:** Malicious browser extension disguised as a legitimate Google Drive extension.

**Impact:** The exact number of impacted devices and financial losses are not specified in the document. However, the malware's ability to steal cryptocurrencies suggests significant potential financial damage to individuals using infected browsers.

**Mitigation:** 
- **User Education:** Inform users about the risks of downloading and enabling unverified browser extensions.
- **Browser Security Configurations:**
  - Enforce strict extension policies to allow only trusted and verified extensions.
  - Regularly update browsers to ensure security patches are applied.
  - Implement browser settings to disable the execution of untrusted extensions.
- **Anti-Malware Solutions:**
  - Utilize anti-malware solutions capable of detecting and removing malicious extensions.
  - Regularly scan systems for malware and remove detected threats.
- **Monitoring and Response:**
  - Monitor network traffic for suspicious activities related to cryptocurrency exchanges.
  - Set up alerts for unusual login attempts or transactions in cryptocurrency accounts.
  
**Detection Signature:**
- **Service:** Web browser (Google Chrome, Microsoft Edge, Brave, Opera)
- **Port:** N/A (browser extension, not a network service)
- **Severity:** Critical
- **Incident:** Rilide browser extension malware
- **Signature name:** "Rilide browser extension detected"
- **Internal checks:**
  - **Setting1:** Verify installed browser extensions and match against a list of known malicious extensions.
  - **Setting2:** Check browser configurations for unauthorized modifications (e.g., injected scripts, altered shortcuts).
  - **Setting3:** Ensure browser security policies are enforced (e.g., disallow unverified extensions).
- **External scanning:**
  - **Browser extension scanning:** Identify and report malicious browser extensions.
  - **Network traffic analysis:** Monitor for communication with known C2 domains associated with Rilide.

**IoCs:**
- **Hashes:**
  - Publisher File: 
    - SHA256: 0e31ff6406b03982581246b7dd60f3b96edcf0bd007b31766954df001fd68f69
  - Aurora Stealer:
    - SHA256: e623984143e0dc6e35c79869ab1521c6714e588e8e648606496f8372ca0d8416
  - Rilide Loader:
    - SHA256: 0f11aeecbde1f355d26c9d406dad80cb0ae8536aea31fdddaf915d4afd434f3f
  - Rilide Extension (various files):
    - SHA256: 4cc83be0fa496855d244050616ee2e86b044a9bc87bc5ca70b305986c1ba3bb8
    - SHA256: 55251c725e9f6f51b8db7a631b54dd85b1b59d644c3219e03ceffb0c49cd00a4
    - SHA256: 1b01c3e554700e1282c7fdd2dcb54314516ee1f0c5eef3560cdbabc1ba776293
    - SHA256: a28c623d120a76dcfeef9504eaeefabac9d33f292576ccf012fa458b8d7bc6ef
    - SHA256: 8989f4244667626728c6c0083422ff714cb622c92c35a53f9cb1e9891f4528ff
    - SHA256: 170a13a7a8757336babe857804fa24b6cb20aaa9593b32546d7151f23095a510
    - SHA256: bb57a504e0b821552344cecb3da9ecdd0d61817264617a4917d6f5e64a1df7e5
    - SHA256: d70e933e10e667ae7ef6e68a625c447be8aabe9b29affdad999c969bd8769003
    - SHA256: c8939f8a7d77022bcc708c354140319718777ca35efdfb76d6c80cb9de8c8091e
    - SHA256: 2e310391d77022bcc708c354140319718777ca35efdfb76d6c80cb9de8c8091e
    - SHA256: 4bbb0584eed0c082b5c43d3f259f37cf1a0b64eabb485e85090951a6566d98d4
    - SHA256: 9dca66f52f31dca921fb238bd36bfc1b1a59d3e4af7b071da9bc4c6bf294e402
    - SHA256: 4df0f18a7e05518bbe93758e751f1f462fef212cdc786c7217d50ddbda14efb5
    - SHA256: ef20c929f5204b223b6e53dc406ea0bcd76d9e98c9ae4942037902883d4bb22a
    - SHA256: e1ad66cc0244fc075e0aabe0fd19502d4c9617829b90aa210e74be1d915275d2
    - SHA256: a7f0fdfdfdf1ef65799fd2114bf5c1e133a8b7635b498b334553fbb64b218a05
    - SHA256: 68278b40b59b1b0db2f814d2d864f0b9c2b4285f5795d22cabf60715f922989c
    - SHA256: 2f947644c7752ba014eae7971b247be60249a6088923c66ffe9886a7f5c5fe1c
- **Domains:**
  - nch-software[.]info
  - 45[.]15[.]156[.]210
  - vceilinichego[.]ru
  - ashgrrwt[.]click
  - nvidia-graphics[.]top
- **Cryptocurrency Addresses:**
  - BTC: bc1qkczacyp5jq29s5kaphth4asu8cv2y4u4gdgj7q
  - BTC: bc1qsjg8dqx6ga30h6szjd8dv2wg50ch50qrey4t7j
  - BTC: 1KqequymujeNJuyB4gH7oJSFTB3En3Hf5n
  - ETH: 0xDBc1330056E2F5e2FB11FB3C96dE2c44B313eA8d
  - LTC: LRYpzmnqBVozkbzJhTWndzYDPfjmNPyaLv
  - XRP: rUPTadzFN6LS662Z2d2AvNyqU1xwg2japJ
  - TRON: THiD8hFLiEyULVKLp3DSbBXQSbR3MQxm4X
  - DOGE: D5asYfjtbTtFmFkrEwqVgbJKYv9YT7Tgjh

**No IoCs found:** N/A (IoCs are provided above).
