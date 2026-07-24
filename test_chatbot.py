from chatbot import SmartSupportChatbot

bot = SmartSupportChatbot()

prompt = bot.generate_prompt(
    "I paid twice for my subscription."
)

print(prompt)