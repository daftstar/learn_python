import random


class Animal(object):
    def __init__(self, age):    # special method to create instance
        self.age = age          # what gets initalized upon creation
        self.name = None        # data attribute setup, but not initialized

    # create getters to bypass e.g. myanimal.name
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    # create setters to assign values
    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal: " + str(self.name) + ": " + str(self.age)


class Rabbit(Animal):
    # create instance variable when Class Rabbit is created
    # gives IDs to each rabbit
    # class variable
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag       # instance variable
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def speak(self):
        print ("meep")

    def __str__(self):  # override string method
        return "Rabbit: " + str(self.name) + ": age:  " + str(self.age)

    def __add__(self, other):   # returns new rabbit with two parents
        # returning object of same type as this class
        return Rabbit(0, self, other)

    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid

        parents_opposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid

        return parents_same or parents_opposite    # return true if either is True





# Create new Rabbit
peter = Rabbit(2)
peter.set_name("peter")

hopsy = Rabbit(3)
hopsy.set_name("hopsy")

# create new rabbit cotton from parents peter and hopsy
cotton = Rabbit(1, peter, hopsy)
cotton.set_name("cottontail")

# create new rabbit using add function from parents peter and hopsy
mopsy = peter + hopsy
mopsy.set_name("mopsy")
print (mopsy)

print ("\n_____________________\n")

print ("Mopsy Parent 1: ", mopsy.get_parent1())
print ("Mopsy Parent 2: ", mopsy.get_parent2())

print (" peter ID: ", peter.get_rid())
print (" hopsy ID: ", hopsy.get_rid())
print ("cotton ID: ", cotton.get_rid())
print (" mopsy ID: ", mopsy.get_rid())
print ()
print (mopsy == cotton)


