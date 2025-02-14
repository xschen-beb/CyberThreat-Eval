import os
import sys

# module_path = os.path.abspath(os.path.join("../.."))
# if module_path not in sys.path:
#    sys.path.append(module_path)
parent_directory = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_directory)
import json
import pandas as pd
from tenacity import (retry, stop_after_attempt, wait_random_exponential)
from openai import AzureOpenAI
import recommendations.step1_prompt as step1_prompt
import recommendations.step2_prompt as step2_prompt
import re
import tiktoken

class Tokenizer:
    """
    A class to tokenize and detokenize input strings using the Hugging Face tokenizers.
    """
    # Initialize the class with the model name
    def __init__(self, model_name):
        # Load the tokenizer from the model name
        self.tokenizer = tiktoken.encoding_for_model(model_name)

    # Define a method to truncate an input string by max token length
    def truncate(self, input_string, max_token_length):
        """This method truncates a string to a maximum token length."""
        # Encode the input string to tokens
        tokens = self.tokenizer.encode(input_string)
        # Check if the number of tokens is greater than the max token length
        if len(tokens) > max_token_length:
            # Truncate the tokens by the max token length
            tokens = tokens[:max_token_length]
        # Decode the tokens back to string
        output_string = self.tokenizer.decode(tokens)
        # Return the output string
        return output_string

    # Define a method to split input string into strings of max token length
    def split(self, input_string, max_token_length):
        """This method splits a string into multiple strings of maximum token length."""
        # Encode the input string to tokens
        tokens = self.tokenizer.encode(input_string)
        # Initialize an empty list to store the output strings
        output_strings = []
        # Loop through the tokens with a step size of max token length
        for i in range(0, len(tokens), max_token_length):
            # Slice the tokens by the current index and the max token length
            sliced_tokens = tokens[i : i + max_token_length]
            # Decode the sliced tokens back to string
            sliced_string = self.tokenizer.decode(sliced_tokens)
            # Append the sliced string to the output strings list
            output_strings.append(sliced_string)
        # Return the output strings list
        return output_strings

    def count_tokens(self, input_string):
        """This method counts the number of tokens in an input string."""
        # Encode the input string to tokens
        tokens = self.tokenizer.encode(input_string)
        # Return the number of tokens
        return len(tokens)

_TOKENIZER = Tokenizer("gpt-4o")
os.environ["LOCAL_ENDPOINT"] = "http://10.150.142.182:9999"
os.environ["PROXY_KEY"] = "59ddb6820482b719e33661ccbfa98042"
client = AzureOpenAI(
    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
    api_key=os.getenv("PROXY_KEY"),
    api_version="2024-05-01-preview",
)

def get_recommendations(data_frame, start, end):
    df_copy = data_frame.copy()
    df_copy["Description"] = df_copy["Description"].apply(lambda x: str(x).replace("\n", " ").replace("<br>", " ").strip() + "\n")
    df_copy["Title"] = df_copy["Title"].apply(lambda x: str(x).replace("\n", " ").replace("<br>", " ").strip())
    df_copy = df_copy.iloc[start:end]
    df_copy.loc[:, "No."] = range(1, len(df_copy) + 1)
    df_copy = df_copy[["No.", "Id", "Title", "Description"]]
    return df_copy.to_markdown(index=False)


def get_recommendation_by_title(data_frame, title):
    try:
        matched_rows = data_frame[data_frame["Title"].str.strip() == title.strip()]
        if len(matched_rows) == 0:
            print(f"No recommendation for '{title}'")
            return None, None
        
        first_match = matched_rows.iloc[0]
        return first_match["Id"], first_match["Description"]
    except Exception as e:
        print(f"Error in finding recommendation: {str(e)}")
        return None, None


def get_recommendations_filtered(data_frame, output):
    try:
        data_frame["Description"] = data_frame["Description"].apply(lambda x: str(x).replace("\n", " ").replace("<br>", " ").strip() + "\n")
        data_frame["Title"] = data_frame["Title"].apply(lambda x: str(x).replace("\n", " ").replace("<br>", " ").strip())
        data_frame = data_frame[data_frame["Title"].isin(output)]
        data_frame["No."] = range(1, len(data_frame) + 1)
        data_frame = data_frame[["No.", "Id", "Title", "Description"]]
        return data_frame.to_markdown(index=False)
    except Exception as e:
        print(f"Error in filtering: {str(e)}")
        return json.dumps({"output_list": []}, ensure_ascii=False)

