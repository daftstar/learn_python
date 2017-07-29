# Implement a function that meets the specifications below.


def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    no_digits = True
    total = 0

    for i in s:
        if i.isdigit():
            total += int(i)
            no_digits = False

    if no_digits:
        raise ValueError("no digits found")
    else:
        return total


print (sum_digits("1aa23"))
# print (sum_digits("ajjdk"))