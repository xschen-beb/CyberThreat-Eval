import pandas as pd
import csv
import json

def test(ground_truth_file, pred_file):
    df = pd.read_csv(ground_truth_file, header=None)
    gt_dict = {}
    for idx, row in df.iterrows():
        source = row[0]
        ioc_items = row.iloc[1:].dropna().tolist()
        cleaned_items = [
            item.replace("[", "").replace("]", "").replace("hxxp", "http").replace("hxxps", "https").replace("[.]", "[]").split(" - ")[0].strip() for item in ioc_items
        ]
        gt_dict[source] = {item.lower() for item in cleaned_items}
    
    # print("Ground Truth by Source:")
    # for src, items in gt_dict.items():
        # print(f"Source: {src}, Items: {items}")
    
    pred_dict = {}
    with open(pred_file, mode='r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            for ioc_data in data:
                value = ioc_data['value']
                source = ioc_data['source']
                cleaned_value = value.replace("[", "") \
                                     .replace("]", "") \
                                     .replace("hxxp", "http") \
                                     .replace("hxxps", "https") \
                                     .replace("[.]", "[]").split(" - ")[0].strip()
                if source not in pred_dict:
                    pred_dict[source] = []
                pred_dict[source].append(cleaned_value)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
    
    # print("\nPredictions by Source:")
    # for src, values in pred_dict.items():
        # print(f"Source: {src}, Values: {values}")
    
    total_true_positives = 0
    total_false_positives = 0
    total_false_negatives = 0
    
    all_sources = set(list(pred_dict.keys()) + list(gt_dict.keys()))
    
    for src in all_sources:
        gt_set = gt_dict.get(src, set())
        pred_list = pred_dict.get(src, [])
        
        # For prediction, if pred.lower() in ground truth
        true_positives = sum(
            any(pred.lower() in gt.lower() for gt in gt_set)
            for pred in pred_list
        )

        false_positives = len(pred_list) - true_positives

        # If for prediction, no pred.lower() in ground truth
        false_negatives = sum(
            not any(pred.lower() in gt.lower() for pred in pred_list)
            for gt in gt_set
        )
        ####################
        # For prediction, if pred.lower() in ground truth or ground truth in pred
        """
        true_positives = sum(
            any((pred.lower() in gt.lower()) or (gt.lower() in pred.lower()) for gt in gt_set)
            for pred in pred_list
        )
        false_positives = len(pred_list) - true_positives
        false_negatives = sum(
            not any((pred.lower() in gt.lower()) or (gt.lower() in pred.lower()) for pred in pred_list)
            for gt in gt_set
        )
        """
        ####################
        # Exact match
        """
        true_positives = sum(
            any(pred.lower() == gt.lower() for gt in gt_set)
            for pred in pred_list
        )
        false_positives = len(pred_list) - true_positives
        false_negatives = sum(
            not any(pred.lower() == gt.lower() for pred in pred_list)
            for gt in gt_set
        )
        """


                
        # print(f"\nSource: {src}")
        # print(f"  True Positives: {true_positives}")
        # print(f"  False Positives: {false_positives}")
        # print(f"  False Negatives: {false_negatives}")
        
        total_true_positives += true_positives
        total_false_positives += false_positives
        total_false_negatives += false_negatives
    
    if total_true_positives + total_false_positives > 0:
        precision = total_true_positives / (total_true_positives + total_false_positives)
    else:
        precision = 0.0

    if total_true_positives + total_false_negatives > 0:
        recall = total_true_positives / (total_true_positives + total_false_negatives)
    else:
        recall = 0.0

    print(f"\nOverall Metrics for {pred}:")
    print(f"Overall Precision: {precision:.4f}")
    print(f"Overall Recall: {recall:.4f}")

if __name__ == '__main__':
    file = 'IoCs.csv'
    # pred = 'o3-mini_unique_iocs.json'
    preds = ['gpt-4o_iocs_output.json', 'gpt-4o_iocs_output_step2.json', 'o3-mini_iocs_output.json', 'o3-mini_iocs_output_step2.json']
    # pred = 'o3-mini_iocs_output_step2.json'
    for pred in preds:
        test(file, pred)