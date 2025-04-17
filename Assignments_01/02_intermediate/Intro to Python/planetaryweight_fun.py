# planetaryweight_fun.py

# Importing colorama for colors and initializing it
from colorama import Fore, Style, init # type: ignore
init(autoreset=True)

# Emojis & Gravity Constants 🌌
PLANET_DATA = {
    "1": ("Mercury 🪙", 0.376),
    "2": ("Venus 🌕", 0.889),
    "3": ("Mars 🔴", 0.378),
    "4": ("Jupiter 🟠", 2.36),
    "5": ("Saturn 💍", 1.081),
    "6": ("Uranus 🌀", 0.815),
    "7": ("Neptune 🌊", 1.14)
}

def show_planet_menu():
    print(Fore.YELLOW + "\n🌍 Choose a planet to calculate your weight on:")
    for key, (name, _) in PLANET_DATA.items():
        print(f"{Fore.CYAN}{key}. {name}")

def get_planet_choice():
    while True:
        choice = input(Fore.GREEN + "\nEnter the number of your planet choice: ")
        if choice in PLANET_DATA:
            return PLANET_DATA[choice]
        else:
            print(Fore.RED + "❌ Invalid choice. Please enter a number from the list.")

def calculate_weight_on_planet(earth_weight, gravity_multiplier):
    return round(earth_weight * gravity_multiplier, 2)

def main():
    print(Fore.MAGENTA + "🚀 Welcome to the Planetary Weight Calculator! 🌌")

    while True:
        try:
            earth_weight = float(input(Fore.GREEN + "\n🌍 Enter your weight on Earth (in kg): "))
        except ValueError:
            print(Fore.RED + "⚠️ Please enter a valid number.")
            continue

        show_planet_menu()
        planet_name, gravity = get_planet_choice()

        new_weight = calculate_weight_on_planet(earth_weight, gravity)
        print(Fore.YELLOW + f"\n💫 Your weight on {planet_name} would be: {Fore.CYAN}{new_weight} kg")

        # Ask to try again or quit
        retry = input(Fore.MAGENTA + "\n🔁 Do you want to calculate again? (yes/no): ").strip().lower()
        if retry not in ['yes', 'y']:
            print(Fore.LIGHTBLUE_EX + "\n👋 Thanks for using the Planetary Weight Calculator. Safe travels through the stars! 🌠")
            break

if __name__ == "__main__":
    main()
