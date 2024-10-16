Source: [https://www.reversinglabs.com/blog/bipclip-malicious-pypi-packages-target-crypto-wallet-recovery-passwords](https://www.reversinglabs.com/blog/bipclip-malicious-pypi-packages-target-crypto-wallet-recovery-passwords)

# BIPClip Malicious PyPI Packages Target Crypto Wallet Recovery Passwords

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: BIPClip: Malicious PyPI packages target crypto wallet recovery passwords 

 Root cause: The root cause includes the use of malicious PyPI packages masquerading as legitimate open-source libraries to steal BIP39 mnemonic phrases for wallet recovery. These packages were uploaded without proper vetting, allowing them to be listed and downloaded by developers, targeting Python users on PyPI to steal Bitcoin wallet phrases *The changes* (https://pythonpro.substack.com/p/pythonpro-21-devops-with-python-bipclip). 

 Threat Actor/group/campaign: The BIPClip campaign, possibly linked to the user accounts 'james_pycode' and 'luislindao' on PyPI. 

 Organization/industry/location: Developers working on projects related to generating and securing cryptocurrency wallets. 

 Start date – End date: December 2022 – March 2024 

 MITRE TTPs: ['T1195: Supply Chain Compromise', 'T1071: Application Layer Protocol', 'T1566: Phishing', 'T1070: Indicator Removal on Host'] 

 Impact: Multiple malicious packages were downloaded almost 5,000 times, potentially exposing developers and their projects to the theft of mnemonic phrases and ensuing financial losses. 

 Mitigation: ['Regularly audit and vet third-party packages and their dependencies before integrating them into projects.', 'Implement multi-factor authentication (MFA) for critical accounts and services.', 'Monitor network traffic for suspicious activities, such as unexpected data exfiltration.', 'Use tools like RL Spectra Assure to scan for malicious characteristics in packages.', 'Educate developers about the risks of supply chain attacks and encourage the use of verified packages.', 'Utilize *Indicators Search* and *Hunting* capabilities from platforms like *LevelBlue - Open Threat Exchange* to enhance detection and prevention efforts (https://otx.alienvault.com/browse/global/pulses?q=tag:pypi).'] 

 Detailed Steps for mitigation: ['Disable and remove any suspicious packages identified in your projects.', 'Review and update dependency management policies to include security checks.', 'Use static and dynamic analysis tools to detect malicious code within dependencies.', 'Regularly update all software components to ensure vulnerabilities are patched.', 'Employ *PCAP Scanning* to detect malicious network traffic patterns (https://otx.alienvault.com/browse/global/pulses?q=tag:pypi).'] 

 Detection Signature: {'Service': 'PyPI (Python Package Index)', 'Severity': 'Critical', 'Incident': 'BIPClip: Malicious PyPI packages', 'Signature name': '“Malicious PyPI package detected”', 'Internal checks': ['Ensure all third-party packages are vetted and verified before use.', 'Monitor for the creation of new PyPI packages by unknown or suspicious accounts.', 'Implement automated scanning of all dependencies for malicious code.'], 'External scanning': ['Monitor for the presence of mentioned malicious PyPI packages.', 'Scan for network communications involving suspicious URLs or IPs listed in the IoCs.']} 

 IoCs: {'PyPI packages': ['jsBIP39-decrypt: a23db65079ef310b87d1f017742149addbb53a81, 03baa36c6551d1414d9907775b4600c873421b34', 'bip39-mnemonic-decrypt: 45130c7a2d92282ee9c0b066206f235198b5ddfb, 087d325c24a5b28ad5342f097c3ebce3653e9ced, 46d3a5b3627e7de58c78f41eed4c95c6112245e7, f2aadcd5bd1ba46b056e2d9e4b53e21a18b61b2a', 'mnemonic_to_address: f6bb6216caf96246f07e3fd9ffcb5f0d83bd6f41, e50864e1db37a75b99596aea6538981991bf4915, a88802edce3d5e70ac2d79272f98c0891c793f2a, c3822c1f181d8f6f12325a00b5bd6cca0c18d124, c1dc8d26946d52a1014ccc6c02156449e8e1e3b6, b74c24938595fe4ccc6efe845d2b095d126ed3fc', 'erc20-scanner: 7ed9e234384e564e6d41da156bc472d5f369727e, ed1eb28a139c456e520726307e280a26b789b367, db61022dd75a63e99544bb5096c2e30d4348608e, 65dab94f5ba56b891ed9bfe20d2b1f21c2d00ee1', 'public-address-generator: 570e483dfdc6389e1d4a87f987c9b3e5a0d886ce, 1619a6fce00eecf5946750ef47d1c5748e963456, f4ff1fe54132ca91ecdf7f4b48fc16b231047b96, a875e313026a5400a920767038d953398b4afcb6, 4a39462ce7b3e2cda9998fb9fd42aeab3d5eb4a3, 19d88ff3e9d32897becc33c07b4cc307871b426e, 791e731b2db1551ccfc6df0990644ed405771aa6, 9aa894169984cfb4835b01f5f5b49d9670818259, dddd55a60d5dcbec45c034330fe12b62e38a87a8, 3e385f6b2c842a490c1729aee1b48b22a728e367, f2ed2e169bbe22aef73158e279e59d04a1f40ed9, 633b858092f7e0eb435a73f5bc972baa4cf79452, 3d82406f8e6ee1018bb39f6d40321940effeab2b, c05d35c4cc9038de3eae4e84fb9b7560f4112a3b', 'hashdecrypt: 01b66f12e9f76342729c1260ff4f0da8fc1bbe01, d5400ef535a8effe8c23cb56c4cb1c2c569beb79, 156610fff622481eb3c37e988a5c8ece20f93aef, 3843c4add1c2960f280d07b047f0c780a7b65e4d, 9c4d2bacc24f70112bc53742e8fe26dad1fa63d1, 989276eb67d5179b5eda055390d850b47198cdd2', 'hashdecrypts: 64cd50f3bc347c894cbf25a2013c04e73e85550a, 206cd1758ceda4abc9622d4f50134444a639f925'], 'Command & Control infrastructure': ['5.42.92.191', 'hxxps://raw.githubusercontent.com/HashSnake/backendapi/main/settings', '194.163.154.242', 'knallos.de', '65.109.70.235']} 

 Additional Information: ReversingLabs exposed the BIPClip campaign in PythonPro #21, along with DevOps guides and insights (https://pythonpro.substack.com/p/pythonpro-21-devops-with-python-bipclip). 


# Related articles (describing the same threat) 
['https://www.reversinglabs.com/blog/bipclip-malicious-pypi-packages-target-crypto-wallet-recovery-passwords', 'https://otx.alienvault.com/browse/global/pulses?q=tag:pypi', 'https://pythonpro.substack.com/p/pythonpro-21-devops-with-python-bipclip']
