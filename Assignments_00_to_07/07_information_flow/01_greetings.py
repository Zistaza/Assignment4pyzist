from datetime import datetime

# Helper function to greet based on the time of day
def greet(name):
    # Get current time of day
    current_hour = datetime.now().hour
    
    if current_hour < 12:
        time_of_day = "Good Morning"
    elif 12 <= current_hour < 18:
        time_of_day = "Good Afternoon"
    else:
        time_of_day = "Good Evening"
    
    return f"{time_of_day} {name}!"

# Main function to handle user input and greet
def main():
    while True:
        name = input("What's your name? ").strip()
        
        # Handle case for empty input
        if not name:
            print("Please enter a valid name.")
            continue
        
        print(greet(name))
        
        # Ask for age and give a personalized message
        try:
            age = int(input(f"How old are you, {name}? "))
            if age >= 18:
                print(f"You're an adult, {name}!")
            else:
                print(f"You're a child, {name}!")
        except ValueError:
            print("Please enter a valid age.")

        # Ask if the user wants to greet someone else
        cont = input("Would you like to greet someone else? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Thank you for using the greeting program!")
            break

# Run the main function
if __name__ == '__main__':
    main()
