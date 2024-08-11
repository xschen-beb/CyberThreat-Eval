Source: [https://blog.morphisec.com/guloader-campaign-targets-law-firms-in-the-us](https://blog.morphisec.com/guloader-campaign-targets-law-firms-in-the-us)

# GuLoader Campaign Targets Law Firms in the US

Incident: GuLoader Campaign Targets Law Firms in the US

Root cause: Phishing campaign leveraging malicious PDF attachments and VBScript payloads.

Impact: The specific number of devices and people impacted, as well as the financial losses, are not disclosed in the blog.

Mitigation:
- **Email Filtering:** Implement advanced email filtering to block phishing emails with malicious attachments.
- **User Training:** Conduct regular cybersecurity training to educate users about phishing and safe email practices.
- **Endpoint Protection:** Deploy advanced endpoint protection solutions, such as Morphisec AMTD, to block unauthorized processes.
- **Network Segmentation:** Segment the network to limit the spread of malware in case of an infection.
- **Regular Updates:** Keep systems and software updated to protect against known vulnerabilities.

Detection Signature:
Service: GitHub Pages  
Port: 443  
Severity: Critical  
Incident: GuLoader Campaign  
Signature name: “Malicious GitHub Pages Hosting”  
Internal checks (see next)  
   - Setting1: Monitor for unusual outbound connections to GitHub Pages domains.  
   - Setting2: Alert on execution of scripts downloaded from GitHub Pages.  
   - Setting3: Detect and block obfuscated VBScript and Powershell scripts.  
External scanning (see next)  
   - URL patterns matching malicious GitHub Pages hosting.
   - Check for phishing indicators in email attachments.

IoCs:
- PDF files:
  - 06b3c92f9718da323c4d3a18d69629696dc5f799a7ddaef4e7415d117b345af4
  - 2438bfe409fb32b18fca95f95fff85a778502553ce627d0f25e54653c84e0e0c
  - 8ef6d783f8aaffffdecfa13bcc20b4f1a18f6c4c3c4cc22e93fb5c8d753ca338
  - 584f1b20d6a1939933663dd57e13603c7fe664f81a117f0d5456b4d448506b7d
  - 3c5d19be4d5e1f600c31f837b9650ad8c7508d6691f6cd4889d2178809703de7
  - a8f7f8900375ad8d2fda626f098cdda95bb4e42855cbae91c290d3f020bfd45f
  - 7add364a2a13388cc035e5f082f7adbb76c1e60d82748acd3eb30d6c9b3ce5be
  - a66b1a9fcf5d5fecd53152ecf68be150028109f484ad349d7029d72b3c5c9564

- VBS:
  - a3855846b501325a4b11cbc27fac9f845a56c91e088edbd75fb5ab651f913ede
  - 60d70005c38b331cd46b8af0f8e3d8cf181bdf43fb685a1962b1e26e085a6e2a
  - 2d343c091484eac696a23418f04df81c35bc538a10d25193ad014d11c4422907
  - f78e18ae09d30f4062de466afb5e1de5041b6cda445b15a3cca912a3294f731a
  - d63a863c26d03016ece637cd34c0f93efa1fe691b4328c7a915ef3c07ae1811f
  - 0873011390fd1d2dce527a726607255693c306774dfed8ac6b5b88efd4920d48
  - c766754790aaf298acbf85229096d8f0493fa9ee64d429facd425e30ceceaa4b
  - 2ba636d017b5df7a706b4dfede215733807fff6db5fea202e4a5b6bf515ba8b4
  - a86c6baa5323f07155cf414cdfd667216fb2816ec999ad240042c78b86175492

- URLs:
  - quickcheckx[.]github.io/quickme/Udgan.u32
  - quickcheckx[.]github.io/quickme/KmJiw22.bin
  - quickcheckx[.]github.io/quickme/Panzersti.lpk
  - quickcheckx[.]github.io/quickme/XbuLYedqxf70.bin
  - zeusblog[.]cloud/Adobe.pdf

- C2:
  - apdfhost[.]online


