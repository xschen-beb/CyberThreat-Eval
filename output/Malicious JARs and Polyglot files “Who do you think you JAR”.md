Source: [https://www.deepinstinct.com/blog/malicious-jars-and-polyglot-files-who-do-you-think-you-jar](https://www.deepinstinct.com/blog/malicious-jars-and-polyglot-files-who-do-you-think-you-jar)

# Malicious JARs and Polyglot files “Who do you think you JAR”

Incident: Malicious JARs and Polyglot Files Exploitation

Root cause: Improper validation of JAR file formats and use of polyglot files to bypass security mechanisms

Impact: Multiple organizations and individuals may be impacted by the spread of StrRAT and Ratty malware, with potential financial losses from data breaches, ransomware, and other malicious activities.

Mitigation: Implement strict validation checks for JAR files and monitor processes that execute JAR files.

Detailed Steps for Mitigation:
1. **Implement Static and Dynamic Analysis**: 
   - Ensure that security solutions perform both static and dynamic analysis on JAR files. Static analysis should validate the presence of the end of the central directory record.
   - Dynamic analysis should monitor processes like “java” and “javaw” and inspect their arguments for “-jar” to treat the file as a JAR regardless of its extension.

2. **Update Security Policies**:
   - Configure security tools to detect and block polyglot files.
   - Use advanced threat prevention technologies such as Deep Instinct’s deep learning framework to identify and prevent malicious file executions.

3. **Network Monitoring and Filtering**:
   - Monitor network traffic for connections to known malicious C2 servers.
   - Implement URL filtering to block access to malicious URL shortening services and Discord CDN links.

4. **User Education and Awareness**:
   - Train users to recognize phishing attempts and avoid downloading and executing suspicious files.
   - Promote safe browsing practices and the use of reputable email services that filter malicious attachments.

Detection Signature:
    Service: Java Runtime Environment (JRE)
    Port: Not applicable (focus on processes)
    Severity: Critical
    Incident: Malicious JAR files and polyglot exploitation
    Signature name: “Java JAR file with polyglot structure”
    Internal checks:
        - Setting1: Monitor and validate JAR file structures for the end of the central directory record. – In platform
        - Setting2: Inspect arguments of “java” and “javaw” processes for “-jar” to identify JAR file execution. – Inside VMs
        - Setting3: Ensure security solutions are updated to detect polyglot files. – Inside VMs
    External scanning:
        - Monitor and block URLs known to distribute malicious JAR files.
        - Scan for known C2 server connections associated with StrRAT and Ratty malware.

IoCs:
- d51d269b62e55d4af8a4bd72dcf3c5115ad27fe5466640041c658c0325194451
- 534a4b0e17723755dd8cbdcdec309004ef59c3dfacb87fac86da4548780d2f1b
- 08921a6b0b2903b9c991acb869930c7cab3cbaf11e002be9c88400af48c3fa21
- 59a02230a78b87c97eebbf7cdba40ea17c7d9411d706fd255c2a6a025584fd9f
- a9ac4ae704da346a0f3d2960b084d8f314c0fd60a934116e3c75647c713314b6
- 47fc7fc1658acfa2f7a0b388bea6b52787f186bf8297ce189a575d547dfbd8e0
- a80add76ff8ad0e1c3bdab9459546fd724e1f4034248d1542aec1264c02d3857
- f0e57c84ba1958cabf24cfec4a0d50be6b7bc0e45c639d08a53097494373ae9e
- e7812ff64dbe51584d3090e008b464510dbb87ac860c68d89e224621755021f9
- 41ef2dfa736e9a24a1a29a373357ac249dad99f86f1cc0283ddd4765fa14e54a
- 8d801f58d10dbcd52739fa35aa862286c3fe9606411f0e5f7b8b3fd71f678cad
- f79ba296aeab13be409ee3ef435f47a8888f7186a062fa481603ec32f3d6b678
- 262e6824f0c4c765e73a7041362d7a3a8d63dab1be91ecf5e80623ac6e2f389e
- b6a0dcd8c9bc11794837e8f9350e2816ae7a60d148f3e6f436c2645f450feeab
- f620c4f59db31c7f63e8fde3016a33b3bfb3934c17874dcfae52ca01e23f14de
- 54814775c2f266cafe3d4ddc58bc400360aad8cea95e0d3ee74ceceb927cb3b8
- 2f4c6eb0a307657fb46f4a8f6850842d75c1535a0ed807cd3da6b6678102e571
- 74c8d5e01e2bb52c6f5cd7863168085ff81bea970b5309ec180c2e1a299096df
- f2b36a7df3d0b4d63bbbc529b7a27282e5626300e1353d2596866e4a82165f64
- 4f00914f63181c0afbfff41a95f5f1364c61d78ffb250ec8ef3102b3d3bd7003
- a989289cd6df1b1c38dbda84eb3b286bb8fb7a2af9beb1e55b029dbf861bac83
- 521a2e7ee2558d83e29bceb68a8c4ea0ecce4bddcb05cc0d3b0365522f126d1f
- 19154b831614211de667c2aedd6a4b5b89d4bfc1e129eb402a6300ad2e156dcf
- e3be7066e6922d7460dea80ca5b7fef8f4abc7b1f056d8f329c03b306e8ca9b0
- 788f1abb67d6f21cf299e2f67a2b414d169e8ab16cc8a61bf698e5c7f1482999
- 5e288df18d5f3797079c4962a447509fd4a60e9b76041d0b888bcf32f8197991
