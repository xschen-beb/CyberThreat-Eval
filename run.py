from src.threat_research import threat_research_playground
import os
import time
from datetime import datetime, timedelta
from src.get_cassie_triage import get_recent_urls
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.add_work_item_comments import add_comment_to_workitem
import logging

# Setup logging
logging.basicConfig(
    filename="processing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def pipeline_ver0(output_dir):
    start_time = time.time()

    links_dict = get_recent_urls()
    # print(links_dict)
    # links_dict = {'2312we3': 'https://www.wiz.io/blog/wiz-research-identifies-exploitation-in-the-wild-of-aviatrix-cve-2024-50603'}
    # links_dict = {
        # '12i909': 'https://socradar.io/black-basta-deploying-zbot-darkgate-bespoke-malware',
        # '323wd': 'https://www.bleepingcomputer.com/news/security/russian-isp-confirms-ukrainian-hackers-destroyed-its-network'
        # '323wd': 'https://www.bleepingcomputer.com/news/security/mikrotik-botnet-uses-misconfigured-spf-dns-records-to-spread-malware'
        # '323wd': 'https://www.bleepingcomputer.com/news/security/ivanti-warns-of-new-connect-secure-flaw-used-in-zero-day-attacks'
    # }
    
    output_location = output_dir
    failed_links = []
    processed_count = 0
    saved_paths = {}  # Dictionary to store {work_id: file_path}

    if not os.path.exists(output_location):
        os.makedirs(output_location)

    for work_id, link in list(links_dict.items())[:10]:
        print("Processing link: ", link, " with work_id: ", work_id)

        # Normalize the link to remove trailing slashes
        if link.endswith("/"):
            link = link[:-1]

        # Generate the file name
        file_name = os.path.join(output_location, link.split("/")[-1] + ".md")

        # Check if the file already exists
        if os.path.exists(file_name):
            print(f"File already exists for link: {link}. Skipping...")
            saved_paths[work_id] = file_name  # Add existing file to dictionary
            continue
        
        
        # try:

        # Generate content for the link
        text_output = threat_research_playground(link, work_id)
        processed_count += 1
        print(f"Output for link {link}: \n{text_output}")

        if not text_output:
            print(f"Empty content for link: {link}. Skipping...")
            failed_links.append({"work_id": work_id, "link": link, "error": "Empty content"})
            continue

        # Enable to add comment to Cassia work item
        write_res = add_comment_to_workitem(work_id, text_output)
        print("==>Write response: ", write_res)

        # Write the content to the file
        with open(file_name, "w", encoding="utf-8") as fw:
            fw.write(text_output)
            print(f"Successfully wrote to {file_name}")

        # Add the successfully processed file to the dictionary
        saved_paths[work_id] = file_name

        # except Exception as e:
        #     # Log the failed link and continue with the next one
        #     print(f"Error processing {link}: {e}")]
        #     break
        #     failed_links.append({"work_id": work_id, "link": link, "error": str(e)})

    # Print all failed links at the end
    if failed_links:
        print("\nFailed to process the following links:")
        for failed_link in failed_links:
            print(f"- Work ID: {failed_link['work_id']}, Link: {failed_link['link']}, Error: {failed_link['error']}")

    # Return the dictionary containing {work_id: file_path}
    print(f"Saved paths: {saved_paths}")
    end_time = time.time()
    if processed_count != 0:    
        print(f"Total Time taken: {(end_time - start_time)/processed_count} seconds")
    print(f"Total processed links: {processed_count}")

    return saved_paths


def debug_pipeline(link, work_id):
    text_output = threat_research_playground(link, work_id)
    print(f"Output for link {link}: \n{text_output}")


def process_link(work_id, link, output_location):
    """Process a single link and save its content."""
    try:
        # Normalize the link to remove trailing slashes
        if link.endswith("/"):
            link = link[:-1]

        # Generate the file name
        file_name = os.path.join(output_location, link.split("/")[-1] + ".md")

        # Check if the file already exists
        if os.path.exists(file_name):
            logging.info(f"File already exists for link: {link}. Skipping...")
            return None

        # Generate content for the link
        text_output = threat_research_playground(link, work_id)

        # Write the content to the file
        with open(file_name, "w", encoding="utf-8") as fw:
            fw.write(text_output)
            logging.info(f"Successfully wrote to {file_name}")
        return None

    except Exception as e:
        logging.error(f"Error processing link {link}: {e}")
        return {"work_id": work_id, "link": link, "error": str(e)}  # Return details of the failure

def main():
    links_dict = get_recent_urls()
    print(links_dict)
    output_location = "250123/"
    if not os.path.exists(output_location):
        os.makedirs(output_location)

    failed_links = []
    max_workers = 3  # Adjust the number of workers based on system resources

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_link = {
            executor.submit(process_link, work_id, link, output_location): link
            for work_id, link in links_dict.items()
        }

        for future in as_completed(future_to_link):
            result = future.result()
            if result:  # If the result contains error details, add to failed_links
                failed_links.append(result)

    # Print and log all failed links at the end
    if failed_links:
        logging.warning("Failed to process the following links:")
        for failure in failed_links:
            logging.warning(f"- Work ID: {failure['work_id']}, Link: {failure['link']}, Error: {failure['error']}")
    else:
        logging.info("All links processed successfully.")

if __name__ == '__main__':
    # output_dir = "ATR_20250130"
    # while True:
    #     print("==> Start Query Cassie and Processing...", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    #     save_links = pipeline_ver0(output_dir)
    #     print("==> Finish Query Cassie and Processing...", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    #     time.sleep(3600)

    tests = [
        # ("https://www.trendmicro.com/en_us/research/25/a/cve-2025-0411-ukrainian-organizations-targeted.html", "18470529"),
        # ("https://www.trendmicro.com/en_us/research/25/a/cve-2025-0411-ukrainian-organizations-targeted.html", "18470529"),
        # ("https://www.bleepingcomputer.com/news/security/cisa-orders-agencies-to-patch-linux-kernel-bug-exploited-in-attacks/", "18472287"),
        ("https://gbhackers.com/hackers-exploiting-simplehelp-vulnerabilities/", "18474995"),
        ("https://www.bleepingcomputer.com/news/security/hackers-exploit-cityworks-rce-bug-to-breach-microsoft-iis-servers/", "18475059"),
        ("https://gbhackers.com/asyncrat-abusing-python-and-trycloudflare/", "18470602"),
        # ("https://www.bleepingcomputer.com/news/security/hackers-spoof-microsoft-adfs-login-pages-to-steal-credentials/", "18472278"),
        # ("https://www.bleepingcomputer.com/news/security/hackers-exploit-cityworks-rce-bug-to-breach-microsoft-iis-servers/", "18475059")
    ]
    for link, work_id in tests:
        print(f"==> Processing link: {link} with work_id: {work_id}")
        debug_pipeline(link, work_id)