Source: [https://www.uptycs.com/blog/quasar-rat](https://www.uptycs.com/blog/quasar-rat)

# Quasar RATs Dual DLL Sideloading Technique

**Incident: QuasarRAT's Dual DLL Sideloading Technique**

**Root cause:** Exploitation of dual DLL sideloading technique utilizing trusted Microsoft files (`ctfmon.exe` and `calc.exe`).

**Impact:** The impact is not specifically quantified in the provided blog, but given the capabilities of QuasarRAT, it could potentially affect numerous devices and lead to significant data breaches, loss of sensitive information, and financial losses for affected individuals and organizations.

**Mitigation:** 
1. **Software and OS Updates:** Regularly update software and operating systems to patch vulnerabilities.
2. **Email Security:** Be cautious with emails from unknown sources. Avoid opening suspicious attachments or links.
3. **Behavioral Analysis Tools:** Implement tools that analyze unusual activities and potential threats.
4. **Security Training:** Educate employees and individuals about recognizing suspicious activities and not running unfamiliar files.
5. **Strong Security Policies:** Develop and enforce robust security policies within the organization.
6. **Advanced Endpoint Security Solutions:** Deploy advanced endpoint security solutions to detect and block suspicious activities at the device level.
7. **Threat Information Sharing:** Collaborate with cybersecurity experts and share threat intelligence within the industry to stay updated on evolving threats.
8. **Registry Monitoring:** Regularly monitor and audit Windows registry keys for unauthorized entries.

**Detection Signature:**
- **Service:** Windows Process Monitoring
- **Port:** Not applicable (local file execution)
- **Severity:** Critical
- **Incident:** QuasarRAT Dual DLL Sideloading
- **Signature name:** “Dual DLL Sideloading Detection”
    - **Internal checks:**
        - **Setting1:** Monitor execution of `ctfmon.exe` and `calc.exe` for unusual activity.
        - **Setting2:** Verify the integrity of `MsCtfMonitor.dll` and any DLLs loaded by `ctfmon.exe` and `calc.exe`.
        - **Setting3:** Ensure proper logging and monitoring of API calls related to process hollowing techniques.
    - **External scanning:**
        - Not applicable (local file execution)

**IoCs:**
- **File Names and Hashes:**
  - `ISO`: e4eb623a0f675960acb002d225c6f1d6
  - `eBill-997358806.exe`: B625C18E177D5BEB5A6F6432CCF46FB3
  - `monitor.ini`: 7074832F0EFB8A2130B1935EAE5A90D6
  - `MsCtfMonitor.dll`: B0DB6ADA5B81E42AADB82032CBC5FD60
  - `FileDownloader.exe`: 32DE5C2E0BA35CEAC3C515FA767E42BF
  - `Calc.exe`: 5da8c98136d98dfec4716edd79c7145f
  - `Secure32.dll`: d07e4afd8f26f3e2ce4560e08b7278fb
  - `Winsecu32.dll`: f11c63cb70a726f1f0b6accd5934e83
  - `Final Payload/Remotify Client`: 532AF2DB4C10352B2199724D528F535F
- **URLs:**
  - 3[.]94[.]91[.]208
  - ec2-3-94-91-208[.]compute-1[.]amazonaws[.]com
