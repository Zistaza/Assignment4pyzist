import time

def main():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)  # Pause for 1 second
    print("Liftoff!")

# Required to call the main() function

if __name__ == '__main__':
    main()
