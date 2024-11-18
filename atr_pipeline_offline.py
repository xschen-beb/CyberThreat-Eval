import concurrent.futures
import time
from new_threat_research import threat_research_playground

# open csv file
# f = open("AutomatedThreatResearch.csv", "r")
f = open("1114AutomatedThreatResearch.csv", "r")

data = f.read()
data = data.split("\n")
data.pop(0)
data.pop()
output_location = "241118_newAgentReport02/"
out_data = []
prefix = "https://microsoftapc-my.sharepoint.com/personal/xuafeng_microsoft_com/Documents/Documents/AutomatedThreatResearch/"

# Function to process each link
def process_link(i):
    link_start_time = time.time()
    print("Processing: ", i)
    i = i.split(",")
    link = i[0]
    if link.endswith("/"):
        link = link[:-1]
    file_name = output_location + link.split("/")[-1] + ".md"
    text_output = threat_research_playground(link)
    with open(file_name, "w") as fw:
        fw.write(text_output)
    out_data.append([link, prefix + file_name])
    link_end_time = time.time()
    link_total_time = link_end_time - link_start_time
    print(f"Processing time for {link}: {link_total_time} seconds")
    with open("processing_times.txt", "a+", encoding="utf-8") as time_file:
        time_file.write(f"Total execution time for link {link}: {link_total_time} seconds\n")

# Use ThreadPoolExecutor to process links concurrently, controlling the number of threads
max_threads = 4
with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
    executor.map(process_link, data)

# write the data to a new csv file
with open("AutomatedThreatResearch_out.csv", "w") as f:
    f.write("OriginalLink,Output,Comments\n")
    for i in out_data:
        f.write(i[0] + "," + i[1] + ',' "\n")