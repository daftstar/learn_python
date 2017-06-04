# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging.
# We encourage you to work smart.
# If you've spent more than a few hours on this problem,
# we suggest that you move on to a different part of the course.

# WHAT WE'RE TRYING TO DO: 
# what's the longest sequence of ordered letters in an string? 

# compare if the a letter in the string comes after the prior letter
# if so, continue on, and increment the counter. 
# when it stops, store that sequence of letters. 

# at the new starting point, redo the prior loop until a new 
# sequence of sequential letters is found. 
# At the stopping point, compare if the new ordered string is 
# greater than the length of the first ordered string. 
# If not, discard the new sequence and resume the first loop. 
# If so, replace the contents of the longest string sequence. 


# Step 1: Define all variables
#     s = 'jlsdlkjfsdlkfjsdjsasdscmnklwnjioweddlqjabcdefgazhijklmnopqrs'
#     string = '' # this defines string as an empty string
#     previous = ''
#     current = ''



# s = 'czqriqfsqteavw'

# string = ''

# tempIndex = 0
# prevLetter = ''
# currLetter = ''

# index = 0
# while index < len(s):
#     currLetter = s[index]
#     # print (currLetter) - used for debugging 
#     if index > 0:
#         if currLetter < prevLetter: 
#             if len(s[tempIndex:index]) > len(string):
#                string = s[tempIndex:index]
#                print (string)
#             tempIndex=index
#         elif index == len(s)-1:
#             if len(s[tempIndex:index+1]) > len(string):
#                string = s[tempIndex:index+1]
#                print (string)
#     prevLetter = currLetter
#     index += 1
# print ('Longest substring in alphabetical order is: %s' % string)



s = 'czqriqfsqteavw'

string = ''
index = 0  # this is the global position
tempIndex = 0  # this is what we reset to 

prevLetter = ''
currLetter = ''


while index < len(s):
    currLetter = s[index]  # sets the position of what we're evaluating
    print (currLetter) # - used for debugging 
    if currLetter < prevLetter:  # this is a literal comparison
        if len(s[tempIndex:index]) > len(string):
            string = s[tempIndex:index]
            print (string) # - used for debugging
        tempIndex = index  # this locks in the position of the character evaluator
    elif index == len(s)-1:  # move back one character because we need to include this in the next evaluation
        if len(s[tempIndex:index + 1]) > len(string):  # we increment by 1 because we need to see if the previous count is greater than the current count (vs. equal to)
            string = s[tempIndex:index + 1]
            print (string) # - used for debugging
    prevLetter = currLetter  # keeps the algo moving forward. 
    index += 1

print ('Longest substring in alphabetical order is: %s' % string)










