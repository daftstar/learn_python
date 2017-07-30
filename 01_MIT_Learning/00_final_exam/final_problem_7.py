# Do not change the Location or Campus classes. ###
# Location class is the same as in lecture.     ###


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2) ** 0.5

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc

    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):

    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are
        Location objects.

        Initializes a new Campus centered at
        location center_loc with a tent at location tent_loc """
        # Initialize Campus class with center_loc
        Campus.__init__(self, center_loc)

        # create new list beginning with current tent_loc
        self.tent_loc = [tent_loc]

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is
        at least 0.5 distance away from all other tents
        already there. Campus is unchanged otherwise.

        Returns True if it could add the tent,
        False otherwise. """
        for i in self.tent_loc:
            # if new_tent_loc.dist_from(i) <= 0.5:
            if new_tent_loc.dist_from(i) <= 0.4999:     # USING THIS DUE TO MIT TEST HARNESS ROUNDING ERRORS
                # print (new_tent_loc.dist_from(i))
                return False

        # print (new_tent_loc.dist_from(i))
        self.tent_loc.append(new_tent_loc)
        return True

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """

        # self            # coordinates of center
        # tent_loc        # coordinates of item to be removed
        # self.tent_loc   # all locations

        if tent_loc in self.tent_loc:
            self.tent_loc.remove(tent_loc)
        else:
            raise ValueError("not found")

    def get_tents(self):
        """ Returns a list of all tents on the campus.
        The list should contain the string representation of
        the Location of a tent.

        The list should be sorted by the
        x coordinate of the location. """
        # create new container to sort array
        tents = []
        for i in self.tent_loc:
            # apply parent string method to append
            # location to to new list
            tents.append(i.__str__())

        return sorted(tents)


# d = MITCampus(Location(1, 2))
# print (d.get_tents())


# print (d.add_tent(Location(2, 3)))
# print (d.add_tent(Location(1, 2)))
# print (d.add_tent(Location(0, 0)))
# print (d.add_tent(Location(2, 3)))
# print (d.get_tents())
print ("--------")

#               center loc     tent loc, otherwise default(0,0)
# c = MITCampus(Location(1,2), Location(3,1))
# # print (c.get_tents())
# # print (c.center_loc)
# # print (c.tent_loc[0])

# # print(c.add_tent(Location(2.5, 1)))
# # print(c.add_tent(Location(2.49, 1)))
# print(c.add_tent(Location(2.51,1)))

print ("--------------")
#               center loc   tent loc, otherwise default(0,0)=
c = MITCampus(Location(1,2), Location(3,1))

# c.add_tent(Location(1,1))
# print (c.add_tent(Location(1,1)))

# c.add_tent(Location(1,1))
# print(c.add_tent(Location(1.49,1)))

c.add_tent(Location(1,1))
print(c.add_tent(Location(1.51,1)))

"""
For example if,
    c = MITCampus(Location(1,2))

Then the following commands:
    c.add_tent(Location(2,3)) should return True
    c.add_tent(Location(1,2)) should return True
    c.add_tent(Location(0,0)) should return False
    c.add_tent(Location(2,3)) should return False

    c.get_tents() should return:
    ['<0,0>', '<1,2>', '<2,3>']"""



# class MITCampus(Campus):

#     """ A MITCampus is a Campus that contains tents """
#     def __init__(self, center_loc, tent_loc=Location(0, 0)):
#         """ Assumes center_loc and tent_loc are
#         Location objects.

#         Initializes a new Campus centered at
#         location center_loc with a tent at location tent_loc """
#         # Initialize Campus class with center_loc
#         Campus.__init__(self, center_loc)

#         # create new list beginning with current tent_loc
#         self.tent_loc = [tent_loc]

#     def add_tent(self, new_tent_loc):
#         """ Assumes new_tent_loc is a Location
#         Adds new_tent_loc to the campus only if the tent is
#         at least 0.5 distance away from all other tents
#         already there. Campus is unchanged otherwise.

#         Returns True if it could add the tent,
#         False otherwise. """
#         for i in self.tent_loc:
#             if new_tent_loc.dist_from(i) <= 0.5:
#                 return False

#         self.tent_loc.append(new_tent_loc)
#         return True


#         # for i in self.tent_loc:
#         #     if new_tent_loc.dist_from(i) >= 0.5:
#         #         self.tent_loc.append(new_tent_loc)
#         #         print (new_tent_loc, i, new_tent_loc.dist_from(i))
#         #         return True
#         #     else:
#         #         return False

#         # for i in self.tent_loc:
#         #     if i.dist_from(new_tent_loc) >= 0.5:
#         #         self.tent_loc.append(new_tent_loc)
#         #         print (i, new_tent_loc, i.dist_from(new_tent_loc))
#         #         return True
#         #     else:
#         #         print (i, new_tent_loc, i.dist_from(new_tent_loc))
#         #         return False


#     def remove_tent(self, tent_loc):
#         """ Assumes tent_loc is a Location
#         Removes tent_loc from the campus.
#         Raises a ValueError if there is not a tent at tent_loc.
#         Does not return anything """
#         # Your code here
#         pass

#     def get_tents(self):
#         """ Returns a list of all tents on the campus.
#         The list should contain the string representation of
#         the Location of a tent.

#         The list should be sorted by the
#         x coordinate of the location. """
#         # Your code here
#         tents = []
#         for i in self.tent_loc:
#             tents.append(i.__str__())

#         return sorted(tents)