import random

# ANSI styling
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def choose_difficulty():
    print(f"{BOLD}Choose a difficulty level:{RESET}")
    print("1. Easy (1–25)")
    print("2. Medium (1–50)")
    print("3. Hard (1–99)")

    while True:
        choice = input("Enter your choice (1/2/3): " + BLUE + BOLD + "")
        print(RESET, end="")
        if choice in ['1', '2', '3']:
            if choice == '1':
                return random.randint(1, 25), 25
            elif choice == '2':
                return random.randint(1, 50), 50
            else:
                return random.randint(1, 99), 99
        else:
            print(RED + "Please enter a valid option (1, 2, or 3)." + RESET)

def get_valid_guess(limit):
    while True:
        guess = input(f"Enter your guess (1–{limit}): " + BLUE + BOLD + "")
        print(RESET, end="")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= limit:
                return guess
            else:
                print(RED + f"❌ Please enter a number within 1–{limit}." + RESET)
        else:
            print(RED + "❌ Invalid input! Please enter a number." + RESET)

def play_game():
    secret_number, max_value = choose_difficulty()
    print(f"\nI'm thinking of a number between 1 and {max_value}...")
    
    attempts = 0
    hint_used = False

    while True:
        guess = get_valid_guess(max_value)
        attempts += 1

        if guess == secret_number:
            print(GREEN + f"🎉 Congrats! The number was {secret_number}." + RESET)
            print(YELLOW + f"You guessed it in {attempts} attempts!" + RESET)
            break
        elif guess < secret_number:
            print(RED + "Your guess is too low." + RESET)
        else:
            print(RED + "Your guess is too high." + RESET)

        # Offer a hint after 3 failed attempts
        if attempts == 3 and not hint_used:
            want_hint = input("Need a hint? (y/n): " + YELLOW + BOLD + "").lower()
            print(RESET, end="")
            if want_hint == 'y':
                if secret_number % 2 == 0:
                    print(YELLOW + "🔎 Hint: It's an even number!" + RESET)
                else:
                    print(YELLOW + "🔎 Hint: It's an odd number!" + RESET)
                hint_used = True

def main():
    print(f"{BOLD}🎮 Welcome to the Guess My Number Game! 🎮{RESET}\n")
    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): " + GREEN + BOLD + "").lower()
        print(RESET, end="")
        if again != 'y':
            print("\nThanks for playing! 👋")
            break

# Python boilerplate
if __name__ == '__main__':
    main()
