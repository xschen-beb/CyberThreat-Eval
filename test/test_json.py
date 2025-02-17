import re
import json


def parse_original_text_to_json(text):
    # Define a dictionary to store parsed data
    result = {
        "Incident": "Not specified",
        "Root cause": "Not specified",
        "Threat actor/group/campaign": "Not specified",
        "Organization/industry/location": "Not specified",
        "Start date – End date": "Not specified",
        "MITRE TTPs": [],
        "Impact": "Not specified",
        "Mitigation Steps": [],
        "Detection Signature": "Not specified",
        "IoCs": "No IoCs found"
    }

    # Extract each section using regex or simple splitting
    patterns = {
        "Incident": r"(?<=Incident:)(.*?)(?=\n|$)",
        "Root cause": r"(?<=Root cause:)(.*?)(?=\n|$)",
        "Threat actor/group/campaign": r"(?<=Threat actor/group/campaign:)(.*?)(?=\n|$)",
        "Organization/industry/location": r"(?<=Organization/industry/location:)(.*?)(?=\n|$)",
        "Start date – End date": r"(?<=Start date – End date:)(.*?)(?=\n|$)",
        "Impact": r"(?<=Impact:)(.*?)(?=\n|$)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            result[key] = match.group(1).strip()

    # Extract Mitigation Steps
    mitigation_pattern = r"(?<=Mitigation Steps:)(.*?)(?=\n(?:Detection Signature|IoCs|$))"
    mitigation_match = re.search(mitigation_pattern, text, re.DOTALL)
    if mitigation_match:
        steps = [step.strip("- ").strip() for step in mitigation_match.group(1).strip().split("\n") if step.strip()]
        result["Mitigation Steps"] = steps

    # Extract Detection Signature
    detection_pattern = r"(?<=Detection Signature:)(.*?)(?=\n(?:IoCs|$))"
    detection_match = re.search(detection_pattern, text, re.DOTALL)
    if detection_match:
        signature_text = detection_match.group(1).strip()
        service_match = re.search(r"Service:\s*(.*?)(?=\n|$)", signature_text)
        port_match = re.search(r"Port:\s*(.*?)(?=\n|$)", signature_text)
        severity_match = re.search(r"Severity:\s*(.*?)(?=\n|$)", signature_text)
        incident_match = re.search(r"Incident:\s*(.*?)(?=\n|$)", signature_text)
        signature_name_match = re.search(r"Signature name:\s*(.*?)(?=\n|$)", signature_text)

        internal_checks = {}
        external_scanning = {}

        internal_pattern = re.compile(r"-\s*(Setting\d+):\s*(.*?)(?=\n|$)")
        external_pattern = re.compile(r"-\s*(Port|Check for known vulnerabilities):\s*(.*?)(?=\n|$)")

        for match in internal_pattern.finditer(signature_text):
            internal_checks[match.group(1)] = match.group(2).strip()

        for match in external_pattern.finditer(signature_text):
            external_scanning[match.group(1)] = match.group(2).strip()

        result["Detection Signature"] = {
            "Service": service_match.group(1).strip() if service_match else "Not available",
            "Port": port_match.group(1).strip() if port_match else "Not available",
            "Severity": severity_match.group(1).strip() if severity_match else "Not available",
            "Incident": incident_match.group(1).strip() if incident_match else "Not available",
            "Signature name": signature_name_match.group(1).strip() if signature_name_match else "Not available",
            "Internal checks": internal_checks,
            "External scanning": external_scanning
        }

    # Extract MITRE TTPs with line merging
    mitre_pattern = r"(?<=MITRE TTPs:)(.*?)(?=\n(?:Impact|$))"
    mitre_match = re.search(mitre_pattern, text, re.DOTALL)

    if mitre_match:
        print("MITRE TTPs Section Found!")  # Debugging: Confirm section is found
        
        # Split the section into lines and merge justification lines with TTP lines
        mitre_ttp_lines = [line.strip("- ").strip() for line in mitre_match.group(1).strip().split("\n") if line.strip()]
        print("Original Lines for TTPs:", mitre_ttp_lines)  # Debugging: Log original lines

        # Merge TTP lines with their justification
        merged_lines = []
        temp_line = ""
        for line in mitre_ttp_lines:
            if line.startswith("T"):  # New TTP line
                if temp_line:  # Append the previous complete TTP entry
                    merged_lines.append(temp_line.strip())
                temp_line = line  # Start a new TTP entry
            else:  # Justification line
                temp_line += " " + line  # Append justification to the current TTP entry
        if temp_line:  # Add the last entry
            merged_lines.append(temp_line.strip())
        
        print("Merged Lines for TTPs:", merged_lines)  # Debugging: Log merged lines

        # Parse the merged TTP entries
        ttp_dict = {}
        for line in merged_lines:
            print("Processing Line:", line)  # Debugging: Log each line
            segments = line.split(". Justification: ")  # Split description and justification
            if len(segments) == 2:
                ttp_match = re.match(
                    r"^(T\d+\.\d+|T\d+):\s*(.*?),\s*Confidence:\s*(.*?)$", segments[0], re.IGNORECASE
                )
                if ttp_match:
                    ttp_id = ttp_match.group(1)  # Matches TTP ID (e.g., T1071.001 or T1071)
                    description = ttp_match.group(2)  # Matches the description (e.g., Application Layer Protocol: Web Protocols)
                    confidence = ttp_match.group(3)  # Matches the confidence level (e.g., High)
                    justification = segments[1]  # Matches justification part after split

                    # Add to the TTP dictionary
                    ttp_dict[ttp_id] = f"{description}, Confidence: {confidence}. Justification: {justification}"
                    print(f"Added TTP: {ttp_id}, Description: {description}")  # Debugging: Confirm addition
                else:
                    print(f"Failed to parse TTP line: {line}")
            else:
                print(f"Failed to split Justification: {line}")

        # Add the TTP dictionary to the result
        result["MITRE TTPs"] = ttp_dict

    else:
        print("No MITRE TTPs section found in the text.")  # Debugging: Confirm absence


    # Extract IoCs (if provided)
    iocs_pattern = r"(?<=IoCs:)(.*?)(?=$)"
    iocs_match = re.search(iocs_pattern, text, re.DOTALL)
    if iocs_match:
        iocs_text = iocs_match.group(1).strip()
        if iocs_text.lower() != "no iocs found":
            iocs_list = [ioc.strip() for ioc in iocs_text.split("\n") if ioc.strip()]
            result["IoCs"] = iocs_list

    return result

# Example Input
def test_func():
    text = """
Incident: WordPress Traffic Redirect Malware

Root cause: The root cause of the incident is the injection of malicious code into the themeΓÇÖs `functions.php` file. This code was likely introduced through vulnerabilities in outdated or nulled plugins or themes, poorly designed custom code, pre-existing backdoors, or compromised user accounts.

Threat actor/group/campaign: Not specified

Organization/industry/location: Not specified

Start date ΓÇô End date: Not specified

MITRE TTPs:
- T1071.001: Application Layer Protocol: Web Protocols, Confidence: High.
  Justification: The malware uses HTTP requests to redirect traffic to malicious domains.
- T1059.007: Command and Scripting Interpreter: JavaScript, Confidence: High.
  Justification: The malicious code includes JavaScript that fetches and executes additional payloads.
- T1070.006: Indicator Removal on Host: Timestomp, Confidence: Medium.
  Justification: The malware avoids detection by checking for specific cookies and bypassing execution for logged-in users and administrators.
- T1190: Exploit Public-Facing Application, Confidence: High.
  Justification: The infection likely occurred due to exploiting vulnerabilities in outdated or nulled plugins or themes.

Impact: Several websites were infected, but the exact number is unknown.

Mitigation Steps:
- Update WordPress Core, Plugins, and Themes. **Detailed Steps for mitigation**: Regularly apply updates to close known vulnerabilities. Ensure all components of the WordPress installation are up-to-date to prevent exploitation of known security flaws.
- Audit Custom Code. **Detailed Steps for mitigation**: Ensure custom PHP scripts follow secure coding practices. Review and refactor custom code to adhere to security best practices.
- Scan for Backdoors. **Detailed Steps for mitigation**: Use malware scanners like Sucuri to identify hidden backdoors. Perform regular scans to detect and remove any malicious code or backdoors.
- Strengthen Account Security. **Detailed Steps for mitigation**: Use strong passwords and two-factor authentication for all accounts. Implement policies for regular password changes and monitor for unauthorized access.
- Employ a Website Firewall. **Detailed Steps for mitigation**: A web application firewall (WAF) can block malicious requests before they reach your site. Configure and maintain a WAF to filter out malicious traffic and protect against common web attacks.

Detection Signature:
Service: WordPress
Port: 80/443
Severity: Critical
Incident: WordPress Traffic Redirect Malware
Signature name: ΓÇ£Malicious JavaScript Injection in WordPressΓÇ¥
Internal checks:
  - Setting1: Check for unauthorized modifications in `functions.php` file. ΓÇô In platform
  - Setting2: Monitor for unusual changes in WordPress theme files. ΓÇô Inside VMs
  - Setting3: Scan for known malicious JavaScript patterns. ΓÇô Inside VMs
External scanning:
  - Detect redirects to known malicious domains
  - Identify injected JavaScript fetching external scripts
    """

    # Parse the text into JSON
    parsed_json = parse_original_text_to_json(text)

    # Output the JSON
    j = parsed_json
    for k, v in parsed_json.items():
        print(k, v)

    print(j)
    return j


def test_tpg(original):
    for _ in range(2):
        try:
            # new_ti, related_docs = threat_research_core(url)
            new_ti = original
            url = "https://www.darkreading.com/endpoint-security/trend-micro-and-intel-innovate-to-weed-out-covert-threats"
            related_docs = [{"link": "https://www.darkreading.com/endpoint-security/trend-micro-and-intel-innovate-to-weed-out-covert-threats"}]
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
            output = filter_duplicate_pipeline(url, articles_text)
            print(f"Related links: {output}")
            if output:
                text_output += output
            else:
                text_output += "No related articles found.\n"
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
                        context = pipeline(threat_actors, 'oneti', token)
                        actors = ", ".join(threat_actors)
                        if '\n\n' in context:
                            context = context.replace('\n\n', '')
                        text_output += f"- Additional threat actor information for {actors} from oneti profile: \n {context}\n\n"
                    else:
                        continue

                elif key == 'Root cause':
                    text_output += f"#### {key} \n {value} \n\n"
                    actors = eval(get_root_cause_with_llm(value))
                    context = root_cause_pipeline(actors, token)
                    if context:
                        context = context.replace('\n\n', '')
                        text_output += f"- Additional context: \n {context}\n\n"

                elif key == 'MITRE TTPs':
                    ttps += f"{value}"
                    formatted_ttps = []
                    data = ast.literal_eval(ttps)
                    
                    if isinstance(data, dict):
                        for ttp_id, details in data.items():
                            parts = details.split(', ')  
                            if len(parts) == 2:
                                description = parts[0].strip()  
                                confidence_part = parts[1].strip()  
                                
                                try:
                                    confidence, justification = confidence_part.split('. ', 1)  
                                except ValueError:
                                    confidence, justification = confidence_part.split('\n', 1) 
                            elif len(parts) == 1:
                                description = parts[0].strip()
                                confidence = "N/A"
                                justification = "N/A"
                            else:
                                continue  

                            formatted_ttps.append(f"- {ttp_id}: {description}\n  {confidence}.\n  {justification}\n")


                        text_output += f"#### {key} \n" + "\n".join(formatted_ttps) + "\n"
                        print(text_output)
                    else:
                        text_output += f"#### {key} \n {value}\n\n"

                elif key == 'IoCs':
                    continue

                elif key == 'Mitigation Steps':
                    text_output += f"#### {key} \n"
                    has_mitigation = False

                    if actors and 'None' not in actors:
                        links, mdti_recommendation = mdti_recommendation_pipeline(threat_actors, token)
                        prof_links = "\n".join(links)
                        actor_name =  ", ".join(threat_actors)
                        if mdti_recommendation != "No recommendations found.":
                            cleaned_recommendation = re.sub(r'\n\s*\n', '\n', mdti_recommendation)
                            text_output += f"- Based on MDTI profile ({actor_name}): {prof_links},"
                            text_output += f"{cleaned_recommendation}\n"
                            has_mitigation = True
                    # elif mdti_recommendation == "No recommendations found.":
                    # else:
                    if not has_mitigation:
                        # rec_dict_mitigation = process_rec_dict_ttps(ttps)
                        rec_dict_mitigation = gen_dict_recommendation_from_report(text_output)
                        if rec_dict_mitigation:
                            text_output += f"- Based on OSINT recommendation dictionary ({rec_dict_mitigation}), the recommendations are:\n"
                            tech = pd.read_csv('recommendations/RecDict.csv')
                            res = get_recommendation_by_title(tech, rec_dict_mitigation)
                            text_output += f"{rec_dict_mitigation}: {res[1]}\n"
                            # for rec in rec_dict_mitigation:
                                # text_output += f"- [{rec["ttp_id"]}] {rec['title']}: {rec['reason']}\n"
                            has_mitigation = True

                        mitigation = process_all_ttps(ttps)
                        if not rec_dict_mitigation and mitigation:
                            # recommendation = eval(mitigation)
                            # for rec in recommendation:
                            text_output += "- Based on recommendation table, the source recommends:\n"
                            for rec in mitigation:
                                text_output += f"[{rec["ttp_id"]}] {rec['title']}: {rec['reason']}\n"
                            has_mitigation = True
                        # else:
                    if not has_mitigation and value:
                        text_output += f"#### {key} \n {value} \n"
                    text_output += '\n'
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
            print(unique_iocs)
            if not unique_iocs:
                text_output += "No IoCs found. \n\n"
                continue
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

                    if is_malicious == True and in_article:
                        # if ioc_type.lower() == 'email' and filter_email(ioc_value, unique_urls, white_list):
                            # continue
                        text_output += f"- {ioc_type}: {ioc_value}  Publish date: {pub_date} [In [this link]({ioc_source}), Verified via VT]\n"
                        paste_ioc_section += f"{ioc_value}\n\n"
                        print(f"The {ioc_type} {ioc_value} is malicious and in article link.")
                    
                    elif is_malicious == False and in_article:
                        # text_output += f"- {ioc_type}: {ioc_value} ([link]({ioc_source}))  Publish date: {pub_date} [In Articles, identified as not malicious via VT]\n"
                        print(f"The {ioc_type} {ioc_value} is not malicious but in article link.")
                    
                    elif is_malicious is None and in_article:
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
                text_output += "No IoCs found.\n\n"
            # For more IoCs note
            # text_output += "- For more IoCs, please refer to the above links. \n\n"

            # Append the paste IoC section
            text_output += paste_ioc_section + "\n"

            return text_output
        except AttributeError as e:
            print(f"Error in processing the blog: {e}")
            continue

def process_mitre_ttps_format(key, value):
    """
    Processes the MITRE TTPs field and formats the output.
    """
    text_output = ""
    
    if not value:
        text_output += f"#### {key} \n - No TTPs provided.\n\n"
        return text_output

    formatted_ttps = []
    
    # Check and parse value
    try:
        if isinstance(value, str):
            data = ast.literal_eval(value)  # Convert string to dict/list
        else:
            data = value  # Already a dict or list
    except Exception as e:
        text_output += f"#### {key} \n - Error parsing TTPs: {str(e)}\n\n"
        return text_output

    if isinstance(data, dict):  # If TTPs are a dictionary
        for ttp_id, details in data.items():
            try:
                # Split details into description, confidence, and justification
                parts = details.split(', Confidence: ')
                description = parts[0].strip()
                confidence_justification = parts[1].split('. Justification: ')
                confidence = confidence_justification[0].strip()
                justification = confidence_justification[1].strip()
                
                formatted_ttps.append(
                    f"- {ttp_id}: {description};\n  Confidence: {confidence}.\n  Justification: {justification}"
                )
            except IndexError:
                formatted_ttps.append(f"- {ttp_id}: {details};\n  Confidence: Not specified.\n  Justification: Not specified")
    elif isinstance(data, list):  # If TTPs are a list of dictionaries
        for ttp in data:
            for ttp_id, details in ttp.items():
                try:
                    parts = details.split(', Confidence: ')
                    description = parts[0].strip()
                    confidence_justification = parts[1].split('. Justification: ')
                    confidence = confidence_justification[0].strip()
                    justification = confidence_justification[1].strip()
                    
                    formatted_ttps.append(
                        f"- {ttp_id}: {description};\n  Confidence: {confidence}.\n  Justification: {justification}"
                    )
                except IndexError:
                    formatted_ttps.append(f"- {ttp_id}: {details};\n  Confidence: Not specified.\n  Justification: Not specified")
    else:  # Unsupported data type
        text_output += f"#### {key} \n - Unsupported TTP format: {data}\n\n"
        return text_output

    # Add formatted TTPs to text output
    text_output += f"#### {key} \n" + "\n".join(formatted_ttps) + "\n\n"
    return text_output

if __name__ == '__main__':
    text = """
Incident: Trend Micro and Intel Collaboration to Combat Covert Threats

Root cause: The root cause behind the need for this collaboration is the increasing sophistication of cyber threats, particularly fileless malware and advanced ransomware. These threats often evade traditional software-based security measures by executing in-memory, residing in the registry, or abusing legitimate tools like PowerShell and Windows Management Instrumentation (WMI).

Threat actor/group/campaign: The specific threat actors or groups are not mentioned in the article. However, the focus is on cybercriminals who employ sophisticated techniques to evade detection and compromise critical systems.

Organization/industry/location: The collaboration targets enterprise customers across various industries who need to protect critical systems from stealthy threats.

Start date – End date: The collaboration was announced on January 7, 2025.

MITRE TTPs:
- T1055: Process Injection, Confidence: High. Justification: The article mentions fileless malware that executes in-memory, which aligns with process injection techniques used to evade detection.
- T1086: PowerShell, Confidence: High. Justification: The article highlights the abuse of legitimate tools like PowerShell, which is a common technique used in fileless attacks. 
- T1047: Windows Management Instrumentation, Confidence: High. Justification: The article mentions the abuse of Windows Management Instrumentation (WMI), which is often used by attackers to execute malicious commands and scripts.
- T1486: Data Encrypted for Impact, Confidence: High. Justification: The article discusses the detection of encryption behavior to differentiate between legitimate and malicious activities, indicating a focus on ransomware attacks that encrypt data for impact.

Impact: The collaboration aims to protect critical systems from fileless malware and advanced ransomware, which can lead to significant financial and reputational damage if not mitigated.

Mitigation Steps:
- Implement Advanced Memory Scanning (AMS) with Intel® TDT to offload scanning workloads from CPU to GPU, enabling deeper and more frequent scans to detect fileless attacks.
- Enhance threat detection and response by leveraging CPU telemetry and Intel® AI to provide visibility into the hardware layer.
- Regularly update and patch systems to protect against known vulnerabilities that could be exploited by fileless malware and ransomware.

Detection Signature:
    Service: PowerShell
    Port: Not available
    Severity: Critical
    Incident: Fileless Malware Detection
    Signature name: “PowerShell Abuse Detection”
    Internal checks:
        - Monitor for unusual PowerShell script executions.
        - Detect and alert on PowerShell commands that download or execute remote scripts.
        - Implement logging and monitoring of PowerShell activities.
    External scanning:
        - Detect PowerShell usage patterns indicative of fileless malware.
        - Monitor network traffic for signs of PowerShell-based attacks.

IoCs: No IoCs found
    """
    # original = parse_text_to_json(text)
    j = test_func()
    ttps = j['MITRE TTPs']
    ttp_text = process_mitre_ttps_format('MITRE TTPs', ttps)
    print(ttp_text)
    # print(original)
    # print(json.dumps(original, indent=4))
    # res = test_tpg(original)
    # print(res)
    # fw = open('ttpg.txt', 'w', encoding='utf-8')
    # fw.write(res)