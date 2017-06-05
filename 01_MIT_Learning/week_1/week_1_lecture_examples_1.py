"""
    operator precedence
    ()
    **
    *
    /
    + and -
"""

print (6 + 12 - 3)
print (- - 4)
print (10 / 3)
print (10.0 / 3.0)

print ((2 + 3) * 4)
print (2 + 3 * 4)
print (2**3 + 1)

print (2.1 ** 2.0)
print (2.2 * 3.0)


a = 3
a = a + 1.0

print (False or False)
print (not False)
print (3.0 - 1.0 != 5.0 - 3.0)
print (3 > 4 or (2 < 3 and 9 > 10))
print (4 > 5 or 3 < 4 and 9 > 8)
print (not(4 > 3 and 100 > 6))


#
print ("\n______________________________________\n")
#


a = 3
a == 5.0
print (a)
print (3 + 5.0)
print (5 / 2.0)
print (5/2 == 5/2.0)

print (round(2.6))
print (int(2.6))


print (1 == 1.0)

# Cast user input as an integer
# num = int(input("give me a number"))
# print (num)
# print (type(num))


temp = 120
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable") 
else:
   print("Cold")