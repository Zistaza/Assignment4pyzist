def main():
    # Ask the user for input and convert it into a list of integers
    user_input = input("Enter numbers separated by spaces: ").strip()
    
    # Convert the input string to a list of integers
    try:
        original_list = [int(num) for num in user_input.split()]
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
        return

    print("Original list:", original_list)

    # Double each element in the list
    for index in range(len(original_list)):
        original_list[index] *= 2

    print("Doubled list:", original_list)

if __name__ == '__main__':
    main()
