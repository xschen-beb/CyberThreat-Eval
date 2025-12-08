from tqdm import tqdm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import json
import os
import numpy as np
import argparse
import sys  


def gen_article_score_with_llms(data_dict, pred_results, article_type):
    """
    Arg: 
    pred_results input:
    {
        "id": data["id"],
        "score": data["score"], # Ground truth score
        "llm_result": result # prediction result from LLM
    }

    """
    biases = []
    results = []
    y_true = []
    y_pred = []
    bias_dict = {1: [], 2: [], 3: [], 5: []}

    for data, pred_result in tqdm(zip(data_dict, pred_results)):
        print("="*60)
        print(f"Data ID {data['id']}")
        # if data['score'] == 4 or data["priority"] is None:
            # continue
        if article_type == 'article':
            if "Cassandra.SourceText" not in data or not data["Cassandra.SourceText"]:
                continue
            article = data["Cassandra.SourceText"]
        elif article_type == 'description':
            article = data["System.Description"]

        result = pred_result["llm_result"]
        bias = int(abs(result - data["score"]))
        y_true.append(data["score"])
        y_pred.append(result)
        biases.append(bias)
        print(f"==> Ground truth score: {data['score']}")
        print(f"==> Predicted score: {result}")
        print(f"==> Correct: {data['score'] == result}")
        print(f"==> Bias: {bias}")

        if data["score"] in bias_dict:
            bias_dict[data["score"]].append(bias)

    overall_bias = round(np.mean(biases), 4) if biases else 0

    avg_bias_per_class = {}
    for score, biases_list in bias_dict.items():
        if biases_list:
            avg_bias_per_class[score] = round(np.mean(biases_list), 4)
        else:
            avg_bias_per_class[score] = 0

    accuracy = accuracy_score(y_true, y_pred)
    precision_macro = precision_score(y_true, y_pred, average='macro', zero_division=0)
    recall_macro = recall_score(y_true, y_pred, average='macro', zero_division=0)
    f1_macro = f1_score(y_true, y_pred, average='macro', zero_division=0)
    labels_order = [1, 2, 3, 5]
    cm = confusion_matrix(y_true, y_pred, labels=labels_order)
    report = classification_report(y_true, y_pred, labels=labels_order, zero_division=0, digits=3)
    print("\n====== Evaluation Metrics ======")
    # print(f"Overall Accuracy: {accuracy:.4f}")
    # print(f"Overall Bias: {overall_bias:4f}")
    # print(f"Overall Precision (macro): {precision_macro:.4f}")
    # print(f"Overall Recall (macro): {recall_macro:.4f}")
    # print(f"Overall F1 Score (macro): {f1_macro:.4f}")
    print("\nConfusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(report)

    matrix = np.array(cm)

    accept_matrix = matrix[0:3, 0:3]  # submatrix for accept (first 3 rows and first 3 columns)
    # Reject category: 4th row (for score 5)
    reject_matrix = matrix[3]  # 4th row

    # Calculate correctness rates:
    # Accept: True positives = diagonal sum of accept submatrix
    accept_true_positives = np.sum(accept_matrix)
    # Total number of elements in the first 3 rows
    accept_total = np.sum(matrix[0:3, :])
    accept_correct_rate = accept_true_positives / accept_total if accept_total else 0

    # Reject: True positive is the (4,4) element (last element in the 4th row)
    reject_true_positives = reject_matrix[3]
    # Total number of elements in the 4th row
    reject_total = np.sum(reject_matrix)
    reject_correct_rate = reject_true_positives / reject_total if reject_total else 0

    print(f"Accept Category - Correct: {accept_true_positives}, Total: {accept_total}, Correct Rate: {accept_correct_rate:.4f}")
    print(f"Reject Category - Correct: {reject_true_positives}, Total: {reject_total}, Correct Rate: {reject_correct_rate:.4f}")
    TP = np.sum(accept_matrix)
    FN = np.sum(matrix[0:3, :]) - TP
    TN = matrix[3][3]
    FP = sum(reject_matrix) - TN

    precision = TP / (TP + FP) if (TP + FP) else 0
    recall = TP / (TP + FN) if (TP + FN) else 0
    accuracy = (TP + FN) / (TP + FP + FN + TN) if (TP + FP + FN + TN) else 0

    print("\n====== Task 1 of Stage 1 Triage: Accepted Articles Metrics ======")
    print(f"Accept Category - Precision: {precision:.4f}, Recall: {recall:.4f}")
    print(f"Accept Category - Accuracy: {accuracy:.4f}")


    print("\n====== Task 2 of Stage 1 Triage: Ground Truth Accept Group Metrics ======")
    accept_matrix_total = matrix[0:3, :]
    acc = np.trace(accept_matrix_total)
    denom_accept = np.sum(accept_matrix_total)
    accuracy_accept = acc / denom_accept if denom_accept else 0
    print(f"Overall Pass rate (Accept Group): {accuracy_accept:.4f}")

    total_bias = 0  # Total bias sum
    total_count = 0  # Total number of elements considered for bias calculation


    for true_index, true_val in enumerate([1, 2, 3]):  # Ground truth values (1, 2, 3)
        for pred_index, pred_val in enumerate([1, 2, 3, 5]):  # Predicted values (1, 2, 3, 5)
            # Calculate bias: absolute difference between ground truth and prediction
            bias = abs(true_val - pred_val)
            # Count is the number of occurrences in the matrix (matrix element at [true_index, pred_index])
            count = accept_matrix_total[true_index, pred_index]
            
            # Update total bias and total count
            total_bias += bias * count
            total_count += count

    # Calculate Average Bias for Accept Group
    avg_bias_accept = total_bias / total_count if total_count != 0 else 0  # Avoid division by zero
    print(f"Average Bias (Accept Group):     {avg_bias_accept:.4f}")

    combined_metrics = {
        "overall_accuracy": float(accuracy),
        "overall_bias": float(overall_bias),
        "precision_macro": float(precision_macro),
        "recall_macro": float(recall_macro),
        "f1_macro": float(f1_macro),
        #"confusion_matrix": cm.tolist(),
        "classification_report": report,
        "avg_bias_per_class": {k: float(v) for k, v in avg_bias_per_class.items()},
        "binary": {
            "accept_correct": float(accept_correct_rate),
            "reject_correct": float(reject_correct_rate),
            "accept_accuracy": float(accuracy_accept),
            "accept_avg_bias": float(avg_bias_accept)
        }
    }
    return results, combined_metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evaluate priority assignment predictions against ground truth",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage with default paths
  python eval.py --ground_truth data/0314-articles.json --predictions predictions.json

  # Use description instead of full article
  python eval.py --ground_truth data/0314-articles.json --predictions predictions.json --article_type description

  # Save results to file
  python eval.py --ground_truth data/0314-articles.json --predictions predictions.json --output results.json
        """
    )
    
    parser.add_argument(
        '--ground_truth',
        type=str,
        default=os.path.join("data", "0314-articles.json"),
        help='Path to ground truth JSON file containing articles (default: data/0314-articles.json)'
    )
    
    parser.add_argument(
        '--predictions',
        type=str,
        required=True,
        help='Path to predictions JSON file (format: list of dicts with "id", "score", "llm_result")'
    )
    
    parser.add_argument(
        '--article_type',
        type=str,
        choices=['article', 'description'],
        default='article',
        help='Type of article content to use: "article" for full text (Cassandra.SourceText) or "description" for summary (System.Description) (default: article)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Path to save evaluation results as JSON (optional, if not provided results are printed to stdout)'
    )
    
    args = parser.parse_args()
    
    # Check if files exist
    if not os.path.exists(args.ground_truth):
        print(f"Error: Ground truth file not found: {args.ground_truth}")
        sys.exit(1)
    
    if not os.path.exists(args.predictions):
        print(f"Error: Predictions file not found: {args.predictions}")
        sys.exit(1)
    
    # Load ground truth data
    try:
        with open(args.ground_truth, "r", encoding="utf-8") as f:
            data_dict = json.load(f)
    except Exception as e:
        print(f"Error loading ground truth file: {e}")
        sys.exit(1)
    
    # Load predictions
    try:
        with open(args.predictions, "r", encoding="utf-8") as f:
            pred_results = json.load(f)
    except Exception as e:
        print(f"Error loading predictions file: {e}")
        sys.exit(1)
    
    # Validate predictions format
    if not isinstance(pred_results, list):
        print("Error: Predictions must be a JSON array")
        sys.exit(1)
    
    for pred in pred_results:
        if not all(key in pred for key in ['id', 'score', 'llm_result']):
            print("Error: Each prediction must have 'id', 'score', and 'llm_result' fields")
            sys.exit(1)
    
    # Run evaluation
    try:
        results, combined_metrics = gen_article_score_with_llms(
            data_dict, 
            pred_results, 
            args.article_type
        )
        
        # Save or print results
        if args.output:
            output_data = {
                "results": results,
                "metrics": combined_metrics
            }
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(output_data, f, ensure_ascii=False, indent=2)
            print(f"\nResults saved to: {args.output}")
        else:
            print("\n" + "="*60)
            print("Evaluation Results:")
            print("="*60)
            print(json.dumps(combined_metrics, indent=2, ensure_ascii=False))
            
    except Exception as e:
        print(f"Error during evaluation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
