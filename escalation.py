ESCALATION_KEYWORDS = [
    "lawsuit",
    "legal",
    "court",
    "fraud",
    "police",
    "angry",
    "manager",
    "human",
    "representative",
    "refund 10000",
    "chargeback"
]


def should_escalate(message: str):

    text = message.lower()

    for keyword in ESCALATION_KEYWORDS:
        if keyword in text:
            return True

    return False