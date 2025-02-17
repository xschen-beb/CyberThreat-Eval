import vt
import requests
import os

URL = 'https://www.virustotal.com/api/v3/'
VT_API_KEY = os.getenv('VT_API_KEY')
HEADERS = {
    'x-apikey': VT_API_KEY
}

def check_ioc(ioc_value, ioc_type):
    try:
        if ioc_type == 'domain':
            url = f"{URL}domains/{ioc_value}"
        elif ioc_type == 'ip':
            url = f"{URL}ip_addresses/{ioc_value}"
        elif ioc_type == 'url':
            url = f"{URL}urls/{ioc_value}"
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
                return True
            else:
                return False
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking IoC {ioc_value}: {e}")
        return False


if __name__ == '__main__':
    ioc = "adonis_eros@outlook.com" 
    ioc_type = "email"  

    is_malicious = check_ioc(ioc, ioc_type)
    if is_malicious:
        print(f"The {ioc_type} {ioc} is malicious.")
    else:
        print(f"The {ioc_type} {ioc} is clean.")
