Source: [https://www.sentinelone.com/labs/icefire-ransomware-returns-now-targeting-linux-enterprise-networks/](https://www.sentinelone.com/labs/icefire-ransomware-returns-now-targeting-linux-enterprise-networks/)

# IceFire Ransomware Returns  Now Targeting Linux Enterprise Networks

**Incident:** IceFire Ransomware Returns Targeting Linux Enterprise Networks

**Root cause:** Exploitation of CVE-2022-47986, a deserialization vulnerability in IBM Aspera Faspex file sharing software.

**Impact:** Multiple media and entertainment sector organizations worldwide were impacted, specifically in Turkey, Iran, Pakistan, and the United Arab Emirates. The exact number of devices/people impacted and financial losses are not specified in the document.

**Mitigation:** 
1. **Patch Vulnerable Software:** Immediately apply the latest security patches for IBM Aspera Faspex to mitigate CVE-2022-47986.
2. **Network Segmentation:** Isolate critical systems and sensitive data to limit the spread of ransomware.
3. **Endpoint Security:** Deploy advanced endpoint protection solutions capable of detecting and responding to ransomware threats.
4. **Regular Backups:** Ensure regular, secure backups of critical data to enable recovery in case of an attack.
5. **Access Controls:** Implement strict access controls and least privilege principles to reduce the attack surface.
6. **Security Training:** Conduct regular security awareness training for employees to recognize and avoid phishing attempts and other common infection vectors.

**Detection Signature:**
- **Service:** IBM Aspera Faspex
- **Port:** 8080 (as observed in the payload URL)
- **Severity:** Critical
- **Incident:** IceFire Ransomware targeting Linux
- **Signature name:** “Aspera Faspex CVE-2022-47986 exploitation”
  
  **Internal checks:**
  - Setting1: IBM Aspera Faspex should be running the latest security patches.
  - Setting2: Limit exposure of Aspera Faspex to the public internet where possible.
  - Setting3: Enable strong authentication mechanisms for accessing Aspera Faspex.

  **External scanning:**
  - Port (8080) open on systems running IBM Aspera Faspex
  - Detection of known exploitation attempts for CVE-2022-47986

**IoCs:**
- **SHA-1:** b676c38d5c309b64ab98c2cd82044891134a9973
- **Payload URLs:**
  - hxxp[://]159.65.217.216:8080/demo

**No additional IoCs found.**
