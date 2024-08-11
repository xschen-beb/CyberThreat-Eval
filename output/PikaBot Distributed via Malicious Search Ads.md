Source: [https://www.malwarebytes.com/blog/threat-intelligence/2023/12/pikabot-distributed-via-malicious-ads](https://www.malwarebytes.com/blog/threat-intelligence/2023/12/pikabot-distributed-via-malicious-ads)

# PikaBot Distributed via Malicious Search Ads

Incident: PikaBot Distributed via Malicious Search Ads

Root cause: Exploitation of Google search ads for distributing malware, utilizing decoy infrastructure to bypass security measures and fingerprinting techniques to evade detection in virtual environments.

Impact: Unknown exact number of devices or people impacted. Financial losses could include costs associated with malware removal, potential data breaches, and system downtime.

Mitigation: Implement stricter security checks for search ads, monitor and restrict the use of third-party marketing platforms, enforce strict application whitelisting, and user education on recognizing malvertising.
 
Detailed Steps for mitigation:
1. **Stricter Ad Verification**: Strengthen ad verification processes to ensure malicious ads are not approved. This can include more rigorous checks and manual reviews.
2. **Enhanced Fingerprinting Detection**: Implement advanced detection mechanisms that can identify and block evasive fingerprinting attempts used by these campaigns.
3. **Application Whitelisting**: Only allow the installation of applications from trusted and verified repositories. Block installation from unknown sources.
4. **User Education**: Train end-users to recognize deceptive ads and suspicious links, and encourage them to report any unusual activity.
5. **Regular Monitoring**: Continuously monitor for new malicious domains and payloads associated with malvertising campaigns.
6. **Collaboration with Ad Platforms**: Work closely with ad platforms like Google to identify and take down malicious ads quickly.

Detection Signature:
- **Service**: Web Browser/Advertising Platform
- **Port**: Not applicable (web-based)
- **Severity**: Critical
- **Incident**: PikaBot Malvertising Campaign
- **Signature name**: “Malicious Search Ad Distribution”
    - Internal checks:
        - Setting1: Monitor search ads and links for signs of malicious behavior.
        - Setting2: Implement ad filtering mechanisms to detect and block suspicious ads.
        - Setting3: Use behavioral analysis to identify potential malvertising patterns.
    - External scanning:
        - Malicious domains detected in ad traffic.
        - Presence of known malicious payloads in downloaded files.

IoCs:
- **Domains**:
    - anadesky[.]ovmv[.]net
    - cxtensones[.]top
- **URLs**:
    - dropbox[.]com/scl/fi/3o9baztz08bdw6yts8sft/Installer.msi?dl=1&rlkey=wpbj6u5u6tja92y1t157z4cpq
    - dropbox[.]com/scl/fi/p8iup71lu1tiwsyxr909l/Installer.msi?dl=1&rlkey=h07ehkq617rxphb3asmd91xtu
    - dropbox[.]com/scl/fi/tzq52v1t9lyqq1nys3evj/InstallerKS.msi?dl=1&rlkey=qbtes3fd3v3vtlzuz8ql9t3qj
- **Hashes**:
    - 0e81a36141d196401c46f6ce293a370e8f21c5e074db5442ff2ba6f223c435f5
    - da81259f341b83842bf52325a22db28af0bc752e703a93f1027fa8d38d3495ff
    - 69281eea10f5bfcfd8bc0481f0da9e648d1bd4d519fe57da82f2a9a452d60320
- **C2s**:
    - 172[.]232[.]186[.]25
    - 57[.]128[.]83[.]129
    - 57[.]128[.]164[.]11
    - 57[.]128[.]108[.]132
    - 139[.]99[.]222[.]29
    - 172[.]232[.]164[.]77
    - 54[.]37[.]79[.]82
    - 172[.]232[.]162[.]198
    - 57[.]128[.]109[.]221
