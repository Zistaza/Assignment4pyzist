ADULT_AGE: int = 18  # U.S. age

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False


def main():
    age = int(input("How old is this person?: "))  # Convert input to integer
    if is_adult(age):
        print("This person is an adult!")
    else:
        print("This person is not an adult.")

if __name__ == "__main__":
    main()
