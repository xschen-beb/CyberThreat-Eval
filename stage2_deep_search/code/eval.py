import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import networkx as nx
import re
import traceback
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from utils.search_engine import click_into_page_with_browser
from tenacity import retry, stop_after_attempt, wait_random_exponential
from tqdm import tqdm
import concurrent
from datetime import datetime
import logging
import tiktoken

# Constants and global variables
RED = "\033[31m"
RESET = "\033[0m"
_AUTH_SCOPE = "https://cognitiveservices.azure.com/.default"
_CREDENTIAL = DefaultAzureCredential()
total_llm_call = 0
total_tokens = 0

def setup_logging(log_file):
    """Set up logging to file and console"""
    # Reset any existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
        
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Create handlers with explicit UTF-8 encoding
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    console_handler = logging.StreamHandler()
    
    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def debug_print(*args, **kwargs):
    try:
        message = ' '.join(str(arg) for arg in args)
        logging.debug(message)
        print(*args, **kwargs)
        sys.stdout.flush()
    except UnicodeEncodeError:
        # Handle encoding errors gracefully
        safe_message = ' '.join(repr(arg) for arg in args)
        logging.debug(f"[Encoding issue with original message] {safe_message}")
        print("[Encoding issue with original message]", repr(args), **kwargs)
        sys.stdout.flush()

def num_tokens_from_string(string, model_name="gpt-4o"):
    """Returns the number of tokens in a text string."""
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")  # Use cl100k_base encoding for unknown models
    num_tokens = len(encoding.encode(string))
    return num_tokens

@retry(wait=wait_random_exponential(min=1, max=10), stop=stop_after_attempt(6))
def api_call(client, messages, model_name, json_enabled=True):
    global total_llm_call
    global total_tokens
    total_llm_call += 1
    total_tokens += num_tokens_from_string(str(messages), model_name)
    debug_print(RED + "==> Total LLM Calls: " + RESET, total_llm_call)
    debug_print(RED + "==> Total Tokens: " + RESET, total_tokens)

    # If using custom 'o3-mini' or other specialized series
    if model_name == 'o3-mini' or 'o3-mini' in model_name:
        new_messages = []
        for message in messages:
            if message["role"] == "system":
                new_messages.append({"role": "developer", "content": [{"type": "text", "text": message["content"]}]})
            else:
                new_messages.append({"role": message["role"], "content": [{"type": "text", "text": message["content"]}]})
        
        return client.chat.completions.create(
            model=model_name,
            messages=new_messages,
            response_format={"type": "json_object"} if json_enabled else None,
            max_completion_tokens=100000
        )

    # Otherwise for gpt-4 or other standard models
    if model_name == 'gpt-4-32k':
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.01,
            max_tokens=8192,
            top_p=0.9
        )
    if json_enabled:
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.01,
            response_format={"type": "json_object"},
            max_tokens=4096,
            top_p=0.9
        )
    else:
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.01,
            max_tokens=4096,
            top_p=0.9
        )

def is_valid_url(url):
    """Check if URL is valid"""
    try:
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])
    except Exception:
        return False
    
def normalize_url(url):
    """Normalize URL by sorting query parameters"""
    parsed = urlparse(url)
    # Sort query parameters for consistent comparison
    query = urlencode(sorted(parse_qsl(parsed.query)))
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', query, ''))

def normalize_url_for_comparison(url):
    """Normalize URL for deeper comparison by removing RSS/feed paths"""
    parsed = urlparse(url)
    path = re.sub(r'/(rss|feed|amp)/?', '/', parsed.path)
    path = path.rstrip('/')
    return urlunparse((parsed.scheme, parsed.netloc, path, '', '', ''))

def are_urls_same_except_protocol(url1, url2):
    """Check if URLs are same except for protocol"""
    parsed_url1 = urlparse(url1)
    parsed_url2 = urlparse(url2)

    return (parsed_url1.netloc == parsed_url2.netloc and
            parsed_url1.path == parsed_url2.path and
            parsed_url1.params == parsed_url2.params and
            parsed_url1.query == parsed_url2.query and
            parsed_url1.fragment == parsed_url2.fragment)

def extract_links_from_content(urls):
    """Extract links from the content of each URL"""
    link_pattern = r'(https?://[^\s\"\'<>]+)'
    url_links = {}  

    # Extract all links from each URL's content
    for url in urls:
        try:
            content = click_into_page_with_browser(url)
            links = set(re.findall(link_pattern, content))
            url_links[url] = {link for link in links if is_valid_url(link)}
        except Exception as e:
            debug_print(f"{RED}Error while processing URL {url}: {str(e)}{RESET}")
            continue

    references = []
    # Check reference relationships between URLs
    for source_url, found_links in url_links.items():
        for target_url in urls:
            if source_url == target_url:
                continue
                
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
                    debug_print(f"{RED}Source: {source_url}, references: {target_url}{RESET}")
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
                        debug_print(f"{RED}Source: {source_url}, references: {target_url} (path match){RESET}")
                        found_match = True
                        break
            
            if found_match:
                continue
    return url_links, references

