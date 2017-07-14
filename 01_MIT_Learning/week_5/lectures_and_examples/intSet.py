class IntSet(object):
    """ An IntSet is a set of integers """
    # Info about the implementation (not abstraction)
    # Value of the set is represented by a list of ints, self.vals.
    # Each int in the set occurs in self.vals exactly once.

    def __init__(self):
        """ creates an empty set of integers """
        self.vals = []

    def insert(self, e):
        """ assumes e is an integer and inserts e into self """
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """ assumes e is an integer
            Returns True if e is in self, and False otherwise """
        return e in self.vals

    def remove(self, e):
        """ Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self """
        try:
            self.vals.remove(e)
        except:
            print (str(e) + ' is just not found')

    def getMembers(self):
        """ returns a list containing the elements of self.
        Nothing can be assumed about the order of the elements"""
        return self.vals[:] # same as return self.vals

    def __str__(self):
        """ Returns a string representation of self """
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}' # -1 omits trailing comma

s = IntSet()
print (s)
print (type(s))
print ()
s.insert("se")
s.remove("se")
s.insert(3)
print (s.member(3))
s.insert(4)
print (s)