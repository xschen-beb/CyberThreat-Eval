# BIPClip Malicious PyPI Packages Target Crypto Wallet Recovery Passwords

**Incident**: BIPClip: Malicious PyPI packages target crypto wallet recovery passwords

**Root cause**: Malicious PyPI packages

**Impact**: Approximately 300, 997, 341, and 224 downloads respectively for the main packages, with a potential impact on various developers and crypto wallet users. The financial losses are indeterminate but could be significant considering the potential theft of cryptocurrency.

**Mitigation**: Strengthen software supply chain security, including regular security assessments of third-party tools and thorough vetting of software release artifacts. 
**Detailed Steps for mitigation**:
1. **Regular Audits**: Regularly audit third-party packages and dependencies for malicious code.
2. **Dependency Management**: Utilize tools that provide insights into the security of dependencies, such as dependency checkers and static analysis tools.
3. **Monitoring and Alerts**: Implement monitoring and alerting systems for unusual network activities, such as unexpected HTTP POST requests.
4. **Developer Training**: Educate developers on the risks of supply chain attacks and best practices for verifying the authenticity of packages.
5. **Access Control**: Restrict the use of high-risk open-source packages and enforce policies that require higher scrutiny for certain types of packages.
6. **Code Review**: Ensure comprehensive code reviews are conducted, focusing on dependencies and imported modules.
7. **Use of Trusted Repositories**: Only use packages from trusted repositories and maintain a whitelist of approved packages.

**Detection Signature**:
- **Service**: Python Package Index (PyPI)
- **Port**: Not applicable
- **Severity**: Critical
- **Incident**: BIPClip: Malicious PyPI packages targeting crypto wallet recovery passwords
- **Signature name**: “Malicious PyPI package detected”
- **Internal checks**:
  - **Setting1**: Ensure all dependencies are verified and scanned for malicious code.
  - **Setting2**: Monitor for unexpected HTTP POST requests originating from development environments.
  - **Setting3**: Implement stricter controls and reviews for packages related to cryptocurrency operations.
- **External scanning**:
  - **Indicator**: PyPI package names (e.g., mnemonic_to_address, bip39_mnemonic_decrypt)
  - **Indicator**: Network traffic analysis for Base64 encoded URLs and unexpected destinations.

**IoCs**:
- **PyPI packages**:
  - `jsBIP39-decrypt 1.0.0` (SHA1: a23db65079ef310b87d1f017742149addbb53a81)
  - `jsBIP39-decrypt 1.0.0` (SHA1: 03baa36c6551d1414d9907775b4600c873421b34)
  - `bip39-mnemonic-decrypt 1.0.0` (SHA1: 45130c7a2d92282ee9c0b066206f235198b5ddfb)
  - `bip39-mnemonic-decrypt 1.0.0` (SHA1: 087d325c24a5b28ad5342f097c3ebce3653e9ced)
  - `bip39-mnemonic-decrypt 1.0.1` (SHA1: 46d3a5b3627e7de58c78f41eed4c95c6112245e7)
  - `bip39-mnemonic-decrypt 1.0.1` (SHA1: f2aadcd5bd1ba46b056e2d9e4b53e21a18b61b2a)
  - `mnemonic_to_address 1.0.0` (SHA1: f6bb6216caf96246f07e3fd9ffcb5f0d83bd6f41)
  - `mnemonic_to_address 1.0.0` (SHA1: e50864e1db37a75b99596aea6538981991bf4915)
  - `mnemonic_to_address 1.2.7` (SHA1: a88802edce3d5e70ac2d79272f98c0891c793f2a)
  - `mnemonic_to_address 1.2.7` (SHA1: c3822c1f181d8f6f12325a00b5bd6cca0c18d124)
  - `mnemonic_to_address 1.2.8` (SHA1: c1dc8d26946d52a1014ccc6c02156449e8e1e3b6)
  - `mnemonic_to_address 1.2.8` (SHA1: b74c24938595fe4ccc6efe845d2b095d126ed3fc)
  - `erc20-scanner 1.0.0` (SHA1: 7ed9e234384e564e6d41da156bc472d5f369727e)
  - `erc20-scanner 1.0.0` (SHA1: ed1eb28a139c456e520726307e280a26b789b367)
  - `erc20-scanner 1.0.1` (SHA1: db61022dd75a63e99544bb5096c2e30d4348608e)
  - `erc20-scanner 1.0.1` (SHA1: 65dab94f5ba56b891ed9bfe20d2b1f21c2d00ee1)
  - `public-address-generator 1.0.0` (SHA1: 570e483dfdc6389e1d4a87f987c9b3e5a0d886ce)
  - `public-address-generator 1.0.0` (SHA1: 1619a6fce00eecf5946750ef47d1c5748e963456)
  - `public-address-generator 1.0.1` (SHA1: f4ff1fe54132ca91ecdf7f4b48fc16b231047b96)
  - `public-address-generator 1.0.1` (SHA1: a875e313026a5400a920767038d953398b4afcb6)
  - `public-address-generator 1.0.2` (SHA1: 4a39462ce7b3e2cda9998fb9fd42aeab3d5eb4a3)
  - `public-address-generator 1.0.2` (SHA1: 19d88ff3e9d32897becc33c07b4cc307871b426e)
  - `public-address-generator 1.0.3` (SHA1: 791e731b2db1551ccfc6df0990644ed405771aa6)
  - `public-address-generator 1.0.3` (SHA1: 9aa894169984cfb4835b01f5f5b49d9670818259)
  - `public-address-generator 1.1.1` (SHA1: dddd55a60d5dcbec45c034330fe12b62e38a87a8)
  - `public-address-generator 1.1.1` (SHA1: 3e385f6b2c842a490c1729aee1b48b22a728e367)
  - `public-address-generator 1.1.2` (SHA1: f2ed2e169bbe22aef73158e279e59d04a1f40ed9)
  - `public-address-generator 1.1.2` (SHA1: 633b858092f7e0eb435a73f5bc972baa4cf79452)
  - `public-address-generator 1.1.3` (SHA1: 3d82406f8e6ee1018bb39f6d40321940effeab2b)
  - `public-address-generator 1.1.3` (SHA1: c05d35c4cc9038de3eae4e84fb9b7560f4112a3b)
  - `hashdecrypt 1.0.0` (SHA1: 01b66f12e9f76342729c1260ff4f0da8fc1bbe01)
  - `hashdecrypt 1.0.0` (SHA1: d5400ef535a8effe8c23cb56c4cb1c2c569beb79)
  - `hashdecrypt 1.0.1` (SHA1: 156610fff622481eb3c37e988a5c8ece20f93aef)
  - `hashdecrypt 1.0.1` (SHA1: 3843c4add1c2960f280d07b047f0c780a7b65e4d)
  - `hashdecrypt 1.0.2` (SHA1: 9c4d2bacc24f70112bc53742e8fe26dad1fa63d1)
  - `hashdecrypt 1.0.2` (SHA1: 989276eb67d5179b5eda055390d850b47198cdd2)
  - `hashdecrypts 1.0` (SHA1: 64cd50f3bc347c894cbf25a2013c04e73e85550a)
  - `hashdecrypts 1.0` (SHA1: 206cd1758ceda4abc9622d4f50134444a639f925)

- **Command & Control infrastructure**:
  - `5.42.92.191`
  - `hxxps://raw.githubusercontent.com/HashSnake/backendapi/main/settings`
  - `194.163.154.242`
  - `knallos.de`
  - `65.109.70.235`

- **Malicious GitHub repository**:
  - `hxxps://github.com/HashSnake/hCrypto`
  - `https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#user-content-Abstract`


