def main():
    # Define voting ages for different countries
    PETURKSBOUIPO_AGE = 16
    STANLAU_AGE = 25
    MAYENGUA_AGE = 48
    NEW_COUNTRY_AGE = 21  # A fictional new country for variety

    # Ask for the user's age and ensure it's a valid number
    while True:
        try:
            # Turn on blue color for user input only
            print("How old are you? ", end="")  # Prompt stays normal
            user_input = input("\033[34m")  # User input starts in blue
            print("\033[0m", end="")  # Reset color back to normal
            user_age = int(user_input)
            if user_age < 0:
                print("Please enter a positive age.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"\nYou are {user_age} years old.\n")

    # Check voting eligibility in each fictional country
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")

    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")

    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

    if user_age >= NEW_COUNTRY_AGE:
        print(f"You can vote in NewCountry where the voting age is {NEW_COUNTRY_AGE}.")
    else:
        print(f"You cannot vote in NewCountry where the voting age is {NEW_COUNTRY_AGE}.")

    print("\nThanks for checking your voting eligibility!")


if __name__ == '__main__':
    main()
