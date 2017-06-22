import string
secretWord = "else"


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
    def isWordGuessed(secretWord, lettersGuessed):
        '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: boolean, True if all the letters of secretWord are in lettersGuessed;
          False otherwise
        '''
        correct_letters_count = 0
        for c in secretWord:
            if c in lettersGuessed:
                correct_letters_count += 1

        return (correct_letters_count == len(secretWord))

    def getGuessedWord(secretWord, lettersGuessed):
        '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: user's guessed word
        '''
        guessed_word = ""

        for c in secretWord:
            if c in lettersGuessed:
                guessed_word += (c + " ")
            else:
                guessed_word += ("_ ")

        return (guessed_word)

    def getAvailableLetters(lettersGuessed):
        '''
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters that represents what letters have not
          yet been guessed.
        '''
        alphabet = list(string.ascii_lowercase)
        sorted_guess = sorted(lettersGuessed)

        for c in sorted_guess:
            if c in alphabet:
                alphabet.remove(c)

        return ''.join(alphabet)

    guessesLeft = 8
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)

    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is %s letters long." % len(secretWord))

    while guessesLeft > 0:
        print ("-------------")
        print ("You have %s guesses left." % guessesLeft)

        print ("Available letters:", availableLetters)
        user_input = input("Please guess a letter: ")

        if user_input in lettersGuessed:
            print ("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))

        elif user_input in secretWord:
            lettersGuessed.append(user_input)
            print ("Good guess: ", getGuessedWord(secretWord, lettersGuessed))

        else:
            lettersGuessed.append(user_input)
            guessesLeft -= 1
            print ("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))

        availableLetters = getAvailableLetters(lettersGuessed)

        # while we're within the number of guesses range, check to see if the player has won.
        if isWordGuessed(secretWord, lettersGuessed):
            print ("------------")
            return ("Congratulations, you won!")

    # number of guesses has reached it's limit. End the game.
    print ("-----------")
    return ("Sorry, you ran out of guesses. The word was %s." % secretWord)


print (hangman(secretWord))