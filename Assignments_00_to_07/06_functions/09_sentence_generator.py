import random

# ANSI escape codes for blue text (optional feature for styling user input)
BLUE = "\033[94m"
RESET = "\033[0m"

def make_sentence(word, part_of_speech):
    """
    Takes a word and part of speech, and prints a sentence with the word inserted into the correct template.
    """
    if part_of_speech == 0:  # noun
        templates = [
            "I am excited to add this " + word + " to my vast collection of them!",
            "I can't wait to show off this " + word + " to all my friends!",
            "I bet this " + word + " will be the best thing in my collection!"
        ]
        print(random.choice(templates))  # Randomly choose a template for nouns

    elif part_of_speech == 1:  # verb
        templates = [
            "It's so nice outside today, it makes me want to " + word + "!",
            "Whenever I hear the word 'summer', I feel like I just want to " + word + "!",
            "On a lazy afternoon, I just want to sit back and " + word + "!"
        ]
        print(random.choice(templates))  # Randomly choose a template for verbs

    elif part_of_speech == 2:  # adjective
        templates = [
            "Looking out my window, the sky is big and " + word + "!",
            "The ocean looks so calm and " + word + " today.",
            "I love the " + word + " color of the sky at sunset!"
        ]
        print(random.choice(templates))  # Randomly choose a template for adjectives

    else:
        print("Part of speech must be 0, 1, or 2! Please try again.")  # Invalid input case

def main():
    while True:
        # Get user input
        word = input("Please type a noun, verb, or adjective: " + BLUE)
        print(RESET, end="")  # Reset color after input
        
        # Input validation for part_of_speech
        while True:
            try:
                part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: " + BLUE))
                print(RESET, end="")  # Reset color after input
                if part_of_speech in [0, 1, 2]:
                    break  # Exit loop if valid part of speech
                else:
                    print("Invalid input! Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input! Please enter an integer (0, 1, or 2).")

        # Generate and print the sentence
        make_sentence(word, part_of_speech)

        # Ask if the user wants to continue
        repeat = input("Would you like to enter another word? (y/n): ")
        if repeat.lower() != 'y':
            print("Thanks for playing! Goodbye!")
            break

# Required at the end of Python file to call the main() function
if __name__ == '__main__':
    main()
