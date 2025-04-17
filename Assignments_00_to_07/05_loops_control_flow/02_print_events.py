def main():
    print("🔢 Even Number Generator")

    # Get how many even numbers the user wants
    try:
        count = int(input("How many even numbers do you want to print? (default: 20): ") or 20)
        if count < 1:
            raise ValueError
    except ValueError:
        print("Invalid input. Using default value of 20.")
        count = 20

    # Optional: Get a custom starting number
    try:
        start = int(input("Enter the starting number (default: 0): ") or 0)
    except ValueError:
        print("Invalid input. Using default start of 0.")
        start = 0

    # Generate even numbers
    print("\n✅ First", count, "even numbers starting from", start, ":")
    even_numbers = []
    num = start
    while len(even_numbers) < count:
        if num % 2 == 0:
            even_numbers.append(num)
        num += 1

    print(" ".join(map(str, even_numbers)))  # Output in one line

    # Optional: Save to file
    save = input("\n💾 Do you want to save the results to 'even_numbers.txt'? (y/n): ").lower()
    if save == 'y':
        with open("even_numbers.txt", "w") as file:
            file.write(" ".join(map(str, even_numbers)))
        print("📁 Saved to even_numbers.txt")

# This is required to run the main function
if __name__ == '__main__':
    main()
