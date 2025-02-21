import sys
import os
from urllib.parse import urlparse, urlunparse
import argparse
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.threat_research import *
import json
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import time
from tqdm import tqdm


def check_ioc_lists_for_non_vt(ioc_value, original_text, model_name): 
    sys_prompt = """
    ### Role Description
    You are a cybersecurity expert. Your task is to evaluate a set of potential Indicators of Compromise (IoCs) that are not in the VT database.
    For each provided item, determine whether it is a valid IoC and if it appears in the provided original text.

    ### Definitions
    - **Valid Indicators of Compromise (IoCs):**
        - **IP Addresses:** Malicious or suspicious IPs involved in cyber attacks.
        - **Domain Names:** Malicious or suspicious domains used in phishing or command-and-control activities.
        - **URLs:** Web addresses linked to malware distribution or phishing.
        - **Email Addresses:** Addresses used in phishing or spam campaigns.
        - **File Hashes:** Cryptographic hashes (e.g., MD5, SHA1, SHA256) of malicious files.
    - **Non-IoCs:** Items not typically associated with malicious activity, such as commit IDs, GUIDs, or random hash strings not linked to malware.

    ### Task Instructions
    1. **Evaluate each item:** For each item provided, check if it qualifies as a valid IoC based on the definitions above.
    2. **Check for presence in text:** Verify whether the item appears in the provided original text.
       Consider exact matches or minor obfuscations (e.g., "[.]", "hXXp", "hXXps", extra spaces, or special characters).
    3. **Output format:**
       - If an item is both a valid IoC and present in the text, include it in the output list.
       - If none of the items satisfy both conditions, output "None".
       - Your output must be strictly a Python list of strings (e.g., ["item1", "item2"]). If no item qualifies, output exactly "None".
    4. **No extra text:** Do not include any explanations, extra text, or code space like ```python
        ["frutosall@proton.me"]
        ```; output only the list or "None".

    ### Examples
    **Items provided:** ['eef3d33656ce2f2dcde74e2abb19c0d50de198e2', 'fee579589ac919ee6145ffd56f4ea022cfd77afe']

    **Original Text:**
    'Mon Nov 11 13:34:33 2024 +0000
    tree
    fee579589ac919ee6145ffd56f4ea022cfd77afe
    parent
    eef3d33656ce2f2dcde74e2abb19c0d50de198e2
    [
    diff
    ]
    UPSTREAM: USB: media: uvcvideo: Skip parsing frames of type UVC_VS_UNDEFINED in uvc_parse_format

    This can lead to out of bounds writes since frames of this type were not
    taken into account when calculating the size of the frames buffer in
    uvc_parse_streaming.

    Fixes: c0efd232929c ("V4L/DVB (8145a): USB Video Class driver")
    Signed-off-by: Benoit Sevens <bsevens@google.com>
    Cc: stable@vger.kernel.org
    Acked-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
    Reviewed-by: Laurent Pinchart <laurent.pinchart@ideasonboard.com>
    Signed-off-by: Hans Verkuil <hverkuil@xs4all.nl>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
    Bug: 378455392
    (cherry picked from commit ecf2b43018da9579842c774b7f35dbe11b5c38dd)
    Signed-off-by: Greg Kroah-Hartman <gregkh@google.com>
    Change-Id:
    I959a6374ba7adf021fc19da755f5c7611fef9b8c
    drivers/media/usb/uvc/uvc_driver.c
    [
    diff
    ]
    1 file changed
    '

    **Result:** None

    **Items provided:** ['6505b488d0c7f3eaee66e3db103d7b05', 'https://accessservicesonline[.]com/setup_wm.exe', '31.172.83.162:443']
    **Original Text:**
    'Encrypted hosts displayed a modified desktop background, redirecting users to the ransom note.\nTimeline\nDiamond Model\nIndicators\nAtomic\nhxxps://accessservicesonline[.]com/setup_wm.exe\nCobalt Strike:\n31.172.83[.]162:443\nuser[.]compdatasystems[.]com\ncompdatasystems[.]com\n159.100.14[.]254:443\nretailadvertisingservices[.]com\nSystemBC:\n185.236.232[.]20:445\nGhostSOCKS:\n91[.]142[.]74[.]28|30001\n195[.]2[.]70[.]38|30001\n38[.]180[.]61[.]247|30001\nFTP exfiltration servers:\n93.115.26[.]127:21\n46.21.250[.]52:21\nComputed\nFile: svchosts.exe\n6505b488d0c7f3eaee66e3db103d7b05\nbf2b396b8fb0b1de27678aab877b6f177546d1c5\nb4ad5df385ee964fe9a800f2cdaa03626c8e8811ddb171f8e821876373335e63\n\nFile: dfg.exe\n671b967eb2bc04a0cd892ca225eb5034\nab1777107d9996e647d43d1194922b810f198514\nb79bb3302691936df7c3315ff3ba7027f722fc43d366ba354ac9c3dac2e01d03\n\n'
    **Result:** ['6505b488d0c7f3eaee66e3db103d7b05', 'https://accessservicesonline[.]com/setup_wm.exe', '31.172.83.162:443']
    """

    user_prompt = f"""
    ### Task Description
    Given the following items and the provided original text, determine which items are valid Indicators of Compromise (IoCs) according to the definitions above and appear in the text.

    **Items provided:** '{ioc_value}'

    **Original Text:**
    '{original_text}'

    **Result:**
    """

    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]

    try:
        response = api_call(messages, [], model_name, json_enabled=False)
        result = response.choices[0].message.content.strip()
        debug_print(RED + "===> The IoC check result is: " + RESET, result)
        return result
    except Exception:
        return False


