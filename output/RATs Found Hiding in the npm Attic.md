Source: [https://www.reversinglabs.com/blog/rats-found-hiding-in-the-npm-attic](https://www.reversinglabs.com/blog/rats-found-hiding-in-the-npm-attic)

# RATs Found Hiding in the npm Attic

Incident: Malicious npm Packages with TurkoRat

Root cause: Malicious npm packages containing TurkoRat malware

Impact: Approximately 1,200 downloads of malicious packages. The specific number of devices or people impacted and the financial losses are not specified in the document.

Mitigation: 
1. **Remove the malicious packages:** Ensure that the identified malicious packages (`nodejs-encrypt-agent` and `nodejs-cookie-proxy-agent`) are removed from all environments.
2. **Audit and validate dependencies:**
   - Regularly audit all npm packages and dependencies in use.
   - Validate package sources and verify the integrity of the packages.
3. **Use package whitelisting:** Implement a whitelisting process for npm packages to ensure only verified packages are used.
4. **Implement automated security tools:**
   - Utilize tools like ReversingLabs Software Supply Chain Security platform to analyze packages for suspicious behavior.
   - Integrate automated scanning tools into the CI/CD pipeline to detect and block malicious packages before they are deployed.
5. **Educate developers:**
   - Train developers on the risks of typosquatting and how to identify suspicious packages.
   - Encourage developers to carefully review package names, versions, and download statistics before use.

Detection Signature:
- **Service:** npm (Node Package Manager)
- **Port:** Not applicable (npm packages are downloaded via HTTPS)
- **Severity:** Critical
- **Incident:** Malicious npm Packages with TurkoRat
- **Signature name:** “TurkoRat npm Package Detection”
- **Internal checks:**
  - Setting1: Validate npm package names and versions against a trusted source.
  - Setting2: Use automated tools to analyze the behavior of npm packages before deployment.
  - Setting3: Implement strict access controls and monitoring for npm package installations.
- **External scanning:**
  - Monitor for known malicious package hashes.
  - Scan for unusual download patterns or newly published high-version-number packages.

IoCs: 
- **Malicious PE file found in nodejs-encrypt-agent:** `ef3ea4dc2d3ba466e40b8cc5e2b20cb026cf7936`
- **Malicious package hashes:**
  - `nodejs-encrypt-agent` version 6.0.2: `1a8a8fa87aff26fc2b269846f0f0d5be588bc6ee`
  - `nodejs-encrypt-agent` version 6.0.3: `99537ef2edffcebe6ebe88cc5d3d9420d397e89c`
  - `nodejs-encrypt-agent` version 6.0.4: `8093060aa8cea40a790ea0538c14bb11f3a02cd0`
  - `nodejs-encrypt-agent` version 6.0.5: `395d592b52c2947dd6bff455725a3c4204f41bb4`
  - `nodejs-cookie-proxy-agent` version 1.1.0: `d6e03a4023a3759cd28eb85c909bc17af4b78b7e`
  - `nodejs-cookie-proxy-agent` version 1.2.0: `a324176ef05a03a244220072f9f1eb168e4ffa89`
  - `nodejs-cookie-proxy-agent` version 1.2.1: `97d9fff201c71ef13bb1b2a7dcd442c59a94e5e0`
  - `nodejs-cookie-proxy-agent` version 1.2.2: `a4ac448a83865bbe7f62f5dad56143f1d5d0b526`
  - `nodejs-cookie-proxy-agent` version 1.2.3: `3576ccdd8fdde01a6d55c62f45aa8960a479ebee`
  - `nodejs-cookie-proxy-agent` version 1.2.4: `301088fc087f4ae61427a4515b3b822372a9d50f`
  - `axios-proxy` version 1.7.3: `aa02262de80a31b50efdf0a84c9915ca43696389`
  - `axios-proxy` version 1.7.4: `82ce0491e2415fa8ab8d75faa26adc2278855507`
  - `axios-proxy` version 1.7.7: `36f4b2e3d1f0e0e791e44178b41c9e53eb1898b5`
  - `axios-proxy` version 1.7.9: `61122f4857ae5c358cee5a79232b6f1b6213025a`
  - `axios-proxy` version 1.8.9: `c29938c79fd7fb0dcd3b646df136333e0ae62fda`
  - `axios-proxy` version 1.9.9: `ebb5b9d0d5416c5eaa0a3b00e9115ac7ed5839d6`