def count_tokens(messages):
    total = 0
    for message in messages:
        total += _TOKENIZER.count_tokens(message["content"])
    return total


def get_chat_messages(prompt):
    messages = []
    sys_msg = []
    if hasattr(prompt, "system_general_message") and prompt.system_general_message != "":
        sys_msg.append(prompt.system_general_message)
    if hasattr(prompt, "system_grounding_message") and prompt.system_grounding_message != "":
        sys_msg.append(prompt.system_grounding_message)
    if hasattr(prompt, "system_instruction_message") and prompt.system_instruction_message != "":
        sys_msg.append(prompt.system_instruction_message)
    if hasattr(prompt, "system_constraint_message") and prompt.system_constraint_message != "":
        sys_msg.append(prompt.system_constraint_message)
    if len(sys_msg) > 0:
        messages.append({"role": "system", "content": "\n".join(sys_msg)})
    if (hasattr(prompt, "user_example_message") and prompt.user_example_message != "") and (
        hasattr(prompt, "prompt_prefix") and prompt.prompt_prefix != ""
    ):
        messages.append(
            {
                "role": "user",
                "content": prompt.prompt_prefix + prompt.user_example_message,
            }
        )
    if hasattr(prompt, "system_response_message") and prompt.system_response_message != "":
        messages.append({"role": "assistant", "content": prompt.system_response_message})
    return messages


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def call_openai(prompt_list):
    """Call the OpenAI API to get a response from the model."""
    responses = []
    for prompt in prompt_list:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=prompt.messages,
            max_tokens=prompt.max_output_tokens,
            temperature=prompt.temperature,
            seed=123,
            top_p=prompt.top_p,
            response_format={"type": prompt.response_format},
        )
        responses.append(response)
    return responses

def get_ai_response(prompt_list, user_input_list):
    for i, prompt in enumerate(prompt_list):
        prompt.messages = get_chat_messages(prompt) + [{"role": "user", "content": prompt.prompt_prefix + user_input_list[i]}]
        if prompt.optimize:
            if count_tokens(prompt.messages) < 120000:
                prompt.deployment_id = "gpt-4o"
    responses = call_openai(prompt_list)
    return [response.choices[0].message.content for response in responses]

def mapping(user_query, data_frame):
    prompt_list = []
    user_input_list = []
    start = [x for x in range(0, 330, 50)]
    end = [x for x in range(50, 360, 50)]
    for i in range(len(start)):
        grounding = get_recommendations(data_frame, start[i], end[i])
        prompt = step1_prompt.Step1Prompt(grounding)
        user_input = user_query
        prompt_list.append(prompt)
        user_input_list.append(user_input)
    output_list = get_ai_response(prompt_list, user_input_list)
    result = []
    for i, output in enumerate(output_list):
        output = json.loads(output)
        result.extend(output["output_list"])
    return result


def validate(user_query, possible_recommendations):
    prompt_list = []
    user_input_list = []
    prompt = step2_prompt.Step2Prompt()
    user_input = "\n[QUERY START]\n" + user_query + " \n[QUERY END] \n"
    user_input += "\n[POSSIBLE RECOMMENDATIONS START]\n" + possible_recommendations + "\n[POSSIBLE RECOMMENDATIONS END]\n"
    prompt_list.append(prompt)
    user_input_list.append(user_input)
    output_list = get_ai_response(prompt_list, user_input_list)
    return output_list[0]

def get_technique_by_id(technique_id):
    try:
        df = pd.read_csv("recommendations/Techniques.csv")
        
        matched_rows = df[df["ID"] == technique_id]
        
        if len(matched_rows) == 0:
            print(f"Technique for ID '{technique_id}' NOT FOUND.")
            return None, None
        
        first_match = matched_rows.iloc[0]
        return first_match["name"], first_match["description"]
        
    except Exception as e:
        print(f"Error in finding: {str(e)}")
        return None, None


