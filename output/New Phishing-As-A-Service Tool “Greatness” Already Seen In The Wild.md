# New Phishing-As-A-Service Tool “Greatness” Already Seen In The Wild

Incident: "Greatness" Phishing-as-a-Service (PaaS) Tool

Root cause: The root cause of the incidents involving the "Greatness" PaaS tool is the deployment and configuration of a phishing kit that facilitates advanced phishing attacks. This kit uses an API key, integrates with Telegram bots, and features multi-factor authentication (MFA) bypass.

Impact: The exact number of devices, people impacted, and financial losses are not explicitly stated in the document. However, it is mentioned that the victims are almost exclusively businesses in the U.S., U.K., Australia, South Africa, and Canada, targeting sectors such as manufacturing, healthcare, technology, and real estate.

Mitigation: 
1. Educate and train employees to recognize phishing attempts and suspicious emails.
2. Implement and enforce strong email security measures, such as using Cisco Secure Email or equivalent solutions.
3. Use multi-factor authentication (MFA) to add an extra layer of security, though be aware of potential MFA bypass techniques.
4. Regularly update and patch software to protect against known vulnerabilities.
5. Monitor network traffic for suspicious activities and use tools like Cisco Secure Firewall or equivalent solutions to detect malicious activity.
6. Employ web scanning solutions such as Cisco Secure Web Appliance to prevent access to malicious websites.
7. Use threat intelligence services to stay updated on the latest phishing campaigns and indicators of compromise (IoCs).

Detection Signature:
Service: Web Server (hosting the phishing kit)  
Port: 80, 443   
Severity: Critical  
Incident: "Greatness" Phishing-as-a-Service Tool  
Signature name: “Greatness Phishing Kit Deployment”    
Internal checks:    
    - Setting1: Ensure that web servers hosting Microsoft 365 login pages are not compromised.    
    - Setting2: Verify that no unauthorized scripts or phishing kits are deployed on web servers.    
    - Setting3: Monitor and restrict the use of API keys and integration with third-party services like Telegram.    
External scanning:    
    - Port (80, 443) open
    - Presence of suspicious or unauthorized web pages mimicking Microsoft 365 login pages

IoCs: 
No IoCs found in the provided document. However, it is suggested to check Cisco Talos GitHub repository for any IoCs related to this research.
