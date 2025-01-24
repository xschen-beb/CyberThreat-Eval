from threat_research import *
import json
from urllib.parse import urlparse
from datetime import datetime


def filter_url(url, url_list):
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    for u in url_list:
        parsed_u = urlparse(u)
        base_u = f"{parsed_u.scheme}://{parsed_u.netloc}"
        if base_u == base_url:
            return True
    
    return False


def llm_judgment_for_ioc_in_blog(ioc_value, original_text): 
    sys_prompt = f"""
    ### Role Description
    You are an expert in cybersecurity. Given the original text below, determine whether the IoC '{ioc_value}' appears in full form in the text, without any modifications or obfuscations. The IoC might be written with markers or characters like '[.]', 'hXXp', 'hXXps', etc., which are commonly used to obfuscate the actual value. No hallucination is allowed.

    ### Task description
    1. Search for any occurrence of '{ioc_value}' in the original text.
    2. If you find the IoC, check if it is surrounded by any obfuscations (such as '[.]', 'hXXp', etc.).
    3. If there are obfuscations, remove them to restore the original IoC.
    4. If the restored IoC matches the original IoC '{ioc_value}' in the text, return True. Otherwise, return False.
    5. If the IoC does not appear at all or cannot be fully restored, return False.
    6. Answer with either 'True' or 'False' directly without any prefixes or explanations.

    ### Example
    IoC_value given: 147.45.44.83
    original text: 
    Indicators of Compromise
    260f06f0c6c1544afcdd9a380a114489ebdd041b846b68703158e207b7c983d6
    3317b8e19e19218e5a7c77a47a76f36e37319f383b314b30179b837e46c87c45
    0d03c7c6335e06c45dd810fba6c52cdb9eafe02111da897696b83811bff0be92
    604fa32b76dbe266da3979b7a49e3100301da56f0b58c13041ab5febe55354d2
    6be9c015c82645a448831d9dc8fcae4360228f76dff000953a76e3bf203d3ec8
    b1a351ee61443b8558934dca6b2fa9efb0a6d2d18bae61ace5a761596604dbfa
    147[.]45.44.83:6483
    185[.]196.9.26:6302
    True
    """

    user_prompt = f"""
    ### Task description
    Given ioc values, parse the original text below according to the task description above.

    IoC_value given: {ioc_value}
    original text:
    {original_text}
    """

    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
    misconf_qeustion = f"Here is the blog: {original_text}."
    messages.append({"role": "user", "content": misconf_qeustion})

    try:
        response = api_call(messages, [], json_enabled=False)
        original = response.choices[0].message.content
        return original
    except Exception as e:
        return False


