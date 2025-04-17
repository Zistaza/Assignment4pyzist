MAX_LENGTH: int = 3  # Set the maximum length for the list

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Check if the list is longer than MAX_LENGTH
        last_elem = lst.pop()  # Remove the last element from the list
        print(f"Removed: {last_elem}")  # Print the removed element

# Function to get the list of items from user input
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Keep prompting until user presses Enter without input
        lst.append(elem)  # Add the entered element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get the list from user input
    print(f"Original list: {lst}")
    shorten(lst)  # Shorten the list and print removed elements
    print(f"Final list: {lst}")  # Print the remaining list after shortening

if __name__ == '__main__':
    main()
