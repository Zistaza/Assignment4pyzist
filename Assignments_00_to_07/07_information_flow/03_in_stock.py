def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    
    # Ask if the user wants to update the stock
    update_stock = input(f"Would you like to update the stock for {fruit}? (yes/no): ").strip().lower()
    
    if update_stock == 'yes':
        try:
            new_stock = int(input(f"Enter the new stock number for {fruit}: "))
            update_fruit_stock(fruit, new_stock)
            print(f"The stock for {fruit} has been updated to {new_stock}.")
        except ValueError:
            print("Please enter a valid number for the stock.")
    
# Function to check the number of fruits in stock
def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    inventory = {
        'apple': 2,
        'durian': 4,
        'pear': 1000
    }
    
    return inventory.get(fruit, 0)

# Function to update the stock of a specific fruit
def update_fruit_stock(fruit, new_stock):
    """
    This function updates the stock of the specified fruit.
    """
    inventory = {
        'apple': 2,
        'durian': 4,
        'pear': 1000
    }
    
    # Update stock if the fruit exists
    if fruit in inventory:
        inventory[fruit] = new_stock
    else:
        # If fruit isn't in the inventory, add it with the new stock
        inventory[fruit] = new_stock
    # In real-world, the updated inventory would be saved in a database or file

if __name__ == '__main__':
    main()
