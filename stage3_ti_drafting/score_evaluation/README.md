# Score Evaluation Framework

This directory contains the evaluation framework for scoring the quality of generated threat intelligence contexts, including threat actor analysis and root cause analysis.

## Overview

The Score Evaluation framework evaluates how well Large Language Models (LLMs) generate contextual information for cybersecurity articles. The evaluation uses a comprehensive 6-criteria scoring system to assess the quality of generated contexts across multiple dimensions.

**Evaluation Criteria:**
- **Relevance**: How closely the generated context aligns with the original article
- **Accuracy**: Factual correctness of the generated context
- **Comprehensiveness**: Extent to which the context covers all critical details
- **Clarity**: How clear and understandable the context is
- **Coherence**: Logical flow and consistency of the context
- **Attribution**: Proper citation and source attribution

Each criterion is scored on a scale of 1-5, with 5 being the highest quality.

## Directory Structure

```
score_evaluation/
├── README.md                    # This file
├── data/                        # Original data files
│   └── 0330-articles-with-rejected-score.json  # Evaluation dataset
├── eval/                        # Evaluation tools
│   ├── __init__.py             # Module exports
│   ├── evaluation_runner.py    # Generic evaluation runner
│   ├── threat_actor.py         # Threat actor evaluation
│   ├── root_cause.py           # Root cause evaluation
│   └── utils.py                # Utility functions
├── example/                     # Example files
│   ├── simple_test.py          # Example test script
│   ├── test_input.json         # Example input file
│   └── test_output/            # Example output directory


```

## Files

### Original Data Files

#### `data/0330-articles-with-rejected-score.json`

The main evaluation dataset containing cybersecurity articles with generated contexts to be evaluated.

**Format**: JSON array of article objects

```json
[
    {
        "id": 18525912,
        "url": "https://example.com/article",
        "System.Description": "Original article description...",
        "baseline_threat_actor_context": "Generated threat actor context...",
        "baseline_root_cause_context": "Generated root cause context..."
    }
]
```

**Key Fields**:
- `id` (int): Unique article identifier
- `url` (str): Article URL
- `System.Description` (str): **Required**. Original article content/description
- `baseline_threat_actor_context` (str): Generated threat actor context (for threat actor evaluation)
- `baseline_root_cause_context` (str): Generated root cause context (for root cause evaluation)

**Note**: The context fields (`baseline_threat_actor_context` or `baseline_root_cause_context`) must be present in the input data for the respective evaluation tasks.

### Evaluation Tools

#### `eval/evaluation_runner.py`

Generic evaluation runner that processes articles and evaluates generated contexts.

**Main Function**: `run_evaluation()`

**Parameters**:
- `model_name`: LLM model name for evaluation
- `input_json`: Path to input JSON file
- `output_dir`: Directory to save output files
- `evaluate_function`: Evaluation function (e.g., `evaluate_actor_context` or `evaluate_root_cause_context`)
- `content_field`: Field name containing article content (default: `"System.Description"`)
- `context_field_name`: Field name containing generated context to evaluate
- `evaluation_field_name`: Name for evaluation scores field in output
- `average_field_name`: Name for average score field in output
- `use_azure`: Whether to use Azure OpenAI (default: True)
- `api_key`: OpenAI API key (when `use_azure=False`)
- `api_base`: OpenAI API base URL (when `use_azure=False`)

**Returns**: Dictionary containing overall average scores

#### `eval/threat_actor.py`

Threat actor context evaluation module.

**Evaluation Function**: `evaluate_actor_context(client, model, original_article, generated_context)`

Evaluates the quality of generated threat actor contexts by comparing them against original articles. Uses LLM-based evaluation with detailed scoring criteria.

**Command-line Interface**:
```bash
python eval/threat_actor.py --model <model_name> [options]
```

**Options**:
- `--model` (required): Model name (e.g., `gpt-4o`, `o3-mini`)
- `--input`: Input JSON file path (default: `score_evaluation/data/0330-articles-with-rejected-score.json`)
- `--output-dir`: Output directory (default: `score_evaluation/description`)
- `--context-field`: Field name containing generated context (default: `baseline_threat_actor_context`)
- `--use-azure`: Use Azure OpenAI (default: True)
- `--api-key`: OpenAI API key (when not using Azure)
- `--api-base`: OpenAI API base URL (when not using Azure)

#### `eval/root_cause.py`

