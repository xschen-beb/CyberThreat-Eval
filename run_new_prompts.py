import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from search_engine import (
    google_web_search,
    click_into_page,
    click_into_page_original,
    click_into_page_with_browser,
    bing_search,
)
from threat_research import *
import re
import json
import time

sys_prompt = f"""
# Task Description

1. You will adopt the viewpoint of a cyber security expert.
2. The text between the <article> and </article> tags is scraped from a web page containing a threat intelligence report. You might see only a portion of the scraped content.
3. Your task is to parse each line of the text between the <article> and </article> tags and extract a list of indicators of compromise (IOCs).
4. You should attempt to extract IOCs which map to one of the following *special types*
    - ip: An IPv4/IPv6 address - Example: 172.10.12.234, 2001:0:2851:fcb0:1871:170e:cedb:843f
    - ip_port - A port number - Example: 80, 443
    - domain - A domain name - Example: abc.com, file.abc.com
    - url - A url to a website - Example: https://www.microsoft.com/
    - email - An email address - Example: badguy@hotmail.com
    - hash_md5 - A MD5 hash - Example: f21cb2d2f8e62e38453fab019fa8f79f
    - hash_sha256 - A SHA256 hash - Example: e923636f1093c414aab39f846e9d7a372beefa7b628b28179197e539c56aa0f0
    - hash_sha1 - A SHA1 hash - Example: 56ca7ef04cd70a596d5a4a8d5ba056ae8e160071
5. Make sure that you only use the list in (4) i.e. *special types* as IOC Type. If you are unable to map the extracted IOC to one of the *special types* then do not include those in the response.
6. Each IOC Type i.e. ip, ip_port, url, hash_md5, hash_sha1, hash_sha256, domain and email can have multiple values from the article.
7. As the first part of your response, generate a bulleted list of IOC types mentioned in (4), together with the different values taken by that IOC type in the article. Add very brief comments about how all these values occuring in the article indicate the malicious activity like attack, campaign, breach, etc. make sure that you eliminate IOCs that are related to the article source, author, etc. and only keep IOCs that indicate the malicious activity.
8. Place the bulleted list in (7) between the tags <reasons> and </reasons>
9. When doing (7) remember that if a particular value from the article is grouped under one IOC type, then it cannot be grouped under another IOC type.
10. Go over the list in (7) and ensure that each IOC type is one of the *special types* and is present in the article.
11. When going over (7) ensure that values of the same IOC type are grouped under the same IOC type.
12. When going over the list in (7), make sure that each value included in the list is present in the given article and is a valid indicator of compromise.
13. For the second part of your response, generate a sequence of rows, one for each IOC type of the form:
    - |IocType|Value 1, Value 2, ..., Value N|
14. The values in (13) should be the values grouped under that IOC in (7).
15. The list of rows in (13) should be enclosed between a row at the start with [START] and a row at the end with [END]
16. Place the list from (14) and the [START] and [END] rows between the tags <IOCS> and </IOCS>

# Examples

Below are some examples.

## Example 1
<article>
Check this out:
  - Our website, example.com, has been accessed from IP address 192.16.32.47.
  - Someone has attempted to login to our system using the email address admin@example.com with the wrong password from China.
  - There is suspicious activity on the following URLs: example.com/login.php and example.com/reset_password.php
  - Multiple hashes of the form MD5 and SHA-256 have been found: 254d91c3b82854956cefcc26f7ca91fa, 53d8b3ab93183aa54c9c0a1e0daed584, 65450d23d2f6ec8c73fd660835d8f1a2a6b95762c319dd4c8a63b3b741a7d576
  - A network scan has revealed that several machines in our network are running outdated versions of software, which could be vulnerable to known exploits.
</article>

Response:
<reasons>
  - ip - Values: 192.16.32.47 - This value is clearly an IP address and its format matches the standards defined in RFC 791.
  - email - Values: admin@example.com - This value has a valid email format and is found being used for login.
  - url - Values: example.com/login.php, example.com/reset_password.php - These values conform to the syntax of URLs and are particularly related to possible security issues such as brute-force attacks.
  - hash_md5 - Values: 254d91c3b82854956cefcc26f7ca91fa, 53d8b3ab93183aa54c9c0a1e0daed584 - These values match the standard format for MD5 hashes and are often used to identify malware or files that have been tampered with
  - hash_sha256 - Values: 65450d23d2f6ec8c73fd660835d8f1a2a6b95762c319dd4c8a63b3b741a7d576 - This value conforms to the standard format for SHA-256 hashes and is often used to verify data integrity or authenticity.
</reasons>

<IOCS>
[START]
|ip|192.16.32.47|
|email|admin@example.com|
|url|example.com/login.php, example.com/reset_password.php|
|hash_md5|254d91c3b82854956cefcc26f7ca91fa, 53d8b3ab93183aa54c9c0a1e0daed584|
|hash_sha256|65450d23d2f6ec8c73fd660835d8f1a2a6b95762c319dd4c8a63b3b741a7d576|
[END]
</IOCS>
"""

user_prompt = f"""
# Task

Parse the article below according to the task description above.

<article>
{{ARTICLE}}
</article>

Response:
"""

