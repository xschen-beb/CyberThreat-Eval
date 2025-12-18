"""
Root Cause Evaluation Script

This script evaluates the quality of root cause context extraction and analysis.
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



def evaluate_root_cause_context(client, model, original_article, generated_context):
    """
    Evaluate the quality of generated root cause context.
    
    Args:
        client: AzureOpenAI client instance
        model: Model name to use for evaluation
        original_article: Original article content
        generated_context: Generated root cause context to evaluate
    
    Returns:
        Dictionary with evaluation scores for each criterion
    """
    sys_prompt = """
    ### Task description:
    You are an expert evaluator in cybersecurity. I will provide you with the name of a malware/tool and the corresponding LLM-generated context.
    Your task is to assess the quality of the LLM-generated context based on the following criteria and scoring metrics, ensuring that you consider how well the malware contributes to the root cause of an incident is explained in the context and its relationship to the overall cybersecurity landscape.


    ### Evaluation Criteria and Metrics:

    1. Relevance:
        - 1: Unrelated to the root cause of the incident or fails to mention key aspects of the malware's role (e.g., attack vector, exploitation method, malware behavior).
        - 2: Limited relevance; partial or tangentially related information but misses key aspects of the malware or incident context.
        - 3: Moderately relevant; covers some important aspects but lacks depth or misses critical connections between the malware and the incident context.
        - 4: Mostly relevant; covers most key aspects with minor omissions or inaccuracies in the relationship between malware and incident context.
        - 5: Highly relevant; fully aligns with the incident's root cause, addressing all key aspects of the malware's role and its relationship with the incident's context comprehensively.

    2. Accuracy:
        - 1: Factually incorrect or inconsistent with known details about the malware and the incident's root cause.
        - 2: Significant inaccuracies or contradictions, though some elements are correct.
        - 3: Moderately accurate; factual but contains minor inconsistencies or errors about how the malware contributes to the incident.
        - 4: Mostly accurate; aligns well with known information about the malware and the incident with very few errors.
        - 5: Completely accurate; perfectly reflects known factual content about the malware's role in the incident's root cause.

    3. Comprehensiveness:
        - 1: Highly incomplete; fails to cover critical details about the malware's role or the broader context of the incident.
        - 2: Covers only minimal details; significant gaps remain in explaining how the malware is related to the incident.
        - 3: Moderately comprehensive; includes some critical details but misses others, such as the attack methodology or the specific impact of the malware.
        - 4: Comprehensive; covers most critical details with minor omissions, explaining how the malware's characteristics contributed to the incident.
        - 5: Fully comprehensive; captures all essential details about the malware, its functionality, and how it relates to the overall context of the incident.

    4. Clarity:
        - 1: Poorly written, unclear, and difficult to understand, with significant ambiguity around the role of the malware in the incident.
        - 2: Significant clarity issues; partially understandable but requires effort to interpret the relationship between the malware and the incident.
        - 3: Moderately clear; generally understandable but with some ambiguities regarding how the malware influenced the incident's outcome.
        - 4: Mostly clear; easy to understand the connection between the malware and the incident with minor ambiguities.
        - 5: Fully clear; well-organized and easy to understand, with a clear and logical explanation of the malware's role in the incident.

    5. Coherence:
        - 1: Explanation lacks logical flow, with no clear connection between the malware and the incident root cause.
        - 2: Some coherence, but there are significant logical gaps or unclear relationships between malware and incident root cause.
        - 3: Generally coherent, though some links between malware and incident root cause may be weak or unclear.
        - 4: Mostly coherent; strong logical connection between malware and incident root cause with only minor gaps.
        - 5: Fully coherent; logical and clear connection throughout, detailing how the malware directly led to the incident's root cause.

    6. Attribution:
        - 1: Attribution is completely incorrect; no connection between the malware and the actual threat actor or root cause.
        - 2: Significant attribution errors; the threat actor is misidentified, or motives are unclear.
        - 3: Basic attribution is correct, but there are minor inaccuracies or omissions regarding the threat actor's identity or objectives.
        - 4: Mostly correct attribution; the threat actor and motives are clearly identified, with only minor inaccuracies.
        - 5: Perfect attribution; accurately identifies the threat actor, their objectives, and the precise relationship to the incident's root cause.

    ### Evaluation Instructions:
    For each criterion, assign a score between 1 and 5 based on the metrics provided above. Then output the evaluation scores strictly in the JSON format below without any prefixes or explanations:
    {"Relevance": <score>, "Accuracy": <score>, "Comprehensiveness": <score>, "Clarity": <score>, "Coherence": <score>, "Attribution": <score>}

    Do not include any additional text or comments outside the JSON object.
    """

    user_prompt = f"""
    ### Task description:
    Evaluate the quality of the generated context for the root cause malware/tool by comparing it against the original article based on the provided criteria and metrics.

    Original article:
    {original_article}

    Generated Context:
    {generated_context}
    """

    # Prepare messages for API call
    new_messages = [{"role": "system", "content": sys_prompt}]
    new_messages.append({"role": "user", "content": user_prompt})

    # Call the API to perform the evaluation
    response_message = api_call(client, new_messages, model_name=model, json_enabled=True)
    response = response_message.choices[0].message.content

    # Parse the JSON response
    try:
        evaluation_scores = json.loads(response)
    except json.JSONDecodeError as e:
        print(f"Error parsing evaluation response: {e}")
        evaluation_scores = {"error": "Unable to parse scores"}

    return evaluation_scores


def main():
    """
    Main function to run root cause evaluation.
    """
    parser = argparse.ArgumentParser(description="Evaluate root cause extraction quality")
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
        default='score_evaluation/root_cause',
        help="Output directory for results (default: score_evaluation/root_cause)"
    )
    parser.add_argument(
        "--context-field",
        type=str,
        default='baseline_root_cause_context',
        help="Field name containing generated context (default: baseline_root_cause_context)"
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
        evaluate_function=evaluate_root_cause_context,
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
