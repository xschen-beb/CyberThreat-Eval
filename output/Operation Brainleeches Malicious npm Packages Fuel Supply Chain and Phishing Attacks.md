Source: [https://www.reversinglabs.com/blog/operation-brainleeches-malicious-npm-packages-fuel-supply-chain-and-phishing-attacks](https://www.reversinglabs.com/blog/operation-brainleeches-malicious-npm-packages-fuel-supply-chain-and-phishing-attacks)

# Operation Brainleeches Malicious npm Packages Fuel Supply Chain and Phishing Attacks

Incident: Operation Brainleeches: Malicious npm packages fuel supply chain and phishing attacks

Root cause: Malicious npm packages published to the npm open-source repository

Impact: Approximately 1,000 downloads of malicious packages. Potentially thousands of Microsoft 365 users targeted through phishing campaigns. Financial losses could include costs related to phishing scams, compromised accounts, and potential damages from supply chain attacks.

Mitigation: 
1. **Review and Audit Packages**:
   - Regularly audit npm packages before incorporating them into your projects.
   - Use tools that can analyze packages for malicious content and obfuscation.

2. **Implement Security Policies**:
   - Establish stringent policies for code reviews and the inclusion of third-party packages.
   - Use package-lock files to ensure consistent dependencies across environments.

3. **Use Advanced Security Tools**:
   - Employ tools like ReversingLabs A1000 and Software Supply Chain Security platforms for visibility into third-party code dependencies.
   - Enable runtime monitoring to detect unusual behavior in applications.

4. **Educate Developers**:
   - Train development teams on recognizing suspicious packages and the importance of scrutinizing package maintainers.
   - Educate on potential indicators of compromise and the importance of verifying package integrity.

Detection Signature:
Service: npm
Port: N/A (npm operates over HTTP/HTTPS ports)
Severity: Critical
Incident: Operation Brainleeches
Signature name: “Malicious npm packages”
Internal checks:
   - Setting1: Verify the package’s source and maintainer credibility.
   - Setting2: Check for obfuscated code in npm packages.
   - Setting3: Ensure dependencies are locked and consistent across environments.
External scanning:
   - Check for known malicious packages in the npm registry.
   - Monitor for abnormal download patterns of newly published packages.

IoCs:
   - Comm
