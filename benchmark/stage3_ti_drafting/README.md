# Stage 3: TI Drafting

This directory contains the code and data for Stage 3 (TI Drafting) evaluation of the CyberThreat-Eval benchmark. Stage 3 evaluates the ability of Large Language Models (LLMs) to extract structured threat intelligence from cybersecurity articles and generate high-quality contextual analysis.

## Overview

Stage 3 (TI Drafting) focuses on three critical aspects of threat intelligence generation:

1. **IOC Extraction**: Identifying and extracting Indicators of Compromise (IPs, domains, URLs, file hashes) from CTI articles
2. **TTP Mapping**: Extracting MITRE ATT&CK Tactics, Techniques, and Procedures from cybersecurity articles
3. **Score Evaluation**: Assessing the quality of generated threat intelligence contexts (threat actor analysis and root cause analysis)

These tasks evaluate different dimensions of threat intelligence drafting:
- **Structured Data Extraction** (IOC and TTP): Measures accuracy in identifying and extracting specific threat indicators
- **Contextual Analysis Quality** (Score Evaluation): Measures the quality of generated analytical contexts using a comprehensive 6-criteria scoring system

Together, these evaluations provide a comprehensive assessment of an LLM's capability to transform raw cybersecurity articles into actionable threat intelligence.

## Directory Structure

```
stage3_ti_drafting/
├── README.md                    # This file
├── ioc/                         # IOC extraction evaluation
│   ├── README.md                # Detailed IOC evaluation documentation
│   ├── data/                    # Data files
│   │   ├── blogs.json          # Input CTI articles
│   │   ├── IoCs.csv            # Ground truth IOC annotations
│   │   └── All Intelligence Feeds.csv
│   ├── eval/                    # Evaluation scripts
│   │   └── eval_ioc.py         # Main evaluation script
│   └── example/                 # Example scripts and sample data
│       ├── simple_test.py
│       └── prediction/
│           └── manual_ioc_predictions.json
├── ttp/                         # TTP mapping evaluation
│   ├── README.md                # Detailed TTP evaluation documentation
│   ├── data/                    # Data files
│   │   ├── 100-days-articles.json  # Articles with ground truth TTPs
│   │   └── TTP_Mapping.csv      # MITRE ATT&CK TTP ID to name mapping
│   ├── eval/                    # Evaluation scripts
│   │   └── compute.py          # Core evaluation functions
│   ├── example/                 # Example files for testing
│   │   ├── example_ground_truth.json
│   │   ├── example_predicted.json
│   │   └── simple_test.py
│   └── utils/                   # Utility functions
│       └── eval_ttps_utils.py
└── score_evaluation/            # Quality scoring evaluation
    ├── README.md                # Detailed score evaluation documentation
    ├── data/                    # Data files
    │   └── 0330-articles-with-rejected-score.json
    ├── eval/                    # Evaluation tools
    │   ├── evaluation_runner.py
    │   ├── threat_actor.py      # Threat actor evaluation
    │   ├── root_cause.py        # Root cause evaluation
    │   └── utils.py             # Utility functions
    └── example/                 # Example files
        ├── simple_test.py
        ├── test_input.json
        └── test_output/
```

## Evaluation Tasks

### Task 1: IOC Extraction (`ioc/`)

**Purpose**: Evaluate the ability to extract Indicators of Compromise (IOCs) from cybersecurity threat intelligence articles.

**What it evaluates**:
- Extraction of IP addresses, domains, URLs, and file hashes
- Handling of obfuscated IOCs (e.g., `hxxp://`, `[.]`)
- Normalization and matching accuracy

**Input**:
- CTI articles from `data/blogs.json`
- Ground truth IOCs from `data/IoCs.csv`

**Output**:
- JSON predictions with extracted IOCs (`source` and `value` fields)
- Micro-averaged precision and recall metrics

**Evaluation Metrics**:
- **Precision**: Accuracy of predicted IOCs
- **Recall**: Completeness of IOC extraction
- Uses substring matching (case-insensitive) after normalization

**Key Features**:
- Automatic IOC normalization (handles obfuscation patterns)
- Supports multiple IOC types (IPs, domains, URLs, hashes)
- Micro-averaged metrics across all sources

For detailed documentation, see [ioc/README.md](ioc/README.md).

### Task 2: TTP Mapping (`ttp/`)

**Purpose**: Evaluate the ability to extract MITRE ATT&CK Tactics, Techniques, and Procedures (TTPs) from cybersecurity articles.

**What it evaluates**:
- Identification of MITRE ATT&CK techniques in articles
- Correct mapping of TTP IDs to official technique names
- Validation against authoritative TTP mapping

**Input**:
- Articles with ground truth TTPs from `data/100-days-articles.json`
- TTP mapping file `data/TTP_Mapping.csv` (authoritative MITRE ATT&CK names)

**Output**:
- JSON predictions with extracted TTPs (TTP ID + description)
- Micro-averaged precision and recall metrics

**Evaluation Metrics**:
- **Precision**: Accuracy of extracted TTPs (validated against mapping)
- **Recall**: Completeness of TTP extraction
- **Validation**: TTP descriptions must match official MITRE names (case-insensitive)

