import os
import re
import json
from crawl_malpedia import extract_threat_actor_info
from crawl_oneti import *
from utils import evaluate_actor_context
from mdti_pipeline import pipeline
from tenacity import retry, stop_after_attempt, wait_random_exponential
from tqdm import tqdm


def find_files_with_threat_actor(directory):
    files_with_threat_actors = []

    # Use tqdm to wrap os.walk for progress tracking
    for root, _, files in tqdm(list(os.walk(directory)), desc="Scanning Directories", unit="directory"):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if extract_threat_actor_info(file_path):
                    files_with_threat_actors.append(file_path)
    return files_with_threat_actors


def save_results(results, output_file):
    with open(output_file, 'a') as f:
        json.dump(results, f)
        f.write('\n')
    print(f"Results saved to {output_file}")


def process_raw():
    directory = 'AgentGenReport'
    files = find_files_with_threat_actor(directory)

    # Prepare for storing the evaluation results
    all_results = []
    total_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    total_known_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    total_unknown_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    
    total_files = 0
    known_files = 0
    unknown_files = 0

    unknown = 0
    for file in tqdm(files, desc="Processing Files", unit="file"):
        print(f"File name: {file}")
        flag = True
        threat_actor_info = extract_threat_actor_info(file)
        threat_actors = eval(get_actor(threat_actor_info))
        if 'None' in threat_actors:
            unknown += 1
            flag = False

        evaluation_scores = evaluate_actor_context(threat_actors, threat_actor_info)
        
        if flag:
            file_results = {
                "file": file,
                "known": 'known',
                "evaluation_scores": evaluation_scores
            }
            known_files += 1
            # Sum up the scores for known files
            for key in total_known_scores:
                total_known_scores[key] += evaluation_scores.get(key, 0)
        else:
            file_results = {
                "file": file,
                "known": 'unknown',
                "evaluation_scores": evaluation_scores
            }
            unknown_files += 1
            # Sum up the scores for unknown files
            for key in total_unknown_scores:
                total_unknown_scores[key] += evaluation_scores.get(key, 0)

        save_results(file_results, "evaluation_results.json")
        all_results.append(file_results)

        # Sum up the scores for averaging later
        for key in total_scores:
            total_scores[key] += evaluation_scores.get(key, 0)
        
        total_files += 1

    # Calculate average scores for all files
    avg_scores = {key: total / total_files if total_files > 0 else 0 for key, total in total_scores.items()}

    # Calculate average scores for known files
    avg_known_scores = {key: total / known_files if known_files > 0 else 0 for key, total in total_known_scores.items()}

    # Calculate average scores for unknown files
    avg_unknown_scores = {key: total / unknown_files if unknown_files > 0 else 0 for key, total in total_unknown_scores.items()}

    # Save all results and averages to JSON file
    results_with_avg = {
        "averages": avg_scores,
        "known_averages": avg_known_scores,
        "unknown_averages": avg_unknown_scores
    }

    save_results(results_with_avg, "evaluation_results.json")

    print(f"Averages: {avg_scores}")
    print(f"Known Averages: {avg_known_scores}")
    print(f"Unknown Averages: {avg_unknown_scores}")
    print(f"Known files: {known_files}, unknown files: {unknown_files}")


def process_source_scores(threat_actors, source, oneti_token, total_scores, total_known_scores, total_unknown_scores, known_files, unknown_files):
    output = ""
    context = pipeline(threat_actors, source, oneti_token=oneti_token)
    
    if not context:
        return output, total_scores, total_known_scores, total_unknown_scores, known_files, unknown_files

    output += f"======================== {source} ========================\n"
    output += str(context)
    output += f"\n======================== {source} ========================\n"
    
    evaluation_scores = evaluate_actor_context(threat_actors, context)
    
    # Update total scores for all files
    for key in total_scores:
        total_scores[key] += evaluation_scores.get(key, 0)

    # Update scores for known or unknown files
    if 'None' in threat_actors:
        unknown_files += 1
        for key in total_unknown_scores:
            total_unknown_scores[key] += evaluation_scores.get(key, 0)
    else:
        known_files += 1
        for key in total_known_scores:
            total_known_scores[key] += evaluation_scores.get(key, 0)

    print(f"Evaluation for {source}: {evaluation_scores}")
    return output, total_scores, total_known_scores, total_unknown_scores, known_files, unknown_files


