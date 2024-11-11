from threat_research import threat_research_playground
import time

# open csv file
f = open("AutomatedThreatResearch.csv", "r")
data = f.read()
data = data.split("\n")
data.pop(0)
data.pop()
out_data = []

num = 0
output_location = "241111_AgentReport/"
for i in data:
    link_start_time = time.time()
    num += 1
    if num < 13:
        continue
    # split the data by comma
    print("Processing: ", i)
    i = i.split(",")
    # append the link to the links list
    link = i[0]
    if link.endswith("/"):
        link = link[:-1]
    file_name = output_location + link.split("/")[-1] + "03.md"
    fw = open(file_name, "w")
    text_output = threat_research_playground(link)
    print(text_output)
    fw.write(text_output)
    fw.close()
    prefix = "https://microsoftapc-my.sharepoint.com/personal/xuafeng_microsoft_com/Documents/Documents/AutomatedThreatResearch/"
    out_data.append([link, prefix + file_name])
    link_end_time = time.time()
    link_total_time = link_end_time - link_start_time
    print(f"Processing time for {link}: {link_total_time} seconds")
    with open("processing_times.txt", "a+", encoding="utf-8") as time_file:
        time_file.write(f"Total execution time for link {link}: {link_total_time} seconds\n")

# write the data to a new csv file
f = open("AutomatedThreatResearch_out.csv", "w")
f.write("OriginalLink,Output,Comments\n")
for i in out_data:
    f.write(i[0] + "," + i[1] + ',' "\n")
f.close()