def extract_ttps(text):
    try:
        pattern = r'T\d{1,4}(?:\.\d{1,3})?'
        
        ttps = re.findall(pattern, text)
        
        unique_ttps = sorted(list(set(ttps)))
        
        return unique_ttps
        
    except Exception as e:
        print(f"Error in extracting: {str(e)}")
        return []
    

def main():
    data_frame = pd.read_csv("Techniques.csv")
    data_frame = data_frame[data_frame["is sub-technique"] == False]
    technique_id = []
    technique_name = []
    technique_description = []
    recommendation_id = []
    recommendation_title = []
    recommendation_description = []
    recommendation_score = []
    recommendation_reason = []
    recommendations_df = pd.read_csv("Recommendations.csv")
    for index, row in data_frame.iterrows():
        try:
            user_query = "Suggest recommendations for mitigating the below attack technique:\n"
            user_query += "Attack Name: " + row["name"] + "\n"
            user_query += "Attack Process: " + row["description"] + "\n"
            output = mapping(user_query, recommendations_df)
            possible_recommendations = get_recommendations_filtered(recommendations_df, output)
            output2 = validate(user_query, possible_recommendations)
            recommendations_list = json.loads(output2)["output_list"]
            for rec in recommendations_list:
                technique_id.append(row["ID"])
                technique_name.append(row["name"])
                technique_description.append(row["description"])
                rec_title = rec["title"]
                recommendation_title.append(rec_title)
                
                id, desc = get_recommendation_by_title(recommendations_df, rec_title)
                if id is None or desc is None:
                    print(f"Information about '{rec_title}' NOT FOUND.")
                    continue
                
                recommendation_id.append(id)
                recommendation_description.append(desc)
                recommendation_reason.append(rec["reason"])
                recommendation_score.append(rec["score"])
        except Exception as ex:
            print(f"处理技术 ID: {row['ID']} 时失败")
            print(f"错误详情: {str(ex)}")
            print(f"当前处理的标题: {rec_title if 'rec_title' in locals() else 'unknown'}")
            continue
    # create a data frame using the lists
    data_frame = pd.DataFrame(
        list(
            zip(
                technique_id,
                technique_name,
                technique_description,
                recommendation_id,
                recommendation_title,
                recommendation_description,
                recommendation_score,
                recommendation_reason,
            )
        ),
        columns=[
            "Technique ID",
            "Technique Name",
            "Technique Description",
            "SCID",
            "Recommendation Title",
            "Recommendation Description",
            "Recommendation Score",
            "Explanation",
        ],
    )
    # save the data frame to a excel file
    data_frame.to_excel("output.xlsx", index=False)

def pipeline_recommendations_for_id(test_id, data_frame="Techniques.csv", recommendations_df="Recommendations.csv"):
    name, description = get_technique_by_id(test_id)
    if not name or not description:
        print("No name")
    data_frame = pd.read_csv(data_frame)
    recommendations_df = pd.read_csv(recommendations_df)

    user_query = "Suggest recommendations for mitigating the below attack technique:\n"
    user_query += "Attack Name: " + name + "\n"
    user_query += "Attack Process: " + description + "\n"
    print(user_query)
    output = mapping(user_query, recommendations_df)
    possible_recommendations = get_recommendations_filtered(recommendations_df, output)
    print(f"Output : {output}")
    output2 = validate(user_query, possible_recommendations)
    print(output2)

    rec_list = eval(output2)
    output_list = rec_list["output_list"]
    for rec in output_list:
        rec_title = rec["title"]
        
        id, desc = get_recommendation_by_title(recommendations_df, rec_title)
        print(f"Recommendation id: {id}, \n Reason: {rec['reason']}, \n Description: {desc}")

