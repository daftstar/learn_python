# Functions can return multiple values as tuples. 
# Tuples are constructed using () 
# Tuples can be unpacked 

# def raise_to_both(value1, value2):
#     """ Raise value1 to the power of value2 and vice versa"""

#     new_value1 = value1 ** value2
#     new_value2 = value2 ** value1

#     new_tuple = (new_value1, new_value2)
#     return (new_tuple)


# print (raise_to_both(4, 3))

# ####################################
# BASIC MULTIPLE PARAMETERS
# ####################################

def shout(word1, word2):
    """ concat strings with 3 exclamation marks"""
    shout1 = word1 + "!!!"
    shout2 = word2 + "!!!"
    new_shout = shout1 + shout2
    return new_shout


yell = shout("congratulations", "you")
# print (yell)


# ####################################
# BASIC TUPLE UNPACKING
# ####################################

nums = (3, 4, 6)

# unpack nums into num1, num2, num3
num1, num2, num3 = nums

# Construct even_nums
even_nums = (2, num2, num3)
# print (even_nums)


# ####################################
# FUNCTIONS RETURNING MULTIPLE VALUES
# ####################################

def shout_all(word1, word2):
    """ concat two words with !!! """
    shout1 = word1 + "!!!"
    shout2 = word2 + "!!!"
    shout_words = (shout1, shout2)
    return (shout_words)


yell1, yell2 = shout_all("congratulations", "you")

print (type(shout_all("congratulations", "you")))
print (yell1)
print (yell2)





