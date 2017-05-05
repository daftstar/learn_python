
lloyd = {
    "name":    "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes":  [88.0, 40.0, 94.0],
    "tests":    [75.0, 90.0]
}


alice = {
    "name":     "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes":  [82.0, 83.0, 91.0],
    "tests":    [89.0, 97.0]
}


tyler = {
    "name":     "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes":  [0.0, 75.0, 78.0],
    "tests":    [100.0, 100.0]
}

"""
to access value of key within dictionary:
# students = [lloyd["name"], alice["name"], tyler["name"]]

to populate a list with the dictionary
students = [lloyd, alice, tyler]

"""

# students = [lloyd, alice, tyler]


# for student in students:
#     print (student["name"])
#     print (student["homework"])
#     print (student["quizzes"])
#     print (student["tests"])


"""
LETS CREATE A WAY TO CALCULATE AVERAGES
"""
homework_weight = .1
quizzes_weight = .3
tests_weight = .6


def average(numbers):
    total = float(sum(numbers))
    return (total / len(numbers))


def get_average(student):
        homework = average(student["homework"]) * homework_weight
        quizzes = average(student["quizzes"]) * quizzes_weight
        tests = average(student["tests"]) * tests_weight
        final_score = homework + quizzes + tests

        return final_score


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


students = [lloyd, alice, tyler]


def get_class_average(students):
    results = []

    for student in students:
        student_average = get_average(student)
        results.append(student_average)

    return average(results)


print (get_class_average(students))
print (get_letter_grade(get_class_average(students)))



