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


# PARENT CLASS (Animal)             = superclass
# Child class (Person, Cat, Rabbit) = subclass
#   - inherits all data and behaviors of parent class
#   - add more info and behavior specific to subclass
#   - override behavior
#   - subclasses cannot be used by Super


class Cat(Animal):  # indicated subclass
    """docstring for ClassName"""
    # __init__ is pulled in from Animal superclass
    def speak(self):
        print ("meow")

    def __str__(self):  # override string method
        return "Cat: " + str(self.name) + ": " + str(self.age)


class Rabbit(Animal):
    def speak(self):
        print ("meep")

    def __str__(self):  # override string method
        return "Rabbit: " + str(self.name) + ": " + str(self.age)


class Person(Animal):   # unique subclass behavior
    def __init__(self, name, age):   
        Animal.__init__(self, age)   # call Animal's constructor
        Animal.set_name(self, name)  # call Animal's method
        self.friends = []            # add new data attribute

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print ("hello")

    def age_diff(self, other):   # compare self object to another person object
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print (self.name, "is", diff, "years older than", other.name)
        else:
            print (self.name, "is", -diff, "years younger than", other.name)

    def __str__(self):
        return "Person: " + str(self.name) + ": " + str(self.age)


class Student(Person):  # subclass of Person, sub-sub class of Animal
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print ("i have homework")
        elif 0.25 <= r < 0.5:
            print ("i need sleeeep")
        elif 0.5 <= r < .75:
            print ("I should eat")
        else:
            print ("I am watching TV")

    def __str__(self):
            return "Student: " + str(self.name) + ": " + str(self.age) + ": " + str(self.major)


# Create new cat
jelly = Cat(1)
print (jelly.get_name())
jelly.set_name("jelly belly")
print (jelly)
print()
print (Animal.__str__(jelly))   # use superclass __str__ method vs. cat __str__


# Create new Rabbit
peter = Rabbit(4)
print (peter)
peter.set_name("peter")
print (peter)
print (peter.get_age())
peter.speak()
print ()


# Create new people
nik = Person('Nik', 37)
gavin = Person('Gavin', 34)
nik.speak()
Person.age_diff(nik, gavin)
print (nik.get_name())

nik.age_diff(gavin)
gavin.age_diff(nik)
Person.age_diff(nik, gavin)
print ()


# create new student
funky = Student("funky", 18, "llama doctorology")
print (funky)
funky.speak()
funky.speak()
funky.speak()
funky.speak()




