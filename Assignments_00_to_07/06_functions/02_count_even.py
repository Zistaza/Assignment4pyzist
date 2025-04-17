def count_even_and_sum(lst):
    """
    Counts and sums the even numbers in a list.

    Args:
        lst (list of int): A list of integers.

    Prints:
        - Number of even integers
        - Total sum of even integers
    """
    count = 0
    total = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
            total += num
    print(f"Number of even integers: {count}")
    print(f"Total sum of even integers: {total}")

def get_list_of_ints():
    """
    Prompts the user to enter integers one by one until they press enter.

    Returns:
        list of int: The list of entered integers.
    """
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")
    return lst

def main():
    lst = get_list_of_ints()
    count_even_and_sum(lst)

if __name__ == '__main__':
    main()
