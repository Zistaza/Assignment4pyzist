def double(num: float) -> float:
    """Returns the number multiplied by 2."""
    return num * 2

def get_number_from_user():
    """Prompts the user for a number until valid input is given."""
    while True:
        user_input = input("Enter a number: ")
        try:
            return float(user_input)
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

def main():
    print("✨ Welcome to the Doubler Program! ✨")
    
    while True:
        num = get_number_from_user()
        doubled = double(num)
        
        # Green color ANSI: \033[92m ; Reset: \033[0m
        print(f"\033[94mDouble of {num} is\033[0m \033[92m{doubled}\033[0m")

        again = input("Would you like to double another number? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("👋 Goodbye! Thanks for using the Doubler Program.")
            break

if __name__ == '__main__':
    main()
