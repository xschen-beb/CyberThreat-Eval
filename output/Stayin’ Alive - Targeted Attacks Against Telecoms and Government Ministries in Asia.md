# Stayin’ Alive - Targeted Attacks Against Telecoms and Government Ministries in Asia

### Incident: Stayin’ Alive - Targeted Attacks Against Telecoms and Government Ministries in Asia

**Root Cause:** 
Exploitation of DLL side-loading vulnerability in Audinate’s Dante Discovery software (CVE-2022-23748). The primary vector involved spear-phishing emails delivering malicious archive files containing DLL side-loading schemes.

**Impact:**
The campaign has been active since at least 2021, primarily targeting the Telecom industry and government organizations in countries such as Kazakhstan, Uzbekistan, Pakistan, and Vietnam. The exact number of devices or people impacted is not disclosed in the blog, nor are the financial losses specified.

**Mitigation:**
1. **Patch Management:**
   - Ensure all software is up-to-date, including applying patches for known vulnerabilities such as CVE-2022-23748 in Audinate’s Dante Discovery software.

2. **Email Filtering and User Training:**
   - Implement advanced email filtering to block spear-phishing attempts.
   - Conduct regular user training to recognize and report phishing emails.

3. **Application Whitelisting:**
   - Use application whitelisting to prevent unauthorized execution of software.

4. **Endpoint Protection:**
   - Deploy advanced endpoint protection solutions, such as Check Point Harmony Endpoint and Threat Emulation, to detect and block malicious activities.

5. **Segregation of Duties:**
   - Limit permissions and access rights to minimize the impact of any potential compromise.

**Detection Signature:**
```plaintext
Service: Audinate’s Dante Discovery software
Port: N/A (exploitation does not rely directly on a specific port)
Severity: Critical
Incident: DLL side-loading exploitation
Signature name: “DLL side-loading exploitation in Dante Discovery”
Internal checks:
    - Setting1: Ensure the software version is up-to-date and patched for CVE-2022-23748.
    - Setting2: Monitor for unauthorized DLL loading activities.
    - Setting3: Enforce strict application execution policies.
External scanning:
    - Indicator of spear-phishing campaigns targeting the organization.
    - Monitor for communications to known malicious C&C servers.
```

**IoCs:**
- **Files:**
  - CurLu: `6eaa33812365865512044020bc4b95079a1cc2ddc26cdadf24a9ff76c81b1746`
  - CurKeep payload: `295b99219d8529d2cd17b71a7947d370809f4e1a3094a74a31da6e30aa39e719`
  - CurLog: `409948cbbeaf051a41385d2e2bc32fc1e59789986852e608124b201d079e5c3c`
  - CurCore: `451f87134438fa7e5735a865989072e7bab4858ca0b1e921224ed27dea0226b0`

- **IPs:**
  - `70.34.201.229`
  - `185.136.163.129`
  - `45.77.171.170`
  - `167.179.91.150`

- **Domains:**
  - `ns01.nayatel.orinafz.com`
  - `eaq.machineaccountquota.com`
  - `admit.pkigoscorp.com`
  - `update.certexvpn.com`

This detailed analysis provides a comprehensive understanding of the root cause, detection methods, and steps for mitigating the "Stayin’ Alive" campaign.
