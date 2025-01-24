import networkx as nx
from search_engine import url_open_with_browser, click_into_page_with_browser
import re
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode
import os
from openai import AzureOpenAI
from tenacity import retry, stop_after_attempt, wait_random_exponential
import json
from bs4 import BeautifulSoup
from deprecated import deprecated
import markdown

os.environ["LOCAL_ENDPOINT"] = "http://10.150.142.182:9999"
os.environ["PROXY_KEY"] = "59ddb6820482b719e33661ccbfa98042"

client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def api_call(messages, temperature, model= "gpt-4o", json_enabled=True):
    if model == 'gpt-4-32k':
        return client.chat.completions.create(
            # model="gpt-4-32k",
            model=model,
            messages=messages,
            # functions= func_list,
            # function_call="auto",  # auto is default, but we'll be explicit
            temperature=temperature,
            # seed=42,
            max_tokens=8192,
        )
    if json_enabled:
        return client.chat.completions.create(
            # model="gpt-4-32k",
            model=model,
            messages=messages,
            # functions= func_list,
            # function_call="auto",  # auto is default, but we'll be explicit
            temperature=temperature,
            response_format={"type": "json_object"},
            # seed=42,
            max_tokens=4096,
        )
    else:
        return client.chat.completions.create(
            # model="gpt-4-32k",
            model=model,
            messages=messages,
            # functions= func_list,
            # function_call="auto",  # auto is default, but we'll be explicit
            temperature=temperature,
            # response_format={ "type": "json_object" },
            # seed=42,
            max_tokens=4096,
        )

def is_valid_url(url):
    try:
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])
    except Exception:
        return False
    
def normalize_url(url):
    parsed = urlparse(url)
    # Sort query parameters for consistent comparison
    query = urlencode(sorted(parse_qsl(parsed.query)))
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', query, ''))

def normalize_url_for_comparison(url):
    parsed = urlparse(url)
    path = re.sub(r'/(rss|feed|amp)/?', '/', parsed.path)
    path = path.rstrip('/')
    return urlunparse((parsed.scheme, parsed.netloc, path, '', '', ''))

def are_urls_same_except_protocol(url1, url2):
    parsed_url1 = urlparse(url1)
    parsed_url2 = urlparse(url2)

    return (parsed_url1.netloc == parsed_url2.netloc and
            parsed_url1.path == parsed_url2.path and
            parsed_url1.params == parsed_url2.params and
            parsed_url1.query == parsed_url2.query and
            parsed_url1.fragment == parsed_url2.fragment)

def extract_links_from_content(urls):
    link_pattern = r'(https?://[^\s\"\'<>]+)'
    url_links = {}  

    # Step 1: Extract all links from each URL's content
    for url in urls:
        try:
            content = url_open_with_browser(url)
            links = set(re.findall(link_pattern, content))
            # Store original links instead of normalized ones
            url_links[url] = {link for link in links if is_valid_url(link)}
        except Exception as e:
            print(f"Error while processing URL {url}: {e}")
            continue

    references = []
    # Step 2: Check reference relationships between URLs
    for source_url, found_links in url_links.items():
        for target_url in urls:
            if source_url == target_url:
                continue
                
            # Check various forms of target URL
            '''
            for found_link in found_links:
                # Protocol-independent comparison
                if are_urls_same_except_protocol(found_link, target_url):
                    print(f"Source: {source_url}, references: {target_url}")
                    references.append((source_url, target_url))
                    break
                
                # Check if URL is contained in content (handles URL rewrites)
                normalized_found = normalize_url(found_link)
                normalized_target = normalize_url(target_url)
                if normalized_target in normalized_found or normalized_found in normalized_target:
                    print(f"Source: {source_url}, references: {target_url}")
                    references.append((source_url, target_url))
                    break
            '''
            found_match = False
            for found_link in found_links:
                # Clean and normalize URLs for comparison
                found_link_clean = found_link.rstrip('/.#')
                target_url_clean = target_url.rstrip('/.#')
                
                # Try different matching strategies
                if any([
                    are_urls_same_except_protocol(found_link_clean, target_url_clean),
                    normalize_url(found_link_clean) == normalize_url(target_url_clean),
                    found_link_clean in target_url_clean or target_url_clean in found_link_clean
                ]):
                    references.append((source_url, target_url))
                    print(f"Source: {source_url}, references: {target_url}")
                    found_match = True
                    break
                
                # Domain-level matching with path consideration
                found_domain = urlparse(found_link_clean).netloc.replace('www.', '')
                target_domain = urlparse(target_url_clean).netloc.replace('www.', '')
                if found_domain == target_domain:
                    found_path = urlparse(found_link_clean).path.rstrip('/')
                    target_path = urlparse(target_url_clean).path.rstrip('/')
                    if found_path and target_path and (found_path in target_path or target_path in found_path):
                        references.append((source_url, target_url))
                        print(f"Source: {source_url}, references: {target_url} (path match)")
                        found_match = True
                        break
            
            if found_match:
                continue
    return url_links, references

