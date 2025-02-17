from src.search_engine import url_open_with_browser, click_into_page_with_browser
from datetime import datetime
import re
from openai import AzureOpenAI
import os
from tenacity import (retry, wait_random_exponential, stop_after_attempt)
import json
from htmldate import find_date


client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)

def add_date(text):
    meta_date_patterns = [
        r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})T',
        r'"datePublished"\s*:\s*"([^"]+)"',
        r'<meta\s+property="article:published_time"\s+content="([^"]+)"'
    ]
    
    for pattern in meta_date_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            try:
                date_str = match.group(1)
                if 'T' in date_str:
                    date_str = date_str.split('T')[0]
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                continue

    iso_date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    iso_matches = re.finditer(iso_date_pattern, text)
    for match in iso_matches:
        try:
            date_str = match.group()
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            continue

    date_indicators = [
        r'Published:?\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}',
        r'Posted:?\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}',
        r'Date:?\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}',
        r'(\d{4}-\d{2}-\d{2})\s*(?:published|posted|updated|written)',
        r'(?:published|posted|updated|written)\s*(?:on|at|date)?\s*(\d{4}-\d{2}-\d{2})',
    ]
    

    for pattern in date_indicators:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            date_str = match.group(1) if len(match.groups()) > 0 else match.group(0)
            try:
                if ',' in date_str:
                    date_obj = datetime.strptime(date_str, '%B %d, %Y')
                else:
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                continue
    

    patterns = [
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}\b',
        r'\b\d{4}-\d{2}-\d{2}\b',
        r'\b\d{1,2}/\d{1,2}/\d{2,4}\b'
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
                
                dates.append((date_obj, date_str))
            except ValueError:
                continue
    
    # Sort dates and return the earliest one (usually the publication date)
    if dates:
        dates.sort()  # Sort by datetime object
        return dates[0][0].strftime('%Y-%m-%d')
    
    return None

from bs4 import BeautifulSoup

def extract_publish_date(url):
    try:
        html = url_open_with_browser(url)
        if not html:
            return "Failed to get page content"
        soup = BeautifulSoup(html, 'html.parser')

        # First check for specific site patterns
        if 'thehackernews.com' in url:
            # TheHackerNews uses specific date format
            date_element = soup.select_one('span[style*="color:#666666"]')
            if date_element:
                return datetime.strptime(date_element.text.strip(), '%b %d, %Y').strftime('%Y-%m-%d')

        # Check common date elements with class attributes
        for tag in ['span', 'time', 'em', 'div']:
            elements = soup.find_all(tag)
            for element in elements:
                classes = element.get('class', [])
                if any(date_class in ' '.join(classes).lower() for date_class in ['published', 'date', 'pubdate', 'post-date', 'entry-date']):
                    try:
                        date_text = element.text.strip()
                        # Try parsing common date formats
                        for fmt in ['%B %d, %Y', '%b %d, %Y', '%Y-%m-%d', '%d %B %Y']:
                            try:
                                return datetime.strptime(date_text, fmt).strftime('%Y-%m-%d')
                            except ValueError:
                                continue
                        return date_text
                    except:
                        continue

        # Check meta tags
        meta_tags = soup.find_all('meta')
        for meta_tag in meta_tags:
            if meta_tag.get('property') in ['article:published_time', 'og:published_time'] or \
               meta_tag.get('name') in ['date', 'publish_date', 'article:published_time']:
                date_content = meta_tag.get('content')
                if date_content:
                    try:
                        return datetime.fromisoformat(date_content.split('T')[0]).strftime('%Y-%m-%d')
                    except ValueError:
                        continue

        # Check URL for date
        url_parts = url.split('/')
        for part in url_parts:
            if re.match(r'\d{4}-\d{2}-\d{2}', part) or \
               re.match(r'\d{4}/\d{2}/\d{2}', part) or \
               re.match(r'\d{4}/\d{2}', part):
                return part.replace('/', '-')

        # Last resort: search in text
        text = soup.get_text()
        date_patterns = [
            r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},?\s+\d{4}\b',
            r'\b\d{4}-\d{2}-\d{2}\b',
            r'\b\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b'
        ]
        
        for pattern in date_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                try:
                    date_str = match.group()
                    if ',' in date_str:
                        return datetime.strptime(date_str, '%b %d, %Y').strftime('%Y-%m-%d')
                    elif '-' in date_str:
                        return date_str
                    else:
                        return datetime.strptime(date_str, '%b %d %Y').strftime('%Y-%m-%d')
                except ValueError:
                    continue

    except Exception as e:
        print(f"Error processing URL {url}: {e}")
        return None

    return None

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def api_call(messages, model="gpt-4o"):
    return client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.01,
        max_tokens=256,
        response_format={"type": "json_object"}
    )
    
    
