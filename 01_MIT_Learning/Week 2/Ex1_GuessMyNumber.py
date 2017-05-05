# In this problem, you'll create a program that guesses a secret number!


# The program works as follows: you (the user) thinks of an integer between
# 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input
# - is its guess too high or too low? Using bisection search,
# the computer will guess the user's secret number!

# Number between 1 & 100


# secretNumber = "please think of a number between 0 and 100."


# userInput = ""
# low = 0
# high = 100
# x = int((high + low) / 2.0)

# choiceAsk = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
# # guessCounter = 0


# print ("Please think of a number between 0 and 100.")


# while userInput != 'c':
#     print ("Is your secret number: %s?" % int(x))
#     userInput = input(choiceAsk)

#     if userInput == 'h':
#         high = x
#         x = round(((x + low) / 2), 0)
#     elif userInput == 'l':
#         low = x
#         x = round(((x + high) / 2), 0)
#     elif userInput != 'c':
#         print ("please enter a valid value of: c, l or h")

# print ("Game over. Your secret number was: %s" % int(x))



# ## TO ACCOMODATE TEST CASES - ROUNDING CAUSING PROBLEMS ###


# userInput = ""
# low = 0
# high = 100
# x = int((high + low) / 2.0)

# choiceAsk = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "

# print ("Please think of a number between 0 and 100.")

# while userInput != 'c':
#     print ("Is your secret number: %s?" % int(x))
#     userInput = input(choiceAsk)

#     if userInput == 'h':
#         high = int(x)
#         x = int((x + low) / 2)
#         print ("x is now at %s" % x)
#         print ("##########\n")

#     elif userInput == 'l':
#         low = int(x)
#         x = int((x + high) / 2)
#         print ("x is now at %s" % x)
#         print ("##########\n")

#     elif userInput != 'c':
#         print ("please enter a valid value of: c, l or h")

# print ("Game over. Your secret number was: %s" % int(x))




# ## CODE OPTIMIZATION - REDUCING INT OCCURRENCES, (ROUNDING CAUSING PROBLEMS) ###


# userInput = ""
# low = 0
# high = 100
# x = int((high + low) / 2.0)

# print("#######")
# print ("x is type: " + str(type(x)))


# choiceAsk = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "

# print ("Please think of a number between 0 and 100.")

# while userInput != 'c':
#     print ("Is your secret number: %s?" % x)
#     userInput = input(choiceAsk)

#     if userInput == 'h':
#         high = x
#         x = int(((x + low) / 2))
#         # print ("x is type: " + str(type(x)))
#         # print ("low is type: " + str(type(low)))
#         # print ("high is type: " + str(type(high)))
#         # print ("x is now at %s" % x)
#         # print ("##########\n")

#     elif userInput == 'l':
#         low = x
#         x = int((x + high) / 2)

#     elif userInput != 'c':
#         print ("please enter a valid value of: c, l or h")

# print ("Game over. Your secret number was: %s" % x)







# ## CODE OPTIMIZATION - REDUCING INT OCCURRENCES, (ROUNDING CAUSING PROBLEMS) ###


import os


def cls():  # clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')


low = 0
high = 100
x = int((high + low) / 2.0)

userInput = ""
numberGuesses = 0
isOdd = ""
valueOdd = ""



choiceAsk = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "

print ("Please think of a number between 0 and 100.\n")


# while isOdd != 'quit':
#     isOdd = input("Is your number odd or even? ").lower()

#     if isOdd == "odd":
#         x = int(x + 1)
#         valueOdd = True
#         break

#     elif isOdd == "even":
#         x = int(x)
#         valueOdd = False
#         break

#     elif isOdd != "odd" or isOdd != "even":
#         print ("please type in either 'odd' or 'even'.")


# numberGuesses += 1

print ("\nYou have an %s number" % isOdd)
print ("Number of Guesses: %s.\n" % numberGuesses)
print ("Let's guess your number\n")

while userInput != 'c':
    print ("Is your secret number: %s?" % x)
    userInput = input(choiceAsk)
    numberGuesses += 1

    print ("that's %s guesses so far.\n" % numberGuesses)
    cls()  # clear the terminal screen

    if userInput == 'h':
        high = x
        x = int(((x + low) / 2))

    elif userInput == 'l':
        low = x
        x = int((x + high) / 2)

    elif userInput != 'c':
        print ("please enter a valid value of: c, l or h")

print ("\n\n")
print ("Game over. Your secret number was: %s" % x)
print ("TOTAL Guesses: %s.\n" % numberGuesses)











# while userInput != 'c':
#     print ("Is your secret number: %s?" % x)
#     userInput = input(choiceAsk)
#     numberGuesses += 1

#     print ("that's %s guesses so far.\n" % numberGuesses)
#     cls()  # clear the terminal screen

#     if userInput == 'h':
#         high = x
#         x = int(((x + low) / 2))

#     elif userInput == 'l':
#         low = x
#         x = int((x + high) / 2)

#     elif userInput != 'c':
#         print ("please enter a valid value of: c, l or h")

# print ("\n\n")
# print ("Game over. Your secret number was: %s" % x)
# print ("TOTAL Guesses: %s.\n" % numberGuesses)








