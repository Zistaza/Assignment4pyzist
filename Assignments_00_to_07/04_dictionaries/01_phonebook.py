# ANSI color codes for styling
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}
    while True:
        name = input(f"{BOLD}{ITALIC}Name (leave blank to stop):{RESET} ")
        if name == "":
            break
        number = input(f"{BOLD}{ITALIC}Number:{RESET} ")
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print(f"\n{BOLD}📖 Phonebook Entries:{RESET}")
    for name in phonebook:
        print(f"{BLUE}{name}{RESET} ➜ {phonebook[name]}")

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers by name.
    """
    print(f"\n{BOLD}🔍 Lookup Numbers (leave blank to stop):{RESET}")
    while True:
        name = input(f"{ITALIC}Enter name to lookup:{RESET} ")
        if name == "":
            break
        if name in phonebook:
            print(f"{BLUE}{name}{RESET}'s number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")

def delete_contact(phonebook):
    """
    Allow the user to delete a contact from the phonebook.
    """
    print(f"\n{BOLD}❌ Delete Contacts (leave blank to stop):{RESET}")
    while True:
        name = input(f"{ITALIC}Enter name to delete:{RESET} ")
        if name == "":
            break
        if name in phonebook:
            del phonebook[name]
            print(f"{name} was deleted.")
        else:
            print(f"{name} not found in the phonebook.")

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)
    delete_contact(phonebook)

    print(f"\n{BOLD}📕 Final Phonebook:{RESET}")
    print_phonebook(phonebook)

if __name__ == '__main__':
    main()
