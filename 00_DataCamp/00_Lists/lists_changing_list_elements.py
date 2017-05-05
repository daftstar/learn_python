# lists do not store the actual values, they store memory location of values

x = ["a", "b", "c"]
print (x)

y = x
print (y)

y[1] = "z"
print (y)

print (x)

# COMPARE THE MEMORY LOCATIONS OF THESE LISTS
print (hex(id(x)))
print (hex(id(y)))
# the x list will have a different x value than "b".
# this is because the value stored in memory was changed


# ################


# to avoid this, you need to use the list function.

print ("\n\n")
a = [1, 2, 3]
print (a)

b = list(a)
print (b)
b[1] = "hellooooo"


print ("here's the new list", b)
print ("here's the original list", a)

# COMPARE THE MEMORY LOCATIONS OF THESE LISTS
print (hex(id(a)))
print (hex(id(b)))