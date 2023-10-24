import random

def choose_word():
    word_list = ["python", "hangman", "terminal", "programming", "developer", "challenge", "function", "variable"]
    return random.choice(word_list)

def display(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman_drawing(errors):
    drawings = [
        '''
         ------
         |    |
         |
         |
         |
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |
         |
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |    |
         |
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        ---
        '''
    ]
    return drawings[errors]

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    incorrect_word_bank = []

    print("Welcome to Hangman!")
    print(display(word, guessed_letters))
    print(hangman_drawing(incorrect_guesses))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter (enter 'new' for a new word or 'restart' to restart): ").lower()

        if guess == 'new':
            return hangman()
        elif guess == 'restart':
            guessed_letters = []
            incorrect_guesses = 0
            incorrect_word_bank = []
            word = choose_word()
            print("\nGame restarted!")
            print(display(word, guessed_letters))
            print(hangman_drawing(incorrect_guesses))
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed {guess}.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            incorrect_word_bank.append(guess)
            print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
        else:
            print("Correct!")

        current_display = display(word, guessed_letters)
        print(current_display)
        print(hangman_drawing(incorrect_guesses))
        print(f"Incorrect Word Bank: {', '.join(incorrect_word_bank)}")

        if "_" not in current_display:
            print("Congratulations! You've guessed the word.")
            break

    else:
        print(f"You've run out of guesses. The word was {word}.")

    # Ask if they want to play again
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice == "yes":
        hangman()

if __name__ == "__main__":
    hangman()