import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Use a set to avoid duplicates
    numbers = set()

    # Keep generating until we have 10 unique numbers
    while len(numbers) < N_NUMBERS:
        num = random.randint(MIN_VALUE, MAX_VALUE)
        numbers.add(num)

    # Convert to sorted list
    sorted_numbers = sorted(numbers)

    # Print all numbers on one line
    print(" ".join(str(n) for n in sorted_numbers))

if __name__ == '__main__':
    main()
