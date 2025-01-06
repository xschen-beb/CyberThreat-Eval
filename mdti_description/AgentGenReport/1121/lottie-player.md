Source: [https://www.reversinglabs.com/blog/differential-analysis-raises-red-flags-over-lottiefiles/lottie-player](https://www.reversinglabs.com/blog/differential-analysis-raises-red-flags-over-lottiefiles/lottie-player)

## Related articles (describing the same threat) 
- https://github.com/LottieFiles/lottie-player/issues/254
- https://forum.lottiefiles.com/t/the-problem-of-someone-elses-popup-appearing/6470/3
- https://www.sonatype.com/blog/lottie-player-compromised-in-supply-chain-attack-all-you-need-to-know
- https://www.theregister.com/2024/10/31/lottiefiles_supply_chain_attack
- https://lottiefiles.com/blog/inside-lottiefiles/resolution-of-security-incident-with-lottiefiles-lottie-player-package
- https://www.techtarget.com/searchsecurity/news/366614668/Lottie-Player-NPM-package-compromised-in-supply-chain-attack
- https://www.reversinglabs.com/blog/differential-analysis-raises-red-flags-over-lottiefiles/lottie-player
- https://snyk.io/blog/lottie-player-npm-package-compromised-crypto-wallet-theft
- https://thehackernews.com/2024/10/lottiefiles-issues-warning-about.html
- https://www.securityweek.com/lottie-player-supply-chain-attack-targets-cryptocurrency-wallets

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: @lottiefiles/lottie-player Supply Chain Attack 

#### Root cause 
 A compromised access token from a highly privileged developer, Aidosmf (aidosmf@gmail.com), allowed attackers to publish malicious versions of the @lottiefiles/lottie-player package on npm, designed to steal crypto wallet assets. *The attack stemmed from a phishing attack on an employee's NPM account* (https://www.securityweek.com/lottie-player-supply-chain-attack-targets-cryptocurrency-wallets/). *The employee's laptop was quarantined* (https://www.securityweek.com/lottie-player-supply-chain-attack-targets-cryptocurrency-wallets/). *Exaforce was engaged for rapid Incident Response and ongoing cloud detection and response* (https://lottiefiles.com/blog/inside-lottiefiles/resolution-of-security-incident-with-lottiefiles-lottie-player-package). *Attack leveraged an npm automation token to bypass 2FA controls* (https://thehackernews.com/2024/10/lottiefiles-issues-warning-about.html). 

#### Threat actor/group/campaign 
 Not specified in the report. 

#### Organization/industry/location 
 Victims are developers and users of the @lottiefiles/lottie-player package, for embedding and playing Lottie animations and Telegram Sticker animations on websites. *Nattu Adnan, co-founder and CTO at LottieFiles confirmed the attack* (https://www.theregister.com/2024/10/31/lottiefiles_supply_chain_attack/). *1inch confirmed some of its users were affected by the supply chain attack* (https://www.techtarget.com/searchsecurity/news/366614668/Lottie-Player-NPM-package-compromised-in-supply-chain-attack). *Checkmarx identified the attack leveraging an npm automation token* (https://thehackernews.com/2024/10/lottiefiles-issues-warning-about.html). 

#### Start date – End date 
 October 2024 

#### MITRE TTPs 
 ['T1078.004 (Valid Accounts: Cloud Accounts) - Confidence score: 80%', 'T1556.004 (Credential Access: Access Token Manipulation) - Confidence score: 75%', 'T1190 (Exploit Public-Facing Application) - Confidence score: 70%', 'T1071.001 (Application Layer Protocol: Web Protocols) - Confidence score: 65%'] 

#### Impact 
 Malicious versions of the package led to users potentially having their crypto wallet assets stolen when connecting their wallets to the compromised @lottiefiles/lottie-player package. *Web3 security platform Scam Sniffer detected a transaction showing a victim losing 10 Bitcoin ($722,508)* (https://www.theregister.com/2024/10/31/lottiefiles_supply_chain_attack/). Unauthorized versions were published on October 30, 2024, affecting users who accessed the library via CDNs without a pinned version, leading to unauthorized access attempts to Meta wallets and references to Cryptocurrency wallets. The malicious code targeted app.1inch.io, aiming to connect to users' crypto wallets, add new blockchain networks, and enable interaction with smart contracts (*The changes* (https://github.com/LottieFiles/lottie-player/issues/254)). *LottieFiles warned users that attackers injected malicious code into versions 2.0.5, 2.0.6, and 2.0.7* (https://www.techtarget.com/searchsecurity/news/366614668/Lottie-Player-NPM-package-compromised-in-supply-chain-attack). *73 npm packages are dependent on the package* (https://snyk.io/blog/lottie-player-npm-package-compromised-crypto-wallet-theft/). *dotLottie Player recommended for better performance and security* (https://lottiefiles.com/blog/inside-lottiefiles/resolution-of-security-incident-with-lottiefiles-lottie-player-package). *Attack bypassed 2FA by using npm automation token* (https://thehackernews.com/2024/10/lottiefiles-issues-warning-about.html). 

#### Mitigation Steps 
 ['Pin dependencies to a specific, known-good version or range of versions instead of using @latest.', 'Regularly update dependencies after vetting them for malicious implants.', 'Conduct security assessments to verify the integrity and quality of public, open-source libraries before they are used.', 'Implement strong access controls and monitor for unusual activity on developer accounts.', 'Utilize tools like Spectra Assure CLI to perform differential analysis and detect potential malicious changes in packages.', 'Update to version 2.0.8, a secure copy of 2.0.4, to ensure stability and security for users accessing the latest tag through CDNs. The compromised versions have been removed from npmjs.com and jsDeliver, with CDNJS redirecting affected versions to 2.0.8. *Sonatype Repository Firewall and Sonatype Lifecycle were noted to block malicious versions from entering builds, protecting users* (https://www.sonatype.com/blog/lottie-player-compromised-in-supply-chain-attack-all-you-need-to-know). *LottieFiles recommended users remove all access and associated tokens/services accounts of the impacted developer* (https://www.techtarget.com/searchsecurity/news/366614668/Lottie-Player-NPM-package-compromised-in-supply-chain-attack). *Snyk CLI can be utilized to identify if the malicious versions are used* (https://snyk.io/blog/lottie-player-npm-package-compromised-crypto-wallet-theft/).', 'Adopt a Content Security Policy to prevent unwanted and untrusted sources from injecting scripts, image tags, and other objects into your web application.', '*Revoke NPM keys and developer access to NPM repositories* (https://www.securityweek.com/lottie-player-supply-chain-attack-targets-cryptocurrency-wallets/).', '*Publish clean version 2.0.8 and coordinated removal of infected files with CDN providers* (https://lottiefiles.com/blog/inside-lottiefiles/resolution-of-security-incident-with-lottiefiles-lottie-player-package).', '*Contact priority_support@lottiefiles.com for assistance* (https://lottiefiles.com/blog/inside-lottiefiles/resolution-of-security-incident-with-lottiefiles-lottie-player-package).'] 

#### Detection Signature 
 {'Service': 'npm', 'Port': 'N/A', 'Severity': 'Critical', 'Incident': 'Supply Chain Attack on @lottiefiles/lottie-player', 'Signature name': 'npm package version tampering', 'Internal checks': ['Ensure access tokens are managed securely and rotated regularly.', 'Implement multi-factor authentication for all developer accounts.', 'Conduct regular audits of package versions and code changes.'], 'External scanning': ['Monitor npm package versions for unexpected changes.', 'Detect presence of malicious behaviors or unusual URLs related to Bitcoin exchange services in package code. *Liran Tal discussed the attack* (https://snyk.io/blog/lottie-player-npm-package-compromised-crypto-wallet-theft/).']} 

#### IoCs:
- hash_sha1: 846f2efc0212317b5e44690234995ba7e269dee3 ([link](https://secure.software/npm/packages/@lottiefiles/lottie-player/2.0.7)) 

- hash_sha1: 5bbd2290a7de5a4736fdafe171f5b6eae6abc27e ([link](https://secure.software/npm/packages/@lottiefiles/lottie-player/2.0.6)) 

- hash_sha1: 446996c35a4188647361733b4c7175b2aeea9611 ([link](https://secure.software/npm/packages/@lottiefiles/lottie-player/2.0.5)) 

- url: https://cdnjs.cloudflare.com/ajax/libs/lottie-player/2.0.4/lottie-player.min.js ([link](https://forum.lottiefiles.com/t/the-problem-of-someone-elses-popup-appearing/6470/3)) 

- For more IoCs, please refer to the above links. 

#### Additional Info 
 *The attack was reported by Ax Sharma, a security researcher and malware analyst at Sonatype* (https://www.sonatype.com/blog/lottie-player-compromised-in-supply-chain-attack-all-you-need-to-know). *Wiz researchers identified the attack and confirmed it was initiated on Wednesday* (https://www.techtarget.com/searchsecurity/news/366614668/Lottie-Player-NPM-package-compromised-in-supply-chain-attack). *Polyfill library was similarly attacked in June 2024* (https://snyk.io/blog/lottie-player-npm-package-compromised-crypto-wallet-theft/). 

#### paste IoC
IoC Type	IoC Value	Source Link
hash_sha1	846f2efc0212317b5e44690234995ba7e269dee3	https://secure.software/npm/packages/@lottiefiles/lottie-player/2.0.7
hash_sha1	5bbd2290a7de5a4736fdafe171f5b6eae6abc27e	https://secure.software/npm/packages/@lottiefiles/lottie-player/2.0.6
hash_sha1	446996c35a4188647361733b4c7175b2aeea9611	https://secure.software/npm/packages/@lottiefiles/lottie-player/2.0.5
url	https://cdnjs.cloudflare.com/ajax/libs/lottie-player/2.0.4/lottie-player.min.js	https://forum.lottiefiles.com/t/the-problem-of-someone-elses-popup-appearing/6470/3

