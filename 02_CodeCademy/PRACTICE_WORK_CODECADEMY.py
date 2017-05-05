"""
TESTING TO SEE IF A NUMBER IS AN INTEGER:

X - X(rounded down), must = 0
"""

# def is_int(x):
#     if x - int(x) == 0:
#         return True
#     else:
#         return False


# print (is_int(3.3))
# sum = 0


"""
ITERATING THROUGH A STRING VALUE TO CALCULATE SUM
"""


# def digit_sum(n):
#     n = str(n)
#     sum = 0

#     for i in n:                 # iterate through each value in n
#         sum = sum + int(i)      # add the value of each integer to the sum value
#     return (sum)                # return the sum of all values


# print (digit_sum(32))


# print (22 // 10)


# def mathy_digit_sum(number):

#     sum = 0

#     while number > 0:                # n will reach 0, once we floor (//) to 0
#         var_first = number % 10      # of the value n, lop off the last digit
#         print ("USING NUMBER %s: \n " % number)

#         sum = sum + var_first        # add the dropped digit to the sum count
#         print ("The total sum so far is %s " % sum)

#         number = number // 10       # make the new number by drop the last number
#         print ("The new value of n is %s \n" % number)

#     return sum
    
# print (mathy_digit_sum(951))



"""
ITERATING THROUGH A FUNCTION WHILE DECREMENTING

    To calculate the factorial of a non-negative integer x,
    just multiply all the integers from 1 through x

    Option is to create a list of all the numbers to be multiplied
    then, multiply through each number in the list.
    CONCERN: Does it make sesnse to create an arbitrary list?


"""


# def factorial(x):
#     x = abs(x)                          # accomodate negative numbers
#     factor_list = []                    # blank list
#     factor_calc = 1                     # prevent hitting 0, which results in final value of 0

#     for i in range(1, x+1):             # from each number in 1 to x (including x)
#         factor_list.append(i)           # append this number to the list, factor_list

#     for i in factor_list:               # within each number in the list, factor_list
#         factor_calc = i * factor_calc   # take current value of the number in the loop and multiply by previous total

#     return (factor_calc)


# # print(factorial(55221))               # uncomment this to see the function's output

# import cProfile                         # this imports the performance testing library
# cProfile.run('factorial(55221)')        # this outputs the performance metrics of the function


# """ 
# FACTORIAL WITHOUT THE LIST
# """


# def factorial_b(x):
#     x = abs(x)                  # accomodate for negative numbers
#     calc = 1                    # prevent multiply by 0, which results in final value of 0

#     for i in range(1, x+1):     # from each number in 1 to x (including x)
#         calc = calc * i         # calc = current calc value * current value of i in range
#     return calc


# # print (factorial_b(55221))         # uncomment this to see the function's output

# import cProfile                      # this imports the performance testing library
# cProfile.run('factorial_b(55221)')   # this outputs the performance metrics of the function


"""
CHECKING FOR PRIME NUMBER
"""

# VERSION 1


# def is_prime(x):
#     print ("is %s a prime number?\n" % x)

#     for n in range(2, x,):
#         print ("%s / %s = " % (x, n) + str(x / n))

#         if (x % n) == 0:
#             return False
#     else:
#         return True


# VERSION 2 - ACCOMODATING FOR 0, 1, 2

# def is_prime(x):
#     print ("is %s a prime number?\n" % x)
#     # x = abs(x)                  # As I understand it, the definition of primes was adjusted to exclude negative numbers

#     if x < 2:                     # all numbers < 2 are not prime. 
#         return False

#     elif x == 2:                  # 2 is a prime number
#         return True

#     else:
#         for n in range(2, x):                           # for each numer from 2, (because we already tested it), up to x
#             print ("%s / %s = " % (x, n) + str(x / n))  # print the number we're testing divided by the number in the for loop

#             if (x % n) == 0:      # if the number we're testing / the current number in the loop equals 0,
#                 return False      # then this number is NOT prime. 
#         else:
#             return True     # else applies to the for loop, so we can continue iterating until we hit a true value. If the previous IF condition never hits False, then the number IS prime.

# print (is_prime(13))



# VERSION 3 - SIMPLIFIED & OPTIMIZED

# from math import sqrt

# def is_prime(x):
#     print ("is %s a prime number?" % x)
#     print ("We need to divide %s by every number up to %s \n" %(x, int(sqrt(x)) + 2))
#     # x = abs(x)                  # As I understand it, the definition of primes was adjusted to exclude negative numbers

#     if x < 2:                     # all numbers < 2 are not prime. 
#         return False

#     elif x == 2:                  # 2 is a prime number
#         return True

#     else:
#         for n in range(2, int(sqrt(x)) + 2):            # sqrt halves the number of possibilities to iterate through. Adding 2, accomodates for any integer rounding issues.
#             print ("%s / %s = " % (x, n) + str(x / n))  # print the number we're testing divided by the number in the for loop

#             if (x % n) == 0:      # if the number we're testing / the current number in the loop equals 0,
#                 return False      # then this number is NOT prime. 
#         return True               # If the previous IF condition never hits False, then the number IS prime.

# print (is_prime(561))


"""
STRING MANIPULATION: REVERSE
WITHOUT USING reverse() or [::-1]
"""

# def reverse(text):
#     text_array = []
#     reverse_array = []
    
#     for i in text:
#         text_array.append(i)

#     text_length = (len(text_array)) - 1

