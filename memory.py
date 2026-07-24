# memory.py

class ConversationMemory:
    """
    Stores conversation history for the current session.
    """

    def __init__(self):
        self.history = []

    def add(self, role: str, message: str):
        self.history.append({
            "role": role,
            "message": message
        })

    def get_history(self):
        return self.history

    def clear(self):
        self.history.clear()

