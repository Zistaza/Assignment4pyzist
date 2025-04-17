import random

def computer_guess():
    print("🧠 Think of a number between 1 and 100.")
    input("🔒 Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        if low > high:
            print("😕 Something went wrong. Did you change your number?")
            break

        guess = random.randint(low, high)
        attempts += 1
        print(f"🤖 My guess is: {guess}")

        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").strip().lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"🎉 Yay! I guessed your number in {attempts} tries!\n")
            break
        else:
            print("🚫 Invalid input! Please enter H, L, or C.\n")

def play_game():
    while True:
        computer_guess()
        again = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for playing!")
            break

# Run the game
play_game()
