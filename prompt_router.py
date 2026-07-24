# prompt_router.py

from config import PROMPTS_DIR

PROMPT_MAP = {
    "refund": PROMPTS_DIR / "refund.txt",
    "billing": PROMPTS_DIR / "billing.txt",
    "technical": PROMPTS_DIR / "technical.txt",
    "order": PROMPTS_DIR / "order.txt",
    "complaint": PROMPTS_DIR / "complaint.txt",
}

def get_prompt_path(intent: str):
    return PROMPT_MAP.get(intent, PROMPT_MAP["complaint"])
