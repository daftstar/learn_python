import datetime

"""
Class hierarchy
______________________________________________________

                              Person
                                |
                            MITPerson
                                |
                    _________________________
                    |                        |         
                 Student                 Professor
                    |
    _______________________________
    |               |             |
    UG      TransferStudent     Grad

"""


class Person(object):
    def __init__(self, name):
        """ Create person called name """
        self.name = name
        self.birthday = None

        # assumes space is between first and last name - extract last name
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """ Return last name """
        return self.lastName

    def setBirthday(self, month, day, year):
        """ Sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """ Returns self's current age in days """
        if self.birthday is None:
            raise ValueError("No birthdate set")
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):   # custom less than methond
        """ Returns True if self's name is < other's name, and False otherwise """
        if self.lastName == other.lastName:
            return (self.name < other.name)
        return (self.lastName < other.lastName)

    def __str__(self):
        """ Return self's name """
        return self.name


class MITPerson(Person):
    nextIDNum = 0   # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name)   # initialize Person attribs
        self.idNum = MITPerson.nextIDNum    # MITPerson attribute: unique ID
        MITPerson.nextIDNum += 1

    def getIdNum(self):
        return self.idNum

    def speak(self, utterance):
        return (self.name + " says: " + utterance)

    # Sorting MIT People user their ID number, not name
    def __lt__(self, other):
        return self.idNum < other.idNum


class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak("It is obvious that " + topic)


# create new superclass that covers all students
class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return (MITPerson.speak(self, "Yo Bro, " + utterance))


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)


class Grades(object):
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []      # list of Student objects
        self.grades = {}        # maps idNum -> list of grades
        self.isSorted = True    # true if self.students is sorted

    def addStudent(self, student):
        """
        Assumes: student is of type Student
        Add student to the grade book
        """
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """
        Assumes: grade is a float
        Add grade to the list of grades for a student
        """
        try:
            # index into dict using IdNum; returns list of grades
            # then mutates self.grades with added grade
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError("Student not in grade book")

    def getGrades(self, student):
        """ Return a list of grades for student """
        try:    # return copy of student's grades
            # index into dict using IdNum, then return a copy [:]
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError("Student not in grade book")

    def allStudents(self):
        """ Return a list of students in the grade book """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]



def gradeReport(course):
    """Assumes: course if of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is '
                          + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)

# def gradeReport(course):
#     """ Assumes: course is of type grades """
#     report = []
#     for s in course.allStudents():
#         tot = 0.0
#         numGrades = 0

#         for g in course.getGrades(s):
#             tot += g
#             numGrades += 1

#         try:
#             average = tot / numGrades
#             report.append(str(s) + '\'s mean grade is ' + str(average))

#         except ZeroDivisionError:
#             report.append(str(s) + ' has no grades')

#     return ('\n'.join)


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()

six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)


six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

for e in six00.students:
    print (e)

print()
print(gradeReport(six00))



# for s in six00.allStudents():
#     print (s.getGrades())