def get_publication_date(blog_content):
    sys_prompt = """You are a cybersecurity expert specializing in threat intelligence. Your task is to:

1. First look for IoC publication/discovery dates in the blog content
2. If no IoC-specific dates are found, extract the blog's publication date
3. Return the date in YYYY-MM-DD format
4. If no dates can be found, return "No date found"

Look for dates in these priority order:
1. Dates specifically tied to IoCs (e.g., "IoC first observed on...", "Malware sample collected on...")
2. Blog publication date indicators (e.g., "Published on", "Posted:", "Last updated")
3. Dates in the URL structure
4. Any other dates mentioned in the content

The result should be returned strictly in the following format without any prefixes or explanations:
{"ioc_date": "YYYY-MM-DD"}  // or null if no IoC-related date found
"""

    user_prompt = f"""Analyze this blog content for dates:
Content:
{blog_content}"""

    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]

    try:
        response = api_call(messages)
        date_info = json.loads(response.choices[0].message.content)
        if not date_info.get('final_date'):
            raise ValueError("No date found in LLM response")
        return date_info
    except Exception as e:
        print(f"Error in LLM date extraction: {e}")
        return None

def extract_meta_date(text):
    meta_date_patterns = [
        r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})T',
        r'"datePublished"\s*:\s*"([^"]+)"',
        r'<meta\s+property="article:published_time"\s+content="([^"]+)"',
        r'<meta\s+name="date"\s+content="([^"]+)"',
        r'<meta\s+name="publish_date"\s+content="([^"]+)"',
        r'<time\s+datetime="([^"]+)"',
        r'<time\s+class="[^"]*"\s+datetime="([^"]+)"'
    ]
    
    for pattern in meta_date_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            try:
                date_str = match.group(1)

                if 'T' in date_str:
                    date_str = date_str.split('T')[0]

                if ' ' in date_str:
                    date_str = date_str.split(' ')[0]
                
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                return date_obj.strftime('%Y-%m-%d')
            except (ValueError, IndexError):
                continue
    
    return None

def get_date(html):
    meta_date = extract_meta_date(html)
    if meta_date:
        return meta_date
    try:
        fallback_date = find_date(html, original_date=True)
        return fallback_date
    except Exception as e:
        print(f"Error in fallback date extraction: {e}")
        return None

if __name__ == "__main__":
    urls = [
    'https://thehackernews.com/2023/10/qubitstrike-targets-jupyter-notebooks.html',
    'https://hackread.com/qubitstrike-malware-jupyter-notebook-cryptojacking-cloud-data',
    'http://www.cadosecurity.com/qubitstrike-an-emerging-malware-campaign-targeting-jupyter-notebooks',
    'https://www.bleepingcomputer.com/news/security/qubitstrike-attacks-rootkit-jupyter-linux-servers-to-steal-credentials/'
    ]
    url = 'http://www.cadosecurity.com/qubitstrike-an-emerging-malware-campaign-targeting-jupyter-notebooks'
    html = url_open_with_browser(url)
    f = open('html.txt', 'w', encoding='utf-8')
    f.write(html)
    # print(html)
    for url in urls:
        html = url_open_with_browser(url)
        date = extract_meta_date(html)
        package_date = find_date(html, original_date=True)
        print(f"My date: {date}, package date: {package_date}")
    # blog = click_into_page_with_browser(url)
            
    # date_info = get_publication_date(blog)
    # print(date_info)
    # fallback_date = find_date(html, original_date=True)
    # print(fallback_date)
    '''
    for url in urls:
        try:
            html = url_open_with_browser(url)
            blog = click_into_page_with_browser(url)
            
            # 首先尝试使用LLM提取日期
            date_info = get_publication_date(blog)
            
            if date_info and date_info.get('ioc_date'):
                print(f"URL: {url}\nIoC Date: {date_info.get('ioc_date')}")
            # elif date_info and date_info.get('blog_date'):
                # print(f"URL: {url}\nBlog Date: {date_info.get('blog_date')}")
            else:
                # 如果LLM失败，使用find_date作为备选
                fallback_date = find_date(html, original_date=True)
                if fallback_date:
                    print(f"URL: {url}\nFallback Date: {fallback_date}")
                else:
                    print(f"URL: {url}\nNo date found")
                    
        except Exception as e:
            print(f"Error processing {url}: {e}")
    '''
