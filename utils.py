# utils.py

from pathlib import Path

def load_prompt(file_path: Path) -> str:
    """
    Load a prompt template from a text file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()