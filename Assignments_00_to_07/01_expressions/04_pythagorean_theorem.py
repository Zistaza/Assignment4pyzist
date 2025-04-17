import math  # Import the math library so we can use the sqrt function

def main():
    ab: float = float(input("\033[1;34mEnter the length of AB: \033[0m"))
    ac: float = float(input("\033[1;34mEnter the length of AC: \033[0m"))

    bc: float = math.sqrt(ab**2 + ac**2)

    print(f"\033[92mThe length of BC (the hypotenuse) is: {bc:.2f}\033[0m")

if __name__ == '__main__':
    main()
