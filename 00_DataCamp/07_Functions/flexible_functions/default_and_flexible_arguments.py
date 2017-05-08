def newline():
    return ("\n_____________________________\n")


# #######################################
# DEFAULT PARAMETERS:
# #######################################


def power(num, n=2):
    """ raise num to the power of n """
    new_value = num ** n
    return (new_value)


# use default value
print (power(3))
print (newline())

# use custom value
print (power(3, 10))
print (newline())

#
# #######################################
# FLEXIBLE ARGUMENTS: *args:
# #######################################


def add_all(*args):
    """ Sum all the values in *args together. """
    sum_all = 0

    for i in args:  # this turns all params into a tuple
        sum_all = sum_all + i

    return (sum_all)


print (add_all(1, 3, 4, 2, 2, 3))
print (newline())


#
# #######################################
# FLEXIBLE ARGUMENTS: *keword arguments (**kwargs):
# arguments preceded by identifiers
# #######################################

def print_all(**kwargs):
    """ print out key-value pairs in **kwargs """

    # print out the key-value pairs
    for key, value in kwargs.items():
        print (key + ": " + value)


print_all(name="Nik Daftary", employer="me")
