# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained
# in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5


# define "vowels"
# set up a counter variable to store instances of vowels 
# iterate through each letter and check to see if it's a vowel
# when reached the end of the string, print the total number of vowels. 


s = 'azcbobobegghakl '
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
print ("Number of vowels: %d " % numVowels)