if __name__ == '__main__':
    directory = 'AgentGenReport'
    files = find_files_with_threat_actor(directory)

    # Prepare for storing the evaluation results
    all_results = []
    total_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    total_known_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    total_unknown_scores = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    
    total_files = 0
    known_files = 0
    unknown_files = 0

    client_id = "a92e7da0-0dec-4653-bae0-8b61258fd045"
    scopes = ["api://a92e7da0-0dec-4653-bae0-8b61258fd045/oneti.api"]
    token = get_access_token(client_id, scopes)

    unknown = 0
    for file in tqdm(files, desc="Processing Files", unit="file"):
        print(f"File name: {file}")
        flag = True
        threat_actor_info = extract_threat_actor_info(file)
        threat_actors = eval(get_actor(threat_actor_info))
        if 'None' in threat_actors:
            unknown += 1
            flag = False

        # Process the sources (malpedia and oneti)
        output = ""
        sources = ['oneti']
        for source in sources:
            context = pipeline(threat_actors, source, oneti_token=token)
            print(context)
            if not context:
                continue
            output += str(context)
            output += f"\n======================== {source} ========================\n"
            evaluation_scores = evaluate_actor_context(threat_actors, context)

            print(f"Evaluation for {source}: {evaluation_scores}")

            # Sum up the new scores for averaging later
            for key in total_scores:
                total_scores[key] += evaluation_scores.get(key, 0)

            if flag:
                total_known_scores[key] += evaluation_scores.get(key, 0)
            if not flag:
                total_unknown_scores[key] += evaluation_scores.get(key, 0)

            # Store the final results
            file_results = {
                "file": file,
                "known": 'known' if flag else 'unknown',
                "source": source,
                "evaluation_scores": evaluation_scores
            }

            save_results(file_results, "oneti_evaluation_results.json")
            all_results.append(file_results)

            total_files += 1

    avg_scores = {key: total / total_files if total_files > 0 else 0 for key, total in total_scores.items()}
    avg_malpedia_known_scores = {key: total / known_files if known_files > 0 else 0 for key, total in total_known_scores.items()}
    # avg_oneti_known_scores = {key: total / known_files if known_files > 0 else 0 for key, total in total_known_scores.items()}

    # Calculate averages for unknown files (malpedia and oneti separately)
    avg_malpedia_unknown_scores = {key: total / unknown_files if unknown_files > 0 else 0 for key, total in total_unknown_scores.items()}
    # avg_oneti_unknown_scores = {key: total / unknown_files if unknown_files > 0 else 0 for key, total in total_unknown_scores.items()}

    # Save all results and averages to JSON file
    results_with_avg = {
        "averages": avg_scores,
        "malpedia_known_averages": avg_malpedia_known_scores,
        # "oneti_known_averages": avg_oneti_known_scores,
        "malpedia_unknown_averages": avg_malpedia_unknown_scores,
        # "oneti_unknown_averages": avg_oneti_unknown_scores
    }

    save_results(results_with_avg, "oneti_evaluation_results.json")

    print(f"Averages: {avg_scores}")
    print(f"Malpedia Known Averages: {avg_malpedia_known_scores}")
    # print(f"Oneti Known Averages: {avg_oneti_known_scores}")
    print(f"Malpedia Unknown Averages: {avg_malpedia_unknown_scores}")
    print(f"Total files: {total_files}")
    # print(f"Oneti Unknown Averages: {avg_oneti_unknown_scores}")