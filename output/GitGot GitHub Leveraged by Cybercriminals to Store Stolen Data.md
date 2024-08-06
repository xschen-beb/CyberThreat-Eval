# GitGot GitHub Leveraged by Cybercriminals to Store Stolen Data

Incident: GitGot: GitHub leveraged by cybercriminals to store stolen data

Root cause: Malicious npm packages warbeast2000 and kodiak2k

Impact: Approximately 1,350 downloads across both packages. Devices and people impacted include developers who downloaded and installed these packages. Financial losses could include costs associated with incident response, system recovery, and potential unauthorized access to proprietary code repositories.

Mitigation: Remove the malicious npm packages and strengthen security measures around the use of open-source packages. Implement the following steps:
1. **Security Audits**: Conduct regular security audits of all third-party and open-source packages before use.
2. **Automated Scanning**: Use automated tools to scan for known vulnerabilities and malicious behaviors in packages.
3. **SSH Key Management**: Regularly rotate SSH keys and use stronger key management practices.
4. **Monitoring & Alerts**: Set up monitoring and alerts for unusual activities, such as unexpected SSH key usage or access to GitHub repositories.
5. **User Training**: Educate developers on the importance of verifying the source and integrity of packages before integrating them into their projects.
6. **Incident Response Plan**: Develop and maintain a robust incident response plan to quickly address security breaches.

Detection Signature:
- Service: npm
- Port: Not applicable
- Severity: Critical
- Incident: GitGot
- Signature name: “Malicious npm package”
  - Internal checks:
    - Setting1: Validate the integrity and authenticity of npm packages before use.
    - Setting2: Monitor for unauthorized script executions post-package installation.
    - Setting3: Ensure that SSH keys are stored securely and accessed appropriately.
  - External scanning:
    - Check for packages with known malicious behavior.
    - Monitor GitHub repositories for suspicious activity.

IoCs:
- package_name: warbeast2000
  - versions:
    - 1.0.8: 2da32a4c9e2c3f345f46c6e06d6eb41e13da13d9
    - 1.0.7: ad888d4e2b05bee35acf61c3cc053ecdc5e6ffaf
    - 1.0.6: 31abb6e4399138b33545ab5dfa3e12fe1ad4d16e
    - 1.0.5: d4a94f63a25891377334909cd544656b16c2b198
    - 1.0.3: ba5c8b0b76b798dea60110a296ba842702aacfa5
    - 1.0.2: d94e7e9f1965c248e17a6629c68f55ffa810e5d5
    - 1.0.1: f1317027456e02fa5c6cadaf897244fc28c24e31
    - 1.0.0: 663d74c7b76e5aae72ed45b3680fa3efbd17586d
- package_name: kodiak2k
  - versions:
    - 1.0.42: 909927bd61f3466d777bbbff38fd844ed8f5c134
    - 1.0.40: c6693fa7d0272562dd56ce8b44c0e99dd1210e43
    - 1.0.39: e762e1456a89218661f97e3ae356c07d35c298e8
    - 1.0.37: 24e376fbbb4c76b6b3c2572efeaa68053fa35202
    - 1.0.35: 7333b0ec183d34a104fd7b9a5f5b93541d39fed3
    - 1.0.34: 8f1311588eae8e2fb4eff6dad523198d49d4a766
    - 1.0.31: 5500ca40b5537f5b6782a143e8e2e9028b92de2d
    - 1.0.30: c6c77b4385978ab9cc1cab0826e75227d612b62a
    - 1.0.29: 9ccc6f5756bb99c5a4eea9e6abc84b79cb3ae6bd
    - 1.0.28: 8f1d36b074f2f6b7bc28718f88849a6aeb9dbbc6
    - 1.0.25: 717fa522c6ee505002bf17d3e79385544834461e
    - 1.0.24: 245f07892c85807e99a3d9da49677bbd6013ff4f
    - 1.0.22: 5117a318483b62cd40298358618e57350cc4158a
    - 1.0.21: 7165b6329ae524392812c534f9bb7e225e305ffe
    - 1.0.20: f6fda33768f859bc0b42bae40ac0c7dafa0f8d93
    - 1.0.19: e70476edc973548abba035993638c1bf3b829d54
    - 1.0.18: c1be7a6bd11236d1302fc6c0b206ec70b3b66d25
    - 1.0.16: 55f6b8f098ce173f4bfba374fc6da3cd8e0ff435
    - 1.0.15: d80e1abd7efcd1304a3b5ce1f6302d3a7edaaad9
    - 1.0.14: 13c0ff1347fe631974797aba94d17180ccc8eded
    - 1.0.13: 6f819af455a3b25edc1f27c938cbaaffdbf3d910
    - 1.0.12: 401b2fcd9359215f2f70f39d7d0aa1d50ab09b43
    - 1.0.11: d0c75071fc20f03d1b6d35ce7240b03c2a79f5c7
    - 1.0.10: ed6e04e810ff085a1a208788e47cce9352ab58bf
    - 1.0.9: 1d5da7f3fbea3d3915bddeb4c223ba147667a6ba
    - 1.0.8: fa562e9f3374055812c463b8e36c113a2aafa61c
    - 1.0.7: 3198a29d70628d1b9feaf8f7215c667383007f48
    - 1.0.6: 94836b8471a22563c91d35df6f3a1f5b8e028aa7
    - 1.0.5: 79c4359c0c21c4a6c43062a6e9e894ca0bd5617a
    - 1.0.4: 562238aff7746bdc60f891670c0c8bff46cebe02
    - 1.0.3: 96b336c4fddbd1d91a9d1eacb4c36441880ac5bf
    - 1.0.2: 445922433303e38e227121046d38dd3f31a1d6e0
    - 1.0.1: 30fb4cb07089d4e5773e1f20f0a0b25c34aa20ea
    - 1.0.0: 9300a1ff6bc49aa3f0bfe46245a470f14fc7fac3
- Second stage payloads:
  - SHA1: dba623bdad6bdb37359e047efcda34de4af5f518
  - SHA1: 9526b820a21fa70641361e061b0f99517ab1b184
