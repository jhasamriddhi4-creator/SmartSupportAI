import streamlit as st
from chatbot import SmartSupportChatbot
from evaluation import evaluate_response


# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="SmartSupport AI",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Session State
# ----------------------------

if "bot" not in st.session_state:
    st.session_state.bot = SmartSupportChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

    # ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.title("🤖 SmartSupport AI")

    st.success("🟢 Gemini Connected")

    st.markdown("---")

    st.subheader("Quick Questions")

    quick_questions = [
        "My payment failed",
        "I want a refund",
        "Track my order",
        "My application is crashing"
    ]

    selected_question = None

    for question in quick_questions:
        if st.button(question, use_container_width=True):
            selected_question = question

    st.markdown("---")

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.bot = SmartSupportChatbot()
        st.rerun()

        # ----------------------------
# Main Page
# ----------------------------

st.title("💬 SmartSupport AI")
st.caption("AI-Powered Customer Support Assistant")

# Display previous messages

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input

user_input = st.chat_input("Ask your question...")

# ----------------------------
# Handle Quick Questions
# ----------------------------

if selected_question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": selected_question
        }
    )

    with st.spinner("Thinking..."):
        result = st.session_state.bot.chat(selected_question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["response"]
        }
    )

    st.rerun()


# ----------------------------
# Handle User Input
# ----------------------------

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.spinner("Thinking..."):
        result = st.session_state.bot.chat(user_input)
        score = evaluate_response(result)
        st.progress(score / 100)
        st.caption(f"Response Quality Score: {score}/100")

    if result.get("escalate"):
        st.warning(
            "⚠️ This conversation should be escalated to a human support representative."
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["response"]
        }
    )

    

    st.rerun()