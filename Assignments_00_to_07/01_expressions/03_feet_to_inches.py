"""
Converts feet to inches.
"""

INCHES_IN_FOOT: int = 12  # 12 inches = 1 foot

def main():
    feet: float = float(input("\033[1;34mEnter number of feet: \033[0m"))
    inches: float = feet * INCHES_IN_FOOT

    # Determine correct pluralization
    foot_label = "foot" if feet == 1 else "feet"
    print(f"\033[92m\n{feet} {foot_label} is equal to {inches} inches!\033[0m")


if __name__ == '__main__':
    main()