def process_all_ttps(text, techniques_path="recommendations/Techniques.csv", recommendations_path="recommendations/Recommendations.csv"):
    try:
        # Extract all TTPs
        ttps = extract_ttps(text)
        if not ttps:
            print("No TTPs found")
            return []
            
        print(f"Found TTPs: {ttps}")
        
        # Read recommendations data
        recommendations_df = pd.read_csv(recommendations_path)
        all_recommendations = []
        
        # Process each TTP
        ttp_recommendations = {}
        for ttp in ttps:
            # Get technique information
            name, description = get_technique_by_id(ttp)
            if not name or not description:
                print(f"Warning: Could not find information for TTP {ttp}, skipping")
                continue
                
            # Build query
            user_query = (
                "Analyze the following attack technique and provide the most relevant and specific recommendation. "
                "The recommendation should:\n"
                "1. Closely match the specific activity described\n"
                "2. Not be generic or obvious ('no duh') advice\n"
                "3. Not mention specific vendor products or detections\n"
                "4. Be actionable and practical\n\n"
                f"Attack Name: {name}\n"
                f"Attack Process: {description}\n"
            )
            
            # Get recommendations
            try:
                output = mapping(user_query, recommendations_df)
                possible_recommendations = get_recommendations_filtered(recommendations_df, output)
                validated_output = validate(user_query, possible_recommendations)
                
                # Parse recommendations
                rec_list = json.loads(validated_output)
                current_ttp_recs = []
                for rec in rec_list.get("output_list", []):
                    rec_title = rec.get("title")
                    if not rec_title:
                        continue
                        
                    rec_id, rec_desc = get_recommendation_by_title(recommendations_df, rec_title)
                    if not rec_id or not rec_desc:
                        continue
                        
                    # Add to recommendations list
                    recommendation = {
                        "ttp_id": ttp,
                        "ttp_name": name,
                        "recommendation_id": rec_id,
                        "title": rec_title,
                        "description": rec_desc,
                        "reason": rec.get("reason", ""),
                        "score": rec.get("score", 0)
                    }
                    # all_recommendations.append(recommendation)
                    current_ttp_recs.append(recommendation)
                current_ttp_recs.sort(key=lambda x: x["score"], reverse=True)
                ttp_recommendations[ttp] = current_ttp_recs[:3]
                all_recommendations.extend(current_ttp_recs[:3])
                    
            except Exception as e:
                print(f"Error processing TTP {ttp}: {str(e)}")
                continue
        
        # Deduplicate recommendations based on recommendation_id
        seen_ids = set()
        unique_recommendations = []
        for rec in all_recommendations:
            if rec["recommendation_id"] not in seen_ids:
                seen_ids.add(rec["recommendation_id"])
                unique_recommendations.append(rec)
        
        return unique_recommendations
        
    except Exception as e:
        print(f"Error processing TTPs: {str(e)}")
        return []

 
