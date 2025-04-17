# ANSI escape codes for blue text (optional feature for styling user input)
BLUE = "\033[94m"
RESET = "\033[0m"

def print_ones_digit(num):
    """
    Takes an integer num and prints the ones digit (last digit) of that number.
    """
    ones_digit = num % 10  # Use modulo to get the ones digit
    print(f"The ones digit is {ones_digit}")

def main():
    while True:
        # Ask for user input with blue color
        try:
            num = int(input(f"Enter a number: {BLUE}"))  # User input in blue text
            print(RESET, end="")  # Reset color after input

            # Call the function to print the ones digit
            print_ones_digit(num)
            
            # Ask if the user wants to continue
            repeat = input("Would you like to enter another number? (y/n): ")
            if repeat.lower() != 'y':
                print("Thanks for using the program! Goodbye!")
                break  # Exit the loop if the user chooses not to continue
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Required at the end of Python file to call the main() function
if __name__ == '__main__':
    main()
