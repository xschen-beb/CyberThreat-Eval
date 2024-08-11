Source: [https://www.cadosecurity.com/tracking-diicot-an-emerging-romanian-threat-actor/](https://www.cadosecurity.com/tracking-diicot-an-emerging-romanian-threat-actor/)

# Tracking Diicot An Emerging Romanian Threat Actor

### Incident: Diicot Malware Campaign

**Root Cause:** Misconfigured SSH services with weak or default credentials, and exposed internet-facing SSH ports.

**Impact:** This campaign had a significant impact, compromising numerous devices globally. The exact number of devices and the financial losses are not specified in the blog, but the widespread nature of the campaign suggests potentially severe consequences, including loss of compute resources due to cryptojacking, disrupted services from DDoS attacks, and exposure of personal information through doxxing.

**Mitigation:** 

**1. Secure SSH Configuration:**
   - Disable password authentication for SSH and enforce key-based authentication.
   - Limit SSH access using firewall rules to specific IP addresses.
   - Regularly update and patch all SSH services.

**2. Network Monitoring:**
   - Implement network monitoring to detect unusual traffic patterns, such as large volumes of SYN packets indicative of internet scanning.

**3. Use Strong, Unique Passwords:**
   - Ensure that all devices and services use strong, unique passwords, and avoid default credentials.

**4. Incident Response Plan:**
   - Develop and rehearse an incident response plan to quickly isolate and remediate infected systems.

**5. Regular Audits:**
   - Conduct regular security audits and vulnerability assessments to identify and mitigate potential weaknesses.

### Detection Signature:
- **Service:** SSH
- **Port:** 22, 2000
- **Severity:** Critical
- **Incident:** Diicot Malware Campaign
- **Signature name:** “SSH Brute Force Attack”
- **Internal checks:**
  - **Setting1:** SSH should use key-based authentication.
  - **Setting2:** SSH should not be accessible from the external internet except from trusted IPs.
  - **Setting3:** SSH should have strong, unique passwords if password authentication is enabled.
- **External scanning:**
  - Open ports (22, 2000)
  - High volume of failed login attempts

### IoCs:
**Discord Webhooks:**
- hxxps://discord[.]com/api/webhooks/1100669270297419808/UQ2bkUBe9JgAhtEIPYqpqKG6YVRW1fqEkadAY3u6PPmcgEVcYaSRiS37JILi2Vk32or6
- hxxps://discord[.]com/api/webhooks/1100666861424754708/pAzInuz8ekK5DmKyoKxmG4H8euCtLkBXZnS33EGnxdl0_hkL5OdRbInQqgdGiQ1U41WF
- hxxps://discord[.]com/api/webhooks/1100666766339866694/ex_yUegpCF4NXGkT3sGFp3oWFUkJWE7XarcgTHRcAwmJQtG4pALhcj6PjKUTthNz_0u_
- hxxps://discord[.]com/api/webhooks/1100666664623812650/_t9NyLTT_Rbg_Vr14n6YCBkseXrz-RpSe94SFIw-1Pyrkns80tU9uWJL3yjc3eLXo0IU

**URLs:**
- arhivehaceru[.]com

**Files SHA-256:**
- Update: 437af650493492c8ef387140b5cb2660044764832d1444e5265a0cd3fe6e0c39
- aliases: de6dff4d3de025b3ac4aff7c4fab0a9ac4410321f4dca59e29a44a4f715a9864
- aliases (variant): a163da5c4d6ee856a06e4e349565e19a704956baeb62987622a2b2c43577cdee
- Chrome: 14779e087a764063d260cafa5c2b93d7ed5e0d19783eeaea6abb12d17561949a
- History: e9bbe9aecfaea4c738d95d0329a5da9bd33c04a97779172c7df517e1a808489c
- .diicot: 7389e3aada70d58854e161c98ce8419e7ab8cd93ecd11c2b0ca75c3cafed78cb
- bins.sh: 180d30bf357bc4045f197b26b1b8941af9ca0203226a7260092d70dd15f3e6ab
- cutie.x86_64: 7d93419e78647d3cdf2ff53941e8d5714afe09cb826fd2c4be335e83001bdabf
- payload: d0e8a398a903f1443a114fa40860b3db2830488813db9a87ddcc5a8a337edd73

**IP addresses:**
- 45[.]88[.]67[.]94
- 84[.]54[.]50[.]198

**SSH Keys:**
- ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAoBjnno5GBoIuIYIhrJsQxF6OPHtAbOUIEFB+gdfb1tUTjs+f9zCMGkmNmH45fYVukw6IwmhTZ+AcD3eD "iImmgU9wlw/lalf/WrIuCDp0PArQtjNg/vo7HUGq9SrEIE2jvyVW59mvoYOwfnDLUiguKZirZgpjZF2DDKK6WpZVTVpKcH+HEFdmFAqJInem/CRUE0bqjMr88bUyDjVw9FtJ5EmQenctjrFVaB7hswOaJBmFQmn9G/BXkMvZ6mX7LzCUM2PVHnVfVeCLdwiOINikzW9qzlr8WoHw4qEGJLuQBWXjJu+m2+FdaOD6PL53nY3w== ElPatrono1337

**Mining Pools:**
- 45[.]88[.]67[.]94:7777
- 139[.]99[.]123[.]196:80
- pool[.]supportxmr[.]com:80

**Paths:**
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

**No further IoCs found.**
