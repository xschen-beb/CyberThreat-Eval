import json
# from run import evaluate_actor_context, calculate_average_score
# from openai import AzureOpenAI
import os

#client = AzureOpenAI(
#    azure_endpoint=os.getenv("LOCAL_ENDPOINT"),
#    api_key=os.getenv("PROXY_KEY"),
#    api_version="2024-05-01-preview",
# )

if __name__ == '__main__':
    # Open the output file in read mode
    models = ['o3-mini', 'gpt-4o', 'gpt-4o-mini-2024-07-18-model_1_datasets_v01_no_sa_all_csf', 'gpt-4o-2024-08-06-ti_prune2_1030']
    for model in models:
        open_file = f'score_evaluation/root_cause/{model}.json'
        print(f"=> Processing: {open_file}")
        with open(open_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        baseline_total = 0.0
        rag_total = 0.0
        count = 0

        # Define the evaluation criteria keys
        criteria_keys = ["Relevance", "Accuracy", "Comprehensiveness", "Clarity", "Coherence", "Attribution"]
        baseline_sum = {key: 0.0 for key in criteria_keys}
        rag_sum = {key: 0.0 for key in criteria_keys}

        # Iterate through each JSON object line (except the last line if reserved for overall averages)
        for line in lines[:-1]:
            data = json.loads(line)

            # Skip entries where the threat actor context is "Not specified"
            if data.get("baseline_threat_actor_context", "") and "not specified" in data["baseline_threat_actor_context"].lower():
                continue

            # Accumulate overall average scores
            baseline_total += data.get("baseline_average", 0)
            rag_total += data.get("rag_average", 0)
            count += 1

            # Accumulate scores for each evaluation criterion (baseline)
            baseline_eval = data.get("baseline_evaluation", {})
            for key in criteria_keys:
                baseline_sum[key] += baseline_eval.get(key, 0)

            # Accumulate scores for each evaluation criterion (rag)
            rag_eval = data.get("rag_evaluation", {})
            for key in criteria_keys:
                rag_sum[key] += rag_eval.get(key, 0)

        # Compute overall average scores for baseline and RAG evaluations
        overall_baseline_average = baseline_total / count if count > 0 else 0
        overall_rag_average = rag_total / count if count > 0 else 0

        # Compute per-criterion average scores for baseline and RAG evaluations
        baseline_avg_keys = {key: (baseline_sum[key] / count if count > 0 else 0) for key in criteria_keys}
        rag_avg_keys = {key: (rag_sum[key] / count if count > 0 else 0) for key in criteria_keys}

        # Prepare the overall averages output in the required JSON structure
        overall_averages = {
            "overall_baseline_average": overall_baseline_average,
            "overall_rag_average": overall_rag_average,
            "baseline_criteria_average": baseline_avg_keys,
            "rag_criteria_average": rag_avg_keys
        }

        print(f"Valid numbers: {count}")
        print("Overall Baseline Average:", overall_baseline_average)
        print("Overall RAG Average:", overall_rag_average)
        print("Baseline Criteria Averages:", baseline_avg_keys)
        print("RAG Criteria Averages:", rag_avg_keys)
