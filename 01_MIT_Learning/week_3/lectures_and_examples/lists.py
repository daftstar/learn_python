# unlike tuples, lists are mutable (changed)
# lists, like tuples can have mixed types


listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

print (listA.sort)
print (listA.sort())

print (listA)

print (listA.insert(0, 100))
print (listA)

listA.remove(3)

listA.append(7)



print (listA)
listA + listB
listB.sort()
listB.pop()

print (listB.count('a'))
# listB.remove('a')

listA.extend([4, 1, 6, 3, 4])

print (listA)
print (listA.count(4))
print()
print (listA)
# print (listA.index("apple"))
# print (listA[1])
print (listA.index(1))

listA.pop(4)


print (listA)


print ()
print ()
print () 

# LIST BINDING AND LIST ALIASES
warm = ['red','yellow','orange']
hot = warm
print (hot)
warm[0] = 'blue'
print (hot)
hot[2] = "buuuurrrrrrn"
print (warm)
print (hot)
print (hot == warm)
print ()


# CLONING A LIST
superhot = warm[:]
warm[1] = "hello world"
print ("    warm:", warm)
print ("     hot:", hot)
print ("superhot:", superhot)
print()
print (hot == warm)
print (warm == hot)
print (warm == superhot)
print (hot == superhot)
print ()
print ()



# SORTING LISTS:
# sort() mutates the list, returns nothing
# sorted() does not mutate list, must assign result to variable

warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print ("warm:       ", warm)
print ("sortedwarm: ", sortedwarm)
print()

cool = ['grey', 'blue', 'green']
sortedcool = sorted(cool)
print ("cool:       ", cool)
print ("sortedcool: ", sortedcool)
sortedcool = cool.sort()
print ("sortedcool:", sortedcool)


