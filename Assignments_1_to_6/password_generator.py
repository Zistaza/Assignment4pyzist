import random
import string

def generate_password(length):
    """Generates a single random password of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Random Password Generator!\n")

    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            password_length = int(input("Enter the length of each password: "))
            break
        except ValueError:
            print("⚠️ Please enter valid numbers only.\n")

    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        print(f"{i+1}: {generate_password(password_length)}")

if __name__ == "__main__":
    main()