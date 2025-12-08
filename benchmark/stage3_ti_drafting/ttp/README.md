# TTP Extraction Evaluation

This directory contains the evaluation framework for MITRE ATT&CK TTP (Tactics, Techniques, and Procedures) extraction from cybersecurity threat intelligence articles.

## Overview

The TTP extraction task evaluates how well Large Language Models (LLMs) can identify and extract MITRE ATT&CK techniques from cybersecurity articles. The evaluation uses micro-averaged precision and recall metrics to measure extraction accuracy across multiple articles.

## Directory Structure

```
ttp/
├── README.md                    # This file
├── data/                        # Original data files
│   ├── 100-days-articles.json  # Evaluation dataset with ground truth TTPs
│   └── TTP_Mapping.csv         # Authoritative TTP ID to name mapping
├── eval/                        # Evaluation tools
│   └── compute.py              # Core evaluation functions
└── example/                     # Example files for testing
    ├── example_ground_truth.json    # Example ground truth articles
    ├── example_predicted.json      # Example LLM prediction results
    └── simple_test.py              # Example test script
```

## Files

### Original Data Files

These are the source data files used for evaluation:

#### `data/100-days-articles.json`

The main evaluation dataset containing cybersecurity articles with ground truth TTP annotations.

**Format**: JSON array of article objects

```json
[
    {
        "title": "Article Title",
        "content": "Full article content in markdown format...",
        "ttps": [
            "T1204 - User Execution",
            "T1189 - Drive-by Compromise",
            "T1036 - Masquerading"
        ],
        "source": "Article Source Name"
    }
]
```

**Key Fields**:
- `title` (str): Article title
- `content` (str): Full article content, typically in markdown format
- `ttps` (list[str]): **Required**. Ground truth TTPs in format `"Txxxx - Description"`
  - `Txxxx`: MITRE ATT&CK technique ID (e.g., "T1204")
  - `Description`: Official technique name (e.g., "User Execution")
- `source` (str, optional): Article source

#### `data/TTP_Mapping.csv`

Authoritative mapping between TTP IDs and their official MITRE ATT&CK names. Used to validate that extracted TTP descriptions match expected names.

**Format**: CSV file
- Column 1 (index 0): Technique ID
- Column 2 (index 1): TTP ID (e.g., "T1204")
- Column 3 (index 2): TTP name (e.g., "User Execution")

The evaluation function reads columns at index 1 (TTP ID) and index 2 (TTP name) to build the mapping.

### Evaluation Tools

#### `eval/compute.py`

Core evaluation module containing:

- **`compute_raw_precision_recall(articles, result)`**: Main evaluation function
  - Computes micro-averaged precision and recall across articles
  - Validates extracted TTPs against `TTP_Mapping.csv`
  - Returns `(precision, recall)` tuple

- **`load_articles_from_file(articles_file)`**: Load articles from JSON file
  - Handles single article or list of articles
  - Returns list of article dictionaries

- **`load_results_from_file(results_file)`**: Load prediction results from file
  - Supports JSON arrays of dicts (converted to JSON strings)
  - Supports JSON arrays of strings
  - Supports line-separated JSON strings
  - Uses `json5` to handle comments in JSON files
  - Returns list of JSON strings

- **Command-line interface**: Run evaluation from command line
  ```bash
  python eval/compute.py --articles <articles_file> --results <results_file> [--ttp-mapping <mapping_file>] [--output <output_file>]
  ```

### Example Files

#### `example/example_ground_truth.json`

Example ground truth articles matching the format of `data/100-days-articles.json`. Contains 2 sample articles for testing.

#### `example/example_predicted.json`

Example LLM prediction results in JSON format. Contains predictions for the 2 articles in `example_ground_truth.json`. Supports JSON5 comments.

**Format**: JSON array of prediction dictionaries

```json
[
    {
        "T1204": "User Execution, Confidence: High. Justification: ...",
        "T1189": "Drive-by Compromise, Confidence: High. Justification: ...",
        "T1036": "Masquerading, Confidence: High. Justification: ...",
        "T1071": "Application Layer Protocol, Confidence: Low. Justification: ..."  // False positive
    }
]
```

#### `example/simple_test.py`

Example test script demonstrating how to:
- Load articles and predictions from files
- Run evaluation using the API
- Display results

## Input/Output Formats

### Input Format

#### Article Input (Ground Truth)

Articles can be provided as:
1. **Python list of dictionaries** (for API usage)
2. **JSON file** (for file-based evaluation)

Each article must have:
- `ttps` (list[str]): **Required**. Ground truth TTPs in format `"Txxxx - Description"`

Optional fields:
- `title`, `content`, `source` (useful for debugging but not used in evaluation)

#### Prediction Input (LLM Results)

Predictions can be provided as:
1. **JSON string** (single article)
2. **Python dictionary** (single article)
3. **List of JSON strings** (multiple articles, one per article)
4. **JSON file** containing array of dicts or strings

