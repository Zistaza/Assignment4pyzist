def main():
    while True:
        try:
            curr_value = int(input("Enter a number: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Please enter a valid integer.")

    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()
