Source: [https://securelist.com/trojan-proxy-for-macos/111325/](https://securelist.com/trojan-proxy-for-macos/111325/)

# Analysis of a New MacOS Trojan-Proxy

Incident: macOS Trojan-Proxy in Cracked Software

Root cause: Distribution of malware via cracked software obtained from unauthorized websites.

Impact: The specific number of devices, people impacted, and financial losses are not provided in the document. However, the impact includes unauthorized access to infected macOS, Android, and Windows devices, which can be used for criminal activities such as launching attacks, purchasing illegal items, and compromising user data.

Mitigation: Users should avoid downloading software from unauthorized sources and ensure that all software is obtained from legitimate vendors. Implementing robust endpoint security solutions and educating users about the risks of using cracked software are essential.

Detailed Steps for mitigation:
1. **Educate Users**: Conduct awareness programs to inform users about the dangers of downloading and using cracked software.
2. **Endpoint Security**: Install and regularly update endpoint security solutions capable of detecting and mitigating malware threats.
3. **Software Policies**: Enforce strict policies that prohibit the use of unauthorized software within the organization.
4. **Regular Scanning**: Perform regular scans of all devices to detect and remove any unauthorized software or malware.
5. **OS and Software Updates**: Ensure that all operating systems and software are kept up-to-date with the latest security patches.
6. **Network Monitoring**: Implement network monitoring to detect unusual traffic patterns that may indicate malware activity.

Detection Signature:
Service: macOS Installer
Port: N/A
Severity: Critical
Incident: macOS Trojan-Proxy in Cracked Software
Signature name: “macOS Trojan-Proxy detected”
Internal checks:
- Setting1: Verify the integrity and source of software before installation.
- Setting2: Monitor and log installation scripts and processes.
- Setting3: Restrict administrative permissions and ensure they are granted only to trusted processes.
External scanning:
- Scan for unauthorized .PKG installers on the network.
- Detect and block C&C communication attempts to known malicious domains (e.g., register[.]akamaized[.]ca).

IoCs:
MD5:
- Trojan-Proxy binaries: 
  - 063d956b55da0d18f3f732c2bbd4bc28 — WindowServer
  - f6d1aa43d40727104f0517c91b117f72 — WindowServer
  - f40affab8ee804a49893fd1df3710622 — WindowServer
- Postinstall Scripts: 
  - 2a4fff0b167654edc7f62a747ea13067
  - 0049c3960ab98e11db3872a98078b7a6
  - ed7fd28bc482d9a822d78f515d18e93c
  - a0fe67385390bab476d9b716f4097907
- Property Lists: 
  - 0049c3960ab98e11db3872a98078b7a6 — GoogleHelperUpdater.plist
  - 2a4fff0b167654edc7f62a747ea13067 — GoogleHelperUpdater.plist
- PKGs:
  - 7b4b44bf6c3d8eb31f14206c0d76c321 — 4K Image Compressor.pkg
  - 00cbaee9a21dd0ca13ecbeca30ef9b26 — 4K Video Downloader Pro v4.24.3 macOS.pkg
  - 3432f1cb6be21938be87ad0b12202423 — Aiseesoft Mac Data Recovery.pkg
  - af7b3ac1adc4f4d563c75e8583c0f239 — Aiseesoft Mac Video Converter Ultimate.pkg
  - ec1698e7900210c642a2772e8d040f8c — allavsoft.pkg
  - 0c369d305e101381dfbd2f277417ca69 — AnyMP4 Android Data Recovery for Mac.pkg
  - 6f58024bfe61351035711f33a2133c40 — AweCleaner.pkg
  - 9b83fc25080d542a9fd71bbe0678e593 — Downie 4.pkg
  - 338f882d4fc0c2cc96eca6edb1d6a6f0 — FonePaw Data Recovery.pkg
  - b35db7dd042ca92ad7180f6a1e2bdad8 — iNet Network Scanner.pkg
  - e06b0fef08b711f8ba307d1c13cc1b97 — MacDroid.pkg
  - 7934bede64f6473576e400aefafae2b3 — MacX Video Converter Pro.pkg
  - 0003a4d2207462e24fbc711fa1b84533 — MouseBoost Pro.pkg
  - b5a334d92906f8a85cc86c582d3232bf — MWeb Pro.pkg
  - 3627fa05f7fb975a4be8392a14474757 — NetShred X.pkg
  - 01675deeb459c0cec6eb6b409698c42a — NetWorker Pro.pkg
  - d874167ece5528e9e997b60906940afa — Path Finder.pkg
  - f5cceb3eea65d0f7ae5a6b62d07cb869 — Patternodes.pkg
  - 311b665dad3d6ea77225b5a6529a8f0c — Perfectly Clear Workbench.pkg
  - 0e59a269fa6a34cc6fab8873e79e8011 — Print to PDF.pkg
  - d9e4e16ec9206ba427d280a955248829 — Project Office X.pkg
  - 206ff97436f3c229502040128bd39bbe — Rocket Typist.pkg
  - 59033b56c99c49a392ed7e653d296375 — Sketch.pkg
  - d933d00c01d1e0fd2df960e166a1e4b5 — SponsorBlock.pkg
  - 704f2606b0a12e42046c95e530bf5f38 — SystemToolkit.pkg
  - 1920e42d286080cc1ed6272db859e7b5 — TransData.pkg
  - b056054c992a386144304f1f3470234c — Vellum.pkg
  - 11fc6ec7cdb93f23c9756a788a4204bc — VideoDuke.pkg
  - a2d5f2c28b2b79cf29942f8bdd847a72 — Wondershare UniConverter 13.pkg
  - 19d3fcff714d7ffa1e325d46f6ddb8b2 — SQLPro Studio.pkg
  - 128068daf917c2df36bccdec97c3b66a — WinX HD Video Converter for Mac.pkg
  - 63086d31bb186abb294a5a737f235098 — Artstudio Pro.pkg
  - 9297a3753ddff6dae048a2a75a42e529 — Magic Sort List.pkg
  - 7f2d204f197e1205f74de603cba40010 — FoneLab Mac Data Retriever.pkg
  - 98c185a785f2ac075849336001bc5b9c — Apeaksoft Video Converter Ultimate for Mac.pkg

Android samples:
- d605b5673ca89a767662a4a83662eaa0 — s276.apk
- fb3c42ca1ff0ba96ac146c1672357994 — Swipis_v2.6.1[Mobile].apk

Windows samples:
- a408e30bbd449367291366d337d54f82 — wsclient.exe

URL:
- register[.]akamaized[.]ca:6101/strvn
