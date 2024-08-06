# QBot Banker Delivered Through Business Correspondence

Incident: QBot Banker Delivered Through Business Correspondence

Root cause: Phishing emails with malicious PDF attachments

Impact: The specific number of impacted devices or financial losses is not provided in the report. However, given the scale of the campaign (approx. 4,500 emails detected), the potential impact could be significant in terms of compromised systems and financial data theft.

Mitigation: Implement a multi-layered security approach including:

1. **Email Security**:
    - Utilize advanced email filtering solutions to detect and block phishing emails.
    - Enable attachment and link scanning to identify malicious content.
    
2. **User Awareness Training**:
    - Conduct regular training programs to educate employees about phishing and social engineering attacks.
    - Simulate phishing attacks to test and improve user responses.
    
3. **Endpoint Protection**:
    - Deploy endpoint security solutions with behavioral detection capabilities to identify and block malicious activities.
    - Ensure all software and systems are up-to-date with the latest security patches.
    
4. **Network Security**:
    - Monitor network traffic for unusual patterns that may indicate an ongoing attack.
    - Implement network segmentation to limit the spread of malware.

Detection Signature:
- **Service**: Email Security Gateway
- **Port**: N/A (Email service)
- **Severity**: Critical
- **Incident**: QBot Banker Delivered Through Business Correspondence
- **Signature name**: “Malicious PDF Attachment in Phishing Email”
- **Internal checks**:
    - Setting1: Ensure all incoming emails are scanned for malicious attachments and URLs.
    - Setting2: Configure email security solutions to quarantine or block emails with suspicious content.
    - Setting3: Implement policies for handling email attachments and links, requiring verification before opening.
- **External scanning**:
    - Monitor for phishing emails targeting the organization.
    - Check for email domains used in phishing attacks and block them at the email gateway.

IoCs:
- **MD5**:
    - PDF files: 253E43124F66F4FAF23F9671BBBA3D98, 39FD8E69EB4CA6DA43B3BE015C2D8B7D
    - ZIP archives: 299FC65A2EECF5B9EF06F167575CC9E2, A6120562EB673552A61F7EEB577C05F8
    - WSF files: 1FBFE5C1CD26C536FC87C46B46DB754D, FD57B3C5D73A4ECD03DF67BA2E48F661
    - DLL: 28C25753F1ECD5C47D316394C7FCEDE2
- **Malicious links**:
    - ZIP archive: cica.com[.]co/stai/stai.php, abhishekmeena[.]in/ducs/ducs.php
    - DLL: rosewoodlaminates[.]com/hea/yWY9SJ4VOH, agtendelperu[.]com/FPu0Fa/EpN5Xvh, capitalperurrhh[.]com/vQ1iQg/u6oL8xlJ, centerkick[.]com/IC5EQ8/2v6u6vKQwk8, chimpcity[.]com/h7e/p5FuepRZjx, graficalevi.com[.]br/0p6P/R94icuyQ, kmphi[.]com/FWovmB/8oZ0BOV5HqEX, propertynear.co[.]uk/QyYWyp/XRgRWEdFv, theshirtsummit[.]com/MwBGSm/lGP5mGh
