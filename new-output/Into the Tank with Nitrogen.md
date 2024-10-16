Source: [https://news.sophos.com/en-us/2023/07/26/into-the-tank-with-nitrogen/](https://news.sophos.com/en-us/2023/07/26/into-the-tank-with-nitrogen/)

# Into the Tank with Nitrogen

# Enriched Doc (enrihcments marked with *content*(link)): 
 Incident: Nitrogen Malvertising Campaign 

 Root cause: The root cause includes the exploitation of pay-per-click (PPC) ad services on Google and Bing to distribute malicious software via compromised WordPress sites and phishing pages. Malicious ads were displayed due to misconfigured ad services and compromised WordPress sites hosting malicious content. 

 Threat Actor/group/campaign: The specific threat actor group behind the Nitrogen campaign is not named. However, the campaign is linked to the distribution of Cobalt Strike, *BlackCat (aka ALPHV)* infection, and employs *Pyramid HTTP/HTTPS C2 server* (*The changes* (https://www.trendmicro.com/en_us/research/23/f/malvertising-used-as-entry-vector-for-blackcat-actors-also-lever.html)). 

 Organization/industry/location: Targets include technology and non-profit sectors in North America. 

 Start date – End date: The campaign was identified in mid-June 2023 and expanded in late July 2023 to include TreeSize, *AnyDesk*, and *Cisco AnyConnect VPN* (*The changes* (https://coretek.co.uk/warning-treesize-users-targeted-in-new-malware-attack/)). 

 MITRE TTPs: ['T1583.001: Acquire Infrastructure: Domains', 'T1583.008: Acquire Infrastructure: Malvertising', 'T1584.001: Compromise Infrastructure: Domains', 'T1608.001: Stage Capabilities: Upload Malware', 'T1588.002: Obtain Capabilities: Tool', 'T1574.002: Hijack Execution Flow: DLL Side-Loading', 'T1053.005: Scheduled Task/Job: Scheduled Task', 'T1069.002: Permission Groups Discovery: Domain Groups', 'T1552.002: Unsecured Credentials: Credentials in Registry', 'T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder', 'T1553.005: Subvert Trust Controls: Mark-of-the-Web Bypass'] 

 Impact: The report does not specify the number of records leaked or financial losses. However, the campaign's goal is to stage compromised environments for potential ransomware deployment, indicating a high potential impact. 

 Mitigation: 1. **Ad-Blocking**: Use ad-blocking extensions or browsers with built-in ad-blocking capabilities. Opt for ad-blockers that allow blocking 'non-intrusive advertising.'
2. **Restrict Virtual File Systems**: Restrict the capability to mount virtual file systems via Group Policy Objects (GPO). Consider disabling auto-mounting of disk image files such as .iso files.
3. **Beware of Suspicious Websites**: Be cautious of websites with misspellings, poor grammar, and unprofessional marketing. Avoid downloading abnormal file extensions.
4. **Credential Management**: Avoid storing credentials within the Registry. Ensure that accounts with stored credentials have limited permissions. 

 Detection Signature: - Service: Google Ads, Bing Ads, WordPress
- Port: Not applicable
- Severity: Critical
- Incident: Nitrogen Malvertising Campaign
- Signature name: 'Malvertising campaign detected'
- Internal checks:
  - Setting1: Monitor for unusual ad-click behavior.
  - Setting2: Scan for and block access to known malicious domains.
  - Setting3: Implement ad-blocking solutions enterprise-wide.
- External scanning:
  - Monitor for SSL/TLS traffic to known C2 servers.
  - Detect and alert on the presence of suspicious ISO files being downloaded. 

 IoCs: ['Domains: softwareinteractivo[.]com, winsccp[.]com, mypondsoftware[.]com, tresize[.]com', 'IP Addresses: 104.234.119[.]16, 172.86.123[.]127, 45.81.39[.]177, 45.81.39[.]175, 167.88.164[.]141, 45.66.230[.]215, 45.66.230[.]216, 23.227.196[.]140, 85.217.144[.]164', 'File Hashes: Available on Sophos GitHub (as mentioned in the blog)'] 

 Additional Info: *Trend Micro incident response* team identified highly suspicious activities through the Targeted Attack Detection service, discovering malicious actors using cloned webpages of legitimate organizations such as *WinSCP cloned webpage* to distribute malware. The actors also leveraged *SpyBoy Terminator*, a tool tampering with protection provided by agents, utilized *Bloodhound-py and LaZagne tools*, and employed a *DLL sideloading technique* for C2 communication (*The changes* (https://www.esentire.com/blog/persistent-connection-established-nitrogen-campaign-leverages-dll-side-loading-technique-for-c2-communication)). Additionally, *TreeSize*, *AnyDesk*, and *Cisco AnyConnect VPN* software were targeted in the campaign. *Deepwatch Adversary Tactics and Intelligence (ATI) team* and *Sophos X-Ops analysis* indicate the campaign involves *phishing emails* and is targeting IT users (*The changes* (https://www.deepwatch.com/labs/cyber-intel-brief-july-26-august-02-2023/)). 


# Related articles (describing the same threat) 
['https://news.sophos.com/en-us/2023/07/26/into-the-tank-with-nitrogen/', 'https://www.trendmicro.com/en_us/research/23/f/malvertising-used-as-entry-vector-for-blackcat-actors-also-lever.html', 'https://www.esentire.com/blog/persistent-connection-established-nitrogen-campaign-leverages-dll-side-loading-technique-for-c2-communication', 'https://coretek.co.uk/warning-treesize-users-targeted-in-new-malware-attack/', 'https://www.deepwatch.com/labs/cyber-intel-brief-july-26-august-02-2023/']