def calculate_pagerank(references, urls):
    url_to_id = {url: idx for idx, url in enumerate(urls)}
    id_to_url = {idx: url for url, idx in url_to_id.items()}
    
    graph = nx.DiGraph()
    for source, target in references:
        graph.add_edge(url_to_id[source], url_to_id[target])
    
    pagerank_scores = nx.pagerank(graph)
    pagerank_with_urls = {id_to_url[node]: score for node, score in pagerank_scores.items()}
    
    return pagerank_with_urls, graph, url_to_id


def check_circular_reporting_with_llm(reference_blog, blog):
    sys_prompt = """
    You are an expert in cybersecurity and information analysis. You are tasked with comparing the content of two blogs:
    1. The content of a blog with the highest PageRank (referred to as the "reference blog").
    2. Another blog provided to you (referred to as the "comparison blog").

    Your goal is to determine if the comparison blog contains any additional information not found in the reference blog. Additional information can include new data points, unique insights, or additional details not present in the reference blog.

    Provide your answer as either "Yes" (the comparison blog has additional information) or "No" (it does not). If the answer is "Yes," briefly justify your decision by listing examples of the additional information found in the comparison blog.

    The output format must be:
    Result: <Yes/No>
    Justification (if applicable): <details about the additional information>
    """

    user_prompt = f"""
    Reference Blog Content:
    {reference_blog}

    Comparison Blog Content:
    {blog}
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    response_message = api_call(new_messages, temperature=0.01, model='gpt-4o', json_enabled=False)
    response = response_message.choices[0].message.content
    return response

@deprecated(reason="Use the new extract_urls_from_text function")
def old_extract_urls_from_text(file_path, section_header):
    urls = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            in_section = False
            for line_number, line in enumerate(file, start=1):
                stripped_line = line.strip()
                
                if re.match(rf'^##\s+{re.escape(section_header)}\s*$', stripped_line, re.IGNORECASE):
                    in_section = True
                    continue
                
                if in_section:
                    if re.match(r'^##\s+', stripped_line) and not re.match(rf'^##\s+{re.escape(section_header)}\s*$', stripped_line, re.IGNORECASE):
                        break
                    
                    if stripped_line.startswith('- '):
                        m_pure = re.match(r'^-\s*(https?://\S+)', stripped_line)
                        if m_pure:
                            url = m_pure.group(1)
                            urls.append(url)
                            continue
                        
                        m_md = re.match(r'^-\s*\[.*?\]\((https?://\S+)\)', stripped_line)
                        if m_md:
                            url = m_md.group(1)
                            urls.append(url)
        return urls
    except FileNotFoundError:
        return urls
    except UnicodeDecodeError:
        return urls
    
# def extract_urls_from_text(file_path, section_header):
def extract_urls_from_text(text, section_header):
    urls = []
    try:
        # with open(file_path, 'r', encoding='iso-8859-1') as file:
        #    text = file.read()

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
    

# def filter_duplicate_pipeline(file_path, section_header):
def filter_duplicate_pipeline(source_url, text):
    text_output = ""
    section_header = 'Related articles (describing the same threat)'

    normalized_source_url = normalize_url(source_url)
    print(normalized_source_url)
    urls = extract_urls_from_text(text, section_header)
    urls = [normalize_url(url) for url in urls if normalize_url_for_comparison(source_url) != normalize_url_for_comparison(url)]
    urls.extend([normalized_source_url])
    
    url_links, references = extract_links_from_content(urls)
    print(f"Original references:{references}")
    
    original_source = False
    # print(references)
    # references = [(normalize_url(source), normalize_url(target)) for source, target in references]

    # filter self-reference
    filtered_references = []
    for source, target in references:
        # source_parsed = urlparse(source)
        # target_parsed = urlparse(target)    
        if normalize_url(source) == normalize_url(target) or normalize_url_for_comparison(source) == normalize_url_for_comparison(target):
            continue
        
        filtered_references.append((normalize_url(source), normalize_url(target)))
    
    references = filtered_references
    print(f"Ref: {references}")
    print(f"urls:\n {urls}")

    if not references:
        text_output = []
        for url in urls:
            if normalize_url(url) != normalized_source_url:
                text_output.append(f"- {url}\n")
        return "".join(text_output) if text_output else "No related links found"

    ref_links = []
    for ref in references:
        # start, ref = ref[0]
        # link = ref[0]
        # ref_links.append(link)
        start, ref_link = ref[0], ref[1]
        ref_links.append(start)
        ref_links.append(ref_link)

    print(ref_links)

    # Add reference relationships to output
    # text_output += "### Reference Relationships:\n"
    # for source, target in references:
        # text_output += f"Source link: {source}, reference: {target}\n"

    pagerank_scores, graph, url_to_id = calculate_pagerank(references, urls)
    # text_output += "\n### PageRank Scores:\n"
    for url, score in pagerank_scores.items():
        print(f"{url}: {score:.4f}\n")

    highest_pagerank_url = max(pagerank_scores, key=pagerank_scores.get)
    
    if normalized_source_url in pagerank_scores:
        if pagerank_scores[normalized_source_url] == pagerank_scores[highest_pagerank_url]:
            highest_pagerank_url = normalized_source_url
            original_source = True
            # original_source_text += f"- {source_url}, [Original link with source]\n"

    # text_output += f"\nHighest PageRank URL: {highest_pagerank_url}\n"

    reference_blog_content = click_into_page_with_browser(highest_pagerank_url)
    # text_output += f"\n### Related urls \n"
    original_marked = []
    source_link_marked = []
    unmarked = []

    for url in urls:
        if url == highest_pagerank_url and not original_source:
            original_marked.append(f"- [Original URL of the source] {url}\n")
            continue
        elif url == highest_pagerank_url and original_source:
            continue
        else:
            try:
                comparison_blog_content = click_into_page_with_browser(url)
            except Exception as e:
                continue        
            
            response = check_circular_reporting_with_llm(reference_blog_content, comparison_blog_content)
            
            if 'Yes' in response:
                if normalize_url(url) == normalized_source_url:
                    continue
                elif url in ref_links:
                    source_link_marked.append(f"- [Link to source url] {url}\n")
                else:
                    unmarked.append(f"- {url}\n")
            else:
                continue

    # Combine outputs in the desired order
    text_output = "".join(original_marked + source_link_marked + unmarked)

    return text_output

    # for url in urls:
        # if url == highest_pagerank_url and not original_source:
            # text_output += f"- {url}, [Original URL of the source]\n"
            # continue
        # elif url == highest_pagerank_url and original_source:
            # continue
        # else:
            # try:
                # comparison_blog_content = click_into_page_with_browser(url)
            # except Exception as e:
                # text_output += f"\nError while fetching blog content for URL {url}: {e}\n"
                # continue        
            
            # response = check_circular_reporting_with_llm(reference_blog_content, comparison_blog_content)
            
            # if 'Yes' in response:
                # if normalize_url(url) == normalized_source_url:
                    # continue
                # elif url in ref_links:
                    # text_output += f"- {url} [link to source url]\n"
                # else:
                    # text_output += f"- {url}\n"
            # else:
                # continue
            # text_output += f"- {url}, result: No additional information\n"
            # text_output += f"Judgment result for {url}:\n{response}\n\n"
    # return text_output
            

if __name__ == '__main__':
    """urls = [
        'https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations',
        'https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/',
        'https://www.govinfosecurity.com/hamas-tied-to-october-wiper-attacks-using-eset-email-a-26795',
    ]"""
    
    # file_path = 'mdti_description/AgentGenReport/1209/crypto-stealing-malware-posing-as-a-meeting-app-targets-web3-pros.md'
    # text = open(file_path, 'r', encoding='utf-8').read()
    text = """## Related articles (describing the same threat)

