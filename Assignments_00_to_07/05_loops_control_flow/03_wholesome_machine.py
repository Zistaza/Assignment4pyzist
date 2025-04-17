import time

# Constant affirmation message
AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("🧠 Welcome to your daily affirmation session!")
    print("✨ Please type the following affirmation exactly as shown:")
    print(f"\n👉 {AFFIRMATION}\n")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == AFFIRMATION.lower():
            print("\n🎉 That's right! Never forget it.")
            time.sleep(1)
            repeat = input("\nWould you like to affirm again? (yes/no): ").lower()
            if repeat not in ["yes", "y"]:
                print("\n💖 Keep believing in yourself. You've got this!")
                break
            else:
                print("\nAlright! Let’s do it again.")
                time.sleep(1)
                print(f"\n👉 {AFFIRMATION}\n")
        else:
            print("\n🤔 Hmmm... That was not quite right.")
            print("Let’s try again. You are capable, let’s believe it together!")
            print(f"\n👉 {AFFIRMATION}\n")

# Required to call the main function
if __name__ == '__main__':
    main()
