import random

def get_user_choice():
    choice = input("🧍 Choose rock, paper, or scissors: ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("🚫 Invalid choice! Try again.")
        choice = input("🧍 Choose rock, paper, or scissors: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    print(f"\n🧍 You chose: {user}")
    print(f"🤖 Computer chose: {computer}\n")

    if user == computer:
        return "😐 It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "🎉 You win!"
    else:
        return "💻 Computer wins!"

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = decide_winner(user_choice, computer_choice)
        print(result)

        again = input("\n🔁 Play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("👋 Thanks for playing!")
            break

# Run the game
play_game()
