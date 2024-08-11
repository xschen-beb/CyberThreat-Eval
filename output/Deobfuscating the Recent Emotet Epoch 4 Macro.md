Source: [https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/deobfuscating-the-recent-emotet-epoch-4-macro/](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/deobfuscating-the-recent-emotet-epoch-4-macro/)

# Deobfuscating the Recent Emotet Epoch 4 Macro

Incident: Emotet Epoch 4 Malware Campaign

Root cause: Emotet botnet leveraging OneNote attachments and zero-byte padding technique to obfuscate malicious macros.

Impact: The specific number of records or devices impacted and the financial losses are not detailed in the blog, but considering Emotet's history, it can affect thousands of systems and cause significant financial and reputational damage to organizations.

Mitigation: 
1. Implement robust email security solutions to detect and block suspicious attachments.
2. Educate employees on recognizing phishing emails and avoiding opening suspicious attachments.
3. Regularly update and patch all software to protect against exploits.
4. Use advanced threat detection systems to identify and mitigate zero-byte padding techniques and other obfuscation methods.

**Detailed Steps for mitigation:**
1. **Email Security Enhancements:**
   - Deploy a comprehensive email security gateway with advanced threat detection capabilities.
   - Enable attachment scanning and sandboxing to analyze and block malicious files.
   - Implement strict email filtering rules to block emails from suspicious sources.

2. **Employee Training:**
   - Conduct regular training sessions to raise awareness about phishing attacks and the importance of not opening email attachments from unknown sources.
   - Simulate phishing attacks to test and improve employee response.

3. **Regular Updates and Patching:**
   - Ensure all systems, including email clients and document viewers (such as Microsoft OneNote), are up to date with the latest security patches.
   - Regularly review and apply security updates for all software and systems.

4. **Advanced Threat Detection:**
   - Use endpoint detection and response (EDR) tools to monitor and analyze suspicious activities on endpoints.
   - Implement network monitoring solutions to detect abnormal traffic patterns that may indicate an ongoing attack.

Detection Signature:
   Service: Microsoft OneNote
   Port: N/A (Email vector)
   Severity: Critical
   Incident: Emotet Epoch 4 Malware Campaign
   Signature name: “Emotet OneNote Attachment”
   Internal checks:
       - Setting1: Monitor for large attachments with zero-byte padding in incoming emails.
       - Setting2: Enable advanced email attachment scanning for OneNote and other document formats.
       - Setting3: Configure EDR solutions to flag and isolate suspicious document macros.
   External scanning:
       - Scan email servers for incoming emails with large attachments.
       - Use threat intelligence feeds to identify known malicious IPs and domains distributing Emotet.

IoCs:
   **URLs:**
   - hxxp://xyktza.nbxyk.net/bwzysov/index/X3hFHbueMtgoEi/etaJ35/
   - hxxp://arlex.su/services/IE2h6fBsQRQOhHBI691U/
   - hxxp://api.660011.cc/wp-includes/b028GIRSxa4lY/
   - hxxp://www.garrett.kz/faq/B0faEHvS9msSo9xbVe/
   - hxxp://abrokov.com/lang/SZnqErcEtuE/
   - hxxp://rref.su/uchastniki/rNNdVArBjNc100n3p/
   - hxxp://mealux.by/pab4/wxuGxcqF85M/

   **Hashes:**
   - ACH Payment info.zip: MD5 68612b3d0094d51d3ca89ed6e3b16b4c, SHA1 b80ac7dda1b65be5297ba03b1ac17dbc2bb10339, SHA256 7041a0d1b2d0c1199e4b7505b0ab181ad2cdc881e01a520fb66758f081e4d40d
   - ACH Payment info.doc: MD5 141c079135312197dcb6d2adfe8b5663, SHA1 4f2e8fcbdb60e099241c0e8e203c700d9d4941b2, SHA256 57903dc1811ef431a8480dc489764d9b2dae324fcf002c924c8f3a592b96a922
   - downloaded.zip: MD5 20758c45171dfad6bb02a77b773782d3, SHA1 e0ea8e2d0580ffe40ec5ed3bdd2bb78c6c7b2ffb, SHA256 a189c6cecce39ab05abb5386ca036887170c28a40cd1acd76dd7b4c36e0a2d9d
   - sHwNyPFidh5lkT7KX86sNryPMvM4.dll: MD5 fa914c6c9744ea25592dfca65a9d13e1, SHA1 663861e36c8d55911a036bbc9108c3d774a97b2a, SHA256 cecdb3028c0879a850ccbf0535cc3918912d9b6e19b40b6dbfedb0c58265227c
