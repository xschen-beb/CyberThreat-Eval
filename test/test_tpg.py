from threat_research import *

def tpg(new_ti, related_docs, url, work_item_id):
    for _ in range(2):
        try:
            # new_ti, related_docs = threat_research_core(url)
            source_blog = click_into_page_with_browser(
                url, is_text=True, headless_flag=False
            )
            if num_tokens_from_string(source_blog, 'gpt-4o') > 120000:
                source_blog = source_blog[:120000]
            text_output = ""

            # Add the source URL
            text_output += f"Source: [{url}]({url})\n\n"

            # Process related articles
            articles_text = "## Related articles (describing the same threat) \n"
            text_output += "## Related articles (describing the same threat) \n"
            unique_urls = set()
            for doc in related_docs:
                normalized_url = standardize_url(doc["link"])
                unique_urls.add(normalized_url)
            for unique_url in unique_urls:
                # text_output += f"- {unique_url}\n"
                articles_text += f"- {unique_url}\n"
            print(f"articles:\n {articles_text}")
            output = filter_duplicate_pipeline(url, articles_text)
            print(f"Related links: {output}")
            
            if output:
                text_output += output
                articles_text = output
            else:
                text_output += "No related articles found.\n"
                articles_text = "No related articles found.\n"
            text_output += "\n"

            # Enriched Document Section
            text_output += "## Enriched Doc (enrichments marked with *content*(link)): \n"
            paste_ioc_section = "#### paste IoC\n"
            ttps = ""
            print(new_ti)

            for key, value in new_ti.items():
                if key == 'Threat actor/group/campaign':
                    text_output += f"#### {key} \n {value} \n\n"
                    actors = get_actor(value)
                    if actors and 'None' not in actors:
                        # threat_actors = eval(get_actor(value))
                        threat_actors = eval(actors)
                        actor_name, links, context = pipeline(threat_actors, 'oneti', token)
                        actor_info_name = ", ".join(f"{name}" for name in set(actor_name[:3]))
                        # prof_links = "\n".join(f"- {link}" for link in set(links))
                        valid_links = []
    
                        for link in links:
                            # Fetch the page content
                            try:
                                blog_content = click_into_page_with_browser(link)  # Assuming this function returns blog content as a string
                                num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                                
                                # Only include links with content exceeding 500 tokens
                                if num_tokens > 500:
                                    valid_links.append(link)
                            except Exception as e:
                                print(f"Error processing {link}: {e}")
                        
                        # Remove duplicates and format as a list
                        prof_links = "\n".join(f"- {link}" for link in set(valid_links))    

                        if context:
                            context = context.replace('\n\n', '\n')
                            if prof_links:
                                text_output += f"- Based on MDTI profile for {actor_info_name} from the following links: \n\n{prof_links}\n\n The additional threat actor information is:\n\n {context}\n\n"
                            else:
                                text_output += f"- Based on profile for {actor_info_name} from the source and the related articles above: \n\n The additional threat actor information is:\n\n {context}\n\n"
                        else:
                            if num_tokens_from_string(value, 'gpt-4o') < 50:
                                context = augment_threat_actor_with_blog(actors, source_blog)
                                if context:
                                    context = context.replace('\n\n', '')
                                    text_output += f"- Based on profile from the source and the related articles above: \n\n The additional threat actor information is:\n\n {context}\n\n"
                                else:
                                    continue
                            else:
                                continue

                    else:
                        continue
                    print(f"After threat actors, \n\n {text_output}\n\n")

                elif key == 'Root cause':
                    text_output += f"#### {key} \n {value} \n\n"
                    actors = eval(get_root_cause_with_llm(value))
                    actor_name, links, context = root_cause_pipeline(actors, token)
                    # prof_links = "\n".join(f"- {link}" for link in set(links))
                    valid_links = []
    
                    for link in links:
                        # Fetch the page content
                        try:
                            blog_content = click_into_page_with_browser(link)  # Assuming this function returns blog content as a string
                            num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                            
                            # Only include links with content exceeding 500 tokens
                            if num_tokens > 500:
                                valid_links.append(link)
                        except Exception as e:
                            print(f"Error processing {link}: {e}")
                    
                    # Remove duplicates and format as a list
                    prof_links = "\n".join(f"- {link}" for link in set(valid_links))
                    cause = ", ".join(f"{name}" for name in set(actor_name[:3]))
                    if context:
                        context = context.replace('\n\n', '\n')
                        # text_output += f"- Based on MDTI profile for {cause} from the following links: \n\n{prof_links}\n\n The additional context for root cause is:\n\n {context}\n\n"
                        if prof_links:
                            text_output += f"- Based on MDTI profile for {cause}, the additional context for root cause is:\n\n {context}\n\n"
                        else:
                            text_output += f"- Based on profile for {cause} from the source and the related articles above, the additional context for root cause is:\n\n {context}\n\n"
                    print(f"After root cause, \n\n {text_output}\n\n")
                        

                elif key == 'MITRE TTPs':
                    ttp_text = process_mitre_ttps_format(key, value)
                    text_output += ttp_text
                    print(f"After TTPs, \n\n {text_output}\n\n")

                elif key == 'IoCs':
                    continue

                elif key == 'Mitigation Steps':
                    text_output += f"#### {key} \n"
                    actors = get_actor(value)
                    has_mitigation = False

                    if actors and 'None' not in actors:
                        names, links, mdti_recommendation = mdti_recommendation_pipeline(actors, token)
                        # prof_links = "\n".join(f"- {link}" for link in set(links))
                        valid_links = []
    
                        for link in links:
                            # Fetch the page content
                            try:
                                blog_content = click_into_page_with_browser(link)  # Assuming this function returns blog content as a string
                                num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                                
                                # Only include links with content exceeding 500 tokens
                                if num_tokens > 500:
                                    valid_links.append(link)
                            except Exception as e:
                                print(f"Error processing {link}: {e}")
                        
                        # Remove duplicates and format as a list
                        prof_links = "\n".join(f"- {link}" for link in set(valid_links))

                        mitigation_name =  ", ".join(f"{name}" for name in set(actor_name[:3]))
                        if mdti_recommendation != "No recommendations found.":
                            cleaned_recommendation = re.sub(r'\n\s*\n', '\n', mdti_recommendation)
                            if prof_links:
                                text_output += f"- Based on MDTI profile for ({mitigation_name}) from the following links: \n\n{prof_links}\n\n The recommendations are:\n\n"
                            else:
                                text_output += f"- Based on profile for ({mitigation_name}) from the source and the related articles above, the recommendations are:\n\n"

                            text_output += f"{cleaned_recommendation}\n"
                            has_mitigation = True
                    # elif mdti_recommendation == "No recommendations found.":
                    # else:
                    if not has_mitigation:
                        # rec_dict_mitigation = process_rec_dict_ttps(ttps)
                        rec_dict_mitigation = gen_dict_recommendation_from_report(text_output)
                        if rec_dict_mitigation:
                            text_output += f"- Based on OSINT recommendation dictionary ({rec_dict_mitigation}), the recommendations are:\n\n"
                            tech = pd.read_csv('recommendations/RecDict.csv')
                            res = get_recommendation_by_title(tech, rec_dict_mitigation)
                            text_output += f"{rec_dict_mitigation}: {res[1]}\n"
                            # for rec in rec_dict_mitigation:
                                # text_output += f"- [{rec["ttp_id"]}] {rec['title']}: {rec['reason']}\n"
                            has_mitigation = True

                        mitigation = process_all_ttps(ttp_text)
                        if not rec_dict_mitigation and mitigation:
                            # recommendation = eval(mitigation)
                            # for rec in recommendation:
                            # text_output += f"- Based on recommendation table, the source recommends:\n"
                            text_output += f"- Did not find related recommendations from MDTI and OSINT Recommendation Dictionary, based on TTPs, we suggest the following recommendations: \n"
                            for rec in mitigation:
                                text_output += f"- [{rec["ttp_id"]}] {rec['title']}: {rec['reason']}\n"
                            has_mitigation = True
                        # else:
                    if not has_mitigation and value:
                        text_output += f"#### {key} \n {value} \n"
                    text_output += '\n'
                    print(f"After mitigation, \n\n {text_output}\n\n")
                
                elif key == 'Detection Signature':
                    text_output += f"#### Detections/Hunting Queries \n"
                    has_detection = False
                    has_cassie_detection = False

                    if actors and 'None' not in actors:
                        actor_names, links, mdti_detection = mdti_detection_pipeline(threat_actors, token)
                        valid_links = []
    
                        for link in links:
                            # Fetch the page content
                            try:
                                blog_content = click_into_page_with_browser(link)  
                                num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                                
                                if num_tokens > 500:
                                    valid_links.append(link)
                            except Exception as e:
                                print(f"Error processing {link}: {e}")
                        
                        # Remove duplicates and format as a list
                        prof_links = "\n".join(f"- {link}" for link in set(valid_links))

                        detection_name =  ", ".join(f"{name}" for name in set(actor_name[:3]))
                        if mdti_detection != "No detections found.":
                            cleaned_detection = re.sub(r'\n\s*\n', '\n', mdti_detection)
                            if prof_links:
                                text_output += f"- Based on MDTI profile for ({detection_name})\n\n The detections are:\n\n"
                            else:
                                continue

                            text_output += f"{cleaned_detection}\n"
                            has_detection = True
                    # elif mdti_recommendation == "No recommendations found.":
                    # else:
                    if not has_detection:
                        cassie_detection = get_cassie_triage(work_item_id)
                        if cassie_detection:
                            text_output += f"- Based on Cassie Triage profile for ID {work_item_id}\n\n The detections are:\n\n{cassie_detection}\n"
                            has_cassie_detection = True
                        else:
                            text_output += f"- No detections found.\n\n"

                    if not has_detection and not has_cassie_detection:
                        continue
                        # text_output += f"#### {key} \n {value} \n"
                    text_output += '\n'
                    print(f"After detection, \n\n {text_output}\n\n")

                else:
                    formatted_output = ""
                    try:
                        if isinstance(eval(value), dict):
                            for k, v in eval(value).items():
                                if isinstance(v, dict):
                                    formatted_output += f"- {k}\n"
                                    for sub_k, sub_v in v.items():
                                        formatted_output += f"\t - {sub_k}: {sub_v}\n"
                                else:
                                    formatted_output += f"- {k}: {v}\n"
                        else:
                            text_output += f"#### {key} \n {value} \n\n"
                    except Exception as e:
                        text_output += f"#### {key} \n {value} \n\n"
                    print(text_output)

            text_output += "#### IoCs:\n"

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
                ioc_value = ioc_data["value"]
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
            print(f"Error in processing the blog: {e}")
            continue

