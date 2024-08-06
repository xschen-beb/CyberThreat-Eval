# Malvertising in Google Search Results Delivering Stealers

Incident: Malvertising in Google search results delivering stealers

Root cause: Abuse of Google Advertising to distribute malware via fake websites mimicking legitimate software download pages.

Impact: The blog does not provide a specific number of impacted devices or financial losses directly. However, given the nature of the attack and the popularity of software like Notepad++ and Blender 3D, the potential scope could include thousands of users globally, leading to significant data compromise and potential financial losses.

Mitigation:
1. **Secure Search Advertisements:**
   - Google and other search engine companies should enhance their verification processes for advertisers to prevent malicious ads from being served.
   - Employ AI and machine learning techniques to detect and block malvertising campaigns more effectively.

2. **User Awareness:**
   - Educate users about the risks of downloading software from search engine ads and encourage them to use official websites or trusted sources.
   - Promote the use of ad blockers that can help reduce exposure to malicious advertisements.

3. **Software Authenticity Verification:**
   - Implement digital signatures and checksums for downloadable software. Users should verify these signatures against known good values before executing the downloaded files.

4. **Endpoint Protection:**
   - Deploy advanced endpoint protection solutions that can detect and block malicious payloads and suspicious behaviors, such as the execution of unknown scripts or binaries.

5. **Network Monitoring:**
   - Monitor network traffic for suspicious activities, such as connections to known malicious IP addresses or domains.
   - Implement DNS filtering to block access to malicious domains.

**Detailed Steps for mitigation:**
1. **For Google and Search Engines:**
   - Enhance the ad verification process to detect and block malvertising.
   - Implement stricter policies and procedures for advertisers, including mandatory verification for software-related ads.

2. **For Organizations:**
   - Educate employees about the risks of downloading software from search engine ads.
   - Deploy enterprise-grade security solutions that include real-time threat detection and response capabilities.
   - Regularly update and patch all software and systems to minimize vulnerabilities.

3. **For End Users:**
   - Use trusted sources for software downloads and avoid clicking on search engine ads for software.
   - Verify the authenticity of downloaded software using checksums or digital signatures.
   - Use ad blockers to reduce exposure to potentially malicious ads.

Detection Signature:
   - Service: Web Browser
   - Port: Not applicable (web traffic via standard HTTP/HTTPS ports 80/443)
   - Severity: Critical
   - Incident: Malvertising in Google search results delivering stealers
   - Signature name: “Malicious Ad Campaign Detection”
   - Internal checks:
       - Setting1: Monitor for unusual or unauthorized downloads from web browsers.
       - Setting2: Use security solutions that can analyze web traffic for malvertising.
       - Setting3: Ensure endpoint protection is active and updated to detect stealer malware.
   - External scanning:
       - Detect unusual DNS requests to known malicious domains.
       - Monitor for connections to IP addresses associated with known malicious activities.

IoCs:
   - IP: 91.229.23[.]200
   - Domain: blahder3dsoft[.]store, blender3d-download[.]com, blender3d-download[.]net, blender3d-download[.]org, and others listed in the document
   - Hashes:
       - E0BDF36E4A7CF1B332DC42FD8914BA8B (blender-3.4.1-windows-x64.zip)
       - BBA8AA93FCDDA5AC7663E90C0EEFA2E7 (blender-3.4.1-windows-x64.exe)
       - 4b6249bea60eec2d9e6890162a7fca5f (Blender.rar)
       - 8d709a5ce84504f83303afda88649b24 (RedLine stealer)
       - d0915b6057eb60c3878ce88d71efc351 (RedLine stealer)
   - URLs:
       - hxxps[:]//download2392.mediafire.com/bb289kqoibyg/1udjwornnpwxlua/blender-3.4.1-windows-x64.zip/
       - hxxps[:]//github.com/sup6724/blender3d13/releases/download/updates/blender-3.4.1-windows-x64.zip
       - hxxps[://]blahder3dsoft[.]store/Blender[.]rar
       - http[:]//45.93.201[.]114/docs/[RandomChars].txt
