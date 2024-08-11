Source: [https://www.welivesecurity.com/en/eset-research/sponsor-batch-filed-whiskers-ballistic-bobcats-scan-strike-backdoor/](https://www.welivesecurity.com/en/eset-research/sponsor-batch-filed-whiskers-ballistic-bobcats-scan-strike-backdoor/)

# Ballistic Bobcat’s Scan and Strike Backdoor

### Incident: Sponsoring Access Campaign by Ballistic Bobcat 

**Root cause:** Exploitation of known vulnerabilities in internet-exposed Microsoft Exchange servers (CVE-2021-26855).

**Impact:** 34 victims, primarily in Israel, with additional victims in Brazil and the UAE. The incident affected various sectors including healthcare, financial services, automotive, and telecommunications. The specific financial losses were not detailed in the report.

**Mitigation:** 
1. **Patch Management:**
   - Ensure all Microsoft Exchange servers are up to date with the latest security patches, particularly CVE-2021-26855.
2. **Network Segmentation:**
   - Segment critical systems and services to limit exposure to potential attackers.
3. **Access Controls:**
   - Implement strict access controls and multi-factor authentication (MFA) for sensitive systems.
4. **Monitoring and Logging:**
   - Enable detailed logging and continuous monitoring of systems for unusual activities.
5. **Incident Response Plan:**
   - Develop and regularly update an incident response plan tailored to address APT threats and backdoor infections.

**Detailed Steps for Mitigation:**

1. **Patch Microsoft Exchange Servers:**
   - Identify all Microsoft Exchange servers in your network.
   - Download and apply the latest patches from the official Microsoft website.
   - Verify that the patches have been successfully applied.

2. **Implement Network Segmentation:**
   - Use VLANs and firewalls to separate critical systems from less sensitive ones.
   - Limit communication between segments to only what is necessary for business operations.

3. **Strengthen Access Controls:**
   - Enforce strong password policies.
   - Implement MFA for all remote access and administrative accounts.
   - Regularly review and update access permissions to ensure minimal access necessary.

4. **Enhance Monitoring and Logging:**
   - Deploy SIEM (Security Information and Event Management) solutions to centralize and analyze logs.
   - Implement real-time alerting for suspicious activities, especially related to command and control traffic.
   - Regularly review logs and conduct threat hunting exercises.

5. **Develop and Test Incident Response Plan:**
   - Establish an incident response team and define roles and responsibilities.
   - Create playbooks for common attack scenarios, including backdoor infections.
   - Regularly conduct drills and tabletop exercises to ensure readiness.

**Detection Signature:**

- **Service:** Microsoft Exchange Server
- **Port:** 443 (typically used for HTTPS)
- **Severity:** Critical
- **Incident:** Sponsoring Access Campaign
- **Signature name:** “Microsoft Exchange Server CVE-2021-26855 Exploitation”
  - **Internal checks:**
    - Setting1: Exchange server should have the latest security patches applied.
    - Setting2: Limit exposure of Exchange server to the public internet.
    - Setting3: Enable and monitor detailed logging on Exchange server.
  - **External scanning:**
    - Port (443) open
    - Known vulnerability CVE-2021-26855 not patched

**IoCs (Indicators of Compromise):**

- **Files:**
  - SHA-1: 098B9A6CE722311553E1D8AC5849BA1DC5834C52 (Sponsor v1)
  - SHA-1: 5AEE3C957056A8640041ABC108D0B8A3D7A02EBD (Sponsor v2)
  - SHA-1: 764EB6CA3752576C182FC19CFF3E86C38DD51475 (Sponsor v3)
  - SHA-1: 2F3EDA9D788A35F4C467B63860E73C3B010529CC (Sponsor v4)
  - SHA-1: E443DC53284537513C00818392E569C79328F56F (Sponsor v5, aka Alumina)
  - SHA-1: C4BC1A5A02F8AC3CF642880DC1FC3B1E46E4DA61 (RevSocks)
  - SHA-1: 39AE8BA8C5280A09BA638DF4C9D64AC0F3F706B6 (ProcDump)
  - SHA-1: A200BE662CDC0ECE2A2C8FC4DBBC8C574D31848A (Mimikatz)
  - SHA-1: 5D60C8507AC9B840A13FFDF19E3315A3E14DE66A (GOST)
  - SHA-1: 50CFB3CF1A0FE5EC2264ACE53F96FADFE99CC617 (Chisel)
  - SHA-1: 1AAE62ACEE3C04A6728F9EDC3756FABD6E342252 (Host2IP)
  - SHA-1: 519CA93366F1B1D71052C6CE140F5C80CE885181 (RevSocks with Enigma Protector)
  - SHA-1: 4709827C7A95012AB970BF651ED5183083366C79 (Plink)
  - SHA-1: 99C7B5827DF89B4FAFC2B565ABED97C58A3C65B8 (WebBrowserPassView)
  - SHA-1: E52AA118A59502790A4DD6625854BD93C0DEAF27 (SQLDump)

- **File paths:**
  - %SYSTEMDRIVE%\inetpub\wwwroot\aspnet_client\
  - %USERPROFILE%\AppData\Local\Temp\file\
  - %USERPROFILE%\AppData\Local\Temp\2\low\
  - %USERPROFILE%\Desktop\
  - %USERPROFILE%\Downloads\a\
  - %WINDIR%\
  - %WINDIR%\INF\MSExchange Delivery DSN\
  - %WINDIR%\Tasks\
  - %WINDIR%\Temp\
  - %WINDIR%\Temp\crashpad\1\Files

- **Network IPs:**
  - 162.55.137[.]20
  - 37.120.222[.]168
  - 198.144.189[.]74
  - 5.255.97[.]172

No other IoCs found in the document.
