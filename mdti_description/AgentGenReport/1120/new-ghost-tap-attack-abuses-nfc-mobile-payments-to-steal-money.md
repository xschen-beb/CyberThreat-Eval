Source: [https://www.bleepingcomputer.com/news/security/new-ghost-tap-attack-abuses-nfc-mobile-payments-to-steal-money](https://www.bleepingcomputer.com/news/security/new-ghost-tap-attack-abuses-nfc-mobile-payments-to-steal-money)

## Related articles (describing the same threat) 
- https://www.bleepingcomputer.com/news/security/new-ghost-tap-attack-abuses-nfc-mobile-payments-to-steal-money
- https://www.threatfabric.com/blogs/ghost-tap-new-cash-out-tactic-with-nfc-relay
- https://www.bankinfosecurity.com/criminals-ghost-tap-nfc-for-payment-cash-out-attacks-a-26860
- https://thehackernews.com/2024/11/ghost-tap-hackers-exploiting-nfcgate-to.html

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Ghost Tap Attack 

#### Root cause 
 The root cause is the use of stolen NFC card data, relayed through money mules, utilizing banking malware to steal card data and OTPs. Attackers use relay servers to obfuscate their location, leveraging the NFCGate tool to relay payment card information and employing 'airplane mode' to evade tracking *Your changes* (https://www.bleepingcomputer.com/news/security/new-ghost-tap-attack-abuses-nfc-mobile-payments-to-steal-money/). *Cybercriminals also exploit legitimate research tools like NFCGate for malicious purposes, scaling the cash-out process and remaining anonymous* (https://www.threatfabric.com/blogs/ghost-tap-new-cash-out-tactic-with-nfc-relay). *The stolen information is relayed between devices using NFCGate, enabling anonymous cash-outs on a larger scale* (https://thehackernews.com/2024/11/ghost-tap-hackers-exploiting-nfcgate-to.html). *Hackers transmit stolen card data in real-time to money mules* (https://www.bankinfosecurity.com/criminals-ghost-tap-nfc-for-payment-cash-out-attacks-a-26860). 

#### Threat actor/group/campaign 
 Threat actors using the 'Ghost Tap' technique, potentially overlapping with those who used NGate malware. Discovered by Threat Fabric *Your changes* (https://www.bleepingcomputer.com/news/security/new-ghost-tap-attack-abuses-nfc-mobile-payments-to-steal-money/). *Cybercriminals are leveraging tools initially designed for research, like NFCGate, to conduct large-scale fraud* (https://www.threatfabric.com/blogs/ghost-tap-new-cash-out-tactic-with-nfc-relay). *The Dutch security company noted the misuse of NFCGate, as documented by ESET in August 2024* (https://thehackernews.com/2024/11/ghost-tap-hackers-exploiting-nfcgate-to.html). *Attackers recruit teenagers and unemployed individuals for risky on-site transactions* (https://www.bankinfosecurity.com/criminals-ghost-tap-nfc-for-payment-cash-out-attacks-a-26860). 

#### Organization/industry/location 
 Victims are individuals using mobile payment systems like Apple Pay and Google Pay. 

#### Start date – End date 
 November 20, 2024 (reported date, exact start date unknown) 

#### MITRE TTPs 
 ['T1071.001 (Application Layer Protocol: Web Protocols)', 'T1071.003 (Application Layer Protocol: Mail Protocols)', 'T1071.004 (Application Layer Protocol: DNS)', 'T1071.005 (Application Layer Protocol: Web Services)', 'T1114.001 (Email Collection: Local Email Collection)', 'T1114.002 (Email Collection: Remote Email Collection)', 'T1119 (Automated Collection)', 'T1214 (Credentials in Files)', 'T1411 (Phishing for Information)', 'T1416 (Input Capture)'] 

#### Impact 
 The total amount lost can be significant if the attack is applied at scale, potentially involving thousands of small fraudulent transactions across various locations globally. *The tactic allows purchasing gift cards at offline retailers without physical presence* (https://thehackernews.com/2024/11/ghost-tap-hackers-exploiting-nfcgate-to.html). *Hackers use faster cell phone networks and lack of response lag detection in ATM and POS terminals to facilitate these attacks* (https://www.bankinfosecurity.com/criminals-ghost-tap-nfc-for-payment-cash-out-attacks-a-26860). 

#### Mitigation Steps 
 ['Flag transactions made from the same card at locations that are not physically possible to get to in the timeframe between charges.', 'Monitor for unusual transaction patterns and small payments across multiple locations.', 'Implement robust anti-fraud mechanisms to detect and block suspicious transactions.', 'Educate consumers on recognizing and reporting fraudulent transactions promptly to minimize losses.', 'Ensure mobile payment systems have strong authentication methods to prevent unauthorized access.'] 

#### Detection Signature 
 {'Service': 'Mobile Payment Systems (Apple Pay, Google Pay)', 'Port': 'Not applicable (NFC-based attacks)', 'Severity': 'Critical', 'Incident': 'Ghost Tap Attack', 'Signature name': 'Ghost Tap NFC Relay Attack', 'Internal checks': ['Setting1: Monitor for unusual transaction locations – In the payment processing system', 'Setting2: Monitor for physical impossibilities in transaction locations – In the payment processing system', 'Setting3: Implement strong authentication for NFC transactions – In the payment processing system'], 'External scanning': ['Monitor cybercrime forums for money mule recruitment', 'Analyze transaction patterns for potential relay attacks']} 

#### IoCs: No IoCs found. 


