import random

words = ["apple", "tiger", "chair", "robot", "house"]
word = random.choice(words)

guessed = ['_'] * len(word)
used = []
tries = 6

print("HANGMAN GAME")

while tries > 0 and '_' in guessed:
    print("\nWord:", ' '.join(guessed))
    print("Used:", used)
    print("Tries left:", tries)

    guess = input("Enter a letter: ").lower()

    if guess in used:
        continue

    used.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        tries -= 1

if '_' not in guessed:
    print("\nYou win! Word:", word)
else:
    print("\nYou lose! Word was:", word)
