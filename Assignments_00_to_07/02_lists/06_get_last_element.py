def get_last_item(item_list):
    """
    Prints the last item of the provided list.
    """
    # Print the last item in the list using negative indexing
    print(f"The last item in the list is: {item_list[-1]}")

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
        get_last_item(item_list)  # Get the last item in the list
    else:
        print("The list is empty, please enter some items.")

if __name__ == '__main__':
    main()
