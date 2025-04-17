def add_three_copies(my_list, data):
    """Add three copies of the given data to the provided list."""
    for i in range(3):
        my_list.append(data)

def main():
    # Get input from the user
    message = input("Enter a message to copy: ")
    
    # Initialize an empty list
    my_list = []
    
    # Print the list before modification
    print("List before:", my_list)
    
    # Add three copies of the message to the list
    add_three_copies(my_list, message)
    
    # Print the list after modification
    print("List after:", my_list)

if __name__ == "__main__":
    main()
