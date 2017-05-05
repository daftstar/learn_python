"""
Lambdas are very similar to functions, but they are anonymous. 
In other words, you don't have to formally / explicitly 
create a function name. 


Lambdas are useful when you need a quick function 
to do some work for you.

If you plan on creating a function you'll use over and over,
you're better off using def and giving that function a name.

________________________________

lambda x: x % 3 == 0

this is the same as: 

def by_three(x):
    return x % 3 == 0

when passing a lambda to filter(), filter uses the lambda 
to determine what to filter out. 



"""






# sum = lambda x, y : x + y
# print (sum(3, 5))

# # the above is the same as: 

# def sum2(x, y):
#     return x + y

# print(sum2(99, 1))


# the advantage of lambda is when using map() functions

# def fahr(t):
#     return ((float(9)/5) * t + 32)


# def cels(t):
#     return (float(5) / 9) * (t - 32)

# temperatures = (36.5, 37, 37.5, 38, 39)

# f = map(fahr, temperatures)
# c = map(cels, f)

# temperatures_in_fahr = list(map(fahr, temperatures))
# temperatures_in_cels = list(map(cels, temperatures_in_fahr))

# print (temperatures_in_fahr)
# print (temperatures_in_cels)


# my_list = range(0, 16, 2)

# my_list = range(16)

# y = filter(lambda x: x %3 == 0, my_list)

# for i in y:
#     print (i)


# languages = ["HTML", "JavaScript", "Python", "Ruby"]
# print (filter(lambda x: x == "Python", languages)) # Python 2
# print (list(filter(lambda x: x == "Python", languages))) # Python 3


"""
In Python 3, this results in: <filter object at 0x101c4b278>, <-- memory location
In Python 2, this results in ['Python']
In python3, filter, map, zip, etc return an object which is iterable, 
   but not a list. In other words,

   filter(func,data) #python 2.x
   IS EQUIVALENT TO: 
   list(filter(func, data))

"""

# cubes = [x ** 3 for x in range (1, 11)]
# print (cubes)


# x = list(filter(lambda z: z % 3 == 0, cubes))
# print (x)


squares = [x ** 2 for x in range(1, 11)]  # list comprehension

filtered_list = list(filter(lambda a: a in range(29, 71), squares))
print (filtered_list)


garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = (str((filter(lambda x: x != "X", garbled))))
print (str(message))

print (type(message))
