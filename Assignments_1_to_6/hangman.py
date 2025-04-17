import random
import string

# 1. Word list with hints
words = {
    "python": "A popular programming language 🐍",
    "apple": "A fruit and a tech company 🍎",
    "hangman": "The name of this game 🎮",
    "guitar": "A string musical instrument 🎸",
    "elephant": "The largest land animal 🐘"
}

# 2. Choose a random word and its hint
word, hint = random.choice(list(words.items()))
word = word.lower()
guessed_letters = []  # Store correct/incorrect letter guesses
lives = 6  # Number of allowed incorrect guesses

print("🎮 Welcome to Hangman!")
print(f"💡 Hint: {hint}")

# 3. Function to display the word with guessed letters
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# 4. Game loop
while lives > 0:
    print("\n" + display_word(word, guessed_letters))
    print(f"❤️ Lives left: {lives}")
    print(f"📝 Guessed letters: {' '.join(guessed_letters) if guessed_letters else 'None'}")

    # 5. Get input from user: letter or full word
    guess = input("🔤 Guess a letter *or* the full word: ").strip().lower()

    # FULL WORD GUESS
    if len(guess) > 1:
        if guess == word:
            print(f"\n🎉 Amazing! You guessed the full word: {word}")
            break
        else:
            print("❌ Wrong full word guess. You lose a life!")
            lives -= 1
            continue

    # SINGLE LETTER GUESS
    if guess not in string.ascii_lowercase or len(guess) != 1:
        print("🚫 Invalid input! Please enter a single letter or full word.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        print("❌ Wrong letter.")
        lives -= 1

    # Check if all letters guessed
    if all(letter in guessed_letters for letter in word):
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
        break
else:
    print(f"\n💀 Game Over! The word was: {word}")
