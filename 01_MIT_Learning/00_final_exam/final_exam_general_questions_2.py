# 1 - You have the following class hierarchy: 

class A(object):
    def foo(self):
        print('hi')


class B(A):
    def foo(self):
        print('bye')

a = A()
print (type(a))

b = B()
print (type(b))

# Which of the following is correct?
# - a = A(), we say that a is an instance of A
# - when b = B(), we say that b is a subclass of A
# - both of the above
# - neither of the above

# Answered: a = A(), we say that a is an instance of A
# Correct Answer: a = A(), we say that a is an instance of A


# 2 - Consider the function f below.
# What is its Big O complexity?


def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print(m)
    for i in range(n):
        g(n)

print (f(8))    # returns None, because m = 0

# - O(1)
# - (O(log(n)))
# - O(n)
# - O(n^2)

# Answered O(1) because this will always return None
# Correct Answer: Incorrect :(  - probably was n^2


# 3 - A dictionary is an immutable object because
# its keys are immutable.
# - True
# - False, because its keys can be mutable >> KEYS MUST BE IMMUTABLE
# - False, because a dictionary is mutable


SCRABBLE_LETTER_VALUES = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10
}


# for a, b in SCRABBLE_LETTER_VALUES.items():
#     print (a, b)

print (SCRABBLE_LETTER_VALUES["l"])
SCRABBLE_LETTER_VALUES["l"] = 939393939
print (SCRABBLE_LETTER_VALUES["l"])


# Answered: False, because a dictionary is mutable
# Correct Answer: False, because a dictionary is mutable


# 4 - Consider the following two functions and select the correct choice below:

def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1          # O(len n)
    return answer


def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1: 
        return 1.0
    else: 
        return n*foo_two(n-1)   # O(n * n^2)

# - worst case O of foo_one is worse than foo_two
# - worst case O of foo_two is worse than foo_one
# - worst case O of foo_one and foo_two are the same
# - Impossible to compare

# Answered foo_two is worse (because of recursion)
# Correct Answer: Incorrect :(



