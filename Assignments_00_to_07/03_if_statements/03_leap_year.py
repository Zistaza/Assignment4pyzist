def main():
    # ANSI color codes
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Get the year to check from the user
    year = int(input("Please input a year: "))

    # Check leap year conditions
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{GREEN}That's a leap year!{RESET}")
                print(f"{GREEN}The year {year} has 366 days.{RESET}")
                print(f"{GREEN}Fun fact: Leap years keep our calendar aligned with the Earth's revolutions! 🌍{RESET}")
            else:
                print(f"{YELLOW}That's not a leap year.{RESET}")
                print(f"{YELLOW}The year {year} has 365 days.{RESET}")
        else:
            print(f"{GREEN}That's a leap year!{RESET}")
            print(f"{GREEN}The year {year} has 366 days.{RESET}")
            print(f"{GREEN}Fun fact: February 29 only exists in leap years! 🎉{RESET}")
    else:
        print(f"{YELLOW}That's not a leap year.{RESET}")
        print(f"{YELLOW}The year {year} has 365 days.{RESET}")


# Required line to call main function
if __name__ == '__main__':
    main()
