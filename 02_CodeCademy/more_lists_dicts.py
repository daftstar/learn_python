webster = {
    "Aardvark": "A star of a popular children's cartoon show.",
    "Baa": "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}


"""
FINDING AND PRINTING KEYS
"""

for key in webster:
    print (key)

print ("")


"""
FINDING AND PRINTING KEY VALUES
"""

for key in webster:
    print (webster[key])



""" 
NESTING IF STATEMENTS IN FOR LOOPS
"""

# numbers = [1, 3, 4, 7]


# for number in numbers: 
#     if number > 6:
#         print (number)
# print ("We printed 7.")


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in a:
    if i % 2 == 0:
        print (i)
