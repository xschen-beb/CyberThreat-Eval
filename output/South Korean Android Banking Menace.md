# South Korean Android Banking Menace

Incident: South Korean Android Banking Menace – FakeCalls

Root cause: Deployment of sophisticated Android malware leveraging anti-analysis techniques and command-and-control (C&C) server disguise mechanisms.

Impact: 170,000 individuals impacted with financial losses amounting to approximately 600 million USD (from 2016 to 2020).

Mitigation: Implement robust mobile security measures, educate users on identifying phishing attempts, and collaborate with financial institutions to develop better fraud detection systems.

**Detailed Steps for Mitigation:**

1. **Enhanced Mobile Security:**
   - Deploy mobile security solutions such as Check Point’s Harmony Mobile which provides real-time detection and blocking of malicious apps.
   - Ensure mobile security solutions include advanced network protection to mitigate threats from C&C servers.

2. **User Education:**
   - Conduct awareness campaigns to educate users about the risks of phishing attacks and how to identify suspicious activities.
   - Encourage users to download apps only from trusted sources like the official app stores.

3. **Financial Institution Collaboration:**
   - Work with financial institutions to develop advanced fraud detection systems that can identify and mitigate phishing attempts.
   - Implement stronger authentication mechanisms like two-factor authentication (2FA) to protect user accounts.

4. **Regular Security Audits:**
   - Perform regular security audits and penetration testing on mobile applications to identify and fix vulnerabilities.
   - Ensure that mobile apps are compliant with security best practices and standards.

5. **Monitor and Block C&C Servers:**
   - Continuously monitor network traffic for connections to known C&C servers and block them using firewalls and intrusion detection systems (IDS).
   - Use threat intelligence services to stay updated on new C&C server domains and IP addresses.

Detection Signature:
   Service: Android Malware
   Port: Not applicable (uses mobile network)
   Severity: Critical
   Incident: South Korean Android Banking Menace – FakeCalls
   Signature name: “FakeCalls Malware Detection”
   Internal checks:
      - Setting1: Ensure mobile security solutions are deployed and up-to-date.
      - Setting2: Monitor for installation of apps from untrusted sources.
      - Setting3: Validate that anti-fraud mechanisms are active and functioning in financial apps.
   External scanning:
      - Monitor for network communications with known C&C server IPs (listed in IoCs).
      - Analyze mobile traffic for patterns indicative of FakeCalls malware behavior.

IoCs:
   **Hashes:**
   - 0e26be5dbdc3656b09cc6d7d231b2285a7e52a4dc42c63021b57ee40b9694f34
   - 2b003f6638b56a56bc4f59058fc5b8e0ca6f34b79b83145fe9d80a5653ee2c85
   - 2fc09a2a0426e1fca7d9675c2f1734e36b3a13c260044ee70a7893419ab1bbe2
   - 3038c7a9c170e974421c5389ecb24f1e27ff9ba178e6f7f4929e5c54cac0c658
   - 39c7f217e55809b762b998198f6ae1e30ed87f0838f8e01e3fd838a77831bd3d
   - 497b9561e84e5bab365fd5283d45f6c76555e89c0b0dc57a91b338bf30ab1a54
   - 49c460158f23d12200488612242d2b8f50fdad38d5edb006e8c3a90b8005172c
   - 4a422047bc0a2ca692b33a80740ab64a5bbc325c348d3d4eea0f304d3c256e03
   - 522b4b565f34309713497d5fa2bfb6aa403cf7547c1ba2c114fc59fa8252b472
   - 65e875b1eed232e462cb654b110a895e2c87d420c9ef21a53683e27bcbcfbcc6
   - 76b94289ad36015d91e26ef1298fc04ca6f7ad7be1fe2d07ecf8a12be20996f3
   - 7d55250d76fcc3006a7cb727ba7521e0f17f8fd9311cf799442b1a737702a028
   - 834e678c8bb755d6bd21a886a39fea19613fd80a3894e4d6ddff3652170a0464
   - 97d20d26826a83de014b6711b87f18a98464e07b6ebc3a0480e4007d2f47e603
   - b7ee5e7a4b9937e5fd9eebed01eabc36b22c8c6931e63f934bbdb961346169b3
   - cbcffbf761b644f20486f7164a3b97a7c083dfcd774ed0ebbbcd6109fd6c47e1
   - cc4dc5afeb91ef2ad364cda511777b888a4ba9a90ae49e9181494b2ff32d50ed
   - db9d55a7b05253fd7367c5fa25d07d6962c1a9b58a136f76c7ef236ad2aec94b
   - de743563f41553f47bb7073ac28ed4d79e1a4031b3da732497805aa8a297943f
   - f8823780d2822307e995528bd7a34a1735e66bd2fe22404e02053cb92b0a56cb

   **URLs:**
   - https://drive.google.com/file/d/1L7CMBiv5NLIrCxmUpkXRZcyFqbgmcKy5/view?usp=sharing
   - https://drive.google.com/file/d/1HZg40qw7DGgl2HT6ZuGkKLkf5a0DnaBT/view?usp=share_link
   - https://www.daebak222.com/huhu/admin.txt
   - https://182.16.42.18:5055/huhu/admin.txt
   - http://182.16.42.18:10102/Teamviewer/admin.txt
   - http://182.16.42.18:10102/HanaBank/admin/admin.txt
   - http://182.16.42.18:10102/HanaBank/admin.txt
   - http://192.168.99.186:5000/admin.txt
   - http://192.168.99.33:5055/admin.txt
   - http://192.168.99.191:5055/admin.txt
