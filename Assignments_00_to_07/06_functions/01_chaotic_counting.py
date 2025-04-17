import random

# Define likelihood of being done
DONE_LIKELIHOOD = 0.2  # You can tweak this number (0.0 to 1.0)

def done():
    """
    Returns True with a probability of DONE_LIKELIHOOD.
    """
    return random.random() < DONE_LIKELIHOOD

def count_to_ten_with_random_stop():
    """
    Counts from 1 to 10, but may stop early if 'done()' returns True.
    """
    for number in range(1, 11):  # 1 to 10 inclusive
        if done():
            return  # Stop counting and return to main
        print(number)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    count_to_ten_with_random_stop()
    print("I'm done.")

# This line ensures main runs only when the file is executed directly
if __name__ == '__main__':
    main()
