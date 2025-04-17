import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

NUM_SIDES: int = 6

def main():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2

    print(Fore.CYAN + f"Dice have {NUM_SIDES} sides each.")
    print(Fore.YELLOW + f"First die: {die1}")
    print(Fore.GREEN + f"Second die: {die2}")
    print(Fore.MAGENTA + f"Total of two dice: {total}")

if __name__ == '__main__':
    main()
