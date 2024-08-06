# Operation Magalenha  Long-Running Campaign Pursues Portuguese Credentials and PII

Incident: Operation Magalenha

Root cause: Compromised user devices via phishing emails and malicious VB scripts.

Impact: Users of over 30 Portuguese financial institutions affected. The exact number of devices and financial losses are not specified in the report.

Mitigation: Implement stringent email filtering and user education programs to prevent phishing attacks. Secure user devices with up-to-date antivirus software and ensure regular updates and patches.

Detailed Steps for mitigation:
1. **Email Filtering and Security**:
    - Deploy advanced email filtering solutions to detect and block phishing emails.
    - Use sandboxing to analyze suspicious email attachments in a safe environment.
    - Implement DMARC, DKIM, and SPF to prevent email spoofing.

2. **User Education**:
    - Conduct regular training sessions on recognizing phishing attempts and social engineering tactics.
    - Create awareness about the dangers of clicking on unknown links or downloading attachments from untrusted sources.

3. **Endpoint Security**:
    - Ensure all user devices have up-to-date antivirus and anti-malware software.
    - Regularly update the operating systems and applications to patch known vulnerabilities.
    - Implement endpoint detection and response (EDR) solutions to detect and respond to suspicious activities.

4. **Network Security**:
    - Monitor network traffic for signs of data exfiltration and unusual activity.
    - Use intrusion detection systems (IDS) and intrusion prevention systems (IPS) to detect and block malicious activities.

5. **Incident Response Plan**:
    - Develop and regularly update an incident response plan to quickly respond to security incidents.
    - Conduct regular drills to ensure the effectiveness of the incident response plan.

Detection Signature:
    Service: Delphi-implemented backdoors (PeepingTitle variants)
    Port: Various, depending on C2 server configuration
    Severity: Critical
    Incident: Operation Magalenha
    Signature name: “PeepingTitle backdoor detection”
    Internal checks:
        - Setting1: Monitor for the presence of Delphi-implemented backdoors on user devices.
        - Setting2: Check for unusual registry key modifications, such as HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run.
        - Setting3: Detect unauthorized process terminations and screenshot captures.
    External scanning:
        - Monitor for communications with known C2 servers used by PeepingTitle backdoors.
        - Check for connections to URLs associated with malware hosting and C2 servers listed in the IoCs.

IoCs:
- Shortened URLs:
    - https://tinyurl.com/edpmobilecliente
    - https://tinyurl.com/dashboaraudicaofastaccoun
    - https://tinyurl.com/edpareaparticulares
    - https://tinyurl.com/miareapersonal

