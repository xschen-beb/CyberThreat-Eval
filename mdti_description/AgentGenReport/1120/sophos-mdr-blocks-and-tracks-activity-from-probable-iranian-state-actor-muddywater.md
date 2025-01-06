Source: [https://news.sophos.com/en-us/2024/11/20/sophos-mdr-blocks-and-tracks-activity-from-probable-iranian-state-actor-muddywater](https://news.sophos.com/en-us/2024/11/20/sophos-mdr-blocks-and-tracks-activity-from-probable-iranian-state-actor-muddywater)

## Related articles (describing the same threat) 
- https://harfanglab.io/insidethelab/muddywater-rmm-campaign
- https://news.sophos.com/en-us/2024/11/20/sophos-mdr-blocks-and-tracks-activity-from-probable-iranian-state-actor-muddywater

## Enriched Doc (enrichments marked with *content*(link)): 
#### Incident: Sophos MDR blocks and tracks activity from probable Iranian state actor 'MuddyWater' 

#### Root cause 
 The root cause behind this incident appears to be a successful phishing campaign that tricked users into downloading a legitimate remote monitoring and management (RMM) tool, Atera. Once installed, this tool was used by the attackers to execute malicious commands, such as credential dumping, system registry backup using the a.ps1 PowerShell script, and domain enumeration commands. The attackers also created an SSH tunnel towards 51.16.209.105 *The changes* (https://news.sophos.com/en-us/2024/11/20/sophos-mdr-blocks-and-tracks-activity-from-probable-iranian-state-actor-muddywater/). Since late October 2023, there has been a significant increase in Atera Agent installation packages linked to MuddyWater, continuing through April 2024. Attackers exploited Atera’s free trial offers using compromised email accounts via methods like password spraying and data breaches *Your changes* (https://harfanglab.io/insidethelab/muddywater-rmm-campaign/). 

#### Threat actor/group/campaign 
 MuddyWater (also known as TA450), probable Iranian state actor, related to campaign STAC 1171 *The changes* (https://news.sophos.com/en-us/2024/11/20/sophos-mdr-blocks-and-tracks-activity-from-probable-iranian-state-actor-muddywater/). 

#### Organization/industry/location 
 The initial attack targeted an organization in Israel, and similar activity was observed in the United States. MuddyWater has also targeted various sectors including Airlines, IT Companies, Telecommunication, Pharmaceutical, Automotive manufacturing, Logistics, Travel and Tourism, Employment/Immigration agency, and small businesses across Israel, India, Algeria, Turkey, Italy, and Egypt *Your changes* (https://harfanglab.io/insidethelab/muddywater-rmm-campaign/). 

#### Start date – End date 
 The first tracked incident was earlier in November 2024. 

#### MITRE TTPs 
 ['- T1566.001: Spearphishing Attachment (Confidence: High)', '- T1078: Valid Accounts (Confidence: Moderate)', '- T1083: File and Directory Discovery (Confidence: Moderate)', '- T1003: Credential Dumping (Confidence: High)', '- T1105: Ingress Tool Transfer (Confidence: Moderate)'] 

#### Impact 
 The financial impacts or number of devices affected are not specified in the report. However, the attack involved credential dumping and potential unauthorized access to sensitive information. 

#### Mitigation Steps 
 ['- Educate employees about phishing techniques and how to recognize suspicious emails.', '- Implement strong email filtering to block phishing attempts.', '- Use multi-factor authentication (MFA) to protect user accounts.', '- Regularly update and patch systems and software to prevent exploitation of known vulnerabilities.', '- Monitor network traffic for unusual activity and regularly review system logs for suspicious actions.', '- Utilize endpoint detection and response (EDR) tools to detect and block malicious actions like credential dumping.'] 

#### Detection Signature 
 {'Service': 'Atera RMM Tool', 'Port': 'Not specified', 'Severity': 'Critical', 'Incident': 'Credential Dumping and Unauthorized Access', 'Signature name': "'Atera RMM Tool Malicious Activity'", 'Internal checks': ['Setting1: Ensure Atera RMM tool usage is monitored and restricted to legitimate purposes.', 'Setting2: Monitor for unusual command executions via RMM tools.', 'Setting3: Implement strict access controls and authentication for RMM tools.'], 'External scanning': ['Detect unusual remote access attempts.', 'Monitor for the use of compromised email accounts for registration of trial accounts.']} 

#### IoCs:
- url: http://ws.onehub.com/files/ ([link](https://news.sophos.com/en-us/2024/11/20/sophos-mdr-blocks-and-tracks-activity-from-probable-iranian-state-actor-muddywater/)) 

- url: http://downloads.level.io/install_windows.exe ([link](https://news.sophos.com/en-us/2024/11/20/sophos-mdr-blocks-and-tracks-activity-from-probable-iranian-state-actor-muddywater/)) 

- ip: 51.16.209.105 ([link](https://news.sophos.com/en-us/2024/11/20/sophos-mdr-blocks-and-tracks-activity-from-probable-iranian-state-actor-muddywater/)) 

- hash_sha256: 5d7eb6c36d261adeef1a59bde9eb965f5d8d7f56a2e607da913e782167ba6cb6 ([link](https://harfanglab.io/insidethelab/muddywater-rmm-campaign/)) 

- hash_sha256: 14c270cf53a50867e42120250abca863675d37abf39d60689e58288a9e870144 ([link](https://harfanglab.io/insidethelab/muddywater-rmm-campaign/)) 

- hash_sha256: 638c7a4f833dc95dbab5f0a81ef03b7d83704e30b5cdc630702475cc9fff86a2 ([link](https://harfanglab.io/insidethelab/muddywater-rmm-campaign/)) 

- hash_sha256: ec553e14b84ccca9b84e96a9ed19188a1ba5f4bf1ca278ab88f928f0b00b9bd0 ([link](https://harfanglab.io/insidethelab/muddywater-rmm-campaign/)) 

- hash_sha256: 165a80f6856487b3b4f41225ac60eed99c3d603f5a35febab8235757a273d1fd ([link](https://harfanglab.io/insidethelab/muddywater-rmm-campaign/)) 

- For more IoCs, please refer to the above links. 


