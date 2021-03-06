# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"



def newline():
    print ("\n_________________________________\n")


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------------------------------------


# ############ PROBLEM 1 ##################
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for i in range(len(word)):
        # match user's letter to value of letter in dictionary, calculate score
        score += SCRABBLE_LETTER_VALUES[word[i]]
        # print ("letter: %s - %s" %(word[i], SCRABBLE_LETTER_VALUES[word[i]]))

    # After individual letter score has been tallie
    score *= len(word)

    # If word uses all available letters, add 50 points to score
    if len(word) == n:
        score += 50
    return (score)


# print (getWordScore("qi", 5))
# print (newline())


# ############ PROBLEM 2 ##################
# Problem #2: Make sure you understand how this function works and what it does!
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: Dictionary {string:int}
    """
    # hand_spelling = ""
    # for key, value in hand.items():
    #     hand_spelling += (key + " ") * value

    # return hand_spelling


    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")    # print all on the same line
    print()                             # print an empty line


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand



def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # created a copy of the dictionary, as to keep the original intact.
    updated_hand = hand.copy()

    # check to see if each letter in the word is available in
    # the copied hand. If so, reduce updated_hand[value] by 1.
    for letter in word:
        if letter in updated_hand and updated_hand[letter] > 0:
            updated_hand[letter] -= 1
        else:
            return False
    return updated_hand


# hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}

# up_hand = updateHand(hand, "quail")
# print (up_hand)
# print (displayHand(up_hand))
# print (newline())


#
# Problem #3: Test word validity
#


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand_copy = hand.copy()
    word_freq = getFrequencyDict(word)

    # for each character in the user's word, 
    # compare the quantity of each character {key:value}
    # to the value of the the character in the user's hand.
    # Using get, so if the letter does not exist,
    # use 0 as default value. 

    for char in word:
        if word_freq[char] > hand.get(char, 0):
            # print ("in word %s, %s does not exist enough times in hand: \n%s" %(word, char, hand))
            return False

    # If the function makes it this far, then evaluate
    # if the word exists in the wordList       
    return (word in wordList)

wordList = loadWords()


# print (isValidWord("kwijibo", {'k': 1, 'j': 1, 'b': 1, 'w': 1, 'i': 2, 'o': 1}, wordList))
# print (isValidWord("chayote", {'c': 2, 'y': 1, 'h': 1, 't': 2, 'z': 1, 'u': 2, 'a': 1, 'o': 2}, wordList))
# print (isValidWord("hammer", {'r': 1, 'a': 1, 'e': 1, 'm': 2, 'h': 1}, wordList))
# print (isValidWord("hammer", {'r': 1, 'a': 1, 'e': 1, 'm': 2, 'h': 1}, wordList))
# print (isValidWord("rapture", {'a': 3, 'r': 1, 't': 1, 'p': 2, 'e': 1, 'u': 1}, wordList))

# print (newline())

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length = 0
    for value in hand.values():
        length += value
    return length


# hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
# print (calculateHandlen(hand))
# print (newline())
# print (newline())



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the word score
    word_score = 0

    # Keep track of the total score
    total_score = 0

    # keep track of how many letters are in the hand
    hand_length = calculateHandlen(hand)

    # As long as there are still letters left in the hand: 
    while hand_length > 0:

        # Display the hand
        print ("Current Hand:  ", end ='')
        displayHand(hand)

        # Ask user for input
        user_input = input("Enter word, or a \".\" to indicate that you are finished: ")

        # If the input is a single period:
        if user_input == ".":

            # End the game (break out of the loop)
            break

        # Otherwise (the input is not a single period):
        # If the word is not valid:
        elif isValidWord(user_input, hand, wordList) is False:
            # Reject invalid word (print a message followed by a blank line)
            print ("Invalid word, please try again.\n")

        # Otherwise (the word is valid):
        else:
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            word_score = getWordScore(user_input, n)
            total_score += word_score
            print ("\"%s\" earned %s points. Total: %s points\n" % (user_input, word_score, total_score))

            # Update the hand
            current_hand = updateHand(hand, user_input)
            hand = current_hand

            hand_length = calculateHandlen(current_hand)
            # print (hand_length)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    return ("Goodbye! Total score: %s points." % total_score)


# hand = {'h': 1, 'i': 1, 'c': 1, 'z': 1, 'm': 2, 'a': 1}
# hand = {'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}
# hand = {'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}
# n = 7
# print (playHand(hand, wordList, n))
print (newline())


# Problem #5: Playing a game
#


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    # by running this function, we turn the game on
    game_on = True

    # when the game begins, initialize hand_played has not yet occured
    hand_played = False

    # while the game runs, execute the following:
    while game_on is True:
        # get user input for game options (n, r, e)
        user_input = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        # If the user gets cold feet, turn the game off and exit the game
        if user_input == "e":
            game_on = False
            break

        # If the user hits 'r' and the first hand hasn't played yet, show error
        # <this seems sloppy, but it's part of the exercise>""
        elif user_input == "r" and hand_played is False:
            print ("You have not played a hand yet. Please play a new hand first!")

        # if the user has already played a hand, then play again, but use the same hand
        # hand has already been set by the next function, do not create a new hand
        elif user_input == "r" and hand_played:
            playHand(hand, wordList, HAND_SIZE)

        # If the user wants a new game, create a new hand and start the game based
        # on the newly created hand.
        elif user_input == "n":
            hand_played = True
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)

        # otherwise, the user has fat-fingered the keys, so tell them they're invalid.
        else:
            print ("Invalid command.")


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
