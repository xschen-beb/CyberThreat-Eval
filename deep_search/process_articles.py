import json
import os
import sys
import time
import traceback
import concurrent.futures
from llm import (
    related_urls, 
    debug_print, 
    RED, 
    RESET, 
    _CREDENTIAL, 
    _AUTH_SCOPE,
    get_bearer_token_provider
)
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential

def process_article(client, article_data, model_name="o3-mini"):
    """Process a single article from the JSON data and return information about related URLs"""
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            # Extract article ID and URL
            article_id = article_data.get("id", "unknown")
            article_url = article_data.get("url", "")
            
            if not article_url:
                debug_print(f"{RED}Article {article_id} has no URL{RESET}")
                return {
                    "id": article_id,
                    "url": "",
                    "number_of_related_urls": 0,
                    "related_urls": [],
                    "error": "No URL provided in article data"
                }
            
            debug_print(f"{RED}Processing article ID: {article_id}, URL: {article_url}{RESET}")
            
            # Get related URLs
            start_time = time.time()
            related_docs = related_urls(client, article_url, model_name)
            end_time = time.time()
            cost_time = end_time - start_time
            
            # Prepare result
            result = {
                "id": article_id,
                "url": article_url,
                "number_of_related_urls": len(related_docs),
                "related_urls": [doc["link"] for doc in related_docs],
                "processing_time": cost_time
            }
            
            debug_print(f"{RED}Article {article_id} processing complete, found {len(related_docs)} related URLs{RESET}")
            return result
            
        except Exception as e:
            retry_count += 1
            debug_print(f"{RED}Error processing article {article_data.get('id', 'unknown')} (attempt {retry_count}/{max_retries}): {str(e)}{RESET}")
            traceback.print_exc()
            
            if retry_count < max_retries:
                debug_print(f"{RED}Retrying article processing...{RESET}")
                time.sleep(2)  # Wait a bit before retrying
            else:
                # Return partial result after all retries failed
                debug_print(f"{RED}All retry attempts failed for article {article_data.get('id', 'unknown')}{RESET}")
                return {
                    "id": article_data.get("id", "unknown"),
                    "url": article_data.get("url", ""),
                    "number_of_related_urls": 0,
                    "related_urls": [],
                    "error": f"Error after {max_retries} attempts: {str(e)}",
                    "traceback": traceback.format_exc()
                }