analysis_prompt = r"""
        You are a security expert. I will give a report/blog on the Internet. You need to analyze it to understand the root cause (including, vulnerable/misconfigured services), how to detect this problem, and the mitigation behind the incident.
        **For IoCs, please also extract those (e,g., hash1, hash256, hash_md5) inside the Yara Rule into the IoCs. e.g., extract '"hash1/hash256/hash_md5": "65c6798eedd33aa36d77432b2ba7ef45dfe760092810b4db487210b19299bdcb"' from YARA rule and put it into IoCs **

        You should provide a signature in the following format:    
        Incident: Shanghai Police Datalake Leak
        
        Root cause: the root cause behind the indicent including vulnerable/misconfigured services. e.g., Misconfigured Kibana instance 
        
        Threat actor/group/campaign: Who carried out the attack? It could be an orgainzation, a malware family, etc (if known)
        
        Organization/industry/location: Who was targeted/vicim? (if known)
        
        Start date – End date: When did the attack happen? (if known)

        MITRE TTPs: How was the attack carried out?  (if known)

        Impact: 100,000 records leaked.  **how many devices people impacted or the financial losses**

        Mitigation Steps: (How to protect myself?) e.g., Secure the Kibana instance with authentication credentials. and **Detailed Steps for mitigation**

        Detection Signature: (How to detect? i.e., detection rules)
            Service: Redis, CouchDB, etc. (it is a concrete service name, not general words like "database")  
            Port: 6379 (make it concrete if possible)   
            Severity: Critical
            Incident: XXX 
            Signature name: “Redis publicly accessible”    
            Internal checks (see next)    
                - Setting1: Redis port (6379) should not be exposed on external Internet. – In platform    
                - Setting2: Redis port (6379) should not listen on the external Internet – Inside VMs    
                - Setting3: Redis server should secure with authentication credentials. – Inside VMs    
            External scanning (see next)    
                - Port (6379) open
                - Redis no-pass-login
        
        IoCs: How do I know I am affected? (for example, IP, domain, email, sha1, sha256, hash1, hash256, hash_md5, url, etc). If the document does not have IoCs, please output "No IoCs found". If the document has IoCs, please MAKE SURE to list top 10 IoCs (IF HAVE) you found in the document.  Change the URL/IP/Domain format to a valid format with standard syntax, without the extra brackets or colons (e.g., change hxxp[:]//2[.]57[.]149[.]233[:]3366/ to http://2.57.149.233:3366/)
        The IoCs should be a in the following format:
        '[{"type":"hash_md5","value":"3edcde37dcecb1b5a70b727ea36521de","source": "https://www.wheretheiocfrom.com/XX/XXXX/"},{"type":"url","value":"http:\/\/50.19.48.59:82\/me1.bat","source": "same as above"}]'
        The type can be "ip", "ip_port",  "domain", "url", "email", "hash_md5", "hash_sha256", "hash_sha1".
"""

os.environ["LOCAL_ENDPOINT"] = "http://10.150.142.182:9999"
os.environ["PROXY_KEY"] = "59ddb6820482b719e33661ccbfa98042"
_HEADLESS_FLAG = False

client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)


def extract_iocs(iocs_text, url):
    iocs_content = re.search(r"<IOCS>\s*\[START\](.*?)\[END\]\s*</IOCS>", iocs_text, re.DOTALL)
    if not iocs_content:
        return []

    iocs_content = iocs_content.group(1).strip()
    iocs_lines = iocs_content.splitlines()
    
    iocs_list = []

    for line in iocs_lines:
        line = line.strip()
        if line:
            ioc_match = re.match(r"\|(\w+)\|(.+)", line)
            if ioc_match:
                ioc_type = ioc_match.group(1)
                values = ioc_match.group(2).split(", ")
                for value in values:
                    clean_value = value.replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https")
                    clean_value = re.sub(r'\[://\]', '://', clean_value)
                    clean_value = re.sub(r'https\[\]', 'https://', clean_value)  
                    clean_value = re.sub(r'http\[\]', 'http://', clean_value)  
                    clean_value = clean_value.strip('|')

                    iocs_list.append({"type": ioc_type, "value": clean_value, "source": url})

    return iocs_list


def original_response(string, url):
    messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ]

    misconf_qeustion = f"Here is the blog: {string}."
    messages.append({"role": "user", "content": misconf_qeustion})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7,
        max_tokens=4096,
    )

    original = response.choices[0].message.content
    iocs = extract_iocs(original, url)

    iocs_json = json.dumps(iocs, indent=4)
    print("IoCs:")
    print(iocs_json)

    fo = open('original_response.txt', 'a+')
    fo.write(iocs_json)
    return iocs_json

def analysis_response(string):
    misconf_qeustion = f"Here is the blog: {string}."
    messages = [
            {"role": "system", "content": analysis_prompt},
            {"role": "user", "content": misconf_qeustion}
        ]

    messages.append({"role": "user", "content": misconf_qeustion})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7,
        max_tokens=4096,
    )

    original = response.choices[0].message.content
    print(original)
    fo = open('analysis_response.txt', 'a+')
    fo.write(original)
    return original

def main():
    urls = [
        'https://www.bleepingcomputer.com/news/security/fake-ai-video-generators-infect-windows-macos-with-infostealers/',
        'https://app.any.run/tasks/896d628c-59ae-409e-b0b2-7fd6719b7c2a',
        'https://www.cyfirma.com/research/lumma-stealer-tactics-impact-and-defense-strategies/'
    ]
    iocs_set = set()
    for link in urls:
        blog = click_into_page_with_browser(
            link, is_text=False, headless_flag=_HEADLESS_FLAG
        )
        length = num_tokens_from_string(blog, "gpt-4o")
        if length > 120000:
            blog = blog[:120000]
        iocs = json.loads(original_response(blog, link))
        print(type(iocs))
        # original = analysis_response(blog)
        for ioc in iocs:
            ioc_tuple = (ioc['type'], ioc['value'], ioc['source'])
            iocs_set.add(ioc_tuple)
        time.sleep(180)

    unique_iocs = [{"type": ioc[0], "value": ioc[1], "source": ioc[2]} for ioc in iocs_set]

    iocs_json = json.dumps(unique_iocs, indent=4)
    print("IoCs:")
    print(iocs_json)

if __name__ == '__main__':
    main()
