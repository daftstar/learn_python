# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which
# the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program
# should print

#     Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print
#     Longest substring in alphabetical order is: abc


s = 'azcbobobegghakl'

string = ""
longest_string = ""

for i in range(len(s)):
    if i == 0:
        string = s[0]
    elif string[-1] <= s[i]:
        string += s[i]
    else:
        string = s[i]

    if len(string) > len(longest_string):
        longest_string = string
print (longest_string)
