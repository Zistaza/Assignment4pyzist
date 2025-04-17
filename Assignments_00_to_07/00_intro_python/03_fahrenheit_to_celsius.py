def main():
    fahrenheit = float(input("\033[1;31mEnter the temperature in Fahrenheit: \033[0m"))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"The temperature in Celsius is: {celsius:.2f}°C")

if __name__ == "__main__":
    main()
