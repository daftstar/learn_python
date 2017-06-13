# #######################################################
# Create a program that guesses a secret number!

# The program works as follows:
# you (user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input -
# is its guess too high or too low?

# Using bisection search, the computer will guess the user's 
# secret number
# #######################################################

low = 0
high = 100
correct = False

print ("Please think of a number between 0 and 100!")

while correct == False:
    guess = (high + low) // 2
    print("Is your secret number %s?" % guess)
    
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if response == 'c':
        correct == True
        break

    elif response == 'l':
        # we guessed too low. Set the floor to the current guess (midpoint)
        low = guess

    elif response == 'h':
        # we guessed too high. Set the ceiling to the current guess (midpoint)
        high = guess

    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: %s' % guess)



# #########
# ORIGINAL WAY, HAD WAY TOO MUCH REPETITION
# ##########


# while correct == False:

#     print ("Is your secret number %s?" % guess)
#     response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

#     if response == "c":
#         print ("Game over. Your secret number was: ", mid)
#         correct = True
#         break

#     elif response == "l":
#         low = mid
#         mid = round((low + high) / 2)
#         guess = mid

#     elif response == "h":
#         high = mid
#         mid = round((low + high) / 2)
#         guess = mid

#     else:
#         response = input("Sorry, I did not understand your input.")