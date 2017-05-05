"""
SIMPLE FUNCTION WITH RETURN OPERATION
"""


def add_function(x, y):
    return x + y


print (add_function(1, 2))


"""
SIMPLE FUNCTION WITH CONCATENATION
"""


def string_function(s):
    return str(s) + "world"


print (string_function("Hello"))


"""
PASSING LISTS TO FUNCTIONS
"""


def list_function(x):
    return x


n = [1, 2, 3]
print (list_function(n))


"""
MODIFYING AN ELEMENT OF A LIST FUNCTION
"""


# def double_first(n):
#     n[0] = n[0] * 2


# numbers = [1, 2, 3, 5]
# double_first(numbers)
# print (numbers)


def list_function(x):
    x[1] = x[1] + 3
    return x


n = [3, 5, 7]
print (list_function(n))


"""
LIST MANIPULATION WITHIN FUNCTIONS
"""

n = [3, 5, 7]

# appending an item to a list
def list_extender(lst):
    lst.append("nice9")
    return lst

print (list_extender(n))


""" 
LIST ITERATION
"""


n = [3, 5, 7]


def print_list(x):
    for i in x:
        print (i)


print_list(n)


"""
MODIFYING ELEMENTS IN A LIST WITHIN A FUNCTION
"""

n = [100, 1000, 10000]


"""
THIS FUNCTION WILL ITERATE THROUGH VALUES, BUT WILL NOT WRITE ANY VALUES
def double_list(x):
    for i in x:
        i = i * 2
    return (x)
"""


def double_list(x):
    for i in range(0, len(x)):  # this writes back to the original list
        x[i] = x[i] * 2
    return x


print(double_list(n))


"""
PASSING RANGES INTO FUNCTIONS


PYTHON 3 
In python3 range is a generator object - 
    it does not return a list. Convert it to a list 
    before printing / returning
    http://stackoverflow.com/questions/20484195/typeerror-range-object-does-not-support-item-assignment

"""

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x



print (my_function(list(range(0, 3))))


"""
ITERATING OVER A LIST IN A FUNCTION
Method 1: useful to loop throught the list, but not possible
    to modify the list this way. 

Method 2: uses indexes to loop through the list, also making 
    it POSSIBLE to modify the list if needed. 
"""

# METHOD 1
list = [1, 2, "jsdfj"]
for item in list:
    print (item)


# METHOD 2
for i in range(len(list)):
    print (list[i])

numbers = [3, 5, 7]


def total(numbers):
    result = 0

    # for n in numbers:
    #     result = result + n
    # return result
    # OOORRRR YOU CAN DO IT THIS WAY

    for n in range(0, len(numbers)):
        result = result + numbers[n]
    return result


print (total(numbers))


"""
USING STRINGS IN LISTS IN FUNCTIONS
"""

n = ["Michael", "Liberman"]


def join_strings(words):
    result = ""

    for word in words:
        result = result + word
    return result


print (join_strings(n))


"""
USING TWO LISTS AS TWO ARGUMENTS IN A FUNCTION
"""

a = [1, 2, 3]
b = [4, 5, 6]

print (a + b)


def join_lists(x, y):
    return x + y


print (join_lists(a, b))


"""
USING A LIST OF LISTS IN A FUNCTION - HOW TO ACCESS SUBLISTS
"""

list_of_lists = [[1, 2, 3], [99, 100, 101]]

print (list_of_lists + a + b)

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


def flatten(lists):
    results = []

    for numbers in lists:
        for item in numbers:
            results.append(item)
    return results


print (flatten(n))


"""
JOINING / REMOVING CHARACTERS IN A LIST

"""

letters = ["a", "b", "c", "d"]

print (" ".join(letters))
print (" --- ".join(letters))
