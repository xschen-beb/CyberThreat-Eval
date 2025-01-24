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
def api_call(messages, temperature, model):
    if model in ['o1-mini', 'o1-preview']:
        return client.chat.completions.create(
            model=model,
            messages=messages,
            # functions= func_list,
            # function_call="auto",  # auto is default, but we'll be explicit
            # temperature=temperature,
            # seed=42,
            # max_tokens=128,
        )
    else:
        return client.chat.completions.create(
            model=model,
            messages=messages,
            # functions= func_list,
            # function_call="auto",  # auto is default, but we'll be explicit
            temperature=temperature,
            # seed=42,
            max_tokens=128,
        )
   


def check_circular_reporting_with_llm(reference_blog, blog):
    sys_prompt = """
    You are an expert in cybersecurity and information analysis. You are tasked with comparing the content of two blogs:
    1. The content of a blog with the highest PageRank (referred to as the "reference blog").
    2. Another blog provided to you (referred to as the "comparison blog").

    Your goal is to determine if the comparison blog contains any additional valid information not found in the reference blog for cybersecurity analysts. Additional information can include new data points, unique insights, additional description ... not present in the reference blog.

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

    # new_messages = [{"role": "system", "content": sys_prompt}]
    # new_messages.append({"role": "user", "content": user_prompt})
    new_messages = [{"role": "user", "content": sys_prompt + user_prompt}]

    response_message = api_call(new_messages, temperature=0.01, model='o1-mini')
    response = response_message.choices[0].message.content
    return response

def calculate():
    directory = 'circular_reporting_result/output'
    TP = TN = FP = FN = 0
    print(len(os.listdir(directory)))
    for path in os.listdir(directory):
        f_path = f"{directory}/{path}"
        f = open(f_path, 'r', encoding='iso-8859-1')
        for line in f:
            data = eval(line)
            if 'No Links' in data['gt_url']:
                continue
            gt = data['gt_result']
            pred = data['pred_result']
            if gt == 'Yes' and pred == 'Yes':
                TP += 1
            elif gt == 'No' and pred == 'No':
                TN += 1
            elif gt == 'No' and pred == 'Yes':
                FP += 1 
            elif gt == 'Yes' and pred == 'No':
                FN += 1
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    print(f"TP: {TP}, TN: {TN}, FP: {FP}, FN: {FN}\n precision: {precision}, recall: {recall}, f1: {f1_score}")

    # return TP, TN, FP, FN, precision, recall, f1_score



if __name__ == '__main__':
    calculate()


    '''
    directory = 'circular_reporting_result/mdti_description/AgentGenReport'
    output_directory = 'circular_reporting_result/output'
    for sub_dir in os.listdir(directory):
        if sub_dir in ['1106', '1111', '1112', '1114', '1115', '1118', '1119', '1120', '1121', '1122', '1125']:
            continue
        sub_directory = f"{directory}/{sub_dir}"
        print(sub_directory)
        for path in os.listdir(sub_directory):
            file_path = f"{sub_directory}/{path}"
            output_path = f"{output_directory}/{path}"
            f = open(file_path, 'r', encoding='iso-8859-1')
            fo = open(output_path, 'a', encoding='utf-8')
            for line in f:
                data = eval(line)
                gt = data['gt_url']
                blog = data["url"]
                pred_res = data["result"]
                if "No links" in gt:
                    continue
                ref_blog = click_into_page_with_browser(gt)
                com_blog = click_into_page_with_browser(blog)
                res = check_circular_reporting_with_llm(ref_blog, blog)
                print(res)
                if 'yes' in res.lower():
                    printable = {"filepath": file_path, "gt_url": "No links", "gt_result": 'Yes', "pred_result": pred_res}
                    fo.write(json.dumps(printable) + '\n')
                else:
                    printable = {"filepath": file_path, "gt_url": "No links", "gt_result": 'No', "pred_result": pred_res}
                    fo.write(json.dumps(printable) + '\n')                

'''
