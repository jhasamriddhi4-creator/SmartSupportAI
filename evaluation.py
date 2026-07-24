"""
evaluation.py
Evaluates the quality of AI responses.
"""

def evaluate_response(result):
    """
    Returns a simple quality score (0-100)
    based on response length, intent detection,
    and response structure.
    """

    response = result.get("response", "")
    intent = result.get("intent", "")

    score = 0

    if len(response) > 100:
        score += 40

    if intent:
        score += 30

    if "Problem Summary" in response:
        score += 30

    return score