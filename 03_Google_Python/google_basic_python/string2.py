#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    """ function that edits the trailing 3 characters of a string
    with either "ing", "ly" or none. """
    # Init word
    word = ""

    # store last 3 characters of string
    ing = s[-3:]

    # replacement / append conditional
    if len(s) >= 3 and ing == "ing":
        word = s + "ly"
        # word = s.replace(ing, "ly")
    elif len(s) > 3:
        word += s + "ing"
    else:
        word = s

    return (word)


# # E. not_bad
# # Given a string, find the first appearance of the
# # substring 'not' and 'bad'. If the 'bad' follows
# # the 'not', replace the whole 'not'...'bad' substring
# # with 'good'.
# # Return the resulting string.
# # So 'This dinner is not that bad!' yields:
# # This dinner is good!


def not_bad(s):
    """ replaces any instance of "not .... bad" in string with "good" """
    # initialize search variables for phrase "not .... bad"
    word_start = "not"
    word_end = "bad"
    index_word_start = s.find(word_start)
    index_word_end = s.find(word_end)

    # test for conditional that not comes before bad for string replacement
    # added flexiblity to allow inclusion of trailing statements (new_string_trailing)
    if index_word_start < index_word_end:
        new_string_prefix = s[0:index_word_start]
        new_string_trailing = s[index_word_end + len(word_end):]
        new_string = new_string_prefix + "good" + new_string_trailing
    else:
        new_string = s

    return (new_string)


#
# # F. front_back
# # Consider dividing a string into two halves.
# # If the length is even, the front and back halves are the same length.
# # If the length is odd, we'll say that the extra char goes in the front half.
# # e.g. 'abcde', the front half is 'abc', the back half 'de'.
# # Given 2 strings, a and b, return a string of the form
# #  a-front + b-front + a-back + b-back
# def front_back(a, b):
#   # +++your code here+++



# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
# fixed test case to be more descriptive.print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
def test(got, expected):
    if got == expected:
        prefix = ' PASSED - '
    else:
        prefix = '        X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print ('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print ()
    print ('not_bad')
    # modified test to make more complex
    test(not_bad('This movie is not so bad you know'), 'This movie is good you know')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

#   # print
#   # print 'front_back'
#   # test(front_back('abcd', 'xy'), 'abxcdy')
#   # test(front_back('abcde', 'xyz'), 'abcxydez')
#   # test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
