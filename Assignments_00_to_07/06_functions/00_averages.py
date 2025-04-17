def average(a: float, b: float) -> float:
    """
    Returns the number which is halfway between a and b
    """
    result = (a + b) / 2
    return result

def print_average(label: str, value: float, color: str = "\033[92m"):
    """
    Prints a labeled average in colored format.
    """
    RESET = "\033[0m"
    print(f"{color}{label}: {value}{RESET}")

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    final_avg = average(avg_1, avg_2)

    # Print results using helper function with colors
    print_average("Average between 0 and 10", avg_1, "\033[94m")  # Blue
    print_average("Average between 8 and 10", avg_2, "\033[96m")  # Cyan
    print_average("Final Average", final_avg, "\033[92m")         # Green

# Required entry point
if __name__ == '__main__':
    main()
