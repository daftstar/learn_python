# Packages are directories of python scripts
# Each script is a module
# They specify functions, methods, types

# to install packages, use pip
# pip3 install numpy   # pip3 specifies python 3

# To import entire package: import numpy

# you can import a package and rename as an alias
# e.g. import numpy as np

# to selectively import:
# from numpy import array


# # Definition of radius
# r = 0.43

# # Import the math package
# import math

# # Calculate C
# C = 2 * math.pi * r

# # Calculate A
# A = math.pi * (r ** 2)

# # Build printout
# print("Circumference: " + str(C))
# print("Area: " + str(A))


# SELECTIVE IMPORTING

from math import radians, pi
print (radians)


print (pi)
print (radians)

# Definition of radius
r = 192500

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist

print (dist)