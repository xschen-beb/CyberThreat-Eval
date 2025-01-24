from urllib.parse import urlparse
from threat_research import get_white_list_urls

def standardize_url(url):
    """Normalize URLs by removing trailing slashes and ensuring consistent formatting."""
    parsed = urlparse(url)
    # Remove trailing slash and reconstruct the URL
    return parsed._replace(path=parsed.path.rstrip("/")).geturl()

def threat_research_playground(url):
    for i in range(2):
        try:
            related_docs = [
                {"link": "https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access"},
                {"link": "https://www.wordfence.com/blog/2024/11/really-simple-security-vulnerability/"},
                {"link": "https://www.wordfence.com/threat-intel/vulnerabilities/detail/really-simple-security-free-pro-and-pro-multisite-900-9111-authentication-bypass"},
                {"link": "https://wordpress.org/plugins/really-simple-ssl/advanced/"},
                {"link": "https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access/"},
                {"link": "https://nvd.nist.gov/vuln/detail/CVE-2024-10924"},
                {"link": "https://www.govinfosecurity.com/wordpress-plugin-vulnerability-threatens-4-million-sites-a-26843"},
                {"link": "https://www.ionix.io/blog/cve-2024-10924-explained-security-plugin-flaw-in-millions-of-wordpress-sites/"},
                {"link": "https://thehackernews.com/2024/11/urgent-critical-wordpress-plugin.html"},
            ]
            
            text_output = ""

            text_output += f"Source: [{url}]({url})\n\n"
            text_output += "## Related articles (describing the same threat) \n"

            unique_urls = set()
            for doc in related_docs:
                normalized_url = standardize_url(doc["link"])
                unique_urls.add(normalized_url)

            # Add unique URLs to the output
            for unique_url in unique_urls:
                text_output += f"- {unique_url}\n"
            text_output += "\n"

            text_output += "## Enriched Doc (enrichments marked with *content*(link)): \n"

            return text_output
        except Exception as e:
            print(f"Error in processing URL {url}: {e}")
            continue

def filter_url(url, url_list, excluded_domains=None):
    if excluded_domains == None:
        excluded_domains = []

    parsed_url = urlparse(url)
    base_domain = parsed_url.netloc.replace('www.', '')
    
    if any(excluded_domain in base_domain for excluded_domain in excluded_domains):
        return False
        
    for u in url_list:
        parsed_u = urlparse(u)
        base_u = parsed_u.netloc.replace('www.', '')
        if base_u == base_domain:
            return True
    
    return False


def filter_email(email, url_list, white_list=None):
    email_domain = email.split('@')[1].lower()
    
    for url in url_list:
        parsed_url = urlparse(url)
        url_domain = parsed_url.netloc.replace('www.', '').lower()
        if email_domain == url_domain:
            return True
            
    if white_list:
        for excluded_domain in white_list:
            if email_domain in excluded_domain.lower():
                return True
                
    return False


if __name__ == '__main__':
    # print(threat_research_playground("sa"))
    value = """{
    'Service': 'Rejetto HTTP File Server',
    'Port': 80,
    'Severity': 'Critical',
    'Incident': 'Russia-Aligned TAG-110 Targets Asia and Europe with HATVIBE and CHERRYSPY',
    'Signature name': 'Rejetto HTTP File Server exploitation',
    'Internal checks': {
        'Setting1': 'Rejetto HTTP File Server should not be exposed on external Internet. In platform',
        'Setting2': 'Rejetto HTTP File Server should not listen on the external Internet. Inside VMs',
        'Setting3': 'Rejetto HTTP File Server should secure with authentication credentials. Inside VMs'
    },
    'External scanning': {
        'Port (80) open': '',
        'Rejetto HTTP File Server exploitation detected': ''
    }
}"""
    urls = [
        'https://techcrunch.com/2024/12/30/verizon-says-it-has-secured-its-network-after-breach-by-china-linked-salt-typhoon-group/',
        'carly.page@techcrunch.com', 
        'sergiu@bleepingcomputer.com',
        'https://www.bloomberg.com/news/articles/2024-12-27/us-plans-more-actions-targeting-china-for-salt-typhoon-breach'
    ]
    url_list = [
        'https://www.reuters.com/technology/cybersecurity/chinese-salt-typhoon-cyberespionage-targets-att-networks-secure-carrier-says-2024-12-29',
        'https://www.techcrunch.com/2024/12/30/verizon-says-it-has-secured-its-network-after-breach-by-china-linked-salt-typhoon-group',
        'https://hackread.com/us-telecom-breaches-firms-chinese-salt-typhoon-hackers',
        'https://www.bleepingcomputer.com/news/security/us-shares-tips-to-block-hackers-behind-recent-telecom-breaches', 
        'https://cyberscoop.com/salt-typhoon-telecom-cybersecurity-gaps-white-house-response',
        'https://www.bleepingcomputer.com/news/security/chinese-hackers-breached-t-mobiles-routers-to-scope-out-network',
        'https://www.bloomberg.com/news/articles/2024-12-28/at-t-says-its-network-is-now-clear-after-salt-typhoon-hack',
        'https://www.theregister.com/2024/12/30/att_verizon_confirm_salt_typhoon_breach',
        'https://www.armis.com/blog/breaking-down-salt-typhoon',
        'https://www.bleepingcomputer.com/news/security/white-house-salt-typhoon-hacked-telcos-in-dozens-of-countries'
    ]


    white_list = get_white_list_urls('All Intelligence Feeds.csv')
    print(white_list)
    for url in urls:
        if '@' in url: 
            print(f"Email: {url}") 
            res = filter_email(url, url_list, white_list)
            print(res)
            continue
        print(filter_url(url, url_list, white_list))
