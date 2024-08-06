# VMConnect Supply Chain Attack Continues, Evidence Points to North Korea

Incident: VMConnect Supply Chain Attack

Root cause: Malicious Python packages posted to PyPI (Python Package Index)

Impact: Potentially thousands of developers and organizations could be impacted due to the widespread use of the compromised packages. Financial losses could vary widely based on the extent of malware deployment and data theft within affected organizations.

Mitigation: 
1. **Remove Malicious Packages**: Immediately remove the identified malicious packages (tablediter, request-plus, and requestspro) from all projects and environments.
2. **Audit Dependencies**: Conduct a thorough audit of all dependencies in your projects to ensure no other malicious packages are present.
3. **Implement Package Verification**: Use tools to verify the integrity and authenticity of packages before incorporating them into your projects. Tools like Sigstore for signing and verifying software artifacts can be helpful.
4. **Enhance Detection Mechanisms**: Implement static and dynamic analysis tools that can detect obfuscated or hidden malicious code within packages.
5. **Update Security Policies**: Educate developers on the risks of typosquatting and ensure they follow best practices when selecting and installing packages from repositories.
6. **Monitor Network Traffic**: Set up network monitoring to detect unusual communications with C2 servers.

Detection Signature:
   - Service: Python Package Index (PyPI)
   - Port: N/A (relates to package repository and HTTP/HTTPS traffic)
   - Severity: Critical
   - Incident: VMConnect Supply Chain Attack
   - Signature name: “Malicious PyPI Package”
   - Internal checks:
       - Setting1: Verify integrity and source of all packages downloaded from PyPI.
       - Setting2: Ensure imported packages do not have hidden or obfuscated code.
       - Setting3: Monitor for unusual package behavior during runtime.
   - External scanning:
       - Check for known malicious package names (e.g., tablediter, request-plus, requestspro).
       - Monitor for unusual HTTP/HTTPS traffic patterns indicating C2 communication.

IoCs:
- **Command and control (C2) domains and IP address**:
  - packages-api.test
  - tableditermanaging.pro
  - 45.61.136.133

- **PyPI packages**:
  - **request-plus**
    - version 2.31.0
    - SHA1: 321363f11464208ee24e56a700ad5d26154df4bd
  - **requestspro**
    - version 2.2
    - SHA1: 5e026885bcf4b67993aefa4e992153f6d81c11da
    - version 2.3
    - SHA1: 049cc8d88a086c8fc69b51d76b6c0c4c2a66fa08
    - version 2.4
    - SHA1: bbb1e2ac1d243b8db922a23821de570702140145
    - version 2.5
    - SHA1: fdea182ffe7c04c28f28f88ceb9624732bb36bdc
    - version 2.6
    - SHA1: e3545b2c53c2cb8f012f0badc1bf452badfee341
  - **tablediter**
    - version 3.8.0
    - SHA1: 859f5b0af717fca9f890dcba0b87ac63be469033
    - SHA1: e063b210b50ca1426da45afa430d87c53b2ef5d2
    - version 3.8.1
    - SHA1: 39e9859f0cf85a0c8361e042e8316d4e185d1cfb
    - SHA1: b1880340818a1feda156abd272255bcc018f8bef
    - version 3.8.3
    - SHA1: 2c72edf29d5bca22525d612c94f1ee323c47be0c
    - SHA1: 9b8eefa1d7ee348c2b1b4c350028df5c2707c3d8
    - version 3.8.5
    - SHA1: aeeb445216a205abd770546dfa8d03f8b94515a1
    - SHA1: 89c05ecd388c5f168704c5a8e1d37f72a7f0f0f4
