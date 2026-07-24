from intent_classifier import classify_intent
from prompt_router import get_prompt_path
from utils import load_prompt

query = "My payment failed yesterday."

intent = classify_intent(query)

print(f"Intent: {intent}")

prompt = load_prompt(get_prompt_path(intent))

print("\nLoaded Prompt:\n")
print(prompt)