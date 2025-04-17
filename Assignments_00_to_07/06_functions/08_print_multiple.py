# ANSI escape codes for blue text to input blue text
BLUE = "\033[94m"
RESET = "\033[0m"

def print_multiple(message: str, repeats: int):
    """
    Prints the given message the specified number of times.
    """
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: " + BLUE)
    print(RESET, end="")  # Reset color after input
    repeats = int(input("Enter a number of times to repeat your message: " + BLUE))
    print(RESET, end="")  # Reset color after input
    print_multiple(message, repeats)

# Required at the end of Python file to call the main() function
if __name__ == '__main__':
    main()
