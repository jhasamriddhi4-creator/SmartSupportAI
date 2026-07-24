# intent_classifier.py

def classify_intent(query: str) -> str:
    """
    Classify the customer's intent.
    """

    text = query.lower()

    if any(word in text for word in ["refund", "money back", "return"]):
        return "refund"

    if any(word in text for word in ["payment", "charged", "invoice", "billing"]):
        return "billing"

    if any(word in text for word in ["error", "bug", "issue", "not working", "crash"]):
        return "technical"

    if any(word in text for word in ["order", "shipment", "delivery", "package"]):
        return "order"

    return "complaint"