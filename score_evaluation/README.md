## Features

- Multi-model evaluation support
- Comprehensive scoring criteria including:
  - Relevance
  - Accuracy
  - Comprehensiveness
  - Clarity
  - Coherence
  - Attribution
- Detailed statistical analysis
- JSON-based result storage and processing

## Project Structure

```
score_evaluation/
├── cal.py                 # Main calculation script
├── search_engine.py      # Search functionality implementation
├── root_cause.py      # Root cause analysis implementation
└── threat_actor.py       # Threat actor analysis implementation
```

## Usage

1. Ensure all required dependencies are installed
2. Place evaluation results in the appropriate directories
3. Run the evaluation script:
   ```bash
    python threat_actor.py -model [model_name]
    python root_cause.py -model [model_name]
   ```
and calculation script:
   ```bash
   python cal.py
   ```

## Supported Models
- o3-mini
- gpt-4o
- gpt-4o-mini-2024-07-18-model_1_datasets_v01_no_sa_all_csf
- gpt-4o-2024-08-06-ti_prune2_1030
