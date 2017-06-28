# USING RAISE
# Raise an exception when unable to produce a
# result consistent with a function's specifications


# raise<exceptionName>[<arguments>]
# raise ValueError("Something is Wrong")

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


L1 = [1, 3, 5, 9, 16]
L2 = [99, 12, 44, 0, 99]


print (get_ratios(L1, L2))


def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

def avg(grades):
    return (sum(grades) / len(grades))


test_grades = [
    [['peter', 'parker'], [10.0, 5.0, 85.0]],
    [['bruce', 'wayne'], [10.0, 8.0, 74.0]]]
    # [['kippin', 'america'], [8.0, 10.0, 96.0]],
    # [['deadpool'], []]
    # ]

print (get_stats(test_grades))