if __name__ == '__main__':
    new_ti = {'Incident': 'HellCat and Morpheus Ransomware Campaigns', 'Root cause': 'The root cause behind the incident is the use of a shared codebase or builder application by affiliates tied to both HellCat and Morpheus ransomware operations. This shared codebase allows affiliates to compile payloads with almost identical code, leading to similar ransomware behavior and characteristics.', 'Threat actor/group/campaign': 'The primary operators behind HellCat are high-ranking members of the BreachForums community, including personas such as Rey, Pryx, Grep, and IntelBroker. Morpheus operates as a semi-private Ransomware-as-a-Service (RaaS) with less visible public branding efforts.', 'Organization/industry/location': 'The victims include organizations in the pharmaceutical and manufacturing industries, with a specific focus on Italian organizations and virtual ESXi environments.', 'Start date ΓÇô End date': 'The activity was observed from late December 2024, with specific payloads uploaded to VirusTotal on December 22 and December 30, 2024.', 'MITRE TTPs': {'T1486': 'Data Encrypted for Impact, Confidence: High. Justification: The ransomware encrypts files on the targeted systems, leaving original file extensions intact and using the Windows Cryptographic API for key generation and file encryption.', 'T1070.004': 'Indicator Removal on Host: File Deletion, Confidence: Medium. Justification: The ransomware uses a batch file (er.bat) to copy and execute the ransomware, which may include steps to remove traces of the attack.', 'T1105': 'Ingress Tool Transfer, Confidence: Medium. Justification: The ransomware payloads were uploaded to VirusTotal, indicating the transfer of malicious tools to the target environment.', 'T1562.001': 'Impair Defenses: Disable or Modify Tools, Confidence: Medium. Justification: The batch file references various Trend Micro products, suggesting potential attempts to disable or bypass security tools.'}, 'Impact': 'Several machines were compromised, but the exact number is unknown.', 'Mitigation Steps': {'Implement robust endpoint protection solutions to detect and prevent ransomware behaviors.': 'Deploy advanced endpoint protection platforms like SentinelOne Singularity to detect and prevent malicious behaviors associated with HellCat and Morpheus ransomware. Ensure regular updates and patches are applied to all systems to mitigate vulnerabilities.', 'Regularly back up critical data and store backups offline.': 'Establish a comprehensive backup strategy that includes regular backups of critical data and storing backups offline to prevent ransomware from encrypting backup files.', 'Educate employees on phishing and social engineering attacks.': 'Conduct regular training sessions to educate employees on recognizing and avoiding phishing and social engineering attacks, which are common vectors for ransomware delivery.', 'Implement network segmentation to limit the spread of ransomware.': 'Segment the network to isolate critical systems and limit the lateral movement of ransomware. Use firewalls and access controls to restrict unauthorized access.'}, 'Detection Signature': {'Service': 'Windows OS', 'Port': 'Not specified', 'Severity': 'Critical', 'Incident': 'HellCat and Morpheus Ransomware Campaigns', 'Signature name': 'Ransomware file encryption detected', 'Internal checks': {'Setting1': "Monitor for the creation of files with names like '_README_.txt' in user directories. ΓÇô In platform", 'Setting2': "Detect the execution of processes with arguments like 'encryptor.exe ww' or similar patterns. ΓÇô Inside VMs", 'Setting3': 'Monitor for the use of Windows Cryptographic API (BCrypt) for file encryption activities. ΓÇô Inside VMs'}, 'External scanning': {'Monitor for unusual file encryption activities on endpoints.': 'Detect the presence of ransom notes and encrypted files without altered extensions.'}}, 'Indicators of Compromise': {'Files (SHA1)': ["b834d9dbe2aed69e0b1545890f0be6f89b2a53c7 'HellCat'", "f62d2038d00cb44c7cbd979355a9d060c10c9051 'er.bat (Morpheus)'", "f86324f889d078c00c2d071d6035072a0abb1f73 'Morpheus'"], 'Network': ["hellcakbszllztlyqbjzwcbdhfrodx55wq77kmftp4bhnhsnn5r3odad.onion 'HellCat DLS'", "izsp6ipui4ctgxfugbgtu65kzefrucltyfpbxplmfybl5swiadpljmyd.onion 'Morpheus DLS'", "hellcat.locker 'HellCat file service'"], 'Personas': ['h3llr4ns@onionmail.com', 'morpheus@onionmail.com']}}

    related_docs = [{'link':'https://www.sentinelone.com/blog/hellcat-and-morpheus-two-brands-one-payload-as-ransomware-affiliates-drop-identical-code'}]
    url = 'https://www.sentinelone.com/blog/hellcat-and-morpheus-two-brands-one-payload-as-ransomware-affiliates-drop-identical-code'
    work_item_id = '18456085'
    res = tpg(new_ti, related_docs, url, work_item_id)
    print(f"TPG res\n")
    print(res)
    file_name = 'test.md'
    with open(file_name, "w", encoding="utf-8") as fw:
        fw.write(res)


