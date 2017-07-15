class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):    # redefine == method
        # returns True if coordinates refer to the same point
        # in the plane - they have the same x and y coordinates
        # planeX = [other.getX(), self.getX()]
        # planeY = [other.getY(), self.getY()]
        groupXa = self.getX()
        groupXb = other.getX()
        groupYa = self.getY()
        groupYb = other.getY()

        if groupXa == groupXb and groupYa == groupYb:
            return True
        else:
            return False

    def __repr__(self):
        # special method that that returns a string that
        # looks like a valid Python expression that can be used
        # to recreate an object with the same value.
        # e.g. eval(repr(c)) == c, given the definition of
        # __eq__
        return ("Coordinate(%i,%i)" %(self.getX(), self.getY()))

# create object called sample, containing coordinates 5, 10
coordOne = Coordinate(5, 10)
coordTwo = Coordinate(5, 5)
coordThree = Coordinate(5, 5)
coordFour = Coordinate(5, 5)


# call getX and getY method on coordOne object
print ("Coordinate X: %s \nCoordinate Y: %s" %(coordOne.getX(), coordOne.getY()))

# use special defined string output function
print (coordOne)

print ()
# call __eq__ method to see if x == y
# print (sample.getX() == sample.getY())

# print (coordTwo == coordOne)
# print (coordTwo == coordOne == coordOne)
print (coordTwo == coordThree)
print (coordTwo == coordThree == coordFour)
print (coordOne)


c1 = Coordinate(1, -8)
c2 = Coordinate(1, -8)

print(c1 == c2)

print (repr(c1))

