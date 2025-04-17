from colorama import init, Fore

# Initialize colorama for colorful output
init(autoreset=True)

def calculate_total(values: list[int]) -> int:
    """
    Returns the sum of a list of integers.
    """
    total: int = 0
    for value in values:
        total += value
    return total

def main():
    user_data = input(Fore.CYAN + "Enter numbers separated by spaces: ")

    # Split input and attempt to convert each to an integer
    number_list = []
    for part in user_data.strip().split():
        try:
            number = int(part)
            number_list.append(number)
        except ValueError:
            print(Fore.RED + f"Invalid input '{part}' ignored. Please enter only integers.")

    if number_list:
        result = calculate_total(number_list)
        print(Fore.YELLOW + f"\nYou entered: {number_list}")
        print(Fore.GREEN + f"Total sum: {result}")
    else:
        print(Fore.RED + "No valid numbers were entered.")

if __name__ == '__main__':
    main()
