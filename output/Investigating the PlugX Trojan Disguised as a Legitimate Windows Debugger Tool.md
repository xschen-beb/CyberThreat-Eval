# Investigating the PlugX Trojan Disguised as a Legitimate Windows Debugger Tool

Incident: PlugX Trojan Disguised as Legitimate Windows Debugger Tool

Root cause: DLL Search Order Hijacking

Impact: The exact number of devices, people impacted, and financial losses are not provided in the document.

Mitigation: Implement multiple security measures to prevent DLL sideloading attacks.
  
  Detailed Steps for mitigation:
  1. **Implement Whitelisting**: Allow only known and trusted applications to run on the system while blocking any suspicious or unknown ones.
  2. **Use Signed Code**: Ensure that all DLLs are signed with a trusted digital signature to guarantee their authenticity and integrity.
  3. **Monitor and Control Application Execution**: Monitor and control the execution of applications and their dependencies, including DLLs, to detect and prevent malicious activities.
  4. **Educate End Users**: Inform users about the dangers of DLL sideloading attacks and encourage them to exercise caution when installing or running unfamiliar software.
  5. **Endpoint Protection**: Use endpoint protection solutions that offer behavioral analysis and predictive machine learning for better security capabilities.
  6. **Implement Effective Incident Response Plans**: Establish a clear and well-defined incident response plan to detect, contain, and respond to security incidents as quickly as possible.

Detection Signature:
  Service: Windows OS
  Severity: Critical
  Incident: PlugX Trojan 
  Signature name: “PlugX DLL sideloading detection”
  Internal checks:
    - Setting1: Monitor for execution of x32dbg.exe from non-standard directories.
    - Setting2: Check for the presence of suspicious DLLs (e.g., x32bridge.dll) in the same directory as legitimate executables.
    - Setting3: Validate digital signatures of DLLs and executables running on the system.
  External scanning:
    - Monitor for unusual network traffic to known C&C servers (e.g., 160[.]20[.]147[.]254).
    - Check for scheduled tasks or registry entries that execute suspicious files.

IoCs: 
  - File name: x32dbg.exe
  - SHA256: ec5cf913773459da0fd30bb282fb0144b85717aa6ce660e81a0bad24a2f23e15
  - File name: x32bridge.dll
  - SHA256: 0490ceace858ff7949b90ab4acf4867878815d2557089c179c9971b2dd0918b9
  - File name: akm.dat
  - SHA256: 0e9071714a4af0be1f96cffc3b0e58520b827d9e58297cb0e02d97551eca3799
  - File name: x32bridge.dat
  - SHA256: e72e49dc1d95efabc2c12c46df373173f2e20dab715caf58b1be9ca41ec0e172
  - File name: DismCore.dll
  - SHA256: b4f1cae6622cd459388294afb418cb0af7a5cb82f367933e57ab8c1fb0a8a8a7
  - File name: Groza_1.dat
  - SHA256: 553ff37a1eb7e8dc226a83fa143d6aab8a305771bf0cec7b94f4202dcd1f55b2
  - IP address: 160[.]20[.]147[.]254 (C&C Server)
