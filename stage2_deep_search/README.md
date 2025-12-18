# Stage 2: Deep Search Evaluation

This directory contains the evaluation framework for Stage 2 (Deep Search) of the CyberThreat-Eval benchmark. The evaluation assesses the quality of related URLs found for cybersecurity articles by analyzing their relationships and information value.

## Overview

The Deep Search evaluation framework evaluates how well systems can find and assess related URLs for cybersecurity articles. The core evaluation focuses on:

1. **Reference Relationship Analysis**: Identifying which URLs reference each other
2. **Reference URL Identification**: Using PageRank algorithm to find the primary reference URL
3. **Additional Information Assessment**: Using LLM to determine if other URLs contain additional information beyond the reference URL

The main evaluation script is `code/eval.py`, which processes articles with related URLs and generates comprehensive metrics.

## Directory Structure

```
stage2_deep_search/
├── README.md                    # This file
├── code/                        # Core evaluation script
│   └── eval.py                 # Main evaluation script (FOCUS)
├── data/                        # Input dataset
│   └── 0510-articles.json     # Articles dataset
├── example/                     # Example scripts 
│   ├── process_articles.py     # Example: Generate related URLs
│   ├── process_related_similarity.py
│   ├── calculate_model_statistics.py
│   └── llm.py
└── utils/                       # Utility functions
    ├── llm.py                  # LLM utilities
    └── search_engine.py        # Web scraping utilities
```

**Note**: The `example/` directory contains reference scripts showing how to generate related URLs. The core evaluation is in `code/eval.py`.

## Evaluation Core: `code/eval.py`

The main evaluation script analyzes related URLs found for articles and assesses their information value.

### Evaluation Process

For each article with related URLs, the evaluation performs:

1. **Extract Reference Relationships**: 
   - Scrapes content from each URL
   - Extracts links from the content
   - Identifies which URLs reference each other

2. **Identify Reference URL**:
   - Builds a directed graph of reference relationships
   - Calculates PageRank scores for all URLs
   - Selects the URL with highest PageRank as the reference URL

3. **Check Additional Information**:
   - For each non-reference URL, compares its content with the reference URL
   - Uses LLM to determine if the URL contains additional information
   - Additional information includes: new facts, analysis, technical details, etc.

4. **Generate Metrics**:
   - Per-article metrics (reference URL, additional info URLs, counts)
   - Aggregate metrics across all articles

### Key Functions

#### `extract_links_from_content(urls)`
Extracts links from the content of each URL and identifies reference relationships between URLs.

- Scrapes content from each URL using browser automation
- Extracts HTTP/HTTPS links using regex patterns
- Matches links to target URLs using multiple normalization strategies
- Returns: `url_links` (dict mapping URL to set of links) and `references` (list of (source, target) tuples)

#### `calculate_pagerank(references, urls)`
Calculates PageRank scores for URLs based on their reference relationships.

- Builds a directed graph from reference relationships
- Uses NetworkX PageRank algorithm
- Returns: PageRank scores, graph, and URL-to-ID mappings

#### `check_additional_information_with_voting(reference_blog, comparison_blog, api_key, api_base)`
Uses LLM to determine if a comparison blog contains additional information beyond the reference blog.

- **Additional Information Definition**: New facts, data, analysis, interpretations, technical details, or contextual information
- Returns JSON with `has_additional_info` (boolean) and `justification` (string)

#### `process_result_file(result_file, output_dir, model_folder, api_key, api_base)`
Processes a single article result file.

**Input Format**:
```json
{
  "id": "article_id",
  "url": "original_article_url",
  "related_urls": ["url1", "url2", "url3", ...]
}
```

**Output Format**:
```json
{
  "id": "article_id",
  "original_url": "original_article_url",
  "related_urls_count": 5,
  "reference_url": "url_with_highest_pagerank",
  "additional_info_urls": [
    {
      "url": "url_with_additional_info",
      "justification": "Contains new CVE details and mitigation strategies"
    }
  ],
  "additional_info_count": 2,
  "model": "model_name"
}
```

#### `process_all_results(results_dir, output_dir, test_model_name, api_key, api_base, max_workers=4)`
Processes all result files in a directory with parallel execution.

- Processes multiple articles in parallel (configurable workers)
- Generates per-article analyses
- Calculates aggregate metrics
- Saves results to JSON files

