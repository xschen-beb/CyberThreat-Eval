import json
from collections import defaultdict

def load_jsonl(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            article = json.loads(line)
            data[article['guid']] = article
    return data

def calculate_recall_rate(input_values, generated_values):
    covered_numbers = sum(1 for value in generated_values if value in input_values)
    recall_rate = covered_numbers / len(input_values) if input_values else 0
    return covered_numbers, recall_rate


def compare_iocs():
    for guid in articles.keys():
        if guid in enhanced_articles:
            input_iocs = articles[guid].get('indicators', [])
            enhanced_data = enhanced_articles[guid].get('enhanced', {})
            generated_iocs = enhanced_data.get('IoCs') if 'IoCs' in enhanced_data else enhanced_data.get("Detection Signature", {}).get("Internal checks").get('IoCs')
            # if generated_iocs == None:
            #    generated_iocs = enhanced_data.get("Detection Signature", {}).get("Internal checks")
            print(f"Input values: {input_iocs} \n\n Generated values: {generated_iocs}\n===================\n")

            input_values = [ioc['value'] for ioc in input_iocs if isinstance(ioc, dict) and 'value' in ioc]
            generated_values = list(set([ioc['value'] for ioc in generated_iocs if isinstance(ioc, dict) and 'value' in ioc]))
            
            covered_numbers, recall_rate = calculate_recall_rate(input_values, generated_values)
            recall_rates[guid] = recall_rate
            print(f"GUID: {guid}, Covered Numbers: {covered_numbers}, Recall Rate: {recall_rate:.2f}")
        else:
            continue

if __name__ == '__main__': 
    # Load articles from the JSONL files
    articles_file_path = 'articles2024.jsonl'
    enhanced_articles_file_path = 'enhanced_articles2024.jsonl'
    # Load the data
    articles = load_jsonl(articles_file_path)
    enhanced_articles = load_jsonl(enhanced_articles_file_path)
    # Analyzing the similarity based on IoCs
    recall_rates = defaultdict(float)
    
    '''enhanced_data = enhanced_articles["6b85cd09-5584-48bb-869d-5106836b11ac"].get('enhanced', {}).get("Detection Signature", {}).get("Internal checks")
    print(enhanced_data)
    enhanced_iocs = enhanced_data.get('IoCs')
    print(enhanced_iocs)
'''
    compare_iocs()
