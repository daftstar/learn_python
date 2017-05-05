print ('Welcome to the Pig Latin Translator!')

# original = raw_input("Enter a word:")
original = "terrible"
pyg = "ay"


# if (len(original) > 3 and original.isalpha() == True):
if len(original) > 3 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = (word[1:len(word)]) + first + pyg
    # above is condensed version of below
    # new_word = word + first + pyg
    # new_word = (new_word[1:len(new_word)])
    print (new_word)

else:
    print ("empty")
