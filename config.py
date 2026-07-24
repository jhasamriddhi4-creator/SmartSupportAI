# config.py

from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent

# Prompt folder
PROMPTS_DIR = BASE_DIR / "prompts"

# Log folder
LOGS_DIR = BASE_DIR / "logs"

# Confidence threshold for escalation
CONFIDENCE_THRESHOLD = 0.70