def process_json_articles(json_file="0510-articles.json", output_dir="processed_results", model_name="o3-mini", max_workers=4):
    """Process all articles from a JSON file and save results to JSON files using thread pool"""
    try:
        # Include model name in the output directory
        model_output_dir = os.path.join(output_dir, model_name)
        
        # Ensure output directory exists
        os.makedirs(model_output_dir, exist_ok=True)
        
        # Initialize Azure OpenAI client
        try:
            if model_name == 'gpt-4o':
                client = AzureOpenAI(
                    azure_endpoint="https://onetiai-swec.openai.azure.com/",
                    azure_ad_token_provider=get_bearer_token_provider(_CREDENTIAL, _AUTH_SCOPE),
                    api_version="2024-12-01-preview",
                )
            else:
                client = AzureOpenAI(
                    azure_endpoint="https://yingqiliu-secphi-aoai.openai.azure.com/",
                    azure_ad_token_provider=get_bearer_token_provider(_CREDENTIAL, _AUTH_SCOPE),
                    api_version="2024-12-01-preview",
                )
        except Exception as e:
            debug_print(f"{RED}Error initializing Azure OpenAI client: {str(e)}{RESET}")
            traceback.print_exc()
            sys.exit(1)
        
        # Load article data from JSON file
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                articles_data = json.load(f)
            
            # Handle different possible JSON structures
            if isinstance(articles_data, dict):
                # If it's a dictionary, check if it has an items list
                if "items" in articles_data:
                    articles = articles_data["items"]
                else:
                    # Otherwise treat the dict values as articles
                    articles = list(articles_data.values())
            elif isinstance(articles_data, list):
                # If it's already a list, use it directly
                articles = articles_data
            else:
                raise ValueError(f"Unexpected JSON format in {json_file}")
                
        except Exception as e:
            debug_print(f"{RED}Error reading JSON file {json_file}: {str(e)}{RESET}")
            traceback.print_exc()
            sys.exit(1)
        
        debug_print(f"{RED}Found {len(articles)} articles to process with {max_workers} workers{RESET}")
        
        # Create a file lock for thread-safe file writing
        from threading import Lock
        file_lock = Lock()
        
        # Function to process one article and save its result
        def process_and_save(i, article_data):
            try:
                debug_print(f"{RED}Processing progress: {i+1}/{len(articles)} - Article ID: {article_data.get('id', 'unknown')}{RESET}")
                
                # Process article and get results
                result = process_article(client, article_data, model_name)
                
                # Thread-safe save individual result to JSON file
                with file_lock:
                    result_filename = f"{result['id']}_results.json"
                    result_path = os.path.join(model_output_dir, result_filename)
                    
                    with open(result_path, 'w', encoding='utf-8') as f:
                        json.dump(result, f, ensure_ascii=False, indent=2)
                    
                    debug_print(f"{RED}Results saved to {result_path}{RESET}")
                
                return result
                
            except Exception as e:
                debug_print(f"{RED}Error processing article {article_data.get('id', 'unknown')}: {str(e)}{RESET}")
                traceback.print_exc()
                
                # Thread-safe save error information
                with file_lock:
                    error_filename = f"error_{article_data.get('id', 'unknown')}.json"
                    error_path = os.path.join(model_output_dir, error_filename)
                    
                    with open(error_path, 'w', encoding='utf-8') as f:
                        json.dump({
                            "id": article_data.get('id', 'unknown'),
                            "error": str(e),
                            "traceback": traceback.format_exc()
                        }, f, ensure_ascii=False, indent=2)
                
                return {
                    "id": article_data.get('id', 'unknown'),
                    "error": str(e)
                }
        
        # Process articles in parallel using ThreadPoolExecutor
        all_results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_article = {
                executor.submit(process_and_save, i, article_data): (i, article_data) 
                for i, article_data in enumerate(articles[45:])
            }
            
            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_article):
                i, article_data = future_to_article[future]
                try:
                    result = future.result()
                    all_results.append(result)
                    debug_print(f"{RED}Completed {i+1}/{len(articles)} - {article_data.get('id', 'unknown')}{RESET}")
                except Exception as e:
                    debug_print(f"{RED}Thread error for article {article_data.get('id', 'unknown')}: {str(e)}{RESET}")
                    all_results.append({
                        "id": article_data.get('id', 'unknown'),
                        "error": f"Thread execution error: {str(e)}"
                    })
        
        # Save all results to a single JSON file
        all_results_path = os.path.join(model_output_dir, "all_results.json")
        with open(all_results_path, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, ensure_ascii=False, indent=2)
            
        debug_print(f"{RED}All articles processed, results saved in {model_output_dir} directory{RESET}")
        debug_print(f"{RED}Summary of all results saved to {all_results_path}{RESET}")
        
    except Exception as e:
        debug_print(f"{RED}Error during processing: {str(e)}{RESET}")
        traceback.print_exc()

if __name__ == "__main__":
    # JSON file and model can be specified via command line arguments
    import argparse
    
    parser = argparse.ArgumentParser(description="Process articles from JSON file and get related URLs")
    parser.add_argument("--json_file", default="0510-articles.json", help="Path to articles JSON file")
    parser.add_argument("--output_dir", default="processed_results", help="Path to output directory")
    parser.add_argument("--model", default="o3-mini", help="Model name to use")
    parser.add_argument("--workers", type=int, default=4, help="Number of worker threads")
    
    args = parser.parse_args()
    
    process_json_articles(args.json_file, args.output_dir, args.model, args.workers) 