import sys
import os
import argparse
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.threat_research import *
import json
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import time
from tqdm import tqdm

_AUTH_SCOPE = "https://cognitiveservices.azure.com/.default"
_CREDENTIAL = DefaultAzureCredential()
client = AzureOpenAI(
    azure_endpoint="https://onetiai-swec.openai.azure.com/",
    azure_ad_token_provider=get_bearer_token_provider(_CREDENTIAL, _AUTH_SCOPE),
    api_version="2024-12-01-preview",
)

"""client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)"""

def test_gen_ioc(model_name):
    """
    This function processes a collection of blogs stored in a JSON file and extracts Indicators of Compromise (IoCs).
    It formats the IoC data, measures the processing time for each blog and all IoCs collectively, and saves the result as a JSON file.
    """
    blog_for_urls = []  # To keep track of processed blogs and their sources
    all_iocs = []  # To store all IoC data extracted from the blogs

    # Open and read the blogs.json file
    print("==> Opening blogs.json...")
    with open("blogs.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        all_blogs = [{"source": item["source"], "blog": item["blog"]} for item in data]
        print("==> Loaded blogs.json content.")

    # Start tracking the total time for all operations
    total_start_time = time.time()
    # Process each blog entry
    for item in tqdm(all_blogs):
        blog_start = time.time()  # Start timing for processing this particular blog
        print(f"==> Processing blog source: {item['source']}")
        print(f"==> Blog content: {item['blog'][:3000]}... [truncated]")  # Print first 500 chars for brevity
        
        blog = item["blog"]
        link = item["source"]

        # Determine the length in tokens and truncate if necessary
        # length = num_tokens_from_string(blog, model_name)
        # if length > 120000:
            # print(f"==> Blog length exceeds 120,000 tokens; truncating to fit.")
            # blog = blog[:120000]

        # Format the blog text
        blog = blog.replace("[.]", ".").replace("hXXp", "http").replace("hXXps", "https").replace("[", "").replace("]", "")
        blog_for_urls.append({"blog": blog, "source": link})
        print("==> Blog formatted.")

        # Extract IoCs from the blog content
        print("==> Extracting IoCs...")
        iocs_json = extract_iocs_from_text(blog, link, model_name)
        print(f"==> IoC json content: {iocs_json}")
        
        # If IoCs are found, format and add them to the results
        if iocs_json:
            for ioc in iocs_json:
                ioc_item = {
                    "type": ioc.get("type", ""),
                    "value": ioc.get("value", ""),
                    "source": ioc.get("source", "")
                }
                all_iocs.append(ioc_item)
            print(f"==> Found {len(iocs_json)} IoCs in this blog.")
        else:
            print("==> No IoCs found in this blog.")

        blog_end = time.time()  # End timing for this blog
        print(f"==> Time taken for processing link {link}: {blog_end - blog_start:.2f} seconds")
    
        # Calculate and print total runtime
    total_end_time = time.time()
    print(f"==> Total time for processing all IoCs: {total_end_time - total_start_time:.2f} seconds.")
    # Save all IoCs to a JSON file
    output_file = f"{model_name}_iocs_output_step1.json"
    print(f"==> Saving IoCs to {output_file}...")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_iocs, f, indent=4)
    print("==> IoCs saved successfully.")

    return all_iocs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run an LLM model")
    parser.add_argument("-model", type=str, required=False, help="Model name to run")
    args = parser.parse_args()

    model_name = args.model
    all_iocs = test_gen_ioc(model_name)
    print(all_iocs)