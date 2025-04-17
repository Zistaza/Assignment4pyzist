import random

# Constants
PROMPT: str = "What do you want? "
JOKES = [
    "🤣 Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs' 😂",
    "😂 Why did the Python developer go broke? Because he couldn’t handle exceptions! 🤣",
    "🤣 Why do Java developers wear glasses? Because they don’t see sharp. 😂",
    "😂 I told my computer I needed a break, and now it won’t stop sending me KitKat ads. 🤣",
    "🤣 Why did the database break up with the application? Too many queries. 😂"
]
SORRY: str = "Sorry I only tell jokes 😅"

# ANSI escape code for blue text
BLUE = "\033[94m"
RESET = "\033[0m"

def main():
    while True:
        print(PROMPT, end="")
        user_input = input(f"{BLUE}").strip()
        print(RESET, end="")  # Reset color after input

        lower_input = user_input.lower()

        if lower_input == "joke":
            print(random.choice(JOKES))
        elif lower_input == "exit":
            print("Goodbye! 👋")
            break
        else:
            print(SORRY)

# Required to call the main function
if __name__ == '__main__':
    main()
