def subtract_seven(num):
    """Subtracts 7 from the given number and returns the result."""
    return num - 7

def main():
    try:
        # Ask the user to input a number
        user_input = int(input("Enter a number to subtract 7 from: "))
        
        # Subtract 7 and show the result
        result = subtract_seven(user_input)
        print(f"The result after subtracting 7 is: {result}")
        
        # Bonus info
        if result == 0:
            print("Whoa! That brought it down to zero. ✨")
        elif result < 0:
            print("The result is negative. 🔻")
        else:
            print("Still a positive number. 👍")
    
    except ValueError:
        print("Please enter a valid integer!")


if __name__ == '__main__':
    main()
