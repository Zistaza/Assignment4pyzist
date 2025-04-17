C: int = 299792458  # The speed of light in m/s

def main():
    print("\033[1;3;92mWelcome to the Mass-Energy Equivalence Calculator!\033[0m")
    print("Enter 'q' to quit at any time.\n")

    while True:
        user_input = input("Enter kilos of mass: ")

        if user_input.lower() == 'q' or user_input.strip() == "":
            print("\033[1;3;92mGoodbye!☺\033[0m")

            break

        try:
            mass_in_kg: float = float(user_input)

            energy_in_joules: float = mass_in_kg * (C ** 2)

            print("\ne = m * C^2...")
            print(f"m = {mass_in_kg} kg")
            print(f"C = {C} m/s")
            print(f"{energy_in_joules} joules of energy!\n")

        except ValueError:
            print("Please enter a valid number or 'q' to quit.\n")


if __name__ == '__main__':
    main()
