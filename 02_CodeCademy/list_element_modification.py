n = [1, 3, 5]

n[1] = (n[1] * 5)  # replacing the 2nd list value with a calculation
print (n)


"""
APPENDING TO A LIST
"""
n.append(4)
print (n)


"""
REMOVING FROM A LIST
item.pop(index) >> this removes the item at index from the list

item.remove("" or literal) will remove the item if it finds it

del(item[index]) >> similar to .pop, but does not return anything.
"""

n.pop(1)  # removes "15 from index[1]"
print (n)


n.remove(5)
print (n)

del(n[1])
print (n)

