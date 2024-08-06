# Organizations Under Attack from Cryptominer-Keylogger-Backdoor Combo

Incident: Cryptominer-Keylogger-Backdoor Combo Attack

Root cause: Exploitation of vulnerabilities on servers and workstations

Impact: Over 200 users worldwide impacted with over 10,000 attacks detected. Specific financial losses are not detailed in the document.

Mitigation: 
1. **Patch Management**: Ensure all servers and workstations are up-to-date with the latest security patches to prevent exploitation of known vulnerabilities.
2. **Enhanced Security Configurations**:
   - **Windows Defender**: Ensure that Windows Defender and other security solutions are configured correctly and cannot be easily disabled or bypassed.
   - **Administrative Rights**: Limit the use of administrative rights to necessary personnel only.
3. **Network Security**:
   - **Firewall Settings**: Configure firewalls to block unauthorized access to critical services.
   - **Intrusion Detection Systems (IDS)**: Implement IDS to monitor and detect suspicious activities in the network.
4. **Endpoint Protection**: Deploy advanced endpoint protection solutions that can detect and block malicious scripts and executables.
5. **User Training**: Conduct regular training for employees to recognize phishing attempts and other social engineering tactics.
6. **Incident Response Plan**: Develop and regularly update an incident response plan to quickly address any breaches.

Detection Signature:
    Service: Windows Defender, General Windows Services   
    Port: Not specific to a port, but monitoring for unauthorized registry changes and script execution  
    Severity: Critical  
    Incident: Cryptominer-Keylogger-Backdoor Combo Attack  
    Signature name: "Unauthorized Windows Defender Modification"  
    Internal checks:    
        - Setting1: Monitor registry changes that disable Windows Defender – Inside VMs    
        - Setting2: Monitor for scripts attempting to add files to Windows Defender exceptions – Inside VMs    
        - Setting3: Ensure security solutions are not renamed or disabled – Inside VMs    
    External scanning:    
        - Unusual network traffic patterns indicating command and control (C2) communications    
        - Download and execution of unknown scripts and executables

IoCs:
MD5 Hashes:
- 0BEFB96279DA248F6D49169E047EE7AB
- 769BC25454799805E83612F0F896E03F
- B747AEDF0F3E4457C6D02BC5AF7C0980
- 0A50081A6CD37AEA0945C91DE91C5D97
- 1DA8E7C92C86FC8DBAB5287BDCA91CA1
- 3C47D45F09948B8E6FDB5F96523BC60B
- 5D3E2B2EE668B2BC071B8D4027C6B8F1
- 227FA5D690A943114FF3CCFE7977192A
- A531FE822618B6A917D50BEE001C95A1
- DDAB66730A84583B98D3415F9181D092
- 830debd1f6d39c726c2d3208e3314f44
- 3b2a270b90b3e24a25cc991df40da3ca
- DDD12566B99343B96609AFA2524ECEC3
- a6d4706baeb9ab97490d745f7a2bb11e
- A7CDE18F991E97037A7899B7669E2548
- AC27DE51896A5BA2FD0DDA9B7955A201
- 2ac1d8e16e47e97db3c60d728270ad5a
- 5919e4e3e06b617d967dc6e8fecb701b
- 8dcd1e4e37838b49214f10c50ef5a5f0
- 51ad216fcb4afe42b9ef01ab472a2914
- df6f39d30dc5e9f4155514cdefb54620
- b2e250b9e3b9d5e6b2080cb782f9698e
- af9327d353b97fd50a777145bc0e8e1e
- 22f9682e543b94532d46541c63512f2d
- 1225f4f50154dd49d4853e4efc3ddf77
- 7d0f67343f128d29a50ccd3639b72884
- 752940da17469330c38ab98d04f3d6b8
- 11ca68ea3500cb03db1f4008d18cb6b2
- b558fa064d0d3f94f5e4c975375cbad1
- 4cdbcfa0d6fd2e7de6ec0030cfb2322d
- 7e09279dcd3655ab1b2e2684746e4bc2
- a38dece5bcb9f6d1c027d86e0318a60e
- 474f517eb23bdfa4c320c091c3eb2dba
- f0881b3c3d1535685d6190df4083f515
- 61d5944634d735c3e6efc3b1349de740
- 99634dcaca690066187e30c36182bf19

No additional IoCs found.
