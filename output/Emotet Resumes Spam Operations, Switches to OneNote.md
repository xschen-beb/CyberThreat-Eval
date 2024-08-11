Source: [https://blog.talosintelligence.com/emotet-switches-to-onenote/](https://blog.talosintelligence.com/emotet-switches-to-onenote/)

# Emotet Resumes Spam Operations, Switches to OneNote

Incident: Emotet Resumes Spam Operations, Switches to OneNote

Root cause: Emotet malware campaign leveraging malicious OneNote documents

Impact: The exact number of devices and individuals affected, as well as financial losses, are not specified in the blog. However, Emotet is known for widespread spam operations that can potentially impact thousands of devices.

Mitigation: 
1. **Endpoint Protection**: Ensure all endpoints are protected with advanced malware protection software.
    - Use Cisco Secure Endpoint or other reputable endpoint protection solutions.
    - Regularly update anti-virus and anti-malware software definitions.

2. **Email Security**: Implement robust email security to filter and block malicious emails.
    - Utilize Cisco Secure Email or similar solutions to block malicious attachments.
    - Educate users on recognizing phishing attempts and suspicious attachments.

3. **Firewall and Network Security**: Deploy and configure next-generation firewalls and network security tools.
    - Use Cisco Secure Firewall and Meraki MX to monitor and block malicious activities.
    - Implement network traffic analysis with tools like Cisco Secure Network/Cloud Analytics.

4. **Web and Internet Security**: Block access to malicious domains and URLs.
    - Use solutions like Cisco Umbrella to prevent connections to known malicious domains.
    - Deploy web security appliances to filter and test suspicious sites before access.

5. **Multi-Factor Authentication (MFA)**: Enforce MFA to ensure secure access to networks.
    - Implement Cisco Duo or similar MFA solutions.

6. **Regular Security Audits and Updates**: Conduct regular security audits and ensure all software and systems are up to date.
    - Monitor for new vulnerabilities and threats.
    - Apply security patches promptly.

Detection Signature:
- **Service**: Microsoft OneNote
- **Port**: Not applicable (OneNote is typically used over standard HTTP/HTTPS ports, 80/443)
- **Severity**: Critical
- **Incident**: Emotet Resumes Spam Operations
- **Signature name**: “Emotet OneNote Malspam”
- **Internal checks**:
    - **Setting1**: Ensure email attachments are scanned for malicious content.
    - **Setting2**: Configure endpoint protection to detect and block OneNote-based malware.
    - **Setting3**: Implement web filtering to block malicious domains used for payload delivery.
- **External scanning**:
    - Detect emails with OneNote attachments.
    - Identify OneNote documents with embedded malicious scripts.

IoCs: 
- No specific IoCs were provided in the blog. However, the blog mentions that "Indicators of compromise (IOCs) associated with ongoing Emotet campaigns can be found here." The exact link to the IOCs was not included in the provided text. 

For further protection, users and organizations should seek detailed IoCs from the relevant security advisories and databases to update their detection mechanisms accordingly.