def process_unique_iocs_per_source(unique_iocs, all_blogs, unique_urls, white_list, model_name):
    text_output = ""
    paste_ioc_section = ""

    
    for blog_entry in all_blogs:
        unknown_malicious_iocs = []
        source = blog_entry["source"]
        print(f"Processing source: {source}")
        blogs_for_target_source = blog_entry["blog"].replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https").replace("[", "").replace("]", "")
        
        # Filter the unique_iocs that correspond to the current source
        iocs_for_source = [ioc for ioc in unique_iocs if ioc["source"] == source]
        
        for ioc_data in tqdm(iocs_for_source):
            piece_start = time.time()
            ioc_value = ioc_data["value"].replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https").replace("[", "").replace("]", "")
            ioc_type = ioc_data["type"]

            print(f"====== Processing IoC: {ioc_value} ======")
            
            if ioc_value in unique_urls or filter_url(ioc_value, unique_urls, white_list):
                continue

            try:
                if ioc_type in ["hash_md5", "hash_sha1", "hash_sha256"]:
                    ioc_type_for_check = 'hash'
                else:
                    ioc_type_for_check = ioc_type

                is_malicious = check_ioc(ioc_value, ioc_type_for_check)
                in_article = ioc_value in blogs_for_target_source
                
                if is_malicious == True and in_article and is_valid_ioc(ioc_value, ioc_type):
                    text_output += f"- {ioc_type}: {ioc_value} [In {source}, Verified via VT]\n"
                    paste_ioc_section += f"{ioc_value}\n\n"
                    print(f"The {ioc_type} {ioc_value} is malicious and in article link.")
                
                elif is_malicious == False and in_article and is_valid_ioc(ioc_value, ioc_type):
                    print(f"The {ioc_type} {ioc_value} is not malicious but in article link.")
                
                elif is_malicious is None and in_article and is_valid_ioc(ioc_value, ioc_type):
                    # Add to list of unknown malicious IoCs
                    unknown_malicious_iocs.append(ioc_value)
                    # Check with LLM for validity
                    # if "True" in check_ioc_llms_for_non_vt(ioc_value, blogs_for_target_source, model_name):
                        # print(f"[Valid checked by LLM] The {ioc_type} {ioc_value} is valid and not included in VT database.")
                    # else:
                        # print(f"[Invalid checked by LLM] The {ioc_type} {ioc_value} is not valid or not in VT database.")
                
                else:
                    print(f"{ioc_type} {ioc_value} is not found in neither article link nor VT.")
                    continue
            
            except Exception as e:
                print(f"Error processing {ioc_type} {ioc_value}: {e}")
            
            piece_end = time.time()
            print(f"==> Time taken for processing IoC {ioc_value}: {piece_end - piece_start:.2f} seconds")
        

    return text_output, paste_ioc_section


