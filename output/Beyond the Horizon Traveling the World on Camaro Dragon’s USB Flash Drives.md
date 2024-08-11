Source: [https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/](https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/)

# Beyond the Horizon Traveling the World on Camaro Dragon’s USB Flash Drives

Incident: Camaro Dragon USB Flash Drive Malware

Root cause: Infected USB drives spreading self-propagating malware

Impact: Multiple healthcare institutions, including a European hospital. Specific figures on the number of devices, people impacted, or financial losses were not provided.

Mitigation: Implement robust endpoint protection to detect and prevent USB-based malware. Ensure all systems have updated anti-virus and anti-malware software. Educate staff on the risks of using USB drives from unknown sources and enforce policies that restrict the use of USB drives.
**Detailed Steps for mitigation:**
1. **Endpoint Protection:**
   - Deploy advanced endpoint protection solutions like Harmony Endpoint to monitor and block malicious activities.
   - Utilize Threat Emulation and Threat Extraction processes to inspect and sanitize files received via email or downloaded from the web.
2. **USB Device Control:**
   - Implement policies to restrict the use of USB drives within the organization.
   - Use hardware and software solutions to control USB device access.
3. **User Education:**
   - Conduct regular training sessions to educate employees about the risks associated with using USB drives from unknown sources.
   - Promote best practices for handling external storage devices.
4. **Regular Updates and Patching:**
   - Ensure all operating systems and applications are up-to-date with the latest security patches.
   - Regularly update anti-virus and anti-malware definitions.
5. **Network Monitoring:**
   - Implement network monitoring tools to detect unusual activities related to USB devices.
   - Use intrusion detection systems (IDS) to identify potential threats.
6. **Incident Response Planning:**
   - Develop and maintain an incident response plan specifically for malware infections propagated through USB drives.
   - Conduct regular drills to ensure the response team is prepared for potential incidents.

Detection Signature:
Service: Windows OS
Port: Not applicable (USB propagation)
Severity: Critical
Incident: Camaro Dragon USB Flash Drive Malware
Signature name: “USB Malware Propagation”
Internal checks:
   - Setting1: Restrict USB port usage to trusted devices – In platform
   - Setting2: Monitor and log all USB device connections – Inside VMs
   - Setting3: Enforce execution of only signed applications from USB – Inside VMs
External scanning:
   - Detect new USB devices connected to the system
   - Monitor for execution of unknown or unsigned applications from USB devices

IoCs:
- EACore.dll: aeacc2d47a88eb68d503f9e30b189641572eb35423df931845f90a4c447ed1be
- libcef.dll: fc598a686a5a77436684cbd0f72f39033cb70a41d4dbcf5dbab47a7c2522fdda
- avkkid.dll: 68eb5590d8ad952215cf54741b0ed6204c19bba4dcb8d704883e007f16de5028
- RiotClient.dat: 6c4226aa2f8bb646f753ffd282cf4624f6bc8e5ca8a2cb2373f640a2a29cdd95
- LDVPOCX.OCX: 7d8b568746a643aa0470b14f271f681dd3b09dbc08c893b191d1d6607b86c501
- vivaldi_elf.dll: 3738e414f43d3b213cf7475a8bb616a3379c09e90c0ba5c6ac0e398d2967ca95
- EACore.dat: 7752fc0c747149d45deeec1023fef8ca73f83a154643531ae9db9cb89b6ce1dc
- EACore.dll: 464888b81e4d67aad73b245efa6442fecf8221abe3ec74d4cd180e4beedaddc6
- ZIPDLL.dll: 0279a0a3effc688097eb14d4bd6f1ab8be86f880d01952af7e2b55c51cf107b1
- HopperTick: 5c878a05fb54c6d06ca4f66d28906d17a423b1305b6aa9bde19df8e8b3e91c5c
- Delphi USB Launcher: 491d9f6f4e754a430a29ac6842ee12c43615e33b0e720c61e3f06636559813f7
- Stealer: ce1615ec67296edd05d9dc9a6a075a4724553fca5398c425372b85170aec2106
