# EQUATION = g - (((g ** 2) - y) / (2 * g))

y = 25
guess = y / 2.0  # randomly chosen
numGuesses = 0

epsilon = 0.1


print ("guess #1 is: %s " % guess)

while abs(guess * guess - y >= epsilon):
    numGuesses += 1
   
    guess = guess - (((guess ** 2) - y) / (2 * guess))
    print ("guess #%s is: %s " % (numGuesses, guess))

print ("")
print ("Number of Guesses = %s" % numGuesses)
print ("Square root of %s is about %s" % (y, guess))




