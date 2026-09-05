"""
Hangman Game
CodeAlpha Python Programming Internship - Task 1

A simple text-based Hangman game where the player guesses a word
one letter at a time.
"""

import random

# A small list of predefined words
WORDS = ["python", "hangman", "developer", "internship", "keyboard"]

MAX_INCORRECT_GUESSES = 6


def choose_word():
    """Pick a random word from the word list."""
    return random.choice(WORDS)


def display_progress(word, guessed_letters):
    """Show the word with guessed letters revealed and others hidden as _."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(f"Try to guess the word. You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(f"Word: {display_progress(word, guessed_letters)}")
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!\n")
            # Check if the player has won
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.\n")
    else:
        # This runs if the while loop exits because incorrect_guesses reached the max
        print(f"Game over! You've used all {MAX_INCORRECT_GUESSES} incorrect guesses.")
        print(f"The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()
