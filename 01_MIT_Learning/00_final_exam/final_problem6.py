#  You are given the following superclass.
# Do not modify this.


class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it.
            I.e., any object occurs 0 times in self. """
        self.vals = {}

    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1

    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s


# Write a class that implements the specifications below.
# Do not override any methods of Container.


class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of
            times it occurs in self by 1.
            Otherwise does nothing.
        """
        if e in self.vals:
            self.vals[e] -= 1
        else:
            pass


    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if e in self.vals:
            return self.vals[e]
        else:
            return 0

    def __add__(self, other):
        """ represents union of e
        from self and other
        """

        # print (self, "\n", other)

        # testing iteration of self
        # for i in self.vals:
        #     print (i)
        #     print (self.count(i))

        # tesing iteration of other
        # for x in other.vals:
        #     print (x)
        #     print (other.count(x))

        # testing matching in self vs. other
        # for x in other.vals:
        #     if x in self.vals:
        #         print ("Huzzzah")
        #     else:
        #         print ("noooo")

        # check each key, value of other to see
        # if exists in self. If it does, add the count of
        # o in other, to the count of o in self.
        # Otherwise, create a new value of o with a
        # count of o from other

        for o in other.vals:
            if o in self.vals:
                self.vals[o] += other.count(o)
            else:
                self.vals[o] = other.count(o)

        return self






"""
FOR EXAMPLE (REMOVE):
    a = Bag()
    a.insert(3)
    a.insert(5)
    b = Bag()
    b.insert(5)
    b.insert(5)
    b.insert(5)
    print(a+b)

PRINTS:
    3:1
    5:4


FOR EXAMPLE (COUNT):
    d1 = Bag()
    d1.insert(4)
    d1.insert(4)
    d1.insert(4)
    print(d1.count(2))
    print(d1.count(4))

PRINTS:
    0
    3


FOR EXAMPLE(ADDITION / MERGE BAGS):
    a = Bag()
    a.insert(4)
    a.insert(3)
    b = Bag()
    b.insert(4)
    print(a+b)

PRINTS:
3:1
4:2


"""

# d1 = Bag()
# d1.insert(4)
# d1.insert(4)
# print(d1)
# d1.remove(2)
# print(d1)


# d1 = Bag()
# d1.insert(4)
# d1.insert(4)
# d1.insert(4)
# print(d1.count(2))
# print(d1.count(4))

# a = Bag()
# a.insert(3)
# a.insert(5)

# b = Bag()
# b.insert(5)
# b.insert(5)
# b.insert(5)

# print(a+b)