**Prediction Format**:
```json
{
    "T1204": "User Execution, Confidence: High. Justification: The article describes...",
    "T1189": "Drive-by Compromise, Confidence: Medium. Justification: ...",
    "T1071": "Application Layer Protocol, Confidence: Low. Justification: ..."
}
```

**Key Requirements**:
- **Keys**: TTP IDs as strings (e.g., `"T1204"`)
- **Values**: Strings in format `"<Description>, Confidence: <Level>. Justification: <text>"`
  - Description (first part before comma) must match official TTP name from `TTP_Mapping.csv` (case-insensitive)
  - Example: `"User Execution, Confidence: High. Justification: ..."`

**File Formats Supported**:
- JSON array of dictionaries: `[{"T1204": "..."}, {"T1189": "..."}]`
- JSON array of JSON strings: `["{\"T1204\": \"...\"}", "{\"T1189\": \"...\"}"]`
- Line-separated JSON strings (one per line)
- JSON5 format (supports comments like `// comment` or `# comment`)

### Output Format

#### Console Output

The evaluation prints:
- Per-article metrics (TP, FP, FN)
- Overall aggregated metrics:
  - Total True Positives
  - Total False Positives
  - Total False Negatives
  - Micro-averaged Precision
  - Micro-averaged Recall
  - Micro-averaged F1-Score

#### JSON Output (when using `--output`)

```json
{
    "precision": 0.8571,
    "recall": 0.7500,
    "f1_score": 0.8000,
    "num_articles": 2
}
```

## Evaluation Process

### Step 1: Extract Ground Truth TTPs

For each article, extract TTP IDs from the `ttps` field:

```python
raw_ttps = article.get("ttps", [])
article_ttps_set = {ttp.split(" - ")[0].strip() for ttp in raw_ttps if " - " in ttp}
```

This creates a set of TTP IDs (e.g., `{"T1204", "T1189", "T1036"}`).

### Step 2: Parse LLM Extraction Results

Parse the LLM result (JSON string or dict) to extract TTP IDs and descriptions.

### Step 3: Validate Extracted TTPs

Each extracted TTP is validated against `TTP_Mapping.csv`:

1. **TTP ID Check**: TTP ID must exist in mapping file
2. **Description Matching**: Description must match official TTP name (case-insensitive)
3. **Filtering**: Only TTPs with matching descriptions are included

**Example**:
- LLM extracts: `"T1204": "User Execution, Confidence: High..."`
- Mapping has: `T1204 -> "User Execution"`
- Result: **Validated** ✓

- LLM extracts: `"T1204": "Execution, Confidence: High..."` (description mismatch)
- Result: **Rejected** ✗ (counted as false positive)

### Step 4: Calculate Metrics

For each article:
- **True Positives (TP)**: TTPs in ground truth AND successfully extracted with matching description
- **False Positives (FP)**: TTPs extracted but NOT in ground truth, OR with description mismatches
- **False Negatives (FN)**: TTPs in ground truth but NOT extracted (or extracted with mismatch)

### Step 5: Aggregate Results

Micro-averaged metrics across all articles:

```python
overall_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
overall_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
```

## Usage

### Method 1: Command-Line Interface

Evaluate using the command-line tool:

```bash
# Basic usage
python eval/compute.py \
    --articles data/100-days-articles.json \
    --results predictions.json

# With custom TTP mapping
python eval/compute.py \
    --articles data/100-days-articles.json \
    --results predictions.json \
    --ttp-mapping data/TTP_Mapping.csv

# Save results to file
python eval/compute.py \
    --articles data/100-days-articles.json \
    --results predictions.json \
    --output results.json
```

**Arguments**:
- `--articles` (required): Path to JSON file containing articles with ground truth TTPs
- `--results` (required): Path to JSON file containing LLM prediction results
- `--ttp-mapping` (optional): Path to TTP mapping CSV file (default: `data/TTP_Mapping.csv`)
- `--output` (optional): Path to save evaluation results as JSON

### Method 2: Python API

Use the evaluation functions directly in Python:

```python
from eval.compute import compute_raw_precision_recall, load_articles_from_file, load_results_from_file

# Load articles and predictions from files
articles = load_articles_from_file("data/100-days-articles.json")
results = load_results_from_file("predictions.json")

# Run evaluation
precision, recall = compute_raw_precision_recall(articles, results)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
```

### Method 3: Using Example Files

Test the evaluation with the provided example files:

```bash
# Run the example test script
cd example
python simple_test.py
```

Or use the example files with the command-line tool:

```bash
python eval/compute.py \
    --articles example/example_ground_truth.json \
    --results example/example_predicted.json
```

## Complete Example

### Example: Using Example Files

This example demonstrates the full evaluation workflow using the files in the `example/` directory.

#### Step 1: Ground Truth File (`example/example_ground_truth.json`)

