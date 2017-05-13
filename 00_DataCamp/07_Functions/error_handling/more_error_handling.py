# #####################################################
# ERROR HANDLING W/ TRY EXCEPT
# #####################################################


def shout_echo(word1, echo=1):
    """ Concat echo copies of word1 and three exclamation
    marks at end of sting """

    # Initialize empty strings: echo_word, shout_words
    echo_word = ""
    shout_words = ""

    # Add exception handling with try-except
    try:
        # Concat echo copies of word1
        echo_word = word1 * echo

        # Concat '!!!' to echo_word:
        shout_words = echo_word + "!!!"
    except:
        print ("word1 must be a string and echo must be an integer")

    return (shout_words)


print (shout_echo("particle", "ddj"))
# word1 must be a string and echo must be an integer


# #####################################################
# ERROR HANDLING BY RAISING AN ERROR
# #####################################################

def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word


# Call shout_echo
shout_echo("particle", echo=2)   # change echo to negative value
