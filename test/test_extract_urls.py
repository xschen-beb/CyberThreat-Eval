import re
from bs4 import BeautifulSoup
import markdown
from src.filter_similar_articles import *

def extract_urls_from_text(file_path, section_header):
    urls = []
    try:
        with open(file_path, 'r', encoding='iso-8859-1') as file:
            text = file.read()

        html = markdown.markdown(text)
        soup = BeautifulSoup(html, 'html.parser')
        
        for header in soup.find_all(['h2', 'h3']):
            if header.text.strip().lower() == section_header.lower():
                for sibling in header.find_next_siblings():
                    if sibling.name in ['h2', 'h3']:
                        break
                    for li in sibling.find_all('li'):
                        a_tag = li.find('a', href=True)
                        if a_tag:
                            urls.append(a_tag['href'].rstrip(').,'))
                        else:
                            text = li.get_text().strip()
                            if text.startswith('https://') or text.startswith('http://'):
                                urls.append(text.rstrip(').,'))
        return urls
    except FileNotFoundError:
        return urls
    except UnicodeDecodeError:
        return urls
    
    
def test_extract_urls_with_bs():
    file_path = 'mdti_description/AgentGenReport/1114/critical-bug-in-eol-d-link-nas-devices-now-exploited-in-attacks02.md'  
    section_header = 'Related articles (describing the same threat)'
    # urls = extract_urls_from_text(file_path, section_header)
    urls = extract_urls_from_text(file_path, section_header)
    print("提取到的 URLs:")
    for url in urls:
        print(url)

def normalize_url(url):
    parsed = urlparse(url)
    # Sort query parameters for consistent comparison
    query = urlencode(sorted(parse_qsl(parsed.query)))
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', query, ''))

def extract_links_from_content(urls):
    link_pattern = r'https?://[^\s\"\'<>]+'  
    url_links = {}  

    for url in urls:
        try:
            content = url_open_with_browser(url)
            links = set(re.findall(link_pattern, content))
            normalized_links = {normalize_url(link) for link in links if is_valid_url(link)}
            url_links[normalize_url(url)] = normalized_links
        except Exception as e:
            print(f"Error while processing URL {url}: {e}")
            continue

    references = []
    for url, links in url_links.items():
        for other_url in urls:
            normalized_other_url = normalize_url(other_url)
            if normalized_other_url in links:
                references.append((url, normalized_other_url))  
    return url_links, references
  
if __name__ == "__main__":
    urls = ['https://blogs.blackberry.com/en/2024/11/lightspy-apt41-deploys-advanced-deepdata-framework-in-targeted-southern-asia-espionage-campaign#new_tab', 'https://blogs.blackberry.com/en/2024/04/lightspy-returns-renewed-espionage-campaign-targets-southern-asia-possibly-india', 'https://www.volexity.com/blog/2024/11/15/brazenbamboo-weaponizes-forticlient-vulnerability-to-steal-vpn-credentials-via-deepdata/', 'https://thehackernews.com/2024/11/warning-deepdata-malware-exploiting.html', 'https://www.securityweek.com/fortinet-vpn-zero-day-exploited-in-malware-attacks-remains-unpatched-report/']
    urls = [normalize_url(url) for url in urls]  # Normalize URLs here

    url_links, references = extract_links_from_content(urls)
    if not references:
        print(f"No references found between URLs in file: {file_path}")

    references = [(normalize_url(source), normalize_url(target)) for source, target in references]  # Normalize references
    pagerank_scores, graph, url_to_id = calculate_pagerank(references, urls)
    print("\nPageRank Scores:")
    for url, score in pagerank_scores.items():
        print(f"{url}: {score:.4f}")

