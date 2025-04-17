from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def main():
    user_list = []  # Initialize an empty list to store user inputs
    
    while True:
        # Display the current list
        print(f"Current list: {user_list}")
        
        # Prompt user for input and display in blue
        value = input(f"{Fore.BLUE}Enter a value (or press Enter to stop): {Fore.RESET}")
        
        if value == "":  # If the user presses Enter without typing anything, stop
            break
        
        if value.lower() == 'remove':  # If the user types 'remove', remove the last item
            if user_list:
                removed_item = user_list.pop()  # Remove the last item from the list
                print(f"Removed: {removed_item}")
            else:
                print("The list is empty, nothing to remove.")
        
        elif value.lower() == 'clear':  # If the user types 'clear', clear the entire list
            user_list.clear()
            print("The list has been cleared.")
        
        else:
            user_list.append(value)  # Add the entered value to the list
        
    print(f"Final list: {user_list}")  # Print the final list after exiting the loop


if __name__ == '__main__':
    main()
