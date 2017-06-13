"""
BISECTION SEARCH ON SQUARE ROOT
square root of a number is between 1 and x.
Instead of trying things starting at 1, pick a number
in the middle of the range from 1 to x
"""

x = 25
epsilon = 0.01
num_guesses = 0

low = 1
high = x
new_mid = (high + low) / 2.0

# the goal is to get the square of the middle value
# minus X, between 0 and 0.01
# new_mid is effectively our 'guess'

while abs((new_mid ** 2) - x) >= epsilon:
    print ('low: %s, high: %s, mid: %s' % (low, high, new_mid))
    num_guesses += 1

    # if mid value squared is less than 25,
    # set the low bound as the current mid-value
    if new_mid ** 2 < x:
        low = new_mid

    # otherwise, set the high bound as the current mid-value
    else:
        high = new_mid

    # change the new mid-value based on the new low and high values
    new_mid = (high + low) / 2

print ("")
print ('number of guesses: %s' % num_guesses)
print ("%s is close to the square root of %s" %(new_mid, x))



# ################################################
"""
BISECTION SEARCH ON CUBE ROOT
"""

cube = 27
epsilon = 0.01

low = 1
high = cube
guess = (high + low) / 2

num_guesses = 0


while abs((guess ** 3) - cube) >= epsilon:
    print ('low: %s, high: %s, guess: %s' % (low, high, guess))
    if guess ** 3 < cube:
        low = guess
    else:
        high = guess

    guess = (high + low) / 2.0
    num_guesses += 1
print ("")
print ('number of guesses: %s' % num_guesses)
print ("%s is close to the cube root of %s" %(guess, cube))



#_______
print ("\n____________________________________\n")
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))