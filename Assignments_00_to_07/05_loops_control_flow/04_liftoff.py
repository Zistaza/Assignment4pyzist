def main():
    start_number = int(input("Enter the countdown start number: "))
    for i in range(start_number, 0, -1):
        print(i)
    print("Liftoff!")

if __name__ == '__main__':
    main()
