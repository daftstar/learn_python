import string

# ## DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


# ## DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


# ## DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'


# PROBLEM 1
class Message(object):
    # ## DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    # ## DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        Returns: self.message_text
        '''
        return self.message_text

    # ## DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        lower_ascii = string.ascii_lowercase
        # shift = 3

        raw_cipher_dict = {}
        low_alph_cipher_dict = {}
        up_alph_cipher_dict = {}

        # For each index value of the ascii alphabet, assign the shifted cipher value
        for i in range(len(lower_ascii)):
            raw_cipher_dict[i] = i + shift

        # Because the alphabet only contains 26 letters, wrap the letters if val > 25 (non-ordinal)
        for key, values in raw_cipher_dict.items():
            if values > 25:  # length of ascii alphabet   (0 - 25)
                raw_cipher_dict[key] = (values - 26)    # (1 - 26)

        # Create the actual plaintext key to cipher value in alphabet
        for key, value in raw_cipher_dict.items():
            # print (lower_ascii[key], lower_ascii[value])
            low_alph_cipher_dict[lower_ascii[key]] = lower_ascii[value]

        # Create a clone of the lower case dictionary to upper case
        for key, value in low_alph_cipher_dict.items():
            up_alph_cipher_dict[key.upper()] = value.upper()

        # copy lower and upper cipher dictionaries to new comprehensive dictionary
        low_up_cipher_dict = dict(low_alph_cipher_dict)
        low_up_cipher_dict.update(up_alph_cipher_dict)

        self.low_up_cipher_dict = low_up_cipher_dict
        return low_up_cipher_dict

    def apply_shift(self, shift):
            '''
            Applies the Caesar Cipher to self.message_text with the input shift.
            Creates a new string that is self.message_text shifted down the
            alphabet by some number of characters determined by the input shift

            shift (integer): the shift with which to encrypt the message.
            0 <= shift < 26

            Returns: the message text (string) in which every character is shifted
                 down the alphabet by the input shift
            '''
            # create empty string for encrypted word
            cipher_word = ""

            # retrieve cipher dictionary from build_shift_dict function above
            translator = self.build_shift_dict(shift)

            # for each character in the message text, if the char is in the dictionary,
            # encrypt it and add the new char to the cipher_word string. If the char
            # is not in the dictionary, add it without encryption.
            for i in self.message_text:
                if i in translator:
                    cipher_word += translator[i]
                else:
                    cipher_word += i

            return cipher_word


# PROBLEM 2
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        Message.__init__(self, text)   # initialize Message attributes
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        self.copy_dict = self.encrypting_dict.copy()
        return self.copy_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


# PROBLEM 3
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # self.message_text and self.valid_words initialized by Message parent class
        Message.__init__(self, text)   # initialize Message attributes

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # print ("_________")
        # debug to get the actual message test - see if func is firing..
        # print (self.get_message_text())
        # print ("_________")

        # instantiate tuple
        best = ()

        # instantiate comparison variable
        highest_word_count = 0

        # for each shift value available in the number of letters
        # in the alphabet (26), decipher the string using each shift value.
        # Split the deciphered string into individual words, and put into list
        # word_list

        # for each word in the word list, check if the word is
        # a valid word. If it is, increment the valid_word_count by 1

        # kepp track of the highest word count against the current valid
        # word count. If the current valid_word_count is higher, then
        # update the tuple with the current shift and the decrypted string
        for i in range(26):
            valid_word_count = 0
            decrypted_string = self.apply_shift(i)
            # print (decrypted_string)
            word_list = decrypted_string.split(' ')

            for word in word_list:
                if is_word(self.valid_words, word):
                    valid_word_count += 1

            if valid_word_count > highest_word_count:
                highest_word_count = valid_word_count
                best = (i, decrypted_string)

        return best
         








# a = Message("hello world")
# print (a.get_message_text())
# print (a.build_shift_dict(1))
# print (a.apply_shift(2))
# print ()
# print ()


# Example test case (PlaintextMessage)
# plaintext = PlaintextMessage('hello', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.get_message_text_encrypted())


# # Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq jgnnq jgnnq')
print('Expected Output:', (24, 'hello hello hello'))
print('Actual Output:', ciphertext.decrypt_message())
