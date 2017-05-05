# def is_even(i):
#     # this is the docstring
#     """ 
#     Input: i, a positive int
#     Returns True if i is even, otherwise False
#     """
#     print ("hi")
#     # print (i % 2 == 0)
#     return i % 2 == 0  # this evaluates and returns if the condition is True or False to whatever called it. 

# is_even(2)




# def square(x):
#     """
#     x: int or float
#     """
#     return (x * x)

# print (square(4))



# def evalQuadratics(a, b, c, x):
#     """
#     a, b, c: numerical vlaues for the coefficients of a
#              quadratic equation.

#     x: numerical value at which to evaluate the quadratic.

#     equation: (a * (x * x)) + (b * x) + c
#     """

#     part1 = (a * (x * x))
#     part2 = (b * x)
#     part3 = c

#     return part1 + part2 + part3


# print (evalQuadratics(-5.02, -8.47, -7.44, -8.08))


# ### VARIABLE SCOPE ###

# def f(x):
#     '''
#     x: int or float
#     '''
#     x = x + 1
#     print ("In f(x) scope: x = %s \n" % x)
#     return x


# x = 3 
# print ("before function is run, x = %s \n" % x)
# z = f(x)  # this will invoke the f(x) function. A new scope is created. 
# print ("after function is run, x = %s \n" % x)
# print ("z is %s" % z)


# #### SCOPE EXAMPLE #### 

# def f(y):
#     x = 1
#     x += 1
#     print (x)

# x = 5
# f(x)
# print (x)



# def g(y):
#     print (x)
#     print (x + 1)

# x = 5
# g(x)
# print (x)

# print ("#########\n\n")




# def h(y):
#     x = 5
#     x = x + 1
#     print (x)

# x = 5
# h(x)
# print (x)







# ### FUNCTIONS AS ARGUMENTS ###


# def func_a():
#     print ("Inside func_a")
#     # because there is no return, returns literally None

# def func_b(y):
#     print ("Inside func_b")
#     return y


# def func_c(z):
#     print ("Inside func_c")
#     return z()


# print (func_a())
# print ("")

# print (5 + func_b(2))
# print ("")

# print (func_c(func_a))
# print ("")



# ### MORE SCOPE DETAILS ###

# def g(x):
#     def h():  # this creates a new scope, inherits from g(x)
#         x = 'abc'
#         print ("In scope h(), x is equal to: %s" % x)
#     x = x + 1
#     print ("in scope g(x): x is equal to: %s" % x)
#     h()
#     return x

# x = 3 
# z = g(x)

# print ("variable z is equal to g(x), where x is %s: and z equals %s" % (x, z))


# ### THE ABOVE IS IDENTICAL TO:  
# def g(x):
#     x = x + 1
#     print ("in scope g(x): x is equal to: %s" % x)

#     def h():
#         x = 'abc'
#         print ("In scope h(), x is equal to: %s" % x)

#     h()
#     return x

# x = 3 
# z = g(x)

# print ("variable z is equal to g(x), where x is %s: and z equals %s" % (x, z))



# def f(x, y):
#    '''
#    x: int or float.
#    y: int or float
#    '''
#    x + y - 2 

# print (f)  # this prints a function


# ###############

# def a(x, y, z):
#     if x:
#         return y
#     else:
#         return z


# def b(q, r):
#     return a(q > r, q, r)

# print (a(False, 2, 3))

# print (b(3, 2))

# print (a(3>2, a, b))  # this will return a function



# ##########

# a = 10
# def f(x):
#     return x + a

# a = 3
# print (f(1))  # this will return 4, since a is overwritten


# x = 12

# def g(x):
#     x = x + 1
#     def h(y):
#         return (x + y)
#     return h(6)


# print (g(x))


def printName(firstName, lastName, reverse):
    if reverse:
        print (lastName + ', ' + firstName)
    else:
        print (firstName, lastName)


printName("Nik", "Daftary", False)
printName("Nik", "Daftary", True)

print("\nYOU CAN ALSO DO THIS")
# printName(firstName = "Nikhil", lastName = "Farenheit", reverse = False)



## YOU CAN ALSO SET A DEFAULT VALUE

def printName(firstName, lastName, reverse = False):
    if reverse:
        print (lastName + ', ' + firstName)
    else:
        print (firstName, lastName)


printName("Nik", "Daftary")



