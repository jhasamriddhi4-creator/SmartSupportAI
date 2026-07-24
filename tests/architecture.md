                +---------------------+
                |      User           |
                +----------+----------+
                           |
                           v
                +---------------------+
                |   Streamlit UI      |
                +----------+----------+
                           |
                           v
                +---------------------+
                | Chatbot Controller  |
                +----------+----------+
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
 Intent Classifier   Prompt Router   Conversation Memory
          |                |
          +----------------+
                   |
                   v
            Prompt Chain
                   |
                   v
             Gemini API
                   |
                   v
      Evaluation + Escalation
                   |
                   v
             Final Response