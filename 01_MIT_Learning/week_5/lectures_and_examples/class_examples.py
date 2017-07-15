class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)

    def __add__(self, other):   # redefine add method
        numerNew = other.getDenom() * self.getNumer() \
                   + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)

    def __sub__(self, other):   # redefine sub method
        numerNew = other.getDenom() * self.getNumer() \
                   - other.getDenom() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)

    def convert(self):
        return (self.getNumer() / self.getDenom())




oneHalf = fraction(1, 2)
oneThird = fraction(1, 3)
threeQuarters = fraction(3, 4)

print (oneHalf)
print (oneThird)

new = oneHalf + oneThird
print (new)

print (oneThird.convert())