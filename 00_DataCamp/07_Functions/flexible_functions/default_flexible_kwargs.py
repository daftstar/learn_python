def newline():
    return ("\n_____________________________\n")


# #######################################
# 1. FUNCTIONS WITH 1 ARGUMENT:
# #######################################

# Define shout_echo
def shout_echo(word1, echo=1):
    """ Concat echo copies of word1 using *: echo_word """
    echo_word = word1 * echo

    # Concat "!!!" to echo_word: shout_word
    shout_word = echo_word + "!!!"

    return (shout_word)


# call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with "Hey" and echo=5
with_echo = shout_echo("Hey", 5)

print (no_echo)
print (with_echo)
print (newline())


#
# #############################################
# 2. FUNCTIONS WITH MULTIPLE DEFAULT ARGUMENTS:
# #############################################

def shout_echo(word1, echo=1, intense=False):
    """ Concat echo copies of word1 and three !!!
    marks at the end of the string. """

    # Concat echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Capitalize echo_word if intense is True
    if intense:
        # Capitalize and concat !!!: echo_word_new
        echo_word_new = echo_word.upper() + "!!!"
    else:
        # Concat '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + "!!!"

    return echo_word_new


# Call shout_echo() with "Hey", echo=5 and intense = True with big_echo
big_echo = shout_echo("Hey", 5, intense=True)

# Call shout_echo() with "Hey" and intense = True: big_no_echo
big_no_echo = shout_echo("Hey", intense=True)


print (big_echo)
print (big_no_echo)
print (newline())


#
# ##############################################
# 3. FUNCTIONS WITH VARIABLE LENGTH PARAMS/ARGS:
# ##############################################

def gibberish(*args):
    """ Concat strings in *args together """

    # Init an empty string: hodgepodge
    hodgepodge = ""

    # Concat strings in args
    for word in args:
        hodgepodge += word + " "

    return (hodgepodge)


one_word = gibberish("luke")
many_words = gibberish("luke", "leia", "han", "obi", "darth")

print (one_word)
print (many_words)
print (newline())


#
# ##############################################
# 3. FUNCTIONS WITH VARIABLE LENGTH KEYWORD ARGS:
# ##############################################

def report_status(**kwargs):
    """ print out the status of a movie character """

    print ("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        print (key + ": " + value)

    print ("\nEND REPORT")


report_status(name="luke", affiliation="jedi", status="missing")
report_status(name="anakin", affiliation="sith lord", status="deceased")

