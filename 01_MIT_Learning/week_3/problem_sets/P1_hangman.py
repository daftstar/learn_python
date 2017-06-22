
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    correct_letters_count = 0
    for c in secretWord:
        if c in lettersGuessed:
            correct_letters_count += 1

    return (correct_letters_count == len(secretWord))


secretWord = 'apple'
lettersGuessed = ['a', 'p', 'l', 'a', 'e']
print(isWordGuessed(secretWord, lettersGuessed))







# def isWordGuessed(secretWord, lettersGuessed):
#     '''
#     secretWord: string, the word the user is guessing
#     lettersGuessed: list, what letters have been guessed so far
#     returns: boolean, True if all the letters of secretWord are in lettersGuessed;
#       False otherwise
#     '''
#     # FILL IN YOUR CODE HERE...
#     correct_letters_count = 0
#     for c in secretWord:
#         if c in lettersGuessed:
#             # print ("yes")
#             correct_letters_count += 1
#         else:
#             # print ("no")

#     return (correct_letters_count == len(secretWord))


# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))