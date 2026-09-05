"""
Basic Chatbot
CodeAlpha Python Programming Internship - Task 4

A simple rule-based chatbot that responds to a fixed set of
predefined user inputs with predefined replies.

Key Concepts Used: if-elif, functions, loops, input/output.
"""

import random


def get_response(user_input):
    """
    Return a chatbot reply based on simple keyword matching
    against the user's input.
    """
    text = user_input.lower().strip()

    # Greetings
    if text in ("hello", "hi", "hey"):
        return "Hi there! How can I help you today?"

    # How are you
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    # Name questions
    elif "your name" in text:
        return "I'm a simple rule-based chatbot built for the CodeAlpha internship!"

    # Thanks
    elif text in ("thanks", "thank you"):
        return "You're welcome!"

    # Help
    elif "help" in text:
        return "I can chat about simple things! Try saying hello, asking how I am, or saying bye."

    # What can you do
    elif "what can you do" in text:
        return "I can respond to greetings, simple questions, and say goodbye. I'm not very smart yet!"

    # Farewell -> handled separately in the main loop to end the conversation,
    # but included here too in case get_response is reused elsewhere.
    elif text in ("bye", "goodbye", "see you"):
        return "Goodbye! Have a great day!"

    # Fallback for anything not recognized
    else:
        return random.choice([
            "Sorry, I didn't understand that. Could you rephrase?",
            "I'm not sure how to respond to that yet.",
            "Can you try asking that a different way?"
        ])


def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' anytime to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ("bye", "goodbye", "see you"):
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()