- SHA1 Hashes:
    - 001334b045e0d1e28c260380f24c1fa072cb12eb
    - 0131862cd70303d560d47333cce4d2b58505222e
    - 045d5be69b5ba4ffb4253b029cc01d827706c75a
    - 0716415bc910e4a9501d43ac03410288a4e860d4
    - 071c53099decea6d9117e4ee519470140c68c7e9
    - 0a202ca568087eabeb741648be4255d834ab14b1
    - 13b370f368c1df2d30bb8fdf96d84e66e07c8a79
    - 17fe9cdd20a64fec5d471f6878a462a2ef0af212
    - 1a5ad2fb1d4fc4971286bdd5abf669722d7e4c19
    - 1e65c104c765e6e46887f7de04cc14f52dbdfe98
    - 208572a9f44d5349382c58d51d2d14532bc87bb3
    - 266a1c4b8bd95595dcdd46bcb409ee773bd2f407
    - 268d93bfd3f0a8a5cd76eea6311eb2a0b754a4e2
    - 26be17aef483d553c0e5678e35611b019acd28a3
    - 280999b0490bbe06665d35f2cda373fa32bfc59c
    - 2ee320533e687da7613721446dabceecafb940c1
    - 3079bba1a2372282f6bb4a35706144d5b9800953
    - 32d15771736bb5c3232c3fa68ee3da4161177413
    - 35597059ae1f14f50d7fe8b1858525552f62da19
    - 3a1e1294e894b9dd35edfdd59f67049729121619
    - 3be8f26dbc49b8a2504c58de247b838888e15a17
    - 418fabf734c0803f2686a41665f06525cfa3adbb
    - 41ab10d5e057e714d8caad5855c115f5bef76097
    - 42ee272c6bc93c5c0c47024f631350c23edc06fe
    - 43a55a5954d56c4e9fe63cfdd6ab0c97766c9642
    - 44da6f99de08e5193a64a89ce696d775248314d9
    - 45304d8ae20e0fcaf975be64b7844c361ae61537
    - 470e52d04a89318a868402617b2edd16e1a20613
    - 483a4a7e4650502e36dacde33652bf6b62718822
    - 48e77c8ab75d042d1526fe3cd40beeea5fff7794
    - 494d166f7b052c7feaf5666062dcf54525873ac2
    - 4fc26b033677b6a6dc77ae3c4451d3d4421bcc04
    - 51be9fb55ff9606b0f4e887d332608f41533215e
    - 52d06e3b0e3b91165bdba769a94710bbdad8d8d7
    - 542b320b77bb3f826ee17009564613352e5a4911
    - 5c9fc5902ced06f7068f95dfa7c25c1939be3f51
    - 5e38e6a927309aac4679a6d63c1e01b3830ca7c7
    - 5ee9c3e8ff35bc0435d0691112d7f101856d9a51
    - 603ac1e61a39c74d5053ccedd6964ce5f9f365f3
    - 62a1fd987b051586132b1d1752d78821139efb7f
    - 62b1ef509f0f9dffa611f3addface8f91089b0c3
    - 69beb59e75f70487edbbf997aba83b926674a355
    - 6a43e8c05194e066b85845e454d41bf86e1ab376
    - 6a977ae1ad3466f20f50e101b5a561ad3ffc3aa7
    - 6c3d57a7b6631adbe3b6a2c2d88eef6593c51900
    - 6e00ef494a5955df4802c078ae3ffc6c6abdcbd7
    - 72b3be646f03a71e8a2632096ddf6638bc0141c9
    - 7339585c17aaa96e93f971b64548666a3b09d1f9
    - 738aff3e88f498c3607eeadd37b95791acf40196
    - 76b1bb307e1489999da725c2c9fac5b4581cb448
    - 7992e075bc9de98e944930372f1768ccc08e429f
    - 79ce7defeed60bba523bc3779cb9379435157f93
    - 7bbe644df54723d7a48bef58a616a62559401d0d
    - 7e82f8608c199eb32230dd2706c11b2e70ba13d8
    - 7f3c5142f60cd36073b54eda77b38be754a5f7d5
    - 824268bffde52dc44fedc254dc59ef559b7b2d17
    - 830c4e2cc10bbf122882a177a3ea8e810b114c82
    - 8752dab95747175bdb6cb7772cf4d11858049c9d
    - 87ff9f5f3f4853d0c218ac36182fa18bc5e206d0
    - 890c8ab68be8990deb26dab6f5c82f0a812b9fcb
    - 8c62851c74dc2bd1077edfb7456f87b47199925c
    - 8cc16c418764d26b15d41f713551a7d0f214ab4c
    - 97bab3df5acbd1e4ad8b9a38cbbd80c297971490
    - 9ab7bc8a9b4ccbc75903e78d96357e11dfd97535
    - 9c997e9ee92209be186de2a4f9696122bdfbc46d
    - 9eaa52e9f72f0b43648699a3a511d0a7c6ffcdd5
    - a0721a76cc8a0e44bf734206638ba013da809325
    - a28db721736fe5d6281c08b4f2f396da480eb170
    - a53b9e14f316a62e8c6c7a53a7c98158fda29533
    - a7c7233274e34b69b6c62caceebb19135f9034b2
    - acc753a084b8172981b3086122929eb4abde131a
    - afd5ccd6effb4eed6aec656a25ed869b954ee213
    - affcb29e3e8b510cab6b836672511bc738f2d328
    - b0253186f56662ecfbebf95cc91a887e161e32d3
    - b427cf74c820985cc3cedef68b9953c2e83631e1
    - b50ced2769e74050b130fbcb28c6d80880cfe612
    - b7ce5ab969a2088a7d6c401c72eeff63173ce491
    - bed147a98e6bff36cf3bccfc7640d444040e1f0c
    - c3aa8423bba6f01528f822eddb692ae56aa1be6b
    - c43f60bf6c24dd6c290b40afb26ea60094688a73
    - c4c59fc68f225bdec7e22bead289fda2503fb6b0
    - c5239a9994ca54ac08e45ce7443d9226151d0b36
    - cd5892ca5b21999799a04d72fb93dc815f7227aa
    - cdd2f94c542bf369702271cd83c6aa9ff2e595ea
    - d1dca2dc87376c833644a04c74e4f102565e810a
    - d2e078450e479a6cd3b1d95597fd2204fd370c42
    - d86aabf4713b18718421b5c0fd4084143d4f7f08
    - db9521169aaad154e31d4e573414459e26b57900
    - dc04ad9e1d8022a06a28d0522b2a1988c8ed4bab
    - dcdf79b172f340dc173d038d05c7eb826c55c3dc
    - dd46a9c61ad4aee2c865a4144733d1daf7d6bc79
    - dec59a76e8f1703d15fcb7f7532c759aaf717165
    - df0a90c8890f83f760e41c853d9033d3971194e9
    - df99c6fabdf6fc664e9c466af8a2986af0bfbfb8
    - dff84020be1f4691bed628d300df8a8b12a4de7e
    - dff84020be1f4691bed628d300df8a8b12a4de7e
    - e6215a2e0c4745eef724019cab07c04dac75725e
    - e9f9a5f559366a8e66f81d43ecc05d051b6e3853
    - eaa2c945b22f5c1b8bfbd6d8692826d841fc9185
    - f00493ea6b1a2cb50c74feb3af65bfaabf327a07
    - f534e0a04ceb6f3e1a10209f416675e9df127afc
    - f5a99ecd7847cc79210d5df505e222828ad63199
    - f66d71e1ab5c85ed43d21ff567ee3369fe97b6ed
    - f72ade72050a6ce63224aad2c7699160705b414c
    - f9db9f525f2bf09f2b85c91ea09f6251e00e2a95
    - fbcd460acbe8c0919f61946ac0c9ee4d8885075a
    - fff1b8681eadf590034f61ddd69ba035c6980e12

