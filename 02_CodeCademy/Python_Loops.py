"""
WHILE w/ ELSE vs. IF w/ ELSE

While / else

    Something completely different about Python is the while/else construction.

    While/else is similar to if/else, but there is a difference:
    the else block will execute anytime the loop condition is
    evaluated to False. This means that it will execute if the
    loop is never entered or if the loop exits normally.
    If the loop exits as the result of a break,
    the else will not be executed.

"""

# from random import randint

# print ("Lucky numbers! 3 numbers will be generated.")
# print ("If one of them is a '5', you lose")

# count = 0

# while count < 3:
#     num = randint(1, 6)
#     print ("You rolled a %s" % num)

#     if num == 5:
#         print ("Sorry, you lose!")
#         break
#     count += 1

# else:
#     print ("You Win!")


"""
ANOTHER EXAMPLE!
"""

# random_number = randint(1, 10)
# guesses_left = 3

# print ("Guess the random number!\n")

# while guesses_left != 0:
#     # user_guess = int(input("What's your guess?"))
#     user_guess = 7

#     if user_guess == random_number:
#         print ("You win!")
#         break
#     elif user_guess != random_number:
#         guesses_left -= 1
# else:
#     print ("You Lose.")




""" 
EXPLORING FOR LOOPS
"""

# print ("Counting")

# for i in range(20):
#     print (i)


"""
USER INPUTS WITHIN FOR LOOPS

hobbies = []

for i in range(3):
    hobby = raw_input("What's your hobby: ")
    hobbies.append(hobby)

print (hobbies)

"""



""" 
LOOP ITERATION
"""

# thing = "spam!"

# for c in thing:
#     print (c)
#     print ("")


"""
STRING MANIPULATION WITHIN LOOPS
"""

# phrase = "A bird in the hand..."

# for char in phrase:
#     if char == "A" or char == "a":
#         print ("X", end ="")  # this prevents new line creation
#     else:
#         print (char, end ="")

"""
*************************************************
LOOPING THROUGH A DICTIONARY!!!!
"""


d = {
    'x': 9, 'y': 10, 'z': 20
    }

for key in d:
    if d[key] == 10:            # key = 'y', [value] = 10
        print ("this dictionary item is: %s" % key)


"""
ACCESSING DICTIONARY KEY & VALUE
"""

d = {
    'a': 'apple',
    'b': 'berry',
    'c': 'cherry'
}


for key in d:
    # print ("key is %s" % key)
    # print ("value is %s" % d[key])
    print ("KEY: %s, VALUE: %s" % (key, d[key]))


"""
ENUMERATE FUNCTION: COUNTING AS YOU GO

    A weakness of using this for-each style of iteration is that
    you don't know the index of the thing you're looking at.

    At times it is useful to know how far into the list you are.
    enumerate function helps with this by supplying a corresponding
    index to each element in the list that you pass it.

    Each time you go through the loop, index will be one greater,
    and item will be the next item in the sequence.

    Very similar to using FOR loop with a list, except this gives
    an easy way to count how many items we've seen so far.

"""

choices = ['pizza', 'pasta', 'salad', 'nachos']

print ("Your choices are: ")

for index, item in enumerate(choices):  # enumerate auto adds a counter
    print (index + 1, item)             # +1 so first choice != 0


list_a = [3, 9, 17, 15, 19]
list_b = [2, 3, 8, 10, 30, 40, 50, 60, 70, 80, 90]


"""
HANDLING MULTIPLE LISTS WITHIN ONE LOOP:

    It's common to need to iterate over two lists at once.
    This is where the built-in zip function works.

    zip creates pairs of elements when passes two lists.
    zip will stop at the end of the shorter list.

    zip can handle 3 or more lists as well.

"""

for a, b in zip(list_a, list_b):
    if a > b:
        print (a)
    elif a < b:
        print (b)


"""
FOR / ELSE
    Just like IF and WHILE statements,
    FOR loops can also have ELSE statements.

    In this case, ELSE is executed after the for,
    but ONLY if the for ends normally / without a BREAK

    FOR EXAMPLE:
"""

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ("You have...")

for f in fruits:
    if f == 'tomato':
        print ('a tomato is not a fruit!')
        break                              # this prevents the else
    print ('A', f)
else:
    print('A fine selection of fruits')

