# Stage 3: IOC Extraction & Evaluation

This directory contains the data, evaluation scripts, and examples for the IOC (Indicators of Compromise) extraction and evaluation portion of the CyberThreat-Eval benchmark. The task involves extracting IOCs (IP addresses, domains, URLs, file hashes, etc.) from cybersecurity threat intelligence (CTI) articles and evaluating the extraction performance against ground truth annotations.

## Overview

The IOC extraction evaluation framework assesses how well systems can identify and extract Indicators of Compromise from CTI articles. IOCs include various types of threat indicators such as:

- **IP addresses**: `31.172.83.162:443`, `107.173.89.16`
- **Domains**: `compdatasystems.com`, `api.telegram.org`
- **URLs**: `https://accessservicesonline.com/setup_wm.exe`
- **File hashes**: SHA256, SHA1, MD5 hashes (e.g., `67d9b4b35c02a19ab364ad19e1972645eb98e24dcd6f1715d2a26229deb2ccf5`)

The evaluation uses micro-averaged precision and recall metrics to measure extraction accuracy.

## Directory Structure

```
ioc/
├── README.md                          # This file
├── data/                              # Data files
│   ├── blogs.json                    # Input CTI articles (JSON format)
│   ├── IoCs.csv                      # Ground truth IOC annotations (CSV format)
│   └── All Intelligence Feeds.csv    # Additional data source
├── eval/                              # Evaluation scripts
│   └── eval_ioc.py                   # Main evaluation script
└── example/                           # Example scripts and sample data
    ├── simple_test.py                # Example test script
    └── prediction/                    # Sample prediction files
       
```

## Data Format

### Input Articles (`data/blogs.json`)

The input data consists of CTI articles in JSON format. Each entry in `blogs.json` contains an article with its text content and metadata (title, source URL, etc.). These articles serve as the input for IOC extraction systems.

**Expected Workflow:**
1. Load articles from `blogs.json`
2. Process each article through your IOC extraction pipeline
3. Extract IOCs (IPs, domains, URLs, hashes, etc.)
4. Format predictions as JSON (see Prediction Format below)
5. Evaluate predictions against ground truth

### Ground Truth (`data/IoCs.csv`)

The ground truth file is a CSV file where:
- **First column**: Source (article URL or identifier) - matches the source field in predictions
- **Subsequent columns**: IOC values (one per column)

**Format:**
```csv
source_url,ioc1,ioc2,ioc3,...
https://example.com/article1,192.168.1.1,malicious-domain.com,abc123def456...
https://example.com/article2,10.0.0.1,evil-site.net,789xyz...
```

**Example row:**
```csv
https://www.cloudsek.com/blog/...,67d9b4b35c02a19ab364ad19e1972645eb98e24dcd6f1715d2a26229deb2ccf5,e92707537fe99713752f3d3f479fa68a0c8dd80439c13a2bb4ebb36a952b63fd,...
```

Each row corresponds to one article/source, with all expected IOCs listed in the subsequent columns. Empty cells are allowed (some articles may have fewer IOCs).

### Prediction Format

Predictions must be provided as a JSON file containing an array of objects. Each object represents one extracted IOC and must have two fields:

- `source`: The article URL or identifier (must match the source in ground truth CSV)
- `value`: The extracted IOC value

**Format:**
```json
[
  {
    "source": "https://www.cloudsek.com/blog/...",
    "value": "67d9b4b35c02a19ab364ad19e1972645eb98e24dcd6f1715d2a26229deb2ccf5"
  },
  {
    "source": "https://www.cloudsek.com/blog/...",
    "value": "e92707537fe99713752f3d3f479fa68a0c8dd80439c13a2bb4ebb36a952b63fd"
  },
  {
    "source": "https://example.com/article",
    "value": "192.168.1.1"
  }
]
```

See `example/prediction/manual_ioc_predictions.json` for a complete example.

## IOC Normalization

Before evaluation, both ground truth and predicted IOCs undergo normalization to handle obfuscation and formatting variations commonly found in CTI articles. The normalization process applies the following rules:

1. **Remove brackets**: `[` and `]` are removed
2. **Replace obfuscated protocols**: 
   - `hxxp` → `http`
   - `hxxps` → `https`
3. **Replace obfuscated dots**: `[.]` → `[]` (note: this creates an empty string, effectively removing the pattern)
4. **Extract primary value**: Split on ` - ` and take the first part (removes descriptions/annotations)
5. **Normalize whitespace**: Strip leading/trailing whitespace
6. **Case normalization**: Convert to lowercase for matching

**Examples:**
- `hxxps://accessservicesonline[.]com/setup_wm.exe` → `https://accessservicesonline.com/setup_wm.exe`
- `31.172.83[.]162:443` → `31.172.83162:443` (after `[.]` → `[]` replacement)
- `api.telegram.org - C2 server` → `api.telegram.org`

## Evaluation Metrics

### Matching Logic

The evaluation uses **substring matching** (case-insensitive) to determine if a predicted IOC matches a ground truth IOC:

- A prediction is considered a **True Positive (TP)** if `pred.lower() in gt.lower()` for any ground truth IOC from the same source
- A prediction is a **False Positive (FP)** if it doesn't match any ground truth IOC from the same source
- A ground truth IOC is a **False Negative (FN)** if no prediction matches it (i.e., `not any(pred.lower() in gt.lower() for pred in predictions)`)

### Metrics Calculation

The evaluation computes **micro-averaged** precision and recall across all sources:

