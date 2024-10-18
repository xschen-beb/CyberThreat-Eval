Source: [https://www.sentinelone.com/blog/bluenoroff-how-dprks-macos-rustbucket-seeks-to-evade-analysis-and-detection/](https://www.sentinelone.com/blog/bluenoroff-how-dprks-macos-rustbucket-seeks-to-evade-analysis-and-detection/)

# BlueNoroff  How DPRK’s macOS RustBucket Seeks to Evade Analysis and Detection

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: BlueNoroff | How DPRK’s macOS RustBucket Seeks to Evade Analysis and Detection

Root cause: The root cause is the use of multi-stage malware targeting macOS users with sophisticated evasion techniques. The initial infection vector involves a disguised AppleScript dropper masquerading as a PDF Viewer app, leveraging social engineering tactics. Subsequent stages involve payloads written in Swift and Objective-C, and sophisticated Rust backdoors capable of downloading and executing further malware. *The dropper requires a Gatekeeper override to execute* (https://www.jamf.com/blog/bluenoroff-apt-targets-macos-rustbucket-malware/). *A new loader variant named EdoneViewer employs the CalculateExtameGCD function for decryption* (https://securelist.com/bluenoroff-new-macos-malware/111290/). *Analysis by Jamf Threat Labs revealed the use of an unsigned application Internal PDF Viewer in the initial stage* (https://www.criticalstart.com/threat-research-rustbucket-malware-takes-aim-at-macos/).

Threat Actor/group/campaign: BlueNoroff APT (a subsidiary of the DPRK cyber attack group known as Lazarus). *These activities are conducted under the Reconnaissance General Bureau (RGB) of the Korean People’s Army* (https://unit42.paloaltonetworks.com/threat-assessment-north-korean-threat-groups-2024/).

Organization/industry/location: The attack targets macOS users, likely within sectors of interest to DPRK, such as finance and cryptocurrency. *The new loader targets financial organizations and individuals related to cryptocurrency* (https://securelist.com/bluenoroff-new-macos-malware/111290/).

Start date – End date: The campaign was first reported in April 2023.

MITRE TTPs:
- T1059.002: Command and Scripting Interpreter: AppleScript
- T1204: User Execution
- T1566: Phishing
- T1071: Application Layer Protocol
- T1059: Command and Scripting Interpreter
- T1105: Ingress Tool Transfer
- T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder

Impact: The specific impact in terms of records leaked or financial losses is not provided, but includes significant risk to targeted macOS users from data theft and further malware installations. *The malware can run on both x86 and ARM architectures* (https://www.criticalstart.com/threat-research-rustbucket-malware-takes-aim-at-macos/).

Mitigation:
- Ensure software from unknown sources is not executed.
- Educate users about the risks of downloading and executing files from unknown or untrusted sources.
- Implement application whitelisting to prevent unauthorized execution of scripts and applications.
- Regularly update and patch systems to protect against known vulnerabilities.
- Deploy comprehensive endpoint security solutions capable of detecting and blocking multi-stage malware.

Detection Signature:
Service: AppleScript, macOS
Port: Not applicable
Severity: Critical
Incident: BlueNoroff | RustBucket Campaign
Signature name: “AppleScript Dropper Execution”
Internal checks:
  - Ensure that only trusted AppleScripts are allowed to execute on macOS devices.
  - Monitor for unusual AppleScript activities, especially those executing shell commands.
External scanning:
  - Regularly scan for malicious AppleScripts or unusual application behaviors.

IoCs:
- SHA1 hashes of Stage 2 and Stage 3 Mach-O binaries
- Malicious PDFs (SHA1 hashes and names)
- AppleScript main.scpt hash
- Command and control domains:
  - cloud[.]dnx.capital
  - crypto.hondchain[.]com
  - *deck[.]31ventures[.]info* (https://www.jamf.com/blog/bluenoroff-apt-targets-macos-rustbucket-malware/)
  - *on-global[.]xyz* (https://securelist.com/bluenoroff-new-macos-malware/111290/)
- File paths:
  - $TMPDIR/ErrorCheck.zip
  - /Users/Shared/1.zip
  - /Users/Shared/Internal PDF Viewer.app
  - /Users/Shared/.pd
  - ~/Library/Metadata/System Update
  - ~/Library/LaunchAgents/com.apple.systemupdate.plist

No other specific IoCs found. The malware employs a *PDFKit Framework* to create a functional PDF viewer and uses *XOR encoded C2 URLs* for communication (https://www.jamf.com/blog/bluenoroff-apt-targets-macos-rustbucket-malware/).

Additional References:
- https://securelist.com/bluenoroff-methods-bypass-motw/108383/
- https://www.proofpoint.com/us/blog/threat-insight/ta444-apt-startup-aimed-at-your-funds
- *https://securelist.com/bluenoroff-new-macos-malware/111290/* (https://securelist.com/bluenoroff-new-macos-malware/111290/)
- *https://www.jamf.com/blog/bluenoroff-apt-targets-macos-rustbucket-malware/* (https://www.jamf.com/blog/bluenoroff-apt-targets-macos-rustbucket-malware/)
- *Unit 42 Incident Response team can be contacted for urgent matters* (https://unit42.paloaltonetworks.com/threat-assessment-north-korean-threat-groups-2024/)

Ensure your macOS endpoints are protected from current and novel Mac-centric threats. *Cortex XDR provides detection and prevention alerts for RustBucket and other North Korean malware* (https://unit42.paloaltonetworks.com/threat-assessment-north-korean-threat-groups-2024/).: The new entities identified in the new found document have been integrated into the original report, improving its detail and density while maintaining coherence and readability. 


# Related articles (describing the same threat) 
['https://www.sentinelone.com/blog/bluenoroff-how-dprks-macos-rustbucket-seeks-to-evade-analysis-and-detection/', 'https://www.jamf.com/blog/bluenoroff-apt-targets-macos-rustbucket-malware/', 'https://securelist.com/bluenoroff-new-macos-malware/111290/', 'https://www.criticalstart.com/threat-research-rustbucket-malware-takes-aim-at-macos/', 'https://unit42.paloaltonetworks.com/threat-assessment-north-korean-threat-groups-2024/']
