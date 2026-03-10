# CyberThreat-Eval Benchmark

[![TMLR](https://img.shields.io/badge/arXiv-TMLR-b31b1b)](https://openreview.net/forum?id=tiFtZHwr7O)
[![Huggingface](https://img.shields.io/badge/🤗%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/xse/CyberThreat-Eval)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

This repo is the dataset of the TMLR paper CyberThreat-Eval: Can Large Language Models Automate Real-World Threat Research?[![TMLR](https://img.shields.io/badge/arXiv-TMLR-b31b1b)](https://openreview.net/forum?id=tiFtZHwr7O)

## What’s included
- **Stage 1: Triage** — Priority assignment for CTI articles.
- **Stage 2: Deep Search** — Quality of related URLs and additional info beyond a reference URL.
- **Stage 3: TI Drafting** — IOC/TTP extraction and analytical quality scoring.

## Directory map
```
.
├── README.md
├── stage1_triage/
│   └── priority/...
├── stage2_deep_search/
│   ├── code/...
│   ├── data/...
│   └── example/...
└── stage3_ti_drafting/
    ├── ioc/...
    ├── ttp/...
    └── score_evaluation/...
```

## Quick install
Run from the repo root:

Stage 1 (Triage) deps  
   ```
   cd stage1_triage/priority
   pip install numpy scikit-learn tqdm
   cd ../..
   ```

Stage 2 (Deep Search) deps + browser runtime  
   ```
   cd stage2_deep_search
   pip install networkx openai azure-identity playwright playwright-stealth tqdm tenacity tiktoken
   python -m playwright install  # installs Chromium for scraping
   cd ..
   ```

Stage 3 (TI Drafting) deps  
   ```
   cd stage3_ti_drafting
   pip install pandas json5 openai tqdm
   cd ..
   ```

API keys
   ```
   export OPENAI_API_KEY=<your_key>
   # Optional: export OPENAI_API_BASE=https://api.openai.com/v1  # or your Azure/OpenAI endpoint
   ```

Datasets are already under each stage’s `data/` directory; no extra download needed for basic tests.

## Quick tests (minimal commands)
- **Stage 1: Triage (priority scoring)**
  ```
  cd stage1_triage/priority
  python code/eval.py \
    --ground_truth data/0314-articles.json \
    --predictions predictions.json \
    --article_type article \
    --output results.json
  ```

- **Stage 2: Deep Search (related URL quality)**  
  Requires your generated result files (`*_results.json`) with related URLs per article.
  ```
  cd stage2_deep_search
  python code/eval.py \
    --results_dir <path_to_results_dir> \
    --output_dir similarity_analyses \
    --test_model_name gpt-4o \
    --api_key $OPENAI_API_KEY \
    --api_base https://api.openai.com/v1 \
    --workers 4
  ```

- **Stage 3: TI Drafting**
  - IOC extraction
    ```
    cd stage3_ti_drafting/ioc
    python eval/eval_ioc.py \
      --dataset data/IoCs.csv \
      --prediction example/prediction/manual_ioc_predictions.json
    ```
  - TTP mapping
    ```
    cd stage3_ti_drafting/ttp
    python eval/compute.py \
      --articles data/100-days-articles.json \
      --results example_predicted.json \
      --ttp-mapping data/TTP_Mapping.csv
    ```
  - Score evaluation (threat actor analysis)
    ```
    cd stage3_ti_drafting/score_evaluation
    python eval/threat_actor.py \
      --model gpt-4o \
      --input data/0330-articles-with-rejected-score.json \
      --output-dir output/
    ```
    For root cause scoring, use `eval/root_cause.py` with the same input/output pattern.



## Documentation links
- Stage 1: `stage1_triage/priority/README.md`
- Stage 2: `stage2_deep_search/README.md`
- Stage 3: `stage3_ti_drafting/README.md`
  - IOC: `stage3_ti_drafting/ioc/README.md`
  - TTP: `stage3_ti_drafting/ttp/README.md`
  - Score evaluation: `stage3_ti_drafting/score_evaluation/README.md`
