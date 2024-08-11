Source: [https://us-cert.cisa.gov/ncas/alerts/aa23-025a](https://us-cert.cisa.gov/ncas/alerts/aa23-025a)

# AA23-025A Protecting Against Malicious Use of Remote Monitoring and Management Software

Incident: Malicious Use of Remote Monitoring and Management Software

Root cause: Phishing emails leading to the download of legitimate RMM software (ScreenConnect/AnyDesk)

Impact: Financial losses due to refund scams. Number of devices affected and specific financial losses are not provided in the document.

Mitigation: Implement the following detailed steps to mitigate the issue:
1. **Email Filtering**: Implement best practices to block phishing emails.
2. **Audit Remote Access Tools**: Identify authorized RMM software on the network.
3. **Log Review**: Review logs for execution of RMM software to detect abnormal use of portable executables.
4. **Security Software**: Use security software to detect instances of RMM software loaded only in memory.
5. **Application Controls**: Implement application controls to manage and control software execution, including allowlisting RMM programs.
6. **Network Restrictions**: Require authorized RMM solutions to be used only from within the network over approved remote access solutions like VPNs or VDIs.
7. **Port Blocking**: Block inbound and outbound connections on common RMM ports and protocols at the network perimeter.
8. **User Training**: Conduct user training and phishing exercises to raise awareness about suspicious websites, links, and attachments.
9. **Incident Response Planning**: Develop and regularly update incident response plans to address potential RMM misuse.

Detection Signature:
   - **Service**: AnyDesk, ScreenConnect
   - **Port**: Variable (depending on the configuration)
   - **Severity**: Critical
   - **Incident**: Malicious Use of RMM Software
   - **Signature name**: “Unauthorized RMM Software Usage”
   - **Internal checks**:
     - Setting1: Audit network for unauthorized RMM software installations.
     - Setting2: Log and monitor execution of RMM software.
     - Setting3: Ensure RMM software usage complies with corporate policies and is restricted to authorized personnel.
   - **External scanning**:
     - Detect unauthorized RMM software connections.
     - Identify uncommon or suspicious use of legitimate RMM tools.

IoCs: 
- win03[.]xyz
- myhelpcare[.]online
- win01[.]xyz
- myhelpcare[.]cc
- 247secure[.]us