def process_iocs(unique_iocs, all_blogs, unique_urls, model_name):
    """
    Process each IoC (Indicator of Compromise) against a set of known sources (blogs)
    and determine its validity and presence in those sources.

    Args:
        unique_iocs (list): List of unique IoC dictionaries with 'type', 'value', and 'source' keys.
        all_blogs (list): List of blog entries containing 'source' and 'blog' keys.
        unique_urls (list): List of known unique URLs to filter against.
        white_list (list): List of white-listed domains or URLs.
        model_name (str): The model name used for any LLM operations.

    Returns:
        dict: JSON-like dictionary with keys "value" and "source" for valid IoCs.
    """
    print("Starting IoC processing...")
    overall_start_time = time.time()
    ioc_results = []
    
    white_list = get_white_list_urls('src/All Intelligence Feeds.csv')

    # Loop through each blog source
    for blog_entry in all_blogs:
        unknown_malicious_iocs = []
        source = blog_entry["source"]
        print(f"==> Processing source: {source}")
        blogs_for_target_source = (
            blog_entry["blog"]
            .replace("[.]", ".")
            .replace("hXXp", "http")
            .replace("hXXps", "https")
            .replace("[", "")
            .replace("]", "")
        )

        # Filter the unique_iocs that belong to this particular source
        iocs_for_source = [ioc for ioc in unique_iocs if ioc["source"] == source]

        # Process each IoC
        for ioc_data in tqdm(iocs_for_source, desc="Processing IoCs for source"):
            single_ioc_start = time.time()
            ioc_value = (
                ioc_data["value"]
                .replace("[.]", ".")
                .replace("hXXp", "http")
                .replace("hXXps", "https")
                .replace("[", "")
                .replace("]", "")
            )
            ioc_type = ioc_data["type"]

            print(f"==> Processing IoC value: {ioc_value}")

            # Check if IoC already exists in known URLs or white-list
            if ioc_value in unique_urls or filter_url(ioc_value, unique_urls, white_list):
                print(f"Skipped IoC {ioc_value}: found in unique_urls or white_list")
                continue

            try:
                # Determine the type for checking (e.g., treating certain hashes generically)
                ioc_type_for_check = (
                    "hash" if ioc_type in ["hash_md5", "hash_sha1", "hash_sha256"] else ioc_type
                )

                # Check if the IoC is malicious using some defined function
                is_malicious = check_ioc(ioc_value, ioc_type_for_check)
                in_article = ioc_value in blogs_for_target_source

                print(f"IoC malicious status: {is_malicious}, in_article: {in_article}")

                if is_malicious and in_article and is_valid_ioc(ioc_value, ioc_type):
                    ioc_results.append(
                        {
                            "source": source,
                            "value": ioc_value
                        }
                    )
                    print(f"IoC {ioc_value} verified as malicious and in article.")
                elif is_malicious is None and in_article and is_valid_ioc(ioc_value, ioc_type):
                    unknown_malicious_iocs.append(ioc_value)
                    print(f"Unknown malicious IoC detected: {ioc_value}")
                else:
                    print(f"IoC {ioc_value} not found or not valid.")
            except Exception as e:
                print(f"Error processing IoC {ioc_value}: {e}")

            single_ioc_end = time.time()
            print(f"==> Time taken for IoC {ioc_value}: {single_ioc_end - single_ioc_start:.2f} seconds")

        print(f"==> All VT-Unknown malicious IoC detected: {unknown_malicious_iocs}")
        if unknown_malicious_iocs:
            valid_ioc_values_for_unknown_malicious_iocs = check_ioc_lists_for_non_vt(unknown_malicious_iocs, blogs_for_target_source, model_name)
            print(f"==> Checked VT-Unknown malicious IoC detected: {unknown_malicious_iocs}")
            valid_ioc_values_for_unknown_malicious_iocs = eval(valid_ioc_values_for_unknown_malicious_iocs)
            print(f"==> Checked listed VT-Unknown malicious IoC detected: {valid_ioc_values_for_unknown_malicious_iocs}")
            for ioc in valid_ioc_values_for_unknown_malicious_iocs:
                ioc_results.append(
                    {
                        "source": source,
                        "value": ioc
                    }
                )
        else:
            continue


    overall_end_time = time.time()
    print(f"==> Total time taken for all IoCs: {overall_end_time - overall_start_time:.2f} seconds")
    print("IoC processing complete.")
    output_file = f"{model_name}_iocs_output_step2.json"
    print(f"==> Saving IoCs to {output_file}...")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(ioc_results, f, indent=4)
    print("==> IoCs saved successfully.")
    return ioc_results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run an LLM model")
    parser.add_argument("-model", type=str, required=False, help="Model name to run")
    args = parser.parse_args()

    model_name = args.model
    # step1_filename = args.step1_filename
    filename = "o3-mini_iocs_output.json"
    with open("o3-mini_iocs_output.json", "r") as file:
        data = json.load(file)

        # Transform the data
        unique_iocs = [{"type": item["type"], "value": item["value"], "source": item["source"]} for item in data]
    with open("blogs.json", "r") as file:
        data = json.load(file)
        # Transform the data
        all_blogs = [{"source": item["source"], "blog": item["blog"]} for item in data]

    file = 'IoCs.csv'
    df = pd.read_csv(file, header=None)  # The first row is assumed to be the header

    # Extract the first row of values (excluding the header)
    # values = df.iloc[0, 1:].dropna().tolist()
    urls = df.iloc[:, 0].dropna().tolist()
    # Output the resulting list
    print(urls)
    process_iocs(unique_iocs, all_blogs, urls, model_name)
