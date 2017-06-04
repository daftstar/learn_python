# happy = 0

# if happy > 2:
#     print("hello world")

# Assume that two variables, varA and varB, are assigned values, either numbers or strings.
# Write a piece of Python code that prints out one of the following messages:
# "string involved" if either varA or varB are strings
# "bigger" if varA is larger than varB
# "equal" if varA is equal to varB
# "smaller" if varA is smaller than varB

varA = -22
varB = -2

if type(varA) is str or type(varB) is str:
    print ("string involved")
elif varA > varB:
    print ("bigger")
elif varA == varB:
    print ("equal")
elif varA < varB:
    print ("smaller")

# OR YOU CAN DO THIS: 


varC = 99
varD = 44

if type(varC) == str or type(varD) == str:
    print ("string involved")
elif varC > varD:
    print ('bigger')
elif varC == varD:
    print ('equal')
else:
    print ('smaller')
