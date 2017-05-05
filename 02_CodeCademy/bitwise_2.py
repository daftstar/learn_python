# bitwise AND property &
# The bitwise AND (&) operator compares two numbers on a bit level
# and returns a number where the bits of that number are turned on
# if the corresponding bits of both numbers are 1

print(bin(0b1110 & 0b1101))

# 0b1110
# 0b1101
# ______
# 0b1100


# bitwise OR property
# The bitwise OR (|) operator compares two numbers on a bit level
# and returns a number where the bits of that number are turned on if
# EITHER of the corresponding bits are "1"
print (bin(0b1110 | 0b101))

# 0b1110
#  0b101
# ______
# 0b1111


# bitwise XOR / ^property ("how many unique ON bits are there")
# The XOR (^) or exclusive or operator compares two numbers
# on a bit level and returns a number where the bits of that number
# are turned on if either of the corresponding bits of the two numbers
# are 1, BUT NOT BOTH.


print (bin(0b1110 ^ 0b101))
# 0b1110
#  0b101
# ______
# 0b1011


# bitwise NOT / ~ property
# The bitwise NOT operator (~) flips all of the bits in a single number.
# What this actually means to the computer is very complicated,
# so we're not going to get into it.
# Just know that mathematically, this is equivalent to
# ADDING 1 TO THE NUMBER, AND THEN MAKING IT NEGATIVE

print ((0b1101))
print (bin(~0b1110))
print (~0b1110)

print (" #" + "\n\n\n\n\n\n\n")

print (1)
print ()
print (bin(1))
print (bin(~1))
print (bin(-2))
print (-0b10)
