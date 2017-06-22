import string



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = list(string.ascii_lowercase)
    sorted_guess = sorted(lettersGuessed)
    
    for c in sorted_guess:
        if c in alphabet:
            alphabet.remove(c)
                        
    return ''.join(alphabet)

lettersGuessed = ['z', 'i', 'k', 'p', 'r', 's']

print (getAvailableLetters(lettersGuessed))