Root cause context evaluation module.

**Evaluation Function**: `evaluate_root_cause_context(client, model, original_article, generated_context)`

Evaluates the quality of generated root cause contexts by comparing them against original articles. Uses LLM-based evaluation with detailed scoring criteria.

**Command-line Interface**:
```bash
python eval/root_cause.py --model <model_name> [options]
```

**Options**:
- `--model` (required): Model name (e.g., `gpt-4o`, `o3-mini`)
- `--input`: Input JSON file path (default: `score_evaluation/data/0330-articles-with-rejected-score.json`)
- `--output-dir`: Output directory (default: `score_evaluation/root_cause`)
- `--context-field`: Field name containing generated context (default: `baseline_root_cause_context`)
- `--use-azure`: Use Azure OpenAI (default: True)
- `--api-key`: OpenAI API key (when not using Azure)
- `--api-base`: OpenAI API base URL (when not using Azure)

#### `eval/utils.py`

Common utility functions used across evaluation scripts.

**Functions**:
- `api_call(client, messages, model_name, json_enabled=True)`: Generic API call wrapper with retry logic
- `get_client(model_name, use_azure=True, api_key=None, api_base=None)`: Create Azure OpenAI or OpenAI client
- `calculate_average_score(evaluation_dict)`: Calculate average score from evaluation dictionary
- `calculate_average_score_for_criteria(total_scores, num_entries)`: Calculate average scores per criterion

### Example Files

#### `example/simple_test.py`

Example test script demonstrating how to use the evaluation framework.

**Features**:
- Loads articles from input file
- Generates simulated contexts
- Runs evaluation using the API
- Displays results

**Usage**:
```bash
cd example
python simple_test.py [--input <input_file>] [--output-dir <output_dir>] [--model <model>] [options]
```

## Evaluation Tasks

### Task 1: Threat Actor Evaluation

Evaluates the quality of generated threat actor contexts extracted from cybersecurity articles.

#### Input Format

JSON file containing articles with threat actor contexts:

```json
[
    {
        "id": 18525912,
        "url": "https://example.com/article",
        "System.Description": "Original article description...",
        "baseline_threat_actor_context": "Generated threat actor summary including aliases, motivations, tactics, etc."
    }
]
```

**Required Fields**:
- `System.Description`: Original article content
- `baseline_threat_actor_context`: Generated threat actor context to evaluate

#### Output Format

JSONL file (one JSON object per line):

```json
{"id": 18525912, "url": "...", "description": "...", "baseline_threat_actor_context": "...", "baseline_evaluation": {"Relevance": 4, "Accuracy": 5, ...}, "baseline_average": 4.5}
{"id": 18528054, ...}
{"overall_baseline_average": {"Relevance": 4.2, "Accuracy": 4.5, ...}}
```

**Output Fields**:
- `id`: Article ID
- `url`: Article URL
- `description`: Original article description
- `baseline_threat_actor_context`: Generated context that was evaluated
- `baseline_evaluation`: Dictionary with scores for each criterion (1-5)
- `baseline_average`: Average score across all criteria
- `overall_baseline_average`: Overall averages across all articles (last line)

#### Usage

**Command-line**:
```bash
python eval/threat_actor.py --model gpt-4o --input data/0330-articles-with-rejected-score.json --output-dir results/
```

**Python API**:
```python
from eval.evaluation_runner import run_evaluation
from eval.threat_actor import evaluate_actor_context

run_evaluation(
    model_name="gpt-4o",
    input_json="data/0330-articles-with-rejected-score.json",
    output_dir="results/",
    evaluate_function=evaluate_actor_context,
    content_field="System.Description",
    context_field_name="baseline_threat_actor_context",
    evaluation_field_name="baseline_evaluation",
    average_field_name="baseline_average",
    use_azure=True
)
```

### Task 2: Root Cause Evaluation

Evaluates the quality of generated root cause contexts that explain how malware/tools contribute to security incidents.

#### Input Format

JSON file containing articles with root cause contexts:

```json
[
    {
        "id": 18525912,
        "url": "https://example.com/article",
        "System.Description": "Original article description...",
        "baseline_root_cause_context": "Generated root cause analysis explaining malware's role in the incident..."
    }
]
```

**Required Fields**:
- `System.Description`: Original article content
- `baseline_root_cause_context`: Generated root cause context to evaluate

