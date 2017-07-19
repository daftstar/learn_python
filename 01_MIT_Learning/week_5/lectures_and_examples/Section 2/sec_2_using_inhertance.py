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


class MITPerson(Person):
    nextIDNum = 0   # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name)   # initialize Person attribs
        self.idNum = MITPerson.nextIDNum    # MITPerson attribute: unique ID
        MITPerson.nextIDNum += 1

    def getIdNum(self):
        return self.idNum

    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)

    # Sorting MIT People user their ID number, not name
    def __lt__(self, other):
        return self.idNum < other.idNum


m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3, 5, 14, 84)

m2 = MITPerson('Drew Houston')
Person.setBirthday(m2, 3, 4, 83)

m1 = MITPerson('Bill Gates')
Person.setBirthday(m1,10,28,55)

MITPersonList = [m1, m2, m3]

print (m1.speak("wubba lubbba dub dub"))
print()

for person in MITPersonList:
    print (person)

print ()
MITPersonList.sort()

for person in MITPersonList:
    print (person.getIdNum(), " ", person)

p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')
print ()
print ("ID: ", p1.getIdNum())


# p4 < p1 is equivalent to p4.__lt__(p1), which means
# we use the __lt__ method associated with the type of p4,
# namely a Person (the one that compares based on name)

# p1 < p4 is equivalent to p1.__lt__(p4), which means we use
# the __lt__ method associated with the type of p1,
# namely an MITPerson (the one that compares based on IDNum)
# and since p4 is a Person, it does not have an IDNum

print (p1 < p2)     # True
# print (p1 < p4)   # Attribute Error
print (p4 < p1)     # False

