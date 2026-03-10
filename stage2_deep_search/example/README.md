# Stage 2: Deep Search

This directory contains an example for Stage 2 (Deep Search) evaluation of the CyberThreat-Eval benchmark.

## Directory Structure

```
example/
├── README.md                        # This file
├── process_articles.py              # Main script: Generate related URLs
├── process_related_similarity.py    # Analyze related URLs
├── calculate_model_statistics.py    # Calculate statistics
├── llm.py                          # LLM integration utilities
├── 0510-articles.json              # Ground truth dataset
└── README.md (original)            # Original README
```

## Usage

### Step 1: Process Articles

```bash
python process_articles.py --json_file 0510-articles.json --output_dir processed_results --model gpt-4o
```

### Step 2: Analyze Related URLs

```bash
python process_related_similarity.py --results_dir processed_results --output_dir similarity_analyses
```

### Step 3: Calculate Statistics

```bash
python calculate_model_statistics.py
```

## Dataset

- **Ground truth**: `0510-articles.json`

## Dependencies

All Python files in this directory are in the same directory and use relative imports (`from llm import ...`).

For detailed documentation, see [STAGE2_DEEP_SEARCH.md](../STAGE2_DEEP_SEARCH.md).
