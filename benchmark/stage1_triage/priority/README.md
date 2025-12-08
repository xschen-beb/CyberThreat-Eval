# Stage 1: Triage

This directory contains the code and data for evaluating priority assignment in Stage 1 (Triage) of the CyberThreat-Eval benchmark. The priority assignment task involves classifying cybersecurity articles into priority scores (1, 2, 3, or 5) based on their subject matter and targeting characteristics.

## Overview

The priority assignment evaluation framework assesses how well Large Language Models (LLMs) can assign priority scores to cybersecurity articles. The priority score indicates the urgency and importance of an article:

- **Score 1**: Highest priority (e.g., APT activity, ransomware, data exfiltration)
- **Score 2**: High priority (e.g., certain vulnerability exploitations)
- **Score 3**: Medium priority (e.g., malware updates, defacement)
- **Score 5**: Rejected/Low priority (articles that should be filtered out)

The evaluation uses a two-step classification approach:
1. **Subject Matter Classification**: Categorize the article into one of 13 subject matter categories
2. **Targeting Classification**: Determine the targeting scope (e.g., Singular System, Multiple Countries, ICS)
3. **Priority Score Assignment**: Map the subject matter and targeting combination to a priority score using predefined rules

## Directory Structure

```
priority/
├── README.md                 # This file
├── code/                     # Implementation code
│   ├── reasoning_run.py      # Main script for running LLM-based priority assignment
│   └── eval.py               # Evaluation script for computing metrics
├── data/                     # Data files
│   ├── 0314-articles.json    # Ground truth dataset with articles and priority scores
│   └── priority_score.py    # Priority mapping rules (subject matter × targeting → score)
└── 0314-articles.json        # Symlink or copy of the dataset
```

## Data Format

### Input Data (`0314-articles.json`)

The dataset is a JSON array where each entry represents a cybersecurity article:

```json
{
    "id": 18440185,
    "state": "Rejected",
    "priority": null,
    "score": 5,
    "Cassandra.SourceIOCsExtracted": 0,
    "System.Description": "Article summary/description...",
    "Cassandra.SourceText": "Full article text content..."
}
```

**Fields:**
- `id`: Unique article identifier
- `score`: Ground truth priority score (1, 2, 3, or 5)
- `state`: Article state (e.g., "Rejected", "Sent to SPECTRE")
- `priority`: Priority level (may be null)
- `Cassandra.SourceText`: Full article content (used when `article_type='article'`)
- `System.Description`: Article description/summary (used when `article_type='description'`)

### Priority Mapping Rules (`data/priority_score.py`)

The priority score is determined by a two-dimensional mapping:
- **Subject Matter** (13 categories): Defacement/Spam, Mobile Malware, Malware Updates, New Malware, Vulnerability Exploitation (CVE < 9), Cryptominer/Resource Hijacking, Phishing Campaign, 0-Day Vulnerability Exploitation, Vulnerability Exploitation (CVE ≥ 9), APT/Threat Actor Activity, Persistent Backdoor/C2, Data Exfiltration, Ransomware
- **Targeting** (9 categories): Unknown/NA, Singular System, Singular Company, Singular Country, Multiple Countries, Industry/Sector, Platform/Service, Drive-by, ICS

Example mapping:
```python
"Phishing Campaign": {
    "Singular Country": 1,
    "Multiple Countries": 1,
    "Industry/Sector": 1,
    "Platform/Service": 1,
    "Unknown/NA": 2,
    "Singular System": 2,
    "Singular Company": 2,
    "Drive-by": 2,
    "ICS": 1
}
```

## Usage

### Priority Assignment Example with LLM

Use `code/reasoning_run.py` to run LLM-based priority assignment example

### Evaluating Predictions

#### Command-Line Interface

Use `code/eval.py` to evaluate prediction results from the command line:

```bash
python code/eval.py \
    --ground_truth data/0314-articles.json \
    --predictions predictions.json \
    --article_type article \
    --output results.json
```

**Arguments**:
- `--ground_truth` (optional, default: `data/0314-articles.json`): Path to ground truth JSON file containing articles
- `--predictions` (required): Path to predictions JSON file
- `--article_type` (optional, default: `article`): Type of article content to use
  - `article`: Use full article text (`Cassandra.SourceText`)
  - `description`: Use article description/summary (`System.Description`)
- `--output` (optional): Path to save evaluation results as JSON. If not provided, results are printed to stdout

**Example**:
```bash
# Basic usage
python code/eval.py --predictions my_predictions.json

# Use description instead of full article
python code/eval.py --predictions my_predictions.json --article_type description

# Save results to file
python code/eval.py --predictions my_predictions.json --output evaluation_results.json
```

#### Python API

You can also use the evaluation function directly in Python:

```python
from code.eval import gen_article_score_with_llms
import json

# Load ground truth data
with open("data/0314-articles.json", "r", encoding="utf-8") as f:
    data_dict = json.load(f)

# Load predictions (format: list of dicts with "id", "score", "llm_result")
pred_results = [
    {"id": 18440185, "score": 5, "llm_result": 1},
    {"id": 18439996, "score": 5, "llm_result": 2},
    # ... more predictions
]

# Run evaluation
results, combined_metrics = gen_article_score_with_llms(
    data_dict, 
    pred_results, 
    article_type="article"  # or "description"
)

# Save results
with open("evaluation_results.json", "w") as f:
    json.dump(combined_metrics, f, indent=4)
```

#### Predictions File Format

The predictions file must be a JSON array where each entry has the following format:

```json
[
    {
        "id": 18440185,
        "score": 5,
        "llm_result": 1
    },
    {
        "id": 18439996,
        "score": 5,
        "llm_result": 2
    }
]
```

**Required Fields**:
- `id`: Article identifier (must match `id` in ground truth)
- `score`: Ground truth score (1, 2, 3, or 5)
- `llm_result`: Predicted priority score (1, 2, 3, or 5)

## Evaluation Metrics

The evaluation framework computes multiple metrics:

### Overall Classification Metrics

- **Accuracy**: Overall classification accuracy
- **Precision (macro)**: Macro-averaged precision across all classes
- **Recall (macro)**: Macro-averaged recall across all classes
- **F1 Score (macro)**: Macro-averaged F1 score
- **Confusion Matrix**: 4×4 matrix for scores [1, 2, 3, 5]
- **Average Bias**: Mean absolute difference between predicted and ground truth scores

### Binary Classification Metrics (Accept vs. Reject)

- **Accept Category**: Scores 1, 2, 3 (articles to accept)
  - Correct rate: Percentage of accept predictions that are correct
  - Precision: TP / (TP + FP)
  - Recall: TP / (TP + FN)
  - Accuracy: Overall accuracy for accept group
  - Average Bias: Mean bias for accept group predictions

- **Reject Category**: Score 5 (articles to reject)
  - Correct rate: Percentage of reject predictions that are correct

### Per-Class Metrics

- **Average Bias per Class**: Mean bias for each priority score (1, 2, 3, 5)



## Notes

- The evaluation distinguishes between "Accept" (scores 1, 2, 3) and "Reject" (score 5) categories
- Bias is calculated as the absolute difference between predicted and ground truth scores
- The confusion matrix uses labels [1, 2, 3, 5] in that order
- Results are saved as JSON with numpy arrays converted to lists for serialization
