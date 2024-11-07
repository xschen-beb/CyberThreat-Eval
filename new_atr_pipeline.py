import pandas as pd
from new_threat_research import threat_research_playground
import os

df = pd.read_csv("AutomatedThreatResearch.csv")

df = df.iloc[6:]

output_location = "241107_ver2_AgentReport/"
prefix = "https://microsoftapc-my.sharepoint.com/personal/xuafeng_microsoft_com/Documents/Documents/AutomatedThreatResearch/"

os.makedirs(output_location, exist_ok=True)

out_data = []

for index, row in df.iterrows():
    link = row['OriginalLinks']
    if pd.isna(link):
        continue  
    if link.endswith('/'):
        link = link[:-1]
    print("Processing:", link)
    
    filename = link.split("/")[-1] + ".md"
    file_path = os.path.join(output_location, filename)
    
    text_output = threat_research_playground(link)
    print(text_output)
    
    with open(file_path, "w", encoding="utf-8") as fw:
        fw.write(text_output)
    
    out_data.append([link, prefix + filename])

out_df = pd.DataFrame(out_data, columns=['OriginalLink', 'Output'])
out_df['Comments'] = '' 
out_df.to_csv("new_AutomatedThreatResearch_out.csv", index=False)
