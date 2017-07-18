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
        return "animal:" + str(self.name) + ":" + str(self.age)

myanimal = Animal(3)
print (myanimal)
print ()


print (myanimal.get_age())
print (myanimal.get_name())
# set name without predefine
myanimal.set_name()
print (myanimal.get_name())
myanimal.set_name("bilbo")
print (myanimal.get_name())
print ()
print (myanimal)
print ()





