from hashlib import sha256

# ANSI styling
BLUE = "\033[94m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"

# Password hashing
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Login function
def login(email, stored_logins, password_to_check):
    email = email.lower()  # Make email lookup case-insensitive
    if email not in stored_logins:
        print(f"{email} is not registered.")
        return False

    stored_hash = stored_logins[email]
    input_hash = hash_password(password_to_check)

    if stored_hash == input_hash:
        print(f"{BOLD}✅ Login successful!{RESET}")
        return True
    else:
        print(f"{BOLD}❌ Incorrect password.{RESET}")
        return False

# Register new user
def register_user(email, stored_logins, password):
    stored_logins[email.lower()] = hash_password(password)
    print(f"{BOLD}✅ Account created for {email}!{RESET}")

# Main program
def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # "Karel"
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"   # "password"
    }

    print(f"{BOLD}🔐 Secure Login System 🔐{RESET}\n")

    email = input(f"Enter your email: {BLUE}{BOLD}{ITALIC}")
    email = email.strip()
    print(f"{RESET}", end="")  # reset styling after input

    # Email check
    if email.lower() not in stored_logins:
        choice = input(f"{email} not found. Do you want to register? (y/n): {BLUE}{BOLD}{ITALIC}").lower()
        print(f"{RESET}", end="")
        if choice == 'y':
            password = input("Create your password: " + BLUE + BOLD + ITALIC)
            print(RESET, end="")
            register_user(email, stored_logins, password)
        else:
            print("Exiting. 👋")
            return
    else:
        attempts = 3
        while attempts > 0:
            password = input("Enter your password: " + BLUE + BOLD + ITALIC)
            print(RESET, end="")
            if login(email, stored_logins, password):
                break
            attempts -= 1
            if attempts > 0:
                print(f"⏳ Attempts left: {attempts}\n")
            else:
                print(f"{BOLD}🔒 Account locked. Please try again later.{RESET}")

# Python entry point
if __name__ == '__main__':
    main()
