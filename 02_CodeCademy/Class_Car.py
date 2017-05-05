# We also use the word object in parentheses because
# we want our classes to inherit the object class.
# This means that our class has all the properties of an object,
# which is the simplest, most basic class.


# class Car(object):
#     condition = "new"

#     def __init__(self, model, color, mpg):
#         self.model = model
#         self.color = color
#         self.mpg = mpg

#     def display_car(self):
#         print ("This is a %s %s with %s MPG." % (self.color, self.model, self.mpg))

#     def drive_car(self):
#         self.condition = "used"


# class ElectricCar(Car):
#     def __init__(self, model, color, mpg, battery_type):
#         self.battery_type = battery_type
#         self.model = model
#         self.color = color
#         self.mpg = mpg

#     def drive_car(self):
#         self.condition = "like new"


# # my_car = Car("DeLorean", "silver", 88)
# my_car = ElectricCar("Tesla", "White", 150, "molten salt")
# # print (my_car.condition)
# print (my_car.display_car())

# my_car.drive_car()
# print (my_car.condition)


class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return ("(%d, %d, %d)" % (self.x, self.y, self.z))

my_point = Point3D(1, 2, 3)

print (my_point)