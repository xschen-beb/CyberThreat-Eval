Source: [https://asec.ahnlab.com/en/51090/](https://asec.ahnlab.com/en/51090/)

# 3CX DesktopApp Supply Chain Attack Also Detected in Korea

Incident: 3CX DesktopApp Supply Chain Attack

Root cause: Compromised 3CX DesktopApp installation files

Impact: The blog does not provide specific numbers on devices or people impacted, nor does it give details on financial losses.

Mitigation: 
1. **Immediate Actions**:
    - **Isolate Affected Systems**: Disconnect the compromised systems from the network to prevent further spread.
    - **Patch and Update**: Ensure all software, especially 3CX DesktopApp, is updated to the latest version that is secure.
    - **Reinstall Software**: Reinstall 3CX DesktopApp from trusted sources to ensure it is not compromised.

2. **Long-term Actions**:
    - **Supply Chain Security**: Implement stringent security measures and regular audits for all third-party software vendors.
    - **Code Signing and Verification**: Ensure all software packages are signed and verify them before deployment.
    - **Network Monitoring**: Set up advanced network monitoring to detect unusual activities that could indicate a compromise.

3. **Detection Mechanisms**:
    - **Endpoint Detection and Response (EDR)**: Implement EDR solutions to detect and respond to threats at the endpoint level.
    - **Threat Intelligence**: Regularly update threat intelligence feeds to stay informed about new vulnerabilities and attack vectors.

4. **User Education**:
    - **Phishing Awareness**: Conduct regular training sessions for employees to recognize and avoid phishing attempts.
    - **Security Best Practices**: Educate users on the importance of downloading software from trusted and verified sources only.

Detection Signature:
- **Service**: 3CX DesktopApp
- **Port**: Not specified
- **Severity**: Critical
- **Incident**: 3CX DesktopApp Supply Chain Attack
- **Signature name**: “Compromised 3CX DesktopApp Installer”
- **Internal checks**:
  - Setting1: Verify the integrity of the 3CX DesktopApp installer file.
  - Setting2: Monitor for unexpected network connections initiated by 3CX DesktopApp.
  - Setting3: Use application whitelisting to ensure only approved versions of 3CX DesktopApp are installed and executed.
- **External scanning**:
  - Check for known malicious domains contacted by compromised 3CX DesktopApp instances.
  - Monitor for unusual traffic patterns, such as connections to C&C servers.

IoCs:
- **SHA2 Hashes**:
  - 11be1803e2e307b647a8a7e02d128335c448ff741bf06bf52b332e0bbf423b03
  - 5009c7d1590c1f8c05827122172583ddf924c53b55a46826abf66da46725505a
  - 5407cda7d3a75e7b1e030b1f33337a56f293578ffa8b3ae19c671051ed314290
  - 59e1edf4d82fae4978e97512b0331b7eb21dd4b838b850ba46794d9c7a2c0983
  - 7986bbaee8940da11ce089383521ab420c443ab7b15ed42aed91fd31ce833896
- **URLs**:
  - http[:]//akamaitechcloudservices[.]com/v2/fileapi
  - http[:]//azuredeploystore[.]com/cloud/images
  - http[:]//azureonlinestorage[.]com/google/storage
  - http[:]//glcloudservice[.]com/v1/status
  - http[:]//msedgepackageinfo[.]com/ms-webview

Additional IoCs are available on AhnLab TIP.

No IoCs found. (Note: This line is included for completeness, but actual IoCs are listed above.)
