Source: [https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/deobfuscating-the-recent-emotet-epoch-4-macro/](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/deobfuscating-the-recent-emotet-epoch-4-macro/)

# Deobfuscating the Recent Emotet Epoch 4 Macro

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Emotet Epoch 4 Macro Campaign 

 Root cause: The root cause behind this incident is the use of highly obfuscated VBA macros in combination with a new tactic of compressing bloated document files into ZIP files. This campaign from Emotet involves the use of OneNote attachments to deliver the malicious payload, leveraging zero-byte padding techniques to inflate file sizes and evade security scanners *and bypass Microsoft macro block* (https://blog.checkpoint.com/security/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/). 

 Threat Actor/group/campaign: Emotet Botnet (Epoch 4), *MUMMY SPIDER* (https://www.logpoint.com/en/blog/emotet-ually-unstable-the-resurgence-of-a-nuisance/) 

 Organization/industry/location: Not specified (General targets of Emotet campaigns include various industries and geographical locations) 

 Start date – End date: Early March 2023 – Ongoing 

 MITRE TTPs: ['T1071.001: Application Layer Protocol - Web Protocols', 'T1566.001: Phishing - Spearphishing Attachment', 'T1059.005: Command and Scripting Interpreter - Visual Basic'] 

 Impact: The impact of this campaign includes the potential compromise of infected systems, leading to data theft, further malware distribution, and potential financial losses depending on the scope of the infection. Attackers gather user email data such as login credentials and contact information, expanding the campaign's reach *using malicious OneNote files and fake message trick* (https://blog.checkpoint.com/security/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/). *Additionally, attackers have utilized Qakbot, Bumblebee Loader, and Redline Stealer, with WSF files embedded in OneNote documents for payload delivery* (https://www.esentire.com/blog/pulse-check-on-onenote-for-malware-delivery). 

 Mitigation: ['Update email security gateways to detect and block malicious attachments, especially those using zero-byte padding techniques.', 'Implement advanced threat detection tools capable of analyzing and deobfuscating VBA macros.', 'Educate employees on recognizing phishing attempts and suspicious attachments.', 'Regularly update antivirus and endpoint protection software to detect and block Emotet-related payloads.', 'Employ network segmentation to limit the spread of the malware if an infection occurs.'] 

 Detection Signature: {'Service': 'Email Gateway', 'Port': 'N/A (Email-based attack)', 'Severity': 'Critical', 'Incident': 'Emotet Epoch 4 Macro Campaign', 'Signature name': 'Emotet Zero-byte padded document', 'Internal checks': {'Setting1': 'Block emails with attachments exceeding typical size limits for document files.', 'Setting2': 'Analyze email attachments for zero-byte padding techniques.', 'Setting3': 'Use sandboxing to open and analyze email attachments before delivery.'}, 'External scanning': {'Monitor for outbound connections to known Emotet C2 servers.': 'Detect and block suspicious download attempts from email attachments.'}} 

 IoCs: {'URLs': ['hxxp://xyktza.nbxyk.net/bwzysov/index/X3hFHbueMtgoEi/etaJ35/', 'hxxp://arlex.su/services/IE2h6fBsQRQOhHBI691U/', 'hxxp://api.660011.cc/wp-includes/b028GIRSxa4lY/', 'hxxp://www.garrett.kz/faq/B0faEHvS9msSo9xbVe/', 'hxxp://abrokov.com/lang/SZnqErcEtuE/', 'hxxp://rref.su/uchastniki/rNNdVArBjNc100n3p/', 'hxxp://mealux.by/pab4/wxuGxcqF85M/'], 'Hashes': {'ACH Payment info.zip': {'MD5': '68612b3d0094d51d3ca89ed6e3b16b4c', 'SHA1': 'b80ac7dda1b65be5297ba03b1ac17dbc2bb10339', 'SHA256': '7041a0d1b2d0c1199e4b7505b0ab181ad2cdc881e01a520fb66758f081e4d40d'}, 'ACH Payment info.doc': {'MD5': '141c079135312197dcb6d2adfe8b5663', 'SHA1': '4f2e8fcbdb60e099241c0e8e203c700d9d4941b2', 'SHA256': '57903dc1811ef431a8480dc489764d9b2dae324fcf002c924c8f3a592b96a922'}, 'downloaded.zip': {'MD5': '20758c45171dfad6bb02a77b773782d3', 'SHA1': 'e0ea8e2d0580ffe40ec5ed3bdd2bb78c6c7b2ffb', 'SHA256': 'a189c6cecce39ab05abb5386ca036887170c28a40cd1acd76dd7b4c36e0a2d9d'}, 'sHwNyPFidh5lkT7KX86sNryPMvM4.dll': {'MD5': 'fa914c6c9744ea25592dfca65a9d13e1', 'SHA1': '663861e36c8d55911a036bbc9108c3d774a97b2a', 'SHA256': 'cecdb3028c0879a850ccbf0535cc3918912d9b6e19b40b6dbfedb0c58265227c'}}} 

 Additional Modules: {'*Outlook Scraper*': '*Scrapes names and email addresses from victims’ Outlook accounts* (https://www.logpoint.com/en/blog/emotet-ually-unstable-the-resurgence-of-a-nuisance/)', '*MailPass View*': '*Reveals passwords and account details from email clients* (https://www.logpoint.com/en/blog/emotet-ually-unstable-the-resurgence-of-a-nuisance/)', '*WebBrowserPassView*': '*Recovers passwords from browsers like Chrome, Firefox* (https://www.logpoint.com/en/blog/emotet-ually-unstable-the-resurgence-of-a-nuisance/)'} 


# Related articles (describing the same threat) 
['https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/deobfuscating-the-recent-emotet-epoch-4-macro/', 'https://www.logpoint.com/en/blog/emotet-ually-unstable-the-resurgence-of-a-nuisance/', 'https://blog.checkpoint.com/security/march-2023s-most-wanted-malware-new-emotet-campaign-bypasses-microsoft-blocks-to-distribute-malicious-onenote-files/', 'https://www.esentire.com/blog/pulse-check-on-onenote-for-malware-delivery']
