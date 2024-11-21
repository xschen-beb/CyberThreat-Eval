import threading
from threat_research import threat_research_playground

# open csv file
f = open("1115AutomatedThreatResearch.csv", "r")
data = f.read()
data = data.split("\n")
data.pop(0)
data.pop()
f.close()

out_data = []
output_location = "241120_AgentGenReport/"
lock = threading.Lock()

def process_link(i):
    global out_data
    link = i[0]
    if link.endswith("/"):
        link = link[:-1]
    file_name = output_location + link.split("/")[-1] + ".md"
    
    # Write to markdown file
    fw = open(file_name, "w")
    text_output = threat_research_playground(link)
    fw.write(text_output)
    fw.close()

    prefix = "https://microsoftapc-my.sharepoint.com/personal/xuafeng_microsoft_com/Documents/Documents/AutomatedThreatResearch/"
    
    # Acquire lock to update shared data
    lock.acquire()
    out_data.append([link, prefix + file_name])
    lock.release()

# Create and start threads
threads = []
for i in data:
    i = i.split(",")
    thread = threading.Thread(target=process_link, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Write the data to a new csv file
f = open("AutomatedThreatResearch_out.csv", "w")
f.write("OriginalLink,Output,Comments\n")
for i in out_data:
    f.write(i[0] + "," + i[1] + ",\n")
f.close()
