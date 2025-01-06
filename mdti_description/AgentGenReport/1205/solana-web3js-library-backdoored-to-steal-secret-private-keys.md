Source: [https://www.bleepingcomputer.com/news/security/solana-web3js-library-backdoored-to-steal-secret-private-keys](https://www.bleepingcomputer.com/news/security/solana-web3js-library-backdoored-to-steal-secret-private-keys)

## Related articles (describing the same threat) 
- https://www.theregister.com/2024/12/05/solana_javascript_sdk_compromised
- https://github.com/solana-labs/solana-web3.js/releases
- https://www.bleepingcomputer.com/news/security/solana-web3js-library-backdoored-to-steal-secret-private-keys
- https://www.securityweek.com/solana-web3-js-library-backdoored-in-supply-chain-attack
- https://socket.dev/blog/supply-chain-attack-solana-web3-js-library
- https://thehackernews.com/2024/12/researchers-uncover-backdoor-in-solanas.html
- https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise
- https://www.mend.io/blog/the-solana-web3-js-incident-another-wake-up-call-for-supply-chain-security
- https://www.reversinglabs.com/blog/malware-found-in-solana-npm-library-with-50m-downloads

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident 
 Solana Web3.js Library Backdoored to Steal Secret, Private Keys 

#### Root cause 
 The root cause was a social engineering/phishing attack targeting maintainers of the @solana/web3.js library. This led to a compromised publish-access account, allowing attackers to publish unauthorized and malicious versions (1.95.6 and 1.95.7) of the library, which included injected code designed to steal private and secret cryptographic keys used to secure wallets and sign transactions. *These unauthorized versions were unpublished within hours* (https://github.com/solana-labs/solana-web3.js/releases). *The attack has been formally assigned CVE-2024-54134 (CVSS-B: 8.3 High)* (https://www.theregister.com/2024/12/05/solana_javascript_sdk_compromised/). *GitHub advisory warned developers to reset all secrets and keys from a different computer due to a full system compromise* (https://www.securityweek.com/solana-web3-js-library-backdoored-in-supply-chain-attack/). *Mend tracked the issue as MSC-2024-17462 and MSC-2024-17463 and issued alerts to their customers* (https://www.mend.io/blog/the-solana-web3-js-incident-another-wake-up-call-for-supply-chain-security/). *The hacker sent spear phishing emails inviting them to collaborate on a private package, leading to the compromise* (https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise/). *Paul Roberts, Content Lead at ReversingLabs, highlighted the severity of the compromise* (https://www.reversinglabs.com/blog/malware-found-in-solana-npm-library-with-50m-downloads). 

#### Threat actor/group/campaign 
 Unknown threat actors (specific group not identified) 

#### Organization/industry/location 
 Solana, a blockchain platform and cryptocurrency organization 

#### Start date – End date 
 December 2, 2024 (from 3:20pm UTC to 8:25pm UTC) 

#### MITRE TTPs 
 ['T1071.001: Application Layer Protocol: Web Protocols (Confidence: High)', 'T1071.002: Application Layer Protocol: File Transfer Protocols (Confidence: Medium)', 'T1588.006: Obtain Capabilities: Vulnerabilities (Confidence: High)', 'T1195.002: Supply Chain Compromise: Compromise Software Dependencies and Development Tools (Confidence: High)', 'T1070.004: Indicator Removal on Host: File Deletion (Confidence: Medium)'] 

#### Impact 
 Estimated $184,000 worth of cryptocurrency stolen. Over 450,000 weekly downloads potentially impacted. *The damage was roughly $130K according to Mert Mumtaz* (https://www.mend.io/blog/the-solana-web3-js-incident-another-wake-up-call-for-supply-chain-security/). *Major wallets and apps were reportedly not affected, according to Helius CEO Mert Mumtaz* (https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise/). *51 million total recorded downloads* (https://www.reversinglabs.com/blog/malware-found-in-solana-npm-library-with-50m-downloads). 

#### Mitigation Steps 
 ['Immediately upgrade to the latest version (v1.95.8) of the @solana/web3.js library.', 'Rotate all keys, including multisigs, program authorities, and server keypairs.', 'Transfer any remaining funds from compromised wallets to new wallets.', 'Discontinue the use of any private keys that were exposed during the attack window.', 'Implement strict access controls and monitoring for publish-access accounts.', 'Regularly audit and review the security of development and deployment pipelines.', '*Developers should check their packages to ensure they do not use compromised versions* (https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise/).'] 

#### Detection Signature 
 {'Service': 'Solana Web3.js', 'Port': 'Not applicable', 'Severity': 'Critical', 'Incident': 'Solana Web3.js library backdoored', 'Signature name': '“Solana Web3.js malicious addToQueue function”', 'Internal checks': ['Verify all versions of @solana/web3.js used are v1.95.8 or later.', 'Check for the presence of the addToQueue function in the codebase.', 'Ensure code review and signing processes are in place for any updates to the library.'], 'External scanning': ['Monitor for any outbound connections to http://sol-rpc.xyz/api/rpc/queue.', 'Check for any unauthorized changes or additions in the Solana Web3.js library used in your projects.']} 

#### Additional Details 
 {"*Socket security firm reported the supply chain attack, which affected versions 1.95.6 and 1.95.7 of the library* (https://www.bleepingcomputer.com/news/security/solana-web3js-library-backdoored-to-steal-secret-private-keys/). *DataDog researcher Christophe Tafani-Dereeper identified the malicious addToQueue function* (https://www.bleepingcomputer.com/news/security/solana-web3js-library-backdoored-to-steal-secret-private-keys/). *The addToQueue function was found in fromSecretKey, fromSeed, createInstructionWithPublicKey, createInstructionWithPrivateKey functions, and the account constructor* (https://www.bleepingcomputer.com/news/security/solana-web3js-library-backdoored-to-steal-secret-private-keys/). *Solscan shows the estimated value of the stolen cryptocurrency* (https://www.bleepingcomputer.com/news/security/solana-web3js-library-backdoored-to-steal-secret-private-keys/). *Anza research firm disclosed the compromised publish-access account and emphasized the attack should not affect non-custodial wallets* (https://socket.dev/blog/supply-chain-attack-solana-web3-js-library). *Mert Mumtaz, CEO of Helius Labs, estimated the damage from this attack to be roughly $130K, while Decrypt projected $160K* (https://socket.dev/blog/supply-chain-attack-solana-web3-js-library). *The attack primarily affected dapps that updated within the window of 3:20pm UTC and 8:25pm UTC on December 2, 2024* (https://github.com/solana-labs/solana-web3.js/releases). *Malicious code exfiltrated keys via CloudFlare headers* (https://thehackernews.com/2024/12/researchers-uncover-backdoor-in-solanas.html). *The domain sol-rpc.xyz was registered on NameSilo* (https://thehackernews.com/2024/12/researchers-uncover-backdoor-in-solanas.html). *Steven Luscher, a maintainer, confirmed the phishing incident* (https://thehackernews.com/2024/12/researchers-uncover-backdoor-in-solanas.html). *Ionut Arghire, international correspondent, reported on the incident* (https://www.securityweek.com/solana-web3-js-library-backdoored-in-supply-chain-attack/). *Binance speculated that third-party tools related to private keys, including bots, might have been compromised due to timely updates of dependency packages* (https://www.securityweek.com/solana-web3-js-library-backdoored-in-supply-chain-attack/). *The attack was detected and tracked by Mend.io* (https://www.mend.io/blog/the-solana-web3-js-incident-another-wake-up-call-for-supply-chain-security/). *The incident underscores the necessity for robust supply chain security* (https://www.mend.io/blog/the-solana-web3-js-incident-another-wake-up-call-for-supply-chain-security/). *Anza published a root cause analysis describing the spear phishing technique used to compromise the npm account* (https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise/). *Differential analysis of Solana package finds malicious URLs* (https://www.reversinglabs.com/blog/malware-found-in-solana-npm-library-with-50m-downloads). *Suspicious top-level domains identified during analysis* (https://www.reversinglabs.com/blog/malware-found-in-solana-npm-library-with-50m-downloads). *The attack captured the victim's username, password, and two-factor authentication details* (https://www.theregister.com/2024/12/05/solana_javascript_sdk_compromised/). *Detected by an ecosystem team that installed the malicious version* (https://www.theregister.com/2024/12/05/solana_javascript_sdk_compromised/).": 'By following these mitigation steps and detection signatures, organizations using the Solana Web3.js library can protect themselves from similar supply chain attacks in the future.'} 

#### IoCs:
- domain: bsky.app ([link](https://www.theregister.com/2024/12/05/solana_javascript_sdk_compromised)) 

- url: https://www.npmjs.com/package/@solana/web3.js ([link](https://thehackernews.com/2024/12/researchers-uncover-backdoor-in-solanas.html)) 
Found in URL, Not found for url https://www.npmjs.com/package/@solana/web3.js in VT. 

- url: https://x.com/0xMert_/status/1864069157257613719 ([link](https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise)) 

- url: https://bsky.app/profile/christophetd.fr/post/3lcgt6l7s4c2a ([link](https://www.helpnetsecurity.com/2024/12/04/solana-web3-js-supply-chain-compromise)) 
Found in URL, Not found for url https://bsky.app/profile/christophetd.fr/post/3lcgt6l7s4c2a in VT. 

- hash_md5: GHSA-jcxm-7wvp-g6p5 ([link](https://www.theregister.com/2024/12/05/solana_javascript_sdk_compromised)) 
Found in URL, Not found for hash_md5 GHSA-jcxm-7wvp-g6p5 in VT. 

- hash_sha256: CVE-2024-54134 ([link](https://www.mend.io/blog/the-solana-web3-js-incident-another-wake-up-call-for-supply-chain-security)) 
Found in URL, Not found for hash_sha256 CVE-2024-54134 in VT. 

- domain: user-images.githubusercontent.com ([link](https://github.com/solana-labs/solana-web3.js/releases)) 

- url: https://user-images.githubusercontent.com/ ([link](https://github.com/solana-labs/solana-web3.js/releases)) 

- hash_sha1: FnvLGtucz4E1ppJHRTev6Qv4X7g8Pw6WPStHCcbAKbfx ([link](https://www.bleepingcomputer.com/news/security/solana-web3js-library-backdoored-to-steal-secret-private-keys)) 
Found in URL, Not found for hash_sha1 FnvLGtucz4E1ppJHRTev6Qv4X7g8Pw6WPStHCcbAKbfx in VT. 

- url: https://bsky.app/profile/did:plc:zwlpsxw2udovqf4mbfi4ibqf/post/3lcgt6l7s4c2a ([link](https://socket.dev/blog/supply-chain-attack-solana-web3-js-library)) 
Found in URL, Not found for url https://bsky.app/profile/did:plc:zwlpsxw2udovqf4mbfi4ibqf/post/3lcgt6l7s4c2a in VT. 

- For more IoCs, please refer to the above links. 

#### paste IoC
bsky.app
https://x.com/0xMert_/status/1864069157257613719
user-images.githubusercontent.com
https://user-images.githubusercontent.com/

