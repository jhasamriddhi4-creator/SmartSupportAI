from chatbot import SmartSupportChatbot

bot = SmartSupportChatbot()

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    answer = bot.chat(query)

    print("\nSmartSupport AI:\n")

    print(answer)