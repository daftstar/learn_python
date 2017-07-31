# jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

"""
When we call a normal Python function, execution starts
at function's first line and continues until
a return statement, exception, or the end of the function
(which is seen as an implicit return None) is encountered.
Once a function returns control to its caller, that's it.

Any work done by the function and stored in local variables
is lost. A new call to the function creates everything from
scratch.

____________________________________________________________
USING YIELD VS. RETURN

There are times, though, when it's beneficial to have the
ability to create a "function" which, instead of simply
returning a single value, is able to yield a series of values.

return implies that the function is returning
control of execution to the point where the function was called.

"Yield," however, implies that the transfer of control is
temporary and voluntary, and our function expects to regain
it in the future.
"""


# ORIGINAL WAY  - USING RETURN - PRIME NUMBERS
# does not work with very large numbers, consumes too much
# memory. This is because current function only gets one chance
# to return results. Until then, everything is stored in memory.

import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True

        if number % 2 == 0:
            return False
#                           start            stop          step
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False

        return True
    return False


def get_primes(input_list):
    result_list = []
    for element in input_list:
        if is_prime(element):
            result_list.append(element)

    return result_list


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

print (get_primes(input_list))


# GENERATOR / YIELD WAY
# By using yields, lists don't need to be stored in memory.
# Each new value is returned as it is generated.

# To get the next value from a generator,
# we use the same built-in function as for iterators: next().
# yield is just return (plus a little magic)
# for generator functions

def simple_gen():
    yield 1
    yield 2
    yield 3


foo = simple_gen()
# print (foo.__next__())
# print (foo.__next__())
# print (foo.__next__())
# print (foo.__next__())  # StopIteration

# print ()
# for n in simple_gen():
#     print (n)


# When a generator function calls yield, the "state" of
# the generator function is frozen. The values of all
# variables are saved and the next line of code to be
# executed is recorded until next() is called again.


def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1


def is_prime(number):
    if number > 1:
        if number == 2:
            return True

        if number % 2 == 0:
            return False
#                           start            stop          step
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False

        return True
    return False




def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)

    for power in range(iterations):
        print(prime_generator.send(base ** power))


print (print_successive_primes(10))

