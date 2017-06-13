"""
This solution is very resource intensive. 
It doesn't start at an idea position, thus it iterates
through values that it does not need to. This can crash
a system depending on number of iterations required to reach
the answer.
"""



cube = 27
epsilon = 0.01

guess = 0.0
increment = 0.0001
num_guesses = 0

# use abs since epsilon is a positive value
# As long as the result of our forumla is > 0.01 and
# guess value is less than the cube value, keep doing ...

while abs((guess ** 3) - cube) > epsilon and guess <= cube:
    # print ("guess is %s, count is: %s" %(guess, num_guesses))
    guess += increment  # add 0.0001 to our guess value
    num_guesses += 1    # add 1 to the guess counter

print ('num guesses = ', num_guesses)

if (abs(guess ** 3) - cube) >= epsilon:
    print ('failed on cube root of ', cube)
else:
    print (guess, 'is closed to the cube root of, ', cube)