**Key Features**:
- Validates extracted TTPs against `TTP_Mapping.csv`
- Rejects TTPs with description mismatches (counted as false positives)
- Supports JSON5 format for prediction files (allows comments)

For detailed documentation, see [ttp/README.md](ttp/README.md).

### Task 3: Score Evaluation (`score_evaluation/`)

**Purpose**: Evaluate the quality of generated threat intelligence contexts using a comprehensive multi-criteria scoring system.

**What it evaluates**:
- Quality of generated threat actor analysis
- Quality of generated root cause analysis
- Six dimensions of context quality

**Input**:
- Articles with generated contexts from `data/0330-articles-with-rejected-score.json`
- Contexts can be for threat actor analysis or root cause analysis

**Output**:
- JSONL file with scores for each article
- Overall average scores across all criteria

**Evaluation Criteria** (1-5 scale each):
- **Relevance**: Alignment with the original article
- **Accuracy**: Factual correctness
- **Comprehensiveness**: Coverage of critical details
- **Clarity**: Understandability
- **Coherence**: Logical flow and consistency
- **Attribution**: Proper citation and source attribution

**Key Features**:
- LLM-based evaluation (uses GPT-4o or other models)
- Supports both threat actor and root cause evaluation tasks
- JSONL output format (one evaluation per line)
- Aggregate statistics calculation

For detailed documentation, see [score_evaluation/README.md](score_evaluation/README.md).

## Quick Start Guide

### Which Task Should I Use?

- **IOC Extraction**: If you want to evaluate extraction of threat indicators (IPs, domains, URLs, hashes) from articles
- **TTP Mapping**: If you want to evaluate extraction of MITRE ATT&CK techniques from articles
- **Score Evaluation**: If you want to evaluate the quality of generated analytical contexts (threat actor or root cause analysis)

### Quick Links

- [IOC Extraction Documentation](ioc/README.md) - Complete guide for IOC extraction evaluation
- [TTP Mapping Documentation](ttp/README.md) - Complete guide for TTP extraction evaluation
- [Score Evaluation Documentation](score_evaluation/README.md) - Complete guide for quality scoring evaluation

## Usage

### IOC Extraction

```bash
cd ioc
python eval/eval_ioc.py \
    --dataset data/IoCs.csv \
    --prediction prediction/predictions.json
```

For more details, see [ioc/README.md](ioc/README.md).

### TTP Mapping

```bash
cd ttp
python eval/compute.py \
    --articles data/100-days-articles.json \
    --results predictions.json \
    --ttp-mapping data/TTP_Mapping.csv
```

For more details, see [ttp/README.md](ttp/README.md).

### Quality Scoring

#### Threat Actor Evaluation

```bash
cd score_evaluation
python eval/threat_actor.py \
    --model gpt-4o \
    --input data/0330-articles-with-rejected-score.json \
    --output-dir output/
```

#### Root Cause Evaluation

```bash
python eval/root_cause.py \
    --model gpt-4o \
    --input data/0330-articles-with-rejected-score.json \
    --output-dir output/
```

#### Calculate Aggregate Statistics

```bash
python cal.py  # Calculate aggregate statistics from multiple model outputs
```

For more details, see [score_evaluation/README.md](score_evaluation/README.md).

## Datasets

### IOC Extraction
- **Input Articles**: `ioc/data/blogs.json` - CTI articles in JSON format
- **Ground Truth**: `ioc/data/IoCs.csv` - IOC annotations (CSV: source, ioc1, ioc2, ...)

### TTP Mapping
- **Input Articles**: `ttp/data/100-days-articles.json` - Articles with ground truth TTPs
- **TTP Mapping**: `ttp/data/TTP_Mapping.csv` - Authoritative MITRE ATT&CK TTP ID to name mapping

### Score Evaluation
- **Input Data**: `score_evaluation/data/0330-articles-with-rejected-score.json` - Articles with generated contexts to evaluate

## Task Relationships

The three evaluation tasks assess different aspects of threat intelligence drafting:

1. **IOC and TTP Extraction** (Structured Data Extraction):
   - Focus on accuracy of extracting specific threat indicators
   - Use precision/recall metrics
   - Evaluate structured output generation

2. **Score Evaluation** (Contextual Analysis Quality):
   - Focus on quality of generated analytical contexts
   - Use multi-criteria scoring (1-5 scale)
   - Evaluate narrative and analytical content

Together, these tasks provide a comprehensive evaluation framework:
- **Extraction tasks** measure technical accuracy in identifying threat indicators
- **Scoring task** measures the quality of analytical insights and context generation

## Notes

- Each task is self-contained within its subdirectory with its own README
- All evaluation scripts support both command-line and Python API usage
- The TTP evaluation validates extracted TTPs against the authoritative MITRE ATT&CK mapping
- Score evaluation uses LLM-based assessment (requires API keys for OpenAI or Azure OpenAI)
- All tasks include example scripts in their respective `example/` directories

For detailed documentation on each task, see the README files in each subdirectory:
- [IOC Extraction](ioc/README.md)
- [TTP Mapping](ttp/README.md)
- [Score Evaluation](score_evaluation/README.md)

For additional context, see [STAGE3_TI_DRAFTING.md](../STAGE3_TI_DRAFTING.md).
