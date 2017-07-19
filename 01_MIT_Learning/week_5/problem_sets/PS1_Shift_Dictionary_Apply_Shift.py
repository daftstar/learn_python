# Encryption lets you share information with other trusted people,
# without fear of disclosure.

# A cipher is an algorithm for performing encryption
# (and the reverse, decryption).
# Original = plaintext. Encrypted = ciphertext

# A cipher usually depends on a piece of auxiliary information,
# called a key. The key is incorporated into the encryption
# process; the same plaintext encrypted with two different keys
# should have two different ciphertexts.

# Without the key, it should be difficult to decrypt
# the resulting ciphertext into readable plaintext.


# Problem 1 - Build the Shift Dictionary and Apply Shift


import string
shift = 1


def build_shift_dict(shift):
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

    return low_up_cipher_dict


def apply_shift(word):   # word = self.message_text
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        translator = build_shift_dict(shift)
        cipher_word = ""
        for i in word:  # change word to self.message_text
            if i in translator:
                cipher_word += translator[i]
            else:
                cipher_word += i

        return cipher_word



print (build_shift_dict(shift))
print (apply_shift("hello, you guy."))






















# lower_ascii = string.ascii_lowercase
# shift = 1

# raw_cipher_dict = {}
# low_alph_cipher_dict = {}
# up_alph_cipher_dict = {}


# # For each index value of the ascii alphabet, assign the shifted cipher value 
# for i in range(len(lower_ascii)):
#     raw_cipher_dict[i] = i + shift

# # Because the alphabet only contains 26 letters, wrap the letters if val > 25 (non-ordinal)
# for key, values in raw_cipher_dict.items():
#     if values > 25:  # length of ascii alphabet   (0 - 25)
#         raw_cipher_dict[key] = (values - 26)    # (1 - 26)

# # Create the actual plaintext key to cipher value in alphabet
# for key, value in raw_cipher_dict.items():
#     # print (lower_ascii[key], lower_ascii[value])
#     low_alph_cipher_dict[lower_ascii[key]] = lower_ascii[value]

# # Create a clone of the lower case dictionary to upper case
# for key, value in low_alph_cipher_dict.items():
#     up_alph_cipher_dict[key.upper()] = value.upper()

# # copy lower and upper cipher dictionaries to new comprehensive dictionary
# low_up_cipher_dict = dict(low_alph_cipher_dict)
# low_up_cipher_dict.update(up_alph_cipher_dict)

# print (low_up_cipher_dict["z"])
# print (low_up_cipher_dict["a"] == low_up_cipher_dict["A"])
# print (len(low_up_cipher_dict))

