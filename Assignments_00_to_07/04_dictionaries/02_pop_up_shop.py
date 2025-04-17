# ANSI escape codes for styling
BLUE = "\033[94m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"

def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0
    cart = {}

    print(f"{BOLD}🍎 Welcome to the Fruit Shop! 🍍{RESET}\n")

    for fruit_name, price in fruits.items():
        while True:
            try:
                quantity = input(f"How many ({BLUE}{fruit_name}{RESET}) do you want?: ")
                quantity = int(quantity)
                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        if quantity > 0:
            item_cost = price * quantity
            total_cost += item_cost
            cart[fruit_name] = (quantity, item_cost)

    # Print receipt
    print(f"\n{BOLD}🧾 Your Fruit Receipt:{RESET}")
    for fruit, (qty, cost) in cart.items():
        print(f"{qty} x {fruit} @ ${fruits[fruit]} each = ${cost:.2f}")
    
    print(f"\n{BOLD}Your total is: ${total_cost:.2f}{RESET}")
    print(f"{BOLD}Thank you for shopping! 🛒{RESET}")

# Boilerplate
if __name__ == '__main__':
    main()
