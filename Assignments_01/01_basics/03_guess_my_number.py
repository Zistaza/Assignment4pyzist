import random

def main():
    # Generate the secret number between 1 and 99
    secret_number: int = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Track number of attempts
    attempts = 0

    # Initial guess
    guess = int(input("Enter a guess: "))
    attempts += 1
    
    # Loop until user guesses correctly
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Empty line for spacing
        guess = int(input("Enter a new guess: "))
        attempts += 1

    # Success message
    print(f"🎉 Congrats! The number was: {secret_number}")
    print(f"🎯 You guessed it in {attempts} tries!")

if __name__ == '__main__':
    main()
