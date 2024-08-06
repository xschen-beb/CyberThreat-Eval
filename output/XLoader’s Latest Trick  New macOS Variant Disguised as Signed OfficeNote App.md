# XLoader’s Latest Trick  New macOS Variant Disguised as Signed OfficeNote App

Incident: XLoader’s Latest Trick - New macOS Variant Disguised as Signed OfficeNote App

Root cause: The root cause of this incident is the distribution of a new variant of the XLoader malware disguised as a legitimate OfficeNote application signed with a now-revoked Apple developer signature.

Impact: 
- Devices impacted: The exact number of devices is not specified, but given the widespread distribution, multiple macOS systems globally are likely affected.
- Financial losses: Specific financial losses are not detailed in the blog, but potential impacts include costs associated with incident response, potential data theft, and subsequent misuse of stolen credentials.

Mitigation: 
1. **Revoke Certificates**: Ensure any compromised developer certificates are revoked immediately, as Apple did with the certificate used for signing OfficeNote.
2. **Endpoint Security**: Deploy comprehensive endpoint security solutions that can detect and block the execution of malicious payloads, such as SentinelOne which detected this variant.
3. **User Education**: Educate users about the risks of downloading and executing applications from untrusted sources.
4. **Regular Updates**: Keep macOS and all installed applications updated to protect against vulnerabilities that malware might exploit.
5. **Application Control**: Implement application control policies to restrict the execution of unauthorized applications.

Detailed Steps for Mitigation:
1. **Revoke Developer Certificates**:
   - Contact Apple Developer Support to revoke any compromised certificates.
   - Ensure that revoked certificates are propagated to all security solutions for blacklisting.

2. **Deploy Endpoint Protection**:
   - Install and configure endpoint protection solutions like SentinelOne across all macOS devices.
   - Ensure real-time protection and enable automatic updates for threat definitions.

3. **Educate Users**:
   - Conduct regular training sessions on recognizing phishing attempts and suspicious applications.
   - Provide guidelines on downloading software only from trusted sources and the official Apple App Store.

4. **Update Systems**:
   - Schedule regular updates for macOS systems and all installed software.
   - Enable automatic updates where possible to ensure timely patching of vulnerabilities.

5. **Implement Application Control**:
   - Use macOS built-in security features, such as Gatekeeper, to control the execution of applications.
   - Set policies to only allow applications from identified developers and the App Store.

Detection Signature:
Service: macOS System
Port: N/A
Severity: Critical
Incident: XLoader Variant Disguised as OfficeNote
Signature name: “Malicious macOS Application - OfficeNote”
Internal checks:
  - Setting1: Verify the developer signature of applications before execution.
  - Setting2: Monitor for creation of hidden directories and unauthorized persistence agents.
  - Setting3: Look for hardcoded error messages and high entropy in binaries as indicators of obfuscation.
External scanning:
  - Scan for known IoCs associated with XLoader, such as specific SHA1 hashes and network communications.

IoCs:
- File Hashes:
  - 26fd638334c9c1bd111c528745c10d00aa77249d (Mach-O Payload)
  - 47cacf7497c92aab6cded8e59d2104215d8fab86 (Mach-O Dropper)
  - 5946452d1537cf2a0e28c77fa278554ce631223c (Disk Image)
  - 958147ab54ee433ac57809b0e8fd94f811d523ba (Mach-O Payload)

- FilePaths:
  - ~/73a470tO

- Developer ID:
  - MAIT JAKHU (54YDV8NU9C)

- Network Communications:
  - 23[.]227.38[.]74
  - 62[.]72.14[.]220
  - 66[.]29.151[.]121
  - 104[.]21.26[.]182
  - 104[.]21.32[.]235
  - 104[.]21.34[.]62
  - 137[.]220.225[.]17
  - 142[.]251.163[.]121
  - www[.]activ-ketodietakjsy620[.]cloud
  - www[.]akrsnamchi[.]com
  - www[.]brioche-amsterdam[.]com
  - www[.]corkagenexus[.]com
  - www[.]growind[.]info
  - www[.]hatch[.]computer
  - www[.]kiavisa[.]com
  - www[.]lushespets[.]com
  - www[.]mommachic[.]com
  - www[.]nationalrecoveryllc[.]com
  - www[.]pinksugarpopmontana[.]com
  - www[.]qhsbobfv[.]top
  - www[.]qq9122[.]com
  - www[.]raveready[.]shop
  - www[.]spv88[.]online
  - www[.]switchmerge[.]com
