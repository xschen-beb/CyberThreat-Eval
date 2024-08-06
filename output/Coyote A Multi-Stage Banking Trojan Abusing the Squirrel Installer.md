# Coyote A Multi-Stage Banking Trojan Abusing the Squirrel Installer

Incident: Coyote Banking Trojan

Root cause: Abuse of the Squirrel installer for initial infection vector, combined with Node.js and Nim loaders for multi-stage malware deployment.

Impact: The blog doesn't specify the number of devices or people impacted, nor the financial losses. However, it mentions that the malware targets users of more than 60 banking institutions, mainly from Brazil, and that up to 90% of infections originated from Brazil.

Mitigation: 
1. **Secure the Squirrel Installer:**
   - Ensure only authorized and signed installers are allowed.
   - Monitor and audit the installation pipeline for suspicious activities.
2. **Harden Node.js and Nim environments:**
   - Regularly update Node.js and Nim libraries and ensure they are sourced from trusted repositories.
   - Implement runtime application self-protection (RASP) to detect and block malicious code execution.
3. **Enhance Endpoint Security:**
   - Deploy advanced endpoint protection solutions capable of detecting and blocking multi-stage malware.
   - Enable behavioral analysis in endpoint security solutions to detect unusual activities such as DLL sideloading.
4. **Improve User Awareness:**
   - Educate users about the risks of downloading and executing installers from untrusted sources.
   - Encourage vigilance regarding unexpected software updates or installations.

Detection Signature:
   Service: Node.js, Nim
   Port: N/A (primarily file and process-based detection)
   Severity: Critical
   Incident: Coyote Banking Trojan
   Signature name: “Coyote multi-stage malware”
   Internal checks:
       - Setting1: Ensure that only authorized Squirrel installations are executed.
       - Setting2: Monitor for Node.js processes executing obfuscated JavaScript code.
       - Setting3: Detect the presence of Nim-based loaders and unpacked .NET executables in memory.
   External scanning:
       - Unusual network traffic patterns associated with command and control (C2) domains.
       - SSL connections with mutual authentication to suspicious or unknown servers.

IoCs: 
Host-based (MD5 hash):
   - 03eacccb664d517772a33255dff96020
   - 071b6efd6d3ace1ad23ee0d6d3eead76
   - 276f14d432601003b6bf0caa8cd82fec
   - 5134e6925ff1397fdda0f3b48afec87b
   - bf9c9cc94056bcdae6e579e724e8dbbd

C2 domain list:
   - atendesolucao[.]com
   - servicoasso[.]com
   - dowfinanceiro[.]com
   - centralsolucao[.]com
   - traktinves[.]com
   - diadaacaodegraca[.]com
   - segurancasys[.]com
