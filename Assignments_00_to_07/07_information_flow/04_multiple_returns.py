import re

def get_user_info():
    # Ask for user details
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    
    # Ask for a valid email address
    while True:
        email_address = input("What is your email address?: ")
        if validate_email(email_address):
            break
        else:
            print("Invalid email format. Please enter a valid email.")
    
    # Ask for a valid phone number
    while True:
        phone_number = input("What is your phone number?: ")
        if validate_phone(phone_number):
            break
        else:
            print("Invalid phone number format. Please enter a valid phone number.")
    
    # Return the collected data as a tuple
    return first_name, last_name, email_address, phone_number


def validate_email(email):
    """Check if the email is in a valid format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def validate_phone(phone):
    """Check if the phone number is in a valid format (support international format)."""
    phone_regex = r'^\+?\d{1,4}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}$'  # International format
    return re.match(phone_regex, phone) is not None


def main():
    # Get user information
    user_data = get_user_info()
    
    # Define color codes
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    
    # Confirm user data with colored output
    print("\nYou entered the following information:")
    print(f"{GREEN}First Name: {user_data[0]}{RESET}")
    print(f"{GREEN}Last Name: {user_data[1]}{RESET}")
    print(f"{BLUE}Email Address: {user_data[2]}{RESET}")
    print(f"{BLUE}Phone Number: {user_data[3]}{RESET}")
    
    # Ask if the information is correct
    confirm = input("\nIs this information correct? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        print("Thank you for signing up!")
    else:
        print("Let's try again!")
        main()  # Restart the process if the user wants to re-enter details


if __name__ == '__main__':
    main()
