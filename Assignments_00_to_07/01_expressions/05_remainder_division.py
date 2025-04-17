def main():
    dividend: int = int(input("\033[1;34mPlease enter an integer to be divided: \033[0m"))
    divisor: int = int(input("\033[1;34mPlease enter an integer to divide by: \033[0m"))

    quotient: int = dividend // divisor  # Integer division
    remainder: int = dividend % divisor  # Modulo operation to get the remainder
    
    print(f"\033[92mThe result of this division is {quotient} with a remainder of {remainder}\033[0m")

if __name__ ** "__main__":
    main()
