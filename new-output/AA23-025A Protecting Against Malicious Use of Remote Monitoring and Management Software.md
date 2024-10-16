Source: [https://us-cert.cisa.gov/ncas/alerts/aa23-025a](https://us-cert.cisa.gov/ncas/alerts/aa23-025a)

# AA23-025A Protecting Against Malicious Use of Remote Monitoring and Management Software

# Enriched Doc (enrihcments marked with *content*(link)): 
 markdown: Incident: Malicious Use of Remote Monitoring and Management Software

Root cause: The incident was caused by cybercriminals using legitimate Remote Monitoring and Management (RMM) software, specifically ScreenConnect (now ConnectWise Control) and AnyDesk, to gain unauthorized access to victim systems. This was facilitated through a phishing campaign tricking victims into downloading and executing the RMM software.

Threat Actor/group/campaign: Cybercriminal actors; potentially selling access to other cybercriminals or advanced persistent threat (APT) actors.

Organization/industry/location: Federal civilian executive branch (FCEB) networks and potentially other victims targeted through phishing campaigns. *The National Security Agency (NSA) and Multi-State Information Sharing and Analysis Center (MS-ISAC) are also involved* (https://www.infosecurity-magazine.com/news/cisa-warns-malicious-use-rmm/).

Start date – End date: Since at least June 2022; identified in October 2022.

*Technical Details*: In June 2022, EINSTEIN IDS identified suspected malicious activity on two FCEB networks *using trusted third-party reporting* (https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-025a).

MITRE TTPs:
- T1078: Valid Accounts
- T1071: Application Layer Protocol
- T1219: Remote Access Software

Impact: Financial losses due to refund scams, potential unauthorized access to sensitive information, and potential misuse of victim accounts.

Mitigation:
- Implement best practices to block phishing emails.
- Audit remote access tools on your network to identify authorized RMM software.
- Review logs for execution of RMM software to detect abnormal use.
- Use security software to detect instances of RMM software only being loaded in memory.
- Implement application controls to manage and control execution of software, including allowlisting RMM programs.
- Require authorized RMM solutions to be used from within your network over approved remote access solutions, such as VPNs or VDIs.
- Block both inbound and outbound connections on common RMM ports and protocols at the network perimeter.
- Implement a user training program and phishing exercises to raise awareness among users about the risks of visiting suspicious websites, clicking on suspicious links, and opening suspicious attachments. *Alessandro Mascellino emphasized the need for stronger anti-phishing controls and cybersecurity awareness* (https://www.infosecurity-magazine.com/news/cisa-warns-malicious-use-rmm/).

Detection Signature:
Service: ScreenConnect (now ConnectWise Control), AnyDesk
Port: Varies based on configuration
Severity: Critical
Incident: Malicious Use of RMM Software
Signature name: “Unauthorized RMM Software Execution”
Internal checks:
- Setting1: Audit for unauthorized RMM software on endpoints.
- Setting2: Monitor for execution of portable executables that match known RMM software.
- Setting3: Ensure RMM software usage is within policy and only executed from authorized sources.
External scanning:
- Port scanning for common RMM software ports.
- Detection of anomalous RMM software usage patterns.

IoCs:
- win03[.]xyz
- myhelpcare[.]online (observed on June 14, 2022)
- win01[.]xyz
- myhelpcare[.]cc
- 247secure[.]us

*Note*: Portable executables bypass controls and risk management assumptions by not requiring administrative privileges *(https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-025a)*.

*Additional Context*: Silent Push identified related malicious typosquatting activity involving Amazon, Microsoft, Geek Squad, McAfee, Norton, and PayPal domains *(https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-025a)*. *Mike Walters from Action1 highlighted detecting hackers' misuse of RMM solutions* (https://www.infosecurity-magazine.com/news/cisa-warns-malicious-use-rmm/). 


# Related articles (describing the same threat) 
['https://us-cert.cisa.gov/ncas/alerts/aa23-025a', 'https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-025a', 'https://www.infosecurity-magazine.com/news/cisa-warns-malicious-use-rmm/']
