Source: [https://www.reversinglabs.com/blog/beware-impostor-http-libraries-lurk-on-pypi](https://www.reversinglabs.com/blog/beware-impostor-http-libraries-lurk-on-pypi)

# Developers Beware Imposter HTTP Libraries Lurk on PyPI

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: PyPI Malicious HTTP Libraries 

 Root cause: The root cause behind the incident is the uploading of malicious packages on the Python Package Index (PyPI) repository. These packages, such as *xhttpsp and httpssp* (https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi), were designed to mimic popular and legitimate HTTP libraries, exploiting the trust developers place in such repositories. The malicious packages contained either downloaders for second-stage malware or infostealers for data exfiltration through methods like the *Base64-encoded setup.py script* (https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi), including the ability to run *Powershell commands* (https://www.linkedin.com/pulse/pypile-on-bad-actors-pour-malware-pypi-npm-repos-reversinglabs). 

 Threat Actor/group/campaign: The threat actors behind this campaign, identified as *malware authors 'Portugal' and 'Brazil'* (https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi), are likely cybercriminals focused on supply chain attacks through open-source repositories. Another campaign was reported by *Phylum* (https://www.linkedin.com/pulse/pypile-on-bad-actors-pour-malware-pypi-npm-repos-reversinglabs). 

 Organization/industry/location: The primary target is the developer community that relies on PyPI for legitimate libraries. 

 Start date – End date: The blog was published on February 22, 2023, but the exact timeline of the attack is not specified. *However, the packages were published on January 27, 2023* (https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi). 

 MITRE TTPs: ['T1505.003: Implanting malicious code in public software repositories.', 'T1071: Application Layer Protocol (HTTP/HTTPS) for command and control.', 'T1005: Data from Local System (exfiltration of sensitive information).'] 

 Impact: 41 malicious packages were detected, and the impact includes potential data theft and system compromise for any developer or organization that inadvertently installed these malicious packages. A similar attack involved the *SentinelSneak* module (https://www.linkedin.com/pulse/pypile-on-bad-actors-pour-malware-pypi-npm-repos-reversinglabs). 

 Mitigation: ['**Verify Package Authenticity**: Always verify the authenticity of packages and maintain a list of trusted sources.', '**Use Security Tools**: Utilize tools like ReversingLabs A1000 for static analysis and threat classification, and their Software Supply Chain Security platform for binary analysis.', '**Conduct Security Assessments**: Regularly assess third-party libraries and dependencies for vulnerabilities.', '**Monitor for Typosquatting**: Be vigilant about typosquatting attempts and educate developers on checking package names carefully.', '**Update and Patch**: Ensure all software and libraries are up-to-date with the latest security patches.'] 

 Detailed Steps for mitigation: ['Implement automated tools to scan and verify the integrity of downloaded packages.', 'Create and enforce policies for the use of third-party libraries, including periodic reviews and updates.', 'Educate developers on the risks associated with typosquatting and the importance of verifying package sources.', 'Use multi-factor authentication (MFA) and other security best practices for accessing development environments.'] 

 Detection Signature: {'Service': 'PyPI Package Repository', 'Port': 'None (as it relates to package management, not network services)', 'Severity': 'Critical', 'Incident': 'Malicious HTTP Libraries on PyPI', 'Signature name': '“Malicious PyPI Package Detected”', 'Internal checks': ['Setting1: Ensure all packages are scanned for known vulnerabilities.', 'Setting2: Verify the integrity and source of all packages before use.', 'Setting3: Implement monitoring for unusual package behavior or metadata.'], 'External scanning': ['Scan for packages with suspicious naming conventions (e.g., slight misspellings of popular libraries).', 'Check for packages with minimal or misleading documentation.']} 

 IoCs: [{'Package Names and SHA1 hashes': ['aio5: 8c80db3ea4ebf67da6839c249270184dc4fcaeab', 'aio6: 92bcbf74010bb056b79968cd64289d100c8a80c7', 'htps1: 2b0822ba5f147dc594c4f9a95669090acab03bc1', '*xhttpsp: Unspecified hash* (https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi)', '*httpssp: Unspecified hash* (https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi)']}, {'Malicious URLs': ['*http://54[.]237[.]36[.]60/inject/QrvxFGKvsSJ5E5bx* (https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi)']}, {'update.exe': '618c11e03328eb0cc47ac21964479901dfaaa8a038e4145e247374169d6528f9', 'Rdudkye.dll': '19e9dbfe9df33f17664e780909054b48c62d3dd66e11f31f3a657d18ac4c752f'}] 

 No IoCs found for IP addresses or domains.: The report indicates the involvement of various IoCs like package names, hashes, and URLs, but does not mention specific IP addresses or domains. 


# Related articles (describing the same threat) 
['https://www.reversinglabs.com/blog/beware-impostor-http-libraries-lurk-on-pypi', 'https://www.fortinet.com/blog/threat-research/more-supply-chain-attacks-via-new-malicious-python-packages-in-pypi', 'https://www.linkedin.com/pulse/pypile-on-bad-actors-pour-malware-pypi-npm-repos-reversinglabs']
