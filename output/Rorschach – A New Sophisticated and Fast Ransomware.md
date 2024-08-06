# Rorschach – A New Sophisticated and Fast Ransomware

### Incident: Rorschach Ransomware Attack

#### Root cause:
The Rorschach ransomware was deployed using DLL side-loading of a Cortex XDR Dump Service Tool, a signed commercial security product. This unconventional loading method allowed the ransomware to evade standard detection mechanisms.

#### Impact:
The exact number of devices or people impacted was not specified in the report. Similarly, financial losses were not detailed. However, given that the ransomware was deployed against a US-based company and considering the typical impact of ransomware, significant operational disruption and financial losses would be expected.

#### Mitigation:
To mitigate this type of attack, several steps should be taken:

1. **Security Patching and Updates:**
   - Ensure that all software, especially security tools like Cortex XDR, are updated with the latest patches to mitigate known vulnerabilities.
   
2. **Application Whitelisting:**
   - Implement application whitelisting to prevent unauthorized applications and software from executing.

3. **Endpoint Detection and Response (EDR):**
   - Deploy advanced EDR solutions that can detect unusual behaviors such as DLL side-loading and unauthorized encryption activities.

4. **Network Segmentation:**
   - Segment the network to limit the spread of ransomware and isolate critical systems.

5. **Regular Backups:**
   - Maintain regular, offline backups of critical data to ensure that recovery is possible without paying the ransom.

6. **User Training:**
   - Conduct regular training for employees to recognize phishing attempts and other social engineering tactics that could lead to ransomware deployment.

**Detailed Steps for mitigation:**
   1. **Update and Patch Management:**
      - Regularly update all software and apply patches promptly, focusing on critical applications and security tools.
   2. **Implement EDR Solutions:**
      - Deploy and configure EDR solutions to monitor and respond to abnormal activities, such as process injection and unauthorized encryption.
   3. **Network Segmentation:**
      - Use VLANs and firewalls to segment the network, ensuring that critical systems are isolated from general user systems.
   4. **Regular Backups and Testing:**
      - Perform regular backups of all critical data and store them offline. Regularly test the backups to ensure data integrity and restore capabilities.
   5. **User Awareness and Training:**
      - Conduct regular security awareness training for employees, focusing on phishing and ransomware threats.

#### Detection Signature:
   - **Service:** Cortex XDR Dump Service Tool
   - **Port:** Not specified (as the attack utilizes DLL side-loading within the host system)
   - **Severity:** Critical
   - **Incident:** Ransomware deployment via Cortex XDR side-loading
   - **Signature name:** “Ransomware side-loading detection”
   
**Internal checks:**
   - **Setting1:** Monitor for unauthorized use of Cortex XDR Dump Service Tool.
   - **Setting2:** Implement monitoring for DLL side-loading activities.
   - **Setting3:** Ensure Cortex XDR and other security tools are configured correctly and updated.

**External scanning:**
   - **Monitor for unusual file transfers:**
      - Regularly scan and monitor network traffic for unusual file transfers and execution patterns.

#### IoCs:
   - **cy.exe:** Hash: 2237ec542cdcd3eb656e86e43b461cd1 (benign file)
   - **winutils.dll:** Hash: 4a03423c77fe2c8d979caca58a64ad6c (Loader and injector)
   - **config.ini:** Hash: 6bd96d06cd7c4b084fe9346e55a81cf9 (Encrypted ransomware payload)

By following these mitigation and detection steps, organizations can better protect themselves against sophisticated ransomware attacks like Rorschach.
