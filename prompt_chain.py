# prompt_chain.py

from utils import load_prompt
from config import PROMPTS_DIR

def build_prompt(system_prompt: str,
                 specialist_prompt: str,
                 user_query: str) -> str:
    """
    Combines prompts into one instruction.
    """

    return f"""
{system_prompt}

--------------------------------

{specialist_prompt}

--------------------------------

Customer Query:

{user_query}

Provide the best customer support response.
"""