Source: [https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster](https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster)

## Related articles (describing the same threat) 
- https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster
- https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/
- https://objective-see.org/blog/blog_0x7A.html
- https://thehackernews.com/2024/10/n-korean-hackers-use-fake-interviews-to.html
- https://www.infosecurity-magazine.com/news/beavertail-malware-job-seekers/

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Fake North Korean IT Worker Linked to BeaverTail Video Conference App Phishing Attack 

#### Root cause 
 The incident was caused by a North Korean IT worker cluster (CL-STA-0237) exploiting a U.S.-based IT services company's credentials and infrastructure to carry out phishing attacks using malware-infected video conference apps, including InvisibleFerret malware *Your changes* (https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/) and BeaverTail stealer *Your changes* (https://objective-see.org/blog/blog_0x7A.html). *The attackers also posed as prospective employers to lure developers into fake interviews, delivering updated BeaverTail and InvisibleFerret malware* (https://thehackernews.com/2024/10/n-korean-hackers-use-fake-interviews-to.html). *The malware targets job seekers via platforms like LinkedIn and X, distributing through files disguised as legitimate applications such as MiroTalk and FreeConference* (https://www.infosecurity-magazine.com/news/beavertail-malware-job-seekers/). 

#### Threat actor/group/campaign 
 North Korean IT worker activity cluster CL-STA-0237, linked to broader DPRK activities including weapons of mass destruction (WMD) programs, and potentially the Lazarus Group *Your changes* (https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/). *The activity cluster CL-STA-0240 is also involved in a campaign named Contagious Interview, targeting job seekers through fake interviews* (https://thehackernews.com/2024/10/n-korean-hackers-use-fake-interviews-to.html). 

#### Organization/industry/location 
 Targeted organizations include small-and-medium-sized businesses (SMB) and at least one major tech company, primarily in the United States. The actors likely operate from Laos using Lao IP addresses and identities *Your changes* (https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/). 

#### Start date – End date 
 The activity was observed in 2022, with significant events occurring in 2024. 

#### MITRE TTPs 
 ['T1071: Application Layer Protocol', 'T1588: Obtain Capabilities', 'T1566: Phishing', 'T1105: Ingress Tool Transfer'] 

#### Impact 
 The exact number of records or financial losses is not specified, but the campaign involves significant credential theft and malware deployment, potentially compromising multiple organizations' IT infrastructure. *BeaverTail malware, now written in the Qt framework, targets both macOS and Windows, stealing browser passwords and cryptocurrency wallets* (https://thehackernews.com/2024/10/n-korean-hackers-use-fake-interviews-to.html). *It now targets 13 different cryptocurrency wallet browser extensions, up from nine earlier* (https://www.infosecurity-magazine.com/news/beavertail-malware-job-seekers/). 

#### Mitigation Steps 
 ['Strengthen hiring screening processes to detect fake identities.', 'Implement robust monitoring for insider threats.', 'Thoroughly evaluate outsourced services and ensure proper due diligence.', 'Restrict the use of corporate machines for personal activities.', 'Utilize advanced threat detection solutions such as Cortex XDR, Prisma Cloud, and advanced DNS/URL filtering services to identify and block malicious activities.'] 

#### Detection Signature 
 {'Service': 'Web (HTTP/HTTPS)', 'Port': '80/443', 'Severity': 'Critical', 'Incident': 'North Korean Phishing Attack', 'Signature name': 'Malware-infected video conference app', 'Internal checks': ['Ensure all email and job application processes are verified and screened.', 'Monitor network traffic for unusual IP addresses and domain access.', 'Implement two-factor authentication for accessing critical systems.'], 'External scanning': ['Scan for newly registered domains resolving to known malicious IP addresses.', 'Monitor for domains mimicking legitimate video conferencing services.']} 

#### IoCs:
- domain: effertz-carroll.com ([link](https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/)) 

- domain: regioncheck.net ([link](same as above)) 

- domain: freeconference.io ([link](same as above)) 

- domain: ipcheck.cloud ([link](same as above)) 

- domain: mirotalk.io ([link](same as above)) 

- domain: mirotalk.net ([link](same as above)) 

- domain: ftpserver0909.com ([link](same as above)) 

- ip: 167.88.36.13 ([link](same as above)) 

- email: adonis_eros@outlook.com ([link](same as above)) 

- email: brightstar1116@outlook.com ([link](same as above)) 

- email: buyerlao@outlook.com ([link](https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/)) 

- email: casey_qadir@outlook.com ([link](same as above)) 

- email: cescernand@outlook.com ([link](same as above)) 

- email: devstar1116@gmail.com ([link](same as above)) 

- email: ebcappservices@gmail.com ([link](same as above)) 

- email: hakajakin@outlook.com ([link](same as above)) 

- email: ideationbrand@gmail.com ([link](same as above)) 

- email: legend_dev@outlook.com ([link](same as above)) 

- email: liko.sonexarth@gmail.com ([link](same as above)) 

- email: liko.sonexarth@hotmail.com ([link](same as above)) 

- email: longines0924@gmail.com ([link](same as above)) 

- email: lujindane@outlook.com ([link](same as above)) 

- email: matthewhall14541@gmail.com ([link](same as above)) 

- email: niko.sonexarth@gmail.com ([link](same as above)) 

- email: niko.sonexarth@hotmail.com ([link](same as above)) 

- email: oscar.vetres127@europe.com ([link](same as above)) 

- email: oscar.vetres127@gmail.com ([link](same as above)) 

- email: pinefirst@outlook.com ([link](same as above)) 

- email: reply9998@gmail.com ([link](same as above)) 

- email: richard.stewart.1202@gmail.com ([link](same as above)) 

- email: richard.stewart.1202@outlook.com ([link](same as above)) 

- email: sniper_bruce@outlook.com ([link](same as above)) 

- email: stp.walsh33@gmail.com ([link](same as above)) 

- email: techcare127@gmail.com ([link](same as above)) 

- email: truepai415@gmail.com ([link](same as above)) 

- email: truestar222@outlook.com ([link](same as above)) 

- email: volodimir.work2020@gmail.com ([link](same as above)) 

- email: zhangming_k@yahoo.com ([link](same as above)) 

- email: zhuming1116@gmail.com ([link](same as above)) 

- email: lisettekolson8@gmail.com ([link](same as above)) 

- email: 312011217@qq.com ([link](same as above)) 

- email: alhinglovena3000@gmail.com ([link](same as above)) 

- email: jumphon2103@gmail.com ([link](same as above)) 

- email: mobilephetjum@gmail.com ([link](same as above)) 

- email: phetchamphone1998@gmail.com ([link](same as above)) 

- ip: 95.164.17.24 ([link](https://objective-see.org/blog/blog_0x7A.html)) 

- hash_sha256: 0F5F0A3AC843DF675168F82021C24180EA22F764F87F82F9F77FE8F0BA0B7132 ([link](https://objective-see.org/blog/blog_0x7A.html)) 

- ip: 88.198.233.174 ([link](https://thehackernews.com/2024/10/n-korean-hackers-use-fake-interviews-to.html)) 

- domain: mirotalk-app.com ([link](same as above)) 

- hash_sha256: A3F9E1F3D3CE6F7E7C0EBD8E7A8B5C4A9D8E0B2D7D8F2A1B1B7F3A3D7E8C5F4A ([link](same as above)) 

- For more IoCs, please refer to the above links. 