#### Output Format

JSONL file (same format as threat actor evaluation):

```json
{"id": 18525912, "url": "...", "description": "...", "baseline_root_cause_context": "...", "baseline_evaluation": {"Relevance": 4, "Accuracy": 5, ...}, "baseline_average": 4.5}
{"overall_baseline_average": {"Relevance": 4.2, "Accuracy": 4.5, ...}}
```

#### Usage

**Command-line**:
```bash
python eval/root_cause.py --model gpt-4o --input data/0330-articles-with-rejected-score.json --output-dir results/
```

**Python API**:
```python
from eval.evaluation_runner import run_evaluation
from eval.root_cause import evaluate_root_cause_context

run_evaluation(
    model_name="gpt-4o",
    input_json="data/0330-articles-with-rejected-score.json",
    output_dir="results/",
    evaluate_function=evaluate_root_cause_context,
    content_field="System.Description",
    context_field_name="baseline_root_cause_context",
    evaluation_field_name="baseline_evaluation",
    average_field_name="baseline_average",
    use_azure=True
)
```

## Complete Example

### Example: Threat Actor Evaluation

This example demonstrates the full evaluation workflow using the example files.

#### Step 1: Input File (`example/test_input.json`)

```json
[
    {
        "id": 18525912,
        "url": "https://www.recordedfuture.com/blog/apache-tomcat-cve-2025-24813-vulnerability-analysis",
        "System.Description": "Researchers at Insikt Group have identified a critical path equivalence vulnerability...",
        "generated_context": "Simulated threat actor summary #1. Key points: Researchers at Insikt Group..."
    }
]
```

#### Step 2: Run Evaluation

**Using command line**:
```bash
python eval/threat_actor.py \
    --model gpt-4o \
    --input example/test_input.json \
    --output-dir example/test_output \
    --context-field generated_context \
    --use-azure
```

**Using Python API**:
```python
from eval.evaluation_runner import run_evaluation
from eval.threat_actor import evaluate_actor_context

run_evaluation(
    model_name="gpt-4o",
    input_json="example/test_input.json",
    output_dir="example/test_output",
    evaluate_function=evaluate_actor_context,
    content_field="System.Description",
    context_field_name="generated_context",
    evaluation_field_name="evaluation",
    average_field_name="average_score",
    use_azure=False,
    api_key="your-api-key",
    api_base="https://api.openai.com/v1"
)
```

#### Step 3: Output File (`example/test_output/gpt-4o.json`)

```json
{"id": 18525912, "url": "...", "description": "...", "generated_context": "...", "evaluation": {"Relevance": 2, "Accuracy": 2, "Comprehensiveness": 1, "Clarity": 3, "Coherence": 3, "Attribution": 1}, "average_score": 2.0}
{"id": 18528054, "url": "...", "description": "...", "generated_context": "...", "evaluation": {"Relevance": 2, "Accuracy": 2, "Comprehensiveness": 2, "Clarity": 3, "Coherence": 3, "Attribution": 1}, "average_score": 2.17}
{"overall_baseline_average": {"Relevance": 2.33, "Accuracy": 2.33, "Comprehensiveness": 1.67, "Clarity": 3.0, "Coherence": 3.0, "Attribution": 1.33}}
```

## Dependencies

Required Python packages:

```bash
pip install openai azure-identity tiktoken tenacity tqdm
```

**Python imports**:
```python
import json
import os
from openai import AzureOpenAI, OpenAI
from azure.identity import DefaultAzureCredential
import tiktoken
from tenacity import retry, stop_after_attempt, wait_random_exponential
from tqdm import tqdm
```

## Environment Variables

For Azure OpenAI:
- `LOCAL_ENDPOINT`: Azure endpoint URL
- `PROXY_KEY`: API key for proxy authentication

For OpenAI API:
- `OPENAI_API_KEY`: OpenAI API key (optional, can be passed via `--api-key`)
- `OPENAI_API_BASE`: OpenAI API base URL (optional, defaults to `https://api.openai.com/v1`)

## Notes

- The evaluation uses **LLM-based scoring**: An LLM evaluates the generated context against the original article
- Output files use **JSONL format**: One JSON object per line, making it easy to process large datasets
- The last line of output files contains overall averages across all articles
- Both evaluation tasks use the same 6-criteria scoring system
- Evaluation results are saved as `{model_name}.json` in the specified output directory
