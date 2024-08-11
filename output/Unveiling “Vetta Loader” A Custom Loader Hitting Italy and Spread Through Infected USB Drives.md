Source: [https://yoroi.company/en/research/unveiling-vetta-loader-a-custom-loader-hitting-italy-and-spread-through-infected-usb-drives/](https://yoroi.company/en/research/unveiling-vetta-loader-a-custom-loader-hitting-italy-and-spread-through-infected-usb-drives/)

# Unveiling “Vetta Loader” A Custom Loader Hitting Italy and Spread Through Infected USB Drives

Incident: Vetta Loader Malware Campaign

Root cause: Spread through infected USB drives

Impact: Several Italian companies in the industrial, manufacturing, and digital printing sectors were affected, exact number of devices and financial losses not specified.

Mitigation: Proactive measures to mitigate the risk associated with Vetta Loader:
- Use only trusted USB drives.
- Enable automatic antivirus scans on all systems.
- Consider adopting USB sanitizers.

**Detailed Steps for Mitigation:**
1. **Policy Implementation:** Create and enforce a strict policy on the use of USB drives within the organization. Only allow company-issued and verified USB drives.
2. **Antivirus and Endpoint Protection:** Ensure all endpoints have up-to-date antivirus software that automatically scans any connected USB drives.
3. **USB Sanitizers:** Invest in hardware or software-based USB sanitizers that can scan and clean USB drives before they are used on the network.
4. **User Education:** Conduct training sessions to educate employees about the risks of using unverified USB drives and practical steps to avoid malware infections.
5. **Network Monitoring:** Implement advanced network monitoring tools to detect unusual activities that might indicate malware infection, such as unexpected data transfers to command and control servers.

Detection Signature:
- Service: USB Drive Malware Detection
- Port: Not applicable
- Severity: Critical
- Incident: Vetta Loader Infected USB Drive
- Signature name: “Vetta Loader USB Infection”
- Internal checks:
  - Setting1: Monitor for new USB devices connected to company systems.
  - Setting2: Ensure USB drives are automatically scanned by antivirus upon connection.
  - Setting3: Logs and alerts for unauthorized USB drive usage.
- External scanning:
  - Monitor for communications to known command and control servers associated with Vetta Loader.
  - Heuristic and signature-based detection of Vetta Loader variants on systems.

IoCs: No IoCs found.
