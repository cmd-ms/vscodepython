import random
import string
from words import words

# pick a random word for the game
def get_valid_word(words):
    word = random.choice(words)  # randomly choose a word
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

# main hangman function code
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    # lives


    # Getting user input
    while len(word_letters) > 0:
        # letters used
        # ' '.join(['a', 'b' 'cd']) --> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already guessed this character. Please try again.")

        else:
            print("Invalid character. Please Try Again.")
    print("word")
    # gets here when len(word_letters) == 0


# Result
hangman()