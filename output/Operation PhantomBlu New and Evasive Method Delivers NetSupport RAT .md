# Operation PhantomBlu New and Evasive Method Delivers NetSupport RAT 

Incident: Operation PhantomBlu: New and Evasive Method Delivers NetSupport RAT

Root cause: Exploitation of Microsoft Office document templates via OLE template manipulation and social engineering tactics.

Impact: Hundreds of employees in various US-based organizations were targeted. The exact number of devices and financial losses are not specified in the report.

Mitigation: To prevent similar incidents, follow these steps:

1. **Email Filtering and Security**:
   - Implement advanced email filtering to detect and block phishing emails.
   - Use anti-phishing tools that can identify and block malicious attachments and links.

2. **User Education**:
   - Train employees to recognize phishing attempts and suspicious emails.
   - Emphasize the importance of not enabling macros or editing on unexpected documents.

3. **Document Security**:
   - Disable macros by default in Microsoft Office applications.
   - Implement policies to restrict the use of OLE objects in email attachments.

4. **Endpoint Protection**:
   - Deploy endpoint protection solutions that can detect and block the execution of malicious scripts like PowerShell.
   - Regularly update and patch software to mitigate vulnerabilities.

5. **Network Security**:
   - Monitor network traffic for unusual patterns that may indicate data exfiltration or command and control communications.
   - Implement network segmentation to limit the spread of malware within the organization.

6. **Incident Response Plan**:
   - Develop an incident response plan to quickly address and mitigate the impact of malware infections.
   - Regularly test and update the incident response plan to ensure effectiveness.

Detection Signature:
   Service: Microsoft Office
   Port: N/A (as this is primarily an email and document-based attack)
   Severity: Critical
   Incident: Operation PhantomBlu
   Signature name: “OLE Template Manipulation in Email”
   Internal checks:
      - Setting1: Monitor for OLE objects in incoming email attachments - In email security solutions
      - Setting2: Detect and alert on the use of PowerShell to download and execute scripts - In endpoint protection solutions
      - Setting3: Ensure macros and OLE objects are disabled by default in Microsoft Office applications - In Office settings
   External scanning:
      - Monitor for known malicious URLs and domains used in the campaign
      - Check for unusual network activity related to command and control servers

IoCs:
   - Hashes (SHA-256):
     - Email: 16e6dfd67d5049ffedb8c55bee6ad80fc0283757bc60d4f12c56675b1da5bf61
     - Docx: 1abf56bc5fbf84805ed0fbf28e7f986c7bb2833972793252f3e358b13b638bb1
     - Injected ZIP: 95898c9abce738ca53e44290f4d4aa4e8486398de3163e3482f510633d50ee6c
     - LNK file: d07323226c7be1a38ffd8716bc7d77bdb226b81fd6ccd493c55b2711014c0188
     - Final ZIP: 94499196a62341b4f1cd10f3e1ba6003d0c4db66c1eb0d1b7e66b7eb4f2b67b6
     - Client32.exe: 89f0c8f170fe9ea28b1056517160e92e2d7d4e8aa81f4ed696932230413a6ce1

   - URLs and Hostnames:
     - yourownmart[.]com/solar[.]txt
     - firstieragency[.]com/depbrndksokkkdkxoqnazneifidmyyjdpji[.]txt
     - yourownmart[.]com
     - firstieragency[.]com
     - parabmasale[.]com
     - tapouttv28[.]com

   - IP Addresses:
     - 192[.]236[.]192[.]48
     - 173[.]252[.]167[.]50
     - 199[.]188[.]205[.]15
     - 46[.]105[.]141[.]54

   - Others:
     - Message ID contains: “sendinblue.com”
     - Return Path contains: “sender-sib.com”
