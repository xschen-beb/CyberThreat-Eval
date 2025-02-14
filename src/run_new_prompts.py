import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from src.search_engine import (
    google_web_search,
    click_into_page,
    click_into_page_original,
    click_into_page_with_browser,
    bing_search,
)
from src.threat_research import *
import re
import json
import time

sys_prompt = f"""
# Task Description

1. You are a cybersecurity expert tasked with extracting Indicators of Compromise (IOCs) from a given article.
2. The article content is enclosed between <article> and </article> tags.
3. Your task is to parse each line between the <article> tags and extract a list of Indicators of Compromise (IOCs). This includes any hashes (hash1, hash256, hash_md5) found inside Yara rules.
4. Only extract IOCs that exactly match the following special types and formats:
    - ip: IPv4 address (e.g., 172.10.12.234)
    - ip_port: IPv4 address with port (e.g., 172.10.12.234:80)
    - domain: A valid domain name (e.g., abc.com, sub.domain.co.uk). 
      * Must have a valid TLD (e.g., .com, .org, .net, .co.uk, etc.).
      * Exclude well-known benign domains if it’s clear they are not used maliciously (like certain vendor domains "microsoft.com," "github.com," etc.) unless the text states these domains are part of malicious activity.
      * Excluding common or benign names like "Microsoft", "Sogou", "QQ", "360".
    - url: Complete valid URL (e.g., http://example.com/file.exe), must be in **URL format**, excluding common or benign names like "Microsoft".
    - email: Malicious email address (e.g., attacker@example.com)
    - hash_md5: A strict 32-character MD5 hash, letter case insensitive (e.g., f21cb2d2f8e62e38453fab019fa8f79f)
    - hash_sha256: A strict 64-character SHA256 hash, letter case insensitive
    - hash_sha1: A strict 40-character SHA1 hash, letter case insensitive
5. Explicitly exclude any content that does not match the above formats, such as CVE identifiers (e.g., CVE-2024-40762) or unrelated data.
6. **Only treat an email address as an IoC if it is used maliciously** or is directly associated with suspicious activity in the article.  
   - For example, an email address used by an attacker to exfiltrate data or impersonate a trusted entity can be considered an IoC.  
   - Conversely, normal "contact us" or "support@company.com"-type addresses used for legitimate business or marketing **are not** to be extracted as IoCs unless the text explicitly indicates malicious context.
7. For each IOC type, list all unique valid values found in the article. If none found, output "No IoCs found".
8. First, generate a bulleted list of IOC types (from the special types above) with their corresponding valid values found, along with brief comments on how these values indicate malicious activity. Exclude IOCs not presented in the article.
9. Enclose this list between <reasons> and </reasons> tags.
10. Ensure each IOC type only lists values that are present in the article and valid.
11. Then, generate rows for each IOC type in the format:
    - |IocType|Value 1, Value 2, ..., Value N|
12. Enclose these rows between [START] and [END] markers, and wrap the entire section with <IOCS> and </IOCS> tags.

# Examples

## Example 1
<article>
Check this out:
  - Our website has been accessed from IP address 192.16.32.47 through port 443.
  - Someone has attempted to login to our system using the email address xxx@yyy.com with the wrong password from China.
  - There is suspicious activity on the following URLs: healthcarb.com and bankjordan.com
  - A network scan has revealed that several machines in our network are running outdated versions of software, which could be vulnerable to known exploits.

  IOCs(Indicators of Compromise):
  MD5s:
  254d91c3b82854956cefcc26f7ca91fa, 
  53d8b3ab93183aa54c9c0a1e0daed584

  SHA-256
  65450d23d2f6ec8c73fd660835d8f1a2a6b95762c319dd4c8a63b3b741a7d576

</article>

Response:
<reasons>
  - ip - Values: 192.16.32.47 - This IP address is associated with unauthorized access attempts.
  - ip_port - Values: 192.16.32.47:443 - This IP and port combination was used in the attack.
  - email - Values: xxx@yyy.com - This email address was used in suspicious login attempts.
  - url - Values: healthcarb.com, bankjordan.com - These URLs show targeted authentication endpoints.
  - hash_md5 - Values: 254d91c3b82854956cefcc26f7ca91fa, 53d8b3ab93183aa54c9c0a1e0daed584 - MD5 hashes of suspicious files.
  - hash_sha256 - Values: 65450d23d2f6ec8c73fd660835d8f1a2a6b95762c319dd4c8a63b3b741a7d576 - SHA256 hash of malicious content.
</reasons>

<IOCS>
[START]
|ip|192.16.32.47|
|ip_port|192.16.32.47:443|
|email|admin@example.com|
|url|healthcarb.com, bankjordan.com|
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

_HEADLESS_FLAG = False


client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)


def validate_ioc(ioc_type, value):    
    if ioc_type == "ip_port":
        try:
            port = int(value)
            return 0 <= port <= 65535
        except ValueError:
            return False
            
    elif ioc_type == "ip":
        try:
            parts = value.split('.')
            if len(parts) == 4:
                return all(0 <= int(part) <= 255 for part in parts)
            return False
        except (ValueError, AttributeError):
            return False
            
    elif ioc_type == "domain":
        import re
        domain_pattern = r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
        return bool(re.match(domain_pattern, value))
        
    elif ioc_type == "url":
        import re
        url_pattern = r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
        return bool(re.match(url_pattern, value))
        
    elif ioc_type == "email":
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, value))
        
    elif ioc_type in ["hash_md5", "hash_sha1", "hash_sha256"]:
        import re
        hash_lengths = {
            "hash_md5": 32,
            "hash_sha1": 40,
            "hash_sha256": 64
        }
        hash_pattern = r'^[a-fA-F0-9]+$'
        return len(value) == hash_lengths[ioc_type] and bool(re.match(hash_pattern, value))
        
    return False


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
                    
                    if validate_ioc(ioc_type, clean_value):
                        iocs_list.append({"type": ioc_type, "value": clean_value, "source": url})
                    else:
                        print(f"Invalid IOC format: {ioc_type} - {clean_value}")  


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
        'https://blog.sekoia.io/sneaky-2fa-exposing-a-new-aitm-phishing-as-a-service/'
        # 'https://www.picussecurity.com/resource/blog/salt-typhoon-telecommunications-threat',
        # 'https://www.bleepingcomputer.com/news/security/chinese-hackers-breached-t-mobiles-routers-to-scope-out-network',
        # 'https://www.bleepingcomputer.com/news/security/atandt-and-verizon-say-networks-secure-after-salt-typhoon-breach',
        # 'https://www.bloomberg.com/news/articles/2024-12-28/at-t-says-its-network-is-now-clear-after-salt-typhoon-hack',
        # 'https://www.bleepingcomputer.com/news/security/white-house-links-ninth-telecom-breach-to-chinese-hackers',
        # 'https://www.bleepingcomputer.com/news/security/atandt-verizon-reportedly-hacked-to-target-us-govt-wiretapping-platform'
    ]
    iocs_set = set()
    for link in urls:
        blog = click_into_page_with_browser(
            link, is_text=True, headless_flag=_HEADLESS_FLAG
        )
        length = num_tokens_from_string(blog, "gpt-4o")
        if length > 120000:
            blog = blog[:120000]
        blog = blog.replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https")
        print(blog)
        iocs = json.loads(original_response(blog, link))
        print(type(iocs))
        # original = analysis_response(blog)
        for ioc in iocs:
            ioc_tuple = (ioc['type'], ioc['value'], ioc['source'])
            iocs_set.add(ioc_tuple)
        # time.sleep(180)

    unique_iocs = [{"type": ioc[0], "value": ioc[1], "source": ioc[2]} for ioc in iocs_set]

    iocs_json = json.dumps(unique_iocs, indent=4)
    print("IoCs:")
    print(iocs_json)

if __name__ == '__main__':
    main()
