# Lazarus Luring Employees with Trojanized Coding Challenges

Incident: Lazarus luring employees with trojanized coding challenges at a Spanish aerospace company

Root cause: Spearphishing attack via LinkedIn with trojanized executables

Impact: The impact specifics on the number of devices and financial losses were not disclosed, but the breach involved a sophisticated espionage toolset aimed at stealing sensitive aerospace technology.

Mitigation: 
1. **Employee Training and Awareness**: Conduct regular training sessions to make employees aware of phishing attacks, particularly those involving social engineering tactics.
2. **Email and Messaging Security**: Implement advanced email and messaging security solutions to detect and block spearphishing attempts.
3. **Application Whitelisting**: Only allow the execution of approved applications.
4. **Endpoint Detection and Response (EDR)**: Deploy EDR solutions to monitor and detect unusual behavior and potential intrusions.
5. **Multi-Factor Authentication (MFA)**: Enforce MFA for access to all critical systems and applications.
6. **Regular Audits and Penetration Testing**: Conduct regular security audits and penetration testing to identify and remediate vulnerabilities.
7. **Isolate Critical Systems**: Ensure that sensitive systems are isolated from the general network to limit access points.
8. **Incident Response Plan**: Develop and regularly update an incident response plan tailored to cyber espionage threats.

Detection Signature:
- **Service**: Windows Operating System
- **Port**: Not applicable (This attack vector involves user execution rather than a service listening on a port)
- **Severity**: Critical
- **Incident**: Lazarus spearphishing and trojanized executables
- **Signature name**: “Lazarus trojanized executable execution”
    - **Internal checks**:
        - **Setting1**: Monitor execution of unusual or unexpected applications, particularly those not commonly used within the organization.
        - **Setting2**: Implement behavioral analysis to detect side-loading and reflective DLL injection techniques.
        - **Setting3**: Ensure EDR solutions are configured to detect and alert on suspicious activity such as unusual DLL loads.
    - **External scanning**:
        - Not applicable (external scanning is not relevant to this attack vector)

IoCs:
- **Files**:
    - C273B244EA7DFF20B1D6B1C7FD97F343201984B3
    - 38736CA46D7FC9B9E5C74D192EEC26F951E45752
    - C830B895FB934291507E490280164CC4234929F0
    - 8CB37FA97E936F45FA8ECD7EB5CFB68545810A22
    - 0F33ECE7C32074520FBEA46314D7D5AB9265EC52
    - C7C6027ABDCED3093288AB75FAB907C598E0237D
    - C136DD71F45EAEF3206BF5C03412195227D15F38
    - E61672B23DBD03FE3B97EE469FA0895ED1F9185D
    - E18B9743EC203AB49D3B57FED6DF5A99061F80E0
    - 10BD3E6BA6A48D3F2E056C4F974D90549AED1B96
    - 3007DDA05CA8C7DE85CD169F3773D43B1A009318
    - 247C5F59CFFBAF099203F5BA3680F82A95C51E6E
    - EBD3EF268C71A0ED11AE103AA745F1D8A63DDF13

- **Network**:
    - 46.105.57[.]169
    - 50.192.28[.]29
    - 67.225.140[.]4
    - 78.11.12[.]13
    - 89.187.86[.]214
    - 118.98.221[.]14
    - 160.153.33[.]195
    - 175.207.13[.]231
    - 178.251.26[.]65
    - 185.51.65[.]233
    - 199.188.206[.]75

No additional IoCs found beyond those listed in the document.
