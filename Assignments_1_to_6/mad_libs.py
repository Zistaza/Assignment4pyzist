import random
from colorama import init, Fore # type: ignore

# Initialize colorama
init(autoreset=True)

# Story templates
story_templates = [
    """
    Once upon a time, there was a person named {name}.
    They had a very {adjective1} pet {animal}, who loved to {verb} all day long.
    One day, they both went to {place}, where they met a {adjective2} wizard.
    The wizard granted them three wishes, and they lived happily ever after!
    """,

    """
    Deep in the jungle, {name} and their {adjective1} {animal} were searching for treasure.
    Suddenly, a {adjective2} storm appeared, forcing them to {verb} toward {place}.
    There, they discovered a hidden map and a golden banana!
    """,

    """
    At the magical academy of {place}, {name} was known for their {adjective1} skills.
    One day, their pet {animal} started to {verb} uncontrollably during class!
    It took a {adjective2} professor to calm things down.
    """
]

def create_mad_lib():
    # Get user input
    name = input("Enter a name: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    # Select a random story
    template = random.choice(story_templates)

    # Fill the template
    story = template.format(
        name=name,
        adjective1=adjective1,
        adjective2=adjective2,
        animal=animal,
        verb=verb,
        place=place
    )

    # Print the story
    print(Fore.CYAN + "\n🎉 Here is your Mad Libs story!")
    print(Fore.YELLOW + story)

    # Optionally save to a file
    with open("mad_libs_story.txt", "w") as file:
        file.write(story)
    print(Fore.GREEN + "✅ Your story was saved to 'mad_libs_story.txt'!")

# Main loop
while True:
    create_mad_lib()
    again = input(Fore.MAGENTA + "\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print(Fore.BLUE + "Thanks for playing Mad Libs! 👋")
        break

