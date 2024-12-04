import re
import chardet
import requests
import base64
import json
import os

API_KEY = "3ffc901469fd1c77c4cccc82873ccbbb8d5ce0b1de9e4e659e0fe4111b84daf3"

URL = 'https://www.virustotal.com/api/v3/'

HEADERS = {
    'x-apikey': API_KEY
}

def parse_iocs(text):
    pattern = r'(?P<type>domain|ip|email|url|file|hash_(md5|sha256|sha1)):\s*(?P<value>[^\s]+)\s*(?:\([^\)]+\))?'
    
    matches = re.finditer(pattern, text)
    
    iocs = []
    for match in matches:
        ioc_type = match.group('type')
        ioc_value = match.group('value')
        source = "https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/"
        iocs.append({
            "type": ioc_type,
            "value": ioc_value,
            "source": source
        })
    
    return iocs


def read_iocs_from_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
        

        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()
            
            iocs_section = re.search(r'#### IoCs(.+?)(?=####|$)', content, re.DOTALL)
            if iocs_section:
                iocs_text = iocs_section.group(1).strip()
                return iocs_text  
            else:
                print("No IoCs section found.")
                return ""
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return ""


def encode_url(url):
    url_bytes = url.encode("utf-8")
    base64_bytes = base64.urlsafe_b64encode(url_bytes)
    base64_string = base64_bytes.decode("utf-8").rstrip("=")
    return base64_string


def check_ioc(ioc_value, ioc_type):
    try:
        if ioc_type == 'domain':
            url = f"{URL}domains/{ioc_value}"
        elif ioc_type == 'ip':
            url = f"{URL}ip_addresses/{ioc_value}"
        elif ioc_type == 'url':
            submit_url = f"{URL}urls"
            data = {"url": ioc_value}
            response = requests.post(submit_url, headers=HEADERS, data=data)
            response.raise_for_status()
            encoded_url = encode_url(ioc_value)
            url = f"{URL}urls/{encoded_url}"
        elif ioc_type == 'hash':
            url = f"{URL}files/{ioc_value}"
        elif ioc_type == 'email':
            url = f"{URL}emails/{ioc_value}"
        else:
            raise ValueError("Unsupported IOC type")

        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  
        if 'data' in response.json():
            data = response.json()['data']
            if data['attributes']['last_analysis_stats']['malicious'] > 0:
                return "malicious"
            else:
                return "clean"
        else:
            return "unable to detect"
    except requests.exceptions.RequestException as e:
        print(f"Error checking IoC {ioc_value}: {e}")
        return "unable to detect"


def analyze_iocs(iocs):
    malicious_count = 0
    clean_count = 0
    unable_to_detect_count = 0

    for ioc_data in iocs:
        ioc = ioc_data["value"]
        ioc_type = ioc_data["type"]

        # 对 hash 类型做统一处理
        if ioc_type in ["hash_md5", "hash_sha1", "hash_sha256"]:
            ioc_type = 'hash'

        try:
            result = check_ioc(ioc, ioc_type)
            if result == "malicious":
                print(f"The {ioc_type} {ioc} is malicious.")
                malicious_count += 1
            elif result == "clean":
                print(f"The {ioc_type} {ioc} is clean.")
                clean_count += 1
            else:
                print(f"The {ioc_type} {ioc} could not be detected.")
                unable_to_detect_count += 1
        except Exception as e:
            print(f"Error checking {ioc}: {e}")
            unable_to_detect_count += 1

    return malicious_count, clean_count, unable_to_detect_count


def analyze_directory(directory_path):
    result_filename = f"new_prompts_ioc_result.json"
    malicious_counts, clean_counts, unable_to_detect_counts = 0, 0, 0
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and file_path.endswith('.md'):  
            print(f"Processing file: {filename}")
            ioc_text = read_iocs_from_file(file_path)
            if ioc_text:
                iocs = parse_iocs(ioc_text)
                malicious_count, clean_count, unable_to_detect_count = analyze_iocs(iocs)
                malicious_counts += malicious_count
                clean_counts += clean_count
                unable_to_detect_counts += unable_to_detect_count

                result_data = {
                    "filename": filename,
                    "malicious_count": malicious_count,
                    "clean_count": clean_count,
                    "unable_to_detect_count": unable_to_detect_count
                }
                
                with open(result_filename, "a") as result_file:
                    json.dump(result_data, result_file, indent=4)
            else:
                result_data = {
                    "filename": filename,
                    "malicious_count": 0,
                    "clean_count": 0,
                    "unable_to_detect_count": 0
                }
                with open(result_filename, "a") as result_file:
                    json.dump(result_data, result_file, indent=4)
                print(f"Skipping file {filename} due to no IoC section.")

    print(f"""
        "malicious_count": {malicious_counts},
        "clean_count": {clean_counts},
        "unable_to_detect_count": {unable_to_detect_counts}
    """
    )


if __name__ == '__main__':
    directory_path = '241204_original_test' 
    analyze_directory(directory_path)