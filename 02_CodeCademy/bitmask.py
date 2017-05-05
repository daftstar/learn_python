# num  = 0b1100
# mask = 0b0100
# desired = num & mask

# print (bin(desired))

# if desired > 0:
#     print ("Bit was on")
# else:
#     print ("Bit was off")


def check_bit4(number):
    mask = 0b1000  # 8
    bit_on = number & mask
    # print (bin(bit_on))

    if bit_on > 0:
        return ("on")
    else:
        return ("off")

# print (0b0110)
# print (bin(8))
# print (check_bit4(8))
# print (check_bit4(0b00110))


#  TURNING ON BITS
a =    0b10111011   # 187
mask = 0b00000100   # 1
desired = a | mask  # 0b10111111

# print (bin(desired))

# USING XOR (^) TO FLIP BITS
a    = 0b110  # 6
mask = 0b111  # 7
     # 0b1
desired = a ^ mask #0b1
# print (desired)
# print (bin(desired))


# FLIPPING BITS USING ^
a    = 0b11101110
mask = 0b11111111
       #  0b10001

desired = a ^ mask
print (bin(desired))

print (0b10001)
print (bin(17))