def process_rec_dict_ttps(text, techniques_path="recommendations/Techniques.csv", recommendations_path="recommendations/RecDict.csv"):
    try:
        # Extract all TTPs
        ttps = extract_ttps(text)
        if not ttps:
            print("No TTPs found")
            return []
            
        print(f"Found TTPs: {ttps}")
        
        # Read recommendations data
        recommendations_df = pd.read_csv(recommendations_path)
        all_recommendations = []
        
        # Process each TTP
        ttp_recommendations = {}
        for ttp in ttps:
            # Get technique information
            name, description = get_technique_by_id(ttp)
            if not name or not description:
                print(f"Warning: Could not find information for TTP {ttp}, skipping")
                continue
                
            # Build query
            user_query = (
                "Analyze the following attack technique and provide the most relevant and specific recommendation. "
                "The recommendation should:\n"
                "1. Closely match the specific activity described\n"
                "2. Not be generic or obvious ('no duh') advice\n"
                "3. Not mention specific vendor products or detections\n"
                "4. Be actionable and practical\n\n"
                f"Attack Name: {name}\n"
                f"Attack Process: {description}\n"
            )
            
            # Get recommendations
            try:
                output = mapping(user_query, recommendations_df)
                possible_recommendations = get_recommendations_filtered(recommendations_df, output)
                validated_output = validate(user_query, possible_recommendations)
                
                # Parse recommendations
                try:
                    rec_list = json.loads(validated_output)
                    if not isinstance(rec_list, dict) or "output_list" not in rec_list:
                        print(f"Invalid response format for TTP {ttp}")
                        continue
                        
                    current_ttp_recs = []
                    for rec in rec_list["output_list"]:
                        if not isinstance(rec, dict):
                            continue

                        relevance_score = float(rec.get("score", 0))
                        if relevance_score < 90: 
                            continue
                            
                        rec_title = rec.get("title")
                        if not rec_title:
                            continue
                            
                        rec_id, rec_desc = get_recommendation_by_title(recommendations_df, rec_title)
                        if not rec_id or not rec_desc:
                            continue
                            
                        recommendation = {
                            "ttp_id": ttp,
                            "ttp_name": name,
                            "recommendation_id": rec_id,
                            "title": rec_title,
                            "description": rec_desc,
                            "reason": rec.get("reason", ""),
                            "score": float(rec.get("score", 0))  
                        }
                        current_ttp_recs.append(recommendation)
                        
                    if current_ttp_recs:
                        current_ttp_recs.sort(key=lambda x: x["score"], reverse=True)
                        ttp_recommendations[ttp] = current_ttp_recs[0]
                        all_recommendations.append(current_ttp_recs[0])
                        
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON for TTP {ttp}: {str(e)}")
                    continue
                    
            except Exception as e:
                print(f"Error processing TTP {ttp}: {str(e)}")
                continue
        
        # Deduplicate recommendations based on recommendation_id
        seen_ids = set()
        unique_recommendations = []
        for rec in all_recommendations:
            if rec["recommendation_id"] not in seen_ids:
                seen_ids.add(rec["recommendation_id"])
                unique_recommendations.append(rec)
        
        return unique_recommendations
        
    except Exception as e:
        print(f"Error processing TTPs: {str(e)}")
        return []

   

if __name__ == "__main__":
    '''
    data_frame = pd.read_csv("Techniques.csv")
    recommendations_df = pd.read_csv("Recommendations.csv")
    test_id = "T1190"
    name, description = get_technique_by_id(test_id)

    # for index, row in data_frame.iterrows():
    user_query = "Suggest recommendations for mitigating the below attack technique:\n"
    user_query += "Attack Name: " + name + "\n"
    user_query += "Attack Process: " + description + "\n"
    print(user_query)
    output = mapping(user_query, recommendations_df)
    possible_recommendations = get_recommendations_filtered(recommendations_df, output)
    print(f"Output : {output}")
    # print(f"Possible recommendations: {possible_recommendations}")
    output2 = validate(user_query, possible_recommendations)
    print(output2)
    # wo_filter = validate(user_query, str(output))
    # print(wo_filter)
    rec_list = eval(output2)
    output_list = rec_list["output_list"]
    for rec in output_list:
        rec_title = rec["title"]
        # recommendation_title.append(rec_title)
        
        id, desc = get_recommendation_by_title(recommendations_df, rec_title)
        print(f"Recommendation id: {id}, \n Reason: {rec['reason']}, \n Description: {desc}")

'''

    # main()
    text = """
    #### MITRE TTPs 
    ['T1190 - Exploit Public-Facing Application (Confidence Score: 75%)', 
    'T1078 - Valid Accounts (Confidence Score: 50%)', """
    
    #'*T1059.001 - Command and Scripting Interpreter: PowerShell* (https://socprime.com/blog/uac-0001-aka-apt28-attack-detection/)', 
    #'*T1218 - System Binary Proxy Execution* (https://socprime.com/blog/uac-0001-aka-apt28-attack-detection/)', 
    #'*T1572 - Protocol Tunneling* (https://socprime.com/blog/uac-0001-aka-apt28-attack-detection/)']
    
    
    # ttps = extract_ttps(text)

    # print("找到的 TTPs:")
    # for ttp in ttps:
        # print(f"- {ttp}")
    # rec = process_rec_dict_ttps(text)
    # print(rec)
    # for t in rec:
        # print(t['ttp_id'], t['title'])
    titles = pd.read_csv('recommendations/RecDict.csv')
    print(titles['Title'].tolist())