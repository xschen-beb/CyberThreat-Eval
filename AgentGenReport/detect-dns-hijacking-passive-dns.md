Source: [https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns)

## Related articles (describing the same threat) 
- https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns
- https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/

## Enriched Doc (enrihcments marked with *content*(link)): 
#### Incident: DNS Hijacking Attacks 

#### Root cause 
 The root cause behind the incidents is the hijacking of DNS records through various methods such as stealing domain owners' credentials at registrars or DNS service providers, or infiltrating these services. Other methods include DNS cache poisoning and MitM attacks. *Our detection pipeline processed 29 billion records, identifying 6,729 hijacking instances using machine learning* (https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/). 

#### Threat actor/group/campaign 
 Groups such as Garuda Security and other unspecified groups performing these hijacking attacks. *Same group likely responsible for attacks on a utility company and ISP, and the Democratic Coalition's domain* (https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/). 

#### Organization/industry/location 
 The victims include a Hungarian political party, a large utility company in the U.S., a large ISP, a university, and a research center. *Additional victims include a major Brazilian bank and various domains hijacked for illicit gambling campaigns* (https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/). 

#### Start date – End date 
 Specific dates mentioned include March 27, 2024 – September 21, 2024. 

#### MITRE TTPs 
 T1071.004 (Application Layer Protocol - DNS), T1557.002 (Adversary-in-the-Middle: DNS Hijacking), T1071.001 (Application Layer Protocol - Web Traffic) 

#### Impact 
 The impact includes the redirection of users to malicious servers, hosting of phishing pages, website defacement, and illicit content distribution. *Hijacked domains also used for phishing, drive-by downloads, and illicit gambling* (https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/). 

#### Mitigation Steps 
 1. Implement DNSSEC to ensure DNS integrity. 2. Use strong, unique passwords and enable multi-factor authentication for accounts related to domain management. 3. Regularly monitor DNS records for unauthorized changes. 4. Ensure that DNS queries and responses are encrypted using protocols such as DoH (DNS over HTTPS) and DoT (DNS over TLS). 5. Work with DNS service providers to implement security measures. 6. Employ a DNS firewall to block malicious DNS activity. 7. Utilize security solutions like Palo Alto Networks' Next-Generation Firewall and Advanced DNS Security for automated detection and protection. 

#### Detection Signature 
 Service: DNS Port: 53 Severity: Critical Incident: DNS Hijacking Signature name: 'Suspicious DNS Record Changes' Internal checks: - Monitoring of DNS record changes for unauthorized modifications. - Ensuring DNS service provider security. - Implementing regular audits of DNS records. External scanning: - Detecting unusual DNS record changes. - Monitoring for DNS queries to unexpected IP addresses. 

#### IoCs: 
- domain: c-sharp.in ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- ip: 139.59.255.10 ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: ccdc.org.do ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- ip: 135.148.57.147 ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- ip: 152.70.176.210 ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: mail.uts.ac.id ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- ip: 159.223.92.200 ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: ns1.uts.ac.id ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: ns2.uts.ac.id ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: ns3.uts.ac.id ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: ns4.uts.ac.id ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: ns5.uts.ac.id ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: ns6.uts.ac.id ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: uts.ac.id ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- ip: 176.9.24.28 ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: ns1.csit-host.com ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 

- domain: ns2.csit-host.com ([link](https://unit42.paloaltonetworks.com/detect-dns-hijacking-passive-dns/)) 


