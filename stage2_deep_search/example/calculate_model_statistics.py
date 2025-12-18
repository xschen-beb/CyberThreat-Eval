import os
import json
import statistics
from collections import defaultdict

def calculate_model_statistics(base_dir="deep_search"):
    """
    Calculate statistics for each model in the processed_results directory
    """
    models_dir = os.path.join(base_dir, "0515-processed_results")
    output_dir = os.path.join(base_dir, "statistics")
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all model directories
    model_dirs = [d for d in os.listdir(models_dir) if os.path.isdir(os.path.join(models_dir, d))]
    
    # Skip directories with 'all_results.json' only
    model_dirs = [d for d in model_dirs if any(f for f in os.listdir(os.path.join(models_dir, d)) 
                                            if f != 'all_results.json' and f.endswith('_results.json'))]
    
    results = {}
    all_data = []
    
    for model in model_dirs:
        print(f"Processing model: {model}")
        model_path = os.path.join(models_dir, model)
        model_results = process_model_dir(model_path, model)
        results[model] = model_results
        all_data.append(model_results)
        
        # Save individual model results
        with open(os.path.join(output_dir, f"{model}_statistics.json"), 'w', encoding='utf-8') as f:
            json.dump(model_results, f, ensure_ascii=False, indent=2)
    
    # Create a comparison table
    model_comparison = create_comparison_table(all_data)
    
    # Save comparison table
    with open(os.path.join(output_dir, "model_comparison.json"), 'w', encoding='utf-8') as f:
        json.dump(model_comparison, f, ensure_ascii=False, indent=2)
    
    # Save combined results
    with open(os.path.join(output_dir, "all_models_statistics.json"), 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # Print results for each model
    print("\nModel Statistics:")
    print("-" * 100)
    print(f"{'Model':<40} | {'Avg URLs':<10} | {'Avg Time (s)':<15} | {'Files':<10} | {'Total URLs':<10}")
    print("-" * 100)
    
    for model_data in all_data:
        model = model_data["model"]
        print(f"{model:<40} | {model_data['avg_related_urls']:<10.2f} | {model_data['avg_processing_time']:<15.2f} | {model_data['total_files']:<10} | {model_data['total_related_urls']:<10}")
    
    return results, model_comparison

def create_comparison_table(all_data):
    """
    Create a comparison table with statistics for all models
    """
    models = [data["model"] for data in all_data]
    
    comparison = {
        "models": models,
        "avg_related_urls": [data["avg_related_urls"] for data in all_data],
        "median_related_urls": [data["median_related_urls"] for data in all_data],
        "avg_processing_time": [data["avg_processing_time"] for data in all_data],
        "median_processing_time": [data["median_processing_time"] for data in all_data],
        "total_files": [data["total_files"] for data in all_data],
        "total_related_urls": [data["total_related_urls"] for data in all_data]
    }
    
    return comparison

def process_model_dir(model_dir, model_name):
    """
    Process all JSON files in a model directory and calculate statistics
    """
    related_urls_count = []
    processing_times = []
    id_to_data = {}
    
    # Walk through model directory
    for root, _, files in os.walk(model_dir):
        for file in files:
            if file.endswith('_results.json') and file != 'all_results.json':
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Extract data
                    article_id = data.get('id', os.path.basename(file_path).replace('_results.json', ''))
                    related_urls = data.get('number_of_related_urls', 0)
                    processing_time = data.get('processing_time', 0)
                    
                    related_urls_count.append(related_urls)
                    processing_times.append(processing_time)
                    
                    # Store by ID for later comparisons
                    id_to_data[str(article_id)] = {
                        'related_urls': related_urls,
                        'processing_time': processing_time,
                        'file_path': file_path
                    }
                    
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")
    
    # Calculate statistics
    result = {
        'model': model_name,
        'total_files': len(related_urls_count),
        'avg_related_urls': statistics.mean(related_urls_count) if related_urls_count else 0,
        'median_related_urls': statistics.median(related_urls_count) if related_urls_count else 0,
        'min_related_urls': min(related_urls_count) if related_urls_count else 0,
        'max_related_urls': max(related_urls_count) if related_urls_count else 0,
        'stdev_related_urls': statistics.stdev(related_urls_count) if len(related_urls_count) > 1 else 0,
        'avg_processing_time': statistics.mean(processing_times) if processing_times else 0,
        'median_processing_time': statistics.median(processing_times) if processing_times else 0,
        'min_processing_time': min(processing_times) if processing_times else 0,
        'max_processing_time': max(processing_times) if processing_times else 0,
        'stdev_processing_time': statistics.stdev(processing_times) if len(processing_times) > 1 else 0,
        'total_related_urls': sum(related_urls_count),
        'total_processing_time': sum(processing_times)
    }
    
    # Additional insights
    if len(related_urls_count) > 0:
        result['urls_per_hour'] = result['total_related_urls'] / (result['total_processing_time'] / 3600) if result['total_processing_time'] > 0 else 0
        
        # URLs distribution
        dist = defaultdict(int)
        for count in related_urls_count:
            dist[count] += 1
        result['url_count_distribution'] = dict(sorted(dist.items()))
    
    return result

if __name__ == "__main__":
    results, comparison = calculate_model_statistics()
    
    # Print formatted comparison table
    print("\nModel Comparison:")
    print("-" * 100)
    print(f"{'Model':<40} | {'Avg URLs':<10} | {'Med URLs':<10} | {'Avg Time':<10} | {'Med Time':<10} | {'Total URLs':<10}")
    print("-" * 100)
    
    models = comparison["models"]
    for i, model in enumerate(models):
        print(f"{model:<40} | {comparison['avg_related_urls'][i]:<10.2f} | {comparison['median_related_urls'][i]:<10.2f} | " +
              f"{comparison['avg_processing_time'][i]:<10.2f} | {comparison['median_processing_time'][i]:<10.2f} | " +
              f"{comparison['total_related_urls'][i]:<10}") 