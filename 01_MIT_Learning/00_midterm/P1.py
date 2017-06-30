def new_line():
    return ("\n__________________________\n")

# 1 - 1
x = "pi"
y = "pie"
print ("x is:", x)
print ("y is:", y)
print ()

x, y = y, x
print ("x is:", x)
print ("y is:", y)
print (new_line())


# 1 - 2
def f(x):
    while x > 3:    # this will infinite loop based on x
        f(x+1)
    print (x)

print (f(2))    # x > 3 will result in infinite recursive loop
print (new_line())


# 1 - 4
x = 5

def testing(n):
    x = n + 1
    return x


def another(n):
    x = n + 5
    return x


x = (testing(10))
print (x)
x = (another(10))
print (x)

print (new_line())


# 1 - 5
i = -2
j = 5
while i >= 0:
    while j >= 0:
        print(i, j)


# 1 - 7

def f():
    return ("apples")


a = f()
print (a)


# 1 - 9
def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)
        print (type(a))
        print (a)
        print ()
        x = x - 1
    return a
print (f(2))
print (new_line())


# 1 - 10
a = (2, 3, 4, [33, 93, 1])
print (a[3][0])
print (type(a))