**Output Files**:
- `{article_id}_similarity_analysis.json`: Per-article analysis
- `all_similarity_analyses.json`: All analyses + aggregate metrics
- `aggregate_metrics.json`: Aggregate metrics only
- `combined_metrics.json`: Combined metrics across all models

## Evaluation Metrics

### Per-Article Metrics

- **`related_urls_count`**: Number of related URLs found for the article
- **`reference_url`**: Primary reference URL identified via PageRank (the most authoritative source)
- **`additional_info_urls`**: List of URLs that contain additional information beyond the reference URL
  - Each entry includes `url` and `justification` (explanation of additional information)
- **`additional_info_count`**: Number of URLs with additional information

### Aggregate Metrics

- **`total_articles`**: Total number of articles analyzed
- **`successful_articles`**: Number of articles successfully processed (no errors)
- **`failed_articles`**: Number of articles that failed processing
- **`total_related_urls`**: Sum of all related URLs across articles
- **`total_additional_info_urls`**: Sum of all additional info URLs
- **`avg_related_urls_per_article`**: Average number of related URLs per article
- **`avg_additional_info_urls_per_article`**: Average number of additional info URLs per article
- **`percentage_with_additional_info`**: Percentage of articles that have at least one URL with additional information

### Metric Interpretation

- **High `avg_related_urls_per_article`**: System finds many related URLs (good coverage)
- **High `avg_additional_info_urls_per_article`**: System finds URLs with valuable additional information (good quality)
- **High `percentage_with_additional_info`**: System consistently finds URLs with additional information across articles

## Usage

### Command-Line Interface

The evaluation script can be run from the command line:

```bash
python code/eval.py \
    --results_dir <path_to_results_directory> \
    --output_dir <output_directory> \
    --test_model_name <model_name> \
    --api_key <openai_api_key> \
    --api_base <api_base_url> \
    --workers <number_of_workers>
```

**Arguments**:
- `--results_dir` (required): Directory containing result JSON files (files ending with `_results.json`)
- `--output_dir` (default: `similarity_analyses`): Output directory for evaluation results
- `--test_model_name` (required): Model name for evaluation (used in output files)
- `--api_key` (required): OpenAI API key for LLM calls
- `--api_base` (required): API base URL (e.g., `https://api.openai.com/v1`)
- `--workers` (default: 4): Number of parallel workers for processing

**Example**:
```bash
cd benchmark/stage2_deep_search
python code/eval.py \
    --results_dir processed_results/gpt-4o \
    --output_dir similarity_analyses \
    --test_model_name gpt-4o \
    --api_key $OPENAI_API_KEY \
    --api_base https://api.openai.com/v1 \
    --workers 4
```

### Python API

You can also use the evaluation functions directly in Python:

```python
from code.eval import (
    process_result_file,
    process_all_results,
    extract_links_from_content,
    calculate_pagerank,
    check_additional_information_with_voting
)

# Process a single result file
result = process_result_file(
    result_file="path/to/article_id_results.json",
    output_dir="output/",
    model_folder="model_folder",
    api_key="your_api_key",
    api_base="https://api.openai.com/v1"
)

# Process all results in a directory
process_all_results(
    results_dir=["path/to/results/dir"],
    output_dir="output/",
    test_model_name="model_name",
    api_key="your_api_key",
    api_base="https://api.openai.com/v1",
    max_workers=4
)
```

## Input/Output Format

### Input Format

The evaluation expects JSON result files with the following structure:

```json
{
  "id": "article_12345",
  "url": "https://example.com/article",
  "related_urls": [
    "https://example.com/related1",
    "https://example.com/related2",
    "https://example.com/related3"
  ]
}
```

**Required Fields**:
- `id`: Article identifier
- `url`: Original article URL
- `related_urls`: List of related URLs found for the article

### Output Format

#### Per-Article Analysis

Each article generates a similarity analysis file: `{article_id}_similarity_analysis.json`

```json
{
  "id": "article_12345",
  "original_url": "https://example.com/article",
  "related_urls_count": 3,
  "reference_url": "https://example.com/related1",
  "additional_info_urls": [
    {
      "url": "https://example.com/related2",
      "justification": "Contains additional CVE details and exploit information"
    }
  ],
  "additional_info_count": 1,
  "model": "gpt-4o"
}
```

#### Aggregate Metrics

The `aggregate_metrics.json` file contains:

