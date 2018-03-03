# Hangman game

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def right_indexes(secretWord, guess):
    """
    Because a letter can be in secret word more than once,
    we want to save indexes of that letter
    -iterate through secret word
    -check if guess is equal with letter from i'th iteration
    -if it is, save in indexes list the index of letter
    """

    indexes = []

    for i in range(len(secretWord)):
        if guess == secretWord[i]:
            indexes.append(i)

    return indexes


def save_guess(secretWord, guess, result):
    """
    Now that we have the indexes we replace * with letter guessed(if it is in secret word)
    at positions from indexes list
    """

    result_list = result.split()

    for i in right_indexes(secretWord, guess):
        result_list[i] = guess

    return ' '.join(result_list)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    tries = 0
    letters_used = []
    result = '* ' * len(secretWord)

    print("The word has {} letters".format(len(secretWord)))
    # print(result)

    while True:

        guess = (raw_input('Type a letter: ')).lower()
                 # ask the user for a letter

        if not guess in letters_used:
            letters_used.append(guess)  # avoid duplicates of letters

        result = save_guess(secretWord, guess, result)

        print("You already used these letters: {}".format(letters_used))

        if guess in secretWord:
            print("Letter {} is in the secret word".format(guess))
            print(result)
        else:
            tries += 1
            print("The letter {} is not in secret word".format(guess))
            print(result)

        if tries >= 8:
            print("Game Over.You tried guessing more than 8 times")
            print("The secret word was {}".format(secretWord))
            break

        if result == secretWord:
            print("Congratulations.You found the secret word")
            print("The secret word was {}".format(secretWord))
            break


secretWord = chooseWord(wordlist).lower()

hangman(secretWord)
