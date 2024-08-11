Source: [https://research.checkpoint.com/2023/byos-bundle-your-own-stealer/](https://research.checkpoint.com/2023/byos-bundle-your-own-stealer/)

# BYOS - Bundle Your Own Stealer

Incident: BYOS - Bundle Your Own Stealer

Root cause: Misuse of dotnet bundle (single-file), self-contained format for malware distribution

Impact: The specific impact in terms of the number of devices, people affected, and financial losses isn't explicitly detailed in the blog. However, given the nature of the malware, it could be extensive, leading to potential financial losses due to theft of sensitive information and compromised accounts.

Mitigation: Implement robust security measures to prevent the distribution and execution of malicious software.
- **Detailed Steps for Mitigation:**
  1. **User Education and Awareness:** Educate users about the risks of downloading software from untrusted sources and clicking on suspicious ads.
  2. **Advanced Threat Detection Solutions:** Deploy advanced threat detection solutions like Check Point’s Harmony Endpoint to detect and block malware.
  3. **Network Security:** Implement network security measures to block access to known malicious URLs and C2 servers.
  4. **Regular Updates and Patches:** Ensure all systems and software are up-to-date with the latest security patches.
  5. **Secure Development Practices:** Enforce secure coding practices to avoid vulnerabilities in software that can be exploited by malware.
  6. **Behavioral Analysis:** Use behavioral analysis tools to detect and mitigate unusual activities indicative of malware infection.

Detection Signature:
  - **Service:** Dotnet applications
  - **Port:** Various (Based on C2 communication, e.g., 5505)
  - **Severity:** Critical
  - **Incident:** BYOS - Bundle Your Own Stealer
  - **Signature Name:** “Dotnet bundle malware detection”
  - **Internal Checks:**
    - Setting1: Verify the integrity of dotnet applications and their sources.
    - Setting2: Monitor for unauthorized downloads and executions of dotnet bundles.
    - Setting3: Ensure dotnet bundles are from trusted sources and are signed.
  - **External Scanning:**
    - Detect network communications to known C2 IP addresses and URLs.
    - Monitor for unusual traffic patterns and data exfiltration attempts.

IoCs: 
```plaintext
Files:
    - Google_AI.rar (SHA-256: dfa9f39ab29405475e3d110d9ac0cc21885760d07716595104db5e9e055c92a6)
    - ADSNEW-1.0.0.3.zip (SHA-256: 303c6d0cea77ae6343dda76ceabaefdd03cc80bd6e041d2b931e7f6d59ca3ef6)
    - Bot_Server6_1.0.0.3.zip (SHA-256: 90b37f26d7574a23437a2f0ad75d3cce5ecf3928efb58beacedde289fd3568bf)
    - ADS_1.0.0.3.zip (SHA-256: af92d0545ce01e5dcbe228a43babe6281a1631836e5631286908c7f0aa225f3d)
    - FB_1.0.0.3.zip (SHA-256: 25c0f65acb3ecfe435a39bed3f5013eadd85eca1e78a0dc754cb4b82389ee4bb)
    - COIN_1.0.0.4.zip (SHA-256: a99dbc0cb0a051ec68bd89c468fd589b201380f47330bdedbb69f9b076099711)
    - Coin_1.0.0.0.zip (SHA-256: b47ac379cc23a059e1aaaba351f528c5a955fd56da35928c0bc0043c4ab8b38a)
    - RiotClientServices.zip (SHA-256: 3198a613574a8ab84637bf80ebe5f6a56c851aa292973515c5de856f1e958d6d)
    - Various .dll and .exe files related to downloader and BundleBot stages.

Network:
    - URLs:
        - https://drive.google[.]com/uc?id=1obRjbjOkXO3aCKKVa6BHKYqsROXRVmzL&export=download&confirm=t
        - https://drive.google[.]com/uc?id=1-mC5c7o_B1VuS6dbQeDAAqLuPbfAV58O&export=download&confirm=t
        - https://drive.google[.]com/uc?id=1f6QEiRPXZ1GKKtu-G_d_iQ448xYPGfMC&export=download&confirm=t
        - https://drive.google[.]com/uc?id=1ypYJpu5pgaFRnXx64ZnCCfoGaUMYBt5E&export=download&confirm=t
        - https://drive.google[.]com/uc?id=1S2G8OmhMREHS8l24hG-BmGKINxEL_DD5&export=download&confirm=t
        - https://drive.google[.]com/uc?id=1Uvyx_Fj7wF9cVnQ3IwIAm5-i2IROsi0R&export=download&confirm=t
        - https://drive.google[.]com/uc?id=1teMU5O6VYsRjH9GVQf1V7h5ya-3Ssbkn&export=download&confirm=t
        - https://cp.bemilcoin[.]io/api/cookiePc?cookie
    - IP Addresses:
        - 51.79.180[.]158:5505
        - 85.239.242[.]27:5505
        - 139.99.80[.]193:5505
        - 139.99.38[.]193:5505

No further IoCs found.
```
