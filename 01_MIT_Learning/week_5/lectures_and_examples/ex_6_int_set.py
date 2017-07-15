# Your task is to define the following two methods for the intSet class:

# Define an intersect method that returns a new intSet
# containing elements that appear in both sets.
# In other words, s1.intersect(s2) would return a
# new intSet of integers that appear in both s1 and s2.
# Think carefully - what should happen if s1 and s2
# have no elements in common?


# Add the appropriate method(s) so that len(s) returns
# the number of elements in s.

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []  # vals can be called anything.

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        """takes in two intSet objects
            outputs new intSet object with duplicate values"""
        # create new intSet object placeholder
        same_num = intSet()

        # create new lists
        list1 = self.vals
        list2 = other.vals

        # compare two lists, and insert same vals into
        # same_num intSet
        for val in list1:
            if val in list2:
                same_num.insert(val)
        return same_num

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __len__(self):  # define length method for object
        """Returns length of intSet list object"""
        return len(self.vals)
        # return (9999999)  # debug to test for method call


s1 = intSet()
s1.insert(1)
s1.insert(2)
s1.insert(3)
s1.insert(4)

s2 = intSet()
s2.insert(1)
s2.insert(2)
s2.insert(99)
s2.insert(88)


print (s1.intersect(s2))
print (len(s1))
