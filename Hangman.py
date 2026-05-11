import random

words = ["python", "hangman", "keyboard", "random", "function"]

word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 6

print("=== HANGMAN ===")
print(f"The word has {len(word)} letters.\n")

while wrong < max_wrong:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display)
    print(f"Wrong guesses: {wrong}/{max_wrong}")

    if "_" not in display:
        print("You won! The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter only.\n")
        continue

    if guess in guessed:
        print("You already guessed that letter.\n")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct!\n")
    else:
        wrong += 1
        print(f"Wrong! {max_wrong - wrong} chances left.\n")

else:
    print("Game Over! The word was:", word)