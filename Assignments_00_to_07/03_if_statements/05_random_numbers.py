import random

# ANSI color codes for styling
GREEN = "\033[92m"
BLUE_BOLD_ITALIC = "\033[94m\033[1m\033[3m"
RESET = "\033[0m"
YELLOW = "\033[93m"
RED = "\033[91m"

def get_int_input(prompt):
    """Helper to get valid integer input."""
    while True:
        try:
            return int(input(f"{BLUE_BOLD_ITALIC}{prompt}{RESET}"))
        except ValueError:
            print(f"{RED}❌ Please enter a valid integer.{RESET}")

def main():
    print("🎲 Welcome to the Random Number Generator!")

    # User can specify range and quantity
    n_numbers = get_int_input("How many random numbers would you like to generate? ")
    min_val = get_int_input("Enter the minimum value: ")
    max_val = get_int_input("Enter the maximum value: ")

    if min_val > max_val:
        print(f"{YELLOW}⚠️ Swapping min and max because min > max.{RESET}")
        min_val, max_val = max_val, min_val

    print(f"\nGenerating {n_numbers} random numbers between {min_val} and {max_val}:\n")

    for i in range(n_numbers):
        value = random.randint(min_val, max_val)
        print(f"{GREEN}{value}{RESET}", end=' ')
    
    print("\n\n✅ Done!")

# Required call to main
if __name__ == '__main__':
    main()
