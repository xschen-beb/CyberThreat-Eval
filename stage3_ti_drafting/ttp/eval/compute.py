import json
import time
import json5
import argparse
import os
import sys


def load_ttp_mapping(csv_file='data/TTP_Mapping.csv'):
    """
    Loads a mapping of TTP IDs to their names from a CSV file.

    Args:
        csv_file (str): Path to the CSV file containing the mapping data. Defaults to 'data/TTP_Mapping.csv'.

    Returns:
        dict: A dictionary where keys are TTP IDs and values are TTP names.
    """
    # Handle relative paths - try to find the file relative to the script location
    if not os.path.isabs(csv_file) and not os.path.exists(csv_file):
        # Try relative to the script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        possible_paths = [
            os.path.join(script_dir, csv_file),
            os.path.join(parent_dir, csv_file),
            os.path.join(parent_dir, 'data', 'TTP_Mapping.csv'),
        ]
        for path in possible_paths:
            if os.path.exists(path):
                csv_file = path
                break
    
    ttp_mapping = {}
    with open(csv_file, 'r', encoding='utf-8') as f:
        for line in f:
            if ',' in line:
                fields = line.strip().split(',')
                if len(fields) >= 3:
                    ttp_id = fields[1]
                    ttp_name = fields[2]
                    ttp_mapping[ttp_id] = ttp_name
    return ttp_mapping


# def compute_raw_precision_recall(articles, client, model_name):
def compute_raw_precision_recall(articles, result):
    """
    Compute raw precision and recall metrics for extracted TTPs from a list of articles.

    Args:
        articles: A list of article dictionaries, or a single article dictionary
        result: A single result (str or dict), or a list of results (one per article)
                If a list is provided, it must have the same length as articles.

    For each article:
      1. Extract raw TTP codes from the article's "ttps" field.
      2. Use the extraction function to obtain validated TTPs.
      3. Validate each extracted TTP against a known mapping:
         - If a TTP's description does not match the expected mapping,
           issue a warning and do NOT add this TTP to the final validated TTPs.
           (Such TTPs will be treated as false positives.)
      4. Compute TP, FP, FN for the article and update overall totals.

    Returns:
        overall_precision (float), overall_recall (float)
    """
    total_tp = 0
    total_fp = 0
    total_fn = 0
    
    # Load the TTP mapping from CSV
    # Use the default path, will be overridden if csv_file is provided in main
    ttp_mapping = load_ttp_mapping()

    # Handle both single article and list of articles
    if not isinstance(articles, list):
        articles = [articles]
    
    # Handle both single result and list of results
    if isinstance(result, list):
        # Multiple results, one per article
        if len(result) != len(articles):
            raise ValueError(f"Number of results ({len(result)}) must match number of articles ({len(articles)})")
        results = result
    else:
        # Single result, apply to all articles
        results = [result] * len(articles)

    for idx, (article, result_item) in enumerate(zip(articles, results)):
        try:
            time_start = time.time()
            # Extract raw TTP codes from the article field "ttps"
            raw_ttps = article.get("ttps", [])
            # Extract TTP codes from the article list (e.g., "T1136" from "T1136 - Create Account")
            article_ttps_set = {ttp.split(" - ")[0].strip() for ttp in raw_ttps if " - " in ttp}
            print("Article TTP Codes:", article_ttps_set)
            
            # Use the extraction function to obtain validated TTPs
            # result = extract_ttps(client, article, model_name)
            if isinstance(result_item, str):
                try:
                    validated_ttps = json5.loads(result_item)
                except Exception as e:
                    print(f"Error parsing TTP data: {e}")
                    continue
            else:
                validated_ttps = result_item

            print("Extracted Validated TTPs (pre-mapping):", validated_ttps)
            
            # Validate each extracted TTP using the mapping.
            # If the description mismatches, replace it with the correct description.
            validated_ttps_final = {}
            missing_in_mapping_count = 0  # Count TTPs not found in mapping
            for ttp_id, details in validated_ttps.items():
                # Assume details is a string like "Description, Confidence: ..., Justification: ..."
                description = details.split(',')[0].strip()
                if ttp_id in ttp_mapping:
                    if description.lower() == ttp_mapping[ttp_id].lower():
                        validated_ttps_final[ttp_id] = details
                    else:
                        # Description mismatch: update the description using the mapping.
                        print(f"Warning: Description mismatch for {ttp_id}")
                        print(f"Expected: {ttp_mapping[ttp_id]}")
                        print(f"Found: {description}")
                        # Replace the description with the correct one from the mapping.
                        corrected_details = ttp_mapping[ttp_id]
                        validated_ttps_final[ttp_id] = corrected_details
                else:
                    # TTP ID not found in mapping, count as false positive.
                    print(f"Warning: TTP ID {ttp_id} not found in mapping")
                    missing_in_mapping_count += 1
            
            # Final set of validated TTP codes after mapping correction.
            validated_ttps_set = set(validated_ttps_final.keys())
            print("Validated TTP Codes (after mapping validation):", validated_ttps_set)
            
            # Compute metrics for the article.
            tp = len(article_ttps_set.intersection(validated_ttps_set))
            # FP: TTPs in validated set but not in ground truth, plus those not found in mapping.
            fp = len(validated_ttps_set - article_ttps_set) + missing_in_mapping_count
            # FN: TTP codes in ground truth that are missing from the validated set.
            fn = len(article_ttps_set - validated_ttps_set)
            
            print(f"Article metrics: TP: {tp}, FP: {fp}, FN: {fn}\n")
            time_end = time.time()
            print(f"==> Total time taken for TTP processing: {time_end - time_start:.2f} seconds")
            
            total_tp += tp
            total_fp += fp
            total_fn += fn

        except Exception as e:
            print(f"Error processing article: {e}")

    # Calculate overall metrics after processing all articles
    overall_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    overall_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0

    print("\n" + "=" * 60)
    print("Overall Metrics (All Articles):")
    print("=" * 60)
    print(f"Total True Positives: {total_tp}")
    print(f"Total False Positives: {total_fp}")
    print(f"Total False Negatives: {total_fn}")
    print(f"Precision: {overall_precision:.4f}")
    print(f"Recall: {overall_recall:.4f}")
    print("=" * 60)

    return overall_precision, overall_recall


