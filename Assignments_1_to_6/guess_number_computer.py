import random
from colorama import init, Fore, Style # type: ignore

# Initialize colorama for colored terminal output
init(autoreset=True)

def guess_the_number():
    print(Fore.CYAN + "\n🎮 Welcome to 'Guess the Number'!")
    print(Fore.YELLOW + "I'm thinking of a number between 1 and 100.")
    print(Fore.YELLOW + "Try to guess it in as few attempts as possible!\n")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input(Fore.WHITE + "🔢 Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print(Fore.BLUE + "📉 Too low! Try a higher number.\n")
            elif guess > number_to_guess:
                print(Fore.MAGENTA + "📈 Too high! Try a lower number.\n")
            else:
                print(Fore.GREEN + f"🎉 Correct! You guessed the number in {attempts} attempts.\n")
                break
        except ValueError:
            print(Fore.RED + "🚫 Invalid input! Please enter a number.\n")

def play_game():
    while True:
        guess_the_number()
        again = input(Fore.CYAN + "🔁 Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print(Fore.GREEN + "\n👋 Thanks for playing! See you next time.\n")
            break

# Start the game
play_game()
