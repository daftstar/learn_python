def new_line():
    print ("\n___________________________\n")

# #################### PROBLEM 1 ############################
# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained
# in the string s. 

# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
#     Number of vowels: 5


s = "azcbobobegghakl"

vowel_count = 0
for i in s:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel_count += 1

print ("Number of vowels: %s" % vowel_count)
new_line()


# #################### PROBLEM 2 ############################
# Assume s is a string of lower case characters.
# Write a program that prints the number of times
# the string 'bob' occurs in s. For example,
# if s = 'azcbobobegghakl', then your program
# should print:
#     Number of times bob occurs is: 2

# set string as s
s = 'azcbobobegghakl'

# initialize counters
bob_count = 0
index_counter = 0

# check if every three letters = 'bob'
# if not, then move the counter up 1, and check
# if the next three letters = 'bob'

for i in s:
    if s[index_counter:index_counter + 3] == 'bob':
        bob_count += 1
    index_counter += 1
print (bob_count)
new_line()


# #################### PROBLEM 3 ############################
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s
# in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program
# should print
#     Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print
#     Longest substring in alphabetical order is: abc


# compare current letter to next letter
# if current letter is > previous letter,
#     add letter to string
#     move to next letter

# if next letter is < previous letter,
#     store string as previous longest and erase string
#     move to next letter

# keep doing this until you get to the last letter

s = 'zyxwvutsrqponmlkjihgfedcba'

# initialize comparison strings
string = ""
longest_string = ""

# use range to set i as the counter. We can use i to define
# which character we're evaluating.
for i in range(len(s)):
    # we could push the below to global variables, but seems sloppy
    # at beginning of counter, set values for comparison strings
    if i == 0:
        string = s[0]
        longest_string = s[0]

    # once we're past the starting point, compare the previous character
    # to the current character (s[index value = i])
    # if the prev character is <= the next character,
    # append the current character to var string     
    elif string[-1] <= s[i]:
        string += s[i]

    # otherwise, overwrite the var string with the current character
    else:
        string = s[i]

    # while we're in the original if loop, check if
    # var string is now longer than var longest_string.
    # If so, overwrite var longest_string with var string
    if len(string) > len(longest_string):
        longest_string = string

print ("Longest substring in alphabetical order is: %s" % longest_string)

# Code without comments:
"""
s = "kjshduihwnsdmnzclkjwabcsddeegoppzsdfkljhsdfiul"
string = ""
longest_string = ""

for i in range(len(s)):
    if i == 0:
        string = s[0]
        longest_string = s[0]
    elif string[-1] <= s[i]:
        string += s[i]
    else:
        string = s[i]

    if len(string) > len(longest_string):
        longest_string = string

print ("Longest substring in alphabetical order is: %s" % longest_string)
"""

# ########################

# Code without comments / doing it the janky way by setting static vars globally:

"""
s = "kjshduihwnsdmnzclkjwabcsddeegoppzsdfkljhsdfiul"
string = s[0]
longest_string = s[0]

for i in range(1, len(s)):
    if string[-1] <= s[i]:
        string += s[i]
    else:
        string = s[i]

    if len(string) > len(longest_string):
        longest_string = string

print ("Longest substring in alphabetical order is: %s" % longest_string)


"""
