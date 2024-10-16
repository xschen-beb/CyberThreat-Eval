Source: [https://research.nccgroup.com/2023/11/13/dont-throw-a-hissy-fit-defend-against-medusa/](https://research.nccgroup.com/2023/11/13/dont-throw-a-hissy-fit-defend-against-medusa/)

# Don’t Throw a Hissy Fit; Defend Against Medusa

# Enriched Doc (enrihcments marked with *content*(link)): 
It appears the content provided is a 404 error page from the NCC Group website and not an actual blog or report on a security incident. Therefore, I cannot provide the requested analysis. If you have another document related to a security incident, please share it, and I will be happy to help with the analysis.

Here's an example of the format you requested based on a hypothetical incident:

---

Incident: Shanghai Police Datalake Leak

Root cause: Misconfigured Elasticsearch instance allowing unauthorized access

Threat Actor/group/campaign: Unknown attackers

Organization/industry/location: Shanghai Police Department, China

Start date – End date: June 2022 – July 2022

MITRE TTPs: T1190 (Exploit Public-Facing Application), T1078 (Valid Accounts)

Impact: 1 billion records leaked, affecting personal information of Shanghai citizens

Mitigation: 
- Secure Elasticsearch instances with strong authentication credentials.
- Implement network segmentation to restrict access to sensitive data.
- Regularly audit and monitor access logs for unusual activity.
- Apply the principle of least privilege to limit access to critical systems.

Detection Signature:
- Service: Elasticsearch 
- Port: 9200 
- Severity: Critical
- Incident: Unauthorized access to Elasticsearch
- Signature name: “Elasticsearch publicly accessible”
- Internal checks:
  - Setting1: Elasticsearch port (9200) should not be exposed on external Internet. – In platform
  - Setting2: Elasticsearch should use secure communication protocols (HTTPS). – Inside VMs
  - Setting3: Elasticsearch instance should be secured with strong authentication credentials. – Inside VMs
- External scanning:
  - Port (9200) open
  - Elasticsearch no-pass-login

IoCs: No IoCs found.

---

Please provide the correct document or more details, and I'll be able to assist you further. 


# Related articles (describing the same threat) 
['https://research.nccgroup.com/2023/11/13/dont-throw-a-hissy-fit-defend-against-medusa/']
