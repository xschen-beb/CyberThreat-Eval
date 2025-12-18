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

from eval.evaluation_runner import run_evaluation
from eval.threat_actor import evaluate_actor_context


def main():
    parser = argparse.ArgumentParser(
        description="Run evaluation on threat actor context generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default settings
  python simple_test.py

  # Specify custom input and output
  python simple_test.py --input data/articles.json --output results/

  # Use Azure OpenAI
  python simple_test.py --use-azure --model gpt-4o
        """
    )
    
    parser.add_argument(
        '--input',
        type=str,
        default='data/0330-articles-with-rejected-score.json',
        help='Path to input JSON file containing articles (default: data/0330-articles-with-rejected-score.json)'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='example/test_output',
        help='Directory to save output files (default: example/test_output)'
    )
    
    parser.add_argument(
        '--temp-input',
        type=str,
        default='example/test_input.json',
        help='Temporary input file path for processed articles (default: example/test_input.json)'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default='gpt-4o',
        help='Model name to use for evaluation (default: gpt-4o)'
    )
    
    parser.add_argument(
        '--use-azure',
        action='store_true',
        help='Use Azure OpenAI (default: False, uses OpenAI API)'
    )
    
    parser.add_argument(
        '--api-key',
        type=str,
        default=None,
        help='API key for OpenAI (required when --use-azure is False)'
    )
    
    parser.add_argument(
        '--api-base',
        type=str,
        default=None,
        help='API base URL for OpenAI (optional, used when --use-azure is False)'
    )
    
    parser.add_argument(
        '--num-articles',
        type=int,
        default=3,
        help='Number of articles to process (default: 3)'
    )
    
    args = parser.parse_args()
    
    # Set default API credentials if not using Azure and not provided
    if not args.use_azure:
        if args.api_key is None:
            args.api_key = os.getenv("OPENAI_API_KEY")
            if args.api_key is None:
                print("Warning: No API key provided. Set OPENAI_API_KEY environment variable or use --api-key")
        if args.api_base is None:
            args.api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    
    # Load and process articles
    print(f"Loading articles from: {args.input}")
    try:
        with open(args.input, "r", encoding="utf-8") as f:
            articles = json.load(f)[:args.num_articles]
        print(f"Loaded {len(articles)} articles")
    except FileNotFoundError:
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading articles: {e}")
        sys.exit(1)
    
    # Generate simulated context for each article
    for idx, article in enumerate(articles, start=1):
        desc = article.get("System.Description", "")
        article["System.Description"] = desc
        article["generated_context"] = (
            f"Simulated threat actor summary #{idx}. "
            f"Key points: {desc[:150]}..."
        )
    
    # Save processed articles to temp file
    os.makedirs(os.path.dirname(args.temp_input), exist_ok=True)
    with open(args.temp_input, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    print(f"Saved processed articles to: {args.temp_input}")
    
    # Run evaluation
    print(f"\nRunning evaluation with model: {args.model}")
    print(f"Output directory: {args.output_dir}")
    print(f"Using Azure: {args.use_azure}")
    
    try:
        run_evaluation(
            model_name=args.model,
            input_json=args.temp_input,
            output_dir=args.output_dir,
            evaluate_function=evaluate_actor_context,
            content_field="System.Description",
            context_field_name="generated_context",
            evaluation_field_name="evaluation",
            average_field_name="average_score",
            use_azure=args.use_azure,
            api_key=args.api_key,
            api_base=args.api_base
        )
        
        output_file = os.path.join(args.output_dir, f"{args.model}.json")
        print(f"\nEvaluation complete. Output file: {output_file}")
        
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"Warning: Output file not found: {output_file}")
            
    except Exception as e:
        print(f"Error during evaluation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

