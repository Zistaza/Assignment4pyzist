# Constant representing the maximum allowed value in Fibonacci sequence
DEFAULT_MAX_FIB_VALUE = 10000

def generate_fibonacci(max_value):
    curr_term = 0
    next_term = 1
    
    while curr_term <= max_value:
        print(curr_term, end=" ")
        curr_term, next_term = next_term, curr_term + next_term

def main():
    print("📈 Fibonacci Sequence Generator")
    user_input = input(f"Enter a max value (or press Enter to use default {DEFAULT_MAX_FIB_VALUE}): ")

    if user_input.strip().isdigit():
        max_value = int(user_input)
    else:
        max_value = DEFAULT_MAX_FIB_VALUE

    print(f"\nFibonacci terms up to {max_value}:\n")
    generate_fibonacci(max_value)
    print()  # clean newline after output

# Standard boilerplate
if __name__ == '__main__':
    main()
