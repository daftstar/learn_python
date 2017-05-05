# YOU CAN USE << AND >> TO SLIDE MASKS INTO PLACE

a = 0b101
# Tenth bit mask

# mask = (0b1 << 3)  # Shift left 3 bits = 0b1000
# print (bin(mask))
# desired = a ^ mask
# print (bin(desired))
# https://discuss.codecademy.com/t/slip-and-slide/77820

def flip_bit(number, n):
    mask = 0b1 << (n - 1)
    # print (bin(mask))
    result = number ^ mask
    return bin(result)


print (flip_bit(0b111, 2))