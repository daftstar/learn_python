def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

print (fancy_divide([0, 2, 4], 0))      # RAISES DIVISION BY ZERO ERROR





def get_ratios(L1, L2):
    """
    Assumes: L1 and L2 are lists of equal length of numbers
    Returns: list containing L1[i] / L2[i]
    """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index] / float(L2[index]))
        except ZeroDivisionError:
            ratios.append('NaN')
        except:
            raise ValueError('get_ratios called with a bad arg')
    return ratios













def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    return item / denom

# print (fancy_divide([0, 2, 4], 0))      # RAISES DIVISION BY ZERO ERROR