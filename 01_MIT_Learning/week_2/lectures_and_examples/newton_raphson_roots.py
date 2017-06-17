"""
Netwon Raphson can be used to find
the real roots of many functions.

if a guess is an approximation to a root of a polynomial,
then (guess – p(guess))/p’(guess),
where p’ is the first derivative of p,
is a better approximation

"""
# EXAMPLE FOR SQUARE ROOT:
# Find x such that x**2 - 24 is < 0.01

epsilon = 0.01
k = 24.0
guess = k / 2.0



while abs((guess * guess) - k) >= epsilon:
    conditional_logic = abs((guess * guess) - k)
    print ("Guess: %s, conditional: %s" %(guess, conditional_logic))
    guess = guess - (((guess ** 2) - k)/(2 * guess))
    # print (guess)
    print()

print ("Square root of %s, is about, %s" %(k, guess))
