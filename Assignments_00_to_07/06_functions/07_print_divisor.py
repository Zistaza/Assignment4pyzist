# ANSI escape code for blue color
BLUE = "\033[94m"
RESET = "\033[0m"

def print_divisors(num: int):
    """
    Prints all divisors of the given number.
    """
    print(f"Divisors of {num} are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

def main():
    try:
        user_input = int(input(f"Enter a number: {BLUE}"))
        print(f"{RESET}", end="")  # Reset to normal color after user input
        print_divisors(user_input)
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == '__main__':
    main()
