
def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; otherwise False
    """
    # alphabetize the string first, so we can use bi-section
    # def sort_string(aStr):
    #     compare = "".join(sorted(aStr))
    #     return compare

    # Base Case: if string length = 0
    if len(aStr) == 0:
        return False

    # Base case, is string length = 1
    if len(aStr) == 1:
        return aStr == char

    # Base case & recursive setup,
    # if char in the middle of the string
    mid_position = len(aStr) // 2
    mid_str_char = aStr[mid_position]

    if char == mid_str_char:
        return True

    # If none of the base cases hold up,
    # test if char is before the next middle character in the
    # first half of aStr

    elif char < mid_str_char:
        return isIn(char, aStr[:mid_position])

    # if the char wasn't located, then check if in top-half
    else:
        return isIn(char, aStr[mid_position + 1:])


print (isIn('s', 'aacfffgkstuww'))