# ANSI color codes
GREEN = "\033[92m"
RESET = "\033[0m"

def main():
    while True:
        try:
            # Get input from user and convert to integer
            start = int(input("Enter a starting number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    curr_value = start
    step = 0

    while curr_value < 100:
        curr_value = curr_value * 2
        step += 1
        print(f"{GREEN}{curr_value}{RESET}")

    print(f"\n🎉 Done in {step} steps! Final value: {curr_value}")


if __name__ == '__main__':
    main()