def calculate_pagerank(references, urls):
    """Calculate PageRank for URLs based on their references"""
    url_to_id = {url: idx for idx, url in enumerate(urls)}
    id_to_url = {idx: url for url, idx in url_to_id.items()}
    
    graph = nx.DiGraph()
    for source, target in references:
        graph.add_edge(url_to_id[source], url_to_id[target])
    
    pagerank_scores = nx.pagerank(graph)
    pagerank_with_urls = {id_to_url[node]: score for node, score in pagerank_scores.items()}
    
    return pagerank_with_urls, graph, url_to_id

def check_additional_information_with_voting(reference_blog, comparison_blog, api_key, api_base):
    sys_prompt = """
    You are an expert in cybersecurity and information analysis. You are tasked with comparing the content of two blogs: "reference blog" and "comparison blog".

    Task: decide whether the comparison blog contains "additional information" beyond the reference blog. "Additional information" = any NEW, concrete content that increases understanding, such as:

    - New facts or data (numbers, dates, CVEs, malware names, actors, tools, geography, ...).  
    - New analysis or interpretations (novel links, causes, trends, forecasts, mitigation advice, ...).  
    - Extra technical or contextual details (methods, background, case studies, impact elaboration, ...).
    - Any other additional details absent from the "reference blog"

    Provide your answer as either "True", (the comparison blog has additional information) or "False" (it does not). If the answer is "True", briefly justify your decision by listing examples of the additional information found in the comparison blog.

    Your response MUST be in valid JSON format with these fields:
    {
        "has_additional_info": true/false,
        "justification": "Your justification if has_additional_info is true"
    }
    """

    user_prompt = f"""
    Reference Blog Content:
    {reference_blog}

    Comparison Blog Content:
    {comparison_blog}
    """

    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})
    
    # Extract model name from folder name
    model_name = os.path.basename(model_folder)

    client = OpenAI(
        api_key=api_key,
        base_url=api_base,
    )
    
    try:
        # Call the model
        response_message = api_call(client, new_messages, model_name=model_name)
        response = json.loads(response_message.choices[0].message.content)
        debug_print(f"{RED}Response: {response}{RESET}")
        
        # Return the result
        return {
            "model": model_name,
            "has_additional_info": response.get("has_additional_info", False),
            "justification": response.get("justification", "")
        }
        
    except Exception as e:
        debug_print(f"{RED}Error with model {model_name}: {str(e)}{RESET}")
        traceback.print_exc()
        return {
            "model": model_name,
            "has_additional_info": False,
            "justification": f"Error: {str(e)}"
        }

def process_result_file(result_file, output_dir, model_folder, api_key, api_base):
    """Process a single result file to analyze related URLs"""
    try:
        # Load the result file
        with open(result_file, 'r', encoding='utf-8') as f:
            result_data = json.load(f)
        
        # Extract information
        article_id = result_data.get('id', 'unknown')
        original_url = result_data.get('url', '')
        related_urls = result_data.get('related_urls', [])
        
        if not related_urls or len(related_urls) <= 1:
            debug_print(f"{RED}Not enough related URLs for {article_id}{RESET}")
            return {
                "id": article_id,
                "original_url": original_url,
                "related_urls_count": len(related_urls),
                "reference_url": None,
                "additional_info_urls": [],
                "additional_info_count": 0,
                "model": os.path.basename(model_folder)
            }
        
        debug_print(f"{RED}Analyzing relationships between {len(related_urls)} URLs for article {article_id}{RESET}")
        
        # Step 1: Analyze reference relationships and calculate PageRank
        _, references = extract_links_from_content(related_urls)
        
        # Filter self-references
        filtered_references = []
        for source, target in references:
            if normalize_url(source) == normalize_url(target) or normalize_url_for_comparison(source) == normalize_url_for_comparison(target):
                continue
            filtered_references.append((source, target))
        
        references = filtered_references
        
        # If no references found, use the original URL as reference
        if not references and original_url in related_urls:
            reference_url = original_url
        elif not references:
            reference_url = related_urls[0]  # Use first URL as reference if original not in list
        else:
            # Calculate PageRank to find the reference URL
            pagerank_scores, _, _ = calculate_pagerank(references, related_urls)
            reference_url = max(pagerank_scores, key=pagerank_scores.get) if pagerank_scores else related_urls[0]
        
        debug_print(f"{RED}Reference URL: {reference_url}{RESET}")
        
        # Step 2: Check if other URLs contain additional information
        reference_content = click_into_page_with_browser(reference_url)
        
        additional_info_urls = []
        for url in related_urls:
            if url == reference_url:
                continue
                
            try:
                comparison_content = click_into_page_with_browser(url)
                analysis = check_additional_information_with_voting(reference_content, comparison_content, api_key, api_base)
                
                if analysis.get("has_additional_info", True):
                    additional_info_urls.append({
                        "url": url, 
                        "justification": analysis.get("justification", "")
                    })
                    debug_print(f"{RED}URL with additional info: {url}{RESET}")
            except Exception as e:
                debug_print(f"{RED}Error processing URL {url}: {str(e)}{RESET}")
        
        # Step 3: Prepare and save results
        results = {
            "id": article_id,
            "original_url": original_url,
            "related_urls_count": len(related_urls),
            "reference_url": reference_url,
            "additional_info_urls": additional_info_urls,
            "additional_info_count": len(additional_info_urls),
            "model": os.path.basename(model_folder)
        }
        
        # Save results
        output_filename = f"{article_id}_similarity_analysis.json"
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
            
        debug_print(f"{RED}Results saved to {output_path}{RESET}")
        return results
        
    except Exception as e:
        debug_print(f"{RED}Error processing file {result_file}: {str(e)}{RESET}")
        traceback.print_exc()
        return {
            "id": os.path.basename(result_file).replace("_results.json", ""),
            "error": str(e),
            "model": os.path.basename(model_folder)
        }

