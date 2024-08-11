Source: [https://research.checkpoint.com/2023/dotrunpex-demystifying-new-virtualized-net-injector-used-in-the-wild/](https://research.checkpoint.com/2023/dotrunpex-demystifying-new-virtualized-net-injector-used-in-the-wild/)

# DotRunpeX - Demystifying New Virtualized .NET Injector Used in the Wild

### Incident: DotRunpeX Injector Analysis

#### Root cause: Vulnerability in Process Explorer Driver and Misconfigured Anti-Malware Services

#### Impact:
- Devices: Targeted systems running various versions of Windows with .NET framework.
- People: Users who downloaded malicious attachments or visited compromised websites.
- Financial losses: Potential losses due to data theft, ransomware, and productivity loss. Specific financial impacts not detailed.

#### Mitigation: 
1. **Secure Anti-Malware Services:**
   - Ensure Anti-Malware services run with the highest privilege and are configured to prevent unauthorized termination.
   - Regularly update Anti-Malware software to the latest versions to patch known vulnerabilities.

2. **Patch Vulnerabilities in Process Explorer:**
   - Ensure usage of the latest versions of Process Explorer to avoid exploitation of known vulnerabilities.
   - Disable or remove outdated drivers that are not in use or known to be vulnerable.

3. **Implement Multi-Layered Security:**
   - Deploy email security solutions to filter out phishing emails.
   - Utilize web filtering solutions to block access to malicious websites.

4. **Strengthen Authentication Mechanisms:**
   - Use strong, unique passwords and enable multi-factor authentication (MFA) for critical systems.

5. **Regular Security Audits:**
   - Conduct regular security audits to detect misconfigurations and vulnerabilities.
   - Use penetration testing to identify and mitigate potential attack vectors.

6. **User Education:**
   - Train users on recognizing phishing attempts and avoiding suspicious downloads.

**Detailed Steps for Mitigation:**
1. **Update Process Explorer Driver:**
   - Uninstall the vulnerable version of Process Explorer.
   - Download and install the latest version from the official Microsoft website.
   - Verify the version number to ensure it is not vulnerable.

2. **Secure Anti-Malware Configurations:**
   - Access the configuration settings of your Anti-Malware software.
   - Enable tamper protection to prevent unauthorized changes.
   - Configure the Anti-Malware processes to run with the highest privileges.
   - Ensure the software is set to auto-update to receive the latest security patches.

3. **Deploy Email and Web Filters:**
   - Implement an email security gateway that scans and filters incoming emails for malicious attachments and links.
   - Configure web filtering software to block access to known malicious websites and categories.

4. **Implement MFA:**
   - Enable MFA for all user accounts, especially those with administrative access.
   - Ensure MFA solutions are compatible with your existing authentication systems.

5. **Conduct Security Audits:**
   - Schedule regular security audits and vulnerability assessments.
   - Use automated tools to scan for misconfigurations and vulnerabilities.
   - Review audit results and take corrective actions promptly.

#### Detection Signature:
**Service: Process Explorer Driver (procexp.sys)**  
**Port: Not applicable (local service)**  
**Severity: Critical**  
**Incident: Unauthorized termination of Anti-Malware services**  
**Signature name: "Procexp driver exploitation"**  
**Internal checks:**
  - Setting1: Ensure Anti-Malware services are running with the highest privileges.
  - Setting2: Verify Anti-Malware services cannot be terminated by unauthorized users.
  - Setting3: Confirm Process Explorer driver is up-to-date and not vulnerable.
**External scanning:**
  - Detect presence of outdated Process Explorer driver.
  - Check for unauthorized termination attempts of Anti-Malware services.

#### IoCs:
- IPs: Not provided
- Domains: 
  - www.galaxyswapper[.]ru
  - gitlab[.]com/forhost1232/galaxyv19.11.14/-/raw/main/GalaxyV19.11.14.zip
  - lastpass[.]shop/en/
  - gitlab[.]com/forhost1232/lastpassinstaller/-/raw/main/LastPassInstaller.zip
  - gitlab[.]com/forhost1232
- Hashes:
  - 457cfd6222266941360fdbe36742486ee12419c95f1d7d350243e795de28200e (example phishing attachment)
  - 0e40e504c05c30a7987785996e2542c332100ae7ecf9f67ebe3c24ad2468527c (trojanized Redline builder)
  - Numerous hashes for various malware families delivered by dotRunpeX as listed in the detailed analysis.

#### Yara Rules:
- [Yara rules provided in the document for detection of dotRunpeX samples]

#### References:
- KoiVM protector: [GitHub](https://github.com/yck1509/KoiVM)
- Reflection in .NET: [Microsoft Documentation](https://learn.microsoft.com/en-us/dotnet/framework/reflection-and-codedom/reflection)
- P/Invoke: [Microsoft Documentation](https://learn.microsoft.com/en-us/dotnet/standard/native-interop/pinvoke)
- D/Invoke: [GitHub](https://github.com/TheWover/DInvoke)
- Backstab: [GitHub](https://github.com/Yaxser/Backstab)
- MinHook: [GitHub](https://github.com/TsudaKageyu/minhook)
- ClrMD: [GitHub](https://github.com/microsoft/clrmd)
- AsmResolver: [GitHub](https://github.com/Washi1337/AsmResolver)
- OldRod: [GitHub](https://github.com/Washi1337/OldRod)
