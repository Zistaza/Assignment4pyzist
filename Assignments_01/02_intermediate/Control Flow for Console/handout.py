import random
import time
import threading
import sys

# Constants
NUM_ROUNDS: int = 5
MIN_VALUE: int = 1
MAX_VALUE: int = 100
TIME_LIMIT: int = 10

# Colored printing helper
def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# Timed input using threading
def input_with_timeout(prompt, timeout):
    result = None

    def get_input():
        nonlocal result
        try:
            result = input(prompt)
        except EOFError:
            result = None

    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    input_thread.join(timeout)

    if input_thread.is_alive():
        return None
    return result

# Game logic as a function (for restarting)
def play_game():
    print_colored("🎮 Welcome to the High-Low Game!", "1;32")
    name = input("Please enter your name: ")
    print_colored(f"👋 Hello, {name}!", "1;34")
    print("--------------------------------")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        player_number = random.randint(MIN_VALUE, MAX_VALUE)
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)

        print_colored(f"\n🌀 Round {round_num}", "1;36")
        print(f"Your number is {player_number}")

        guess = input_with_timeout(f"⏳ Do you think your number is higher or lower than the computer's? (You have {TIME_LIMIT} seconds): ", TIME_LIMIT)

        if guess is None:
            print_colored(f"⏰ Time Over! The computer's number was: {computer_number}", "1;31")
            print(f"Your score is still {score}")
            continue

        guess = guess.strip().lower()

        if guess == 'higher' and player_number > computer_number:
            print_colored(f"✅ You were right! The computer's number was {computer_number}", "1;32")
            score += 1
        elif guess == 'lower' and player_number < computer_number:
            print_colored(f"✅ You were right! The computer's number was {computer_number}", "1;32")
            score += 1
        else:
            print_colored(f"❌ Aww, that's incorrect. The computer's number was {computer_number}", "1;31")

        print(f"📊 Your score is now {score}")

    # Game over feedback
    print_colored("\n🎉 Thanks for playing!", "1;32")
    print(f"🏁 Your final score is: {score}")

    if score == NUM_ROUNDS:
        print_colored("🌟 Wow! You played perfectly! 🎯", "1;33")
    elif score >= NUM_ROUNDS // 2:
        print_colored("👍 Good job, you played really well! 👏", "1;33")
    else:
        print_colored("😕 Better luck next time!", "1;31")

    # Restart option
    while True:
        play_again = input("\n🔁 Would you like to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            print_colored("\n🔄 Restarting the game...\n", "1;36")
            time.sleep(1)
            play_game()  # Recursively restart
        elif play_again == "no":
            print_colored("\n👋 Exiting the game... See you next time!", "1;35")
            time.sleep(2)
            sys.exit()
        else:
            print_colored("❓ Please enter 'yes' or 'no'.", "1;33")

# Run the game
if __name__ == '__main__':
    play_game()