def process_all_results(results_dir, output_dir, test_model_name, api_key, api_base, max_workers=4):
    """Process all specified model folders and their result files
    Input results directory is results_dir, which is a list of result files.

    For each result, Your input should be like:
    {
        "id": article_id,
        "original_url": original_url, # the original url of the article from the data
        "related_urls_count": len(related_urls),
        "reference_url": reference_url,
        "additional_info_urls": additional_info_urls,
        "additional_info_count": len(additional_info_urls),
        "model": os.path.basename(model_folder)
    }
    """
    try:
        all_analyses = []
        
        # Process each model folder
        for model_folder in results_dir:
            if not os.path.exists(model_folder):
                debug_print(f"{RED}Model folder not found: {model_folder}{RESET}")
                continue
                
            # Set up logging for this model
            log_file = f"sim-{test_model_name}.log"
            setup_logging(log_file)
            
            debug_print(f"{RED}Processing model folder: {model_folder}{RESET}")
            
            # Create output directory for this model
            model_output_dir = os.path.join(output_dir, test_model_name)
            os.makedirs(model_output_dir, exist_ok=True)
            
            # Get all result files for this model
            result_files = []
            for file in os.listdir(model_folder):
                if file.endswith('_results.json'):
                    result_files.append(os.path.join(model_folder, file))
            
            if not result_files:
                debug_print(f"{RED}No result files found in {model_folder}{RESET}")
                continue
            
            debug_print(f"{RED}Processing {len(result_files)} result files with {max_workers} workers{RESET}")
            
            # Process files in parallel
            model_analyses = []
            
            # File lock for thread-safe operations
            file_lock = Lock()
            
            # Create a progress bar for overall progress
            pbar = tqdm(total=len(result_files), desc=f"Processing {model_name} files", ncols=100, 
                       bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]")
            
            # Counter for completed tasks, protected by lock
            completed_count = 0
            
            # Custom callback to update progress bar
            def update_progress(future):
                nonlocal completed_count
                with file_lock:
                    completed_count += 1
                    pbar.update(1)
                    # Show some stats in progress bar description
                    if not future.exception():
                        result = future.result()
                        add_info_count = result.get("additional_info_count", 0)
                        pbar.set_description(f"Processed {completed_count}/{len(result_files)} files, Add. Info: {add_info_count}")
            
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Submit all tasks
                future_to_file = {}
                for file in result_files:
                    future = executor.submit(process_result_file, file, model_output_dir, model_folder, api_key, api_base)
                    future.add_done_callback(update_progress)
                    future_to_file[future] = file
                
                # Collect results as they complete
                for future in concurrent.futures.as_completed(future_to_file):
                    file = future_to_file[future]
                    try:
                        analysis = future.result()
                        with file_lock:
                            model_analyses.append(analysis)
                    except Exception as e:
                        debug_print(f"{RED}Error in executor for file {file}: {str(e)}{RESET}")
                        traceback.print_exc()
            
            # Close the progress bar
            pbar.close()
            
            # Calculate aggregate statistics for this model
            debug_print(f"{RED}Calculating aggregate metrics for {model_name}...{RESET}")
            
            total_articles = len(model_analyses)
            successful_articles = len([a for a in model_analyses if "error" not in a])
            total_related_urls = sum(a.get("related_urls_count", 0) for a in model_analyses if "error" not in a)
            total_additional_info_urls = sum(a.get("additional_info_count", 0) for a in model_analyses if "error" not in a)
            
            avg_related_urls = total_related_urls / successful_articles if successful_articles else 0
            avg_additional_info_urls = total_additional_info_urls / successful_articles if successful_articles else 0
            percentage_with_additional_info = 100 * len([a for a in model_analyses if a.get("additional_info_count", 0) > 0]) / successful_articles if successful_articles else 0
            
            # Add aggregate metrics to results
            model_aggregate_metrics = {
                "aggregate_metrics": {
                    "model": model_name,
                    "total_articles": total_articles,
                    "successful_articles": successful_articles,
                    "failed_articles": total_articles - successful_articles,
                    "total_related_urls": total_related_urls,
                    "total_additional_info_urls": total_additional_info_urls,
                    "avg_related_urls_per_article": avg_related_urls,
                    "avg_additional_info_urls_per_article": avg_additional_info_urls,
                    "percentage_with_additional_info": percentage_with_additional_info,
                    "timestamp": datetime.now().isoformat()
                }
            }
            
            # Create a final result object with both analyses and aggregate metrics
            model_final_result = {
                "analyses": model_analyses,
                "aggregate_metrics": model_aggregate_metrics["aggregate_metrics"]
            }
            
            # Save all analyses to a single file
            debug_print(f"{RED}Saving results for {model_name}...{RESET}")
            all_analyses_path = os.path.join(model_output_dir, "all_similarity_analyses.json")
            with open(all_analyses_path, 'w', encoding='utf-8') as f:
                json.dump(model_final_result, f, ensure_ascii=False, indent=2)
            
            # Also save just the aggregate metrics to a separate file for easy access
            metrics_path = os.path.join(model_output_dir, "aggregate_metrics.json")
            with open(metrics_path, 'w', encoding='utf-8') as f:
                json.dump(model_aggregate_metrics, f, ensure_ascii=False, indent=2)
                
            debug_print(f"{RED}All analyses for {model_name} completed and saved to {all_analyses_path}{RESET}")
            debug_print(f"{RED}Aggregate metrics for {model_name}:{RESET}")
            debug_print(f"{RED}  Total articles analyzed: {total_articles}{RESET}")
            debug_print(f"{RED}  Articles with additional info: {len([a for a in model_analyses if a.get('additional_info_count', 0) > 0])}{RESET}")
            debug_print(f"{RED}  Average related URLs per article: {avg_related_urls:.2f}{RESET}")
            debug_print(f"{RED}  Average additional info URLs per article: {avg_additional_info_urls:.2f}{RESET}")
            debug_print(f"{RED}  Percentage of articles with additional info: {percentage_with_additional_info:.2f}%{RESET}")
            
            # Add this model's analyses to the overall results
            all_analyses.extend(model_analyses)
        
        # Create combined metrics for all models
        debug_print(f"{RED}Creating combined metrics for all models...{RESET}")
        combined_metrics = {}
        
        for model_name in [os.path.basename(folder) for folder in model_folders]:
            model_results = [a for a in all_analyses if a.get("model") == model_name]
            successful_articles = len([a for a in model_results if "error" not in a])
            
            if successful_articles == 0:
                continue
                
            combined_metrics[model_name] = {
                "total_articles": len(model_results),
                "successful_articles": successful_articles,
                "articles_with_additional_info": len([a for a in model_results if a.get("additional_info_count", 0) > 0]),
                "percentage_with_additional_info": 100 * len([a for a in model_results if a.get("additional_info_count", 0) > 0]) / successful_articles,
                "avg_additional_info_urls": sum(a.get("additional_info_count", 0) for a in model_results if "error" not in a) / successful_articles
            }
        
        # Save combined metrics
        combined_metrics_path = os.path.join(output_dir, "combined_metrics.json")
        with open(combined_metrics_path, 'w', encoding='utf-8') as f:
            json.dump(combined_metrics, f, ensure_ascii=False, indent=2)
            
        debug_print(f"{RED}Combined metrics saved to {combined_metrics_path}{RESET}")
        
    except Exception as e:
        debug_print(f"{RED}Error processing results: {str(e)}{RESET}")
        traceback.print_exc()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Analyze related URLs and information value using model-specific analysis")
    parser.add_argument("--results_dir", help="Directory containing the processed results for all models")
    parser.add_argument("--output_dir", default="similarity_analyses", help="Output directory for similarity analyses")
    parser.add_argument("--workers", type=int, default=4, help="Number of worker threads")
    parser.add_argument("--test_model_name", help="Test model name")
    parser.add_argument("--api_key", help="API key")
    parser.add_argument("--api_base", help="API base")
    args = parser.parse_args()
    
    process_all_results(args.results_dir, args.output_dir, args.test_model_name, args.api_key, args.api_base, args.workers)
    
    