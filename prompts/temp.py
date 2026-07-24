from utils import load_prompt
from config import PROMPTS_DIR

print(load_prompt(PROMPTS_DIR / "refund.txt"))