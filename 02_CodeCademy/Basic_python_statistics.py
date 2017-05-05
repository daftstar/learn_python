
"""
MANUAL AVERAGE
"""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
# grades = [5, 8, 5, 7, 5, 4, 6, 3]


def print_grades(grades):
    for grade in grades:
        print (grade)


def grades_sum(scores):
    total = 0
    for i in scores:
        total += i
    return (total)


def grades_average(grades):
    average = (grades_sum(grades) / float(len(grades)))
    return average


"""
CALCULATING VARIANCE
"""


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0

    for score in scores:
        variance += ((average - score) ** 2)

    total_var = variance / len(scores)
    return (total_var)


"""
CALCULATING STANDARD DEVIATION
"""


def grades_std_deviation(variance):
    return (variance ** .5)


variance = grades_variance(grades)
# print (grades_std_deviation(variance))


print (print_grades(grades))
print ()
print (grades_sum(grades))
print ()
print (grades_average(grades))
print ()
print (grades_variance(grades))
print ()
print (grades_std_deviation(variance))