```json
[
    {
        "title": "DeepSeek Lure Using CAPTCHAs To Spread Malware",
        "content": "## Snapshot\r\nResearchers at ThreatLabz...",
        "ttps": [
            "T1204 - User Execution",
            "T1189 - Drive-by Compromise",
            "T1036 - Masquerading"
        ],
        "source": "DeepSeek Lure Using CAPTCHAs To Spread Malware"
    },
    {
        "title": "Auto-Color: An Emerging and Evasive Linux Backdoor",
        "content": "## Snapshot\r\nPalo Alto Networks...",
        "ttps": [
            "T1204 - User Execution",
            "T1036 - Masquerading",
            "T1070 - Indicator Removal",
            "T1219 - Remote Access Software"
        ],
        "source": "Auto-Color: An Emerging and Evasive Linux Backdoor"
    }
]
```

#### Step 2: Prediction File (`example/example_predicted.json`)

```json
[
    {
        "T1204": "User Execution, Confidence: High. Justification: The article describes users executing malicious PowerShell commands from clipboard.",
        "T1189": "Drive-by Compromise, Confidence: High. Justification: The article mentions fake CAPTCHA pages and drive-by download techniques.",
        "T1036": "Masquerading, Confidence: High. Justification: The campaign uses fake DeepSeek look-alike domains to masquerade as legitimate services.",
        "T1071": "Application Layer Protocol, Confidence: Low. Justification: The article mentions communication via Telegram and Steam."  // False positive
    },
    {
        "T1036": "Masquerading, Confidence: High. Justification: The malware disguises itself with benign-sounding names like 'door' or 'egg'.",
        "T1070": "Indicator Removal, Confidence: High. Justification: The malware alters network activity data to conceal C2 connections.",
        "T1219": "Remote Access Software, Confidence: High. Justification: The malware provides remote access capabilities including reverse shell creation.",
        "T1055": "Process Injection, Confidence: Low. Justification: The article mentions hooking into system libraries."  // False positive
    }
]
```

#### Step 3: Run Evaluation

**Using command line**:
```bash
python eval/compute.py \
    --articles example/example_ground_truth.json \
    --results example/example_predicted.json
```

**Using Python API**:
```python
from eval.compute import compute_raw_precision_recall, load_articles_from_file, load_results_from_file

# Load files
articles = load_articles_from_file("example/example_ground_truth.json")
results = load_results_from_file("example/example_predicted.json")

# Evaluate
precision, recall = compute_raw_precision_recall(articles, results)

# Calculate F1
f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
```

#### Step 4: Expected Output

```
Loading articles from: example/example_ground_truth.json
Loaded 2 articles
Loading results from: example/example_predicted.json
Loaded 2 results

============================================================
Computing Precision and Recall Metrics
============================================================

Article TTP Codes: {'T1204', 'T1189', 'T1036'}
Extracted Validated TTPs (pre-mapping): {'T1204': '...', 'T1189': '...', 'T1036': '...', 'T1071': '...'}
Validated TTP Codes (after mapping validation): {'T1204', 'T1189', 'T1036'}
Article metrics: TP: 3, FP: 1, FN: 0

Article TTP Codes: {'T1204', 'T1036', 'T1070', 'T1219'}
Extracted Validated TTPs (pre-mapping): {'T1036': '...', 'T1070': '...', 'T1219': '...', 'T1055': '...'}
Validated TTP Codes (after mapping validation): {'T1036', 'T1070', 'T1219'}
Article metrics: TP: 3, FP: 1, FN: 1

============================================================
Overall Metrics (All Articles):
============================================================
Total True Positives: 6
Total False Positives: 2
Total False Negatives: 1
Precision: 0.7500
Recall: 0.8571
============================================================

============================================================
Final Summary
============================================================
Micro-Averaged Precision: 0.7500
Micro-Averaged Recall: 0.8571
Micro-Averaged F1-Score: 0.8000
============================================================
```

## Function Reference

### `compute_raw_precision_recall(articles, result)`

Compute micro-averaged precision and recall for TTP extraction.

**Parameters**:
- `articles` (list[dict]): List of article dictionaries. Each must have `ttps` field.
- `result` (str | dict | list): 
  - Single result: JSON string or dict (applied to all articles)
  - Multiple results: List of JSON strings or dicts (one per article)

**Returns**:
- `tuple`: `(precision, recall)` as floats

**Example**:
```python
# Single article with single result
article = [{"ttps": ["T1204 - User Execution"]}]
result = '{"T1204": "User Execution, Confidence: High. Justification: ..."}'
precision, recall = compute_raw_precision_recall(article, result)

# Multiple articles with multiple results
articles = load_articles_from_file("articles.json")
results = load_results_from_file("predictions.json")
precision, recall = compute_raw_precision_recall(articles, results)
```

## Dependencies

Required Python packages:

```bash
pip install json5
```

**Python imports**:
```python
import json
import json5  # For flexible JSON parsing (supports comments)
import time
```

## Notes

- The evaluation uses **micro-averaging**: metrics are calculated by aggregating TP, FP, FN across all articles, then computing precision/recall
- TTP descriptions must match the official MITRE ATT&CK names (case-insensitive) from `TTP_Mapping.csv`
- Description mismatches are counted as false positives, even if the TTP ID is correct
- The `ttps` field format must be `"Txxxx - Description"` with space-hyphen-space separator
- JSON5 format is supported for prediction files, allowing comments (useful for documentation)
