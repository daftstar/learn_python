
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    masked_word = "_ " * len(secretWord)
    guessed_word = ""
    
    print ("Here's your word:", masked_word)

    for c in secretWord:
        if c in lettersGuessed:
            guessed_word += (c + " ")
        else:
            guessed_word += ("_ ")

    return (guessed_word)


secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'p', 'a']


print(getGuessedWord(secretWord, lettersGuessed))




