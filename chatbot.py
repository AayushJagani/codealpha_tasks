def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi there! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"

    elif user_input == "i am fine" or user_input == "i'm fine":
        return "Great to hear that!"

    elif user_input == "what is your name":
        return "I'm a simple chatbot made in Python!"

    elif user_input == "what can you do":
        return "I can chat with you! Try saying hello, asking how I am, or say bye."

    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that. Try: hello, how are you, bye."


def main():
    print("=" * 35)
    print("      Simple Python Chatbot")
    print("=" * 35)
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip() == "":
            print("Bot: Please type something!\n")
            continue

        response = get_response(user_input)
        print("Bot:", response)
        print()

        if user_input.lower().strip() in ["bye", "goodbye"]:
            break

main()