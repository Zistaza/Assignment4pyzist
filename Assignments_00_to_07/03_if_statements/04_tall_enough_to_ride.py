def main():
    MIN_HEIGHT = 50

    # ANSI escape codes
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE_BOLD_ITALIC = "\033[94m\033[1m\033[3m"
    RESET = "\033[0m"

    print("🎢 Welcome to the Rollercoaster Ride Checker!")
    print("Enter your height (or press Enter to quit):")

    while True:
        height_input = input(f"{BLUE_BOLD_ITALIC}How tall are you? {RESET}")

        if height_input == "":
            print("👋 Goodbye! Have a great day!")
            break

        try:
            height = float(height_input)

            if height >= MIN_HEIGHT:
                print(f"{GREEN}✅ You're tall enough to ride!{RESET}")
            else:
                print(f"{YELLOW}⚠️ You're not tall enough to ride, but maybe next year!{RESET}")
        except ValueError:
            print(f"{YELLOW}❌ Please enter a valid number!{RESET}")

# Run the program
if __name__ == '__main__':
    main()