def threat_research_playground():
    for _ in range(1):
        try:
            unique_urls = [
                'https://www.bitdefender.com/en-gb/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users',
                'https://hackread.com/facebook-malvertising-malware-via-fake-bitwarden',
                'https://www.bleepingcomputer.com/news/security/fake-bitwarden-ads-on-facebook-push-info-stealing-chrome-extension',
                'https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users',
                'https://www.wizcase.com/news/malicious-facebook-ads-target-bitwarden-users-with-fake-security-update',
                'https://www.bitdefender.com/en-au/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users',
                'https://cyberinsider.com/facebook-ads-target-bitwarden-users-with-malicious-chrome-extension',
                'https://social.cyware.com/news/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users-3f5d8ce1',
                'https://www.techradar.com/pro/hackers-pushing-fake-bitwarden-updates-hit-thousands-of-devices-with-data-stealing-malware'
            ]
            text_output = ""
            paste_ioc_section = ""
            blog_for_urls = []

            iocs_dict = {}  # Use a dictionary to remove duplicates by value
            for link in unique_urls:
                blog = click_into_page_with_browser(
                    link, is_text=False, headless_flag=False
                )
                date = add_date(blog)
                if date:
                    pub_date = date
                else:
                    pub_date = "Unspecified"
                length = num_tokens_from_string(blog, "gpt-4o")
                if length > 120000:
                    blog = blog[:120000]
                blog = blog.replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https")
                blog_for_urls.append({"blog": blog, "source": link})
                
                iocs_json = extract_iocs_from_text(blog, link)
                if iocs_json:
                    for ioc in iocs_json:
                        ioc_tuple = (ioc['type'], ioc['value'], ioc['source'], pub_date)
                        # Use ioc['value'] as the key to ensure uniqueness
                        iocs_dict[ioc['value']] = ioc_tuple

            unique_iocs = [{"type": ioc[0], "value": ioc[1], "source": ioc[2], "publish_date": ioc[3]} for ioc in iocs_dict.values()]
            print(unique_iocs)
            

            for ioc_data in unique_iocs:
                ioc_value = ioc_data["value"]
                # if ioc_value in unique_urls or filter_url(ioc_value, unique_urls):
                if ioc_value in unique_urls or filter_url(ioc_value, unique_urls):
                    continue
                ioc_type = ioc_data["type"]
                ioc_source = ioc_data.get('source', 'No link provided')  # Ensure a default value
                pub_date = ioc_data['publish_date']
                blogs_for_target_source = next((entry["blog"] for entry in blog_for_urls if entry["source"] == ioc_source), None)

                try:
                    if ioc_type in ["hash_md5", "hash_sha1", "hash_sha256"]:
                        ioc_type_for_check = 'hash'
                    else:
                        ioc_type_for_check = ioc_type

                    is_malicious = check_ioc(ioc_value, ioc_type_for_check)
                    if is_malicious == True:
                        if ioc_value in blogs_for_target_source and "True" in llm_judgment_for_ioc_in_blog(ioc_value, blogs_for_target_source):
                            # ioc_source = ioc_data.get('source', 'No link provided')
                            text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source}))  Publish date: {pub_date}\n\n"
                            paste_ioc_section += f"{ioc_value}\n"

                            print(f"The {ioc_type} {ioc_value} is malicious.")
                        else:
                            print(f"The {ioc_type} {ioc_value} not in urls.")
                            continue
                            # text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source})) \n\n"
                            # text_output += f"Not found for {ioc_type} {ioc_value} in url. \n\n"

                    elif is_malicious == False:
                        print(f"The {ioc_type} {ioc_value} is clean.")
                    else:
                        if ioc_value in blogs_for_target_source and "True" in llm_judgment_for_ioc_in_blog(ioc_value, blogs_for_target_source):
                            text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source}))  Publish date: {pub_date} \n"
                            text_output += f"Found in URL, Not found for {ioc_type} {ioc_value} in VT. \n\n"
                            print(f"The {ioc_type} {ioc_value} in urls but not in VT.")
                        else:
                            print(f"Not Found in URL and VT for {ioc_type} {ioc_value}.")
                            continue
                            # text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source})) \n"
                            # text_output += f"Not Found in URL and VT for {ioc_type} {ioc_value}. \n\n"
                except Exception as e:
                    print(e)
            
            # For more IoCs note
            text_output += "- For more IoCs, please refer to the above links. \n\n"

            # Append the paste IoC section
            text_output += paste_ioc_section + "\n"

            return text_output
        except AttributeError:
            print("Error in processing the blog.")
            continue


def add_date(text):
    patterns = [
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}\b',  
        r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',                                                          
        r'\b\d{4}-\d{2}-\d{2}\b'                                                                 
    ]
    
    dates = []
    
    for pattern in patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            date_str = match.group()
            try:
                if ',' in date_str:
                    date_obj = datetime.strptime(date_str, '%B %d, %Y')
                elif '/' in date_str:
                    try:
                        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                    except ValueError:
                        date_obj = datetime.strptime(date_str, '%m/%d/%y')
                else:
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                
                formatted_date = date_obj.strftime('%Y-%m-%d')
                dates.append(formatted_date)
            except ValueError:
                continue
    
    return dates[0] if dates else None


if __name__ == '__main__':
    '''
    url = 'bleepingcomputer.com/news/security/us-says-chinese-hackers-breached-multiple-telecom-providers/'
    link = "https://www.bleepingcomputer.com/news/security/chinese-hackers-compromised-us-government-officials-private-communications-in-recent-telecom-breach"
    blog = click_into_page_with_browser(
        link, is_text=False, headless_flag=False
    )
    if "True" in llm_judgment_for_ioc_in_blog(url, blog):
        print(True)
    '''
    output = threat_research_playground()
    print("="*50)
    print(output)
    fw = open('test.md', 'w')
    fw.write(output)
    fw.close()
    unique_urls = [
        'https://www.bitdefender.com/en-gb/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users',
        'https://hackread.com/facebook-malvertising-malware-via-fake-bitwarden',
        'https://www.bleepingcomputer.com/news/security/fake-bitwarden-ads-on-facebook-push-info-stealing-chrome-extension',
        'https://www.bitdefender.com/en-us/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users',
        'https://www.wizcase.com/news/malicious-facebook-ads-target-bitwarden-users-with-fake-security-update',
        'https://www.bitdefender.com/en-au/blog/labs/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users',
        'https://cyberinsider.com/facebook-ads-target-bitwarden-users-with-malicious-chrome-extension',
        'https://social.cyware.com/news/inside-bitdefender-labs-investigation-of-a-malicious-facebook-ad-campaign-targeting-bitwarden-users-3f5d8ce1',
        'https://www.techradar.com/pro/hackers-pushing-fake-bitwarden-updates-hit-thousands-of-devices-with-data-stealing-malware'
    ]
    for link in unique_urls:
        blog = click_into_page(link)
        date = add_date(blog)
        if date:
            print(f"Publish Date: {date}")
        else:
            print(f"Publish date unspecified.")
    