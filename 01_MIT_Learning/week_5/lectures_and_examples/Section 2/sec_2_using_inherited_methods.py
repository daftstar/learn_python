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


m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3, 5, 14, 84)

m2 = MITPerson('Drew Houston')
Person.setBirthday(m2, 3, 4, 83)

m1 = MITPerson('Bill Gates')
Person.setBirthday(m1, 10, 28, 55)

MITPersonList = [m1, m2, m3]

p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')

s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo di Caprio')
s5 = TransferStudent('Robert deNiro')

p1 = Professor("Professor Arrogant", "Computer Science")

print(s1)
print(s1.getClass())
print(s1.speak('where is the quiz?'))
print(s2.speak('I have no clue!'))
print()

student_list = [s1, s2, s3, s4, s5]
for e in student_list:
    print ("%s is a student? %s" % (e, isStudent(e)))
print ()

print (m1.speak('Hi there. '))
print()

print (s1.speak("hi there"))
print()

print (p1.speak("Hi There."))
print (p1.lecture("a string is not an integer"))



