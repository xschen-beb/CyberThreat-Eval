"""
Threat Actor Evaluation Script

This script evaluates the quality of threat actor context extraction and analysis.
It uses the generic evaluation runner to process articles and generate evaluation scores.
"""
import json
import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)

for path in [CURRENT_DIR, PARENT_DIR]:
    if path not in sys.path:
        sys.path.append(path)

import argparse


from utils import api_call
from evaluation_runner import run_evaluation


def evaluate_actor_context(client, model, original_article, generated_context):
    sys_prompt = """
    ### Task Description:
    You are an expert evaluator in cybersecurity research with a strong background in threat intelligence and OSINT analysis. Based on recent literature and best practices, your task is to assess the quality of a generated context provided for a specific threat actor by comparing it against an original article containing verified details.

    ### Input:
    - Generated Context: An automatically generated summary or analysis about the threat actor.
    - Original Article: The source article containing verified information on the threat actor.

    ### Evaluation Criteria and Metrics:

    1. Relevance: Measures how closely the generated context aligns with the key details of the original article (e.g., aliases, motivations, tactics).
    - 1: Unrelated or fails to mention key aspects.
    - 2: Limited relevance; misses critical details.
    - 3: Moderately relevant; covers some aspects but lacks depth.
    - 4: Mostly relevant; minor omissions or inaccuracies.
    - 5: Highly relevant; fully aligns with the original article.

    2. Accuracy: Assesses the factual correctness of the generated context compared to the original article.
    - 1: Factually incorrect or inconsistent.
    - 2: Contains significant inaccuracies.
    - 3: Moderately accurate; minor inconsistencies.
    - 4: Mostly accurate; very few errors.
    - 5: Completely accurate; perfectly reflects the original article.

    3. Comprehensiveness: Evaluates the extent to which the generated context covers all critical details from the original article.
    - 1: Highly incomplete; critical details missing.
    - 2: Covers only minimal details; significant gaps.
    - 3: Moderately comprehensive; some key details missing.
    - 4: Comprehensive; minor omissions.
    - 5: Fully comprehensive; captures all essential details.

    4. Clarity: Measures how clear and understandable the generated context is.
    - 1: Poorly written, unclear, and difficult to understand.
    - 2: Significant clarity issues; partially understandable.
    - 3: Moderately clear; some ambiguities.
    - 4: Mostly clear; minor issues.
    - 5: Perfectly clear; highly readable and easily understandable.

    5. Coherence: Assesses the logical structure and flow of the generated context.
    - 1: Disorganized and difficult to follow.
    - 2: Significant coherence issues; scattered information.
    - 3: Moderately coherent; inconsistent flow.
    - 4: Mostly coherent; well-organized with minor issues.
    - 5: Fully coherent; logically structured and easy to follow.

    6. Attribution: Evaluates whether the generated context properly attributes information to the original article.
    - 1: Information is unverified or unattributed.
    - 2: Major attribution issues; many details are not clearly linked.
    - 3: Moderately attributable; some details lack clear source references.
    - 4: Mostly attributable; minor gaps in linking information.
    - 5: Fully attributable; all details are clearly linked to the original article.

    ### Evaluation Instructions:
    For each criterion, assign a score between 1 and 5 based on the metrics provided. Then output the evaluation scores strictly in the following JSON format without any additional text, prefixes, or comments:

    {"Relevance": <score>, "Accuracy": <score>, "Comprehensiveness": <score>, "Clarity": <score>, "Coherence": <score>, "Attribution": <score>}
    """

    user_prompt = f"""
    ### Task Description:
    Evaluate the quality of the generated context for the given threat actor by comparing it against the original article.

    Generated Context:
    {generated_context}

    Original Article:
    {original_article}
    """

    # Prepare messages for API call
    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    # Call the API to perform the evaluation
    response_message = api_call(client, new_messages, model_name=model, json_enabled=True)
    response = response_message.choices[0].message.content

    try:
        evaluation_scores = json.loads(response)
    except json.JSONDecodeError as e:
        print(f"Error parsing evaluation response: {e}")
        evaluation_scores = {"error": "Unable to parse scores"}

    return evaluation_scores


def main():
    """
    Main function to run threat actor evaluation.
    """
    parser = argparse.ArgumentParser(description="Evaluate threat actor extraction quality")
    parser.add_argument(
        "--model", 
        type=str, 
        required=True, 
        help="Model name to run (e.g., gpt-4o, o3-mini, etc.)"
    )
    parser.add_argument(
        "--input",
        type=str,
        default='score_evaluation/data/0330-articles-with-rejected-score.json',
        help="Path to input JSON file (default: score_evaluation/data/0330-articles-with-rejected-score.json)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default='score_evaluation/description',
        help="Output directory for results (default: score_evaluation/description)"
    )
    parser.add_argument(
        "--context-field",
        type=str,
        default='baseline_threat_actor_context',
        help="Field name containing generated context (default: baseline_threat_actor_context)"
    )
    parser.add_argument(
        "--use-azure",
        action="store_true",
        default=True,
        help="Use Azure OpenAI (default: True)"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="OpenAI API key (used when not using Azure)"
    )
    parser.add_argument(
        "--api-base",
        type=str,
        default=None,
        help="OpenAI API base URL (used when not using Azure)"
    )

    args = parser.parse_args()
    
    # Run evaluation using the generic runner
    run_evaluation(
        model_name=args.model,
        input_json=args.input,
        output_dir=args.output_dir,
        evaluate_function=evaluate_actor_context,
        content_field="System.Description",
        context_field_name=args.context_field,
        evaluation_field_name="baseline_evaluation",
        average_field_name="baseline_average",
        use_azure=args.use_azure,
        api_key=args.api_key,
        api_base=args.api_base
    )


if __name__ == '__main__':
    main()

