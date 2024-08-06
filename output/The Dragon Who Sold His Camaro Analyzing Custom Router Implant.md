# The Dragon Who Sold His Camaro Analyzing Custom Router Implant

Incident: Dragon Who Sold His Camaro: Analyzing Custom Router Implant

Root cause: Infected TP-Link router firmware with malicious implants

Impact: Potentially affects numerous users with TP-Link routers, exact number of devices and financial losses unknown.

Mitigation: Secure routers by regularly updating firmware, changing default credentials, and using advanced threat prevention solutions.
- **Detailed Steps for Mitigation**:
  1. Regularly update router firmware from official manufacturer sources.
  2. Change default login credentials to strong, unique passwords.
  3. Implement multi-factor authentication where possible.
  4. Monitor network traffic for anomalies and use advanced network security solutions.
  5. Employ network segmentation to limit the spread of infections.
  6. Utilize IoT security solutions like Check Point’s Quantum IoT Protect.

Detection Signature:
  - **Service**: TP-Link Router
  - **Port**: 80, 14444
  - **Severity**: Critical
  - **Incident**: TP-Link Router Firmware Compromise
  - **Signature Name**: “TP-Link firmware infected with Horse Shell”
  - **Internal Checks**:
    - Setting1: Ensure router firmware is up-to-date – In platform
    - Setting2: Verify that no unauthorized firmware changes have been made – Inside VMs
    - Setting3: Ensure strong authentication credentials for router access – Inside VMs
  - **External Scanning**:
    - Port (80, 14444) open
    - Detection of unusual HTTP headers or traffic patterns

IoCs:
- **SHA256 Hashes**:
  - 998788472cb1502c03675a15a9f09b12f3877a5aeb687f891458a414b8e0d66c (udhcp)
  - 7985f992dcc6fcce76ee2892700c8538af075bd991625156bf2482dbfebd5a5a (sheel)
  - ed3d667a4fa92d78a0a54f696f4e8ff254def8d6f3208e6fe426dbe7fb3f3dd0 (shell)
  - 66cc81a7d865941cb32ed7b1b84b20270d7d667b523cab28b856cd4e85f135b6 (timer)
  - 8a2e9f6c2b0c898090fdce021b3813313e73a256a5de39c100bf9868abc09dbb (9406.dat)
  - da046a1fe6f3b94e48c24ffd341f8d97bfc06252ddf4d332e8e2478262ad1964 (9404.dat)
- **File Names**:
  - /vat/udhcp.cnf
  - /var/udhcp
  - .remote_shell.log
- **Infrastructure**:
  - m.cremessage[.]com (C2 domain)
  - 91.245.253[.]72 (hosts TP-Link implant C2 domain)

Yara Signatures:
```plaintext
rule apt_CN_CamaroDragon_horseshell_strings {
    meta:
        author = "Itay Cohen @ Check Point Research"
        date = "2023-04-01"
        description = "Detects CamaroDragon's HorseShell implant for routers based on embedded strings. This rule is broad."
        hash = "998788472cb1502c03675a15a9f09b12f3877a5aeb687f891458a414b8e0d66c"
        reference = ""
    strings:
        $crypto_1 = "wzsw_srand"
        // ... (other strings redacted for brevity)
        $error_62 = "wzsw_init failed"
    condition:
        filesize < 2MB and 3 of ($crypto_*) or 2 of ($filename_*) or 3 of ($debug_*) or any of ($command_*) or 3 of ($error_*) or 3 of ($function_*) or $global_1 or 5 of them
}
```

```plaintext
rule apt_CN_CamaroDragon_sheel_strings {
    meta:
        author = "Itay Cohen @ Check Point Research"
        date = "2023-04-01"
        description = "Detects CamaroDragon's sheel tool."
        hash = "7985f992dcc6fcce76ee2892700c8538af075bd991625156bf2482dbfebd5a5a"
        reference = ""
    strings:
        $ = "write failed.open fail."
        $ = "open fail.%m"
        $ = "./sheel -h server_ip -p server_port -i update_index[0-4] [-r]"
        $ = "./sheel -h"
        $ = "update server list success!"
    condition:
        filesize < 12KB and 3 of them
}
```
