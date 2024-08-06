# Following the LNK Metadata Trail

**Incident:** Malicious LNK files used for initial access by various malware families

**Root cause:** Shift towards using LNK files as initial access vectors due to Microsoft's macro blocking policy

**Impact:** The exact number of records, devices, or financial losses is not specified in the blog. However, the spread of malware like Qakbot, Gamaredon, and Bumblebee using LNK files could potentially affect numerous users and organizations, leading to significant financial and operational impacts.

**Mitigation:** Implement robust email filtering, endpoint protection, and user education on the risks of opening unknown files.

**Detailed Steps for Mitigation:**
1. **Email Filtering:**
   - Configure email security solutions to block or flag emails containing LNK files.
   - Implement advanced threat protection to scan attachments for malicious content.

2. **Endpoint Protection:**
   - Deploy endpoint protection solutions that include behavior-based detection to identify and block suspicious file types like LNK.
   - Ensure all endpoints are updated with the latest security patches and antivirus definitions.

3. **User Education:**
   - Conduct regular training sessions for users on the risks of opening email attachments from unknown sources.
   - Periodically simulate phishing attacks to test and reinforce user awareness.

4. **Network Security:**
   - Use network segmentation to limit the spread of malware.
   - Monitor network traffic for signs of unusual activity, such as connections to known malicious IP addresses.

5. **Metadata Analysis:**
   - Employ tools to analyze LNK file metadata for suspicious attributes, such as missing timestamps or unusual VolumeID and MachineID values.

**Detection Signature:**
- **Service:** Windows Shell Link (LNK)
- **Port:** Not applicable
- **Severity:** High
- **Incident:** Malicious LNK file usage
- **Signature name:** “Malicious LNK file with wiped metadata”
- **Internal checks:**
  - **Setting1:** Monitor for LNK files with missing or suspicious metadata fields (e.g., empty MAC timestamps).
  - **Setting2:** Use endpoint protection solutions to detect and block the execution of LNK files.
  - **Setting3:** Regularly scan endpoints for the presence of unauthorized LNK files.
- **External scanning:**
  - **Indicator:** Presence of LNK files with wiped metadata or pointing to suspicious file types (e.g., .js, .bat, .cmd).

**IoCs:**
- **Hashes:**
  - 8fda14f91e27afec5c1b1f71d708775c9b6e2af31e8331bbf26751bc0583dc7e
  - 2f9da7145056a4217552a5a536ceb8365e853fbd04d28ae2d494afb20e9c021f
  - 52458b4aaddbcb04048be963ea7d669c2ff7a69642d027f88812a5c6c1ade955
  - 56a980d7659efb8bfb997dec3259d6eb090d4e6a4609e4c0666e04ad612151d7
  - 167bbffb2ff5f724a201445f26018cb09fbf0588689f98f90fd82082aae7c6ee
  - cda2a0d9a6b5dd2123c4c2cbd55d81fd22ab72bf7ceb1489a5a770e10bcf6713
  - 754681cbb4c61dd4fe03341cfd8d2b796366a0372b53dd3e1d52c9e6ff98692d
  - 1a7f31c98147d98ac08f4b8afe7faa2f2b4aab821655717f4bde519fcd87300a
  - cc5c0daaa26815bb6528332dd4f56f7eb72db4456d5a84b8bc69239c45079a1c
  - 4efdb91497fe213e8f696065c2fe81f64cbaa219da16e2b3f8e1e146d098652b
  - 5c9dfafd3536977289b4bfda1369fbd113a778cf06ac0c01cdc8e00e1c300e77
  - 4e818b0115a9a877a9517c99b16e5a2df9cf7c5eb1fb249d9153b68e8fa94e60
  - b7ba3eaee591cc73ab85aeb09d8c02b1e569b9dcaffcbc7c4473f504f939697d
- **IP Address:**
  - 88.198.148[.]231

By addressing these points, organizations can better protect themselves against the rising threat of malicious LNK files used for initial access in malware campaigns.
