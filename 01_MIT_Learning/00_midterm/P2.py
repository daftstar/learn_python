def new_line():
    return ("\n__________________________\n")


# 2 - 1
L = {'1': 1, '2': 2, "3": 3}

print (L)
print (len(L))
print (new_line())


# 2 - 2
def test(x):
    while x > 0:
        break
        print ("wowowowowo")
    print ("hello")

print (test(15))
print (new_line())


# 2 - 3     - Mutability
a = "hello"       # Not Mutable
b = (1, 2, 4)     # Not Mutable
c = [11, 12, 13]  # MUTABLE

# a[1] = "2"
# b[1] = "2"
c[1] = "2"



