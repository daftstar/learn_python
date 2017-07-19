import datetime


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
        if self.birthday == None:
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

# ##############
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)

p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)

p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)

p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')
personList = [p1, p2, p3, p4, p5]

for e in personList:
    print (e)
print ()
personList.sort()

for e in personList:
    # print (e)
    print (e.getLastName())