```json
{
  "aggregate_metrics": {
    "model": "gpt-4o",
    "total_articles": 100,
    "successful_articles": 98,
    "failed_articles": 2,
    "total_related_urls": 450,
    "total_additional_info_urls": 120,
    "avg_related_urls_per_article": 4.59,
    "avg_additional_info_urls_per_article": 1.22,
    "percentage_with_additional_info": 75.51,
    "timestamp": "2024-01-15T10:30:00"
  }
}
```

## Example Scripts (Reference Only)

The `example/` directory contains reference scripts showing how to generate related URLs. These are **not part of the core evaluation** but provide examples for:

- **`example/process_articles.py`**: Example script for processing articles and generating related URLs using LLM
- **`example/process_related_similarity.py`**: Alternative similarity analysis script (reference)
- **`example/calculate_model_statistics.py`**: Example script for calculating statistics from results

**Note**: The core evaluation is in `code/eval.py`. The example scripts are provided for reference only to show how related URLs might be generated.

## Dependencies

Required Python packages:

```bash
pip install networkx openai azure-identity playwright playwright-stealth tqdm tenacity tiktoken
```

**Key Dependencies**:
- **networkx**: For PageRank calculation
- **openai** / **azure-identity**: For LLM API calls
- **playwright** / **playwright-stealth**: For web scraping (via `utils/search_engine.py`)
- **tqdm**: For progress bars
- **tenacity**: For retry logic
- **tiktoken**: For token counting

## Key Features

### Parallel Processing
- Supports multi-threaded processing with configurable worker count
- Thread-safe file operations
- Progress tracking with `tqdm`

### PageRank-Based Reference Identification
- Uses NetworkX PageRank algorithm to identify the most authoritative reference URL
- Handles cases with no references (falls back to original URL or first URL)

### LLM-Based Additional Information Detection
- Uses LLM to assess if URLs contain additional information
- Provides justifications for additional information
- Handles errors gracefully with retry logic

### URL Normalization
- Multiple normalization strategies for URL matching:
  - Protocol-agnostic matching
  - Query parameter sorting
  - RSS/feed path removal
  - Domain-level matching with path consideration

### Comprehensive Logging
- Logs to both file and console
- UTF-8 encoding support
- Detailed debug information

### Error Handling
- Retry logic for API calls (up to 6 attempts with exponential backoff)
- Graceful error handling for individual articles
- Continues processing even if some articles fail

## Evaluation Methodology

### Reference Relationship Extraction

The evaluation extracts reference relationships by:
1. Scraping content from each URL using browser automation
2. Extracting HTTP/HTTPS links using regex patterns
3. Normalizing URLs for comparison (handling protocol differences, query parameters, etc.)
4. Matching extracted links to target URLs using multiple strategies

### PageRank Calculation

The PageRank algorithm is used to identify the most authoritative reference URL:
- Builds a directed graph where edges represent reference relationships
- URLs that are referenced by more other URLs receive higher PageRank scores
- The URL with the highest PageRank is selected as the reference URL

### Additional Information Assessment

The LLM-based assessment checks for:
- **New facts or data**: Numbers, dates, CVEs, malware names, actors, tools, geography
- **New analysis or interpretations**: Novel links, causes, trends, forecasts, mitigation advice
- **Extra technical or contextual details**: Methods, background, case studies, impact elaboration
- **Any other additional details** absent from the reference blog

The LLM provides a boolean decision (`has_additional_info`) and a justification explaining the additional information found.

## Notes

- The evaluation requires internet access for web scraping (to extract links from URLs)
- LLM API calls are required for additional information assessment
- Processing time depends on the number of URLs and API response times
- The evaluation handles cases where URLs cannot be accessed (continues with available URLs)
- Results are saved incrementally (per-article files) and aggregated (all analyses + metrics)

## Troubleshooting

### Common Issues

1. **URL Access Failures**: Some URLs may be inaccessible. The evaluation continues with available URLs.

2. **API Rate Limits**: If you encounter rate limits, reduce the `--workers` parameter or add delays.

3. **Memory Issues**: For large datasets, process in batches or reduce parallel workers.

4. **Encoding Errors**: The evaluation handles UTF-8 encoding, but some URLs may contain problematic characters.

### Logging

Check the log file (e.g., `sim-{model_name}.log`) for detailed debug information about the evaluation process.

