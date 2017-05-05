class Fruit(object):
    """ A class that makes tasty fruits """
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print ("I'm a %s %s and I taste %s" % (self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print ("Yep, I'm edible")
        else:
            print ("Don't eat me. I'm super poisonous")


lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()


""" 
CLASS SYNTAX

Basic class consists of the keyword class, the name of the class
    and the class from which the new class inherits (in parenth)

__init__(argument, ... ) is requred for classes. 
    It's used to initialize the objects it creates. 
    __init__() always takes at least one argument, self. 

Self refers to the object being created. 
    Think of  __init__() as the function that boots up each object
    that the class creates


class NewClassName(object):
    # class magic goies here

"""


class Animal(object):
    # pass   # used as a placeholder for def __init__(self)
    def __init__(self, name):
        self.name = name

zebra = Animal("Jeffrey")
print (zebra.name)





class Square(object):
    def __init__(self):
        self.sides = 4

my_shape = Square()
print (my_shape.sides)