- https://www.elastic.co/security-labs/beyond-the-wail
- https://github.com/Evi1Grey5/MacOS-S """
    url = 'https://research.checkpoint.com/2025/banshee-macos-stealer-that-stole-code-from-macos-xprotect'
    output = filter_duplicate_pipeline(url, text)
    print(output)
    # section_header = 'Related articles (describing the same threat)'
    # file_path = 'example.txt'
    # filter_duplicate_pipeline(file_path, section_header)
    # url1 = "https://www.cadosecurity.com/qubitstrike-an-emerging-malware-campaign-targeting-jupyter-notebooks"
    # url2 = "http://www.cadosecurity.com/qubitstrike-an-emerging-malware-campaign-targeting-jupyter-notebooks"

    # if are_urls_same_except_protocol(url1, url2):
    #    print(f"{url1} and {url2} are the same except for the protocol.")
    # else:
    #     print(f"{url1} and {url2} are different.")
    # urls = ['https://thehackernews.com/2023/10/qubitstrike-targets-jupyter-notebooks.html', 'https://hackread.com/qubitstrike-malware-jupyter-notebook-cryptojacking-cloud-data', 'https://www.cadosecurity.com/qubitstrike-an-emerging-malware-campaign-targeting-jupyter-notebooks', 'https://www.bleepingcomputer.com/news/security/qubitstrike-attacks-rootkit-jupyter-linux-servers-to-steal-credentials/'] 
    # urls = ['https://blog.checkpoint.com/research/hamas-linked-threat-group-expands-espionage-and-destructive-operations', 'https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/','https://www.govinfosecurity.com/hamas-tied-to-october-wiper-attacks-using-eset-email-a-26795']
    # url, ref = extract_links_from_content(urls)
    # print(url['https://www.bleepingcomputer.com/news/security/qubitstrike-attacks-rootkit-jupyter-linux-servers-to-steal-credentials/'])
    # print(ref)


    '''
    urls = [
    'https://thehackernews.com/2024/12/hackers-using-fake-video-conferencing.html',
    'https://medium.com/@cyberstrategy1/fake-meeting-apps-targeting-web3-professionals-how-meeten-malware-steals-crypto-and-sensitive-521591b4b0fb',
    'https://www.cadosecurity.com/blog/meeten-malware-threat',
    'https://cyberinsider.com/new-realst-stealer-campaign-targets-windows-and-macos-systems',
    'https://www.the420.in/hackers-use-fake-video-conferencing-apps-to-deploy-realst-malware-targeting-web3-professionals',
    'https://www.bleepingcomputer.com/news/security/crypto-stealing-malware-posing-as-a-meeting-app-targets-web3-pros',
    'https://www.helpnetsecurity.com/2024/12/06/information-cryptocurrency-stealing-malware-windows-macos',
    'https://www.intego.com/mac-security-blog/mac-malware-masquerades-as-meeting-apps-realst-stealer-is-back'
    ]
     
    urls = extract_urls_from_text(file_path, section_header)
    print(urls)
    url_links, references = extract_links_from_content(urls)

    print("Reference Relationships:")
    for source, target in references:
        print(f"{source} references {target}")

    pagerank_scores, graph, url_to_id = calculate_pagerank(references, urls)
    
    print("\nPageRank Scores:")
    for url, score in pagerank_scores.items():
        print(f"{url}: {score:.4f}")
    print("\nGraph Nodes and Edges:")
    print("Nodes:")
    for node_id, url in url_to_id.items():
        print(f"Node {node_id}: {url}")
    print("Edges:")
    for edge in graph.edges:
        print(f"Edge from Node {edge[0]} to Node {edge[1]}")

    highest_pagerank_url = max(pagerank_scores, key=pagerank_scores.get)
    print(f"\nHighest PageRank URL: {highest_pagerank_url}")

    reference_blog_content = click_into_page_with_browser(highest_pagerank_url)

    for url in urls:
        if url == highest_pagerank_url:
            continue
        
        comparison_blog_content = click_into_page_with_browser(url)
        print(f"\nComparing blog at {url} with the highest PageRank blog...")
        
        response = check_circular_reporting_with_llm(reference_blog_content, comparison_blog_content)
        print(f"Comparison result for {url}:")
        print(response)
    '''

    '''directory = 'mdti_description/AgentGenReport'
    for sub_dir in os.listdir(directory):
        if sub_dir in ['1101', '1106', '1111', '1112', '1114', '1115', '1118', '1119', '1120', '1121', '1122', '1125']:
            continue
        sub_directory = f"{directory}/{sub_dir}"
        print(sub_directory)
        for path in os.listdir(sub_directory):
            if '.md' in path:
                file_path = f"{sub_directory}/{path}"
                filter_duplicate_pipeline(file_path, section_header)
            else:
                continue
'''