import csv
import json
import os
import sys
import argparse

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)

if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)

try:
    from eval.eval_ioc import test as eval_ioc_test
except ImportError:
    from eval_ioc import test as eval_ioc_test


def main():
    parser = argparse.ArgumentParser(
        description="Simple test for IOC evaluation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default paths
  python simple_test.py

  # Specify custom paths
  python simple_test.py --dataset data/IoCs.csv --prediction prediction/my_predictions.json
        """
    )
    
    parser.add_argument(
        '--dataset',
        type=str,
        default=os.path.join(PARENT_DIR, "data", "IoCs.csv"),
        help='Path to ground truth CSV file (default: ioc/data/IoCs.csv)'
    )
    
    parser.add_argument(
        '--prediction',
        type=str,
        default=os.path.join(CURRENT_DIR, "prediction", "manual_ioc_predictions.json"),
        help='Path to prediction JSON file (default: example/prediction/manual_ioc_predictions.json)'
    )
    
    args = parser.parse_args()
    
    dataset_path = args.dataset
    manual_pred_path = args.prediction
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(manual_pred_path), exist_ok=True)

    # Check if dataset file exists
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset file not found: {dataset_path}")
        sys.exit(1)
    
    # grab the second record from IoCs.csv
    second_row = None
    try:
        with open(dataset_path, "r", encoding="utf-8") as src:
            reader = csv.reader(src)
            for idx, row in enumerate(reader):
                if idx == 1:  # second entry
                    second_row = row
                    break
    except Exception as e:
        print(f"Error reading dataset file: {e}")
        sys.exit(1)

    if not second_row:
        raise RuntimeError("Unable to read second row from IoCs.csv")

    source = second_row[0]
    iocs = [val for val in second_row[1:] if val][:5]  # take first five IoCs for simplicity

    sample_preds = []
    for value in iocs[:4]:  # four correct ones
        sample_preds.append({"source": source, "value": value})
    sample_preds.append({"source": source, "value": "totally-wrong-ioc.com"})  # one false positive

    with open(manual_pred_path, "w", encoding="utf-8") as f:
        json.dump(sample_preds, f, ensure_ascii=False, indent=2)

    print("=" * 60)
    print("IOC Evaluation Simple Test (5 IoCs)")
    print("=" * 60)
    print(f"Ground truth file : {dataset_path} (using second entry)")
    print(f"Prediction file   : {manual_pred_path}")

    eval_ioc_test(dataset_path, manual_pred_path)


if __name__ == "__main__":
    main()

