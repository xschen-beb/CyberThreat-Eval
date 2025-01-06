Source: [https://www.reversinglabs.com/blog/malicious-pypi-crypto-pay-package-aiocpa-implants-infostealer-code](https://www.reversinglabs.com/blog/malicious-pypi-crypto-pay-package-aiocpa-implants-infostealer-code)

## Related articles (describing the same threat) 
- https://thehackernews.com/2024/11/pypi-python-library-aiocpa-found.html
- https://www.reversinglabs.com/blog/malicious-pypi-crypto-pay-package-aiocpa-implants-infostealer-code
- https://security.snyk.io/vuln/SNYK-PYTHON-AIOCPA-8442272
- https://blog.pypi.org/posts/2024-11-25-aiocpa-attack-analysis
- https://www.infosecurity-magazine.com/news/malicious-pypi-exposes-crypto
- https://www.broadcom.com/support/security-center/protection-bulletin/aiocpa-a-malicious-python-module

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident 
 Malicious PyPI crypto pay package aiocpa implants infostealer code 

#### Root cause 
 The root cause of the incident is the malicious package `aiocpa` published on the Python Package Index (PyPI) repository. The package, created by user VoVcHiC, was designed to compromise cryptocurrency wallets by deploying infostealer code that exfiltrates sensitive information such as tokens, API servers, and other Crypto Pay-related data to a remote Telegram bot. The attackers did not use typical typosquatting techniques but instead created a legitimate-looking package to attract users and then introduced malicious updates in later versions. The infostealer code was hidden within the utils/sync.py file and employed layers of Base64 encoding and zlib compression to obfuscate its intent *Your changes* (https://www.infosecurity-magazine.com/news/malicious-pypi-exposes-crypto/). The package was quarantined by PyPI administrators to prevent further installation *Your changes* (https://thehackernews.com/2024/11/pypi-python-library-aiocpa-found.html). *Your changes* (https://www.broadcom.com/support/security-center/protection-bulletin/aiocpa-a-malicious-python-module). *Your changes* (https://security.snyk.io/vuln/SNYK-PYTHON-AIOCPA-8442272). 

#### Threat actor/group/campaign 
 The specific threat actor or group behind this campaign is not identified in the report. It is unclear if the original developer was behind the rogue update or if their credentials were compromised by a different threat actor *Your changes* (https://thehackernews.com/2024/11/pypi-python-library-aiocpa-found.html). 

#### Organization/industry/location 
 The incident targeted users of the PyPI repository, particularly those involved in cryptocurrency-related activities. 

#### Start date – End date 
 The malicious package was first published in September 2024, with the malicious versions (0.1.13 and 0.1.14) published on November 20, 2024. The incident was detected and reported on November 21, 2024, and the package was subsequently removed by PyPI. 

#### MITRE TTPs 
 ['T1071: Application Layer Protocol (Confidence: High) — The exfiltration of data to a remote Telegram bot aligns with this TTP.', 'T1027: Obfuscated Files or Information (Confidence: High) — The use of obfuscated code within the package.', 'T1190: Exploit Public-Facing Application (Confidence: Medium) — The use of a public package repository to distribute malicious code.'] 

#### Impact 
 The exact number of users affected is not specified, but the package had over 10,000 downloads. The financial impact could include stolen cryptocurrency assets from compromised wallets. *Your changes* CVSS Score: 9.3 critical (https://security.snyk.io/vuln/SNYK-PYTHON-AIOCPA-8442272). 

#### Mitigation Steps 
 ['Regularly monitor and audit dependencies in your software projects.', 'Use advanced software supply chain security tools to assess and manage third-party software risks.', 'Pin dependencies and versions to prevent unwanted updates.', 'Perform a security assessment of third-party packages, code, tools, and extensions used in your software development.', 'Implement automated threat detection systems and maintain a comprehensive software bill of materials (SBOM) and risk assessment.'] 

#### Detection Signature 
 {'Service': 'PyPI (Python Package Index)', 'Port': 'N/A (HTTP/HTTPS)', 'Severity': 'Critical', 'Incident': 'Malicious PyPI crypto pay package aiocpa implants infostealer code', 'Signature name': 'Malicious PyPI package detected', 'Internal checks': ['Monitor for unusual or obfuscated code patterns in PyPI packages.', 'Verify the integrity of package maintainers and their repositories.', 'Use machine learning-based threat hunting systems to detect anomalies in package behavior.'], 'External scanning': ['Packages downloaded from PyPI should be scanned and analyzed for malicious behavior.', 'Monitor for communication with known malicious IPs or domains, particularly those associated with Telegram bots.']} 

#### Additional Information 
 {'Snyk ID': 'SNYK-PYTHON-AIOCPA-8442272 *Your changes* (https://security.snyk.io/vuln/SNYK-PYTHON-AIOCPA-8442272)', 'CWE': 'CWE-506: Common Weakness Enumeration *Your changes* (https://security.snyk.io/vuln/SNYK-PYTHON-AIOCPA-8442272)', 'Credit': 'Phylum Research Team *Your changes* (https://security.snyk.io/vuln/SNYK-PYTHON-AIOCPA-8442272)'} 

#### IoCs:
- url: https://pypi.org/project/aiocpa/ ([link](https://thehackernews.com/2024/11/pypi-python-library-aiocpa-found.html)) 
Found in URL, Not found for url https://pypi.org/project/aiocpa/ in VT. 

- url: https://clickpy.clickhouse.com/dashboard/aiocpa ([link](https://thehackernews.com/2024/11/pypi-python-library-aiocpa-found.html)) 
Found in URL, Not found for url https://clickpy.clickhouse.com/dashboard/aiocpa in VT. 

- url: https://github.com/pypi/support/issues/4682 ([link](https://thehackernews.com/2024/11/pypi-python-library-aiocpa-found.html)) 
Found in URL, Not found for url https://github.com/pypi/support/issues/4682 in VT. 

- url: https://secure.software/pypi/packages/aiocpa ([link](https://www.reversinglabs.com/blog/malicious-pypi-crypto-pay-package-aiocpa-implants-infostealer-code)) 
Found in URL, Not found for url https://secure.software/pypi/packages/aiocpa in VT. 

- hash_sha1: a1187d2a4acfe8ddaee3c7be79a9bb838142903a ([link](https://www.reversinglabs.com/blog/malicious-pypi-crypto-pay-package-aiocpa-implants-infostealer-code)) 

- hash_sha1: 7007be259829d72e73ff63ad409770ca56cfc418 ([link](https://www.reversinglabs.com/blog/malicious-pypi-crypto-pay-package-aiocpa-implants-infostealer-code)) 
Found in URL, Not found for hash_sha1 7007be259829d72e73ff63ad409770ca56cfc418 in VT. 

- hash_sha1: fc36c157075dd4302f71ed2660e19a61016b085c ([link](https://www.reversinglabs.com/blog/malicious-pypi-crypto-pay-package-aiocpa-implants-infostealer-code)) 

- hash_sha1: 01f7db47368bffa279fb15c688518774454650cf ([link](https://www.reversinglabs.com/blog/malicious-pypi-crypto-pay-package-aiocpa-implants-infostealer-code)) 
Found in URL, Not found for hash_sha1 01f7db47368bffa279fb15c688518774454650cf in VT. 

- url: https://snyk.io/vulnerability-disclosure/ ([link](https://security.snyk.io/vuln/SNYK-PYTHON-AIOCPA-8442272)) 
Found in URL, Not found for url https://snyk.io/vulnerability-disclosure/ in VT. 

- url: https://snyk.io/careers/ ([link](https://security.snyk.io/vuln/SNYK-PYTHON-AIOCPA-8442272)) 
Found in URL, Not found for url https://snyk.io/careers/ in VT. 

- url: https://preferences.snyk.io/dont_sell ([link](https://security.snyk.io/vuln/SNYK-PYTHON-AIOCPA-8442272)) 
Found in URL, Not found for url https://preferences.snyk.io/dont_sell in VT. 

- domain: snyk.io ([link](https://security.snyk.io/vuln/SNYK-PYTHON-AIOCPA-8442272)) 

- url: https://api.telegram.org/bot7858967142:AAGeM6QvKdEUK9ZWD9XoVM_Zl1cmj_mlyJo ([link](https://blog.pypi.org/posts/2024-11-25-aiocpa-attack-analysis)) 

- domain: www.google-analytics.com ([link](https://www.infosecurity-magazine.com/news/malicious-pypi-exposes-crypto)) 

- domain: www.infosecurity-magazine.com/favicon.ico ([link](https://www.infosecurity-magazine.com/news/malicious-pypi-exposes-crypto)) 
Found in URL, Not found for domain www.infosecurity-magazine.com/favicon.ico in VT. 

- For more IoCs, please refer to the above links. 

#### paste IoC
a1187d2a4acfe8ddaee3c7be79a9bb838142903a
fc36c157075dd4302f71ed2660e19a61016b085c
snyk.io
https://api.telegram.org/bot7858967142:AAGeM6QvKdEUK9ZWD9XoVM_Zl1cmj_mlyJo
www.google-analytics.com