- URLs:
    - http://128.199.228.142/int/publi.php
    - http://128.199.228.142/itest/envd.php
    - http://128.199.228.142/lgimp/envd.php
    - http://128.199.228.142/vcpu/
    - http://128.199.68.249/libex/track01.wma
    - http://128.199.68.249/libex/track02.wma
    - http://157.245.44.246/cliente/IRS.php
    - http://157.245.44.246/fex/basf.msf
    - http://157.245.44.246/fex/coldplay.msf
    - http://176.57.221.92/cdd/
    - http://178.128.174.182/board/alf.cdr
    - http://178.128.174.182/board/bets.cdr
    - http://185.104.114.253/alp/
    - http://193.218.204.207/int/publi.php
    - http://2.59.41.206/fork/Material.psd
    - http://213.226.124.48/dboard/Material.psd
    - http://45.95.234.10/lofi/index.php
    - http://81.200.152.38:9000/arquivos
    - http://85.193.80.19/rpt/bdb.jpeg
    - http://85.193.83.224/dash/support.psd
    - http://85.193.95.154/odc/
    - http://85.217.170.140/may/
    - http://87.249.44.177/partic/Material.ppt
    - http://89.223.68.22/sonic/movie.wma
    - http://92.255.76.181/mag.psd
    - http://92.53.107.216/shv/
    - http://94.156.35.182/jn/
    - http://94.228.121.36/suport/
    - http://ingretationcompatible.sgp1.digitaloceanspaces.com/board.zip
    - http://jackfrostgo.fra1.digitaloceanspaces.com/thems%20(4).cdr
    - http://pexelsfiles.ams3.digitaloceanspaces.com/pexels.ppt
    - http://ryzenbootsector.fra1.digitaloceanspaces.com/ryzen%20(3).zip
    - http://s3.timeweb.com/41907bc4-clarentis/Steam.cpp
    - http://s3.timeweb.com/41907bc4-clarentis/artinos.cpp
    - http://s3.timeweb.com/41907bc4-clarentis/balarius.cpp
    - http://s3.timeweb.com/41907bc4-clouddeabril/Belcar.cpt
    - http://s3.timeweb.com/41907bc4-clouddeabril/almar.cpt
    - http://s3.timeweb.com/41907bc4-maiotronicelevation/asen.ptt
    - https://ams3.digitaloceanspaces.com/bucket202
