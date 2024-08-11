Source: [https://blog.talosintelligence.com/cybercriminals-target-graphic-designers-with-gpu-miners/](https://blog.talosintelligence.com/cybercriminals-target-graphic-designers-with-gpu-miners/)

# Cybercriminals Target Graphic Designers with GPU Miners

Incident: Cybercriminals target graphic designers with GPU miners

Root cause: Abuse of Advanced Installer’s Custom Actions feature to package legitimate software with malicious scripts.

Impact: The exact number of devices and financial losses are not specified in the blog. However, the impact involves multiple countries including France, Switzerland, the U.S., Canada, Algeria, Sweden, Germany, Tunisia, Madagascar, Singapore, and Vietnam.

Mitigation: Implement the following detailed steps to mitigate such incidents:

1. **Secure software distribution channels:**
   - Ensure that all software installers are obtained from verified and trusted sources.
   - Perform rigorous integrity checks on software packages before deployment.

2. **Monitor and control application behavior:**
   - Use security solutions that can detect and block malicious script execution.
   - Implement application whitelisting to prevent unauthorized applications from running.

3. **Harden PowerShell and script execution policies:**
   - Set PowerShell execution policies to 'Restricted' or 'AllSigned' to block unauthorized scripts.
   - Enable logging for PowerShell script executions and monitor logs for suspicious activities.

4. **Enhance endpoint security:**
   - Deploy robust endpoint protection solutions that can detect and mitigate RATs and cryptominers.
   - Regularly update and patch endpoint security solutions to ensure they can handle the latest threats.

5. **Implement network-level defenses:**
   - Use firewalls and intrusion detection/prevention systems to monitor and block malicious network traffic.
   - Restrict outbound connections to known malicious domains and IP addresses.

6. **Conduct regular security awareness training:**
   - Educate users on the risks of downloading and executing software from untrusted sources.
   - Train users to recognize phishing attempts and other social engineering tactics.

Detection Signature:

Service: Advanced Installer
Port: N/A (Detection is based on behavior rather than specific port usage)
Severity: Critical
Incident: Abuse of Advanced Installer
Signature name: “Advanced Installer – Malicious Script Execution”
Internal checks:
  - Setting1: Monitor for the creation of suspicious batch and PowerShell scripts during software installation.
  - Setting2: Check for the abuse of Task Scheduler for unauthorized tasks.
  - Setting3: Detect and block the execution of known malicious PowerShell commands.
External scanning:
  - Monitor for DNS requests to known malicious domains (e.g., sysnod[.]duckdns[.]org).
  - Detect connections to known malicious IP addresses.

IoCs: 
- Domains: sysnod[.]duckdns[.]org
- IP Addresses: 104[.]244[.]76[.]183, 79[.]134[.]225[.]70, 79[.]134[.]225[.]124, 51[.]178[.]39[.]184
- Wallet Addresses: 
  - Ethereum Classic: 0xbEB015945E9Da17dD0dc9A4b316f8F3150d93352, 0xbCa8d14Df89cc74B158158E55FCaF5022a103795
  - FLUX (ZelHash): t1KHZ5Piuo4Ke7i6BXfU4, t1KHZ5Piuo4Ke7i6BXfU4A

By following these guidelines, organizations can better protect themselves against similar threats and minimize the risk of unauthorized cryptocurrency mining and other malicious activities.
