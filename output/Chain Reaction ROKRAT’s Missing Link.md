Source: [https://research.checkpoint.com/2023/chain-reaction-rokrats-missing-link/](https://research.checkpoint.com/2023/chain-reaction-rokrats-missing-link/)

# Chain Reaction ROKRAT’s Missing Link

### Incident: ROKRAT Multi-Stage Infection Chains

#### Root cause:
Misconfigured permissions and lack of strict controls on LNK file execution.

#### Impact:
The incident primarily targeted South Korean government sectors, journalists, activists, and North Korean defectors. While exact financial losses are not specified, the leak and unauthorized access to sensitive information from these sectors could have significant geopolitical and security implications.

#### Mitigation:
- **Secure LNK file execution:** Implement policies to restrict execution of LNK files from untrusted sources.
- **Enhance Endpoint Protection:** Utilize advanced endpoint security solutions like Check Point's Harmony Endpoint to detect and block malicious scripts and executables.
- **Regular Security Awareness Training:** Educate users on the risks of opening LNK files from unknown sources.
- **Harden PowerShell Execution Policies:** Restrict the use of PowerShell scripts and only allow signed scripts to execute.
- **Deploy Threat Emulation Sandboxes:** Use sandboxes to analyze and detect malicious files before they reach end-users.

**Detailed Steps for Mitigation:**
1. **Implement Group Policies:**
   - Use Group Policy Objects (GPOs) to disable the execution of LNK files from untrusted locations.
   - Configure Windows Defender to block or warn about suspicious LNK files.
2. **Enable Script-Block Logging:**
   - Enable logging for script block execution in PowerShell to monitor and block malicious scripts.
3. **Use Application Whitelisting:**
   - Implement application whitelisting to allow only approved applications and scripts to run on endpoints.
4. **Regular Updates and Patching:**
   - Ensure all systems, especially those using Office applications and other common attack vectors, are regularly updated and patched.
5. **Deploy Network Segmentation:**
   - Use network segmentation to isolate critical systems and sensitive data from general network access.

#### Detection Signature:
- **Service:** PowerShell
- **Port:** N/A
- **Severity:** Critical
- **Incident:** ROKRAT Multi-Stage Infection Chains
- **Signature name:** “PowerShell-based multi-stage infection”
- **Internal checks:**
  - **Setting1:** PowerShell execution policy should be set to "AllSigned" or "Restricted" – In platform
  - **Setting2:** Monitor and alert on changes to PowerShell execution policies – Inside VMs
  - **Setting3:** Block execution of LNK files from untrusted sources via GPO – Inside VMs
- **External scanning:**
  - **Port:** N/A
  - **Indicators:** 
    - Large LNK files with embedded scripts
    - Unusual PowerShell command executions

#### IoCs:
**File Hashes:**
- 1c5b9409243bfb81a5924881cc05f63a301a3a7ce214830c7a83aeb2485cc5c3
- cb4c7037c7620e4ce3f8f43161b0ec67018c09e71ae4cea3018104153fbed286
- 240e7bd805bd7f2d17217dd4cebc03ac37ee60b7fb1264655cfd087749db647a
- 12ecabf01508c40cfea1ebc3958214751acfb1cd79a5bf2a4b42ebf172d7381b
- 00d88009fa50bfab849593291cce20f8b2f2e2cf2428d9728e06c69fced55ed5
- 6753933cd54e4eba497c48d63c7418a8946b4b6c44170105d489d29f1fe11494
- 732fca9be66ba2c40c5d05845540207b9e1480e609d767aff63895bf49d33a81
- eb03f8b8e41b3ad27ccdecb092111e2c3c010436ad59add42755e2af04762b67
- 050c65d45e5f21018aa940f0188c4aa1318ac3df865d901f8643ed7ce4a4b52c
- 5a3f1d14b9cc4890db64fbc41818d7039f25b0120574dcdec4e20d13e6b2740c
- c4029a2f1d0c07ae2b388b5a4076fba41e57af0dd0d2d0f86844464f22d63861
- 17399.zip
- 9a4c61cdf0e291dc364c568aa161f744f59065efeafc72a3f892e12cbf88fc5b
- 0e926d8b6fbf6f14a2a19d4d4af843253f9f5f6de337956a12dde279f3321d78
- 6234ef67435dfcb65bd661b5f3bb0b77b82fe6cdd2109b6dfb9dea1b65a17d5d
- 479894be4c5dec0992ad3c5b21fb1423643996d80d59dcca76386bb325dc811e
- c5c05f9df89fc803884fed2bd20a3824eae95eeb34a1827bf5210e4ac17beadd
- 70f9216f0c5badb24120f74270dbbc5100b07c4fc6eb45f6652b00882290a73c
- 3252345b2640efc44cdd98667dbd25806ee2316d1e01eec488fd678e885aa960
- 1e0b5d6b85fca648061fdaf2830c5a90248519e81e78122467c29beeb78daa1e
- f92297c4efabba98befeb992a009462d1aba6f3c3a11210a7c054ff5377f0753
- 06431a5d8f6262cc3db39d911a920f793fa6c648be94daf789c11cc5514d0c3d

**URLs:**
- hxxps[://]api[.]onedrive[.]com/v1[.]0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3UvcyFBaFFNUDZlZzhhUkZiN0xVMUNPQ2YzeE5vVFU_ZT1wZ2liaUM/root/content
- hxxps[://]api[.]onedrive[.]com/v1[.]0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3UvcyFBdTJteTF4aDZ0OFhkSUpseW14b21abFd2WW8_ZT15SjJTSkk/root/content
- hxxps[://]api[.]onedrive[.]com/v1[.]0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3UvcyFBdTJteTF4aDZ0OFhnUjJNem1zOG5oUndvLTZCP2U9akhIQzZ5/root/content
- hxxps[://]api[.]onedrive[.]com/v1[.]0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3UvcyFBalFOTHZFRV9DVU9iUFdnLXhPZG8xRXFYckU_ZT1BM1QwV2Q/root/content
- hxxps[://]api[.]onedrive[.]com/v1[.]0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL2kvcyFBaFhFWExKU05NUFRiZnpnVU14TmJJbkM2Q0k_ZT1WZElLSjE/root/content
- hxxps[://]1erluw[.]bl[.]files[.]1drv[.]com/y4mjq91jEOFfIt8XWokhkvDA3nd2tPKC9x6YXe5KPoia1IoxaHAT0f4N[...]8IqzILVZkrM48fYGI1jkeYjBkceuEgARw-IRenUX4NuenWy_g/my[.]jpg
- hxxps[://]u9izog[.]dm[.]files[.]1drv[.]com/y4mKSGc6jShxeCkGYNOnZdeG42N9DXsT4dFh5t6umtqb8bI9VePGNlZG7GP_-K9ly6IW0xeiUqMR8o6Sk9pGqnPraGVk-PxQce9pcUKcGPoKvXYaPqoiBNLDb3KK94OjeEV0RiejfEGjZ1ccTQqeWZZ0_DnN4T5NGFZRCkc4ZvlJERfXrb5JgWm1U3gC4leSiTrTtV12NtA3UrdgsHv46eCoQ/AutumnPark
- hxxps[://]qb3oaq[.]bl[.]files[.]1drv[.]com/y4mHRkXCvSNkEazYL8KsgjxXW3y4EfgcyTsS_t5Wi6fefz383ova6apylWD0q0dsmeV2UbuXHYDd_IbfVazPybUB72j-fJ8cPvgLhX1dYRSVWpxXnpKq1GiHngnCioOASAeaS33ztlC74MpGEWsDuNksijGCqmtnIelhg-FBefDcwLwqsbCH01dRolRMhazBj1ZxYizw_CyFwdRbApbmUCNOQ/dragon32[.]zip
- hxxps[://]link[.]b4a[.]app/download[.]html?search=cHJvamVjdHMgaW4gTGlieWEuemlw
- hxxps[://]docx1[.]b4a[.]app/download[.]html?id=88&search=tuh3m0xez3npqzr4terfd2zhsnzasgt1zedgawjhvxflazkwyudwewzieglimli1tg5safltegw=
- hxxps[://]naver-file[.]com/download/list[.]php?q=e1&18467=41

**Domains:**
- link[.]b4a[.]app
- docx1[.]b4a[.]app
- naver-file[.]com
- nate-download[.]com
- daum-store[.]com
- naver-storage[.]com
