import numpy as np
# Images are represented by arrays of numbers, representing location & RGB

n = np.arange(27)
# 1 dimensional array
#
# print (n)
# print (list(n))
two_d =n.reshape(3, 9)
print (two_d)
print ()

three_d =n.reshape(3, 3, 3)
print (three_d)
#

array = [[123, 144, 152, 12, 33],[],[]]
m = np.asarray(array)

print (m)
print (type(array))
print (type(m))
