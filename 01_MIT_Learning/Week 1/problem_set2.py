# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' 
# occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

# define string that we're looking for
# this will be the counter that we reference
# take in a string value, called 's'
# Look within the string to see if it contains the string we're looking for. 
# Continue searching within the string until you've reached the end. 


# look in the string for an instance of the word bob. 
# mark the first spot the string bob was found. 
# add 1 to the counter 
# move the search spot by 1 
# resume searching
# continue doing this until reached the end of the string. 


# ### BASELINE PRIMITIVE TO SEE IF SOMETHING EXISTS
# if searchString in s:
#     print ("yep, it exists")
#     stringCount += 1
#     print (stringCount)


# s = 'bobob'
# bobString = s.lower()

# count = 0
# searchValue = 'bob'

# totalCount = bobString.count(searchValue)

# print ("Number of times bob occurs is: %s" % totalCount)

# this solution doesn't work as it counts bobob as 
# having only 1 instance of bob. 

# ##################################################
# HERE'S A HARD CODED WAY TO PERFORM THE ABOVE, 
# we know the length of Bob
# ##################################################

# bobString = s.lower()
# count = 0

# for i in range(len(bobString)):
#     if bobString[i:i+3] == 'bob':
#         # print("bob was found at spot %s in the sequence\n" %i) #this is for debugging
#         count += 1

# print ("Number of times bob occurs is: %s" % count)

# ##################################################
# HERE'S A MORE FLEXIBILE WAY TO PERFORM THE ABOVE, 
# we know the length of Bob
# ##################################################




s = 'popoopopopppppoopppoppooooppopoppooppoooooopPPooposdfsdjhfjspop '  # this can be converted to ask for user input
lowercaseString = s.lower()  # to accomodate for mixed case strings

searchString = "pop"  # this can be converted to capture user input
lenSubString = len(searchString)  # the length of the string we're searching for

count = 0

for i in range(len(lowercaseString)):
    if lowercaseString[i:i+lenSubString] == searchString:
        print("%s was found at spot %s in the sequence\n" %(searchString, i)) #this is for debugging
        count += 1

print ("Number of times %s occurs is: %s" % (searchString, count))













