# THREAT ANALYSIS From IcedID to Domain Compromise

**Incident: IcedID to Domain Compromise**

**Root cause:** Successful phishing campaign leading to IcedID infection

**Impact:** The analysis does not specify the number of records or devices impacted, or the exact financial losses. However, it details significant compromise of the Active Directory domain and potential widespread access to sensitive information.

**Mitigation:** 
1. **Secure the Email Gateway:**
   - Block or quarantine password-protected zip files.
   - Warn users against opening unusual files, especially ISO and LNK files.
   - Disable auto-mounting of disk image files via GPOs by modifying Windows Explorer file associations.

2. **Network and Host-Based Hardening:**
   - Identify and block malicious network connections to known bad domains.
   - Reset Active Directory access and reset the krbtgt account twice.
   - Isolate and re-image all infected machines to prevent further compromise.

3. **Incident Response and Recovery:**
   - Engage Incident Response teams to investigate thoroughly and patch vulnerabilities.
   - Cleanse compromised machines and ensure no lingering threats.

4. **Utilize Advanced Detection and Prevention Tools:**
   - Enable signature and AI modes on Cybereason NGAV.
   - Set Behavioral Execution Prevention (BEP) and Variant Payload Prevention to Prevent mode.

**Detection Signature:**
- **Service:** Windows (cmd.exe, rundll32.exe, regsvr32.exe, etc.)
- **Port:** N/A (various ports used for different services)
- **Severity:** Critical
- **Incident:** IcedID to Domain Compromise
- **Signature name:** “IcedID infection leading to domain compromise”
- **Internal checks:**
  - Setting1: Monitor for execution of cmd.exe, rundll32.exe, and regsvr32.exe with suspicious arguments.
  - Setting2: Monitor for the creation of scheduled tasks by rundll32.exe.
  - Setting3: Monitor for network connections to known malicious domains (e.g., crhonofire[.]info, blackleaded[.]tattoo).
- **External scanning:**
  - Monitor for traffic to known C2 domains.
  - Monitor for unusual network scanning activities (e.g., netscan.exe).

**IoCs:**  
- Domains: 
  - crhonofire[.]info
  - blackleaded[.]tattoo
  - curioasshop[.]pics
  - cerupedi[.]com
  - dimabup[.]com

- Files: 
  - dealing.bat
  - homesteading.dll
  - xaeywn1.dll
  - init_dll_64.dll
  - power.bat
  - PowerDEF.bat
  - 2.txt
  - 2.exe
  - cuaf.dll
  - gv.dll
  - db.dll

- Commands: 
  - net.exe, ping.exe, wmic.exe, nltest.exe
  - rundll32.exe with arguments referencing DLLs and "license.dat"
  - regsvr32.exe loading Cobalt Strike modules.

**No IoCs found for specific IP addresses or hashes.**
