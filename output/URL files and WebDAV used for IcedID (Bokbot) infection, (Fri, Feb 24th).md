Source: [https://isc.sans.edu/diary/rss/29578](https://isc.sans.edu/diary/rss/29578)

# URL files and WebDAV used for IcedID (Bokbot) infection, (Fri, Feb 24th)

Incident: IcedID (Bokbot) infection via URL files and WebDAV

Root cause: Vulnerable WebDAV Server

Impact: Potentially significant, though specific numbers of impacted devices and financial losses are not provided in the document.

Mitigation: Secure the WebDAV server and ensure safer email practices:
1. **Authentication and Access Control:**
   - Implement strong authentication mechanisms for accessing the WebDAV server.
   - Restrict WebDAV access to authenticated users only.
2. **Network Segmentation:**
   - Isolate the WebDAV server from the rest of the network to limit the spread of malware.
3. **Regular Updates:**
   - Keep the WebDAV software and associated components up to date with the latest security patches.
4. **Email Filtering:**
   - Employ advanced email filtering to detect and block malicious attachments like .url files.
5. **User Training:**
   - Educate users about the risks of opening unknown files and the importance of verifying email sources.
6. **Intrusion Detection:**
   - Deploy intrusion detection systems (IDS) to monitor network traffic for suspicious activities such as unusual WebDAV requests.
7. **Endpoint Protection:**
   - Ensure endpoints have up-to-date antivirus software capable of detecting and mitigating threats like IcedID.

Detection Signature:
```
Service: WebDAV
Port: 80 (HTTP)
Severity: Critical
Incident: IcedID (Bokbot) infection via URL files and WebDAV
Signature name: “WebDAV malicious activity”
Internal checks:
    - Setting1: WebDAV server should require authentication for access. – In platform
    - Setting2: WebDAV server should not be accessible from the external Internet without proper access control – Inside VMs
    - Setting3: WebDAV server should be kept up to date with security patches – Inside VMs
External scanning:
    - Port (80) open
    - WebDAV accessible without authentication
```

IoCs: 
```
IP: 104.156.149[.]6, 157.254.195[.]65, 5.61.47[.]8, 38.180.0[.]89, 37.252.6[.]77, 80.78.24[.]30
Domain: mandalorecnote[.]com, ituitem[.]net, renomesolar[.]com, palasedelareforma[.]com, noosaerty[.]com
File Hashes:
  - 0a79166f95d1f1a3542135241ea42026188916ea9c06510c20247849c5ad6f0e (PO#56034.url)
  - 0dfd67dafe621b57eac338e581d65598197cdb0a499a8345fa9beeae9196d8e8 (PO#15986.url)
  - 145b2d2a7d52f6c9ff96fbd2338204a7eb062ed271893faa7ad5a87b0879fa50 (PO#66438.url)
  - 1574ed0b6c1b82089dc8fc098acc3bb86c63aa11f24e45c6683a485fe109777a (PO#89932.url)
  - 161baa1e72a4f23c9c7fee1431d3fcb07a0fd832a4318c1ebe7526de71baedda (PO#39134.url)
  - 1c3ece4a1e0c9cf42a063b76da6d22c1bd43e929ce01cc51d506880b8d86f72f (PO#36627.url)
  - 2505d97d1b34bc27e13e6e212fa591866a3a384952d404ceb7c1a8f385ac6238 (PO#84049.url)
  - 266c106ef803493a9dc14f48437c482088764ea47eb14214f09d49ad1ad62c71 (PO#31084.url)
  - 2bdc4b5aa6b3f9395065f2c31ba130ecc21fbe4db3fcdb3c60a526e34e72bd74 (PO#61467.url)
  - 48b05dcb2f48ae742498e040135079a8b59f3698d1619c44622b0fe558760342 (PO#92390.url)
  - 4cc43b0ec10ad3f8521504df13f38182d945b865dac070b8663c262ec2b2ed69 (PO#96856.url)
  - 5d9ffcd009e5fde1eaa2eb6a2fbead02b3169024401720e2a06e90e3edd10cb9 (PO#37820.url)
  - 690b002884d71774f0877ad69385c12d0f814606296c69b647bd19a900cdd768 (PO#66703.url)
  - acc3d0964c41f6553d3aca71ba8baec044a2158ea019ecf50d8fa1d9e6720298 (PO#68631.url)
  - accf567245e184467ead9e9e5a52ab68d7bd0c9eaa81848b439cec69fd808416 (PO#69421.url)
  - b1c1977b5d5b0705fa3e29b9cd5760e2f394698ad9594f626104021893bddc20 (PO#59042.url)
  - c823261b03d11d23e76756643c8ca28baf024353464297346612af908bda4d8e (PO#94545.url)
  - d02a84eb7972ce9e1a092702595750ec687f850ebbd1879a3fe5944f51b24473 (PO#16873.url)
  - d5332249fcef78250100b4a147ef336279f188336f2d543dd5b3638973b107be (PO#84805.url)
  - dcf2a4d0ee66d3f47d9ff4ee9bcbc63c3286559a0ba80ab129034639b063f7f1 (PO#44959.url)
  - f4c46cf9ffd25764a63bcc6d158bfad5495802f830266111a37d39f107eee6d4 (PO#36434.url)
  - fae4e3388e95d2e710257ae86ff482258f0f51458f42d116349ebc6a9266b29f (PO#99805.url)
  - 2c814c61891a1b3b9067b82b5357d13505b4ced6fd827fdde4c3116efb3f9cef (.bat file)
  - 6daeb5feb3cf988790b30152a25617566523fad65cbc4846e3a715c2e4dfb307 (Probable decoy DLL file)
  - 8d076fe2d93a9ebd5701eb7a1acab37e9d390df7f50e6d155c6c7289934d2b54 (host.dll)
  - d1ac1a32c791141d89d3df990f95b8011cfc2ec585a8c8715c0bac61e63b1a95 (gzip binary)
  - f2ab26557364d548a40ab3c43db78e03750e8eb391258080dda31b5c3f71c1d9 (license.dat)
  - a01a82f3edd13700ea85115e553fb7a601b098891cbbebbc94b2289ae40bedce (Persistent DLL)
```

