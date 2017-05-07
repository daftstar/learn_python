# Nested Functions I
# ################################################
# 1. Input 3 words, output tuple with word + !!!
# ################################################


def three_shouts(word1, word2, word3):
    """ Returns a tuple of strings concat with !!! """

    def inner(word):
        """ takes one of above params and concats with '!!!' """
        return (word + "!!!")

    # Return tuple of strings
    # this is inefficent, but it works - too much repitition of inner()
    return (inner(word1), inner(word2), inner(word3))


# Call function
print (three_shouts("hey", "you", "guys"))


# Nested Functions II - Use Closure
"""Closures are inner functions that remember the state
of the enclosing scope when called. Anything defined
locally in the enclosing scope is available to the
inner function even when the outer function has
finished execution."""
# ################################################
# 2. Input 3 words, output tuple with word + !!!
# ################################################


def echo(n):
    """ Return the inner_echo function """

    def inner_echo(word1):
        """ this creates a callable function that
        concat n copies of param: word1 """
        echo_word = word1 * n
        return echo_word

    return (inner_echo)


# Create function from closure called twice that * 2
twice = echo(2)

# Create function from closure called thrice that * 3
thrice = echo(3)

print (twice("hello"), thrice("hello"))
