# class Animal(object):
#     """ Makes animals cute again """
#     # for initializing instance objects

#     is_alive = True
#     def __init__(self, name, age, is_hungry):
#         self.name = name
#         self.age = age
#         self.is_hungry = is_hungry

#         # Note that self is only used in the __init__()
#         # function definition, we don't need to pass it
#         # to our instance objects

#     # When a class has its own functions, those are called methods. 
#     # __init__() is an example of a class method

#     def description(self):
#         print (self.name)
#         print (self.age)


# zebra = Animal("Jeffrey", 2, True)
# giraffe = Animal("Bruce", 1, False)
# panda = Animal("Chad", 7, True)
# hippo = Animal("Hollowey The Hippo", 19, True)

# print (zebra.is_alive)
# print (zebra.name, zebra.age, zebra.is_hungry)
# print (giraffe.name)
# print (panda)

# print (hippo.name)
# print (hippo.age)



class Animal(object):
    """ makes cute animals """
    # Default values
    is_alive = True
    health = "good"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print (self.name)
        print (self.age)


sloth = Animal("Susie", 5)
ocelot = Animal("Oscaar", 23)
hippo = Animal("Funkytown", 19)

print (hippo.health)
print (sloth.health)
print (ocelot.health)


print (hippo.name)
print (hippo.is_alive)

hippo.is_alive = False
print (hippo.is_alive)