import json
import os
import sys
from tqdm import tqdm


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)
from utils import (
    calculate_average_score,
    calculate_average_score_for_criteria,
    get_client
)


# Evaluation criteria list (shared across all evaluation types)
EVALUATION_CRITERIA = ["Relevance", "Accuracy", "Comprehensiveness", "Clarity", "Coherence", "Attribution"]


def run_evaluation(
    model_name: str,
    input_json: str,
    output_dir: str,
    evaluate_function,
    content_field: str = "System.Description",
    context_field_name: str = "generated_context",
    evaluation_field_name: str = "evaluation",
    average_field_name: str = "average_score",
    use_azure: bool = True,
    api_key: str = None,
    api_base: str = None
):
    """
    Run evaluation on a dataset of articles.
    
    This function processes articles from an input JSON file, extracts context using
    the provided extraction function, evaluates it using the evaluation function,
    and writes results to an output file.
    
    Args:
        model_name: Name of the model to use for extraction
        input_json: Path to input JSON file containing articles
        output_dir: Directory to save output files
        evaluate_function: Function to evaluate generated context
                          Signature: (eval_client, model_name, original_article, generated_context) -> evaluation_dict
        content_field: Field name in input data containing article content (default: "System.Description")
        context_field_name: Field name containing the generated context to evaluate (default: "generated_context")
        evaluation_field_name: Name for the evaluation scores field in output (default: "evaluation")
        average_field_name: Name for the average score field in output (default: "average_score")
        use_azure: Whether to use Azure OpenAI for evaluation (default: True)
        api_key: API key for OpenAI (used when use_azure=False)
        api_base: API base URL for OpenAI (used when use_azure=False)
    
    Returns:
        Dictionary containing overall average scores
    """
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    output_json = os.path.join(output_dir, f"{model_name}.json")
    
    # Setup evaluation client
    eval_client = get_client(
        model_name=model_name,
        use_azure=use_azure,
        api_key=api_key,
        api_base=api_base
    )
    
    # Load input data
    with open(input_json, 'r', encoding='utf-8') as fi:
        input_data = json.load(fi)
    
    # Initialize score tracking
    total_scores = {criterion: [] for criterion in EVALUATION_CRITERIA}
    num_entries = len(input_data)
    
    # Process each article
    with open(output_json, 'w', encoding='utf-8') as fo:
        for data in tqdm(input_data, desc="Evaluating articles"):
            article_content = data.get(content_field, "")
            
            generated_context = data.get(context_field_name)
            if generated_context is None:
                raise ValueError(f"Missing '{context_field_name}' in input data for id={data.get('id')}")
            
            # Evaluate the generated context
            evaluation = evaluate_function(eval_client, model_name, article_content, generated_context)
            average_score = calculate_average_score(evaluation)
            
            # Track scores for overall average calculation
            for criterion in EVALUATION_CRITERIA:
                if criterion in evaluation:
                    total_scores[criterion].append(evaluation[criterion])
            
            # Prepare output data
            output_data = {
                "id": data.get('id', ''),
                "url": data.get('url', ''),
                "description": article_content,
                context_field_name: generated_context,
                evaluation_field_name: evaluation,
                average_field_name: average_score,
            }
            
            # Write output
            json.dump(output_data, fo, ensure_ascii=False)
            fo.write('\n')
        
        # Calculate and write overall averages
        overall_average = calculate_average_score_for_criteria(total_scores, num_entries)
        overall_averages = {
            "overall_baseline_average": overall_average,
        }
        json.dump(overall_averages, fo, ensure_ascii=False)
        fo.write('\n')
    
    return overall_average

