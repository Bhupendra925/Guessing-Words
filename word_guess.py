import random

name = input("What is your name: ")
print("Good Luck!", name)

words = ["hello", "computer", "programming", "science", "python", "college", "water", "save", "apple", "aman", "jitesh","van","even"]

word = random.choice(words)
print("\nGuess the characters of the word")

guesses = ''  # characters guessed by user
turns = 11    # total allowed wrong guesses

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()  # New line after word display

    if failed == 0:
        print("You win!")
        print("The word is:", word)
        break

    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have", turns, "more guesses left.")

        if turns == 0:
            print("You lose!")
            print("The word was:", word)
            print("Well Done ", name)
            print("Play again ! "," ",name)
