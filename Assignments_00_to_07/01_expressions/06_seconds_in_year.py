DAYS_IN_YEAR: int = 365
HOURS_IN_DAY: int = 24
MINUTES_IN_HOUR: int = 60
SECONDS_IN_MINUTE: int = 60

def main():
    total_seconds = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
    print(f"\033[95mThere are {total_seconds} seconds in a year!\033[0m")

if __name__ == "__main__":  # Corrected the operator here
    main()
