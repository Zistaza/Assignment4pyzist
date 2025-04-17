# ANSI color codes
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

def get_user_numbers():
    user_numbers = []
    while True:
        user_input = input(f"{BOLD}{ITALIC}Enter a number (or leave blank to finish):{RESET} ")
        
        if user_input == "":
            break
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print(f"{BLUE}Invalid input. Please enter a number.{RESET}")
    
    return user_numbers

def count_nums(num_lst):
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict

def print_counts(num_dict):
    for num, count in num_dict.items():
        print(f"{num} appears {count} time{'s' if count > 1 else ''}.")

def main():
    print("🎯 Number Frequency Counter")
    user_numbers = get_user_numbers()
    print("\n📊 Result:")
    print_counts(count_nums(user_numbers))

if __name__ == "__main__":
    main()