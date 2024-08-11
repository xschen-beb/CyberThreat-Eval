Source: [https://yoroi.company/research/ducktail-dissecting-a-complex-infection-chain-started-from-social-engineering/](https://yoroi.company/research/ducktail-dissecting-a-complex-infection-chain-started-from-social-engineering/)

# DuckTail Dissecting a Complex Infection Chain Started From Social Engineering

Incident: DuckTail: Dissecting a complex infection chain started from social engineering

Root cause: Social Engineering leading to malware installation

Impact: Business social media accounts compromised. Specific numbers of impacted devices or people and financial losses are not mentioned.

Mitigation: 
1. User Education: Educate users about the risks of social engineering and the importance of not clicking on suspicious links or downloading files from unknown sources.
2. Use Advanced Security Measures: Implement advanced threat protection solutions to detect and prevent malware.
3. Regular Updates: Ensure that all software and systems are regularly updated.
4. Strong Authentication: Use strong, multi-factor authentication for social media accounts.
5. Network Segmentation: Segment the network to limit the spread of malware.
6. Continuous Monitoring: Implement continuous monitoring and threat hunting to detect suspicious activities.
7. Incident Response Plan: Develop and maintain an incident response plan to handle potential security breaches.

Detection Signature:
Service: Web Hosting Services (e.g., Mediafire, Google Cloud, etc.)
Port: Not specified
Severity: Critical
Incident: DuckTail Malware Campaign
Signature name: “DuckTail malware distribution”
Internal checks:
   - Setting1: Ensure social media accounts are monitored for unusual activities.
   - Setting2: Educate employees about phishing and social engineering attacks.
   - Setting3: Use URL filtering to block access to known malicious domains.
External scanning:
   - Monitor for access to known malicious domains.
   - Detect and block downloads from suspicious file hosting services.

IoCs:
   - Fake File Hosting Domains:
     - download5s.]com
     - x-photos.]net
     - beautygirls-photos.]com
     - beautygirls-picture.]com
     - photo-cam.]com
     - x-album.]com
     - x-albums.]com
     - x-pictures.]net
     - hxxps://sites.google.]com/view/lonely-in-car
   - True Hosting Domains:
     - s1-download-photos.]com
     - jmooreassoc.]com
     - meetstaci.]com
     - kimhasa.]com
     - notodaiya.]com
     - karbilyazilim.]com
     - shble.]com
     - velascasadelaluz.]com
     - hxxps://download2388.mediafire.]com/eif5tfodd4ng/hrcyyor418tp8hw/Album_Beautiful_Girl_In_The_Hotels.rar
     - romeflirt.]com
     - ikejd.]com
     - hxxps://storage.googleapis.]com/migc/AlbumNo6128183.zip
   - Pages:
     - camliveproduction
     - The-Best-moment-105684484236827
     - xphotonetn
   - DuckTail Python:
     - fcec8d28e17f7af13d0961eb8b8d25eaf0e76e50fdc8cd4e2e79de7d6b67d25d (Archive)
     - c17524501439d58ffb701907d83e3e20558a445363fa0733bb328e0d69c91441 (InnoSetup Installer)
     - e1517e6bd6169c543083e36c45894a98b8ae592bf9dc265978f198af70a853b1 (DuckTail)
   - DuckTail PHP:
     - 0fad31fc16beeb24ca924a94614f3905f5c463a972ae395eec58614d014e73ad (Malicious DLL)
     - cb807472bb6d4d1113fcbc209d6a08fa80ff9e53c83b1aa37f9d6f549affd68c (Legitimate WDSyncService Tool)
     - 8c60a4691f610e325597af83ee2c99945e7eb1cb189fff03cf2264e461fead53 (InnoSetup Sample)
     - 16ad22f8ab4f99a03bc2b68bf3314397f30f67a01bb5a283020e85979b811d93 (Rust Sample)
     - 4abdb3f59e3433b2d410106c75d4711574e0b61b0ef92653b9971154d9841a4f (index.php)
     - 52bd6d7d8c9fe087ba64adafbfa623e49b69425829b8c9c8a8eadb2e06669892 (include.php)
     - 5bac0b4ee00c1cb9a5b2969a18077ab74257790bd2610224253d3faf58714f43 (index.php not obfuscated)
     - 8fd4910dd8b05c9ea617f9b86f31aac5663db12495e9295ccaf19e3d58b8b3b4 (include.php not obfuscated)
   - C2:
     - rapadtrai.]com
     - graeslavur.]com
     - caseiden.]com
     - te5.techgeetam.]com
     - sensetria.]com