- **Precision**: `TP / (TP + FP)` - Measures the accuracy of predicted IOCs
- **Recall**: `TP / (TP + FN)` - Measures the completeness of extraction

**Important Notes:**
- Recall is calculated against **all** IOCs in the ground truth CSV, even if you only predict for a subset of sources
- If you only predict IOCs for a subset of articles, recall will be low because every unpredicted IOC from other articles is treated as a false negative
- For accurate recall measurement, predictions should cover all sources present in the ground truth file

## Usage

### Command-Line Interface

The evaluation script `eval/eval_ioc.py` provides a command-line interface:

```bash
python eval/eval_ioc.py --dataset data/IoCs.csv --prediction prediction/predictions.json
```

**Arguments:**
- `--dataset` (required): Path to the ground truth CSV file
- `--prediction` (required): Path to the prediction JSON file

**Example:**
```bash
cd benchmark/stage3_ti_drafting/ioc
python eval/eval_ioc.py \
    --dataset data/IoCs.csv \
    --prediction example/prediction/manual_ioc_predictions.json
```

**Output:**
```
Overall Metrics for example/prediction/manual_ioc_predictions.json:
Overall Precision: 0.8000
Overall Recall: 0.6667
```

### Python API

You can also use the evaluation function directly in Python:

```python
from eval.eval_ioc import test

# Run evaluation
test(
    ground_truth_file="data/IoCs.csv",
    pred_file="prediction/predictions.json"
)
```

The function prints precision and recall metrics to stdout.

### Example Test Script

The `example/simple_test.py` script demonstrates a simple evaluation workflow:

```bash
cd benchmark/stage3_ti_drafting/ioc/example
python simple_test.py
```

Or with custom paths:

```bash
python simple_test.py \
    --dataset ../data/IoCs.csv \
    --prediction prediction/my_predictions.json
```

This script:
1. Reads the second row from `IoCs.csv`
2. Generates sample predictions (4 correct IOCs + 1 false positive)
3. Saves predictions to a JSON file
4. Runs the evaluation

## Complete Workflow Example

Here's a step-by-step example of the complete IOC extraction and evaluation workflow:

### Step 1: Load Input Articles

```python
import json

# Load CTI articles
with open("data/blogs.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

# Process each article
for article in articles:
    article_url = article.get("url")  # or article.get("source")
    article_text = article.get("text")  # or article.get("content")
    # ... extract IOCs from article_text ...
```

### Step 2: Extract IOCs

Run your IOC extraction pipeline on each article. This could involve:
- Regular expression matching
- Named entity recognition (NER)
- Machine learning models
- LLM-based extraction
- Rule-based parsers

### Step 3: Format Predictions

```python
predictions = []

# For each extracted IOC
for article_url, extracted_iocs in your_results.items():
    for ioc_value in extracted_iocs:
        predictions.append({
            "source": article_url,
            "value": ioc_value
        })

# Save predictions
with open("predictions.json", "w", encoding="utf-8") as f:
    json.dump(predictions, f, ensure_ascii=False, indent=2)
```

### Step 4: Run Evaluation

```bash
python eval/eval_ioc.py \
    --dataset data/IoCs.csv \
    --prediction predictions.json
```

### Step 5: Interpret Results

- **High Precision, Low Recall**: Your system is accurate but misses many IOCs
- **Low Precision, High Recall**: Your system finds most IOCs but includes many false positives
- **High Precision, High Recall**: Optimal performance

## Dependencies

The evaluation script requires:

- **pandas**: For CSV file reading
- **json**: Standard library for JSON file handling
- **argparse**: Standard library for command-line argument parsing
- **os, sys**: Standard library for file operations

Install dependencies:

```bash
pip install pandas
```

## Important Notes

1. **Source Matching**: The `source` field in predictions must exactly match the first column (source) in the ground truth CSV file. URL normalization or mismatches will result in false negatives.

2. **IOC Normalization**: The normalization rules are applied automatically during evaluation. Ensure your extraction pipeline handles obfuscated IOCs (e.g., `hxxp://`, `[.]`) appropriately, or let the normalization handle them.

3. **Substring Matching**: The evaluation uses substring matching, so partial matches are considered correct. For example, `api.telegram.org` matches `https://api.telegram.org/bot...`.

4. **Recall Calculation**: Recall includes all sources in the ground truth file. If you're only evaluating on a subset of articles, consider filtering the ground truth CSV accordingly, or be aware that recall will be calculated against the full dataset.

5. **Multiple IOCs per Source**: Both ground truth and predictions can contain multiple IOCs per source. The evaluation aggregates all IOCs per source before computing metrics.

6. **Case Sensitivity**: Matching is case-insensitive after normalization, so `API.TELEGRAM.ORG` and `api.telegram.org` are considered matches.

## Evaluation Script Details

The main evaluation logic is in `eval/eval_ioc.py`:

- **`test(ground_truth_file, pred_file)`**: Core evaluation function that:
  1. Loads and normalizes ground truth IOCs from CSV
  2. Loads and normalizes predicted IOCs from JSON
  3. Computes TP, FP, FN for each source
  4. Calculates micro-averaged precision and recall
  5. Prints results to stdout

- **`main()`**: Command-line entry point that:
  1. Parses command-line arguments
  2. Validates file existence
  3. Calls `test()` with provided paths
  4. Handles errors gracefully

## See Also

- `example/simple_test.py` - Example usage script
- `example/prediction/manual_ioc_predictions.json` - Sample prediction format
- `data/IoCs.csv` - Ground truth format reference
