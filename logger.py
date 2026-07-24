import json
from pathlib import Path
from datetime import datetime

LOG_FILE = Path("logs/conversations.json")


def log_conversation(intent, question, response):

    LOG_FILE.parent.mkdir(exist_ok=True)

    if LOG_FILE.exists():
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = []
    else:
        data = []

    data.append(
        {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "intent": intent,
            "question": question,
            "response": response
        }
    )

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)