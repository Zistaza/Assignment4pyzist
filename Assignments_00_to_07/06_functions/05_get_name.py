def get_name():
    return "Sophia"

def main():
    name = get_name()
    print("Howdy", name, "! 🤠")

    # Feature: Let user enter their own name optionally
    use_custom = input("Would you like me to greet you with your own name? (yes/no): ").strip().lower()
    if use_custom in ("yes", "y"):
        user_name = input("Enter your name: ").strip().title()
        print(f"Howdy {user_name}! 👋 Nice to meet you.")
    
    print("Have a great day! 🌞")

if __name__ == '__main__':
    main()
