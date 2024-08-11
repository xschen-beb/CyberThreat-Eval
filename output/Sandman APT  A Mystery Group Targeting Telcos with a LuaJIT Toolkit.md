Source: [https://www.sentinelone.com/labs/sandman-apt-a-mystery-group-targeting-telcos-with-a-luajit-toolkit/](https://www.sentinelone.com/labs/sandman-apt-a-mystery-group-targeting-telcos-with-a-luajit-toolkit/)

# Sandman APT  A Mystery Group Targeting Telcos with a LuaJIT Toolkit

Incident: Sandman APT | A Mystery Group Targeting Telcos with a LuaJIT Toolkit

Root cause: Misconfigured or unprotected Windows services (Fax and Spooler) allowing DLL hijacking

Impact: The blog does not specify the exact number of records or devices affected, nor does it provide details on financial losses. However, it mentions targeted workstations in telecommunications providers across the Middle East, Western Europe, and South Asia.

Mitigation: Secure Windows services and applications to prevent DLL hijacking.
**Detailed Steps for Mitigation:**
1. **Audit DLLs:**
   - Regularly audit and monitor DLLs loaded by critical services such as Fax and Spooler.
   - Use tools like Sysinternals Process Monitor to track DLL loading.
   
2. **Apply Patches:**
   - Ensure that all Windows services, especially Fax and Spooler, are updated with the latest security patches.

3. **Restrict Service Permissions:**
   - Limit the permissions of services to only necessary operations.
   - Use Group Policy to enforce service-specific security settings.

4. **Implement Code Signing:**
   - Enforce code signing for all DLLs to ensure only trusted DLLs are loaded.

5. **Enable Windows Defender Exploit Guard:**
   - Utilize features like Controlled Folder Access to prevent unauthorized changes to key directories.

6. **Monitor and Alert:**
   - Set up monitoring and alerting for any unauthorized DLL loads or changes to service configurations.
   - Use SIEM tools to correlate suspicious activities and alert security teams in real-time.

Detection Signature:
   Service: Windows Fax and Spooler Services
   Port: Not applicable (focus on service configuration)
   Severity: Critical
   Incident: Sandman APT
   Signature name: “DLL Hijacking in Windows Services”
   Internal checks:
      - Setting1: Ensure only trusted DLLs are loaded by the Fax and Spooler services – In platform
      - Setting2: Monitor for unauthorized changes in service configurations – Inside VMs
      - Setting3: Implement and enforce code signing for DLLs – Inside VMs
   External scanning:
      - Scan for unauthorized or suspicious DLLs in system directories
      - Check for anomalies in service behavior

IoCs:
   - SHA1 File names:
     1cd0a3dd6354a3d4a29226f5580f8a51ec3837d4 (fax.dat)
     27894955aaf082a606337ebe29d263263be52154 (fax.Application)
     5302c39764922f17e4bc14f589fa45408f8a5089 (ualapi.dll)
     77e00e3067f23df10196412f231e80cec41c5253 (fax.cache)
     b9ea189e2420a29978e4dc73d8d2fd801f6a0db2 (UpdateCheck.dll)
     fb1c6a23e8e0693194a365619b388b09155c2183 (updater.ver)
     ff2802cdbc40d2ef3585357b7e6947d42b875884 (fax.module)

   - File paths:
     %ProgramData%\FaxConfig
     %ProgramData%\FaxLib

   - C2 Server Domains:
     mode.encagil[.]com
     ssl.explorecell[.]com

   - IP addresses associated with C2 domains:
     185.82.218[.]230 (Bulgaria, ITLDC hosting provider)
     172.67.173[.]208 (Cloudflare)
     104.21.47[.]226 (Cloudflare)