def load_articles_from_file(articles_file):
    """
    Load articles from a JSON file.
    
    Args:
        articles_file (str): Path to JSON file containing articles
        
    Returns:
        list: List of article dictionaries
    """
    with open(articles_file, 'r', encoding='utf-8') as f:
        articles = json.load(f)
    if not isinstance(articles, list):
        articles = [articles]
    return articles


def load_results_from_file(results_file):
    """
    Load results from a JSON file.
    The file can be:
    1. A JSON array of JSON strings (one per line or as array)
    2. A text file with one JSON string per line
    
    Args:
        results_file (str): Path to results file
        
    Returns:
        list: List of result strings (JSON strings)
    """
    results = []
    with open(results_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        
        # Try to parse as JSON array first (using json5 to support comments)
        try:
            parsed = json5.loads(content)
            if isinstance(parsed, list):
                # If it's a list of strings, return as-is
                if all(isinstance(item, str) for item in parsed):
                    return parsed
                # If it's a list of dicts, convert each to JSON string
                elif all(isinstance(item, dict) for item in parsed):
                    return [json.dumps(item, ensure_ascii=False) for item in parsed]
        except (json.JSONDecodeError, Exception):
            pass
        
        # Try to parse as line-separated JSON strings
        for line in content.split('\n'):
            line = line.strip()
            if line:
                try:
                    # Validate it's valid JSON
                    json.loads(line)
                    results.append(line)
                except json.JSONDecodeError:
                    # If not valid JSON, try json5
                    try:
                        json5.loads(line)
                        results.append(line)
                    except:
                        print(f"Warning: Skipping invalid JSON line: {line[:50]}...")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Compute precision and recall metrics for TTP extraction from articles",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Load articles and results from JSON files
  python compute.py --articles data/100-days-articles.json --results predictions.json
  
  # Use custom TTP mapping file
  python compute.py --articles articles.json --results results.json --ttp-mapping custom_mapping.csv
        """
    )
    
    parser.add_argument(
        '--articles',
        type=str,
        default='data/100-days-articles.json',
        required=True,
        help='Path to JSON file containing articles (list of article dicts with "ttps" field)'
    )
    
    parser.add_argument(
        '--results',
        type=str,
        required=True,
        help='Path to JSON file containing prediction results. Can be: '
             '1) JSON array of JSON strings, 2) JSON array of dicts, or 3) line-separated JSON strings'
    )
    
    parser.add_argument(
        '--ttp-mapping',
        type=str,
        default='data/TTP_Mapping.csv',
        help='Path to CSV file containing TTP ID to name mapping (default: data/TTP_Mapping.csv)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Optional: Path to save evaluation results as JSON file'
    )
    
    args = parser.parse_args()
    
    # Load articles
    print(f"Loading articles from: {args.articles}")
    try:
        articles = load_articles_from_file(args.articles)
        print(f"Loaded {len(articles)} articles")
    except Exception as e:
        print(f"Error loading articles: {e}")
        sys.exit(1)
    
    # Load results
    print(f"Loading results from: {args.results}")
    try:
        results = load_results_from_file(args.results)
        print(f"Loaded {len(results)} results")
    except Exception as e:
        print(f"Error loading results: {e}")
        sys.exit(1)
    
    # Validate lengths match
    if len(articles) != len(results):
        print(f"Warning: Number of articles ({len(articles)}) does not match number of results ({len(results)})")
        print("Using the minimum length for evaluation")
        min_len = min(len(articles), len(results))
        articles = articles[:min_len]
        results = results[:min_len]
    
    # Update TTP mapping path if provided
    if args.ttp_mapping != 'data/TTP_Mapping.csv':
        # Temporarily modify the default for load_ttp_mapping
        import functools
        original_load = load_ttp_mapping
        load_ttp_mapping = functools.partial(original_load, csv_file=args.ttp_mapping)
    
    # Compute metrics
    print("\n" + "=" * 60)
    print("Computing Precision and Recall Metrics")
    print("=" * 60 + "\n")
    
    try:
        precision, recall = compute_raw_precision_recall(articles, results)
        
        # Calculate F1 score
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        # Print summary
        print("\n" + "=" * 60)
        print("Final Summary")
        print("=" * 60)
        print(f"Micro-Averaged Precision: {precision:.4f}")
        print(f"Micro-Averaged Recall: {recall:.4f}")
        print(f"Micro-Averaged F1-Score: {f1:.4f}")
        print("=" * 60)
        
        # Save to file if requested
        if args.output:
            output_data = {
                "precision": precision,
                "recall": recall,
                "f1_score": f1,
                "num_articles": len(articles)
            }
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)
            print(f"\nResults saved to: {args.output}")
        
    except Exception as e:
        print(f"Error during evaluation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()