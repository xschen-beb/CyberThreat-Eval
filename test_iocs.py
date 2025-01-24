from threat_research import *
import json

def threat_research_playground():
    for _ in range(1):
        try:
            unique_urls = [
                "https://medium.com/walmartglobaltech/qbot-is-back-connect-2d774052369f#new_tab"
                # "https://www.picussecurity.com/resource/blog/salt-typhoon-telecommunications-threat"
                # "https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity"
            ]
            unique_urls = set(unique_urls)


            text_output = ""
            paste_ioc_section = ""

            iocs_dict = {}  # Use a dictionary to remove duplicates by value
            # for each url, extract iocs from url directly
            blog_for_urls = []

            iocs_dict = {}  # Use a dictionary to remove duplicates by value
            for link in unique_urls:
                #blog = click_into_page_with_browser(
                    #link, is_text=False, headless_flag=False
                #)
                blog = click_into_page_with_browser(
                    link, is_text=True, headless_flag=False
                )
                html = url_open_with_browser(link)
                date = add_date(html)
                if date:
                    pub_date = date
                else:
                    pub_date = "Unspecified"

                length = num_tokens_from_string(blog, "gpt-4o")
                if length > 120000:
                    blog = blog[:120000]
                # Proper formatting for IoCs
                blog = blog.replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https")
                blog_for_urls.append({"blog": blog, "source": link})
                
                iocs_json = extract_iocs_from_text(blog, link)
                if iocs_json:
                    for ioc in iocs_json:
                        ioc_tuple = (ioc['type'], ioc['value'], ioc['source'], pub_date)
                        # Use ioc['value'] as the key to ensure uniqueness
                        iocs_dict[ioc['value']] = ioc_tuple


            unique_iocs = [{"type": ioc[0], "value": ioc[1], "source": ioc[2], "publish_date": ioc[3]} for ioc in iocs_dict.values()]
            print(f"Unique IoCs: {unique_iocs}")
            if not unique_iocs:
                text_output += "- No IoCs found. \n"
                return text_output
            white_list = get_white_list_urls('All Intelligence Feeds.csv')
            unique_urls.update(white_list)

            for ioc_data in unique_iocs:
                ioc_value = ioc_data["value"].replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https").replace("[", "").replace("]", "")
                print(f"====== Processing IoC: {ioc_value} ======")
                if ioc_value in unique_urls or filter_url(ioc_value, unique_urls, white_list):
                    continue
                ioc_type = ioc_data["type"]

                pub_date = ioc_data['publish_date']
                ioc_source = ioc_data.get('source', 'No link provided')
                blogs_for_target_source = next((entry["blog"] for entry in blog_for_urls if entry["source"] == ioc_source), None)

                try:
                    if ioc_type in ["hash_md5", "hash_sha1", "hash_sha256"]:
                        ioc_type_for_check = 'hash'
                    else:
                        ioc_type_for_check = ioc_type

                    is_malicious = check_ioc(ioc_value, ioc_type_for_check)
                    in_article = ioc_value in blogs_for_target_source and "True" in llm_judgment_for_ioc_in_blog(ioc_value, blogs_for_target_source)

                    if is_malicious == True and in_article and is_valid_ioc(ioc_value, ioc_type):
                        # if ioc_type.lower() == 'email' and filter_email(ioc_value, unique_urls, white_list):
                            # continue
                        text_output += f"- {ioc_type}: {ioc_value}  Publish date: {pub_date} [In [this link]({ioc_source}), Verified via VT]\n"
                        paste_ioc_section += f"{ioc_value}\n\n"
                        print(f"The {ioc_type} {ioc_value} is malicious and in article link.")
                    
                    elif is_malicious == False and in_article and is_valid_ioc(ioc_value, ioc_type):
                        # text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source}))  Publish date: {pub_date} [In Articles, identified as not malicious via VT]\n"
                        print(f"The {ioc_type} {ioc_value} is not malicious but in article link.")
                    
                    elif is_malicious is None and in_article and is_valid_ioc(ioc_value, ioc_type):
                        if ioc_type.lower() == 'email' and filter_email(ioc_value, unique_urls, white_list):
                            continue
                        text_output += f"- {ioc_type}: {ioc_value}  Publish date: {pub_date} [In [this link]({ioc_source}), not included in VT database]\n"
                        paste_ioc_section += f"{ioc_value}\n\n"
                        print(f"The {ioc_type} {ioc_value} is not in VT database but in article link.")
                    
                    else:
                        print(f"{ioc_type} {ioc_value} is not found in neither article link nor VT.")
                        continue

                except Exception as e:
                    print(f"Error processing {ioc_type} {ioc_value}: {e}")
            
            if paste_ioc_section == "#### paste IoC\n":
                text_output += "- No IoCs found.\n\n"

            text_output += "\n" + paste_ioc_section + "\n"

            return text_output
        except AttributeError as e:
            print("Error in processing the blog.")
            print(e)
            continue

from urllib.parse import urlparse, urlunparse

def sanitize_url(url):
    try:
        parsed = urlparse(url)
        # Handle potential IPv6 addresses
        if parsed.hostname and ':' in parsed.hostname and not parsed.hostname.startswith('['):
            sanitized_hostname = f"[{parsed.hostname}]"
            parsed = parsed._replace(netloc=sanitized_hostname)
        return urlunparse(parsed)
    except Exception as e:
        raise ValueError(f"Invalid URL: {url} - {e}")
    
if __name__ == '__main__':
    url = "https://medium.com/walmartglobaltech/qbot-is-back-connect-2d774052369f#new_tab"
    sani = sanitize_url(url)
    f = filter_url(sani, [url], excluded_domains=None)
    print(sani)
    print(f)
    output = threat_research_playground()
    print("="*50)
    print(output)
    fw = open('test_ioc.md', 'w')
    fw.write(output)