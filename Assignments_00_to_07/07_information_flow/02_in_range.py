def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    Also checks if the number is even when within the range.
    """
    if n >= low and n <= high:
        if n % 2 == 0:
            print(f"{n} is even and in the range!")
            return True
        return True
    
    return False

def main():
    # Example usage
    n = int(input("Enter a number: "))
    low = int(input("Enter the low value of the range: "))
    high = int(input("Enter the high value of the range: "))
    
    if in_range(n, low, high):
        print(f"{n} is in the range {low} to {high}.")
    else:
        print(f"{n} is not in the range {low} to {high}.")


if __name__ == '__main__':
    main()
