def get_first_item(item_list):
    """
    Prints the first item of the provided list.
    """
    print(f"The first item in the list is: {item_list[0]}")

def get_item_list():
    """
    Prompts the user to enter one item of the list at a time and returns the resulting list.
    """
    user_list = []
    item = input("Please enter an item for the list (or press Enter to stop): ")
    while item != "":
        user_list.append(item)
        item = input("Please enter an item for the list (or press Enter to stop): ")
    return user_list

def main():
    item_list = get_item_list()  # Get the list from the user
    if item_list:  # Check if the list is not empty
        print(f"Total items in your list: {len(item_list)}")  # Print the total number of items
        get_first_item(item_list)  # Get the first item in the list
    else:
        print("The list is empty, please enter some items.")

if __name__ == '__main__':
    main()
