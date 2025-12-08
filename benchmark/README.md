# CyberThreat-Eval Benchmark

This directory contains the evaluation framework for the CyberThreat-Eval benchmark, which assesses the capabilities of Large Language Models (LLMs) in cybersecurity threat intelligence tasks.

## Overview

The CyberThreat-Eval benchmark evaluates LLMs across three critical stages of threat intelligence processing:

1. **Stage 1: Triage** - Priority assignment and article classification
2. **Stage 2: Deep Search** - Related URL discovery and information value assessment
3. **Stage 3: TI Drafting** - Threat intelligence extraction and quality evaluation

Each stage focuses on different aspects of threat intelligence workflows, from initial triage to structured data extraction and contextual analysis.

## Directory Structure

```
benchmark/
├── README.md                    # This file
├── stage1_triage/               # Stage 1: Priority assignment evaluation
│   └── priority/
│       ├── README.md
│       ├── code/
│       └── data/
├── stage2_deep_search/          # Stage 2: Deep search evaluation
│   ├── README.md
│   ├── code/
│   ├── data/
│   └── example/
└── stage3_ti_drafting/          # Stage 3: Threat intelligence drafting
    ├── README.md
    ├── ioc/                     # IOC extraction evaluation
    ├── ttp/                     # TTP mapping evaluation
    └── score_evaluation/        # Quality scoring evaluation
```

## Evaluation Stages

### Stage 1: Triage

**Purpose**: Evaluate priority assignment for cybersecurity articles

**Task**: Classify articles into priority scores (1, 2, 3, or 5) based on subject matter and targeting characteristics.

**Key Features**:
- Two-step classification (subject matter + targeting)
- Priority score mapping (1=highest, 5=rejected)
- Comprehensive metrics (accuracy, precision, recall, confusion matrix)

**Documentation**: [stage1_triage/priority/README.md](stage1_triage/priority/README.md)

### Stage 2: Deep Search

**Purpose**: Evaluate the quality of related URLs found for cybersecurity articles

**Task**: Assess related URLs by analyzing their relationships and determining which URLs provide additional information beyond a reference URL.

**Key Features**:
- Reference relationship extraction
- PageRank-based reference URL identification
- LLM-based additional information assessment
- Aggregate metrics (average related URLs, additional info URLs, etc.)

**Documentation**: [stage2_deep_search/README.md](stage2_deep_search/README.md)

### Stage 3: TI Drafting

**Purpose**: Evaluate threat intelligence extraction and contextual analysis quality

**Tasks**:
1. **IOC Extraction**: Extract Indicators of Compromise (IPs, domains, URLs, hashes) from CTI articles
2. **TTP Mapping**: Extract MITRE ATT&CK Tactics, Techniques, and Procedures from articles
3. **Score Evaluation**: Assess quality of generated threat intelligence contexts (6-criteria scoring)

**Key Features**:
- Structured data extraction (IOC, TTP) with precision/recall metrics
- Contextual analysis quality assessment (Relevance, Accuracy, Comprehensiveness, Clarity, Coherence, Attribution)
- Comprehensive evaluation across multiple dimensions

**Documentation**: [stage3_ti_drafting/README.md](stage3_ti_drafting/README.md)

## Browsing Tasks

### Stage 1: Triage
```bash
cd stage1_triage/priority
# See README.md for detailed usage
```

### Stage 2: Deep Search
```bash
cd stage2_deep_search
```

### Stage 3: TI Drafting

**IOC Extraction**:
```bash
cd stage3_ti_drafting/ioc
```

**TTP Mapping**:
```bash
cd stage3_ti_drafting/ttp
```

**Score Evaluation**:
```bash
cd stage3_ti_drafting/score_evaluation
```

## Evaluation Flow

The three stages represent a typical threat intelligence processing pipeline:

1. **Triage** → Filter and prioritize articles based on urgency and importance
2. **Deep Search** → Find and assess related sources for additional context
3. **TI Drafting** → Extract structured intelligence (IOCs, TTPs) and generate quality analysis

Each stage can be evaluated independently, but together they provide a comprehensive assessment of LLM capabilities in threat intelligence workflows.

## Detailed Documentation

For detailed documentation on each stage, see:

- **Stage 1**: [stage1_triage/priority/README.md](stage1_triage/priority/README.md)
- **Stage 2**: [stage2_deep_search/README.md](stage2_deep_search/README.md)
- **Stage 3**: [stage3_ti_drafting/README.md](stage3_ti_drafting/README.md)
  - IOC: [stage3_ti_drafting/ioc/README.md](stage3_ti_drafting/ioc/README.md)
  - TTP: [stage3_ti_drafting/ttp/README.md](stage3_ti_drafting/ttp/README.md)
  - Score Evaluation: [stage3_ti_drafting/score_evaluation/README.md](stage3_ti_drafting/score_evaluation/README.md)

## Notes

- Each stage is self-contained with its own evaluation scripts and data
- All stages support both command-line and Python API usage
- Evaluation metrics and methodologies are documented in each stage's README
- Dependencies and setup instructions are provided in individual stage documentation
