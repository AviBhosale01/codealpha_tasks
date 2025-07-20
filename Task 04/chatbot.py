# Basic chatbot by Avishkar Bhosale 


from colorama import init, Fore, Style

# Initialize colorama for auto-reset
init(autoreset=True)

def print_intro():
    print(Fore.CYAN + Style.BRIGHT + "🤖 Welcome to ChatBuddy - Your Rule-Based Python Chatbot")
    print(Fore.YELLOW + "Type 'bye' or 'exit' anytime to end the chat.\n")

# Core dictionary of rule-based responses
def get_response(user_input):
    user_input = user_input.lower().strip()
    if user_input in ['hello', 'hi', 'hey']:
        return "Hi there! 👋"
    elif user_input in ['how are you', 'how are you doing']:
        return "I'm doing great, thanks! 😊"
    elif user_input in ['bye', 'exit']:
        return "Goodbye! 👋 Have a nice day!"
    elif user_input in ['what is your name', 'who are you']:
        return "I'm ChatBuddy – your simple Python chatbot. 🤖"
    elif user_input in ['help', 'commands']:
        return "Try saying: hello, how are you, what is your name, bye."
    else:
        return "I'm not sure how to respond to that 🤔 Try 'help'."

def chatbot_loop():
    print_intro()
    while True:
        user_input = input(Fore.WHITE + "You: ")

        response = get_response(user_input)
        print(Fore.GREEN + "Bot: " + response)

        if user_input.lower() in ['bye', 'exit']:
            break

if __name__ == "__main__":
    chatbot_loop()
