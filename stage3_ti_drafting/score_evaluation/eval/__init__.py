"""
Evaluation module for scoring generated contexts.

This module provides:
- Common utilities (utils.py)
- Generic evaluation runner (evaluation_runner.py)
- Threat actor evaluation (threat_actor.py)
- Root cause evaluation (root_cause.py)
"""

from .utils import (
    api_call,
    calculate_average_score,
    calculate_average_score_for_criteria,
    get_client
)
from .evaluation_runner import run_evaluation

__all__ = [
    'api_call',
    'calculate_average_score',
    'calculate_average_score_for_criteria',
    'get_client',
    'run_evaluation',
]