#     for i in range(0, len(text_array)):
#         reverse_array.append((text_array[text_length]))
#         text_length -= 1

#     return ("".join(reverse_array))

# print (reverse("Hello My Name is Nik!"))


"""
OPTIMIZED & CLEANER CODE
"""

# def reverse_b(text):
#     text_array = []
#     x = len(text) - 1

#     for i in text:
#         text_array.append(text[x])
#         # print ("current value x is: %s" % x)
#         # print ("letter appending is: %s" % text_array)
#         x -= 1
#     return ("".join(text_array))


# print (reverse_b("hellow"))


"""
STRIPPING STRINGS OF SPECIFIC CHARACTERS
"""

# def anti_vowel(text):
#     vowels = ("AaEeIiOoUu")

#     text_array = []

#     for i in text:
#         if i not in vowels:
#             text_array.append(i)
#     return ("".join(text_array))


# print (anti_vowel("where is wAldo today?"))


"""
MATCHING STRING CHARS WITH DICTIONARY KEY VALUES
"""

# letter_score = {
#     "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#     "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#     "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#     "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#     "x": 8, "z": 10, " ": 0
# }


# def scrabble_score(text):
#     word_score = 0
#     text = text.lower()

#     for letter in text:
#         word_score = word_score + letter_score[letter]
#         print ("you get %s points for letter: %s" %((letter_score[letter]), letter))
#         print ("current score is %s \n" % word_score)
#     return ("TOTAL WORD SCORE: %s" % word_score)

# print (scrabble_score("Nik"))


"""
HANDLING MULTIPLE STRINGS and REPLACE STRINGS
"""

"""
METHOD 1: Split the sentence into individual words"
"""

# def censor(text, word):
#     phrase = text.split()
#     censor_word = ("*" * len(word))
#     censored_phrase = []

#     for i in phrase:
#         if i in word:
#             censored_phrase.append(censor_word)
#         else:
#             censored_phrase.append(i)
#     return (" ".join(censored_phrase))


# print (censor("hello my cathAR scratch darling","CATHAR"))


"""
METHOD 2: Search for the Cartesian product literal value, 
    and replace within the string
"""

# STEP 1: What are all variations of the bad word? (Cartesian)
from itertools import product

# THIS FUNCTION IS A COLLECTION:
# SOURCED FROM: 
# http://stackoverflow.com/a/20063816/7546949

# def censor_word_iterations(bad_word):
#     l = [(c, c.upper()) if not c.isdigit() else (c,) for c in bad_word.lower()]
#     # * collects all the positional arguments in a tuple
#     # ** collects all the keyword arguments in a dictionary
#     bad_word_list = ["".join(item) for item in product(*l)]
#     return (bad_word_list)


# def censor_b(text, word):
#     phrase = text.split()
#     censor_word_variations = censor_word_iterations(word)
#     censor_word_replacement = ("*" * len(word))
#     censored_phrase = []

#     for i in phrase:
#         if i in censor_word_variations:
#             censored_phrase.append(censor_word_replacement)
#         else:
#             censored_phrase.append(i)
#     return (" ".join(censored_phrase))


# print (censor_b("hello my cathAR scratch darling","CATHAR"))


"""
TAKING LISTS AS ARGUMENTS
"""

# def count(sequence, item):
#     """
#     sequence = list arrary
#     item     = search string (int or string or [])
#     """

#     scan_list = []
#     count = 0

#     for i in sequence:
#         if i == item:
#             count += 1
#         else:
#             count = count

#     return count

# print (count([1,2,1,1, [], "food"], []))



"""
PURIFY - FILTERING A LIST - REMOVE ALL ODD NUMBERS
"""

# def purify(sequence):
#     """
#     requires list of numbers
#     """
#     cleansed_list = []

#     for i in sequence:
#         if i % 2 == 0:
#             cleansed_list.append(i)

#     return (cleansed_list)

# print (purify([1,2,3]))


"""
PRODUCT / FUNCITON FOR MULTIPLICATION
"""

# def product(sequence):
#     """
#     requires list of numbers
#     """

#     mult_total = 1

#     for i in sequence:
#         mult_total = mult_total * i
#         print (mult_total)

#     return (mult_total)

# print(product([4, 5, 5]))



"""
REMOVE DUPLICATES - Remove elements of the list that are the same
"""

# def remove_duplicates(sequence):
#     """
#     takes in a list and removes duplicate values
#     we're basically turning the list into a set
#     """

#     setted_list = []

#     for i in sequence:
#         if i not in setted_list:
#             setted_list.append(i)

#     return setted_list


# print (remove_duplicates([1,1,2,3, 52, 9, 9, 8, 1, 0, "string"]))


"""
FINDING THE MEDIAN WITHIN A LIST (the middle value)
"""


def median(sequence):
    """
    sequence = array of integers and/or float
    """

    seq_list = sorted(sequence)
    length = len(seq_list)
    med_value_even = int((length / 2) - 1)   # for sequences w/ even # length
    med_value_odd = int((length - 1) / 2)    # for sequences w/ odd # length
    print ("SORTED LIST: %s" % seq_list)

    if length % 2 == 0:
        return (float(seq_list[med_value_even] + seq_list[med_value_even + 1]) / 2)     # explicit float is for Python 2

    else:   # if not even number, than length % 2 != 0
        return float(seq_list[(med_value_odd)])


print (median([4, 5, 5, 4]))


