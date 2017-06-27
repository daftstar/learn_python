#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.


Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys




# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

filename = 'alice.txt'


# ################## TEXT-2-DICT GROUP ########################
# Function to strip non meaningful words

def cleanse_words(words_to_cleanse):
    # ignore = ["the", "a", "it", "in", "but", "all", "on", "as", "to", "i", "so", "of", "was", "be", "this", "they", "not", "for", "and", "at", "had", "her", "he", ""]
    ignore = ["would", "what", "what'"]
    new_words = []

    for word in words_to_cleanse:
        if word not in ignore and len(word) >= 4:
            new_words.append(word.lower())

    return new_words


# Function that converts textfile to individual words
def file_convert_to_words(filename):
    words_file = open(filename, 'r')
    text_to_words = []

    for line in words_file:
        words = line.split()

        for word in words:
            word = word.lower()
            text_to_words.append(word)

    words_file.close()
    return text_to_words


def words_to_frequencies(filename):
    words_to_cleanse = file_convert_to_words(filename)
    cleansed_words = cleanse_words(words_to_cleanse)

    word_count = {}
    for word in cleansed_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# ############### END GROUP ####################

# dow = dictionary of words
def most_common_words(dow):
    """
    INPUT: dow = dictionary of words
    Results from output of words_to_frequencies(filename)

    OUTPUT: words 
    """
    values = dow.values()
    unique_list = []

    for i in values:
        if i in unique_list:
            pass
        else:
            unique_list.append(i)

    ordered_list = sorted(unique_list)

    high = len(ordered_list)
    low = high - 20
    top_twenty_words = ordered_list[low:high]


    count = 0
    top_twenty_dict = {}

    for key, value in dow.items():
        if value in top_twenty_words:
            top_twenty_dict[key] = value


    #     if value in top_twenty_words:
    #         top_twenty_dict[key] += 1
    #     else:
    #         top_twenty_dict[key] = 1

    #         print ("True")
    #         count += 1
    # print (count)
            # print (key, value)



    print (len(top_twenty_dict))
    return top_twenty_dict






story_word_count_dict = words_to_frequencies(filename)
print (most_common_words(story_word_count_dict))






# Function that creates count of each word in newly created
# cleansed list of words
# def words_to_dict(text_to_words):
#     words_for_review = 


# def file_convert_to_words(filename):
#     words_file = open(filename, 'r')
#     word_count = {}
    
#     for line in words_file:
#         words = line.split()

#         for word in words:
#             word = word.lower()

#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1

#     return (word_count)
#     words_file.close()



# def most_common_words(story_words):
#     # Get values from dictionary
#     values = story_words.values()
#     best = max(values)
#     print (values)
#     print (max(values))




# story_words = file_convert_to_words(filename)
# print (story_words)
# print (most_common_words(story_words))











# def top_twenty(filename):
#     word_count = file_convert_to_words(filename)
#     values = word_count.values()
#     highest_count = max(values)
#     print (highest_count)

#     print (values)
#     print ()






    # return (word_count)





# def print_words(path):
#     word_count = word_count_dict(path)
#     words = sorted(word_count.keys())
#     print (type(words))
#     for word in words:
#         print (word, word_count[word])
#     # return words

# print (print_words(path))
    









# # This basic command line argument parsing code is provided and
# # calls the print_words() and print_top() functions which you must define.
# def main():
#     if len(sys.argv) != 3:
#         print ('usage: ./wordcount.py {--count | --topcount} file')
#         sys.exit(1)

#     option = sys.argv[1]
#     filename = sys.argv[2]
#     if option == '--count':
#         print_words(filename)
#     elif option == '--topcount':
#         print_top(filename)
#     else:
#         print ('unknown option: ' + option)
#         sys.exit(1)


# if __name__ == '__main__':
#     main()
