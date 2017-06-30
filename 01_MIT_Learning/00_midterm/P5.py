# Write a Python function that takes in a string and prints out a version
# of this string that does not contain any vowels,
# according to the specification below.
# Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

# For example,
#   if s = "This is great!"
#   then print_without_vowels will print:
#   Ths s grt!

# VERSION 2: USING REPLACE

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters
    appear in the same order they appear in s.
    Prints this version of s.

    Function only prints, does not return anything
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in s:
        if letter.lower() in vowels:
            s = s.replace(letter,"")
    print (s)

s = "This is GREAT!"
print (print_without_vowels(s))






# VERISON 1: CHECKING TRUTHINESS

# def print_without_vowels(s):
#     '''
#     s: the string to convert
#     Finds a version of s without vowels and whose characters
#     appear in the same order they appear in s.
#     Prints this version of s.

#     Function only prints, does not return anything
#     '''
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     new_string = ""
#     for i in s:
#         if i.lower() not in vowels:
#             new_string += i

#     print (new_string)


# # s = "This is great!"
# s = "This is GREAT!"


# print (print_without_vowels(s))