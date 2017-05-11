# lambdas are functions on the fly
# WITHOUT LAMBDA


def new_line():
    print ("\n_____________________________\n")


def raise_to_power(x, y):
    """ raise int x to the power of int y """
    raised = x ** y
    return (raised)


print (raise_to_power(4, 2))
new_line()

# WITH LAMBDA
# best not to use all the time - can be dirty
# see error on line 19


l_raise_to_power = lambda x, y: x ** y
print (l_raise_to_power(8, 4))
new_line()


# BETTER USE OF LAMBDAS
nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num ** 2, nums)

print (square_all)  # <map object at 0x10294b320>
print (list(square_all))
new_line()


# ORIGINAL WAY
def add_bangs_def(a):
    return (a + "!!!")


# DIRTY WAY
add_bangs = lambda a: a + "!!!"

print (add_bangs_def("hello"))
print (add_bangs("hello"))
new_line()


# ORIGINAL WAY:
def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words


# DIRTY / SHORT LAMBDA WAY

echo_word = lambda word1, echo: word1 * echo
print (echo_word("hey", 2))
