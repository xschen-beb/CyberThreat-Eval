Source: [https://www.cadosecurity.com/tracking-diicot-an-emerging-romanian-threat-actor/](https://www.cadosecurity.com/tracking-diicot-an-emerging-romanian-threat-actor/)

# Tracking Diicot An Emerging Romanian Threat Actor

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Diicot Campaign Targeting SSH Servers 

 Root cause: The root cause includes misconfigured SSH servers with password authentication enabled, making them susceptible to brute-force attacks via weak SSH credentials *weak SSH credentials* (https://www.bitdefender.co.uk/blog/labs/how-we-tracked-a-threat-group-running-an-active-cryptojacking-campaign/). 

 Threat Actor/group/campaign: Diicot (formerly known as Mexals), a Romanian-based group *Romanian-based* (https://www.cadosecurity.com/blog/tracking-diicot-an-emerging-romanian-threat-actor). Diicot shares its name with the Romanian anti-terrorism policing unit and uses similar messaging and imagery *shares its name* (https://hackread.com/diicot-hackers-ssh-servers-brute-force-malware/). Diicot has traditionally been associated with cryptojacking campaigns but has expanded to deploying a Mirai-based bot named Cayosin targeting OpenWrt routers *Mirai-based bot* (https://securityaffairs.com/147581/cyber-crime/diicot-gang-attack-capabilities.html). *The group employs Mirai-style spreader scripts for propagation* (https://advisory.eventussecurity.com/advisory/cryptojacking-to-ddos-attacks-diicot-expands-tactics-with-cayosin-botnet/). 

 Organization/industry/location: Multiple organizations with internet-exposed SSH servers, especially those using default or easily guessed credentials. 

 Start date – End date: The campaign is ongoing, with notable activity observed on April 26, 2023, and updates noted on May 27 and June 5, 2023. 

 MITRE TTPs: - Initial Access: T1078.001 (Valid Accounts: Default Accounts)
- Execution: T1059.004 (Command and Scripting Interpreter: UNIX Shell)
- Persistence: T1098.004 (Account Manipulation: SSH Authorized Keys)
- Exfiltration: T1041 (Exfiltration Over C2 Channel)
- Impact: T1486 (Data Encrypted for Impact) 

 Impact: Details about the exact number of impacted devices or financial losses are not provided, but the campaign involves widespread cryptojacking and doxxing activities. Evidence also shows deployment of a botnet agent named Cayosin for DDoS attacks *Cayosin* (https://www.cadosecurity.com/blog/tracking-diicot-an-emerging-romanian-threat-actor), as well as a Monero cryptominer valued at approximately US$10,000 in XMR *US$10,000 in XMR* (https://www.akamai.com/blog/security-research/mexals-cryptojacking-malware-resurgence). *The payload scripts change user passwords and remove prior compromise artifacts* (https://advisory.eventussecurity.com/advisory/cryptojacking-to-ddos-attacks-diicot-expands-tactics-with-cayosin-botnet/). 

 Mitigation: 1. Implement mandatory key-based authentication for SSH instances.
2. Apply firewall rules to restrict SSH access to specific IP addresses.
3. Regularly update and patch SSH servers and related software.
4. Monitor network traffic for signs of brute-force attacks and unusual outbound connections.
5. Deploy intrusion detection/prevention systems (IDS/IPS) to identify and block malicious activities. 

 Detailed Steps for mitigation: 1. **Enforce Key-Based Authentication:**
   - Disable password authentication by editing the `/etc/ssh/sshd_config` file:
     ```bash
     PasswordAuthentication no
     ```
   - Restart the SSH service:
     ```bash
     sudo systemctl restart sshd
     ```
2. **Restrict SSH Access:**
   - Configure firewall rules to allow SSH access only from trusted IP addresses:
     ```bash
     sudo ufw allow from <trusted_ip> to any port 22
     ```
3. **Regular Updates:**
   - Regularly update the system and SSH service:
     ```bash
     sudo apt-get update && sudo apt-get upgrade
     ```
4. **Network Monitoring:**
   - Implement network monitoring tools like Wireshark or Zeek to detect unusual traffic patterns.
5. **Deploy IDS/IPS:**
   - Use tools like Snort or Suricata to detect and block malicious activities. 

 Detection Signature: ```plaintext
Service: SSH
Port: 22, 2000
Severity: Critical
Incident: Diicot SSH Brute-force
Signature name: “SSH brute-force detection”
Internal checks:
  - Setting1: Ensure SSH password authentication is disabled.
  - Setting2: Restrict SSH access to specific IP addresses.
  - Setting3: Monitor login attempts and unusual activity in SSH logs.
External scanning:
  - Large number of failed login attempts.
  - Unusual outbound connections to known C2 servers or mining pools.
``` 

 IoCs: - **Discord Webhooks:**
  - hxxps://discord[.]com/api/webhooks/1100669270297419808/UQ2bkUBe9JgAhtEIPYqpqKG6YVRW1fqEkadAY3u6PPmcgEVcYaSRiS37JILi2Vk32or6
  - hxxps://discord[.]com/api/webhooks/1100666861424754708/pAzInuz8ekK5DmKyoKxmG4H8euCtLkBXZnS33EGnxdl0_hkL5OdRbInQqgdGiQ1U41WF
  - hxxps://discord[.]com/api/webhooks/1100666766339866694/ex_yUegpCF4NXGkT3sGFp3oWFUkJWE7XarcgTHRcAwmJQtG4pALhcj6PjKUTthNz_0u_
  - hxxps://discord[.]com/api/webhooks/1100666664623812650/_t9NyLTT_Rbg_Vr14n6YCBkseXrz-RpSe94SFIw-1Pyrkns80tU9uWJL3yjc3eLXo0IU
- **URLs:**
  - arhivehaceru[.]com
- **Files and Hashes:**
  - Update: 437af650493492c8ef387140b5cb2660044764832d1444e5265a0cd3fe6e0c39
  - aliases: de6dff4d3de025b3ac4aff7c4fab0a9ac4410321f4dca59e29a44a4f715a9864
  - Chrome: 14779e087a764063d260cafa5c2b93d7ed5e0d19783eeaea6abb12d17561949a
  - History: e9bbe9aecfaea4c738d95d0329a5da9bd33c04a97779172c7df517e1a808489c
  - .diicot: 7389e3aada70d58854e161c98ce8419e7ab8cd93ecd11c2b0ca75c3cafed78cb
  - bins.sh: 180d30bf357bc4045f197b26b1b8941af9ca0203226a7260092d70dd15f3e6ab
  - cutie.x86_64: 7d93419e78647d3cdf2ff53941e8d5714afe09cb826fd2c4be335e83001bdabf
  - payload: d0e8a398a903f1443a114fa40860b3db2830488813db9a87ddcc5a8a337edd73
  - Opera: aabf2ef1e16a88ae0d802efcb2525edb90a996bb5d280b4c61d2870351e3fba4
- **IP addresses:**
  - 45[.]88[.]67[.]94
  - 84[.]54[.]50[.]198
- **SSH Keys:**
  - ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAoBjnno5GBoIuIYIhrJsQxF6OPHtAbOUIEFB+gdfb1tUTjs+f9zCMGkmNmH45fYVukw6IwmhTZ+AcD3eD  

 Mining Pools: - 45[.]88[.]67[.]94:7777
  - 139[.]99[.]123[.]196:80
  - pool[.]supportxmr[.]com:80
- **Paths:**
  - /var/tmp/Documents/
  - /var/tmp/Documents/.b4nd1d0
  - /var/tmp/Documents/.5p4rk3l5
  - /var/tmp/Documents/Opera
  - /var/tmp/Documents/.diicot
  - /var/tmp/.update-logs
  - /tmp/...
  - /var/tmp/.ladyg0g0/
  - /var/tmp/.ladyg0g0/.pr1nc35
  - /lib/systemd/system/myservice.service
  - /usr/bin/.pidsclip
  - /usr/bin/.locatione
- **Additional TTPs:**
  Diicot's recent campaign includes deployment of a self-propagating initial access tool *self-propagating initial access tool* (https://www.cadosecurity.com/blog/tracking-diicot-an-emerging-romanian-threat-actor), use of custom packers to obfuscate binary payloads *custom packers* (https://hackread.com/diicot-hackers-ssh-servers-brute-force-malware/), and deployment of a botnet agent named Cayosin targeting OpenWrt routers *OpenWrt* (https://www.cadosecurity.com/blog/tracking-diicot-an-emerging-romanian-threat-actor). The group also uses a custom API endpoint for C2 reporting *Custom API endpoint* (https://www.cadosecurity.com/blog/tracking-diicot-an-emerging-romanian-threat-actor), and a LAN spreader module *LAN spreader module* (https://www.akamai.com/blog/security-research/mexals-cryptojacking-malware-resurgence), with their servers hosted in a Netherlands-based VPS *Netherlands-based VPS* (https://www.akamai.com/blog/security-research/mexals-cryptojacking-malware-resurgence). The campaign utilizes a Golang SSH bruteforcer *Golang SSH bruteforcer* (https://www.bitdefender.co.uk/blog/labs/how-we-tracked-a-threat-group-running-an-active-cryptojacking-campaign/) distributed via a centralized API server *centralized API server* (https://www.bitdefender.co.uk/blog/labs/how-we-tracked-a-threat-group-running-an-active-cryptojacking-campaign/). Additionally, the group employs the Shell Script Compiler to make loader scripts difficult to analyze and packs payloads with a custom version of UPX using a modified header with the byte sequence 0x59545399 *Shell Script Compiler; custom version of UPX; 0x59545399* (https://hackread.com/diicot-hackers-ssh-servers-brute-force-malware/). Diicot also uses Snowflake timestamps in Discord links for data exfiltration and campaign statistics *Snowflake timestamps* (https://hackread.com/diicot-hackers-ssh-servers-brute-force-malware/). Additionally, Cado Labs identified the use of a customized internet scanner named Chrome based on Zmap *Zmap* and a custom SSH brute-forcing tool named aliases *aliases* (https://securityaffairs.com/147581/cyber-crime/diicot-gang-attack-capabilities.html). *The group automates through cronjobs and systemd services* (https://advisory.eventussecurity.com/advisory/cryptojacking-to-ddos-attacks-diicot-expands-tactics-with-cayosin-botnet/). 


# Related articles (describing the same threat) 
['https://www.cadosecurity.com/tracking-diicot-an-emerging-romanian-threat-actor/', 'https://www.cadosecurity.com/blog/tracking-diicot-an-emerging-romanian-threat-actor', 'https://www.akamai.com/blog/security-research/mexals-cryptojacking-malware-resurgence', 'https://www.bitdefender.co.uk/blog/labs/how-we-tracked-a-threat-group-running-an-active-cryptojacking-campaign/', 'https://hackread.com/diicot-hackers-ssh-servers-brute-force-malware/', 'https://securityaffairs.com/147581/cyber-crime/diicot-gang-attack-capabilities.html', 'https://advisory.eventussecurity.com/advisory/cryptojacking-to-ddos-attacks-diicot-expands-tactics-with-cayosin-botnet/']
