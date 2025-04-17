import random

# Sentence starters and random variations
SENTENCE_STARTS: list = [
    "Panaversity is fun. I learned to program and used Python to make my ",
    "Learning Python is great. I used it to make my ",
    "I had an amazing day at Panaversity where I made my "
]

def get_input(prompt: str) -> str:
    """Helper function to ensure valid input from the user."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Please provide a valid input.")

def main():
    # Get the three inputs from the user to make the adlib
    adjective: str = get_input("Please type an adjective and press enter: ")
    noun: str = get_input("Please type a noun and press enter: ")
    verb: str = get_input("Please type a verb and press enter: ")

    # Randomly select a sentence start
    sentence_start = random.choice(SENTENCE_STARTS)

    # Create and print the fun sentence with different colors for each part
    print(f"\033[92m{sentence_start}\033[0m", end="")  # Green for sentence start
    print(f"\033[94m{adjective}\033[0m", end=" ")      # Blue for adjective
    print(f"\033[95m{noun}\033[0m", end=" ")           # Magenta for noun
    print(f"\033[96m{verb}\033[0m!")                   # Cyan for verb

if __name__ == '__main__':
    main()
