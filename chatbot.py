from intent_classifier import classify_intent
from prompt_router import get_prompt_path
from prompt_chain import build_prompt
from utils import load_prompt
from config import PROMPTS_DIR
from gemini_service import generate_response
from memory import ConversationMemory
from logger import log_conversation
from escalation import should_escalate



class SmartSupportChatbot:
    def __init__(self):
        self.memory = ConversationMemory()

    def chat(self, query: str):

        intent = classify_intent(query)

        system_prompt = load_prompt(
            PROMPTS_DIR / "system.txt"
        )

        specialist_prompt = load_prompt(
            get_prompt_path(intent)
        )

        final_prompt = build_prompt(
            system_prompt,
            specialist_prompt,
            query
        )

        response = generate_response(final_prompt)

        log_conversation(
    intent,
    query,
    response
)

        self.memory.add("user", query)
        self.memory.add("assistant", response)

        escalation = should_escalate(query)

        return {
    "intent": intent,
    "response": response,
    "history": self.memory.get_history(),
    "escalate": escalation
}
